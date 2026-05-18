---
title: AnhГ¤nge zu PDF in Python hinzufГјgen
linktitle: Anhang zu einem PDF-Dokument hinzufГјgen
type: docs
weight: 10
url: /de/python-net/add-attachment-to-pdf-document/
description: Erfahren Sie, wie Sie DateianhГ¤nge zu PDF-Dokumenten in Python mit Aspose.PDF for Python via .NET hinzufГјgen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man AnhГ¤nge zu PDF mit Python hinzufГјgt
Abstract: "Dieser Artikel bietet eine schrittweise Anleitung, wie man AnhГ¤nge zu einer PDFвЂ‘Datei mit Python und der Aspose.PDFвЂ‘Bibliothek hinzufГјgt. Er beschreibt den Vorgang, ein neues PythonвЂ‘Projekt einzurichten, das erforderliche Aspose.PDFвЂ‘Paket zu importieren und ein `Document`вЂ‘Objekt zu erstellen. Der Artikel erklГ¤rt, wie man ein `FileSpecification`вЂ‘Objekt mit der gewГјnschten Datei und Beschreibung erstellt und dieses Objekt mithilfe der `add`вЂ‘Methode zur `EmbeddedFileCollection` des PDFвЂ‘Dokuments hinzufГјgt. Die `EmbeddedFileCollection` enthГ¤lt alle AnhГ¤nge innerhalb des PDFs. Ein CodeвЂ‘Snippet ist enthalten, um den Vorgang zu demonstrieren: Г–ffnen eines Dokuments, Einrichten einer Datei fГјr den Anhang, AnhГ¤ngen an die Anhangssammlung des Dokuments und Speichern des aktualisierten PDFs."
---

AnhГ¤nge kГ¶nnen eine breite Palette von Informationen enthalten und kГ¶nnen verschiedene Dateitypen haben. Dieser Artikel erklГ¤rt, wie man einen Anhang zu einer PDFвЂ‘Datei hinzufГјgt.

Verwenden Sie eingebettete PDF-AnhГ¤nge, wenn Sie unterstГјtzende Quelldateien, Tabellenkalkulationen, Bilder oder zugehГ¶rige Dokumente zusammen mit der Haupt-PDF verpacken mГјssen.

1. Erstellen Sie ein neues PythonвЂ‘Projekt.
1. Importieren Sie das Aspose.PDFвЂ‘Paket
1. Erstelle ein [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Objekt.
1. Erstelle ein [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) Objekt mit der Datei, die Sie hinzufГјgen, und Dateibeschreibung.
1. FГјgen Sie das [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) Objekt zu dem [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Objekts [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) Sammlung, mit der Sammlung's [hinzufГјgen](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) Methode.

Der [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) Die Sammlung enthГ¤lt alle AnhГ¤nge in der PDF-Datei. Der folgende Codeausschnitt zeigt, wie Sie einen Anhang zu einem PDF-Dokument hinzufГјgen.

```python
from os import path
import aspose.pdf as ap

def add_attachments(infile, attachment_path, outfile):
    with ap.Document(infile) as document:
        file_spec = ap.FileSpecification(attachment_path, "Sample text file")
        document.embedded_files.add(path.basename(attachment_path), file_spec)
        document.save(outfile)
```

## Verwandte Anhangsthemen

- [Arbeiten mit PDF-AnhГ¤ngen in Python](/pdf/de/python-net/attachments/)
- [AnhГ¤nge aus PDF in Python entfernen](/pdf/de/python-net/removing-attachment-from-an-existing-pdf/)
- [PDF-Portfolios in Python erstellen und verwalten](/pdf/de/python-net/portfolio/)

