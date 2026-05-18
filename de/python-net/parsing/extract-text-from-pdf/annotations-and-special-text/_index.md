---
title: Annotationen und Sondertext mit Python
linktitle: Annotationen und Sondertext
type: docs
weight: 40
url: /de/python-net/annotation-and-special-text/
description: Erfahren Sie, wie Sie Text aus Stempelannotationen, hervorgehobenem Text und hoch-/tiefgestelltem Inhalt in PDF-Dokumenten mit Aspose.PDF for Python extrahieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Text aus Stempelannotationen extrahieren

Verwenden [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) um Text zu extrahieren, der in einem [StampAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/stampannotation) appearance stream. Dies ist nützlich, wenn Stamp-Inhalte als Form-XObject gerendert werden, anstatt als Klartext gespeichert zu sein.

1. Öffnen Sie das [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Greifen Sie von der Zielannotation aus zu `page.annotations`.
1. Überprüfen Sie, ob es ein `StampAnnotation`, dann rufen Sie seine normale Erscheinungs-XForm ab.
1. Übergeben Sie das XForm an `TextAbsorber.visit()` um den eingebetteten Text zu extrahieren.

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

## Hervorgehobenen Text extrahieren

Iteriere über die Anmerkungen einer Seite und verwende [HighlightAnnotation.get_marked_text()](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation) um die von jeder Hervorhebung abgedeckten Textabschnitte zu lesen. Die Anmerkungssammlung der Seite ist 1-basiert.

1. Öffnen Sie das [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) und wählen Sie die Zielseite aus.
1. Durchlaufen `page.annotations`.
1. Verwenden `is_assignable` filtern nach [HighlightAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation) Instanzen.
1. Wandeln Sie die Anmerkung um und rufen Sie sie auf `get_marked_text()` um den hervorgehobenen Inhalt abzurufen.

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

## Hoch- und Tiefgestellten Text extrahieren

Hoch- und Tiefgestellte erscheinen häufig in Formeln, mathematischen Ausdrücken und Namen chemischer Verbindungen. Aspose.PDF for Python via .NET unterstützt das Extrahieren dieses Inhalts über [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber), die Metadaten zur Zeichenpositionserkennung erkennt.

1. Öffnen Sie das [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Erstelle ein `TextFragmentAbsorber` Instanz.
1. Anruf `document.pages[page_number].accept(absorber)` die Zielseite zu scannen.
1. Den vollständigen extrahierten Text abrufen von `absorber.text`.
1. Schreiben Sie das Ergebnis in eine Datei und schließen Sie das Dokument.

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

## Iterieren Sie durch Textfragmente, um Superscript/Subscript zu erkennen

Für die Inspektion pro Fragment iterieren Sie über `absorber.text_fragments` und lese das `text_state.superscript` und `text_state.subscript` boolesche Flags bei jedem [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment).

1. Öffnen Sie das [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) und erstelle ein [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber).
1. Akzeptieren Sie den Absorber auf der Zielseite, um sie zu füllen `absorber.text_fragments`.
1. Für jedes Fragment, lesen `fragment.text`, `fragment.text_state.superscript`, und `fragment.text_state.subscript`.
1. Schreiben Sie die Ergebnisse in die Ausgabedatei und schließen Sie das Dokument.

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
