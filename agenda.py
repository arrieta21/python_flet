import flet as ft 

def agenda(page: ft.page):
    page.title = "Agenda de contactos"
    page.window_width = 350
    page.window_height = 400
    page.padding = 10
    
    page.appbar = ft.AppBar(
        title= ft.Text("Agenda de contactos"),
        actions=[
            ft.IconButton(
                icon=ft.icons.START,
                icon_color="blue_50",
                icon_size=30,
            ),
            ft.IconButton(
                icon=ft.icons.EXIT_TO_APP,
                icon_color="blue_50",
                icon_size=30,
            ),
            ft.PopupMenuButton(
            items = [
                ft.PopupMenuItem(text= "Ayuda"),
                ft.PopupMenuItem(text= "Acerca de mi"),
            ]
        )
        ]
    )
    
    texto_registro = ft.Text("Nuevo Registro", size= 17)
    
    Contenedor_nombre = ft.Container (
        content = ft.Text("Nombre", size = 12, color=ft.colors.BLACK),
        bgcolor = '#D4AC0D',
        padding=5,
        width=100,
        height=35,
        border_radius=10,
    )
    
    Contenedor_numero = ft.Container (
        content = ft.Text("Numero", size = 12, color=ft.colors.BLACK),
        bgcolor = '#D4AC0D',
        padding=5,
        width=100,
        height=35,
        border_radius=10,
    )
    
    Contenedor_correo = ft.Container (
        content = ft.Text("Correo", size = 12, color=ft.colors.BLACK),
        bgcolor = '#D4AC0D',
        padding=5,
        width=100,
        height=35,
        border_radius=10,
    )
    
    cuadro_nombre = ft.Container(
        content = ft.TextField(color=ft.colors.BLACK),
        bgcolor = '#EC7063',
        padding = 5,
        width = 150,
        height = 35,
        border_radius = 10
    )
    
    cuadro_numero = ft.Container(
        content = ft.TextField(color=ft.colors.BLACK),
        bgcolor = '#EC7063',
        padding = 5,
        width = 150,
        height = 35,
        border_radius = 10
    )
    
    cuadro_correo = ft.Container(
        content = ft.TextField(color=ft.colors.BLACK),
        bgcolor = '#EC7063',
        padding = 5,
        width = 150,
        height = 35,
        border_radius = 10
    )
    
    fila1 = ft.Row(
        [
            Contenedor_nombre,
            cuadro_nombre,
                ft.IconButton(
                icon=ft.icons.ADD,
                icon_color="blue_50",
                icon_size=30,
                )
        ]
    )
    
    fila2 = ft.Row(
        [
        Contenedor_numero,
        cuadro_numero,
        ft.IconButton(
            icon=ft.icons.UPDATE,
            icon_color="blue_50",
            icon_size=30,
        )
        ]
    )
    
    fila3 =ft.Row(
        [
            Contenedor_correo,
            cuadro_correo,
            ft.IconButton(
                icon=ft.icons.DELETE_OUTLINE,
                icon_color="blue_50",
                icon_size=30,
            )
        ]
    )
    
    buscar=ft.Text("Buscar", size= 17)
    
    fila5 = ft.Row(
        [
            Contenedor_nombre,
            cuadro_nombre,
            ft.IconButton(
                icon=ft.icons.SEARCH,
                icon_color="blue_50",
                icon_size=30,
                )
        ]
    )
    
    page.update()
    page.add(
        texto_registro,
        fila1,
        fila2,
        fila3,
        buscar,
        fila5
        )
    
ft.app(target=agenda)
