---
title: Textstempel zu PDF in Python hinzufügen
linktitle: Textstempel in PDF-Datei
type: docs
weight: 20
url: /de/python-net/text-stamps-in-the-pdf-file/
description: Erfahren Sie, wie Sie Textstempel zu PDF-Dokumenten in Python hinzufügen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man Textstempel in PDF mit Python hinzufügt
Abstract: Dieser Artikel bietet eine umfassende Anleitung zum Hinzufügen von Textstempeln zu PDF-Dateien mithilfe der Aspose.PDF-Bibliothek für Python. Er erläutert die Verwendung der `TextStamp`‑Klasse, um anpassbare Textstempel mit Eigenschaften wie Schriftgröße, Stil, Farbe und Ausrichtung zu erstellen. Der Artikel enthält Code‑Snippets, die zeigen, wie ein einfacher Textstempel hinzugefügt, die Textausrichtung konfiguriert und erweiterte Render‑Modi wie Fill‑Stroke‑Text angewendet werden. Der erste Abschnitt erklärt die Erstellung eines `Document`‑ und `TextStamp`‑Objekts, das Festlegen von Texteigenschaften und das Hinzufügen des Stempels zu einer bestimmten Seite. Der zweite Abschnitt führt die `text_alignment`‑Eigenschaft ein, um Text horizontal und vertikal auszurichten, und liefert ein Code‑Beispiel für das Zentrieren von Text auf einer PDF‑Seite. Der letzte Abschnitt behandelt Render‑Modi und demonstriert, wie man Fill‑Stroke‑Text mithilfe eines `TextState`‑Objekts hinzufügt, um die Strichfarbe und den Render‑Modus festzulegen, bevor er an einen Stempel gebunden wird. Jeder Abschnitt wird von praktischen Beispielen begleitet, um das Verständnis und die Implementierung zu erleichtern.
---

## Hinzufügen von Textstempeln mit Python

Sie können verwenden [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) Klasse, um einen Textstempel in einer PDF-Datei hinzuzufügen. [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) Die Klasse stellt Eigenschaften bereit, die zum Erstellen eines textbasierten Stempels erforderlich sind, wie Schriftgröße, Schriftstil und Schriftfarbe usw. Um einen Textstempel hinzuzufügen, müssen Sie ein Document-Objekt und ein TextStamp-Objekt mit den erforderlichen Eigenschaften erstellen. Anschließend können Sie die [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) Methode der Page, um den Stempel in das PDF einzufügen. Das folgende Code‑Snippet zeigt, wie Sie einen Textstempel in die PDF‑Datei einfügen. Dies ist nützlich, um Anmerkungen, Wasserzeichen oder Beschriftungen zu PDF‑Seiten hinzuzufügen.

1. Öffnen Sie das PDF-Dokument.
1. Erstelle ein TextStamp-Objekt.
1. Setze das Hintergrundverhalten des Stempels.
1. Positioniere den Stempel auf der Seite.
1. Drehe den Stempel bei Bedarf.
1. Lege Texteigenschaften fest.
1. Füge den Stempel zu einer Seite hinzu.
1. Speichern Sie das modifizierte PDF‑Dokument.

```python
import sys
import aspose.pdf as ap
from os import path

def add_text_stamp(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    # Create text stamp
    text_stamp = ap.TextStamp("Sample Stamp")
    # Set whether stamp is background
    text_stamp.background = True
    # Set origin
    text_stamp.x_indent = 100
    text_stamp.y_indent = 100
    # Rotate stamp
    text_stamp.rotate = ap.Rotation.ON90
    # Set text properties
    text_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_stamp.text_state.font_size = 14.0
    text_stamp.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    text_stamp.text_state.foreground_color = ap.Color.dark_green
    # Add stamp to particular page
    document.pages[1].add_stamp(text_stamp)

    document.save(output_file_name)
```

## Verwandte Stempel-Themen

- [PDF-Seiten in Python stempeln](/pdf/de/python-net/stamping/)
- [Seitenstempel zu PDF in Python hinzufügen](/pdf/de/python-net/page-stamps-in-the-pdf-file/)
- [Bildstempel zu PDF in Python hinzufügen](/pdf/de/python-net/image-stamps-in-pdf-page/)
- [Seitenzahlen zum PDF in Python hinzufügen](/pdf/de/python-net/add-page-number/)