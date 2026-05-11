---
title: Importar datos XFDF
linktitle: Importar datos XFDF
type: docs
weight: 20
url: /es/python-net/import-xfdf-data/
description: Este ejemplo muestra cómo importar datos de formulario desde un archivo XFDF a un formulario PDF usando Aspose.PDF for Python via .NET. Muestra cómo enlazar un documento PDF, leer datos XFDF basados en XML mediante un flujo de archivo y rellenar automáticamente los campos de formulario coincidentes. La importación de datos XFDF permite un intercambio de datos de formulario eficiente y admite flujos de trabajo de documentos automatizados que dependen de formatos XML estructurados.
lastmod: "2026-02-19"
---

XFDF (Formato de Datos de Formularios XML) es una representación XML de los datos de formularios PDF diseñada para la interoperabilidad y el intercambio de datos. En este ejemplo, el [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada del [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) módulo se utiliza para enlazar un formulario PDF e importar valores de campos desde un archivo XFDF externo. Después de importar los datos, el PDF actualizado se guarda como un nuevo documento.

1. Inicializar pdf_facades.Form() para interactuar con los campos de formulario PDF.
1. Llama a 'bind_pdf()' para adjuntar la plantilla del formulario PDF.
1. Use 'open()' para leer el archivo XFDF.
1. Llame a 'import_xfdf()' para rellenar los campos PDF con valores del archivo XFDF.
1. Guarda el Documento actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import Data from XFDF
def import_data_from_xfdf(infile, datafile, outfile):
    """Import form data from XFDF file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XFDF file as stream
    with open(datafile, "rb") as xfdf_input_stream:
        # Import data from XFDF into PDF form fields
        pdf_form.import_xfdf(xfdf_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```
