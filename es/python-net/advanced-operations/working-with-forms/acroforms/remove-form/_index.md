---
title: Eliminar formularios de PDF en Python
linktitle: Eliminar formularios
type: docs
weight: 70
url: /es/python-net/remove-form/
description: Eliminar texto basado en subtipo/formulario con la biblioteca Aspose.PDF para Python a través de .NET. Eliminar todos los formularios del PDF.
lastmod: "2025-09-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar formularios de PDF con Aspose.PDF para Python a través de .NET
Abstract: Este documento presenta dos enfoques basados en Python para eliminar elementos de formulario de archivos PDF utilizando Aspose.PDF para Python a través de .NET. El primer método muestra cómo limpiar todos los objetos de formulario de una página específica accediendo a su diccionario de recursos e invocando el método clear() en la colección de formularios. El segundo método ofrece una solución más específica al iterar sobre las anotaciones de formulario, identificar formularios tipo máquina de escribir y eliminarlos selectivamente según sus atributos. Ambas técnicas concluyen guardando el PDF actualizado en una ruta de salida especificada, ofreciendo opciones flexibles para la limpieza de formularios y el refinamiento de documentos en flujos de trabajo automatizados.
---

## Eliminar todos los formularios del PDF

Este código elimina todos los elementos de formulario de la primera página de un documento PDF y luego guarda el documento modificado en la ruta de salida especificada.

1. Cargar el documento PDF.
1. Acceder a los recursos de la página.
1. Limpiar los objetos de formulario.
1. Guardar el documento actualizado.

```python

    import aspose.pdf as ap
    import os

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(data_dir, infile)
    path_outfile = os.path.join(data_dir, outfile)

    document = ap.Document(path_infile)
    forms = document.pages[page_num].resources.forms
    forms.clear()
    document.save(path_outfile)
```

## Eliminar formulario especificado

El siguiente ejemplo itera a través de los objetos de formulario en una página PDF dada, identifica anotaciones de formulario tipo máquina de escribir, los elimina y luego guarda el PDF actualizado usando Aspose.PDF para Python a través de .NET.

1. Cargar el documento PDF.
1. Acceder a los formularios de la página.
1. Iterar sobre los formularios.
1. Verificar formularios tipo máquina de escribir.
1. Eliminar el formulario coincidente.
1. Guardar el documento actualizado.

```python

    import aspose.pdf as ap
    import os

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    document = ap.Document(path_infile)
    forms = document.pages[page_num].resources.forms
    for form in forms:
        if (form.it == "Typewriter" and form.subtype == "Form"):
            name = forms.get_form_name(form)
            forms.delete(name)
    document.save(path_outfile)
```
