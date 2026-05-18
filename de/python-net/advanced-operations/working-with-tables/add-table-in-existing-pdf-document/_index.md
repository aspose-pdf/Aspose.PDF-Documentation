---
title: Tabellen zu PDF in Python hinzufügen
linktitle: Tabellen hinzufügen
type: docs
weight: 10
url: /de/python-net/adding-tables/
description: Erfahren Sie, wie Sie Tabellen zu vorhandenen PDF‑Dokumenten in Python hinzufügen und konfigurieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Fügen Sie Tabellen zu PDF‑Dokumenten mit Python hinzu und formatieren Sie sie.
Abstract: Dieser Artikel erklärt, wie man Tabellen in PDF-Dokumenten mit Aspose.PDF for Python via .NET hinzufügt und konfiguriert. Er behandelt die Tabellenerstellung, Rahmen, Ränder, Abstand, Zeilen‑ und Spaltenüberspannungen, das AutoFit‑Verhalten, die Handhabung der Tabellenbreite, das Einfügen von Bildern in Zellen und die Steuerung der Darstellung über Seiten hinweg.
---

Das Hinzufügen von Tabellen zu bestehenden PDF-Dokumenten ist ein häufiges Anliegen für die Datenpräsentation, strukturierte Inhalte und Berichterstellung. **Aspose.PDF for Python via .NET** stellt eine praktische API zum Einfügen und Formatieren von Tabellen in bestehenden PDFs bereit.

Dieses Handbuch bietet Schritt‑für‑Schritt‑Beispiele für die Tabellenerstellung, Spaltengrößen, Rahmen, Zeilen und Zellen sowie das Speichern des geänderten Dokuments. Es behandelt außerdem erweiterte Optionen wie Zellenrahmen, Ränder, Abstand und AutoFit‑Einstellungen für die dynamische Tabellengröße.

Verwenden Sie diese Seite, wenn Sie neuen Tabellen zu bestehenden PDFs hinzufügen und deren Layoutverhalten in Python steuern müssen.

## Grundlegende Tabellen erstellen

### Tabelle erstellen

Dieses Beispiel zeigt, wie man eine Tabelle in einem PDF-Dokument mit Rahmen und mehreren Zeilen erstellt.

1. Erstellen Sie ein neues PDF-Dokument.
1. Fügt dem Dokument eine leere Seite hinzu.
1. Initialisieren Sie die Tabelle.
1. Legen Sie den Gesamtrahmen der Tabelle fest.
1. Legen Sie den Rand für einzelne Zellen fest.
1. Zeilen und Zellen hinzufügen.
1. Fügen Sie die Tabelle in die Seite ein.
1. Speichern Sie das PDF im angegebenen Pfad.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def create_table(outfile: str) -> None:
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()
    # Initializes a new instance of the Table
    table = ap.Table()
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.light_gray)
    # Create a loop to add 10 rows
    for row_count in range(10):
        # Add row to table
        row = table.rows.add()
        # Add table cells
        row.cells.add("Column (" + str(row_count) + ", 1)")
        row.cells.add("Column (" + str(row_count) + ", 2)")
        row.cells.add("Column (" + str(row_count) + ", 3)")
    # Add table object to first page of input document
    page.paragraphs.add(table)

    # Save updated document containing table object
    document.save(outfile)
```

### Bilder zu Tabellenzellen hinzufügen

Dieses Codebeispiel zeigt, wie man Bilder in Tabellenzellen in einem PDF-Dokument einfügt.

1. Erstellen Sie ein neues PDF-Dokument.
1. Initialisieren Sie die Tabelle.
1. Spaltenbreiten in Punkten festlegen.
1. Ein Textfragment wird zur ersten Zelle hinzugefügt.
1. Eine 'ap.Image()'-Instanz wird der zweiten Zelle hinzugefügt.
1. Setzen Sie den Pfad zur Bilddatei mit 'img.file'.
1. Die 'img.fix_width' und 'img.fix_height' steuern die Bildgröße innerhalb der Zelle.
1. Fügen Sie die Tabelle in die PDF‑Seite ein.
1. Speichern Sie das PDF.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_image(image: str, outfile: str) -> None:
    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()
    # Set width for table cells
    table.column_widths = "200 100"

    # Create row object and add it to table instance
    row = table.rows.add()
    # Create cell object and add it to row instance
    cell = row.cells.add()
    # Add textfragment to paragraphs collection of cell object
    cell.paragraphs.add(ap.text.TextFragment(image))
    # Create an image instance
    img = ap.Image()
    # Set image type as SVG
    # Path for source file
    img.file = image
    # Set width for image instance
    img.fix_width = 50
    # Set height for image instance
    img.fix_height = 50
    # Add another cell to row object
    cell = row.cells.add()
    # Add SVG image to paragraphs collection of recently added cell instance
    cell.paragraphs.add(img)

    # Add table to paragraphs collection of page object
    page.paragraphs.add(table)
    # Save PDF file
    document.save(outfile)
```

