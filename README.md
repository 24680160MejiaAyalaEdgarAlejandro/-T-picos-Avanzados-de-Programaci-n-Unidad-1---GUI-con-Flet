Para el desarrollo de estos proyectos se utilizaron las siguientes herramientas. Haz clic en las insignias para ir a los sitios de descarga oficial:

[![Python 3.12+](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Flet 0.21+](https://img.shields.io/badge/Flet-0.21+-0052FF?style=for-the-badge&logo=flutter&logoColor=white)](https://flet.dev/docs/install/)
[![Git Bash-](https://img.shields.io/badge/Git_Bash-v2.44-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/downloads)
[![Visual Studio Code](https://img.shields.io/badge/VS_Code-1.87+-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)

### 1.1 Creación de Interfaz Gráfica para Usuarios 🏗️

La creación de una GUI trasciende el diseño visual; es la implementación de una capa de abstracción entre la lógica del negocio y el usuario final. 

* **Paradigma de Diseño Declarativo:** A diferencia del modelo imperativo (donde se instruye cómo dibujar cada píxel), en este proyecto se utiliza el enfoque declarativo.
* Se define el **Estado Deseado** de la interfaz y el framework se encarga del renderizado optimizado.
* **Arquitectura de Contenedores (Layout Engine):** * **Composición sobre Herencia:** La interfaz se construye mediante la composición de objetos. Un `ft.Container` no es solo un
* cuadro; es un objeto con propiedades de **Modelo de Caja (Box Model)** que gestiona `padding`, `margin`, y `alignment`.
    * **Sistemas de Coordenadas Flexibles:** Se implementan `Row` (Eje Horizontal) y `Column` (Eje Vertical) para crear layouts responsivos. Esto permite que componentes como los
    * botones de la **Calculadora** mantengan proporciones áureas independientemente de la resolución del dispositivo.



### 1.2 Tipos de Eventos ⚡
En programación avanzada, un evento es un mensaje asíncrono enviado por el Sistema Operativo hacia el **Event Loop** de la aplicación. Los clasificamos técnicamente como:

* **Eventos de Dispositivo de Entrada (HCI):** * **Basados en Puntero:** `on_click`, `on_hover`. Manejan la posición (x, y) y el estado del periférico.
    * **Basados en Teclado:** `on_submit`. Permiten la captura de buffers de texto de forma eficiente (aplicado en la **App de Chat**).
* **Eventos de Estado y Cambio:** El evento `on_change` es crítico para la validación reactiva; permite interceptar el flujo de datos en el instante en que el usuario modifica un componente.
* **Eventos de Sesión y Protocolo:** En entornos multiusuario, manejamos eventos de entrada/salida de sesión, fundamentales para la gestión de sockets y concurrencia.

### 1.3 Manejo de Eventos (Event Handling) ⚙️
El manejo de eventos se basa en el **Patrón de Diseño Observer**. La aplicación se mantiene en un estado de "espera activa" hasta que una fuente genera un estímulo.

* **Pilares del Manejo:**
    1. **Fuente (Source):** El componente que emite la señal.
    2. **Callback (Handler):** La función de orden superior que se suscribe al evento.
    3. **Objeto de Evento (`e`):** Una estructura de datos que encapsula información contextual (ID del control, timestamp, coordenadas, valores).
* **Flujo Lógico:** Cuando ocurre un clic en el **Formulario de Registro**, el manejador detiene el flujo normal para ejecutar la **Lógica de Validación** (Regex), asegurando la
* integridad de la información antes de permitir la persistencia de datos.



### 1.4 Manejo de Componentes Gráficos de Control 🛠️
Los componentes de control son la unidad mínima de interacción. Según la ingeniería de software, estos deben poseer **Encapsulamiento** y **Baja Cohesión**.

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
