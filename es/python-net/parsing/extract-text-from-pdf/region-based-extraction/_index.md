---
title: Extracción basada en regiones usando Python
linktitle: Extracción basada en regiones
type: docs
weight: 20
url: /es/python-net/region-based-extraction/
description: Aprenda cómo extraer texto de una región de página específica o de la estructura de párrafos en documentos PDF con Aspose.PDF for Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraer texto de una región específica de una página

Usar [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) junto con un [Rectángulo](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) para limitar la extracción a un área específica de una página. Este método es útil para la extracción basada en zonas de encabezados, pies de página, celdas de tabla, campos de formulario, facturas o de otras regiones de diseño fijo donde la posición del texto se conoce de antemano.

1. Abre el PDF de origen como un [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crear un `TextAbsorber` instancia.
1. Configurar `text_search_options` para limitar la extracción a un rectángulo.
1. Acepta el absorbente en la página de destino.
1. Escribe el texto extraído en un archivo de salida.

```python
import aspose.pdf as ap


def extract_text_from_region(infile, page_number, rect_coords, outfile):
    """
    Extract text from a specified rectangular region on a given page.
    Args:
        infile (str): Path to input PDF file.
        page_number (int): 1-based index of the page.
        rect_coords (tuple): (llx, lly, urx, ury) coordinates of the rectangle.
        outfile (str): Output text file path.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextAbsorber()
        # Set options to restrict search to the rectangle
        absorber.text_search_options.limit_to_page_bounds = True
        llx, lly, urx, ury = rect_coords
        absorber.text_search_options.rectangle = ap.Rectangle(llx, lly, urx, ury, True)
        # Accept on the specific page
        document.pages[page_number].accept(absorber)
        extracted_text = absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

## Extrae párrafos iterando a través de ellos

Usar [ParagraphAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/paragraphabsorber/) cuando necesitas una extracción consciente de párrafos en lugar de texto de página simple. A diferencia de [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) o [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/), esta API organiza la salida por página, sección y párrafo, lo que es útil para el análisis de texto, la exportación estructurada y el procesamiento sensible al diseño.

1. Abre el PDF de origen como un [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crear un `ParagraphAbsorber` instancia.
1. Llamar `absorber.visit(document)` para analizar todas las páginas.
1. Iterar a través de `page_markups`, luego a través de cada sección y párrafo.
1. Lea los fragmentos de texto de cada párrafo y escriba el resultado en un archivo.

```python
import aspose.pdf as ap


def extract_paragraphs_from_pdf(infile, outfile):
    """
    Extract all paragraphs from a PDF document, and write each paragraph’s text into an output file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.ParagraphAbsorber()
        absorber.visit(document)

        with open(outfile, "w", encoding="utf-8") as tw:
            for page_markup in absorber.page_markups:
                for sec_idx, section in enumerate(page_markup.sections, start=1):
                    for para_idx, paragraph in enumerate(section.paragraphs, start=1):
                        # Concatenate all fragments/lines in the paragraph
                        parts = []
                        for line in paragraph.lines:
                            for fragment in line:
                                parts.append(fragment.text)
                            parts.append("\r\n")
                        paragraph_text = "".join(parts)
                        tw.write(
                            f"Page {page_markup.number}, Section {sec_idx}, Paragraph {para_idx}:\n"
                        )
                        tw.write(paragraph_text + "\n")
    finally:
        document.close()
```

## Extraer párrafos con renderizado de polígonos delimitadores

También puedes usar [ParagraphAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/paragraphabsorber/) para inspeccionar la geometría de los párrafos. Además de extraer texto, este enfoque registra el rectángulo de cada sección y el polígono del párrafo, lo cual es útil para el mapeo de diseño, análisis de documentos, herramientas de accesibilidad o procesamiento posterior sensible a regiones.

1. Abre el PDF de origen como un [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Crear un `ParagraphAbsorber` instancia.
1. Visite la página de destino.
1. Leer el marcado de la página desde `absorber.page_markups`.
1. Iterar a través de secciones y párrafos para capturar la geometría y el texto.
1. Escriba los datos de rectángulo, polígono y texto en el archivo de salida.

```python
import aspose.pdf as ap


def extract_paragraphs_with_geometry(infile, outfile):
    """
    Extract paragraphs and record geometry info (rectangle / polygon) for each paragraph in a PDF.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.ParagraphAbsorber()
        absorber.visit(document.pages[1])  # Visit page 2 (pages are 1-indexed)

        page_markup = absorber.page_markups[0]
        with open(outfile, "w", encoding="utf-8") as tw:
            for sec_idx, section in enumerate(page_markup.sections, start=1):
                tw.write(f"Section {sec_idx}: rectangle = {section.rectangle}\n")
                for para_idx, paragraph in enumerate(section.paragraphs, start=1):
                    tw.write(f"  Paragraph {para_idx}: polygon = {paragraph.points}\n")
                    # Concatenate paragraph text
                    parts = []
                    for line in paragraph.lines:
                        for fragment in line:
                            parts.append(fragment.text)
                        parts.append("\r\n")
                    tw.write("    Text: " + "".join(parts) + "\n\n")
    finally:
        document.close()
```