Sie können SVG-Bilder in Tabellenzellen eines PDF-Dokuments einfügen:

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_svg_image(images: list[str], outfile: str) -> None:
    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()
    # Set width for table cells
    table.column_widths = "200 100"
    for image in images:
        # Create row object and add it to table instance
        row = table.rows.add()
        # Create cell object and add it to row instance
        cell = row.cells.add()
        # Add textfragment to paragraphs collection of cell object
        cell.paragraphs.add(ap.text.TextFragment(image))
        # Create an image instance
        img = ap.Image()
        # Set image type as SVG
        img.file_type = ap.ImageFileType.SVG
        # Path for source file
        img.file = image
        # Set width for image instance
        img.fix_width = 50
        # Set height for image instance
        img.fix_height = 50
        # Add another cell to row object
        cell = row.cells.add()
        # Add SVG image to paragraphs collection of recently added cell instance
        cell.paragraphs.add(img)

    # Add table to paragraphs collection of page object
    page.paragraphs.add(table)
    # Save PDF file
    document.save(outfile)
```

### ColSpan und RowSpan in Tabellen

Dieses Beispiel zeigt, wie man Tabellenzellen vertikal und horizontal zusammenführt, um komplexe Tabellengestaltungen zu erstellen.

1. Legen Sie den Gesamtrahmen der Tabelle fest.
1. Legen Sie die Standardzellenrahmen fest.
1. Führen Sie zwei Zellen horizontal zu einer zusammen.
1. Fügen Sie die Zelle vertikal über zwei Zeilen zusammen.
1. Zeile 5 berücksichtigt das Rowspan, indem sie die zusammengeführte Spalte überspringt.
1. Fügen Sie die Tabelle in die Seite ein.
1. Speichern Sie das PDF.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_rowspan_or_colspan(outfile: str) -> None:
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    # Initializes a new instance of the Table
    table = ap.Table()
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # Add 1st row to table
    row1 = table.rows.add()
    for cell_count in range(1, 5):
        # Add table cells
        row1.cells.add("Test 1" + str(cell_count))

    # Add 2nd row to table
    row2 = table.rows.add()
    row2.cells.add("Test 2 1")
    cell = row2.cells.add("Test 2 2")
    cell.col_span = 2
    row2.cells.add("Test 2 4")

    # Add 3rd row to table
    row3 = table.rows.add()
    row3.cells.add("Test 3 1")
    row3.cells.add("Test 3 2")
    row3.cells.add("Test 3 3")
    row3.cells.add("Test 3 4")

    # Add 4th row to table
    row4 = table.rows.add()
    row4.cells.add("Test 4 1")
    cell = row4.cells.add("Test 4 2")
    cell.row_span = 2
    row4.cells.add("Test 4 3")
    row4.cells.add("Test 4 4")

    # Add 5th row to table
    row5 = table.rows.add()
    row5.cells.add("Test 5 1")
    row5.cells.add("Test 5 3")
    row5.cells.add("Test 5 4")

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(outfile)
```

![ColSpan und RowSpan Demo](colspan_rowspan.png)

### Anwenden von Rahmen auf Tabellen und Zellen

Dieses Beispiel zeigt, wie man den Zellenabstand, die Tabellenränder festlegt und den Zeilenumbruch für Text in Tabellenzellen steuert.

