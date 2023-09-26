import flet as ft 

def registro(page: ft.page):
    page.title = "Registro nuevo usuario"
    page.bgcolor = '#21618C'
    page.window_width = 1170
    page.window_height = 600
    page.padding = 20
    
    texto_titulo = ft.Text("Nuevo registro", size = 25)
    texto_datospersonales = ft.Text("Datos personales", size = 35, weight=ft.FontWeight.W_900, selectable=True)
    
    Contenedor_nombre = ft.Container (
        content = ft.Text("Nombre", size = 15),
        bgcolor = '#D4AC0D',
        padding=5,
        width=550,
        height=50,
        border_radius=10,
    )
    cuadro_nombre = ft.Container(
        content = ft.TextField(),
        bgcolor = '#EC7063',
        padding = 5,
        width = 550,
        height = 50,
        border_radius = 10
    )
    
    Contenedor_apellido = ft.Container (
        content= ft.Text("Apellido", size = 15),
        bgcolor = '#D4AC0D',
        padding=5,
        width=550,
        height=50,
        border_radius=10,
    )
    cuadro_apellido =ft.Container(
        content = ft.TextField(),
        bgcolor = '#EC7063',
        padding = 5,
        width = 550,
        height = 50,
        border_radius = 10
    )
    
    Contenedor_email = ft.Container (
        content= ft.Text("e mail", size = 15),
        bgcolor = '#D4AC0D',
        padding=5,
        width=550,
        height=50,
        border_radius=10,
    )
    cuadro_email = ft.Container(
        content = ft.TextField(),
        bgcolor = '#EC7063',
        padding = 5,
        width = 550,
        height = 50,
        border_radius = 10
    )
    
    Contenedor_direccion = ft.Container (
        content= ft.Text("Direccion", size = 15),
        bgcolor = '#D4AC0D',
        padding=5,
        width= 1100,
        height=50,
        border_radius=10,
    )
    cuadro_direccion = ft.Container(
        content = ft.TextField(),
        bgcolor = '#EC7063',
        padding = 5,
        width = 1100,
        height = 50,
        border_radius = 10
    )
    
    Contenedor_telefono = ft.Container (
        content = ft.Text("telefono", size = 15),
        bgcolor = '#D4AC0D',
        padding=5,
        width=550,
        height=50,
        border_radius=10,
    )
    cuadro_telefono = ft.Container(
        content = ft.TextField(),
        bgcolor = '#EC7063',
        padding = 5,
        width = 550,
        height = 50,
        border_radius = 10
    )
    
    boton = ft.Container(
        content = ft.ElevatedButton(text="Registrar"),
        alignment=ft.alignment.center
    )
    
    fila_1 = ft.Row([
        Contenedor_nombre,
        Contenedor_apellido
    ])
    
    fila_2 = ft.Row ([
        cuadro_nombre,
        cuadro_apellido
    ])
    
    fila_3 = ft.Row ([
        Contenedor_email,
        Contenedor_telefono
    ])
    
    fila_4 = ft.Row ([
        cuadro_email,
        cuadro_telefono
    ])
    
    fila_5  = ft.Row([
        boton],
        alignment=ft.MainAxisAlignment.CENTER
    )
    
    page.update()
    page.add(
        texto_titulo,
        texto_datospersonales,
        fila_1,
        fila_2,
        fila_3,
        fila_4,
        Contenedor_direccion,
        cuadro_direccion,
        fila_5
    )
    
ft.app(target=registro)