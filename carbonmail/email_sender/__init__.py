from carbonmail.email_sender.manager import validate_email_sending
from carbonmail.list_editor.manager import load_lists, update_lists
from carbonmail.list_editor.manager import initialize as initialize_list_editor
import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED

from carbonmail.email_sender import view
from carbonmail import list_editor


class Email_Sender:
    def __init__(self):
        self.window = None

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

            if event == "-Send-":
                title = values["-Title-"]
                content = values["-Content-"]
                code_path = values["-Code-"]
                status_code = validate_email_sending(
                    self.window, code_path, title, content, self.list
                )

                if status_code == -2:
                    sg.popup("Arquivo (código) não encontrado.", title="Erro")
                elif status_code == -1:
                    sg.popup("Título ou Corpo inválido.", title="Erro")
                elif status_code == 0:
                    sg.popup("Lista sem contatos válidos.", title="Erro")
                else:
                    sg.popup(
                        "Os e-mails estão sendo enviados, aguarde.",
                        title="Sucesso",
                        non_blocking=True
                    )

            elif event == "-ListManager-":
                self.window.Hide()
                initialize_list_editor(self)

            elif event == WIN_CLOSED:
                self.window.close()
                break

            elif event == "-Thread-":
                sg.popup(
                    "Todos os e-mails foram enviados.",
                    title="Sucesso",
                )

    def hide_window(self):
        self.instantiate()
        self.window.Hide()

    def unhide_window(self):
        update_lists(self.window, self.list)

        self.instantiate()
        self.window.UnHide()

    def close_window(self):
        self.instantiate()
        self.window.Close()
