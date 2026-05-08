---
title: Publicar formularios en PDF mediante Python
linktitle: Publicar formularios
type: docs
weight: 75
url: /es/python-net/posting-form/
description: Agregar botones de envío y acciones de envío a los PDF AcroForms mediante Aspose.PDF for Python via .NET.
lastmod: "2026-04-28"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo agregar botones de envío y acciones de envío de formularios a un PDF usando Python
Abstract: Este artículo muestra dos enfoques para agregar funcionalidad de envío a formularios PDF mediante Aspose.PDF for Python via .NET. Puedes agregar un botón de envío prefabricado a través de FormEditor o crear un campo de botón personalizado con SubmitFormAction para un control avanzado. Estos patrones ayudan a integrar formularios PDF con puntos finales de procesamiento de formularios del lado del servidor.
---

## Agregar botón de envío con FormEditor

El siguiente fragmento de código muestra cómo agregar un botón de envío a un formulario PDF usando la clase FormEditor en Aspose.PDF for Python via .NET. El botón está configurado para enviar los datos del formulario a una URL especificada al hacer clic.

1. Cree un `FormEditor` objeto.
1. Agregar un botón de envío a la página objetivo.
1. Establecer la URL de envío y las coordenadas del botón.
1. Guarda el PDF actualizado.

```python
import aspose.pdf as ap

def add_submit_button(input_file_name, output_file_name):
    editor = ap.facades.FormEditor(input_file_name, output_file_name)
    editor.add_submit_btn(
        "submitbutton", 1, "Submit", "http://localhost/testing/show", 100, 450, 150, 475
    )
    editor.save()
```

## Agregar acción de envío personalizada

El siguiente fragmento de código explica cómo crear un botón de envío personalizado en un formulario PDF usando Aspose.PDF for Python via .NET. El botón está configurado para enviar los datos del formulario a una URL especificada al hacer clic.

1. Abra el PDF con ap.Document().
1. Crear una acción de envío.
1. Establezca la URL de destino y las banderas de envío.
1. Cree un campo de botón y vincule su acción de clic.
1. Agregue el botón al formulario.
1. Guarda el PDF actualizado.

```python
import aspose.pdf as ap

def add_submit_action(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    submit_action = ap.annotations.SubmitFormAction()
    submit_action.url = ap.FileSpecification("http://localhost:3000/submit")
    submit_action.flags = (
        ap.annotations.SubmitFormAction.EXPORT_FORMAT
        | ap.annotations.SubmitFormAction.SUBMIT_COORDINATES
    )

    rect = ap.Rectangle(10, 10, 100, 40)
    submit_button = ap.forms.ButtonField(document.pages[1], rect)
    submit_button.partial_name = "SubmitButton"
    submit_button.value = "Submit"
    submit_button.actions.on_release_mouse_btn = submit_action

    document.form.add(submit_button, 1)
    document.save(output_file_name)
```

## Temas relacionados

- [Crear AcroForm](/pdf/es/python-net/create-form/)
- [Rellenar AcroForm](/pdf/es/python-net/fill-form/)
- [Modificando AcroForm](/pdf/es/python-net/modifying-form/)
- [Importar y Exportar datos de Form](/pdf/es/python-net/import-export-form-data/)