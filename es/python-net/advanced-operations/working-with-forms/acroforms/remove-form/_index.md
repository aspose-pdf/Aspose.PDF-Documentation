---
title: Eliminar formularios de PDF en Python
linktitle: Eliminar formularios
type: docs
weight: 70
url: /es/python-net/remove-form/
description: Elimine texto basado en subtipo/Form con Aspose.PDF para Python a traves de .NET. Tambien puede eliminar todos los formularios de un PDF.
lastmod: "2025-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar formularios PDF con Aspose.PDF para Python a traves de .NET
Abstract: Este documento presenta dos enfoques basados en Python para eliminar elementos de Form de archivos PDF utilizando Aspose.PDF for Python via .NET. El primer método muestra cómo borrar todos los objetos de Form de una página específica accediendo a su diccionario de recursos e invocando el método clear() en la colección de Forms. El segundo método ofrece una solución más específica al iterar a través de anotaciones de Form, identificar Forms de estilo máquina de escribir y eliminarlos de forma selectiva según sus atributos. Ambas técnicas concluyen guardando el PDF actualizado en una ruta de salida especificada, ofreciendo opciones flexibles para la limpieza de Forms y el refinamiento de documentos en flujos de trabajo automatizados.
---

## Eliminar todos los formularios de PDF

Este código elimina todos los elementos del formulario de la primera página de un documento PDF y luego guarda el documento modificado en la ruta de salida especificada.

1. Cargar el documento PDF.
1. Acceder a los recursos de la página.
1. Borrar objetos del formulario.
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

El siguiente ejemplo recorre los objetos de formulario en una página PDF dada, identifica las anotaciones de formulario de máquina de escribir, las elimina y luego guarda el PDF actualizado usando Aspose.PDF for Python via .NET.

1. Cargar el documento PDF.
1. Acceder a los formularios de la página.
1. Iterar sobre formularios.
1. Comprobar formularios de máquina de escribir.
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
    if form.it == "Typewriter" and form.subtype == "Form":
        name = forms.get_form_name(form)
        forms.delete(name)
document.save(path_outfile)
```
