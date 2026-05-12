---
title: Anotaciones de marca de agua usando Python
linktitle: Anotaciones de marca de agua
type: docs
weight: 70
url: /es/python-net/watermark-annotations/
description: Aprenda cómo agregar, inspeccionar y eliminar anotaciones de marca de agua en documentos PDF usando Aspose.PDF for Python via .NET.
lastmod: "2026-04-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Trabaje con anotaciones de marca de agua en archivos PDF usando Python.
Abstract: Este artículo explica cómo crear, leer y eliminar anotaciones de marca de agua en documentos PDF usando Aspose.PDF for Python via .NET. Cubre la adición de una anotación de marca de agua de texto con estado de texto personalizado y opacidad, la inspección de anotaciones de marca de agua existentes y la eliminación de anotaciones de marca de agua de una página PDF.
---

Este artículo muestra cómo trabajar con anotaciones de marca de agua en documentos PDF usando Aspose.PDF for Python via .NET.

El script de ejemplo muestra tres flujos de trabajo comunes:

- agregar una anotación de marca de agua
- obtener rectángulos de anotación de marca de agua
- eliminar anotaciones de marca de agua

## Agregar anotación de marca de agua

Este ejemplo agrega una anotación de marca de agua a la primera página de un documento PDF. La marca de agua usa un estado de texto para controlar la configuración de la fuente y aplica una opacidad personalizada para lograr una apariencia semitransparente.

### Abra el PDF y obtenga la página objetivo

```python
document = ap.Document(infile)
page = document.pages[1]
```

### Crear la anotación de marca de agua

Define el rectángulo de anotación y añádelo a la colección de anotaciones de la página.

```python
watermark_annotation = ap.annotations.WatermarkAnnotation(
    page,
    ap.Rectangle(100, 100, 400, 200, True),
)

page.annotations.append(watermark_annotation)
```

### Configurar la apariencia del texto

Crear un `TextState` objeto para controlar el color del texto, el tamaño de fuente y la familia de fuentes.

```python
text_state = ap.text.TextState()
text_state.foreground_color = ap.Color.blue
text_state.font_size = 25
text_state.font = ap.text.FontRepository.find_font("Arial")
```

### Establecer opacidad y texto de marca de agua

El ejemplo utiliza una opacidad del 50% y escribe tres líneas de texto en la anotación de marca de agua.

```python
watermark_annotation.opacity = 0.5
watermark_annotation.set_text_and_state(["HELLO", "Line 1", "Line 2"], text_state)
```

### Guardar el PDF

```python
document.save(outfile)
```

### Ejemplo completo

```python
def watermark_add(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    watermark_annotation = ap.annotations.WatermarkAnnotation(
        page,
        ap.Rectangle(100, 100, 400, 200, True),
    )

    page.annotations.append(watermark_annotation)

    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.blue
    text_state.font_size = 25
    text_state.font = ap.text.FontRepository.find_font("Arial")

    watermark_annotation.opacity = 0.5
    watermark_annotation.set_text_and_state(["HELLO", "Line 1", "Line 2"], text_state)

    document.save(outfile)
```

## Obtener anotación de marca de agua

Para inspeccionar las anotaciones de marca de agua existentes, filtre las anotaciones de la primera página por la `WATERMARK` escriba e imprima sus rectángulos.

### Cargar el documento y recopilar anotaciones de marca de agua

```python
document = ap.Document(infile)
watermark_annotations = [
    a
    for a in document.pages[1].annotations
    if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
]
```

### Imprimir los rectángulos de anotación

```python
for watermark_annotation in watermark_annotations:
    print(watermark_annotation.rect)
```

### Ejemplo completo

```python
def watermark_get(infile, outfile):
    document = ap.Document(infile)
    watermark_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
    ]

    for watermark_annotation in watermark_annotations:
        print(watermark_annotation.rect)
```

## Eliminar anotación de marca de agua

Este flujo de trabajo elimina todas las anotaciones de marca de agua de la primera página y guarda el PDF actualizado.

### Buscar anotaciones de marca de agua para eliminar

```python
document = ap.Document(infile)
watermark_annotations = [
    a
    for a in document.pages[1].annotations
    if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
]
```

### Eliminar las anotaciones y guardar el PDF

```python
for watermark_annotation in watermark_annotations:
    document.pages[1].annotations.delete(watermark_annotation)

document.save(outfile)
```

### Ejemplo completo

```python
def watermark_delete(infile, outfile):
    document = ap.Document(infile)
    watermark_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.WATERMARK
    ]

    for watermark_annotation in watermark_annotations:
        document.pages[1].annotations.delete(watermark_annotation)

    document.save(outfile)
```

## Temas relacionados

- [Importar y Exportar Anotaciones](/python-net/import-export-annotations/)
- [Anotaciones Interactivas](/python-net/interactive-annotations/)
- [Anotaciones de marcado](/python-net/markup-annotations/)
- [Anotaciones multimedia](/python-net/media-annotations/)
- [Anotaciones de seguridad](/python-net/security-annotations/)
- [Anotaciones de forma](/python-net/shape-annotations/)
- [Anotaciones basadas en texto](/python-net/text-based-Annotations/)
