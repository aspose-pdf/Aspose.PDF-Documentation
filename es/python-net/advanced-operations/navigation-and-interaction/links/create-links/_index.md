---
title: Crear enlaces en archivo PDF con Python
linktitle: Crear enlaces
type: docs
weight: 10
url: /es/python-net/create-links/
description: Esta sección explica cómo crear enlaces en su documento PDF con Python.
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo crear enlaces en PDF
Abstract: La guía de Aspose.PDF para Python a través de .NET sobre la creación de enlaces brinda a los desarrolladores instrucciones prácticas para añadir hipervínculos interactivos a documentos PDF usando Python. Cubre cómo crear varios tipos de enlaces, incluidos aquellos que ejecutan aplicaciones externas, navegan a páginas específicas dentro del mismo documento o abren otros archivos PDF. La documentación explica cómo usar objetos LinkAnnotation, definir áreas clicables con Rectangle y asignar acciones como LaunchAction o GoToRemoteAction. Con ejemplos de código claros y una guía paso a paso, este recurso ayuda a los desarrolladores a mejorar la navegación e interactividad de los PDFs en sus aplicaciones Python.
---

## Enlaces en documentos PDF

Según la especificación PDF 1.7 (ISO 32000-1:2008), una **anotación de enlace** puede desencadenar varios tipos de acciones que definen lo que ocurre cuando la anotación se activa. Aquí están las acciones principales admitidas:

1. **GoTo** – Navega a un destino dentro del mismo documento.
1. **GoToR** – Salta a un destino en otro archivo PDF (go-to remoto).
1. **URI** – Abre un identificador uniforme de recursos, típicamente un enlace web.
1. **Launch** – Lanza una aplicación o abre un archivo (dependiendo de la plataforma y a menudo restringido por seguridad).
1. **Named** – Ejecuta una acción predefinida, como ir a la página siguiente o imprimir el documento.
1. **JavaScript** – Ejecuta código JavaScript incrustado (usado con precaución debido a problemas de seguridad).
1. **SubmitForm** – Envía datos del formulario a una URL especificada.
1. **ResetForm** – Restablece los campos del formulario a sus valores predeterminados.
1. **ImportData** – Importa datos al documento desde un archivo externo.

Al agregar un enlace a una aplicación dentro de un documento, es posible enlazar a aplicaciones desde un documento. Esto es útil cuando desea que los lectores realicen una acción determinada en un punto específico de un tutorial, por ejemplo, o para crear un documento con muchas funciones.

Para crear un enlace a una aplicación con 'LaunchAction':

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Open the input PDF document
    document = ap.Document(path_infile)

    # Select the second page (index 1)
    page = document.pages[1]

    # Create a link annotation with specific dimensions and position
    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))

    # Configure the link's border
    border = ap.annotations.Border(link)
    border.width = 5  # Border width of 5 units
    border.dash = ap.annotations.Dash(1, 1)  # Dashed border style

    # Set link appearance
    link.color = ap.Color.green  # Green color for the link

    # Set the action to launch another PDF file
    # Note: Commented out system command demonstrates potential alternative launch actions
    # link.action = ap.annotations.LaunchAction(document, "start %windir%\explorer.exe")
    link.action = ap.annotations.LaunchAction(document, "sample.pdf")

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified document
    document.save(path_outfile)
```

## Crear enlace de documento PDF en un archivo PDF

### Usando GoToRemoteAction

Este fragmento de código demuestra cómo añadir una anotación de enlace a una página específica de un documento PDF usando una biblioteca PDF de Python.

1. Abrir el documento PDF
1. Seleccionar la segunda página del documento (índice 1)
1. Crear una anotación de enlace:
1. Posicionado en las coordenadas (10, 580, 120, 600)
1. Color verde
1. Enlaza a 'sample.pdf' en su primera página
1. Añadir la anotación de enlace a la página
1. Guardar el documento modificado en la ruta del archivo de salida

Para crear un enlace de documento PDF usando 'GoToRemoteAction':

```python

import aspose.pdf as ap
from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

# Load the input PDF document
document = ap.Document(path_infile)

# Access the first page of the document (Aspose uses 1-based indexing)
page = document.pages[1]

# Create a link annotation in the specified rectangle area on the page
link = ap.annotations.LinkAnnotation(
    page, ap.Rectangle(10, 580, 120, 600, True)  # (left, bottom, right, top, isEmpty)
)

# Set the color of the link annotation to green
link.color = ap.Color.green

# Define a remote action to open "sample.pdf" and navigate to its first page
link.action = ap.annotations.GoToRemoteAction("sample.pdf", 1)

# Add the link annotation to the current page
page.annotations.append(link)

# Save the updated PDF to the specified output path
document.save(path_outfile)
```

### Usando GoToAction

Este código demuestra cómo añadir una anotación de enlace a una página específica de un documento PDF usando Aspose.PDF para Python. El enlace aparece como un rectángulo verde con borde punteado y permite al usuario navegar a otra página dentro del mismo PDF. Para crear un enlace de documento PDF usando 'GoToAction':

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Open the PDF document
    document = ap.Document(path_infile)

    # Select the second page (index 1)
    page = document.pages[1]

    # Create a link annotation with specific coordinates
    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))

    # Customize link annotation border
    border = ap.annotations.Border(link)
    border.width = 5  # Border width
    border.dash = ap.annotations.Dash(1, 1)  # Dashed border style

    # Set link color to green
    link.color = ap.Color.green

    # Set link destination
    if document.pages.count >= 4:
        # Link to 4th page if document has 4 or more pages
        link.action = ap.annotations.GoToAction(document.pages[4])
    else:
        # Fallback: link to the last page if less than 4 pages
        link.action = ap.annotations.GoToAction(document.pages[document.pages.count])

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified document
    document.save(path_outfile)
```

### Aplicando GoToURIAction

El siguiente ejemplo demuestra cómo añadir una anotación de enlace a un documento PDF usando Aspose.PDF para Python. El enlace aparece como un área verde clicable en la primera página y, al hacer clic, abre la documentación de Aspose.PDF para Python en un navegador web mediante un GoToURIAction.

Esta funcionalidad es útil para incrustar referencias externas útiles, documentación o enlaces de soporte directamente dentro de sus PDFs.

1. Cargar el documento PDF. Abra el archivo PDF existente usando ap.Document.
1. Acceder a la primera página. Use document.pages[1] para acceder a la primera página (Aspose usa indexación basada en 1).
1. Crear una anotación de enlace. Cree un objeto LinkAnnotation y especifique el área rectangular clicable usando ap.Rectangle.
1. Establecer la apariencia de la anotación. Defina el color de la anotación a verde usando link.color = ap.Color.green.
1. Asignar una acción URI. Use GoToURIAction para enlazar la anotación a una URL externa.
1. Añadir la anotación a la página. Adjunte la anotación de enlace configurada a la colección de anotaciones de la primera página.
1. Guardar el documento modificado. Guarde el documento PDF actualizado en la ruta de salida especificada.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Access the first page (Aspose uses 1-based indexing)
    page = document.pages[1]

    # Create a link annotation at the specified rectangle position
    link = ap.annotations.LinkAnnotation(
        page, ap.Rectangle(10, 580, 120, 600, True)  # (left, bottom, right, top, isEmpty)
    )

    # Set the color of the link annotation to green
    link.color = ap.Color.green

    # Define a URI action that navigates to the Aspose.PDF Python documentation
    link.action = ap.annotations.GoToURIAction("https://docs.aspose.com/pdf/python")

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified PDF to the output path
    document.save(path_outfile)
```

