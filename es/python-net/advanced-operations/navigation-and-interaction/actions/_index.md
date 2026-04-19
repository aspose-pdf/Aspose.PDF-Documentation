---
title: Trabajar con acciones PDF en Python
linktitle: Acciones
type: docs
weight: 20
url: /es/python-net/actions/
description: Aprenda cómo agregar, actualizar y eliminar acciones de documento, página y formulario en archivos PDF usando Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Agregue acciones de documento, página y formulario a archivos PDF en Python.
Abstract: Este artículo explora cómo trabajar con acciones en documentos PDF utilizando la biblioteca Aspose.PDF, abarcando interacciones a nivel de documento, a nivel de página y a nivel de formulario. Las acciones PDF son disparadores predefinidos o personalizables que responden a eventos del usuario, permitiendo la navegación, la ejecución de JavaScript, la reproducción multimedia, el envío de formularios y más. La guía demuestra cómo agregar, personalizar y eliminar acciones, como abrir URLs en eventos del documento, crear navegación o efectos de zoom específicos de página, añadir botones interactivos para imprimir y navegar, ocultar elementos de formulario de forma dinámica y enviar datos de formulario a puntos finales web. A través de ejemplos detallados de código Python, los lectores aprenden a mejorar la interactividad de los PDF, optimizar flujos de trabajo e integrar los PDF con sistemas externos mientras comprenden consideraciones de compatibilidad del visor.
---

Las acciones en un PDF son tareas predefinidas que se activan mediante la interacción del usuario o eventos del documento. Pueden usarse para:

- Navegar a una página específica o archivo externo
- Abrir un enlace web
- Reproducir contenido multimedia
- Ejecutar JavaScript
- Enviar o restablecer un formulario
- Mostrar/ocultar campos
- Cambiar nivel de zoom o modo de vista

Casi todas las acciones utilizan parámetros incorporados, pero hay algunas que pueden personalizarse. Por ejemplo - Acciones de JavaScript.

Esta guía es útil cuando necesitas activar la navegación, la impresión, el envío de formularios o JavaScript desde eventos del documento, eventos de página o controles interactivos de formularios PDF.

## Acciones a nivel de documento

### Agregar acciones al documento PDF

Los documentos PDF admiten varias acciones a nivel de documento, incluido código que se ejecuta al abrir el documento o en respuesta a eventos específicos. Use el `open_action` propiedad para acciones al abrir; otras acciones se gestionan en el `actions` colección.

Consideremos cómo usar `open_action.`

```python
import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

document = ap.Document(path_infile)
document.open_action = ap.annotations.JavascriptAction(
    "app.launchURL('http://localhost:3000/open');"
)
document.save(path_outfile)
```

En este ejemplo llamamos `launchURL` método de `app` obejct y abrir sitio web (para fines de demostración).

Otras acciones se pueden añadir de la misma manera, pero con cambios menores:

```python
import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

document = ap.Document(path_infile)
document.actions.before_saving = ap.annotations.JavascriptAction(
    "app.launchURL('http://localhost:3000/save');"
)
document.actions.before_printing = ap.annotations.JavascriptAction(
    "app.launchURL('http://localhost:3000/print');"
)
```

Puede agregar acciones para los siguientes eventos: `before_saving`, `before_printing`, `before_closing`, `after_saving`, `after_printing`.

Este fragmento de código muestra cómo adjuntar acciones JavaScript a varios eventos a nivel de documento en un PDF. Primero, carga un documento PDF existente desde la ruta de archivo de entrada especificada. El `document.open_action` la propiedad está configurada con una acción JavaScript que abre una URL cuando se abre el documento, provocando que el visor PDF se abra `http://localhost:3000/open` en el navegador del usuario.

A continuación, se asignan dos acciones JavaScript adicionales al documento `before_saving` y `before_printing` eventos. Estas acciones se activan cuando el usuario intenta guardar o imprimir el documento, respectivamente, cada vez lanzando una URL diferente (`/save` o `/print`) en el navegador. Esto puede ser útil para rastrear interacciones de usuario o integrarse con flujos de trabajo basados en la web.

### Eliminando acciones del documento PDF

