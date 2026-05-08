---
title: Mejorando la extracción de texto de PDFs de varias columnas
linktitle: Extracción de texto de PDFs de varias columnas
type: docs
weight: 30
url: /es/python-net/text-extraction-from-multi-column-pdf/
description: Aprenda técnicas para mejorar la extracción de texto en diseños PDF de varias columnas con Aspose.PDF for Python via .NET.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Reduzca el tamaño de fuente manualmente y luego extraiga

En algunos diseños de varias columnas, reducir el tamaño de fuente de los fragmentos de texto antes de la extracción puede mejorar el orden de lectura y reducir los problemas de superposición. Esta técnica puede ayudar con documentos de formato estrecho, como revistas, artículos de investigación, folletos o informes con columnas densas de texto.

1. Cargue el PDF.
1. Utilice [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) para recopilar los fragmentos de texto.
1. Reduzca el tamaño de la fuente de cada fragmento, luego guarde y vuelva a abrir el documento.
1. Utilice [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) para extraer el texto.
1. Escriba el texto extraído en un archivo de salida.

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

Otra opción para la extracción en varias columnas consiste en configurar [TextExtractionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textextractionoptions/) con un factor de escala. Ajustar este factor puede mejorar la interpretación de fragmentos compactos y ayudar a conservar un orden de lectura más preciso en diseños densos, tablas o documentos organizados por columnas.

1. Cargue el PDF.
1. Cree un [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/).
1. Configure `TextExtractionOptions.scale_factor`.
1. Asigne las opciones de extracción al absorbedor.
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
