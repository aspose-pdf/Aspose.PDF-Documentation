---
title: Importar y exportar datos de formularios
linktitle: Importar y exportar datos de formularios
type: docs
weight: 80
url: /es/python-net/import-export-form-data/
description: Importe y exporte datos de campos AcroForm en formatos XML, FDF, XFDF y JSON usando Aspose.PDF for Python via .NET.
lastmod: "2026-05-08"
TechArticle: true
AlternativeHeadline: Técnicas de importación y exportación usando Aspose.PDF for Python via .NET.
Abstract: Esta compilación presenta un conjunto completo de técnicas de importación y exportación de datos de formularios usando Aspose.PDF for Python via .NET. Cubre flujos de trabajo para integrar formularios PDF con formatos de datos externos, incluidos XML, FDF, XFDF y JSON. Los usuarios pueden automatizar el llenado masivo de formularios importando datos estructurados en campos interactivos, o extraer los valores de los campos para análisis, copias de seguridad o integración con otros sistemas. Los ejemplos demuestran cómo vincular formularios PDF, transferir datos entre formatos y guardar documentos actualizados, lo que permite un procesamiento de documentos escalable y coherente en diversas aplicaciones.
---

Esta página muestra flujos de trabajo habituales para importar y exportar datos de AcroForm con Aspose.PDF for Python via .NET. Todas las operaciones utilizan la fachada [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/).

## Importar datos de campos de formulario desde XML

Utilice este enfoque para rellenar un formulario PDF con datos XML externos.

1. Crear un objeto `Form`.
1. Vincular el PDF de entrada.
1. Abre el archivo de datos XML.
1. Importar datos XML en el formulario.
1. Guarda el PDF actualizado.

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_xml(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_xml(f)

    form.save(output_file_name)
```

## Exportar datos de campos de formulario a XML

Este método exporta los valores de los campos de formulario de un documento PDF a XML.

1. Crear un objeto `Form`.
1. Vincular el PDF de entrada.
1. Abra el archivo de salida XML.
1. Exportar datos del formulario a XML.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_xml(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)
    with FileIO(output_file_name, "w") as f:
        form.export_xml(f)
```

## Importar datos de campos de formulario desde FDF

El método `import_data_from_fdf` importa datos de campos de formulario desde un archivo FDF (Formato de datos de formularios) a un formulario PDF.

1. Crear un objeto `Form`.
1. Vincular el PDF de entrada.
1. Importar los datos del formulario con `import_fdf()`.
1. Guarda el PDF actualizado.

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_fdf(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_fdf(f)
        form.save(output_file_name)
```

## Exportar datos de campos de formulario a FDF

Este ejemplo exporta los datos del formulario de un documento PDF a un archivo FDF.

1. Crear un objeto `Form`.
1. Vincular el documento PDF.
1. Exportar datos de formulario con `export_fdf()`.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_fdf(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_fdf(f)
```

## Importar datos de campos de formulario desde XFDF

Utilice este método para importar datos de campos de formulario desde un archivo XFDF (XML Forms Data Format) a un formulario PDF.

1. Crear un objeto `Form`.
1. Vincular el PDF de entrada.
1. Importar datos del formulario desde un archivo XFDF.
1. Guarda el PDF actualizado.

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_xfdf(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_xfdf(f)
        form.save(output_file_name)
```

## Exportar datos de campos de formulario a XFDF

Este código exporta datos de campos de formulario de un documento PDF a un archivo XFDF.

1. Crear un objeto `Form`.
1. Vincular el PDF de entrada.
1. Exportar datos del formulario a XFDF.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_xfdf(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_xfdf(f)
```

## Importar datos de otro PDF

Este ejemplo transfiere los datos de los campos de formulario de un PDF de origen a un PDF de destino exportando XFDF a un flujo en memoria e importándolo en el formulario objetivo.

1. Crear los objetos `Form` de origen y destino.
1. Vincular los PDF de origen y destino.
1. Exportar datos del formulario del PDF de origen.
1. Importar datos del formulario al PDF de destino.
1. Guarda el PDF de destino actualizado.

```python
from io import StringIO
import aspose.pdf as ap

def import_data_from_another_pdf(source_pdf_name, destination_pdf_name, output_file_name):
    form_source = ap.facades.Form()
    form_dest = ap.facades.Form()

    form_source.bind_pdf(source_pdf_name)
    form_dest.bind_pdf(destination_pdf_name)

    with StringIO() as xfdf_stream:
        form_source.export_xfdf(xfdf_stream)
        xfdf_stream.seek(0)
        form_dest.import_xfdf(xfdf_stream)

    form_dest.save(output_file_name)
```

## Extraer campos de formulario a JSON

Este método exporta los campos de formulario a un archivo JSON mediante `export_json()`.

1. Crear un objeto `Form`.
1. Abre el archivo de salida JSON.
1. Exportar campos de formulario usando `export_json()`.

```python
from io import FileIO
import aspose.pdf as ap

def extract_form_fields_to_json(input_file_name, output_file_name):
    form = ap.facades.Form(input_file_name)
    with FileIO(output_file_name, "w") as json_file:
        form.export_json(json_file, True)
```

## Extraer campos de formulario a documento JSON

Este ejemplo crea un documento JSON personalizado a partir de los nombres y valores de los campos de formulario.

1. Cree un objeto Form a partir del archivo de entrada.
1. Inicializar un diccionario vacío para almacenar los datos de los campos del formulario.
1. Itera a través de todos los campos del formulario y extrae sus valores.
1. Serializa el diccionario de datos del formulario a una cadena JSON con una sangría de 4 espacios.
1. Escribe la cadena JSON en el archivo de salida con codificación UTF-8.

```python
import json
import aspose.pdf as ap

def extract_form_fields_to_json_doc(input_file_name, output_file_name):
    form = ap.facades.Form(input_file_name)
    form_data = {}
    for field_name in form.field_names:
        form_data[field_name] = form.get_field(field_name)

    json_string = json.dumps(form_data, indent=4)

    with open(output_file_name, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## Temas relacionados (enfoque de fachadas)

- [Importar datos XML](/pdf/es/python-net/import-xml-data/)
- [Importar datos FDF](/pdf/es/python-net/import-fdf-data/)
- [Importar datos XFDF](/pdf/es/python-net/import-xfdf-data/)
- [Importar datos JSON](/pdf/es/python-net/import-json-data/)
- [Exportar a XML](/pdf/es/python-net/export-to-xml/)
- [Exportar a FDF](/pdf/es/python-net/export-to-fdf/)
- [Exportar a XFDF](/pdf/es/python-net/export-to-xfdf/)
- [Exportar a JSON](/pdf/es/python-net/export-to-json/)
