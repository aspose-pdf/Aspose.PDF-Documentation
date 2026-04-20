---
title: Importar y Exportar datos de formulario
type: docs
weight: 80
url: /es/python-net/import-export-form-data/
description: Esta sección explica cómo importar y exportar datos de formulario.
lastmod: "2025-08-05"
TechArticle: true
AlternativeHeadline: Técnicas de importación y exportación usando Aspose.PDF for Python via .NET.
Abstract: Esta compilación presenta un conjunto completo de técnicas de importación y exportación de datos de formulario usando Aspose.PDF for Python via .NET. Cubre flujos de trabajo para integrar formularios PDF con formatos de datos externos, incluidos XML, FDF, XFDF y JSON. Los usuarios pueden automatizar el llenado masivo de formularios importando datos estructurados en campos interactivos, o extraer valores de los campos para análisis, respaldo o integración con otros sistemas. Los ejemplos demuestran cómo enlazar formularios PDF, transferir datos entre formatos y guardar los documentos actualizados, lo que permite un procesamiento de documentos escalable y coherente en diversas aplicaciones.
---

Esta página resume los flujos de trabajo disponibles para importar y exportar datos AcroForm con Aspose.PDF for Python via .NET. Estas operaciones se realizan a través del [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada, por lo que los ejemplos canónicos paso a paso están documentados en la sección **Working with Facades**.

## Ejemplos de importación y exportación

Utilice los siguientes artículos para los escenarios estándar de intercambio de datos:

- [Importar datos XML](/pdf/es/python-net/import-xml-data/)
- [Importar datos FDF](/pdf/es/python-net/import-fdf-data/)
- [Importar datos XFDF](/pdf/es/python-net/import-xfdf-data/)
- [Importar datos JSON](/pdf/es/python-net/import-json-data/)
- [Exportar a XML](/pdf/es/python-net/export-to-xml/)
- [Exportar a FDF](/pdf/es/python-net/export-to-fdf/)
- [Exportar a XFDF](/pdf/es/python-net/export-to-xfdf/)
- [Exportar a JSON](/pdf/es/python-net/export-to-json/)

## Importar datos de otro PDF

Este fragmento de código muestra cómo transferir datos de campos de formulario de un PDF fuente a un PDF de destino. Los datos del formulario se exportan a una secuencia XFDF del PDF fuente y luego se importan al PDF objetivo usando Aspose.PDF for Python via .NET.

1. Cree un objeto Form usando Aspose.PDF.
1. Vincule el documento PDF al Form.
1. Exportar datos del formulario del PDF de origen.
1. Importar datos del formulario al PDF de destino.
1. Guardar el PDF de destino actualizado.

```python
from io import StringIO
from os import path
import aspose.pdf as ap

path_infile = path.join(self.workdir_path, infile)
path_outfile = path.join(self.workdir_path, outfile)

# Create Form objects for the source and destination PDFs
form_source = ap.facades.Form()
form_dest = ap.facades.Form()

# Bind the PDF documents
form_source.bind_pdf(path_infile)
form_dest.bind_pdf(path_outfile)

# Transfer form data through an XFDF stream
with StringIO() as xfdf_stream:
    form_source.export_xfdf(xfdf_stream)
    form_dest.import_xfdf(xfdf_stream)
    form_dest.save()
```

## Extraer campos de formulario a JSON

Este método extrae los campos de formulario de un archivo de entrada y los exporta a un archivo JSON utilizando la funcionalidad incorporada `export_json()` método.

1. Cree un objeto Form usando Aspose.PDF.
1. Abra el archivo de salida en modo de escritura usando FileIO().
1. Exporte los campos del formulario al archivo JSON usando el método form.export_json().

```python
from io import FileIO
from os import path
import aspose.pdf as ap

path_infile = path.join(self.workdir_path, infile)
path_outfile = path.join(self.workdir_path, outfile)

form = ap.facades.Form(path_infile)
with FileIO(path_outfile, "w") as json_file:
    form.export_json(json_file, True)
```

## Extraer campos de formulario a documento JSON

1. Crear un objeto Form a partir del archivo de entrada.
1. Inicializar un diccionario vacío para almacenar los datos del campo de formulario.
1. Iterar a través de todos los campos del formulario y extraer sus valores.
1. Serializar el diccionario de datos del formulario a una cadena JSON con sangría de 4 espacios.
1. Escribir la cadena JSON en el archivo de salida con codificación UTF-8.

```python
import json
from os import path
import aspose.pdf as ap

path_infile = path.join(self.workdir_path, infile)
path_outfile = path.join(self.workdir_path, outfile)

form = ap.facades.Form(path_infile)
form_data = {}

# Get values from all fields
for form_field in form.field_names:
    form_data[form_field] = form.get_field(form_field)

# Serialize to JSON
json_string = json.dumps(form_data, indent=4)

with open(path_outfile, "w", encoding="utf-8") as json_file:
    json_file.write(json_string)
```
