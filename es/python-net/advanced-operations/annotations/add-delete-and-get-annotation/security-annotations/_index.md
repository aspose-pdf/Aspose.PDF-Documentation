---
title: Anotaciones de seguridad usando Python
linktitle: Anotaciones de seguridad
type: docs
weight: 75
url: /es/python-net/security-annotations/
description: Aprenda cómo marcar texto para redactar, aplicar anotaciones de redacción y redactar áreas de imagen en archivos PDF usando Aspose.PDF for Python via .NET.
lastmod: "2026-04-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Redactar contenido sensible de PDF en Python con anotaciones de seguridad.
Abstract: Este artículo explica cómo trabajar con anotaciones de seguridad en documentos PDF usando Aspose.PDF for Python via .NET. Cubre el marcado de texto coincidente con anotaciones de redacción, la aplicación permanente de redacciones y la eliminación de áreas de imagen seleccionadas basándose en los rectángulos de ubicación de imagen detectados.
---

Este artículo muestra cómo utilizar anotaciones de seguridad en documentos PDF con Aspose.PDF for Python via .NET.

El script de ejemplo muestra tres flujos de trabajo comunes de redacción:

- marcar fragmentos de texto con anotaciones de redacción
- aplicar permanentemente las anotaciones de redacción existentes
- redactar un área de imagen detectada en una página

## Marcar redacción de texto

Este flujo de trabajo busca texto coincidente en el documento y coloca anotaciones de redacción sobre cada coincidencia. No elimina el contenido todavía; solo marca el texto para su posterior redacción.

### Abra el PDF y busque el texto objetivo

Crear un `TextFragmentAbsorber` para el término de búsqueda y habilitar las opciones de búsqueda de texto normales antes de escanear todas las páginas.

```python
document = ap.Document(infile)
text_fragment_absorber = ap.text.TextFragmentAbsorber(search_term)

text_search_options = ap.text.TextSearchOptions(True)
text_fragment_absorber.text_search_options = text_search_options
document.pages.accept(text_fragment_absorber)
```

### Crear anotaciones de redacción para cada coincidencia

Para cada fragmento de texto coincidente, crear un `RedactionAnnotation` usando el rectángulo del fragmento y configurando su apariencia visual.

```python
for text_fragment in text_fragment_absorber.text_fragments:
    page = text_fragment.page
    annotation_rectangle = text_fragment.rectangle
    redaction_annotation = ap.annotations.RedactionAnnotation(
        page, annotation_rectangle
    )
    redaction_annotation.fill_color = ap.Color.gray
    redaction_annotation.border_color = ap.Color.red
    redaction_annotation.color = ap.Color.white
    redaction_annotation.overlay_text = "REDACTED"
    redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
    redaction_annotation.repeat = True
    page.annotations.add(redaction_annotation, True)
```

### Guardar el PDF marcado

```python
document.save(outfile)
```

### Ejemplo completo

```python
def mark_text_redaction(infile, outfile, search_term):
    document = ap.Document(infile)
    text_fragment_absorber = ap.text.TextFragmentAbsorber(search_term)

    text_search_options = ap.text.TextSearchOptions(True)
    text_fragment_absorber.text_search_options = text_search_options
    document.pages.accept(text_fragment_absorber)

    for text_fragment in text_fragment_absorber.text_fragments:
        page = text_fragment.page
        annotation_rectangle = text_fragment.rectangle
        redaction_annotation = ap.annotations.RedactionAnnotation(
            page, annotation_rectangle
        )
        redaction_annotation.fill_color = ap.Color.gray
        redaction_annotation.border_color = ap.Color.red
        redaction_annotation.color = ap.Color.white
        redaction_annotation.overlay_text = "REDACTED"
        redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
        redaction_annotation.repeat = True
        page.annotations.add(redaction_annotation, True)

    document.save(outfile)
```



## Aplicar Redacción

