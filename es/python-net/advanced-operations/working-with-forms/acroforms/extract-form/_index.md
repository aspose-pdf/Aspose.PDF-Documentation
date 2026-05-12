---
title: Extraer AcroForm - Extraer datos de Form de PDF en Python
linktitle: Extraer AcroForm
type: docs
weight: 30
url: /es/python-net/extract-form/
description: Extraer valores de los campos AcroForm en documentos PDF utilizando Aspose.PDF for Python via .NET.
lastmod: "2026-04-28"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo obtener datos de Form de PDF usando Python
Abstract: Este artículo muestra cómo extraer datos de los campos AcroForm en documentos PDF utilizando Aspose.PDF for Python via .NET. El ejemplo itera a través de los nombres de los campos Form, lee los valores mediante la fachada Form y devuelve un diccionario para el procesamiento posterior. Este flujo de trabajo es útil para la generación de informes, la validación y la integración con sistemas externos.
---

## Extraer datos de Form

### Obtener valores de todos los campos en un documento PDF

Para leer los valores de todos los campos en un documento PDF, itere a través de los nombres de los campos del formulario y recupere cada valor del [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) fachada.

Utilice los siguientes pasos:

1. Vincular el PDF de entrada a un `Form` objeto.
1. Iterar a través de `field_names`.
1. Lea cada valor con `get_field()`.
1. Almacenar valores en un diccionario.
1. Devolver o procesar los valores extraídos.

El siguiente fragmento de código Python muestra este enfoque.

```python
import aspose.pdf as ap


def get_values_from_all_fields(input_file_name):
    form = ap.facades.Form(input_file_name)

    form_values = {}
    for field_name in form.field_names:
        form_values[field_name] = form.get_field(field_name)

    print(form_values)
    return form_values
```

## Temas relacionados

- [Crear AcroForm](/pdf/es/python-net/create-form/)
- [Rellenar AcroForm](/pdf/es/python-net/fill-form/)
- [Importar y Exportar datos de Form](/pdf/es/python-net/import-export-form-data/)
- [Modificando AcroForm](/pdf/es/python-net/modifying-form/)