import flet as ft

def main(page: ft.Page):
    page.title = "Registro de Estudiantes - Diseño Pro"
    page.bgcolor = "#FDFBE3" 
    page.padding = 40
    page.theme_mode = ft.ThemeMode.LIGHT
    
    page.window_width = 650
    page.window_height = 750
    page.window_resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- CONTROLES DE ENTRADA ---
    txt_nombre = ft.TextField(label="Nombre Completo", border_color="#4D2A32", border_width=2)
    txt_control = ft.TextField(label="Número de Control", border_color="#4D2A32", border_width=2)
    txt_email = ft.TextField(label="Email Institucional", border_color="#4D2A32", border_width=2)

    dd_carrera = ft.Dropdown(
        label="Carrera",
        expand=True,
        border_color="#4D2A32",
        border_width=2,
        options=[
            ft.dropdown.Option("Ingeniería en Sistemas"),
            ft.dropdown.Option("Ingeniería Civil"),
            ft.dropdown.Option("Ingeniería Industrial"),
            ft.dropdown.Option("Ingeniería en Mecatrónica"),
            ft.dropdown.Option("Ingeniería Gestión Empresarial"),
            ft.dropdown.Option("Contador Público"),
        ]
    )

    dd_semestre = ft.Dropdown(
        label="Semestre",
        width=140,
        border_color="#4D2A32",
        border_width=2,
        options=[ft.dropdown.Option(str(i)) for i in range(1, 9)]
    )
    
    rg_genero = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="masculino", label="Masculino", fill_color="#4D2A32"),
            ft.Radio(value="femenino", label="Femenino", fill_color="#4D2A32"),
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

    def limpiar_formulario(e):
        txt_nombre.value = ""
        txt_control.value = ""
        txt_email.value = ""
        dd_carrera.value = None
        dd_semestre.value = None
        rg_genero.value = None
        page.update()

    btn_enviar = ft.Button(
        content=ft.Text("REGISTRAR ALUMNO", color="white", size=16, weight="bold"),
        bgcolor="#4D2A32",
        height=50,
        on_click=limpiar_formulario,
    )

    # --- CONSTRUCCIÓN DEL FORMULARIO ---
    formulario = ft.Container(
        content=ft.Column([
            ft.Text("👤", size=40), 
            ft.Text("REGISTRO ESCOLAR", size=24, weight="bold", color="#4D2A32"),
            ft.Divider(color="#4D2A32", height=10),
            
            txt_nombre,
            txt_control,
            txt_email,
            
            ft.Row([dd_carrera, dd_semestre], spacing=10),
            
            ft.Column([
                ft.Text("Género:", color="#4D2A32", weight="bold"),
                rg_genero,
            ], spacing=5, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            
            ft.Divider(height=10, color="transparent"),
            btn_enviar
        ], spacing=20, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        
        bgcolor="white",
        padding=30,
        border_radius=25,
        # CORRECCIÓN DE BORDER: Usamos Border para evitar el DeprecationWarning
        border=ft.Border(
            top=ft.BorderSide(2, "#4D2A32"),
            bottom=ft.BorderSide(2, "#4D2A32"),
            left=ft.BorderSide(2, "#4D2A32"),
            right=ft.BorderSide(2, "#4D2A32")
        ),
        # CORRECCIÓN DE COLORS: Usamos Colors con Mayúscula
        shadow=ft.BoxShadow(
            blur_radius=15,
            color=ft.Colors.with_opacity(0.2, "black"),
            offset=ft.Offset(0, 10)
        ),
        width=500,
    )

    page.add(formulario)

ft.run(main)