Después de que se hayan añadido anotaciones de redactado, este flujo de trabajo las aplica permanentemente en la primera página. Una vez aplicadas, el contenido original se elimina de la salida del documento.

### Cargar el PDF y recopilar anotaciones de redacción

```python
document = ap.Document(infile)
redaction_annotations = [
    annotation
    for annotation in document.pages[1].annotations
    if annotation.annotation_type == ap.annotations.AnnotationType.REDACTION
]
```

### Aplicar cada anotación de redacción

La muestra verifica que cada anotación pueda ser tratada como una `RedactionAnnotation` antes de llamar `redact()`.

```python
for redaction_annotation in redaction_annotations:
    if is_assignable(redaction_annotation, ap.annotations.RedactionAnnotation):
        cast(ap.annotations.RedactionAnnotation, redaction_annotation).redact()
```

### Guardar el PDF redactado

```python
document.save(outfile)
```

### Ejemplo completo

```python
def apply_redaction(infile, outfile):
    document = ap.Document(infile)
    redaction_annotations = [
        annotation
        for annotation in document.pages[1].annotations
        if annotation.annotation_type == ap.annotations.AnnotationType.REDACTION
    ]

    for redaction_annotation in redaction_annotations:
        if is_assignable(redaction_annotation, ap.annotations.RedactionAnnotation):
            cast(ap.annotations.RedactionAnnotation, redaction_annotation).redact()

    document.save(outfile)
```



## Área de Redacción

Este ejemplo redacta un área de imagen detectada en lugar de texto. Escanea la página en busca de ubicaciones de imágenes, selecciona un rectángulo de ubicación y agrega una anotación de redacción sobre esa área.

### Abra el PDF y detecte la colocación de imágenes

Usar `ImagePlacementAbsorber` para encontrar las posiciones de la imagen en la primera página.

```python
document = ap.Document(infile)

image_placement_absorber = ap.ImagePlacementAbsorber()
page = document.pages[1]
page.accept(image_placement_absorber)
```

### Crear una anotación de redacción para el área de imagen seleccionada

El ejemplo utiliza la tercera ubicación de imagen detectada y aplica el mismo estilo de redacción utilizado en el ejemplo de marcación de texto.

```python
target_rect = image_placement_absorber.image_placements[2].rectangle
redaction_annotation = ap.annotations.RedactionAnnotation(page, target_rect)
redaction_annotation.fill_color = ap.Color.gray
redaction_annotation.border_color = ap.Color.red
redaction_annotation.color = ap.Color.white
redaction_annotation.overlay_text = "REDACTED"
redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
redaction_annotation.repeat = True
```

### Añadir la anotación y guardar el PDF

```python
page.annotations.add(redaction_annotation, True)
document.save(outfile)
```

### Ejemplo completo

```python
def redact_area(infile, outfile):
    document = ap.Document(infile)

    image_placement_absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(image_placement_absorber)

    target_rect = image_placement_absorber.image_placements[2].rectangle
    redaction_annotation = ap.annotations.RedactionAnnotation(page, target_rect)
    redaction_annotation.fill_color = ap.Color.gray
    redaction_annotation.border_color = ap.Color.red
    redaction_annotation.color = ap.Color.white
    redaction_annotation.overlay_text = "REDACTED"
    redaction_annotation.text_alignment = ap.HorizontalAlignment.CENTER
    redaction_annotation.repeat = True

    page.annotations.add(redaction_annotation, True)
    document.save(outfile)
```

## Temas relacionados

- [Importar y Exportar Anotaciones](/python-net/import-export-annotations/)
- [Anotaciones Interactivas](/python-net/interactive-annotations/)
- [Anotaciones de marcado](/python-net/markup-annotations/)
- [Anotaciones multimedia](/python-net/media-annotations/)
- [Anotaciones de forma](/python-net/shape-annotations/)
- [Anotaciones basadas en texto](/python-net/text-based-Annotations/)
- [Anotaciones de marca de agua](/python-net/watermark-annotations/)
