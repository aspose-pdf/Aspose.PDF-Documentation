---
title: Importar y Exportar datos del formulario
linktitle: Importar y Exportar datos del formulario
type: docs
weight: 80
url: /es/python-net/import-export-form-data/
description: Importar y exportar datos de campos AcroForm en formatos XML, FDF, XFDF y JSON usando Aspose.PDF for Python via .NET.
lastmod: "2026-04-28"
TechArticle: true
AlternativeHeadline: Técnicas de importación y exportación utilizando Aspose.PDF for Python via .NET.
Abstract: Esta compilación presenta un conjunto completo de técnicas de importación y exportación de datos de formularios utilizando Aspose.PDF for Python via .NET. Cubre flujos de trabajo para integrar formularios PDF con formatos de datos externos, incluidos XML, FDF, XFDF y JSON. Los usuarios pueden automatizar el llenado masivo de formularios importando datos estructurados en campos interactivos, o extraer valores de campos para análisis, copia de seguridad o integración con otros sistemas. Los ejemplos demuestran cómo vincular formularios PDF, transferir datos entre formatos y guardar documentos actualizados, lo que permite un procesamiento de documentos escalable y coherente en diversas aplicaciones.
---

Esta página muestra flujos de trabajo comunes para importar y exportar datos de AcroForm con Aspose.PDF for Python via .NET. Todas las operaciones usan el [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada.

## Importar datos de FormField desde XML

Utilice este enfoque para rellenar un formulario PDF a partir de datos XML externos.

1. Crear un `Form` objeto.
1. Vincular el PDF de entrada.
1. Abre el archivo de datos XML.
1. Importar datos XML al formulario.
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

## Exportar datos de FormField a XML

Este método exporta los valores de los campos de formulario de un documento PDF a XML.

1. Crear un `Form` objeto.
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

El `import_data_from_fdf` Método importa datos de campos de formulario de un archivo FDF (Formato de Datos de Formularios) en un formulario PDF.

1. Crear un `Form` objeto.
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

1. Crear un `Form` objeto.
1. Vincular el documento PDF.
1. Exportar datos del formulario con `export_fdf()`.

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

Utilice este método para importar datos de campos de formulario desde un archivo XFDF (Formato de datos de formularios XML) a un formulario PDF.

1. Crear un `Form` objeto.
1. Vincular el PDF de entrada.
1. Importar datos de formulario desde un archivo XFDF.
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

## Exportar datos de campo de formulario a XFDF

Este código exporta los datos de los campos de formulario de un documento PDF a un archivo XFDF.

1. Crear un `Form` objeto.
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

Este ejemplo transfiere datos de campos de formulario de un PDF de origen a un PDF de destino exportando XFDF a un flujo en memoria e importándolo al formulario de destino.

1. Crear origen y destino `Form` objetos.
1. Vincula los PDFs de origen y destino.
1. Exportar datos del formulario del PDF de origen.
1. Importar datos del formulario al PDF de destino.
1. Guarde el PDF de destino actualizado.

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

1. Crear un `Form` objeto.
1. Abra el archivo de salida JSON.
1. Exportar campos de formulario mediante `export_json()`.

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

1. Crear un objeto Form a partir del archivo de entrada.
1. Inicializa un diccionario vacío para almacenar los datos de los campos del formulario.
1. Iterar a través de todos los campos del formulario y extraer sus valores.
1. Serialice el diccionario de datos del formulario a una cadena JSON con una sangría de 4 espacios.
1. Escriba la cadena JSON en el archivo de salida con codificación UTF-8.

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

## Temas relacionados (enfoque de Fachadas)

- [Importar datos XML](/pdf/es/python-net/import-xml-data/)
- [Importar datos FDF](/pdf/es/python-net/import-fdf-data/)
- [Importar datos XFDF](/pdf/es/python-net/import-xfdf-data/)
- [Importar datos JSON](/pdf/es/python-net/import-json-data/)
- [Exportar a XML](/pdf/es/python-net/export-to-xml/)
- [Exportar a FDF](/pdf/es/python-net/export-to-fdf/)
- [Exportar a XFDF](/pdf/es/python-net/export-to-xfdf/)
- [Exportar a JSON](/pdf/es/python-net/export-to-json/)