Para limpiar (o eliminar) acciones, simplemente establezca el controlador en `None`.

```python
import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

document = ap.Document(path_infile)
document.open_action = None
document.actions.before_saving = None
document.actions.before_printing = None
document.save(path_outfile)
```

## Acciones a nivel de página

### Agregar acciones a la página en el documento PDF

Los disparadores similares se proporcionan para las páginas: `on_open`, `on_close`.

```python
import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...


def add_page_actions(self, infile, outfile):
    """
    Add actions to the third page of the PDF.

    Adds two actions to page 3:
    - On page open: Navigate to the top of the page with specific zoom
    - On page close: Launch a URL with page-specific information

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Raises:
        ValueError: If document has fewer than 3 pages

    Example:
        >>> actions.add_page_actions("multipage.pdf", "page_actions.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    document = ap.Document(path_infile)

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

    document.save(path_outfile)
```

Agregamos dos acciones a esta página. Primero, crea una acción \u0022GoTo\u0022 que se activa cuando se abre la página. Esta acción usa un destino explícito para saltar a la esquina superior izquierda de la página a un nivel de zoom específico. Segundo, adjunta una acción JavaScript que se ejecuta cuando se cierra la página, indicando al visor de PDF que abra una URL específica en el navegador. Finalmente, el documento modificado se guarda en la ruta de salida especificada.

Un punto sutil a vigilar es la indexación de páginas, ya que usar el índice incorrecto podría provocar un comportamiento inesperado o errores. Además, el uso de acciones JavaScript en PDFs puede no ser compatible con todos los lectores de PDF, por lo que esta característica podría no funcionar en todas partes.

### Eliminando acciones de la página PDF

Usar `remove_actions` para eliminar la acción en la página.

```python
import aspose.pdf as ap
from os import path

document = ap.Document(path_infile)

if len(document.pages) < 3:
    print("Error: The document does not have at least 3 pages.")
    return

page = document.pages[3]
page.actions.remove_actions()

document.save(path_outfile)
```

## Acciones en AcroForms

### Usando acciones de navegación

El estándar PDF contempla un conjunto determinado de acciones con nombre. El significado de dichas acciones se determina por su nombre.
En el siguiente código usaremos acciones para navegaciones.

```python
import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...


def add_navigation_buttons(self, infile, outfile):
    """
    Add navigation buttons to each page of the PDF.

    Creates four navigation buttons on each page:
    - First Page: Navigate to the first page
    - Previous Page: Navigate to the previous page
    - Next Page: Navigate to the next page
    - Last Page: Navigate to the last page

    Buttons are automatically disabled when not applicable (e.g.,
    "Previous" is disabled on the first page).

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Example:
        >>> actions.add_navigation_buttons("multipage.pdf", "nav_buttons.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    # Configuration for each navigation button
    button_config = [
        ("First Page", 10.0, PredefinedAction.FIRST_PAGE, lambda p, t: p == 1),
        ("Previous Page", 120.0, PredefinedAction.PREV_PAGE, lambda p, t: p == 1),
        ("Next Page", 230.0, PredefinedAction.NEXT_PAGE, lambda p, t: p == t),
        ("Last Page", 340.0, PredefinedAction.LAST_PAGE, lambda p, t: p == t),
    ]

    try:
        document = ap.Document(path_infile)
        total_pages = len(document.pages)

        # Add navigation buttons to each page
        for page in document.pages:
            page_number = page.number

            for name, x_pos, action, is_readonly_fn in button_config:
                # Create button rectangle
                rect = Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
                button = ButtonField(page, rect)
                button.partial_name = name

                # Disable button when not applicable
                button.read_only = is_readonly_fn(page_number, total_pages)
                button.actions.on_release_mouse_btn = NamedAction(action)

                document.form.add(button)

        document.save(path_outfile)

    except Exception as e:
        print(f"Error adding navigation buttons: {e}")
```

Este código agrega botones de navegación a cada página de un documento PDF, facilitando a los usuarios moverse entre las páginas. Comienza determinando las rutas completas de los archivos de entrada y salida mediante un método auxiliar. La lista button_config define cuatro tipos de botones de navegación—First Page, Previous Page, Next Page, y Last Page—junto con sus posiciones horizontales, las acciones de navegación predefinidas que desencadenan y una función lambda que determina si cada botón debe ser de solo lectura en una página dada (por ejemplo, los botones "First Page" y "Previous Page" son de solo lectura en la primera página).

