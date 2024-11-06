---
title: Crear documento PDF
linktitle: Crear PDF
type: docs
weight: 10
url: es/python-cpp/create-document/
description: Esta página describe cómo crear un documento PDF desde cero con la biblioteca Aspose.PDF para Python vía C++.
---

Para los desarrolladores, hay muchos escenarios en los que se hace necesario generar archivos PDF programáticamente. Puede ser necesario generar informes PDF y otros archivos PDF programáticamente en su software. Es bastante largo e ineficiente escribir su propio código y funciones desde cero. Para crear un archivo PDF con Python, hay una mejor solución - **Aspose.PDF para Python vía C++**.

## Crear archivo PDF usando Python

Para crear un archivo PDF usando Python, se pueden utilizar los siguientes pasos.

* importar todas las clases y métodos de la biblioteca Aspose.PDF para Python vía C++.
* Crear un nuevo objeto Document que representa un documento PDF vacío usando [document_create](https://reference.aspose.com/pdf/python-cpp/core/document_create/)

* Obtener el objeto [document_get_pages](https://reference.aspose.com/pdf/python-cpp/core/document_get_pages/) que contiene todas las páginas del documento.
* Agrega una nueva página al final de la colección de páginas [page_collection_add_page](https://reference.aspose.com/pdf/python-cpp/core/page_collection_add_page/) y devuelve el objeto Page que representa la página agregada.
* Guarda el documento en un archivo con el nombre especificado en el directorio de trabajo actual.
* Cierra el manejador del documento y libera cualquier recurso asociado con él.

```python

    from AsposePDFPython import *

    doc = document_create()
    pages = document_get_pages(doc)
    page = page_collection_add_page(pages)
    document_save(doc, "blank_pdf_document.pdf")
    close_handle(doc)
```


## Crear archivo PDF basado en DOM

```python

    from AsposePDFPythonWrappers import *

    doc = Document()
    page = doc.pages.add()
    doc.save("blank_pdf_document1.pdf")
```