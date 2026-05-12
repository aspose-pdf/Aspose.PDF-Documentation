---
title: Anotaciones de marcado usando Python
linktitle: Anotaciones de marcado
type: docs
weight: 30
url: /es/python-net/markup-annotations/
description: Aprende cómo agregar, leer y eliminar texto, cursor y reemplazar anotaciones en documentos PDF usando Aspose.PDF for Python via .NET.
lastmod: "2026-04-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Trabaja con anotaciones de marcado en archivos PDF usando Python.
Abstract: Este artículo explica cómo crear, inspeccionar y eliminar anotaciones de marcado en documentos PDF utilizando Aspose.PDF for Python via .NET. Cubre anotaciones de texto, anotaciones de cursor y anotaciones de sustitución, con cada flujo de trabajo dividido en pasos pequeños y ejemplos de código.
---

Este artículo muestra cómo trabajar con anotaciones de marcado en documentos PDF utilizando Aspose.PDF for Python via .NET.

El script de ejemplo muestra tres flujos de trabajo comunes de anotaciones:

- anotaciones de texto para comentarios de estilo nota
- anotaciones de caret para marcadores de inserción
- reemplazar anotaciones para el marcado de reemplazo de texto

## Anotaciones de texto

### Agregar anotaciones de texto

Este ejemplo crea una anotación de texto en la primera página y la vincula a una ventana emergente. Las anotaciones de texto son útiles para comentarios al estilo de notas adhesivas en flujos de trabajo de revisión.

#### Abra el PDF de origen

```python
document = ap.Document(infile)
```

#### Crear y configurar la anotación de texto

Defina el rectángulo de anotación y establezca su título, asunto, contenido, banderas de visualización, color e ícono.

```python
text_annotation = ap.annotations.TextAnnotation(
    document.pages[1],
    ap.Rectangle(299.988, 613.664, 428.708, 680.769, True),
)
text_annotation.title = "Aspose User"
text_annotation.subject = "Sticky Note"
text_annotation.contents = (
    "This is a text annotation added by Aspose.PDF for Python via .NET"
)
text_annotation.flags = ap.annotations.AnnotationFlags.PRINT
text_annotation.color = ap.Color.blue
text_annotation.icon = ap.annotations.TextIcon.HELP
```

#### Crear la anotación emergente

Crear una ventana emergente y conectarla a la anotación de texto.

```python
popup = ap.annotations.PopupAnnotation(
    document.pages[1],
    ap.Rectangle(428.708, 613.664, 528.708, 713.664, True),
)
popup.open = True

text_annotation.popup = popup
```

#### Añadir la anotación y guardar el PDF

```python
document.pages[1].annotations.add(text_annotation, consider_rotation=False)
document.save(outfile)
```

#### Ejemplo completo

```python
def text_annotation_add(infile, outfile):
    document = ap.Document(infile)

    text_annotation = ap.annotations.TextAnnotation(
        document.pages[1],
        ap.Rectangle(299.988, 613.664, 428.708, 680.769, True),
    )
    text_annotation.title = "Aspose User"
    text_annotation.subject = "Sticky Note"
    text_annotation.contents = (
        "This is a text annotation added by Aspose.PDF for Python via .NET"
    )
    text_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    text_annotation.color = ap.Color.blue
    text_annotation.icon = ap.annotations.TextIcon.HELP

    popup = ap.annotations.PopupAnnotation(
        document.pages[1],
        ap.Rectangle(428.708, 613.664, 528.708, 713.664, True),
    )
    popup.open = True

    text_annotation.popup = popup

    document.pages[1].annotations.add(text_annotation, consider_rotation=False)
    document.save(outfile)
```

### Obtener anotaciones de texto

Para inspeccionar las anotaciones de texto existentes, filtre la colección de anotaciones en la primera página y mantenga solo los elementos cuyo tipo sea `TEXT`.

#### Cargar el documento y recopilar anotaciones de texto

```python
document = ap.Document(infile)
text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
]
```

#### Imprimir los rectángulos de anotación

```python
for annotation in text_annotations:
    print(annotation.rect)
```

#### Ejemplo completo

```python
def text_annotation_get(infile, outfile):
    document = ap.Document(infile)
    text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
    ]

    for annotation in text_annotations:
        print(annotation.rect)
```

### Eliminar anotaciones de texto

