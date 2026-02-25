---
title: Anotaciones y Texto Especial usando Python
linktitle: Anotaciones y Texto Especial
type: docs
weight: 40
url: /es/python-net/annotation-and-special-text/
description: Esta sección contiene artículos sobre anotación y extracción de Texto especial de documentos PDF usando Aspose.PDF en Python.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Extraer Texto de Anotaciones de Sello

La biblioteca Aspose.PDF para Python le permite extraer texto de una anotación de sello (específicamente una StampAnnotation) en una página PDF.

1. Abrir el documento.
1. Acceder a la anotación de sello desde la colección de anotaciones de la página.
1. Obtener el flujo de apariencia del sello (XForm).
1. Utilizar un 'TextAbsorber' para extraer el texto incrustado de esa apariencia.

```python

import os
import aspose.pdf as ap

def extract_text_from_stamp(infile, page_number, annotation_index, outfile):
    """
    Extracts text from a stamp annotation on a given page in a PDF document.
    Args:
        infile (str): Path to the input PDF file.
        page_number (int): 1-based index of the page containing the stamp.
        annotation_index (int): 1-based index of the annotation in that page.
        outfile (str): Path to the output text file where extracted text will be saved.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[page_number]
        annot = page.annotations[annotation_index]
        # Ensure it's a StampAnnotation
        if isinstance(annot, ap.annotations.StampAnnotation):
            # Get normal appearance XForm of the stamp
            xform = annot.appearance["N"]
            absorber = ap.text.TextAbsorber()
            absorber.visit(xform)
            extracted = absorber.text
            with open(outfile, "w", encoding="utf-8") as f:
                f.write(extracted)
    finally:
        document.close()
```

## Extraer Texto Resaltado

El estándar PDF permite resaltar partes del texto en un documento. Para extraer ese contenido resaltado, siga estos pasos:

1. Importar `aspose.pdf as ap` y cualquier ayuda que use (`is_assignable`, `cast`).
2. Llamar a `ap.Document(infile)` para abrir el PDF.
3. Seleccionar la página deseada con `document.pages` (la colección de páginas comienza en 1).
4. Recorrer `page.annotations` para examinar cada anotación en esa página.
5. Filtrar anotaciones para que solo se procesen las anotaciones de resaltado.
6. Convertir la anotación a `HighlightAnnotation` y llamar a `get_marked_text()` para leer el texto resaltado.
7. Imprimir o manejar de otra forma el texto devuelto.

```python
def extract_highlight_text(infile):
    """
    Extract text from highlight annotations.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_highlight_text("sample.pdf")

    Note:
        Prints marked text from each highlight annotation on first page.
    """
    document = ap.Document(infile)
    page = document.pages[1]

    for annotation in page.annotations:
        if is_assignable(annotation, ap.annotations.HighlightAnnotation):
            highlight_annotation = cast(ap.annotations.HighlightAnnotation, annotation)
            print(highlight_annotation.get_marked_text())
```

## Extraer Texto de Superíndices y Subíndices

**Subíndices y Superíndices** se usan con mayor frecuencia en fórmulas, expresiones matemáticas y especificaciones de compuestos químicos. Es difícil editarlos cuando pueden haber muchos en el mismo fragmento de texto.
En una de las últimas versiones, la biblioteca **Aspose.PDF for Python via .NET** agregó soporte para extraer texto de Superíndices y Subíndices de PDF. Extraiga todo el texto (incluyendo superíndices y subíndices) de una página específica de un documento PDF usando 'TextFragmentAbsorber'.

1. Cargar el documento PDF.
1. Instanciar un 'TextFragmentAbsorber()', que soporta la detección de texto en superíndice/subíndice según las capacidades de la versión.
1. Llamar a 'document.pages[page_number].accept(absorber)' para escanear solo la página indicada.
1. Recuperar el texto extraído mediante 'absorber.text'.
1. Escribir el texto en el archivo de salida usando I/O de archivo estándar.
1. Cerrar el documento para liberar recursos.

```python

import os
import aspose.pdf as ap

def extract_super_sub_text(infile, outfile, page_number=1):
    """
    Extract text (including superscript/subscript) from a specified page of a PDF and write to a text file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1‑based index of the page to extract.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextFragmentAbsorber()
        # Accept only the specific page for extraction
        document.pages[page_number].accept(absorber)
        extracted_text = absorber.text
        with open(outfile, "w", encoding="utf‑8") as f:
            f.write(extracted_text)
    finally:
        document.close()
```

## Iterar a través de TextFragments para Detectar Superíndice/Subíndice

Recorrer cada fragmento de texto en una página, comprobar si es superíndice o subíndice y procesarlo en consecuencia.

1. Cargar el documento PDF.
1. Crear 'TextFragmentAbsorber()' y aceptarlo en la página seleccionada.
1. Acceder a 'absorber.text_fragments', que devuelve una colección de fragmentos encontrados en esa página.
1. Para cada fragmento:
- Recuperar 'fragment.text'.
- Verificar 'fragment.text_state.superscript' y 'fragment.text_state.subscript'.
- Escribir una línea en el archivo de salida con el texto del fragmento y las banderas.
1. Cerrar el archivo y el documento.

```python

import os
import aspose.pdf as ap

def extract_super_sub_details(infile, outfile, page_number=1):
    """
    Extract details of each text fragment on a page, identifying superscript and subscript items.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1‑based page index.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages[page_number].accept(absorber)

        with open(outfile, "w", encoding="utf‑8") as f:
            for fragment in absorber.text_fragments:
                text = fragment.text
                is_sup = fragment.text_state.superscript  # True if superscript
                is_sub = fragment.text_state.subscript    # True if subscript
                f.write(f"Text: '{text}' | Superscript: {is_sup} | Subscript: {is_sub}\n")
    finally:
        document.close()
```