El código luego carga el PDF y recorre cada página. Para cada página, recorre las configuraciones de los botones, creando un área rectangular para cada botón e instanciando un ButtonField en esa ubicación. A cada botón se le asigna un nombre, su estado de solo lectura se establece en función de la página actual, y su acción de clic se asigna a la acción de navegación correspondiente. El botón se agrega entonces a los campos de formulario del PDF.

Después de que todos los botones se añaden a todas las páginas, el documento modificado se guarda. Si se produce algún error durante este proceso, se captura y se imprime. Este enfoque asegura que cada página tenga un conjunto consistente de controles de navegación, mejorando la usabilidad de los PDFs de varias páginas. Un detalle sutil es el uso de la lambda is_readonly_fn para desactivar los botones de navegación cuando no tendría sentido (por ejemplo, "Siguiente página" en la última página), lo que ayuda a prevenir la confusión del usuario.

### Usando acciones de impresión

Cuando se utilizan formularios PDF, a menudo es necesario imprimir dichos documentos PDF. Esta acción puede realizarse usando un PDF Reader, pero a veces resulta más conveniente hacerlo directamente desde el documento mediante un botón especial.

De hecho, este es otro ejemplo más de cómo usar acciones con nombre. Usaremos `PredefinedAction.FILE_PRINT` (simulando el uso del elemento del menú Archivo->Imprimir), pero también puedes usar `PredefinedAction.PRINT` o `PredefinedAction.PRINT_DIALOG`, dependiendo de sus propios propósitos.

```python
import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...


def add_named_action_print(self, infile, outfile):
    """
    Add a print button to the first page of the PDF.

    Creates a button labeled "Print" that triggers the system print dialog
    when clicked. The button is positioned at the bottom-left corner of
    the first page with a 1-pixel border.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Example:
        >>> actions.add_named_action_print("input.pdf", "output.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    document = ap.Document(path_infile)
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
    document.save(path_outfile)
```

Este fragmento de código demuestra cómo agregar un botón \"Print\" a la primera página de un documento PDF. Comienza cargando el PDF desde la ruta de archivo de entrada especificada y seleccionando la primera página (document.pages[1]).

Se define un área rectangular para la posición y el tamaño del botón en la página. Luego se crea un ButtonField en esa ubicación, se le asigna el nombre "printButton," y su valor de visualización se establece en "Print." El botón se configura de manera que, cuando se hace clic en él (específicamente, cuando se suelta el botón del ratón), active la acción predefinida "Print File" y haga que el visor de PDF abra el cuadro de diálogo de impresión.

Para mejorar la apariencia del botón, se crea un borde y se asigna al botón, con su ancho establecido en 1 unidad. Luego, el botón se añade a los campos de formulario PDF en la primera página. Finalmente, el documento modificado se guarda en la ruta del archivo de salida. Este enfoque proporciona a los usuarios una manera conveniente de imprimir el documento directamente desde el PDF. Tenga en cuenta que la efectividad de esta función depende del soporte del visor PDF para campos de formulario interactivos y acciones predefinidas.

### Usando la acción Ocultar

```python
import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...


def add_named_action_hide(self, infile, outfile):
    """
    Add a hide button that toggles visibility of all checkbox fields.

    Creates a button labeled "Hide Checkboxes" that can hide or show
    all checkbox fields in the document. Useful for forms with many
    checkboxes that might clutter the interface.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Example:
        >>> actions.add_named_action_hide("form.pdf", "form_with_hide.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    try:
        document = ap.Document(path_infile)
        # Collect all checkbox fields in the document
        checkboxes = [
            field for field in document.form if isinstance(field, ap.CheckboxField)
        ]

        # Create the hide button
        rect = Rectangle(10, 510, 100, 540)
        hide_button = ButtonField(document.pages[1], rect)
        hide_button.partial_name = "HideButton"
        hide_button.value = "Hide Checkboxes"

        # Add HideAction to button - will hide all checkboxes when clicked
        hide_button.actions.on_release_mouse_btn = ap.HideAction(checkboxes, True)

        # Add button to the form on page 1
        document.form.add(hide_button, 1)

        # Save the modified PDF
        document.save(path_outfile)

    except Exception as e:
        print(f"Error adding hide button: {e}")
```

