---
title: Rellenar AcroForm - Rellenar formulario PDF usando Python
linktitle: Rellenar AcroForm
type: docs
weight: 20
url: /es/python-net/fill-form/
description: Rellenar campos AcroForm en un documento PDF mediante Aspose.PDF for Python via .NET.
lastmod: "2026-04-28"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo rellenar un campo de formulario en PDF usando Python
Abstract: Este artículo explica cómo rellenar campos AcroForm en un documento PDF mediante Aspose.PDF for Python via .NET. El ejemplo utiliza la fachada Form, asigna nombres de campos a nuevos valores en un diccionario, actualiza los campos coincidentes y guarda el PDF de salida. Este enfoque es útil para flujos de trabajo automatizados de completado de documentos y procesamiento masivo de formularios.
---

## Rellenar campo de formulario en un documento PDF

El siguiente ejemplo rellena varios campos en un formulario PDF existente mediante el [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada.

Utilice los siguientes pasos:

1. Crea un diccionario con nombres de campo y valores.
1. Vincula el PDF de entrada a un objeto Form.
1. Itera a través de los campos de formulario disponibles.
1. Rellena los campos que existen en el diccionario.
1. Guarda el PDF actualizado.

```python
import aspose.pdf as ap

def fill_form(input_file_name, output_file_name):
    new_field_values = {
        "First Name": "Alexander_New",
        "Last Name": "Greenfield_New",
        "City": "Yellowtown_New",
        "Country": "Redland_New",
    }

    form = ap.facades.Form(input_file_name)

    for field_name in form.field_names:
        if field_name in new_field_values:
            form.fill_field(field_name, new_field_values[field_name])

    form.save(output_file_name)
```

## Temas relacionados

- [Crear AcroForm](/pdf/es/python-net/create-form/)
- [Extraer AcroForm](/pdf/es/python-net/extract-form/)
- [Importar y Exportar datos de Form](/pdf/es/python-net/import-export-form-data/)