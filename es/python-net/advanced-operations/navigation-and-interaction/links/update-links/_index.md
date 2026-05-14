---
title: Actualizar enlaces PDF en Python
linktitle: Actualizar enlaces
type: docs
weight: 20
url: /es/python-net/update-links/
description: Aprende cómo actualizar la apariencia y los destinos de los enlaces PDF en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo actualizar los enlaces en PDF
Abstract: La guía Aspose.PDF for Python via .NET sobre actualización de enlaces guía a los desarrolladores a través del proceso de modificar el comportamiento de los hipervínculos dentro de documentos PDF usando Python. Explica cómo cambiar los destinos de los enlaces para que apunten a páginas específicas, sitios web externos o incluso a otros archivos PDF. La documentación también cubre cómo ajustar la apariencia de las anotaciones de enlace, incluido el color del texto, y ofrece ejemplos de código prácticos para cada escenario. Ya sea que esté corrigiendo URL obsoletas o mejorando la navegación, este recurso ofrece un enfoque claro y eficiente para gestionar enlaces programáticamente.
---

## Actualizar color de texto de LinkAnnotation

Este ejemplo muestra cómo detectar todas las anotaciones de enlace en la primera página de un PDF usando Aspose.PDF for Python, y luego resaltar el texto cercano a cada enlace cambiando el color de su fuente a rojo. Utiliza TextFragmentAbsorber con un área ligeramente ampliada alrededor de cada rectángulo de enlace para encontrar y modificar el texto cercano.

Esto se puede usar para:

- Marcar visualmente los enlaces en un documento
- Mejorar la accesibilidad enfatizando el contenido enlazado
- Preprocesamiento de archivos PDF antes de la revisión o exportación

Para cada una de estas anotaciones de enlace, el script recupera su límite rectangular y amplía ligeramente esa región para incluir texto cercano, lo que permite una identificación visual más amplia. Luego aplica un TextFragmentAbsorber sobre esta área ampliada para extraer cualquier fragmento de texto situado dentro de ella. Estos fragmentos capturados se modifican cambiando su color de fuente a rojo, marcando efectivamente el texto circundante para enfatizar y revisar. Después de aplicar todas estas actualizaciones, el documento modificado se guarda en la ruta de salida, preservando las anotaciones resaltadas y su texto asociado.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_text_color(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        ta = ap.text.TextFragmentAbsorber()
        rect = la.rect
        rect.llx -= 2
        rect.lly -= 2
        rect.urx += 2
        rect.ury += 2
        ta.text_search_options = ap.text.TextSearchOptions(rect)
        ta.visit(document.pages[1])
        for textFragment in ta.text_fragments:
            textFragment.text_state.foreground_color = ap.Color.red

    document.save(outfile)
```

## Actualizar borde

El script se centra en la primera página del documento y filtra todas las anotaciones, seleccionando solo aquellas del tipo LINK—estas generalmente representan elementos interactivos, como hipervínculos o disparadores de navegación. Para cada una de estas anotaciones de enlace, el código las convierte al tipo LinkAnnotation y actualiza su propiedad de color a rojo, resaltándolas visualmente para que se destaquen del resto del contenido. Después de que todas las anotaciones de enlace hayan sido modificadas, el documento actualizado se guarda en la ubicación de salida definida, preservando el nuevo estilo.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_border(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        link_annotation = cast(ap.annotations.LinkAnnotation, la)
        link_annotation.color = ap.Color.red

    document.save(outfile)
```

## Actualizar destino web

Una vez que las rutas están en su lugar, el documento original se carga utilizando la biblioteca Aspose.PDF, lo que permite que su contenido sea accesible para su modificación. El script luego se centra en la primera página del documento, filtrando todas las anotaciones y seleccionando solo aquellas de tipo enlace, que normalmente representan áreas clicables o hipervínculos. Para evitar errores de tipo y garantizar un manejo seguro, cada anotación se verifica con is_assignable y luego se convierte al tipo LinkAnnotation apropiado. Si el enlace está asociado a una GoToURIAction, lo que significa que apunta a una dirección web, el script actualiza esa URI para redirigir a los usuarios ahttps://www.aspose.com". Finalmente, después de que se hayan aplicado todos los cambios deseados, el documento modificado se guarda en la ruta de salida especificada.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_web_destination(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        if is_assignable(la, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, la)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                action = cast(ap.annotations.GoToURIAction, annotation.action)
                action.uri = "https://www.aspose.com"
    document.save(outfile)
```

## Temas relacionados de enlaces

- [Trabajar con enlaces PDF en Python](/pdf/es/python-net/links/)
- [Crear enlaces PDF en Python](/pdf/es/python-net/create-links/)
- [Extraer enlaces PDF en Python](/pdf/es/python-net/extract-links/)