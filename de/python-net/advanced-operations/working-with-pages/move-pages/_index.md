---
title: PDF-Seiten in Python verschieben
linktitle: PDF-Seiten verschieben
type: docs
weight: 100
url: /de/python-net/move-pages/
description: Erfahren Sie, wie Sie PDF-Seiten innerhalb eines Dokuments oder zwischen Dokumenten in Python verschieben.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Seiten zwischen Dokumenten in Python verschieben
Abstract: Dieser Artikel erklärt, wie man Seiten in PDFs mit Aspose.PDF for Python via .NET verschiebt. Erfahren Sie, wie Sie eine einzelne Seite oder mehrere Seiten in ein anderes Dokument verschieben und wie Sie eine Seite innerhalb derselben PDF mit den Document- und PageCollection-APIs neu positionieren.
---

## Verschieben Sie eine Seite von einem PDF Document zu einem anderen

Aspose.PDF for Python ermöglicht es Ihnen, eine Seite (nicht nur zu kopieren) von einem PDF zu einem anderen zu verschieben. Es entfernt die ausgewählte Seite aus dem Originaldokument und fügt sie anschließend zu einer neuen PDF-Datei hinzu.

Stellen Sie sich das vor, als würden Sie eine Seite aus einem Buch ausschneiden und in ein anderes einkleben — die Seite existiert nach dem Verschieben nicht mehr in der ursprünglichen Datei.

1. Öffnen Sie das Quell-PDF-Dokument mit dem [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Klasse.
1. Wählen Sie eine bestimmte Seite zum Verschieben aus (in diesem Fall Seite 2) — dies bezieht sich auf ein [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Erstellen Sie ein neues PDF-Dokument (instanziieren Sie ein weiteres [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. Fügen Sie die ausgewählte Seite dem neuen PDF-Dokument unter Verwendung des Zieldokuments [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (zum Beispiel, `another_document.pages.add(page)`).
1. Löschen Sie die Seite aus dem Originaldokument über dessen [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (zum Beispiel, `document.pages.delete(index)`).
1. Speichern Sie beide Dokumente.

Der folgende Codeausschnitt zeigt Ihnen, wie Sie eine Seite verschieben.

```python
import aspose.pdf as ap

def move_page_from_one_document_to_another(
    input_file_name: str, output_file_name: str
) -> None:

    document = ap.Document(input_file_name)
    page = document.pages[2]
    another_document = ap.Document()
    another_document.pages.add(page)
    document.pages.delete(2)
    document.save(input_file_name.replace(".pdf", "_new.pdf"))
    another_document.save(output_file_name)
```

## Mehrere Seiten von einem PDF-Dokument in ein anderes verschieben

Im Gegensatz zum Kopieren überträgt dieser Vorgang die ausgewählten Seiten — entfernt sie aus der Quelldatei und speichert sie in einem neuen PDF.

1. Erstellen Sie ein neues, leeres Zieldokument (`Document`).
1. Wählen Sie mehrere Seiten (in diesem Fall die Seiten 1 und 3) aus dem Quell‑Dokument aus [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Durchlaufen Sie die ausgewählten Seiten und fügen jede einzelne dem Zieldokument hinzu [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Speichern Sie das Zieldokument, das die verschobenen Seiten enthält.
1. Löschen Sie die verschobenen Seiten aus dem Quell-Dokument mit dessen [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Speichern Sie das modifizierte Quelldokument unter einem neuen Dateinamen, um beide Versionen zu erhalten.

Das folgende Code-Snippet zeigt, wie mehrere Seiten verschoben werden.

```python
import aspose.pdf as ap

def move_multiple_pages_from_one_document_to_another(
    input_file_name: str, output_file_name: str
) -> None:
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    pages = [1, 2]
    for page_index in pages:
        page = src_document.pages[page_index]
        dst_document.pages.add(page)
    # Save output files
    dst_document.save(output_file_name)
    src_document.pages.delete(pages)
    src_document.save(input_file_name.replace(".pdf", "_new.pdf"))
```

## Verschieben einer Seite an einen neuen Ort im selben PDF-Dokument

Es zeigt, wie man eine bestimmte Seite an eine andere Position innerhalb desselben Dokuments verschiebt — ein häufiges Bedürfnis beim Umorganisieren oder Bearbeiten von PDF‑Layouts.

1. Laden Sie das Eingabe‑PDF‑Dokument mit der [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Klasse.
1. Wählen Sie die Seite aus, die Sie verschieben möchten (Seite 2) — dies ist ein [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Fügen Sie sie am Ende des Dokuments hinzu, indem Sie das Dokument verwenden. [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Löschen Sie die Originalseite von ihrem vorherigen Speicherort über die [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Speichern Sie das bearbeitete Dokument als neue Datei.

```python
import aspose.pdf as ap

def move_page_in_new_location_in_same_document(
    input_file_name: str, output_file_name: str
) -> None:
    src_document = ap.Document(input_file_name)

    page = src_document.pages[2]
    src_document.pages.add(page)
    src_document.pages.delete(2)

    # Save output file
    src_document.save(output_file_name)
```

## Verwandte Seitenthemen

- [Arbeiten Sie mit PDF-Seiten in Python](/pdf/de/python-net/working-with-pages/)
- [PDF‑Seiten in Python hinzufügen](/pdf/de/python-net/add-pages/)
- [PDF‑Seiten in Python löschen](/pdf/de/python-net/delete-pages/)
- [PDF-Seiten in Python extrahieren](/pdf/de/python-net/extract-pages/)
