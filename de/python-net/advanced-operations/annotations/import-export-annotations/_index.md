---
title: Importieren und Exportieren von Anmerkungen mit Python
linktitle: Import und Export von Anmerkungen
type: docs
weight: 80
url: /de/python-net/import-export-annotations/
description: Erfahren Sie, wie Sie Anmerkungen aus einem PDF importieren und sie mithilfe von Aspose.PDF for Python via .NET in ein neues PDF-Dokument exportieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Übertragen Sie PDF-Anmerkungen zwischen Dokumenten in Python.
Abstract: Dieser Artikel erklärt, wie man Anmerkungen aus einer Quell-PDF kopiert und sie mithilfe von Aspose.PDF for Python via .NET in ein neues PDF-Dokument exportiert. Der Leitfaden unterteilt den Vorgang in kleine Schritte, einschließlich des Ladens der Quelldatei, des Erstellens des Ziel-Dokuments, dem Hinzufügen einer Seite, dem Kopieren von Anmerkungen von der ersten Seite und dem Speichern des Ergebnisses.
---

Dieser Artikel zeigt, wie man Anmerkungen aus einer bestehenden PDF importiert und sie mithilfe von Aspose.PDF for Python via .NET in ein neues PDF-Dokument exportiert.

Das Beispiel liest Anmerkungen von der ersten Seite einer Quelldatei, erstellt ein neues PDF, fügt eine leere Seite hinzu und kopiert jede Anmerkung auf diese neue Seite. Dieser Ansatz ist nützlich, wenn Sie Kommentare, Markierungen oder Überprüfungsnotizen in ein separates Ausgabedokument verschieben müssen.

## Lade die Quell-PDF

Erstelle ein `Document` Objekt für die Eingabedatei, die bereits Anmerkungen enthält. Dieses Objekt bietet Zugriff auf die Sammlung von Seiten und die auf jeder Seite gespeicherten Anmerkungen.

```python
source_document = ap.Document(infile)
```

## Erstelle das Ziel-PDF

Als Nächstes erstellen Sie ein leeres PDF-Dokument, das die importierten Anmerkungen erhalten wird. In diesem Stadium enthält das Ziel-Dokument keine Seiten.

```python
destination_document = ap.Document()
```

## Seite für exportierte Anmerkungen hinzufügen

Da Anmerkungen zu einer Seite gehören müssen, fügen Sie dem Zieldokument eine neue Seite hinzu, bevor Sie etwas kopieren.

```python
page = destination_document.pages.add()
```

## Kopiere Anmerkungen von der Quellseite

Iterieren Sie durch die Annotationssammlung auf der ersten Seite des Quell-PDFs und fügen Sie jede Anmerkung der neuen Seite im Zieldokument hinzu.

Das zweite Argument in `page.annotations.add(annot, True)` weist Aspose.PDF an, die Anmerkung in die Zielseite zu kopieren, anstatt nur die vorhandene Objektreferenz wiederzuverwenden.

```python
for annot in source_document.pages[1].annotations:
    page.annotations.add(annot, True)
```

## Speichern Sie das Ausgabedokument

Nachdem alle Anmerkungen kopiert wurden, speichern Sie das Zieldokument, um die endgültige PDF-Datei zu erstellen.

```python
destination_document.save(outfile)
```

## Vollständiges Beispiel

Der folgende Code kombiniert alle Schritte zu einer wiederverwendbaren Funktion:

```python
import sys
import aspose.pdf as ap
from os import path


sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def import_export(infile, outfile):
    """
    Import annotations from one PDF document and export them to a new PDF document.
    """
    source_document = ap.Document(infile)
    destination_document = ap.Document()

    page = destination_document.pages.add()

    for annot in source_document.pages[1].annotations:
        page.annotations.add(annot, True)

    destination_document.save(outfile)
```

## Verwandte Themen

- [Interaktive Anmerkungen](/python-net/interactive-annotations/)
- [Markup-Anmerkungen](/python-net/markup-annotations/)
- [Medien-Anmerkungen](/python-net/media-annotations/)
- [Sicherheitsanmerkungen](/python-net/security-annotations/)
- [Form‑Annotationen](/python-net/shape-annotations/)
- [Textbasierte Anmerkungen](/python-net/text-based-Annotations/)
- [Wasserzeichen-Annotationen](/python-net/watermark-annotations/)
