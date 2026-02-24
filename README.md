# 📘 Unidad 1: Ingeniería de Interfaces de Usuario (GUI)

# 🚀 Tópicos Avanzados de Programación

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flet](https://img.shields.io/badge/flet-D1345B?style=for-the-badge&logo=google-chrome&logoColor=white)
![VS Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

### 🎨 De Líneas de Comando a Píxeles Perfectos

Bienvenido al repositorio de **Tópicos Avanzados de Programación**. Aquí el código cobra vida y forma. En esta primera unidad, exploramos el ecosistema de **Flet (v0.80.5)** para transformar simples scripts de Python en interfaces potentes.

---

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 🐍
* **Framework:** Flet (Entorno de desarrollo ágil para GUIs)
* **Entorno:** Visual Studio Code + Virtual Environments (`.venv`)
* **Control de Versiones:** Git & GitHub

### 1.1 Creación de Interfaz Gráfica para Usuarios 🏗️

La creación de una GUI consiste en diseñar el entorno visual a través del cual el usuario interactúa con el software. En el desarrollo moderno, esto se basa en Layouts (estructuras de acomodo).

Contenedores (Container): Son la base del diseño. Permiten agrupar elementos, aplicar bordes, colores de fondo, sombras y redondeado (border_radius).
Columnas y Filas (Column / Row): Organizan los elementos de forma vertical u horizontal. Son esenciales para lograr una interfaz responsiva.

Alineación: Se controla mediante propiedades como horizontal_alignment y vertical_alignment para centrar o distribuir los componentes en la pantalla.
* **Paradigma de Diseño Declarativo:** A diferencia del modelo imperativo (donde se instruye cómo dibujar cada píxel), en este proyecto se utiliza el enfoque declarativo.
* Se define el **Estado Deseado** de la interfaz y el framework se encarga del renderizado optimizado.
* **Arquitectura de Contenedores (Layout Engine):** * **Composición sobre Herencia:** La interfaz se construye mediante la composición de objetos. Un `ft.Container` no es solo un
* cuadro; es un objeto con propiedades de **Modelo de Caja (Box Model)** que gestiona `padding`, `margin`, y `alignment`.
    * **Sistemas de Coordenadas Flexibles:** Se implementan `Row` (Eje Horizontal) y `Column` (Eje Vertical) para crear layouts responsivos. Esto permite que componentes como los
    * botones de la **Calculadora** mantengan proporciones áureas independientemente de la resolución del dispositivo.
<img width="265" height="190" alt="image" src="https://github.com/user-attachments/assets/b473eb6e-8493-4772-a721-e09c255c2b80" />


### 1.2 Tipos de Eventos ⚡

Un evento es una acción que ocurre en el sistema y a la cual el programa puede responder. En programación avanzada, los eventos se clasifican según su origen:

Eventos de Ratón: Clics (on_click), pasar el cursor por encima (on_hover) o arrastrar.
Eventos de Teclado: Presionar una tecla específica o enviar un formulario con la tecla Enter (on_submit).
Eventos de Cambio: Se disparan cuando el contenido de un componente se modifica, como escribir en un cuadro de texto (on_change) o seleccionar una opción en un menú.
Eventos de Sesión: Ocurren cuando un usuario entra o sale de la aplicación (como lo que manejamos en el Chat).

En programación avanzada, un evento es un mensaje asíncrono enviado por el Sistema Operativo hacia el **Event Loop** de la aplicación. Los clasificamos técnicamente como:

* **Eventos de Dispositivo de Entrada (HCI):** * **Basados en Puntero:** `on_click`, `on_hover`. Manejan la posición (x, y) y el estado del periférico.
    * **Basados en Teclado:** `on_submit`. Permiten la captura de buffers de texto de forma eficiente (aplicado en la **App de Chat**).
* **Eventos de Estado y Cambio:** El evento `on_change` es crítico para la validación reactiva; permite interceptar el flujo de datos en el instante en que el usuario modifica un componente.
* **Eventos de Sesión y Protocolo:** En entornos multiusuario, manejamos eventos de entrada/salida de sesión, fundamentales para la gestión de sockets y concurrencia.

<img width="265" height="190" alt="image" src="https://github.com/user-attachments/assets/5d0e867e-b0ad-4dc8-9610-f1bbd1245265" />


### 1.3 Manejo de Eventos (Event Handling) ⚙️
El manejo de eventos (Event Handling) es la lógica que se ejecuta cuando ocurre un evento. Se basa en tres pilares:

Event Source (Fuente): El componente que genera el evento (un Botón, por ejemplo).
Event Listener (Escuchador): La propiedad del componente que está atenta a la acción (ej: on_click).
Event Handler (Manejador): La función de Python que se ejecuta. En Flet, estas funciones suelen recibir un argumento e (el evento) que contiene información extra.

Ejemplo: def mi_funcion(e): print("Botón presionado")
* **Pilares del Manejo:**
    1. **Fuente (Source):** El componente que emite la señal.
    2. **Callback (Handler):** La función de orden superior que se suscribe al evento.
    3. **Objeto de Evento (`e`):** Una estructura de datos que encapsula información contextual (ID del control, timestamp, coordenadas, valores).
* **Flujo Lógico:** Cuando ocurre un clic en el **Formulario de Registro**, el manejador detiene el flujo normal para ejecutar la **Lógica de Validación** (Regex), asegurando la
* integridad de la información antes de permitir la persistencia de datos.



### 1.4 Manejo de Componentes Gráficos de Control 🛠️
Los componentes de control son objetos visuales que permiten al usuario introducir datos o tomar decisiones. En nuestro trabajo hemos dominado los siguientes:

TextField: Para entrada de texto. Incluye validaciones mediante la propiedad error_text.
Dropdown: Menú desplegable para seleccionar una opción de una lista predefinida (ej: Carreras).
RadioGroup: Conjunto de botones de opción donde solo se puede seleccionar uno a la vez (ej: Género).

Button: El disparador principal de acciones. Puede contener texto, iconos y estilos personalizados.
* **Controles de Entrada Primaria (`TextField`):** Gestionan el buffer de entrada. Poseen propiedades de validación como `error_text` para reducir la carga cognitiva del usuario.
* **Controles de Selección Restringida (`Dropdown` / `RadioGroup`):** Implementan lógica de selección única para evitar estados inválidos en el sistema (ej. selección de carrera o género).
* **Controles de Retroalimentación Activa:**
    * **`SnackBar`:** Notificaciones asíncronas de bajo impacto visual.
    * **`AlertDialog`:** Interrupciones modales de alto impacto para decisiones críticas.
* **Controles Dinámicos (`ListView`):** Componentes especializados en la gestión eficiente de memoria para renderizar grandes colecciones de datos, utilizando técnicas de reciclaje de
* celdas (visto en el **Chat**).

---

## 📂 Análisis de Casos Prácticos
| Proyecto | Teoría Aplicada | Componentes Clave |
| :--- | :--- | :--- |
| **Calculadora** | Layouts complejos y jerarquía de contenedores. | `Container`, `Row`, `Text` |
| **App de Chat** | Comunicación asíncrona y eventos de sesión. | `ListView`, `TextField`, `PubSub` |
| **Formulario** | Validación de datos y manejo de errores (UX). | `Dropdown`, `RadioGroup`, `SnackBar` |

---

## 🚀 Guía de Despliegue (Git Bash)
Para replicar el entorno de investigación y ejecución:

```bash
# 1. Preparación del Entorno Virtual (Aislamiento de dependencias)
python -m venv venv
source venv/Scripts/activate

# 2. Instalación del motor de la GUI
pip install flet

# 3. Ejecución en modo desarrollo (Hot Reload)
flet run main.py