Este flujo de trabajo elimina todas las anotaciones de texto de la primera página y guarda el PDF modificado.

#### Buscar anotaciones de texto para eliminar

```python
document = ap.Document(infile)
text_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
]
```

#### Eliminar las anotaciones y guardar el archivo

```python
for annotation in text_annotations:
    document.pages[1].annotations.delete(annotation)

document.save(outfile)
```

#### Ejemplo completo

```python
def text_annotation_delete(infile, outfile):
    document = ap.Document(infile)
    text_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.TEXT
    ]

    for annotation in text_annotations:
        document.pages[1].annotations.delete(annotation)

    document.save(outfile)
```

## Anotaciones de cursor

### Agregar anotaciones de cursor

Las anotaciones caret se utilizan para marcar puntos de inserción en escenarios de revisión. Este ejemplo agrega una anotación caret con una nota emergente adjunta.

#### Abra el documento y obtenga la página objetivo

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### Crear y configurar la anotación caret

```python
caret_annotation = ap.annotations.CaretAnnotation(
    page, ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
)
caret_annotation.title = "Aspose User"
caret_annotation.subject = "Inserted text 1"
caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
caret_annotation.color = ap.Color.blue
```

#### Adjunte la ventana emergente y guarde el documento

```python
caret_annotation.popup = ap.annotations.PopupAnnotation(
    page, ap.Rectangle(310, 713, 410, 730, True)
)
page.annotations.append(caret_annotation)

document.save(outfile)
```

#### Ejemplo completo

```python
def caret_annotations_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotation = ap.annotations.CaretAnnotation(
        page, ap.Rectangle(299.988, 713.664, 308.708, 720.769, True)
    )
    caret_annotation.title = "Aspose User"
    caret_annotation.subject = "Inserted text 1"
    caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    caret_annotation.color = ap.Color.blue
    caret_annotation.popup = ap.annotations.PopupAnnotation(
        page, ap.Rectangle(310, 713, 410, 730, True)
    )
    page.annotations.append(caret_annotation)

    document.save(outfile)
```

### Obtener anotaciones de cursor

Para inspeccionar las anotaciones caret, itere a través de las anotaciones de la página y filtre por el `CARET` tipo de anotación.

#### Cargar el documento y la página

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### Imprimir rectángulos de anotación de caret

```python
for annot in page.annotations:
    if annot.annotation_type == ap.annotations.AnnotationType.CARET:
        print(annot.rect)
```

#### Ejemplo completo

```python
def caret_annotations_get(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    for annot in page.annotations:
        if annot.annotation_type == ap.annotations.AnnotationType.CARET:
            print(annot.rect)
```

### Eliminar anotaciones de caret

Este flujo de trabajo recopila primero las anotaciones de caret, las elimina una por una y luego guarda el archivo actualizado.

#### Cargar el documento y recopilar las anotaciones de cursor

```python
document = ap.Document(infile)
page = document.pages[1]

caret_annotations = [
    annot
    for annot in page.annotations
    if annot.annotation_type == ap.annotations.AnnotationType.CARET
]
```

#### Elimina las anotaciones y guarda el documento

```python
for annot in caret_annotations:
    page.annotations.delete(annot)

document.save(outfile)
```

#### Ejemplo completo

```python
def caret_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotations = [
        annot
        for annot in page.annotations
        if annot.annotation_type == ap.annotations.AnnotationType.CARET
    ]

    for annot in caret_annotations:
        page.annotations.delete(annot)

    document.save(outfile)
```

## Reemplazar anotaciones

### Agregar Reemplazar Anotaciones

Las anotaciones de reemplazo combinan una anotación de caret y una anotación de tachado agrupada. Este patrón marca el texto que debe ser reemplazado y enlaza la nota de reemplazo con el contenido tachado.

#### Abre el documento y obtén la página

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### Crear la anotación caret para texto de reemplazo

```python
caret_annotation = ap.annotations.CaretAnnotation(
    page, ap.Rectangle(361.246, 727.908, 370.081, 735.107, True)
)
caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
caret_annotation.subject = "Inserted text 2"
caret_annotation.title = "Aspose User"
caret_annotation.color = ap.Color.blue
caret_annotation.popup = ap.annotations.PopupAnnotation(
    page, ap.Rectangle(310, 713, 410, 730, True)
)
```

#### Crear la anotación tachada agrupada