1. Legen Sie die Breiten der Spalten fest.
1. Definieren Sie die Tabellen- und Zellenränder.
1. Innenabstand in Zellen festlegen für konsistente Abstände.
1. Wenden Sie die Polsterung standardmäßig auf alle Zellen an.
1. Text hinzufügen und Zeilenumbruch steuern.
1. Zeilen und Zellen hinzufügen.
1. Speichern Sie das PDF.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_borders(outfile: str) -> None:
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    tab1 = ap.Table()
    # Add the table in paragraphs collection of the desired section
    page.paragraphs.add(tab1)
    # Set with column widths of the table
    tab1.column_widths = "50 50 50"
    # Set default cell border using BorderInfo object
    tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # Set table border using another customized BorderInfo object
    tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # Create MarginInfo object and set its left, bottom, right and top margins
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # Set the default cell padding to the MarginInfo object
    tab1.default_cell_padding = margin
    # Create rows in the table and then cells in the rows
    row1 = tab1.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add()
    text = ap.text.TextFragment("col3 with large text string")
    row1.cells[2].paragraphs.add(text)
    row1.cells[2].is_word_wrapped = False
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # Save updated document containing table object
    document.save(outfile)
```

![Rand und Rahmen in PDF‑Tabelle](margin-border.png)

## Tabellenlayout und -größe

### Automatisches Anpassen von Spalten und Zeilen

Dieses Code‑Snippet zeigt, wie man Tabellenspaltenbreiten automatisch an die Seite anpasst.
Bitte beachten Sie, dass im Parameter table.column_widths = "50 50 50" – es sind Punkte. Aber Sie können auch Zentimeter (cm), Zoll oder % angeben.

1. Setzen Sie die anfänglichen Spaltenbreiten.
1. Passt Spalten automatisch an die Seitenbreite an.
1. Definieren Sie Zell- und Tabellengrenzen.
1. Der 'table.default_cell_padding' verwendet 'MarginInfo()' für konsistente Abstände innerhalb von Zellen.
1. Fügen Sie Zeilen mit 'table.rows.add()' hinzu und fügen Sie Zellen mit 'row.cells.add()' hinzu.
1. Speichern Sie das PDF.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def auto_fit(outfile: str) -> None:
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()

    page.paragraphs.add(table)

    table.column_widths = "50 50 50"
    table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_WINDOW

    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)

    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1)

    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5

    table.default_cell_padding = margin

    row1 = table.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add("col3")
    row2 = table.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")

    document.save(outfile)
```

### Komplexe PDF-Tabellen mit zusammengeführten Zellen und wiederholenden Spalten erstellen

Erstellen Sie eine erweiterte Tabelle in einem PDF mit Python und Aspose.PDF. Sie enthält zusammengeführte Kopfzeilenzellen, farbige Hintergründe, wiederholende Spalten und einen großen strukturierten Datensatz. Die Tabelle ist so konfiguriert, dass sie vertikale Umbrüche und komplexe Layouts für berichtsstilige Dokumente handhabt.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_table_hide_borders(outfile: str) -> None:
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Instantiate a table object that will be nested inside outerTable that will break inside the same page
    table = ap.Table()
    table.broken = ap.TableBroken.VERTICAL
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL)
    table.repeating_columns_count = 2
    page.paragraphs.add(table)

    # Add header Row
    row = table.rows.add()
    cell = row.cells.add("header 1")
    cell.col_span = 2
    cell.background_color = ap.Color.light_gray
    row.cells.add("header 3")

    cell2 = row.cells.add("header 4")
    cell2.col_span = 2
    cell2.background_color = ap.Color.light_blue
    row.cells.add("header 6")

    cell3 = row.cells.add("header 7")
    cell3.col_span = 2
    cell3.background_color = ap.Color.light_green
    cell4 = row.cells.add("header 9")

    cell4.col_span = 3
    cell4.background_color = ap.Color.light_coral
    row.cells.add("header 12")
    row.cells.add("header 13")
    row.cells.add("header 14")
    row.cells.add("header 15")
    row.cells.add("header 16")
    row.cells.add("header 17")

    row_counter = 0
    while row_counter < 3:
        # Create rows in the table and then cells in the rows
        row1 = table.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
        row1.cells.add("col " + str(row_counter) + ", 4")
        row1.cells.add("col " + str(row_counter) + ", 5")
        row1.cells.add("col " + str(row_counter) + ", 6")
        row1.cells.add("col " + str(row_counter) + ", 7")
        row1.cells.add("col " + str(row_counter) + ", 8")
        row1.cells.add("col " + str(row_counter) + ", 9")
        row1.cells.add("col " + str(row_counter) + ", 10")
        row1.cells.add("col " + str(row_counter) + ", 11")
        row1.cells.add("col " + str(row_counter) + ", 12")
        row1.cells.add("col " + str(row_counter) + ", 13")
        row1.cells.add("col " + str(row_counter) + ", 14")
        row1.cells.add("col " + str(row_counter) + ", 15")
        row1.cells.add("col " + str(row_counter) + ", 16")
        row1.cells.add("col " + str(row_counter) + ", 17")
        row_counter += 1

    document.save(outfile)
