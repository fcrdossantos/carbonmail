import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED
from PySimpleGUI.PySimpleGUI import Window

from carbonmail.list_editor import view
from carbonmail.list_editor.manager import (
    create_list,
    delete_list,
    import_contact,
    get_list_contacts,
)
from carbonmail.list_editor.manager import update_lists, create_contact
from carbonmail import email_sender


class List_Editor:
    def __init__(self, email_sender):
        self.window = None
        self.ms = email_sender

    def instantiate(self):
        global window

        if self.window == None:
            self.window = view.get_window()

    def enable_window(self):
        self.instantiate()

        while True:
            event, values = self.window.read()

            if values is not None:
                self.list = values["-Lists-"]

            if event == "-Create-":
                list_name = values["-ListName-"]

                if create_list(list_name):
                    sg.popup("Sua lista foi criada.", title="Sucesso")
                    update_lists(self.window, self.list)
                else:
                    sg.popup("Insira um nome válido.", title="Erro")

            elif event == "-Import-":
                csv_path = values["-CSV-"]

                status_code = import_contact(csv_path, self.list)

                if status_code == -1:
                    sg.popup("Arquivo não encontrado", title="Erro")
                elif status_code == 0:
                    sg.popup(
                        "Os cabeçalhos devem se chamar name e e-mail",
                        title="Erro",
                    )
                else:
                    sg.popup(
                        "Sua lista de contados foi importada",
                        title="Sucesso",
                    )

            elif event == "-Add-":
                name = values["-Name-"]
                email = values["-Email-"]

                if create_contact(name, email, self.list):
                    sg.popup("Seu contato foi criado.", title="Sucesso")
                else:
                    sg.popup("Insira um nome e um e-mail válido.", title="Erro")

            elif event == "-Delete-":
                delete_list(self.list)
                answer = sg.popup(
                    "Isso removerá todos os seus contatos desta lista. Deseja continuar?",
                    title="Cuidado!",
                    custom_text=("Sim", "Não"),
                )

                if answer == "Sim":
                    update_lists(self.window)
                    sg.popup("A lista foi deletada.", title="Sucesso")

            elif event == "-ShowContacts-":
                contacts = "\n".join(
                    [
                        f"{contact[0]} <{contact[1]}>"
                        for contact in get_list_contacts(self.list)
                    ]
                )
                sg.popup_scrolled(
                    f"Contatos da lista: {self.list}",
                    contacts,
                    title="Contatos",
                )

            elif event in (WIN_CLOSED, "-Back-"):
                self.window.close()
                self.window = None
                self.ms.unhide_window()
                break

    def hide_window(self):
        self.instantiate()
        self.window.Hide()

    def unhide_window(self):
        self.instantiate()
        self.window.UnHide()

    def close_window(self):
        self.instantiate()
        self.window.Close()
