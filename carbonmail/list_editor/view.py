from carbonmail.utils import innerElementSpacer
import PySimpleGUI as sg
from carbonmail.list_editor.manager import load_lists


def get_layout():

    lists = load_lists()

    frame_list = [
        innerElementSpacer(590),
        [
            sg.Text("Selecione a lista:"),
            sg.Combo(lists, default_value=lists[0], key="-Lists-"),
        ],
        [
            sg.Text("Criar uma lista:"),
            sg.InputText(key="-ListName-"),
            sg.Button("Criar", key="-Create-", size=(10, 1)),
        ],
        [
            sg.Button(
                "Deletar Lista",
                key="-Delete-",
                pad=(5, (7, 0)),
                size=(15, 1),
            ),
            sg.Button(
                "Mostrar contatos",
                key="-ShowContacts-",
                pad=(5, (7, 0)),
                size=(15, 1),
            ),
        ],
        innerElementSpacer(590),
    ]

    frame_import = [
        innerElementSpacer(590),
        [
            sg.Text(
                "Selecione o arquivo (CSV):",
                tooltip="Cabeçalhos: name e email",
            ),
            sg.In(key="-CSV-"),
            sg.FileBrowse(
                "Selecionar",
                file_types=(("CSV", "*.csv"),),
                size=(10, 1),
                tooltip="Cabeçalhos: name e email",
            ),
        ],
        [
            sg.Button(
                "Importar arquivos",
                key="-Import-",
                pad=(0, (7, 0)),
                size=(15, 1),
            ),
        ],
        innerElementSpacer(590),
    ]

    frame_add = [
        innerElementSpacer(590),
        [
            sg.Text("Insira o nome: "),
            sg.InputText(key="-Name-"),
        ],
        [
            sg.Text("Insira o e-mail:"),
            sg.InputText(key="-Email-"),
        ],
        [
            sg.Button(
                "Adicionar",
                key="-Add-",
                pad=(0, (7, 0)),
                size=(15, 1),
            ),
        ],
        innerElementSpacer(590),
    ]

    layout = [
        [
            sg.Frame(
                "Configurações da Lista",
                frame_list,
                element_justification="c",
            )
        ],
        [
            sg.Frame(
                "Importação em Lote",
                frame_import,
                element_justification="c",
            )
        ],
        [
            sg.Frame(
                "Adição de Usuário",
                frame_add,
                element_justification="c",
            )
        ],
        [
            sg.Button(
                "Voltar",
                key="-Back-",
                pad=(0, (7, 0)),
                size=(15, 1),
            )
        ],
        innerElementSpacer(590),
    ]
    return layout


def get_window():
    sg.theme("DarkBlue14")
    return sg.Window(
        "Gerenciador de Listas",
        get_layout(),
        element_justification="c",
    )
