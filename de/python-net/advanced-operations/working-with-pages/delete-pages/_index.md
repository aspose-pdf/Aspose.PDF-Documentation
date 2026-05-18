---
title: PDF‑Seiten in Python löschen
linktitle: PDF‑Seiten löschen
type: docs
weight: 80
url: /de/python-net/delete-pages/
description: Erfahren Sie, wie Sie Seiten aus PDF‑Dateien in Python löschen können.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Löschen Sie eine oder mehrere PDF‑Seiten in Python
Abstract: Dieses Dokument erklärt, wie man Seiten aus PDF‑Dateien mit Aspose.PDF for Python via .NET entfernt. Erfahren Sie, wie Sie eine einzelne Seite oder mehrere Seiten aus einem Dokument mithilfe der PageCollection API löschen und anschließend das aktualisierte PDF speichern.
---

Sie können Seiten aus einer PDF‑Datei mithilfe von Aspose.PDF for Python via .NET löschen. Um eine bestimmte Seite zu löschen, verwenden Sie [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) von einem [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Verwenden Sie diesen Ablauf, wenn Sie unerwünschte Seiten aus einem PDF entfernen müssen, bevor Sie es teilen, archivieren oder Dokumente zusammenführen.

## Seite aus PDF-Datei löschen

Aspose.PDF for Python via .NET löscht Seite 2 aus dem Eingabe-PDF und speichert das aktualisierte Dokument in einer neuen Datei. Diese Funktion ist hilfreich, um unerwünschte oder sensible Seiten zu entfernen, ohne den Rest des Dokuments zu verändern.

1. Laden Sie das Eingabe-PDF als ein [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Löschen Sie die Seite mit dem [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Rufen Sie die [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) Methode, um die aktualisierte PDF-Datei zu speichern.

Das folgende Code‑Snippet zeigt, wie man mit Python eine bestimmte Seite aus der PDF-Datei löscht.

```python
import aspose.pdf as ap

def delete_page(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.delete(2)
    document.save(output_file_name)
```

## Mehrere Seiten aus einem PDF-Dokument löschen

Das Löschen mehrerer Seiten ermöglicht das Entfernen einer Menge bestimmter Seiten in einem einzigen Vorgang, was effizienter ist, als Seiten einzeln zu löschen. Das resultierende PDF wird in einer neuen Datei gespeichert, wobei das Originaldokument erhalten bleibt.

1. Laden Sie das Eingabe-PDF als ein [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Löschen Sie die in dem pages‑Array aufgeführten Seiten mit dem [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Speichere das Aktualisierte [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) in eine neue Datei.

```python
import aspose.pdf as ap

def delete_multiple_pages(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    # Example: delete pages 2, 3, and 4.
    pages = [2, 3, 4]
    document.pages.delete(pages)
    document.save(output_file_name)
```

## Verwandte Seitenthemen

- [Arbeiten Sie mit PDF-Seiten in Python](/pdf/de/python-net/working-with-pages/)
- [PDF‑Seiten in Python hinzufügen](/pdf/de/python-net/add-pages/)
- [PDF‑Seiten in Python verschieben](/pdf/de/python-net/move-pages/)
- [PDF-Seiten in Python extrahieren](/pdf/de/python-net/extract-pages/)
