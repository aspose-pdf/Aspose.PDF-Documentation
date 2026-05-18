---
title: Verbesserung der Textextraktion aus mehrspaltigen PDFs
linktitle: Textextraktion aus mehrspaltigen PDFs
type: docs
weight: 30
url: /de/python-net/text-extraction-from-multi-column-pdf/
description: Erfahren Sie Techniken zur Verbesserung der Textextraktion aus mehrspaltigen PDF-Layouts mit Aspose.PDF for Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Schriftgröße manuell reduzieren und dann extrahieren

In einigen mehrspaltigen Layouts kann das Reduzieren der Schriftgröße von Textfragmenten vor der Extraktion die Lesereihenfolge verbessern und Überlappungsprobleme verringern. Diese Technik kann bei eng formatierten Dokumenten wie Zeitschriften, Forschungsarbeiten, Broschüren oder Berichten mit dichten Textspalten helfen.

1. Laden Sie das PDF.
1. Verwenden [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) um die Textfragmente zu sammeln.
1. Reduzieren Sie die Schriftgröße jedes Fragments, speichern Sie das Dokument und öffnen Sie es erneut.
1. Verwenden [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) um den Text zu extrahieren.
1. Schreiben Sie den extrahierten Text in eine Ausgabedatei.

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

## Text mit Skalierungsfaktor extrahieren

Eine weitere Möglichkeit für die mehrspaltige Extraktion besteht darin, zu konfigurieren [TextExtractionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textextractionoptions/) mit einem Skalierungsfaktor. Das Anpassen des Skalierungsfaktors kann die Interpretation von dicht gepackten Fragmenten verbessern und dazu beitragen, die Lesereihenfolge in dichten Layouts, Tabellen oder spaltenbasierten Dokumenten genauer zu erhalten.

1. Laden Sie das PDF.
1. Erstelle ein [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/).
1. Konfigurieren `TextExtractionOptions.scale_factor`.
1. Weisen Sie die Extraktionsoptionen dem Absorber zu.
1. Extrahiere den Text der Seite und schreibe das Ergebnis in eine Ausgabedatei.

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
