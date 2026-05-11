---
title: Exportar a XML
linktitle: Exportar a XML
type: docs
weight: 40
url: /es/python-net/export-to-xml/
description: Este ejemplo demuestra cómo exportar los datos de formulario PDF a un archivo XML usando Aspose.PDF for Python via .NET. Muestra cómo cargar un documento PDF, acceder a sus campos de formulario a través del Form facade y guardar los datos extraídos como XML estructurado usando Form Class.
lastmod: "2026-02-19"
---

Exportar datos de formulario permite a los desarrolladores reutilizar la información almacenada en PDF AcroForms sin copiar manualmente los valores de los campos. En este ejemplo, un [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) objeto se crea a partir de aspose.pdf. En el módulo facades, el PDF de origen se vincula a él, y los datos del formulario se escriben en un flujo XML.

1. Cree un Form Object. Inicialice pdf_facades.Form() para acceder y gestionar los campos del formulario.
1. Use \u0027bind_pdf()\u0027 para adjuntar el documento PDF de origen a la instancia Form.
1. Crea un flujo de archivo escribible usando 'FileIO()'.
1. Llame a 'export_xml()' para extraer todos los valores de los campos del formulario y escribirlos en el archivo XML.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Export Data to XML
def export_pdf_form_data_to_xml(infile, datafile):
    """Export PDF form data to XML file."""
    # Create Form object
    pdf_form = pdf_facades.Form()

    # Bind PDF document
    pdf_form.bind_pdf(infile)

    # Open XML file as stream
    with FileIO(datafile, "w") as xml_output_stream:
        # Export data from PDF form fields to XML
        pdf_form.export_xml(xml_output_stream)
```
