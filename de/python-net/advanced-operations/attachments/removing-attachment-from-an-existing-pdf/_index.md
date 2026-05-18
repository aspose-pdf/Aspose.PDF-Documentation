---
title: AnhГ¤nge aus PDF in Python entfernen
linktitle: Entfernen von Anhang aus einer bestehenden PDF
type: docs
weight: 30
url: /de/python-net/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF kann AnhГ¤nge aus Ihren PDF-Dokumenten entfernen. Verwenden Sie die Python PDFвЂ‘API, um AnhГ¤nge in PDFвЂ‘Dateien mit Aspose.PDF fГјr Python via .NETвЂ‘Bibliothek zu entfernen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man AnhГ¤nge aus PDF mit Python lГ¶scht
Abstract: "Dieser Artikel beschreibt, wie man AnhГ¤nge aus PDFвЂ‘Dateien mit Aspose.PDF fГјr Python entfernt. AnhГ¤nge in einem PDFвЂ‘Dokument werden in der `EmbeddedFiles`вЂ‘Sammlung des `Document`вЂ‘Objekts gespeichert. Um alle AnhГ¤nge aus einem PDF zu lГ¶schen, kГ¶nnen Sie die `delete()`вЂ‘Methode der `EmbeddedFiles`вЂ‘Sammlung aufrufen und anschlieГџend das aktualisierte Dokument mit der `save()`вЂ‘Methode des `Document`вЂ‘Objekts speichern. Ein CodeвЂ‘Snippet wird bereitgestellt, um diesen Vorgang zu demonstrieren und die Schritte zu zeigen: Г–ffnen eines Dokuments, LГ¶schen seiner AnhГ¤nge und Speichern der modifizierten Datei."
---

Aspose.PDF fГјr Python kann AnhГ¤nge aus PDFвЂ‘Dateien entfernen. Die AnhГ¤nge eines PDFвЂ‘Dokuments werden im DocumentвЂ‘Objekt gehalten. [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) Sammlung.

Dieser Arbeitsablauf ist nГјtzlich, wenn Sie veraltete eingebettete Dateien bereinigen, die PaketgrГ¶Гџe reduzieren oder ein PDF fГјr die Weiterverteilung ohne angehГ¤ngte Quelldateien vorbereiten mГјssen.

Um alle mit einer PDF-Datei verbundenen AnhГ¤nge zu lГ¶schen:

1. Rufen Sie die [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) collection\u0027s [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) Methode.
1. Speichern Sie die aktualisierte Datei mit der [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Objekts [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) Methode.

Das folgende CodeвЂ‘Snippet zeigt, wie man AnhГ¤nge aus einem PDFвЂ‘Dokument entfernt.

```python

import aspose.pdf as ap

def remove_attachment(infile, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        document.embedded_files.delete()
        document.save(outfile)
```

## Entfernen Sie einen bestimmten Anhang nach Namen

Wenn Sie nur einen Anhang entfernen und die anderen behalten mГјssen, verwenden Sie die [delete_by_key()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/delete_by_key/) Methode und Гјbergeben Sie den Namen des Anhangs.

Um einen bestimmten Anhang zu lГ¶schen:

1. Г–ffnen Sie die Quell-PDF-Datei.
1. Anruf `document.embedded_files.delete_by_key(attachment_name)`.
1. Speichern Sie die aktualisierte PDF-Datei.

Das folgende CodeвЂ‘Snippet entfernt einen Anhang anhand seines Namens.

```python

import aspose.pdf as ap

def remove_attachment(infile, attachment_name, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        document.embedded_files.delete_by_key(attachment_name)
        document.save(outfile)
```

## Verwandte Anhangsthemen

- [Arbeiten mit PDF-AnhГ¤ngen in Python](/pdf/de/python-net/attachments/)
- [AnhГ¤nge zu PDF in Python hinzufГјgen](/pdf/de/python-net/add-attachment-to-pdf-document/)
- [PDF-Portfolios in Python erstellen und verwalten](/pdf/de/python-net/portfolio/)

