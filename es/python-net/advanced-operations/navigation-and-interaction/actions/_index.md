---
title: Trabajar con Acciones PDF en Python
linktitle: Acciones
type: docs
weight: 20
url: /es/python-net/actions/
description: Aprende cómo agregar, actualizar y eliminar acciones de documento, página y formulario en archivos PDF utilizando Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Agrega acciones de documento, página y formulario a archivos PDF en Python
Abstract: Este artículo explora cómo trabajar con acciones en documentos PDF utilizando la biblioteca Aspose.PDF, cubriendo interacciones a nivel de documento, de página y de formulario. Las acciones PDF son disparadores predefinidos o personalizables que responden a eventos del usuario, habilitando la navegación, la ejecución de JavaScript, la reproducción multimedia, el envío de formularios y más. La guía muestra cómo agregar, personalizar y eliminar acciones, como abrir URL en eventos del documento, crear navegación o efectos de zoom específicos de la página, agregar botones interactivos para imprimir y navegar, ocultar elementos de formulario de forma dinámica y enviar datos de formulario a puntos finales web. A través de ejemplos de código Python detallados, los lectores aprenden a mejorar la interactividad de los PDF, optimizar flujos de trabajo e integrar los PDF con sistemas externos mientras comprenden consideraciones de compatibilidad del visor.
---

Las acciones en un PDF son tareas predefinidas que se activan mediante la interacción del usuario o eventos del documento. Se pueden usar para:

- Navega a una página específica o archivo externo
- Abrir un enlace web
- Reproducir contenido multimedia
- Ejecutar JavaScript
- Enviar o restablecer un formulario
- Mostrar/ocultar campos
- Cambiar nivel de zoom o modo de vista

Casi todas las acciones utilizan parámetros incorporados, pero hay algunas que pueden personalizarse. Por ejemplo - Acciones de JavaScript.

## Agregar acciones de lanzamiento de PDF

Agregue acciones de lanzamiento basadas en JavaScript a un documento PDF usando Python y Aspose.PDF. Asigna acciones a eventos clave del documento, como la apertura, el guardado y la impresión, permitiendo que las URL se lancen automáticamente cuando esos eventos ocurran en los visores PDF compatibles.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_launch_actions(infile, outfile):
    """Add JavaScript launch actions for document events.

    Adds JavaScript actions that launch URLs when specific document events occur:
    - On document open: launches http://localhost:3000/open
    - Before saving: launches http://localhost:3000/save
    - Before printing: launches http://localhost:3000/print

    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to save the output PDF with document actions.

    Returns:
        None

    Example:
        >>> add_launch_actions("sample_data/input/add_launch_actions_in.pdf", "sample_data/output/add_launch_actions_out.pdf")

    Notes:
        - Uses `ap.annotations.JavascriptAction` with `app.launchURL()`.
        - URLs are opened in the default browser depending on viewer support.
    """

    document = ap.Document(infile)

    # Add JavaScript actions for document events
    document.open_action = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/open');"
    )
    document.actions.before_saving = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/save');"
    )
    document.actions.before_printing = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/print');"
    )

    document.save(outfile)
```

## Eliminando acciones del documento PDF

Para limpiar (o eliminar) acciones, simplemente establece el controlador en `None`.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def remove_page_actions(infile, outfile):
    document = ap.Document(infile)

    if len(document.pages) < 3:
        print("Error: The document does not have at least 3 pages.")
        return

    page = document.pages[3]
    page.actions.remove_actions()

    document.save(outfile)
```

## Agregar acciones a la página en el documento PDF

Los activadores similares se proporcionan para páginas: `on_open`, `on_close`.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_page_actions(infile, outfile):
    document = ap.Document(infile)

    if len(document.pages) < 3:
        print("Error: The document does not have at least 3 pages.")
        return

    page = document.pages[3]

    # Add GoTo action on page open - navigate to top of page
    action = ap.annotations.GoToAction(page)
    action.destination = ap.annotations.XYZExplicitDestination(
        page, 0, page.page_info.height, 1
    )
    page.actions.on_open = action

    # Add JavaScript action on page close
    page.actions.on_close = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/page/3');"
    )

    document.save(outfile)
