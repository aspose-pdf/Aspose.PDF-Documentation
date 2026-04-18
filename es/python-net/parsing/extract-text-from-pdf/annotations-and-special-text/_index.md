---
title: Anotaciones y texto especial usando Python
linktitle: Anotaciones y texto especial
type: docs
weight: 40
url: /es/python-net/annotation-and-special-text/
description: Aprenda cómo extraer texto de anotaciones de sello, texto resaltado y contenido de superíndice/subíndice en documentos PDF usando Aspose.PDF for Python.
lastmod: "2025-11-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraer texto de anotaciones de sello

Usar [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) para extraer texto incrustado en un [StampAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/stampannotation) flujo de apariencia. Esto es útil cuando el contenido del sello se renderiza como un XObject de formulario en lugar de almacenarse como texto plano.

1. Abre el [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Acceder a la anotación de destino desde `page.annotations`.
1. Verifique que es un `StampAnnotation`, luego recupere su apariencia normal XForm.
1. Pase el XForm a `TextAbsorber.visit()` para extraer el texto incrustado.

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

## Extraer texto resaltado

Iterar sobre las anotaciones de una página y usar [HighlightAnnotation.get_marked_text()](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation) para leer los fragmentos de texto cubiertos por cada resaltado. La colección de anotaciones de la página es de base 1.

1. Abre el [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) y seleccione la página objetivo.
1. Recorrer `page.annotations`.
1. Usar `is_assignable` filtrar por [HighlightAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation) instancias.
1. Realice un casting de la anotación y llame `get_marked_text()` para recuperar el contenido resaltado.

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

## Extraer texto de superíndice y subíndice

Los superíndices y subíndices aparecen con frecuencia en fórmulas, expresiones matemáticas y nombres de compuestos químicos. Aspose.PDF for Python via .NET admite la extracción de este contenido mediante [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber), que detecta los metadatos de posicionamiento a nivel de carácter.

1. Abre el [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Crear un `TextFragmentAbsorber` instancia.
1. Llamar `document.pages[page_number].accept(absorber)` para escanear la página objetivo.
1. Recuperar el texto completo extraído de `absorber.text`.
1. Escriba el resultado en un archivo y cierre el documento.

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
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(extracted_text)
    finally:
        document.close()
```

## Iterar a través de fragmentos de texto para detectar superíndice/subíndice

Para la inspección por fragmento, iterar sobre `absorber.text_fragments` y lea el `text_state.superscript` y `text_state.subscript` banderas booleanas en cada [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment).

1. Abre el [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) y crear un [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber).
1. Acepta el absorber en la página de destino para poblar `absorber.text_fragments`.
1. Para cada fragmento, lea `fragment.text`, `fragment.text_state.superscript`, y `fragment.text_state.subscript`.
1. Escribe los resultados en el archivo de salida y cierra el documento.

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

        with open(outfile, "w", encoding="utf-8") as f:
            for fragment in absorber.text_fragments:
                text = fragment.text
                is_sup = fragment.text_state.superscript  # True if superscript
                is_sub = fragment.text_state.subscript  # True if subscript
                f.write(
                    f"Text: '{text}' | Superscript: {is_sup} | Subscript: {is_sub}\n"
                )
    finally:
        document.close()
```
