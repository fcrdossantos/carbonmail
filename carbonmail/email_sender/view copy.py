import PySimpleGUI as sg

listas = ["Lista Alunos", "Lista Administração"]


def get_layout():
    layout = [
        [
            sg.Text("Selecione o Código"),
            sg.In(),
            sg.FileBrowse("Selecionar", file_types=(("Python", "*.py"),)),
        ],
        [
            sg.Text("Selecione a lista de destinatário:"),
            sg.Combo(listas, default_value=listas[0]),
        ],
        [
            sg.Text("Insira o Título:"),
            sg.InputText(key="-Title-"),
        ],
        [
            sg.Text("Insira o Corpo do E-mail:"),
            sg.MLine(key="-Message-", size=(45, 20)),
        ],
        [
            sg.Button("Enviar", key="-Send-"),
            sg.Button("Gerenciar Lista", key="-ListManager-"),
        ],
    ]
    return layout


def get_window():
    return sg.Window("Enviador de E-mail", get_layout(), finalize=True)
