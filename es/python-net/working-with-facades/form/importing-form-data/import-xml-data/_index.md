---
title: Importar datos XML
type: docs
weight: 40
url: /es/python-net/import-xml-data/
description: Este ejemplo muestra cómo importar datos de formulario desde un archivo XML a los campos de formulario PDF utilizando Aspose.PDF for Python via .NET. Muestra cómo vincular un documento PDF, leer datos XML estructurados a través de un flujo de archivo y rellenar automáticamente los campos de formulario correspondientes.
lastmod: "2026-02-19"
---

XML se usa comúnmente para almacenar datos de formulario estructurados, lo que lo convierte en un formato práctico para transferir valores entre sistemas. En este ejemplo, el [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada de [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) se usa para cargar un formulario PDF y aplicar valores de campo directamente desde un archivo XML. Después de importar los datos, el PDF actualizado se guarda como un nuevo documento.

1. Inicializar pdf_facades.Form() para interactuar con los campos de formulario PDF.
1. Llama a 'bind_pdf()' para adjuntar la plantilla del formulario PDF.
1. Use 'FileIO()' para acceder al archivo XML que contiene los datos del formulario.
1. Llama a 'import_xml()' para rellenar los campos PDF con valores del archivo XML.
1. Guarde el PDF actualizado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Import data from XML
def import_xml_to_pdf_fields(infile, datafile, outfile):
    """Import form data from XML file into PDF form fields."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XML file as stream
    with FileIO(datafile, "r") as xml_input_stream:
        # Import data from XML into PDF form fields
        pdf_form.import_xml(xml_input_stream)

    # Save updated PDF
    pdf_form.save(outfile)
```
