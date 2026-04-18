---
title: Mejorar la extracción de texto de PDFs de varias columnas
linktitle: Extracción de texto de PDFs de varias columnas
type: docs
weight: 30
url: /es/python-net/text-extraction-from-multi-column-pdf/
description: Aprenda técnicas para mejorar la extracción de texto de diseños PDF de varias columnas con Aspose.PDF for Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Reduzca el tamaño de fuente manualmente y luego extraiga

En algunos diseños de varias columnas, reducir el tamaño de fuente de los fragmentos de texto antes de la extracción puede mejorar el orden de lectura y reducir los problemas de superposición. Esta técnica puede ayudar con documentos muy formateados, como revistas, artículos de investigación, folletos o informes con columnas de texto densas.

1. Cargue el PDF.
1. Usar [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) para recopilar los fragmentos de texto.
1. Reduzca el tamaño de fuente de cada fragmento, luego guarde y vuelva a abrir el documento.
1. Usar [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) para extraer el texto.
1. Escribe el texto extraído en un archivo de salida.

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
```

## Extraer texto con factor de escala

Otra opción para la extracción de varias columnas es configurar [TextExtractionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textextractionoptions/) con un factor de escala. Ajustar el factor de escala puede mejorar la interpretación de fragmentos muy compactos y ayudar a preservar un orden de lectura más preciso en diseños densos, tablas o documentos basados en columnas.

1. Cargue el PDF.
1. Crear un [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/).
1. Configurar `TextExtractionOptions.scale_factor`.
1. Asigne las opciones de extracción al absorbente.
1. Extraiga el texto de la página y escriba el resultado en un archivo de salida.

```python
import aspose.pdf as ap


def extract_text_scale_factor(infile, outfile, scale_factor=0.5):
    """
    Extract text from a PDF with multi-column layout using scale factor.
    Args:
        infile (str): Input PDF path.
        outfile (str): Output text file path.
        scale_factor (float): Scale factor between 0.1 and 1.0 or 0 for auto-scaling.
    """
    doc = ap.Document(infile)
    text_absorber = ap.text.TextAbsorber()
    ext_opts = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    ext_opts.scale_factor = scale_factor
    text_absorber.extraction_options = ext_opts
    doc.pages.accept(text_absorber)
    extracted_text = text_absorber.text
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```
