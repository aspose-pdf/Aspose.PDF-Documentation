---
title: Bilder aus PDF-Datei mit Python löschen
linktitle: Bilder löschen
type: docs
weight: 20
url: /de/python-net/delete-images-from-pdf-file/
description: Erfahren Sie, wie Sie bestimmte oder alle Bilder aus PDF-Dateien in Python löschen.
lastmod: "2026-05-18"
TechArticle: true
AlternativeHeadline: Bilder aus PDF-Dateien mit Python löschen
Abstract: Dieser Artikel zeigt, wie man Bilder aus PDF-Dokumenten mit Aspose.PDF for Python via .NET löscht. Er behandelt das Entfernen einer bestimmten Bildressource und das Löschen aller Bilder von einer ausgewählten Seite.
---

Verwenden Sie diese Seite, wenn Sie unnötige Grafiken entfernen, die PDF-Größe reduzieren oder sensible visuelle Inhalte aus einem Dokument bereinigen müssen.

## Bilder aus PDF-Datei löschen

Verwenden Sie die folgenden Schritte, um ein Bild aus einer Seite zu löschen:

1. Laden Sie das Quell-PDF mit `ap.Document(infile)`.
1. Wählen Sie die Seite und den Bild‑Ressourcen‑Index aus.
1. Lösche das Bild mit `resources.images.delete(index)`.
1. Speichere das aktualisierte PDF.

```python
import aspose.pdf as ap


def delete_image(infile, outfile):
    document = ap.Document(infile)
    document.pages[1].resources.images.delete(1)
    document.save(outfile)
```

## Alle Bilder von einer Seite löschen

Verwenden Sie dieses Beispiel, um jedes Bild von einer bestimmten Seite zu entfernen.

```python
import aspose.pdf as ap


def delete_all_images_from_page(infile, outfile, page_number):
    document = ap.Document(infile)
    page = document.pages[page_number]

    while len(page.resources.images) != 0:
        page.resources.images.delete(1)

    document.save(outfile)
```

## Verwandte Bildthemen

- [Arbeiten mit Bildern in PDF mit Python](/pdf/de/python-net/working-with-images/)
- [Bilder in vorhandenen PDF-Dateien ersetzen](/pdf/de/python-net/replace-image-in-existing-pdf-file/)
- [Bilder aus PDF-Dateien extrahieren](/pdf/de/python-net/extract-images-from-pdf-file/)
- [Bilder zu bestehenden PDF-Dateien hinzufügen](/pdf/de/python-net/add-image-to-existing-pdf-file/)