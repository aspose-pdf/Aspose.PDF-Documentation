---
title: Modificando AcroForm
linktitle: Modificando AcroForm
type: docs
weight: 45
url: /es/python-net/modifying-form/
description: Modificar campos AcroForm en documentos PDF utilizando Aspose.PDF for Python via .NET, incluyendo borrar texto, establecer límites, aplicar estilos a los campos y eliminar campos.
lastmod: "2026-04-28"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gestión y personalización de campos de formulario PDF
Abstract: Este artículo presenta ejemplos prácticos para modificar campos AcroForm utilizando Aspose.PDF for Python via .NET. Cubre la eliminación de texto del contenido de formulario Typewriter, el establecimiento y lectura de límites de caracteres en campos de texto, la aplicación de una apariencia de fuente personalizada y la eliminación de campos por nombre. Estos flujos de trabajo respaldan tareas comunes de mantenimiento de formularios en tuberías de procesamiento automático de PDF.
---

## Borrar texto en el formulario

Este ejemplo muestra cómo borrar texto de los campos de formulario Typewriter en un PDF usando Aspose.PDF for Python via .NET. Escanea la primera página del PDF, identifica formularios Typewriter, elimina su contenido y guarda el documento actualizado. Este enfoque es útil para restablecer o sanitizar los campos de formulario antes de redistribuir un PDF.

1. Cargue el documento PDF de entrada.
1. Acceda a los formularios en la primera página.
1. Iterar sobre cada formulario y comprobar si es un `Typewriter` formulario.
1. Utilice TextFragmentAbsorber para encontrar fragmentos de texto en el formulario.
1. Borre el texto de cada fragmento.
1. Guarde el PDF modificado en el archivo de salida.

```python
import aspose.pdf as ap


def clear_text_in_form(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    forms = document.pages[1].resources.forms

    for form in forms:
        if form.it == "Typewriter" and form.subtype == "Form":
            absorber = ap.text.TextFragmentAbsorber()
            absorber.visit(form)

            for fragment in absorber.text_fragments:
                fragment.text = ""

    document.save(output_file_name)
```

## Establecer límite de campo

Usar `set_field_limit(field, limit)` de `FormEditor` para definir el número máximo de caracteres permitidos en un campo de texto.

1. Cree un `FormEditor` objeto.
1. Vincula el PDF de entrada.
1. Establezca el límite del campo para un campo objetivo.
1. Guarda el PDF actualizado.

```python
import aspose.pdf as ap


def set_field_limit(input_file_name, output_file_name):
    form = ap.facades.FormEditor()
    form.bind_pdf(input_file_name)
    form.set_field_limit("First Name", 15)
    form.save(output_file_name)
```

## Obtener límite del campo

También puedes leer el límite de caracteres de un campo de texto.

1. Cargue el documento PDF.
1. Accede al campo de formulario objetivo.
1. Asegúrese de que el campo sea un `TextBoxField`.
1. Leer e imprimir `max_len`.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable


def get_field_limit(input_file_name):
    document = ap.Document(input_file_name)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        text_box_field = cast(ap.forms.TextBoxField, document.form[1])
        print(f"Limit: {text_box_field.max_len}")
```

## Establecer fuente personalizada para el campo del formulario

Este ejemplo establece una apariencia predeterminada personalizada para un campo de cuadro de texto, incluyendo la fuente, el tamaño y el color.

1. Cargue el documento PDF.
1. Acceda al campo objetivo y verifique su tipo.
1. Buscar la fuente en `FontRepository`.
1. Aplicar un nuevo `DefaultAppearance`.
1. Guarda el PDF actualizado.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable


def set_form_field_font(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        text_box_field = cast(ap.forms.TextBoxField, document.form[1])
        font = ap.text.FontRepository.find_font("Calibri")
        text_box_field.default_appearance = ap.annotations.DefaultAppearance(
            font, 10, ap.Color.black.to_rgb()
        )

    document.save(output_file_name)
```

## Eliminar campos en un formulario existente

Este código elimina un campo de formulario específico (por su nombre) de un documento PDF y guarda el archivo actualizado usando Aspose.PDF for Python via .NET.

1. Cargue el documento PDF.
1. Eliminar un campo de formulario por nombre.
1. Guarda el PDF actualizado.

```python
import aspose.pdf as ap


def delete_form_field(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    document.form.delete("First Name")
    document.save(output_file_name)
```

## Temas relacionados

- [Crear AcroForm](/pdf/es/python-net/create-form/)
- [Rellenar AcroForm](/pdf/es/python-net/fill-form/)
- [Extraer AcroForm](/pdf/es/python-net/extract-form/)
- [Importar y Exportar datos de Form](/pdf/es/python-net/import-export-form-data/)
