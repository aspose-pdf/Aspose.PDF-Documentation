---
title: PDF-Tabellen mit Datenquellen in Python integrieren
linktitle: Tabelle integrieren
type: docs
weight: 30
url: /de/python-net/integrate-table/
description: Erfahren Sie, wie Sie PDF-Tabellen mit Datenquellen wie Datenbanken und pandas DataFrames in Python integrieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PDF-Tabellen mit Datenbanken und DataFrames mithilfe von Python integrieren
Abstract: Dieser Artikel erklärt, wie man PDF-Tabellen mit externen Datenquellen unter Verwendung von Aspose.PDF for Python via .NET integriert. Erfahren Sie, wie Sie PDF-Tabellen aus pandas DataFrames und anderen strukturierten Quellen erstellen, sie in Dokumente einfügen und den Tabellenfluss beim Rendern über PDF-Seiten hinweg in Python steuern.
---

## PDF aus DataFrame erstellen

Der `create_pdf_from_dataframe` Funktion erstellt ein neues PDF und fügt eine Tabelle ein, die aus einem pandas DataFrame generiert wurde. Dieser Ansatz ist nützlich für Reporting‑Workflows, bei denen Ihre Daten bereits in Tabellenform vorliegen.

Die Funktion führt die folgenden Schritte aus:

1. Erstellen Sie ein leeres PDF‑Dokument mit `ap.Document()`.
1. Fügen Sie dem Dokument eine Seite hinzu.
1. Konvertieren Sie den DataFrame in eine Aspose.PDF-Tabelle, indem Sie aufrufen `create_table_from_dataframe(df, max_rows)`.
1. Fügen Sie die Tabelle zur Seite mit `page.paragraphs.add(table)`.
1. Speichern Sie das PDF im Ausgabepfad.

```python
from os import path
import sys

import pandas as pd
import aspose.pdf as ap
from config import set_license, initialize_data_dir

def create_pdf_from_dataframe(
    outfile: str, df: pd.DataFrame, max_rows: int = 20
) -> None:
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    table = create_table_from_dataframe(df, max_rows)

    # Add table object to first page of input document
    page.paragraphs.add(table)
    document.save(outfile)
```

## Tabelle aus DataFrame erstellen

Der `create_table_from_dataframe` Funktion konvertiert ein DataFrame in ein Aspose.PDF `Table` Objekt, das Sie zu jeder Seite hinzufügen können.

Es führt Folgendes aus:

1. Erstelle ein leeres `ap.Table()` Instanz.
1. Setze Tabellen- und Zellrahmen für eine konsistente Formatierung.
1. Füge eine Kopfzeile hinzu, indem du die Spaltennamen des DataFrames verwendest.
1. Datenzeilen hinzufügen aus `df.head(max_rows)`.
1. Gib das befüllte Tabellenobjekt zurück.

```python
from os import path
import sys

import pandas as pd
import aspose.pdf as ap
from config import set_license, initialize_data_dir

def create_table_from_dataframe(df: pd.DataFrame, max_rows: int = 20) -> ap.Table:
    """Create an Aspose.PDF table from a pandas DataFrame."""
    # Initializes a new instance of the Table
    table = ap.Table()
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOTTOM, 1, ap.Color.light_gray
    )

    # Add header row with column names
    header_row = table.rows.add()
    header_row.is_row_broken = False  # Prevent header row from being split across pages
    for column_name in df.columns:
        cell = header_row.cells.add(str(column_name))
        cell.background_color = ap.Color.light_gray

    # Add data rows
    for row_data in df.head(max_rows).itertuples(index=False):
        row = table.rows.add()
        for value in row_data:
            row.cells.add(str(value))

    return table
```

## Verwandte Tabellenthemen

- [Tabellen in PDF mit Python bearbeiten](/pdf/de/python-net/working-with-tables/)
- [Tabellen zu PDF mit Python hinzufügen](/pdf/de/python-net/adding-tables/)
- [Tabellen aus PDF-Dokumenten extrahieren](/pdf/de/python-net/extracting-table/)
- [Tabellen in bestehenden PDFs manipulieren](/pdf/de/python-net/manipulating-tables/)