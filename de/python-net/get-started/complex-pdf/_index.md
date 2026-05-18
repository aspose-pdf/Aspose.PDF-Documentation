---
title: Erstellen eines komplexen PDFs
linktitle: Erstellen eines komplexen PDFs
type: docs
weight: 30
url: /de/python-net/complex-pdf-example/
description: Aspose.PDF for Python via .NET ermöglicht das Erstellen komplexerer Dokumente, die Bilder, Textfragmente und Tabellen in einem Dokument enthalten.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Erstellen eines komplexen PDFs mit Python
Abstract: Dieser Artikel erweitert den grundlegenden PDF-Erstellungsprozess, der im Beispiel "Hello, World" demonstriert wird, indem gezeigt wird, wie man mit Python und Aspose.PDF ein komplexeres PDF‑Dokument erstellt. Das Beispieldokument wurde für ein fiktives Passagierfährenunternehmen entwickelt und enthält ein Bild, zwei Textfragmente (eine Überschrift und einen Absatz) sowie eine Tabelle. Der Vorgang umfasst mehrere Schritte – das Instanziieren eines `Document`‑Objekts zum Erstellen eines leeren PDFs, das Hinzufügen einer `Page` und anschließend das Einfügen eines `Image` in die Seite. Ein `TextFragment` wird für die Überschrift mit der Schrift Arial in Größe 24 pt und zentrierter Ausrichtung erstellt, das dann zu den Absätzen der Seite hinzugefügt wird. Ein zweites `TextFragment` wird für die Beschreibung mit der Schrift Times New Roman in Größe 14 pt und linker Ausrichtung hinzugefügt. Anschließend wird eine Tabelle erstellt und mit spezifischen Spaltenbreiten, Rahmen und Abständen formatiert. Die Tabelle enthält eine Kopfzeile mit hervorgehobenen Zellen und mehrere Datenzeilen, die durch Iteration erzeugt werden
---

Der [Hallo, Welt](/pdf/de/python-net/hello-world-example/) Beispiel zeigte einfache Schritte, um ein PDF-Dokument mit Python und Aspose.PDF zu erstellen. In diesem Artikel werfen wir einen Blick auf die Erstellung eines komplexeren Dokuments mit Aspose.PDF for Python. Als Beispiel nehmen wir ein Dokument von einem fiktiven Unternehmen, das Passagierfähren betreibt. Unser Dokument wird ein Bild, zwei Textfragmente (Überschrift und Absatz) und eine Tabelle enthalten.

Wenn wir ein Dokument von Grund auf neu erstellen, müssen wir bestimmte Schritte befolgen:

1. Instanziiere ein [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Objekt. In diesem Schritt werden wir ein leeres PDF-Dokument mit ein paar Metadaten, aber ohne Seiten, erstellen.
1. Hinzufügen [Seite](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) zum Dokumentobjekt. Jetzt hat unser Dokument eine Seite.
1. Hinzufügen [Bild](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/) zur Page.
1. Erstelle ein [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) für die Kopfzeile. Für die Kopfzeile verwenden wir die Arial Font mit einer Schriftgröße von 24pt und zentrierter Ausrichtung.
1. Header zur Page hinzufügen [Absätze](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. Erstelle ein [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) für die Beschreibung. Für die Beschreibung verwenden wir die Arial Font mit einer Schriftgröße von 24pt und zentrierter Ausrichtung.
1. Beschreibung zu den Page-Absätzen hinzufügen.
1. Table erstellen und formatieren. Spaltenbreite, Ränder, Padding und Font festlegen.
1. Tabelle zur Seite hinzufügen [Absätze](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. Speichere ein Dokument "Complex.pdf".

```python
from datetime import timedelta
import aspose.pdf as ap


def run_complex(self):

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()

    # Add image
    imageFileName = self.data_dir + "logo.png"
    page.add_image(imageFileName, ap.Rectangle(20, 730, 120, 830, True))

    # Add Header
    header = ap.text.TextFragment("New ferry routes in Fall 2029")
    header.text_state.font = ap.text.FontRepository.find_font("Arial")
    header.text_state.font_size = 24
    header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    header.position = ap.text.Position(130, 720)
    page.paragraphs.add(header)

    # Add description
    descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. \
    Ferry service is operating at half capacity and on a reduced schedule. Expect lineups."
    description = ap.text.TextFragment(descriptionText)
    description.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # Add table
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray)
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.BOX, 0.5, ap.Color.black)
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font("Helvetica")

    headerRow = table.rows.add()
    headerRow.cells.add("Departs City")
    headerRow.cells.add("Departs Island")

    i = 0
    while i < headerRow.cells.count:
        headerRow.cells[i].background_color = ap.Color.gray
        headerRow.cells[
            i
        ].default_cell_text_state.foreground_color = ap.Color.white_smoke
        i += 1

    time = timedelta(hours=6, minutes=0)
    incTime = timedelta(hours=0, minutes=30)

    i = 0
    while i < 10:
        dataRow = table.rows.add()
        dataRow.cells.add(str(time))
        time = time.__add__(incTime)
        dataRow.cells.add(str(time))
        i += 1

    page.paragraphs.add(table)

    document.save(self.data_dir + "Complex.pdf")
```
