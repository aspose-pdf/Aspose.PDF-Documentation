---
title: Beispiel für Hello World mit Python
linktitle: Hello World Beispiel
type: docs
weight: 20
url: /de/python-net/hello-world-example/
description: Dieses Beispiel demonstriert, wie man ein einfaches PDF Document mit dem Text Hello World unter Verwendung von Aspose.PDF for Python via .NET erstellt.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hello World Beispiel via Python
Abstract: Dieser Artikel bietet ein Hello World Beispiel, das die Aspose.PDF for Python via .NET Bibliothek verwendet, um ein PDF Document zu erstellen. Das Beispiel demonstriert die grundlegenden Schritte zur Nutzung der Aspose.PDF API, indem ein PDF mit dem Text "Hello World!" erzeugt wird. Der Vorgang beinhaltet das Instanziieren eines `Document`‑Objekts, das Hinzufügen einer `Page`, das Erstellen eines `TextFragment`‑Objekts, das Festlegen von Texteigenschaften wie Schriftgröße und Farbe sowie die Verwendung eines `TextBuilder`, um den Text zur Seite hinzuzufügen. Das resultierende PDF wird dann unter dem Namen "HelloWorld_out.pdf" gespeichert. Der Artikel enthält ein vollständiges Python‑Code‑Snippet, das diese Schritte illustriert und als Einführungsleitfaden zur Nutzung der Bibliothek dient.
---

Ein "Hello World" Beispiel zeigt die einfachste Syntax und das einfachste Programm in jeder beliebigen Programmiersprache. Entwickler werden in die grundlegende Syntax der Programmiersprache eingeführt, indem sie lernen, "Hello World" auf dem Bildschirm auszugeben. Daher beginnen wir traditionell unsere Bekanntmachung mit unserer Bibliothek damit.

In diesem Artikel erstellen wir ein PDF-Dokument, das den Text "Hello World!" enthält. Nachdem Sie **Aspose.PDF for Python via .NET** in Ihrer Umgebung installiert haben, können Sie das untenstehende Codebeispiel ausführen, um zu sehen, wie die Aspose.PDF-API funktioniert.

Der nachstehende Codeabschnitt folgt diesen Schritten:

1. Instanziiere ein [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Objekt
1. Hinzufügen [Seite](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) zum Dokumentobjekt
1. Erstelle ein [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) Objekt
1. Textfarben festlegen
1. Einen Text-Builder erstellen
1. Hinzufügen [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) zur Page
1. [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) resultierendes PDF Document

Der folgende Codeabschnitt ist ein "Hello World"-Programm, das die Funktionalität von Aspose.PDF for Python via .NET API demonstriert.

```python
from datetime import timedelta
import aspose.pdf as ap


def run_simple(self):
    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Add text to new page
    textFragment = ap.text.TextFragment("Hello, world!")
    textFragment.position = ap.text.Position(100, 600)

    textFragment.text_state.font_size = 12
    textFragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    textFragment.text_state.background_color = ap.Color.blue
    textFragment.text_state.foreground_color = ap.Color.yellow

    # Create TextBuilder object
    textBuilder = ap.text.TextBuilder(page)

    # Append the text fragment to the PDF page
    textBuilder.append_text(textFragment)

    document.save(self.data_dir + "HelloWorld_out.pdf")
```