```

## Acciones en AcroForms

### Usando acciones de navegación

El estándar PDF contempla un conjunto determinado de acciones nombradas. El significado de dichas acciones se determina por su nombre.
En el siguiente código utilizaremos acciones para navegaciones.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_navigation_buttons(infile, outfile):
    # Configuration for each navigation button
    button_config = [
        ("First Page", 10.0, PredefinedAction.FIRST_PAGE, lambda p, t: p == 1),
        ("Previous Page", 120.0, PredefinedAction.PREV_PAGE, lambda p, t: p == 1),
        ("Next Page", 230.0, PredefinedAction.NEXT_PAGE, lambda p, t: p == t),
        ("Last Page", 340.0, PredefinedAction.LAST_PAGE, lambda p, t: p == t),
    ]

    document = ap.Document(infile)
    total_pages = len(document.pages)

    # Add navigation buttons to each page
    for page in document.pages:
        for name, x_pos, action, is_readonly_fn in button_config:
            # Create button rectangle
            rect = Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
            button = ButtonField(page, rect)
            button.partial_name = name
            button.value = name
            button.characteristics.border = ap.Color.red.to_rgb()
            button.characteristics.background = ap.Color.orange.to_rgb()
            # Disable button when not applicable
            button.read_only = is_readonly_fn(page.number, total_pages)
            button.actions.on_release_mouse_btn = NamedAction(action)
            document.form.add(button)

    document.save(outfile)
```

Este código agrega botones de navegación a cada página de un documento PDF, facilitando a los usuarios moverse entre páginas. Comienza determinando las rutas de archivo completas para los archivos de entrada y salida usando un método auxiliar. La lista button_config define cuatro tipos de botones de navegación—First Page, Previous Page, Next Page y Last Page—junto con sus posiciones horizontales, las acciones de navegación predefinidas que desencadenan y una función lambda que determina si cada botón debe ser de solo lectura en una página dada (por ejemplo, los botones "First Page" y "Previous Page" son de solo lectura en la primera página).

El código luego carga el PDF y recorre cada página. Para cada página, recorre las configuraciones de botones, creando un área rectangular para cada botón e instanciando un ButtonField en esa ubicación. A cada botón se le asigna un nombre, su estado de solo lectura se establece según la página actual, y su acción de clic se asigna a la acción de navegación correspondiente. El botón se agrega luego a los campos de formulario del PDF.

Después de que todos los botones se añaden a todas las páginas, el documento modificado se guarda. Si ocurre algún error durante este proceso, se captura y se imprime. Este enfoque asegura que cada página tenga un conjunto coherente de controles de navegación, mejorando la usabilidad de los PDFs de varias páginas. Una sutileza es el uso de la lambda is_readonly_fn para desactivar los botones de navegación cuando no tendrían sentido (por ejemplo, \u0022Next Page\u0022 en la última página), lo que ayuda a prevenir la confusión del usuario.

### Usando acciones de impresión

Al usar formularios PDF, a menudo es necesario imprimir dichos documentos PDF. Esta acción se puede realizar con un PDF Reader, pero a veces es más conveniente hacerlo directamente desde el documento mediante un botón especial.

