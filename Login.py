import flet as ft

def main(page: ft.Page):
    #titulo de la ventana 
    page.title = "Inicio de sesion"
    #tamaño de la ventana 
    page.window_height = 600
    page.window_width = 400
    # Primer contenedor con texto centrado
    contenedor_texto = ft.Container(
        content=ft.Text("Bienvenido", size=24),
        alignment=ft.alignment.center
    )

    # Segundo contenedor con otro contenido
    contenedor_otro = ft.Container(
        content=ft.Text("USUARIO", size=20),
        alignment=ft.alignment.center
    )
    # Cuadro para que el usuario ponga su nombre
    cuadro_usiario = ft.Container(
        content= ft.TextField(label ="escribe el nombre de usuario"),
        alignment=ft.alignment.center
    )
    # Contenedor para el texto contraseña
    contenedor_contraseña = ft.Container(
        content=ft.Text("CONTRASEÑA", size=20),
        alignment=ft.alignment.center
    )
    # Cuadro para que el usuario ponga su contraseña 
    cuadro_contraseña = ft.Container(
        content= ft.TextField(label ="escribe la contraseña", password=True, can_reveal_password=True),
        alignment=ft.alignment.center
    )
     #Boton 
    buton = ft.Container(
        ft.ElevatedButton(text="Entrar"),
        alignment= ft.alignment.center
    )
    

    # Crea una columna que contiene los contenedores
    columna = ft.Column([contenedor_texto, contenedor_otro, cuadro_usiario, contenedor_contraseña, cuadro_contraseña, buton], alignment=ft.MainAxisAlignment.CENTER)

    # Agrega la columna a la página
    page.add(columna)

ft.app(target=main)
