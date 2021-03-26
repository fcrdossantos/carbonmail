from carbonmail.utils import innerElementSpacer
from carbonmail.list_editor.manager import load_lists
import PySimpleGUI as sg

listas = ["Lista Alunos", "Lista Administração"]


def get_layout():

    lists = load_lists()

    frame_campaign = [
        innerElementSpacer(500),
        [
            sg.Text("Selecione o código:"),
            sg.In(size=(35, 1), key="-Code-"),
            sg.FileBrowse(
                "Selecionar",
                file_types=(("Python", "*.py"),),
                size=(10, 1),
            ),
        ],
        [
            sg.Text("Selecione a lista de destinatário:", pad=(0, (7, 0))),
            sg.Combo(
                lists,
                default_value=lists[0],
                pad=(10, (7, 0)),
                key="-Lists-",
            ),
        ],
        innerElementSpacer(500),
    ]

    frame_email = [
        innerElementSpacer(500),
        [sg.Text("Insira o título", font=("Helvetica 15"))],
        [sg.InputText(key="-Title-", size=(62, 1))],
        [sg.Text("Insira o corpo do e-mail", font=("Helvetica 15"))],
        [
            sg.MLine(
                key="-Content-",
                size=(60, 10),
                pad=(0, (0, 10)),
            )
        ],
        innerElementSpacer(500),
    ]

    layout = [
        [
            sg.Frame(
                "Configurações da Camapanha",
                frame_campaign,
                element_justification="c",
            )
        ],
        [
            sg.Frame(
                "Configurações do E-mail",
                frame_email,
                element_justification="c",
            )
        ],
        [
            sg.Button(
                "Enviar E-mail",
                key="-Send-",
                size=(15, 1),
                pad=(10, (10, 0)),
            ),
            sg.Button(
                "Gerenciar Lista",
                key="-ListManager-",
                size=(15, 1),
                pad=(10, (10, 0)),
            ),
        ],
        innerElementSpacer(500),
    ]
    return layout


def get_window():
    sg.theme("DarkBlue14")
    return sg.Window(
        "Enviador de E-mail",
        get_layout(),
        element_justification="c",
    )