De hecho, este es otro ejemplo de cómo usar acciones nombradas. Usaremos `PredefinedAction.FILE_PRINT` (simulando el uso del elemento de menú File->Print), pero también puedes usar `PredefinedAction.PRINT` o `PredefinedAction.PRINT_DIALOG`, dependiendo de sus propios propósitos.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_named_action_print(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    # Create print button with specific dimensions and position
    rect = Rectangle(10, 10, 100, 40, True)
    print_button = ButtonField(page, rect)
    print_button.partial_name = "printButton"
    print_button.value = "Print"
    print_button.actions.on_release_mouse_btn = NamedAction(PredefinedAction.FILE_PRINT)

    # Add border for better visibility
    border = ap.annotations.Border(print_button)
    border.width = 1
    print_button.border = border

    # Add button to the form on page 1
    document.form.add(print_button, 1)
    document.save(outfile)
```

Este fragmento de código demuestra cómo agregar un botón "Print" a la primera página de un documento PDF. Comienza cargando el PDF desde la ruta de archivo de entrada especificada y seleccionando la primera página (document.pages[1]).

Se define un área rectangular para la posición y el tamaño del botón en la página. Luego se crea un ButtonField en esa ubicación, se le asigna el nombre "printButton" y su valor de visualización se establece en "Print". El botón está configurado de modo que, cuando se pulsa (específicamente, cuando se suelta el botón del ratón), active la acción predefinida "Print File", lo que hace que el visor de PDF abra el cuadro de diálogo de impresión.

Para mejorar la apariencia del botón, se crea un borde y se asigna al botón, con su ancho establecido en 1 unidad. Luego, el botón se añade a los campos de formulario PDF en la primera página. Finalmente, el documento modificado se guarda en la ruta del archivo de salida. Este enfoque brinda a los usuarios una forma conveniente de imprimir el documento directamente desde el PDF. Tenga en cuenta que la efectividad de esta función depende del soporte del visor PDF para campos de formulario interactivos y acciones predefinidas.

### Usando la acción Ocultar

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_named_action_hide(infile, outfile):
    document = ap.Document(infile)
    # Collect all checkbox fields in the document
    checkboxes = [
        field for field in document.form if is_assignable(field, CheckboxField)
    ]

    # Create the hide button
    rect = Rectangle(10, 410, 140, 440, True)
    hide_button = ButtonField(document.pages[1], rect)
    hide_button.partial_name = "HideButton"
    hide_button.value = "Hide Checkboxes"

    # Add HideAction to button - will hide all checkboxes when clicked
    hide_button.actions.on_release_mouse_btn = HideAction(checkboxes, True)

    # Add button to the form on page 1
    document.form.add(hide_button, 1)

    # Save the modified PDF
    document.save(outfile)
```

Este fragmento de código agrega un botón a la primera página de un PDF que, al hacer clic, oculta todos los campos de casilla de verificación en el documento. Comienza resolviendo las rutas completas de los archivos de entrada y salida usando un método auxiliar. El PDF se carga y todos los campos de casilla de verificación se recopilan filtrando los campos del formulario por instancias de `ap.CheckboxField`.

Se define un área rectangular para la posición del nuevo botón cerca de la parte superior de la página. Se crea un ButtonField en esta ubicación, llamado "HideButton", y etiquetado como "Hide Checkboxes". El botón está configurado de modo que, cuando se hace clic en él (al soltar el botón del ratón), ejecuta una HideAction que oculta todas las casillas de verificación recopiladas.

El botón se agrega luego a los campos del formulario en la primera página, y el PDF modificado se guarda en el archivo de salida. Si ocurre algún error durante este proceso, se capturan y se imprimen. Esta característica brinda a los usuarios una forma de ocultar rápidamente todas las casillas de verificación en el PDF, lo que puede ser útil para personalizar la apariencia o el flujo de trabajo del documento.

### Aplicando acción de envío

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_submit_action(infile, outfile):
    document = ap.Document(infile)

    # Create the submit action
    submit_action = SubmitFormAction()
    submit_action.url = ap.FileSpecification("http://localhost:3000/submit")
    submit_action.flags = (
        SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES
    )

    # Create the submit button
    rect = Rectangle(10, 10, 100, 40, True)
    submit_button = ButtonField(document.pages[1], rect)
    submit_button.partial_name = "SubmitButton"
    submit_button.value = "Submit"
    submit_button.actions.on_release_mouse_btn = submit_action

    # Add the button to the form on page 1
    document.form.add(submit_button, 1)

    # Save the document
    document.save(outfile)
```

Esta función agrega un botón "Submit" a la primera página de un formulario PDF, permitiendo a los usuarios enviar los datos del formulario a un punto final web especificado. Comienza construyendo las rutas completas para los archivos PDF de entrada y salida, luego carga el PDF de entrada usando la biblioteca Aspose.PDF.

A `SubmitFormAction` se crea para definir el comportamiento cuando se hace clic en el botón. La url de la acción se establece usando un `FileSpecification` apuntando a http://localhost:3000/submit, lo que significa que los datos del formulario se enviarán a esta URL. La propiedad flags combina `EXPORT_FORMAT` y `SUBMIT_COORDINATES`, asegurándose de que los datos del formulario se exporten en un formato estándar y que las coordenadas del clic del botón se incluyan en el envío.

Se define un área rectangular para la posición y el tamaño del botón en la página. Se crea un ButtonField en esta ubicación en la primera página, con el nombre "SubmitButton," y su valor de visualización se establece en "Submit." La acción de envío se asigna al evento de liberación del ratón del botón, de modo que la acción se dispara cuando el usuario hace clic en el botón.

Finalmente, el botón se agrega a los campos del formulario en la primera página, y el PDF modificado se guarda en el archivo de salida. Si ocurre algún error durante este proceso, se captura y se muestra. Este enfoque brinda una forma fácil de usar para que los usuarios de PDF envíen los datos del formulario directamente a un punto final del servidor.

## Temas de navegación relacionados

- [Navegación e interacción en PDF usando Python](/pdf/es/python-net/navigation-and-interaction/)
- [Trabajar con marcadores en PDF usando Python](/pdf/es/python-net/bookmarks/)
- [Trabajar con enlaces en PDF usando Python](/pdf/es/python-net/links/)
