---
title: Renombrar campos de formulario
linktitle: Renombrar campos de formulario
type: docs
weight: 30
url: /es/python-net/rename-form-fields/
description: Este ejemplo demuestra cómo renombrar campos de formulario en un documento PDF usando Aspose.PDF for Python via .NET. Muestra cómo enlazar un formulario PDF, actualizar los nombres de los campos existentes programáticamente y guardar el archivo modificado. Renombrar los campos ayuda a estandarizar las estructuras de los formularios, mejorar el mapeo de datos y simplificar la integración con flujos de trabajo automatizados o sistemas externos.
lastmod: "2026-02-19"
---

Renombrar campos de formulario es útil al alinear los formularios PDF con convenciones de nombres internas o al preparar documentos para el procesamiento de datos estructurados. En este ejemplo, el [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada del [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) módulo se utiliza para enlazar el PDF de origen y aplicar una asignación que reemplaza los nombres de campo antiguos por los nuevos. Después de actualizar los identificadores de los campos, el documento se guarda con los cambios aplicados.

1. Inicializar pdf_facades.Form() para interactuar con los campos de formulario PDF.
1. Llame a 'bind_pdf()' para adjuntar el documento PDF.
1. Cree una lista de tuplas que contengan los nombres de campo antiguos y sus nuevos nombres correspondientes.
1. Itera a través del mapeo y llama a 'rename_field()' para cada entrada.
1. Guarda el Documento actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Rename form fields
def rename_form_fields(infile, outfile):
    """Rename form fields in a PDF document."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Rename form fields by providing a mapping of old names to new names
    field_renaming_map = [("First Name", "NewFirstName"), ("Last Name", "NewLastName")]
    for old_name, new_name in field_renaming_map:
        pdf_form.rename_field(old_name, new_name)

    # Save updated PDF
    pdf_form.save(outfile)
```
