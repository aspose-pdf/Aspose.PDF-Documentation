---
title: Bildstempel zu PDF in Python hinzufügen
linktitle: Bildstempel in PDF-Datei
type: docs
weight: 10
url: /de/python-net/image-stamps-in-pdf-page/
description: Erfahren Sie, wie Sie Bildstempel zu PDF-Seiten in Python hinzufügen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man Bildstempel zu PDF mit Python hinzufügt
Abstract: Dieser Artikel bietet eine umfassende Anleitung zum Hinzufügen von `ImageStamp`-Stempeln zu PDF‑Dateien mithilfe der Aspose.PDF‑Bibliothek für Python. Er beschreibt die Verwendung der `ImageStamp`‑Klasse, die die Anpassung von bildbasierten Stempeln ermöglicht, einschließlich Eigenschaften wie Höhe, Breite, Deckkraft und Drehung. Der Vorgang umfasst das Erstellen eines `Document`‑Objekts und eines `ImageStamp`‑Objekts mit den gewünschten Eigenschaften und das Hinzufügen des Stempels zu einer bestimmten Seite des PDFs mithilfe der `add_stamp()`‑Methode. Der Artikel enthält Python‑Code‑Snippets, die demonstrieren, wie ein `ImageStamp` auf ein PDF angewendet und seine Qualität über die `quality`‑Eigenschaft gesteuert werden kann, welche die Bildqualität in Prozent angibt. Zusätzlich erklärt der Artikel, wie `ImageStamp`s als Hintergründe in schwebenden Boxen mit der `FloatingBox`‑Klasse verwendet werden können, und liefert ein weiteres Code‑Beispiel, um zu zeigen, wie dies implementiert werden kann. Diese Anleitung dient Entwicklern als nützliche Ressource, um PDFs mit `ImageStamp`‑Stempeln mithilfe von Aspose.PDF zu erweitern.
---

## Hinzufügen von ImageStamp in PDF-Datei

Sie können das [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) Klasse, um einen ImageStamp zu einer PDF-Datei hinzuzufügen. Der [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) Klasse stellt die für die Erstellung eines bildbasierten Stempels benötigten Eigenschaften bereit, wie Höhe, Breite, Opazität usw. Der Stempel kann positioniert, skaliert, rotiert und teilweise transparent gemacht werden, wodurch Wasserzeichen, Markenkennzeichnung oder Anmerkungen ermöglicht werden.

Das folgende Code‑Snippet zeigt, wie ein Bildstempel zur PDF‑Datei hinzugefügt wird.

1. Laden Sie das PDF mit 'ap.Document()'.
1. Erstellen Sie einen Bildstempel mit 'ImageStamp()'.
1. Stempel-Eigenschaften konfigurieren.
1. Fügen Sie den Stempel zur Zielseite hinzu.
1. Speichere das bearbeitete PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_stamp(infile, input_image_file, outfile):
    document = ap.Document(infile)
    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.background = True
    image_stamp.x_indent = 100
    image_stamp.y_indent = 100
    image_stamp.height = 300
    image_stamp.width = 300
    image_stamp.rotate = ap.Rotation.ON270
    image_stamp.opacity = 0.5

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## Steuern Sie die Bildqualität beim Hinzufügen eines Stempels

Beim Hinzufügen eines Bildes als Stempelobjekt können Sie die Qualität des Bildes steuern. Der [quality](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/#properties) Eigenschaft der [ImageStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/imagestamp/) Klasse wird zu diesem Zweck verwendet. Sie gibt die Qualität des Bildes in Prozent an (gültige Werte sind 0..100).
Durch das Festlegen der quality‑Eigenschaft können Sie die Bildauflösung reduzieren, um die PDF‑Größe zu optimieren, oder eine höhere Treue für Klarheit beibehalten.

1. Öffnen Sie das PDF-Dokument.
1. Erstellen Sie einen ImageStamp.
1. Legen Sie die Bildqualität fest.
1. Fügen Sie den Stempel zur Zielseite hinzu.
1. Speichere das bearbeitete PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_stamp_with_quality_control(infile, input_image_file, outfile):
    document = ap.Document(infile)

    image_stamp = ap.ImageStamp(input_image_file)
    image_stamp.quality = 10

    document.pages[1].add_stamp(image_stamp)
    document.save(outfile)
```

## Image Stamp als Hintergrund in schwebender Box

Erstelle ein [FloatingBox](https://reference.aspose.com/pdf/python-net/aspose.pdf/floatingbox/) In einem PDF ein Bild als Hintergrund anwenden. Es zeigt auch, wie man Text hinzufügt, Rahmen festlegt, die Hintergrundfarbe setzt und die Box präzise auf der Seite positioniert. Dies ist nützlich, um visuell ansprechende PDF‑Inhalte wie Hinweisfelder, Banner oder hervorgehobene Abschnitte mit Text über Bildern zu erstellen.

1. Öffnen oder erstellen Sie ein PDF-Dokument.
1. Erstellen Sie ein 'FloatingBox'-Objekt.
1. Fügen Sie Textinhalt zur Box hinzu.
1. Legen Sie die Rahmen- und Hintergrundfarbe der Box fest.
1. Füge ein Hintergrundbild hinzu.
1. Füge die FloatingBox zur Seite hinzu.
1. Speichern Sie das PDF-Dokument.

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_as_background_in_floating_box(infile, input_image_file, outfile):
    document = ap.Document(infile)
    page = document.pages[1]
    # Create FloatingBox object
    box = ap.FloatingBox(200.0, 100.0)
    # Set left position for FloatingBox
    box.left = 40
    # Set Top position for FloatingBox
    box.top = 80
    # Set the Horizontal alignment for FloatingBox
    box.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Add text fragment to paragraphs collection of FloatingBox
    box.paragraphs.add(ap.text.TextFragment("Text in Floating Box"))
    # Set border for FloatingBox
    box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    img = ap.Image()
    img.file = input_image_file
    # Add background image
    box.background_image = img
    # Set background color for FloatingBox
    box.background_color = ap.Color.yellow
    # Add FloatingBox to paragraphs collection of page object
    page.paragraphs.add(box)
    # Save the PDF document
    document.save(outfile)
```

## Verwandte Stempel-Themen

- [PDF-Seiten in Python stempeln](/pdf/de/python-net/stamping/)
- [Seitenstempel zu PDF in Python hinzufügen](/pdf/de/python-net/page-stamps-in-the-pdf-file/)
- [Textstempel zu PDF in Python hinzufügen](/pdf/de/python-net/text-stamps-in-the-pdf-file/)
- [Seitenzahlen zum PDF in Python hinzufügen](/pdf/de/python-net/add-page-number/)