---
title: Tabellen in bestehenden PDF-Dokumenten bearbeiten
linktitle: Tabellen bearbeiten
type: docs
weight: 40
url: /de/python-net/manipulating-tables/
description: Erfahren Sie, wie Sie Tabellen in bestehenden PDF-Dokumenten mit Python inspizieren und ändern.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Bestehende PDF-Tabellen mit Python inspizieren und ändern
Abstract: Dieser Artikel erklärt, wie man Tabellen, die bereits in PDF-Dokumenten vorhanden sind, mit Aspose.PDF for Python via .NET bearbeitet. Erfahren Sie, wie man Tabellen mit TableAbsorber findet, spezifische Zeilen und Zellen zugreift, den Tabellentextinhalt aktualisiert und das geänderte PDF in Python speichert.
---

## Tabellen in bestehenden PDF bearbeiten

Aspose.PDF for Python via .NET ermöglicht es Ihnen, Tabellen zu aktualisieren, die bereits in einem PDF-Dokument vorhanden sind. Sie können die [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) Klasse, um Tabellen auf einer Seite zu finden, Zeilen und Zellen zuzugreifen, den Textinhalt zu ändern und die aktualisierte Datei zu speichern.

Verwenden Sie diese Seite, wenn Sie bestehenden Tabelleninhalt in PDFs aktualisieren müssen, ohne das gesamte Dokumentlayout neu zu erstellen.

## Text in PDF-Tabellenzellen finden und ersetzen

Dieses Beispiel findet die erste Tabelle auf Seite 1, greift auf die erste Zelle zu, ersetzt deren Text und speichert das Ausgabe-PDF.

1. Öffnen Sie die Eingabe-PDF.
1. Erstellen Sie einen TableAbsorber und besuchen Sie Seite 1.
1. Stellen Sie sicher, dass mindestens eine Tabelle erkannt wird.
1. Greifen Sie auf die erste Zelle in der ersten Zeile der ersten Tabelle zu.
1. Stellen Sie sicher, dass die Zelle Textfragmente enthält, und aktualisieren Sie dann das erste Fragment.
1. Speichere das bearbeitete PDF.

```python
import aspose.pdf as ap

def replace_cell_text(infile: str, outfile: str) -> None:
    """Replace text in the first cell of the first detected table."""
    # Open PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    if len(absorber.table_list) == 0:
        raise ValueError("No tables were found on page 1.")

    first_cell = absorber.table_list[0].row_list[0].cell_list[0]
    if len(first_cell.text_fragments) == 0:
        raise ValueError("The target cell has no text fragments.")

    # Change text of the first text fragment in the cell
    first_cell.text_fragments[0].text = "New Value"

    # Save PDF document
    document.save(outfile)
```

## Ersetzen Sie eine vorhandene Tabelle durch eine neue Tabelle

Sie können auch eine erkannte Tabelle durch eine neu erstellte ersetzen. Dieser Ansatz ist nützlich, wenn sowohl die Struktur als auch der Inhalt geändert werden müssen.

Der nachstehende Code öffnet ein PDF, findet die erste Tabelle auf Seite 1, erstellt eine Ersatz‑Tabelle, tauscht die alte Tabelle gegen die neue aus und speichert das Ergebnis.

```python
import aspose.pdf as ap

def replace_table(infile: str, outfile: str) -> None:
    """Replace an entire table with a new one."""
    # Open PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    if len(absorber.table_list) == 0:
        raise ValueError("No tables were found on page 1.")

    # Get first table on the page
    old_table = absorber.table_list[0]

    # Create new table
    new_table = ap.Table()
    new_table.column_widths = "100 100 100"
    new_table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 1.0)

    row = new_table.rows.add()
    row.cells.add("Col 1")
    row.cells.add("Col 2")
    row.cells.add("Col 3")
    row = new_table.rows.add()
    row.cells.add("Col 12")
    row.cells.add("Col 22")
    row.cells.add("Col 32")

    # Replace the old table with the new one
    absorber.replace(document.pages[1], old_table, new_table)

    # Save PDF document
    document.save(outfile)
```

## Verwandte Tabellenthemen

- [Tabellen in PDF mit Python bearbeiten](/pdf/de/python-net/working-with-tables/)
- [Tabellen zu PDF mit Python hinzufügen](/pdf/de/python-net/adding-tables/)
- [Tabellen aus PDF-Dokumenten extrahieren](/pdf/de/python-net/extracting-table/)
- [Tabellen aus vorhandenen PDFs entfernen](/pdf/de/python-net/removing-tables/)
