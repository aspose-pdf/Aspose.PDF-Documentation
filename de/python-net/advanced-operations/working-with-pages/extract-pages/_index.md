---
title: PDF-Seiten in Python extrahieren
linktitle: Extrahieren von PDF-Seiten
type: docs
weight: 80
url: /de/python-net/extract-pages/
description: Erfahren Sie, wie Sie einzelne oder mehrere PDF-Seiten in neue Dateien in Python extrahieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man PDF-Seiten mit Python extrahiert
Abstract: Dieser Artikel erklärt, wie man Seiten aus PDF-Dateien mit Aspose.PDF for Python via .NET extrahiert. Erfahren Sie, wie Sie eine einzelne Seite oder mehrere Seiten in ein neues Dokument kopieren, indem Sie die 1‑basierte Seitennummerierung und die PageCollection‑API verwenden.
---

## Einzelne Seite aus einem PDF extrahieren

Extrahieren Sie eine bestimmte Seite aus einem PDF-Dokument und speichern Sie sie als neue Datei. Mit der Aspose.PDF-Bibliothek kopiert das Skript die gewünschte Seite in ein neues PDF, wobei das Originaldokument unverändert bleibt. Dies ist nützlich zum Aufteilen von PDFs oder zum Isolieren wichtiger Seiten für die Verteilung.

1. Laden Sie das Quell-PDF mit [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`).
1. Neu erstellen [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) um die extrahierte Seite zu halten.
1. Fügen Sie das gewünschte [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) aus dem Quell-Dokument zum neuen PDF unter Verwendung des Ziel-Dokuments [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) (`dst_document.pages.add(...)`).
    - In diesem Beispiel wird Seite 2 extrahiert (1-basierte Indizierung).
1. Speichern Sie das neue [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) mit der extrahierten Seite in die angegebene Ausgabedatei.

```python
import aspose.pdf as ap

def extract_page(input_file_name: str, output_file_name: str) -> None:
    src_document = ap.Document(input_file_name)
    dst_document = ap.Document()
    dst_document.pages.add(src_document.pages[2])
    dst_document.save(output_file_name)
```

## Mehrere Seiten aus einer PDF extrahieren

Extrahieren Sie mehrere bestimmte Seiten aus einem PDF-Dokument und speichern Sie sie in einer neuen Datei. Mit der Aspose.PDF-Bibliothek werden ausgewählte Seiten in ein neues PDF kopiert, während das Originaldokument unverändert bleibt. Dies ist nützlich, um kleinere PDFs zu erstellen, die nur relevante Abschnitte eines größeren Dokuments enthalten.

1. Laden Sie das Quell-PDF mit [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) API (`ap.Document()`).
1. Neu erstellen [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) um die extrahierten Seiten zu halten.
1. Wählen Sie die zu extrahierenden Seiten aus (in diesem Beispiel die Seiten 2 und 3 unter Verwendung einer 1‑basierten Indizierung).
1. Fügen Sie jede ausgewählte [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) aus dem Quelldokument in das neue PDF unter Verwendung seiner [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Speichern Sie das neue [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) mit den extrahierten Seiten in die angegebene Ausgabedatei.

```python
import aspose.pdf as ap

def extract_multiple_pages(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    pages = [2, 3]
    another_document = ap.Document()
    for page_index in pages:
        another_document.pages.add(document.pages[page_index])
    another_document.save(output_file_name)
```

## Verwandte Seitenthemen

- [Arbeiten Sie mit PDF-Seiten in Python](/pdf/de/python-net/working-with-pages/)
- [PDF‑Seiten in Python löschen](/pdf/de/python-net/delete-pages/)
- [PDF‑Seiten in Python verschieben](/pdf/de/python-net/move-pages/)
- [PDF-Dateien in Python teilen](/pdf/de/python-net/split-document/)
