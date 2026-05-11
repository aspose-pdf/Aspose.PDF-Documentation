---
title: Copiar campo externo
type: docs
weight: 30
url: /es/python-net/copy-outer-field/
description: Este ejemplo muestra cómo copiar un campo de formulario de un documento PDF a otro usando Aspose.PDF for Python.
lastmod: "2026-03-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Copiar campos de formulario PDF de otro documento usando Python
Abstract: Este artículo explica cómo crear un nuevo documento PDF, copiar el campo "First Name" de un PDF de origen a la página 1 en las coordenadas (200, 600), y guardar el documento de destino actualizado.
---

A veces, los formularios PDF requieren reutilizar campos de un documento en otro. Usando Aspose.PDF for Python, los desarrolladores pueden copiar programáticamente los campos de formulario de un PDF de origen a un PDF de destino.

El [FormEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formeditor/) la clase proporciona el método 'copy_outer_field', que copia un campo de un documento de origen a un documento de destino en una página y coordenadas especificadas.

El código crea un nuevo PDF (destino), agrega una página y luego copia un campo de un PDF existente (origen) al documento de destino en coordenadas especificadas.

1. Crear un nuevo documento PDF de destino.
1. Agregue al menos una página al PDF de destino.
1. Guarde el documento de destino vacío.
1. Cree un objeto FormEditor y vincúlelo al PDF de destino.
1. Copie el campo 'First Name' del PDF fuente a la página 1 en (200, 600).
1. Guardar el PDF de destino actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def copy_outer_field(infile, outfile):
    # Since copy_outer_field() method needs to copy field from source document to target document, we need to create a new document as target document first.
    doc = ap.Document()
    doc.pages.add()
    doc.save(outfile)

    # Create FormEditor object
    form_editor = pdf_facades.FormEditor()
    # Bind document to FormEditor
    form_editor.bind_pdf(outfile)
    # Copies an existing field to a new position specified by both page number and ordinates.
    # A new document will be produced, which contains everything the source document has except for the newly copied field.
    form_editor.copy_outer_field(infile, "First Name", 1, 200, 600)
    # Save updated document
    form_editor.save(outfile)
```

**Tenga en cuenta:**

La firma del método 'copy_outer_field' se ve así:

```python
copy_outer_field(original_field_name, new_field_name, page_number, x, y)
```

- 'original_field_name' – el campo que desea duplicar.
- 'new_field_name' – el nombre del nuevo campo.
- 'page_number' – la página en la que aparecerá el nuevo campo.
- x, y – coordenadas en esa página.

Se espera que page_number sea un entero positivo que corresponda a una página existente en el PDF (indexación basada en 1).

Si pasa un parámetro negativo, p. ej.:

```python
form_editor.copy_outer_field("First Name", "First Name Copy", 1, -200, 600)
```

El programa entonces restablecerá los parámetros anteriores.