```

![Rahmen, Ränder und Abstände](set-border-style-margins-and-padding-of-table_1.png)

### Styling von Tabellenecken

Aspose.PDF for Python via .NET zeigt, wie man abgerundete Ecken auf eine Tabelle anwendet und den Randradius anpasst.

1. Erstellen Sie eine neue Tabelleninstanz.
1. Initialisieren Sie einen Rand für alle Seiten.
1. Eckradius festlegen.
1. Wenden Sie den abgerundeten Eckstil an.
1. Zeilen und Zellen hinzufügen.
1. Fügen Sie die Tabelle mit 'page.paragraphs.add(table)' in die PDF-Seite ein.
1. Speichern Sie das PDF-Dokument.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def create_table_with_round_corner(outfile: str) -> None:
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create a table
    table = ap.Table()

    # Create a blank BorderInfo object
    b_info = ap.BorderInfo(ap.BorderSide.ALL)

    # Set the border a rounded border where radius of round is 15
    b_info.rounded_border_radius = 15

    # Set the table corner style as Round
    table.corner_style = ap.BorderCornerStyle.ROUND

    # Set the table border information
    table.border = b_info

    # Create a loop to add 10 rows
    for row_count in range(0, 10):
        # Add row to table
        row = table.rows.add()
        # Add table cells
        row.cells.add("Column (" + str(row_count) + ", 1)")
        row.cells.add("Column (" + str(row_count) + ", 2)")
        row.cells.add("Column (" + str(row_count) + ", 3)")

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(outfile)
```

## Inhalte zu Tabellen hinzufügen

### Verwendung von HTML-Fragmenten in Zellen

Dieses Beispiel zeigt, wie man HTML-formatierten Inhalt in Tabellenzellen einfügt.

1. Tabellen- und Zellenränder festlegen.
1. HTML-Inhalt hinzufügen.
1. Zeilen hinzufügen. Eine Schleife fügt mehrere Zeilen mit HTML-formatiertem Inhalt in jeder Zelle hinzu.
1. Fügen Sie die Tabelle mit 'page.paragraphs.add(table)' in die PDF-Seite ein.
1. Speichern Sie das PDF-Dokument.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_html_fragments(outfile: str) -> None:
    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()

    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.ALL, 0.5, ap.Color.light_gray
    )
    # Create a loop to add 10 rows
    row_count = 1
    while row_count < 10:
        # Add row to table
        row = table.rows.add()
        # Add table cells
        cell = row.cells.add()
        cell.paragraphs.add(
            ap.HtmlFragment(f"Column <strong>({row_count}, 1)</strong>")
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.HtmlFragment(f"Column <span style='color:red'>({row_count}, 2)</span>")
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.HtmlFragment(
                f"Column <span style='text-decoration: underline'>({row_count}, 3)</span>"
            )
        )
        row_count += 1

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(outfile)
```

### Verwendung von LaTeX-Fragmenten in Zellen

Dieses Beispiel zeigt, wie man LaTeX-formatierte Inhalte in Tabellenzellen einfügt, um mathematische oder formatierte Ausdrücke darzustellen.

1. Tabellen- und Zellenränder festlegen.
1. LaTeX-Inhalt hinzufügen.
1. Zeilen hinzufügen. Eine Schleife fügt mehrere Zeilen mit LaTeX‑formatiertem Inhalt in jeder Zelle hinzu.
1. Fügen Sie die Tabelle mit 'page.paragraphs.add(table)' in die PDF-Seite ein.
1. Speichern Sie das PDF-Dokument.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_latex_fragments(outfile: str) -> None:
    # Instantiate Document object
    document = ap.Document()
    page = document.pages.add()
    # Instantiate a table object
    table = ap.Table()

    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.ALL, 0.5, ap.Color.light_gray
    )
    # Create a loop to add 10 rows
    row_count = 1
    while row_count < 10:
        # Add row to table
        row = table.rows.add()
        # Add table cells
        cell = row.cells.add()
        cell.paragraphs.add(ap.LatexFragment(f"Column $\\mathbf{{({row_count}, 1)}}$"))

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.LatexFragment(f"Column $\\textcolor{{red}}{{({row_count}, 2)}}$")
        )

        cell = row.cells.add()
        cell.paragraphs.add(
            ap.LatexFragment(f"Column $\\underline{{({row_count}, 3)}}$")
        )
        row_count += 1

    # Add table object to first page of input document
    page.paragraphs.add(table)
    # Save updated document containing table object
    document.save(outfile)
```

