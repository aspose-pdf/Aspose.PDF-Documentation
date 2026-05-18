---
title: PDF-Dateien in Python aufteilen
linktitle: PDF-Dateien aufteilen
type: docs
weight: 60
url: /de/python-net/split-pdf/
description: Erfahren Sie, wie Sie PDF‑Seiten in separate PDF‑Dateien mit Python aufteilen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aufteilen von PDF‑Seiten mit Python
Abstract: Der Artikel beschreibt den Vorgang, PDF‑Seiten mit Python in einzelne Dateien zu splitten, und hebt den Nutzen einer solchen Funktion für die Verwaltung großer PDF‑Dokumente hervor. Er verweist auf den Aspose.PDF Splitter, ein Online‑Tool, das die PDF‑Split‑Funktionalität demonstriert. Der Artikel liefert eine detaillierte Methode, um dies in Python‑Anwendungen zu erreichen, indem man über die Seiten eines PDF‑Dokuments mittels der `Document`‑Objekt‑`PageCollection` iteriert. Für jede Seite wird ein neues `Document`‑Objekt erstellt, die Seite wird hinzugefügt und die neue PDF‑Datei wird mit der `save()`‑Methode gespeichert. Ein begleitendes Python‑Code‑Snippet illustriert diesen Vorgang und zeigt die notwendigen Schritte, um ein PDF‑Dokument in separate Dateien zu splitten, indem man über seine Seiten iteriert und jede als einzelne PDF speichert.
---

Das Aufteilen von PDF-Seiten kann eine nützliche Funktion für diejenigen sein, die eine große Datei in einzelne Seiten oder Seitengruppen aufteilen möchten.

Verwenden Sie diesen Workflow, wenn Sie große PDFs in Einzelseiten‑Dateien oder kleinere Dokumentensätze für die Verteilung, Überprüfung oder nachgelagerte Verarbeitung aufteilen müssen.

## Live‑Beispiel

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) ist eine kostenlose Online-Webanwendung, die es Ihnen ermöglicht zu untersuchen, wie die Präsentationsaufteilungsfunktion funktioniert.

[![Aspose PDF aufteilen](splitter.png)](https://products.aspose.app/pdf/splitter)

Dieses Thema zeigt, wie Sie PDF-Seiten in einzelne PDF-Dateien in Ihren Python-Anwendungen aufteilen können. Um PDF-Seiten mit Python in einseitige PDF-Dateien aufzuteilen, können Sie die folgenden Schritte ausführen:

1. Durchlaufen Sie die Seiten des PDF-Dokuments durch die [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objekts [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) Sammlung
1. Für jede Iteration erstellen Sie ein neues Document-Objekt und fügen das Einzelne hinzu. [Seite](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) Objekt in das leere Dokument
1. Speichern Sie das neue PDF mit [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) Methode

## PDF in mehrere Dateien aufteilen oder separate PDFs in Python

Das folgende Python-Code‑Snippet zeigt Ihnen, wie Sie PDF‑Seiten in einzelne PDF‑Dateien aufteilen.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    page_count = 1

    # Loop through all the pages
    for pdfPage in document.pages:
        new_document = ap.Document()
        new_document.pages.add(pdfPage)
        new_document.save(output_path + "_page_" + str(page_count) + ".pdf")
        page_count = page_count + 1
```

## Verwandte Dokumentthemen

- [Arbeiten mit PDF-Dokumenten in Python](/pdf/de/python-net/working-with-documents/)
- [PDF-Dateien in Python zusammenführen](/pdf/de/python-net/merge-pdf-documents/)
- [PDF‑Dateien in Python optimieren](/pdf/de/python-net/optimize-pdf/)
- [PDF‑Dokumente in Python manipulieren](/pdf/de/python-net/manipulate-pdf-document/)

