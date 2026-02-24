---
title: Mejora de la extracción de texto de PDFs multicolumna
linktitle: Extracción de texto de PDFs multicolumna
type: docs
weight: 30
url: /es/python-net/text-extraction-from-multi‑column-pdf/
description: Esta sección contiene artículos sobre formato y escalado de texto usando Aspose.PDF en Python.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

## Reducir el tamaño de fuente manualmente y luego extraer

La precisión de extracción en PDFs multicolumna se logra reduciendo primero el tamaño de fuente de todos los fragmentos de texto antes de la extracción. El proceso ayuda a evitar problemas de texto superpuesto que pueden ocurrir en diseños muy ajustados o multicolumna.
Ayuda a extraer texto de diseños complejos —como revistas, trabajos académicos o folletos— donde cambiar el tamaño del texto mejora la claridad del diseño y los resultados de extracción.

1. Cargar el PDF.
1. Reducir el tamaño de fuente de los fragmentos de texto existentes, guardar y volver a abrir el documento.
1. Utilizar 'TextAbsorber' para extraer texto de las páginas.
1. Guardar el texto extraído.

```python

import io
import aspose.pdf as ap

def extract_text_reduce_font(infile, outfile, reduce_ratio=0.7):
    """
    Extract text from a multi-column PDF by first reducing font size of all text fragments.
    Args:
        infile (str): Path to input PDF.
        outfile (str): Output text file.
        reduce_ratio (float): Ratio to reduce font size (e.g., 0.7 = 70%).
    """
    doc = ap.Document(infile)
    try:
        frag_absorber = ap.text.TextFragmentAbsorber()
        doc.pages.accept(frag_absorber)
        for frag in frag_absorber.text_fragments:
            frag.text_state.font_size = frag.text_state.font_size * reduce_ratio
        # Save to memory stream and reopen (to apply changes)
        ms = io.BytesIO()
        doc.save(ms)
        ms.seek(0)
        doc2 = ap.Document(ms)
        text_absorber = ap.text.TextAbsorber()
        doc2.pages.accept(text_absorber)
        extracted_text = text_absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        doc.close()
```

## Extraer texto con factor de escala

Extraer texto de PDFs con diseños multicolumna aplicando un factor de escala al documento. Ajustar el factor de escala garantiza que los fragmentos de texto se interpreten correctamente, reduciendo la superposición o desalineación durante la extracción.
Es útil para PDFs con columnas, tablas o diseños densos, donde el escalado ayuda a mantener el orden de lectura y la estructura adecuados en el texto extraído.

1. Cargar el PDF.
1. Configurar 'TextExtractionOptions.ScaleFactor'.
1. Utilizar 'TextAbsorber' para extraer texto de las páginas.
1. Guardar el texto extraído.

```python

import aspose.pdf as ap

def extract_text_with_scale_factor(infile, outfile, scale_factor=0.5):
    """
    Extract text from a PDF with multi-column layout using scale factor.
    Args:
        infile (str): Input PDF path.
        outfile (str): Output text file path.
        scale_factor (float): Scale factor between 0.1 and 1.0 or 0 for auto-scaling.
    """
    doc = ap.Document(infile)
    try:
        text_absorber = ap.text.TextAbsorber()
        ext_opts = ap.text.TextExtractionOptions(ap.text.TextExtractionOptions.TextFormattingMode.PURE)
        ext_opts.scale_factor = scale_factor
        text_absorber.extraction_options = ext_opts
        doc.pages.accept(text_absorber)
        extracted_text = text_absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        doc.close()
```