## Erweiterte Tabellenfunktionen

### Automatische Seitenumbrüche in einer PDF-Tabelle einfügen

Erstellen Sie eine große Tabelle in einem PDF mit Python und Aspose.PDF, wobei nach einer bestimmten Anzahl von Zeilen automatische Seitenumbrüche erfolgen. Es wird eine mehrzeilige Tabelle erstellt, es werden Rahmen angewendet und ausgewählte Zeilen werden erzwungen, auf einer neuen Seite zu beginnen, um eine bessere Layoutkontrolle zu ermöglichen.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def insert_page_break(outfile: str) -> None:
    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Create table instance
    table = ap.Table()

    # Set border style for table
    table.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    # Set default border style for table with border color as Red
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)

    # Specify table columns width
    table.column_widths = "100 100"

    # Create a loop to add 200 rows for table
    for counter in range(201):
        row = ap.Row()
        table.rows.add(row)

        cell1 = ap.Cell()
        cell1.paragraphs.add(ap.text.TextFragment(f"Cell {counter}, 0"))
        row.cells.add(cell1)

        cell2 = ap.Cell()
        cell2.paragraphs.add(ap.text.TextFragment(f"Cell {counter}, 1"))
        row.cells.add(cell2)

        # When 10 rows are added, render new row in new page
        if counter % 10 == 0 and counter != 0:
            row.is_in_new_page = True

    # Add table to paragraphs collection of PDF file
    page.paragraphs.add(table)

    # Save PDF document
    document.save(outfile)
```

### Wiederholende Kopfzeilen auf mehreren Seiten

Dieses Beispiel zeigt, wie man eine Tabelle erstellt, die sich über mehrere Seiten erstreckt, wobei die Kopfzeilen auf jeder Seite sichtbar bleiben.

1. Initialisieren Sie die Tabelle.
1. Kopfzeilen wiederholen, einschließlich Schriftart, Größe und Farbe.
1. Spaltenbreiten festlegen und Rahmen auf die Tabelle anwenden.
1. Header‑Zeilen hinzufügen.
1. Fügen Sie viele Datenzeilen hinzu, um die Tabelle über mehrere Seiten hinweg zu erzwingen.
1. Fügen Sie die Tabelle mit 'page.paragraphs.add(table)' in die PDF-Seite ein.
1. Speichern Sie das PDF-Dokument.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_repeating_rows(outfile: str) -> None:
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Instantiate a table object
    table = ap.Table()

    # Set the table to break across pages
    table.broken = ap.TableBroken.VERTICAL

    # Set number of repeating header rows
    table.repeating_rows_count = 2

    text_state = ap.text.TextState()
    text_state.font_size = 12
    text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_state.foreground_color = ap.Color.red
    table.repeating_rows_style = text_state

    # Set column widths
    table.column_widths = "100 100 100"

    # Set borders
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.black)

    # Add header rows that will repeat on each page
    header_row1 = table.rows.add()
    header_row1.cells.add("Header 1-1")
    header_row1.cells.add("Header 1-2")
    header_row1.cells.add("Header 1-3")

    # Set background color for header rows
    for cell in header_row1.cells:
        cell.background_color = ap.Color.light_gray

    header_row2 = table.rows.add()
    header_row2.cells.add("Header 2-1")
    header_row2.cells.add("Header 2-2")
    header_row2.cells.add("Header 2-3")

    for cell in header_row2.cells:
        cell.background_color = ap.Color.light_blue

    # Add many data rows to force table across multiple pages
    for i in range(1, 101):
        row = table.rows.add()
        row.cells.add(f"Data {i}-1")
        row.cells.add(f"Data {i}-2")
        row.cells.add(f"Data {i}-3")

    # Add table to page
    page.paragraphs.add(table)

    # Save document
    document.save(outfile)
```