Este fragmento de código agrega un botón a la primera página de un PDF que, al hacer clic, oculta todos los campos de casilla de verificación en el documento. Comienza resolviendo las rutas completas de los archivos de entrada y salida mediante un método auxiliar. El PDF se carga y se recopilan todos los campos de casilla de verificación filtrando los campos del formulario para instancias de `ap.CheckboxField`.

Se define un área rectangular para la posición del nuevo botón cerca de la parte superior de la página. Se crea un ButtonField en esta ubicación, llamado “HideButton” y etiquetado como “Hide Checkboxes”. El botón está configurado para que, cuando se haga clic en él (al soltar el botón del ratón), desencadene una HideAction que oculta todas las casillas de verificación recopiladas.

El botón se agrega a los campos de formulario en la primera página, y el PDF modificado se guarda en el archivo de salida. Si ocurre algún error durante este proceso, se captura y se imprime. Esta función brinda a los usuarios una manera de ocultar rápidamente todas las casillas de verificación en el PDF, lo cual puede ser útil para personalizar la apariencia o el flujo de trabajo del documento.

### Aplicando acción de envío

```python
import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...


def add_submit_action(self, infile, outfile):
    """
    Submit form.

    Parameters:
    - infile (str): The name of the input PDF file.
    - outfile (str): The name of the output PDF file.
    """
    path_infile = self.dataDir + infile
    path_outfile = self.dataDir + outfile

    try:
        document = ap.Document(path_infile)

        # Create the submit action
        submit_action = ap.SubmitFormAction()
        submit_action.url = FileSpecification("http://localhost:3000/submit")
        submit_action.flags = (
            SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES
        )

        # Create the submit button
        rect = Rectangle(10, 10, 100, 40)
        submit_button = ButtonField(document.pages[1], rect)
        submit_button.partial_name = "SubmitButton"
        submit_button.value = "Submit"
        submit_button.actions.on_release_mouse_btn = submit_action

        # Add the button to the form on page 1
        document.form.add(submit_button, 1)

        # Save the document
        document.save(path_outfile)

    except Exception as e:
        print(f"Error adding submit button: {e}")
```

Esta función agrega un botón "Submit" a la primera página de un formulario PDF, permitiendo a los usuarios enviar los datos del formulario a un endpoint web especificado. Comienza construyendo las rutas completas para los archivos PDF de entrada y salida, luego carga el PDF de entrada usando la biblioteca Aspose.PDF.

A `SubmitFormAction` se crea para definir el comportamiento cuando se hace clic en el botón. La URL de la acción se establece usando un `FileSpecification` apuntando a http://localhost:3000/submit, lo que significa que los datos del formulario se enviarán a esta URL. La propiedad flags combina `EXPORT_FORMAT` y `SUBMIT_COORDINATES`, asegurando que los datos del formulario se exporten en un formato estándar y que las coordenadas del clic del botón se incluyan en el envío.

Se define un área rectangular para la posición y el tamaño del botón en la página. Se crea un ButtonField en esta ubicación en la primera página, se le asigna el nombre "SubmitButton" y su valor de visualización se establece en "Submit". La acción de envío se asigna al evento de liberación del mouse del botón, de modo que la acción se activa cuando el usuario hace clic en el botón.

Finalmente, el botón se añade a los campos del formulario en la primera página y el PDF modificado se guarda en el archivo de salida. Si se produce algún error durante este proceso, se captura y se muestra. Este enfoque brinda una manera fácil de usar para que los usuarios de PDF envíen los datos del formulario directamente a un punto final del servidor.

## Temas de Navegación Relacionados

- [Navegación e interacción en PDF usando Python](/pdf/es/python-net/navigation-and-interaction/)
- [Trabajar con marcadores en PDF usando Python](/pdf/es/python-net/bookmarks/)
- [Trabajar con enlaces en PDF usando Python](/pdf/es/python-net/links/)
