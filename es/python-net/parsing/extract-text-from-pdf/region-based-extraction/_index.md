---
title: Extracción basada en regiones usando Python
linktitle: Extracción basada en regiones
type: docs
weight: 20
url: /es/python-net/region-based-extraction/
description: Esta sección contiene artículos sobre extracción basada en regiones de documentos PDF usando Aspose.PDF en Python.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Extraer texto de una región específica de una página

Extraiga texto de una región rectangular definida en una página específica de un PDF usando Aspose.PDF para Python. Al especificar coordenadas, puede enfocar la extracción en un área concreta — como una celda de tabla, un bloque de párrafo o una región de campo de formulario.

Ideal para la extracción de texto basada en zonas, como extraer datos de encabezados, pies de página, facturas o informes de diseño fijo donde el texto aparece en posiciones predecibles.

1. Abra el documento PDF.
1. Cree un 'TextAbsorber'.
1. Configure 'text_search_options' para restringir a la región rectangular.
1. Acepte el absorber en la página específica.
1. Escriba el texto extraído.

```python

import os
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

## Extraer párrafos iterando a través de ellos

Podemos obtener texto de un documento PDF buscando un texto concreto (usando "texto plano" o "expresiones regulares") en una sola página o en todo el documento, o podemos obtener el texto completo de una página única, un rango de páginas o del documento completo. Sin embargo, en algunos casos es necesario extraer párrafos de un documento PDF o texto en forma de párrafos. Hemos implementado funcionalidad para buscar secciones y párrafos en el texto de las páginas del documento PDF. Hemos introducido la clase ParagraphAbsorber (similar a TextFragmentAbsorber y TextAbsorber), que puede usarse para extraer párrafos de documentos PDF.

La biblioteca Aspose.PDF le permite leer un archivo PDF y extraer todo el texto de los párrafos de cada página usando 'ParagraphAbsorber'. Organiza la salida por página, sección y párrafo, y escribe el contenido extraído en un archivo de texto sin formato. Esto es útil para el análisis de texto, archivado o conversión de contenido PDF estructurado a formatos legibles.

1. Abra el documento PDF.
1. Instancie un 'ParagraphAbsorber'.
1. Llame a 'absorber.visit(document)' para escanear todas las páginas en busca de párrafos.
1. Recorra la colección 'page_markups' del absorber.
1. Para cada 'page‑markup', recorra sus 'sections', luego cada 'paragraph' en la sección.
1. Dentro de cada párrafo, recorra 'lines', luego cada 'fragment' en la línea, acumulando 'fragment.text'.
1. Escriba cada párrafo (con índices de página/ sección/ párrafo) en el archivo de salida.
1. Cierre el documento cuando haya terminado.

```python

import os
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

        with open(outfile, "w", encoding="utf‑8") as tw:
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
                        tw.write(f"Page {page_markup.number}, Section {sec_idx}, Paragraph {para_idx}:\n")
                        tw.write(paragraph_text + "\n")
    finally:
        document.close()
```

## Extraer párrafos con renderizado de polígono delimitador

Este fragmento de código extrae texto a nivel de párrafo e información de diseño de una página específica en un PDF. Captura el rectángulo delimitador y las coordenadas del polígono de cada párrafo, junto con el contenido de texto real, y escribe los resultados en un archivo de texto. Esto es útil para analizar la estructura del documento, mapear el diseño o preparar datos para tareas de accesibilidad y extracción de contenido.

1. Abra el PDF y cargue el documento.
1. Instancie 'ParagraphAbsorber'.
1. Llame a 'absorber.visit(page)' para la página específica que desea.
1. Obtenga el primer 'page_markup' de 'absorber.page_markups'.
1. Para cada sección en ese marcado:
- Recupere su 'rectangle'.
1. Para cada párrafo en la sección:
- Obtenga sus 'points' (polígono).
- Extraiga texto recorriendo 'paragraph.lines' - 'fragment.text'.
1. Escriba la información de geometría y texto en el archivo de salida.
1. Cierre el documento.

```python

import os
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
        with open(outfile, "w", encoding="utf‑8") as tw:
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

