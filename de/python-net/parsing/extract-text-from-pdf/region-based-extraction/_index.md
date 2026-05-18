---
title: Regionsbasierte Extraktion mit Python
linktitle: Regionsbasierte Extraktion
type: docs
weight: 20
url: /de/python-net/region-based-extraction/
description: Erfahren Sie, wie Sie Text aus einem bestimmten Seitenbereich oder einer Absatzstruktur in PDF-Dokumenten mit Aspose.PDF for Python extrahieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Text aus einem bestimmten Bereich einer Seite extrahieren

Verwenden [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) zusammen mit einem [Rechteck](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) um die Extraktion auf einen bestimmten Bereich einer Seite zu beschränken. Dieser Ansatz ist nützlich für zonebasierte Extraktion aus Kopfzeilen, Fußzeilen, Tabellenzellen, Formularfeldern, Rechnungen oder anderen festgelegten Layout‑Bereichen, bei denen die Textposition im Voraus bekannt ist.

1. Öffnen Sie das Quell‑PDF als [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Erstelle ein `TextAbsorber` Instanz.
1. Konfigurieren `text_search_options` die Extraktion auf ein Rechteck zu beschränken.
1. Akzeptieren Sie den Absorber auf der Zielseite.
1. Schreiben Sie den extrahierten Text in eine Ausgabedatei.

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

## Absätze extrahieren, indem man sie durchläuft

Verwenden [ParagraphAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/paragraphabsorber/) wenn Sie eine abschnittsbezogene Extraktion anstelle von einfachem Seitentext benötigen. Im Gegensatz zu [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) oder [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/), diese API organisiert die Ausgabe nach Seite, Abschnitt und Absatz, was für Textanalyse, strukturierten Export und layoutempfindliche Verarbeitung nützlich ist.

1. Öffnen Sie das Quell‑PDF als [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Erstelle ein `ParagraphAbsorber` Instanz.
1. Anruf `absorber.visit(document)` um alle Seiten zu analysieren.
1. Durchlaufen `page_markups`, dann durch jeden Abschnitt und Absatz.
1. Lesen Sie die Textfragmente aus jedem Absatz und schreiben Sie das Ergebnis in eine Datei.

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

## Absätze mit Begrenzungs-Polygon-Rendering extrahieren

Sie können auch verwenden [ParagraphAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/paragraphabsorber/) um die Absatzgeometrie zu untersuchen. Zusätzlich zum Extrahieren von Text zeichnet dieser Ansatz jedes Abschnittsrechteck und Absatzpolygon auf, was nützlich ist für Layout‑Mapping, Dokumentenanalyse, Barrierefreiheits‑Tools oder regionsabhängige Nachbearbeitung.

1. Öffnen Sie das Quell‑PDF als [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Erstelle ein `ParagraphAbsorber` Instanz.
1. Besuchen Sie die Zielseite.
1. Lese das Seiten‑Markup von `absorber.page_markups`.
1. Durchlaufen Sie Abschnitte und Absätze, um Geometrie und Text zu erfassen.
1. Schreibe die Rechteck‑, Polygon‑ und Textdaten in die Ausgabedatei.

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
