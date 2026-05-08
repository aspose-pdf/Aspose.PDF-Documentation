---
title: Eliminar formularios de PDF en Python
linktitle: Eliminar formularios
type: docs
weight: 70
url: /es/python-net/remove-form/
description: Eliminar objetos de formulario de las páginas PDF utilizando Aspose.PDF for Python via .NET, incluyendo una limpieza completa y eliminación dirigida.
lastmod: "2026-04-28"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar formularios de PDF con Aspose.PDF for Python via .NET
Abstract: Este artículo presenta dos enfoques para eliminar elementos de formulario de documentos PDF mediante Aspose.PDF for Python via .NET. El primer método elimina todos los objetos de formulario de una página seleccionada, mientras que el segundo método elimina solo los recursos de formulario Typewriter coincidentes. Estos ejemplos ayudan con la limpieza de formularios, la preparación de plantillas y los flujos de trabajo de normalización de documentos.
---

## Eliminar todos los formularios de una página

Este código elimina todos los objetos de formulario de la página especificada por `page_num` y guarda el documento actualizado.

1. Cargue el documento PDF.
1. Acceder a los recursos de la página.
1. Borrar objetos de formulario.
1. Guardar el documento actualizado.

```python
import aspose.pdf as ap

def remove_all_forms(input_file_name, page_num, output_file_name):
    document = ap.Document(input_file_name)
    forms = document.pages[page_num].resources.forms
    forms.clear()
    document.save(output_file_name)
```

## Eliminar un tipo de formulario específico

El siguiente ejemplo recorre los objetos de formulario en una página PDF dada, identifica las anotaciones de formulario de máquina de escribir, las elimina y luego guarda el PDF actualizado usando Aspose.PDF for Python via .NET.

1. Cargue el documento PDF.
1. Acceder a los formularios de la página.
1. Iterar sobre los formularios.
1. Comprobar formularios de máquina de escribir.
1. Eliminar el formulario coincidente.
1. Guardar el documento actualizado.

```python
import aspose.pdf as ap

def remove_specified_form(input_file_name, page_num, output_file_name):
    document = ap.Document(input_file_name)
    forms = document.pages[page_num].resources.forms
    for form in forms:
        if form.it == "Typewriter" and form.subtype == "Form":
            name = forms.get_form_name(form)
            forms.delete(name)
    document.save(output_file_name)
```

## Temas relacionados

- [Crear AcroForm](/pdf/es/python-net/create-form/)
- [Rellenar AcroForm](/pdf/es/python-net/fill-form/)
- [Modificando AcroForm](/pdf/es/python-net/modifying-form/)
- [Publicar formularios](/pdf/es/python-net/posting-form/)