Definir el área tachada, asignar los puntos cuádruples y vincularlo a la anotación caret a través de `in_reply_to` y `reply_type`.

```python
strikeout_annotation = ap.annotations.StrikeOutAnnotation(
    page, ap.Rectangle(318.407, 727.826, 368.916, 740.098, True)
)
strikeout_annotation.color = ap.Color.blue
strikeout_annotation.quad_points = [
    ap.Point(321.66, 739.416),
    ap.Point(365.664, 739.416),
    ap.Point(321.66, 728.508),
    ap.Point(365.664, 728.508),
]
strikeout_annotation.subject = "Cross-out"
strikeout_annotation.in_reply_to = caret_annotation
strikeout_annotation.reply_type = ap.annotations.ReplyType.GROUP
``` 

#### Añade ambas anotaciones y guarda el PDF

```python
page.annotations.append(caret_annotation)
page.annotations.append(strikeout_annotation)

document.save(outfile)
```

#### Ejemplo completo

```python
def replace_annotations_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    caret_annotation = ap.annotations.CaretAnnotation(
        page, ap.Rectangle(361.246, 727.908, 370.081, 735.107, True)
    )
    caret_annotation.flags = ap.annotations.AnnotationFlags.PRINT
    caret_annotation.subject = "Inserted text 2"
    caret_annotation.title = "Aspose User"
    caret_annotation.color = ap.Color.blue
    caret_annotation.popup = ap.annotations.PopupAnnotation(
        page, ap.Rectangle(310, 713, 410, 730, True)
    )

    strikeout_annotation = ap.annotations.StrikeOutAnnotation(
        page, ap.Rectangle(318.407, 727.826, 368.916, 740.098, True)
    )
    strikeout_annotation.color = ap.Color.blue
    strikeout_annotation.quad_points = [
        ap.Point(321.66, 739.416),
        ap.Point(365.664, 739.416),
        ap.Point(321.66, 728.508),
        ap.Point(365.664, 728.508),
    ]
    strikeout_annotation.subject = "Cross-out"
    strikeout_annotation.in_reply_to = caret_annotation
    strikeout_annotation.reply_type = ap.annotations.ReplyType.GROUP

    page.annotations.append(caret_annotation)
    page.annotations.append(strikeout_annotation)

    document.save(outfile)
```

### Obtener Reemplazar Anotaciones

Para identificar anotaciones de reemplazo, encuentre anotaciones de tachado que estén agrupadas como respuestas a otra anotación. El ejemplo convierte cada anotación de tachado antes de comprobar sus campos de relación.

#### Cargue el documento y recorra las anotaciones

```python
document = ap.Document(infile)
page = document.pages[1]
```

#### Filtrar anotaciones de tachado agrupadas

```python
for annot in page.annotations:
    if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT:
        sa = cast(ap.annotations.StrikeOutAnnotation, annot)
        if (
            sa.in_reply_to is not None
            and sa.reply_type == ap.annotations.ReplyType.GROUP
        ):
            print(f"Replace annotation rect: {sa.rect}")
```

#### Ejemplo completo

```python
def replace_annotations_get(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    for annot in page.annotations:
        if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT:
            sa = cast(ap.annotations.StrikeOutAnnotation, annot)
            if (
                sa.in_reply_to is not None
                and sa.reply_type == ap.annotations.ReplyType.GROUP
            ):
                print(f"Replace annotation rect: {sa.rect}")
```

### Eliminar Reemplazar Anotaciones

Este flujo de trabajo recopila anotaciones de tachado utilizadas para reemplazar el marcado, las elimina de la página y guarda el PDF de salida.

#### Cargar el documento y recopilar anotaciones de reemplazo

```python
document = ap.Document(infile)
page = document.pages[1]

replace_annotations = [
    cast(ap.annotations.StrikeOutAnnotation, annot)
    for annot in page.annotations
    if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
]
```

#### Elimina las anotaciones y guarda el documento

```python
for annot in replace_annotations:
    page.annotations.delete(annot)

document.save(outfile)
```

#### Ejemplo completo

```python
def replace_annotations_delete(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    replace_annotations = [
        cast(ap.annotations.StrikeOutAnnotation, annot)
        for annot in page.annotations
        if annot.annotation_type == ap.annotations.AnnotationType.STRIKE_OUT
    ]

    for annot in replace_annotations:
        page.annotations.delete(annot)

    document.save(outfile)
```
