---
title: Crear enlaces PDF en Python
linktitle: Crear enlaces
type: docs
weight: 10
url: /es/python-net/create-links/
description: Aprende cómo crear enlaces PDF internos, externos y remotos en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo crear enlaces en PDF
Abstract: La guía Aspose.PDF for Python via .NET sobre la creación de enlaces proporciona a los desarrolladores instrucciones prácticas para agregar hipervínculos interactivos a documentos PDF usando Python. Cubre cómo crear varios tipos de enlaces, incluidos los que lanzan aplicaciones externas, navegan a páginas específicas dentro del mismo documento o abren otros archivos PDF. La documentación explica cómo usar objetos LinkAnnotation, definir áreas clicables con Rectangle y asignar acciones como LaunchAction o GoToRemoteAction. Con ejemplos de código claros y una guía paso a paso, este recurso ayuda a los desarrolladores a mejorar la navegación e interactividad de los PDF en sus aplicaciones Python.
---

## Enlaces en documentos PDF

Según la especificación PDF 1.7 (ISO 32000-1:2008), una **Link annotation** puede activar varios tipos de acciones que definen lo que ocurre cuando se activa la anotación. Aquí están las acciones principales admitidas:

1. **GoTo** – Navega a un destino dentro del mismo documento.
1. **GoToR** – Salta a un destino en otro archivo PDF (go-to remoto).
1. **URI** – Abre un identificador uniforme de recursos, típicamente un enlace web.
1. **Launch** – Lanza una aplicación o abre un archivo (dependiendo de la plataforma y a menudo restringido por motivos de seguridad).
1. **Named** – Ejecuta una acción predefinida, como ir a la página siguiente o imprimir el documento.
1. **JavaScript** – Ejecuta código JavaScript incrustado (se usa con precaución debido a preocupaciones de seguridad).
1. **SubmitForm** – Envía los datos del formulario a una URL especificada.
1. **ResetForm** – Restablece los campos del formulario a sus valores predeterminados.
1. **ImportData** – Importa datos al documento desde un archivo externo.

Al agregar un enlace a una aplicación dentro de un documento, es posible enlazar a aplicaciones desde un documento. Esto es útil cuando deseas que los lectores realicen una acción determinada en un punto específico de un tutorial, por ejemplo, o para crear un documento con muchas funciones.

Para crear un enlace a una aplicación con ‘LaunchAction’:

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_launch_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    border = ap.annotations.Border(link)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    link.color = ap.Color.green
    link.action = ap.annotations.LaunchAction(document, "sample.pdf")
    page.annotations.append(link)
    document.save(outfile)
```

## Crear enlace de documento PDF en un archivo PDF

### Usando GoToRemoteAction

Este fragmento de código demuestra cómo agregar una anotación de enlace a una página específica de un documento PDF usando una biblioteca PDF de Python.

1. Abre el documento PDF
1. Selecciona la segunda página del documento (índice 1)
1. Crea una anotación de enlace:
1. Posicionado en las coordenadas (10, 580, 120, 600)
1. Coloreado verde
1. Enlaces a 'sample.pdf' en su primera página
1. Agregar la anotación de enlace a la página
1. Guardar el documento modificado en la ruta del archivo de salida

Para crear un enlace de documento PDF usando 'GoToRemoteAction':

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_go_to_remote_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    link.color = ap.Color.green
    link.action = ap.annotations.GoToRemoteAction("sample.pdf", 1)
    page.annotations.append(link)
    document.save(outfile)
```

### Usando GoToAction

Este código muestra cómo agregar una anotación de enlace a una página específica de un documento PDF usando Aspose.PDF for Python. El enlace aparece como un rectángulo verde con borde discontinuo y permite al usuario navegar a otra página dentro del mismo PDF. Para crear un enlace de documento PDF usando 'GoToAction':

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_go_to_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    border = ap.annotations.Border(link)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    link.color = ap.Color.green
    if document.pages.length >= 4:
        link.action = ap.annotations.GoToAction(document.pages[4])
    else:
        link.action = ap.annotations.GoToAction(document.pages[document.pages.length])
    page.annotations.append(link)
    document.save(outfile)
```

### Aplicando GoToURIAction

El siguiente ejemplo muestra cómo agregar una anotación de enlace a un documento PDF usando Aspose.PDF for Python. El enlace aparece como un área verde clicable en la primera página, y al hacer clic, abre la documentación de Aspose.PDF for Python en un navegador web mediante una GoToURIAction.

Esta funcionalidad es útil para incrustar referencias externas útiles, documentación o enlaces de soporte directamente dentro de sus PDFs.

1. Cargue el documento PDF. Abra el archivo PDF existente usando ap.Document.
1. Acceda a la primera página. Use document.pages[1] para acceder a la primera página (Aspose usa indexación basada en 1).
1. Cree una anotación de enlace. Cree un objeto LinkAnnotation y especifique el área rectangular clicable usando ap.Rectangle.
1. Establecer apariencia de la anotación. Establecer el color de la anotación a verde usando link.color = ap.Color.green.
1. Asignar una acción URI. Utilizar GoToURIAction para vincular la anotación a una URL externa.
1. Agregar la anotación a la página. Añadir la anotación de enlace configurada a la colección de anotaciones de la primera página.
1. Guardar el documento modificado. Guardar el documento PDF actualizado en la ruta de salida especificada.

```python
import aspose.pdf as ap
from os import path
import sys
    
def create_link_annotation_go_to_URI_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    link.color = ap.Color.green
    link.action = ap.annotations.GoToURIAction("https://docs.aspose.com/pdf/python")
    page.annotations.append(link)
    document.save(outfile)
```

## Temas relacionados de enlaces

- [Trabajar con enlaces PDF en Python](/pdf/es/python-net/links/)
- [Extraer enlaces del PDF en Python](/pdf/es/python-net/extract-links/)
- [Actualizar enlaces en el PDF usando Python](/pdf/es/python-net/update-links/)