### Wiederholende Spalten

Die Funktion 'add_repeating_columns' erstellt ein PDF-Dokument mit einer Tabelle, die wiederholende Spalten hat. Sie richtet eine umrandete Tabelle ein, fügt Kopfzeilen hinzu, füllt Datenzeilen aus und speichert die erzeugte PDF-Datei am angegebenen Speicherort. Das Setzen dieser Eigenschaft bewirkt, dass die Tabelle spaltenweise auf die nächste Seite umbricht und die angegebene Spaltenanzahl zu Beginn der nächsten Seite wiederholt wird.

1. Initialisiert ein neues PDF‑Dokument.
1. Fügt eine Seite mit benutzerdefinierten Abmessungen hinzu.
1. Tabellenrandstil festlegen.
1. Tabelle initialisieren.
1. Tabelle zur PDF-Seite hinzufügen.
1. Kopfzeile hinzufügen.
1. Datenzeilen hinzufügen.
1. PDF Document speichern.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def add_repeating_columns(outfile: str) -> None:
    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()
    page.set_page_size(ap.PageSize.a5.height, ap.PageSize.a5.width)

    # Define border
    border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.light_gray)

    # Create table
    table = ap.Table()
    table.broken = ap.TableBroken.VERTICAL_IN_SAME_PAGE
    table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    table.repeating_columns_count = 5
    table.border = border
    table.default_cell_border = border

    # Add table to page
    page.paragraphs.add(table)

    # Add header row
    row = table.rows.add()
    for i in range(1, 6):
        cell = row.cells.add(f"header {i}")
        cell.background_color = ap.Color.light_gray

    for i in range(6, 18):
        row.cells.add(f"header {i}")

    # Add data rows
    for row_counter in range(1, 6):
        row = table.rows.add()
        for i in range(1, 6):
            cell = row.cells.add(f"cell {row_counter},{i}")
            cell.background_color = ap.Color.light_gray
        for i in range(6, 18):
            row.cells.add(f"cell {row_counter},{i}")

    # Save PDF document
    document.save(outfile)
```

### Erstelle eine PDF-Tabelle mit gedrehten Textzellen

Erstellen Sie eine Tabelle in einem PDF mit Python und Aspose.PDF, wobei der Text in jeder Zelle um unterschiedliche Winkel gedreht ist. Das ist nützlich für vertikale Überschriften, kreative Layouts, kompakte Tabellen und benutzerdefinierte Berichtformatierung.

```python
import aspose.pdf as ap
from aspose.pdf import Color, HorizontalAlignment
from os import path
import sys

def rotated_text_table(outfile: str) -> None:
    # Create PDF document
    document = ap.Document()

    # Add page
    page = document.pages.add()

    # Initializes a new instance of the Table
    table = ap.Table()
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, Color.black)
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, Color.black)

    # Add 1st row to table
    row1 = table.rows.add()
    row1.min_row_height = 200

    for cell_count in range(4):
        # Add table cells
        cell = row1.cells.add()

        tf = ap.text.TextFragment(f"Cell 1 {cell_count - 1}")
        tf.text_state.rotation = 90 * cell_count
        tf.horizontal_alignment = HorizontalAlignment.CENTER

        cell.paragraphs.add(tf)

    # Add table object to first page of input document
    page.paragraphs.add(table)

    # Save result
    document.save(outfile)
```

## Verwandte Tabellenthemen

- [Tabellen in PDF mit Python bearbeiten](/pdf/de/python-net/working-with-tables/)
- [Tabellen aus PDF-Dokumenten extrahieren](/pdf/de/python-net/extracting-table/)
- [PDF-Tabellen mit Datenquellen integrieren](/pdf/de/python-net/integrate-table/)
- [Tabellen in bestehenden PDFs manipulieren](/pdf/de/python-net/manipulating-tables/)
