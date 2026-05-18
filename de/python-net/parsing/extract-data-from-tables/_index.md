---
title: Daten aus Tabelle in PDF mit Python extrahieren
linktitle: Daten aus Tabelle extrahieren
type: docs
weight: 40
url: /de/python-net/extract-data-from-table-in-pdf/
description: Erfahren Sie, wie Sie Tabellendaten aus PDF-Dateien mit Aspose.PDF for Python extrahieren und die Ergebnisse für die weitere Verarbeitung exportieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man Daten aus Tabelle in PDF via Python extrahiert
Abstract: Dieser Artikel erklärt, wie man Tabellendaten aus PDF-Dokumenten mit Aspose.PDF for Python extrahiert und verarbeitet. Er zeigt, wie man jede Seite mit TableAbsorber scannt, Zeilen und Zellen aus erkannten Tabellen liest, die Extraktion auf einen bestimmten annotierten Bereich beschränkt und den PDF-Inhalt in das CSV-Format exportiert, um ihn in Tabellenkalkulationswerkzeugen und nachgelagerten Prozessen zu verwenden.
---

## Tabellen programmgesteuert aus PDF extrahieren

Verwenden [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) um Tabellen auf jeder Seite eines [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Nach dem Aufrufen einer Seite iterieren Sie durch `table_list`, dann gehen Sie jede Zeile und Zelle durch, um den Tabelleninhalt in einem lesbaren Textformat wiederherzustellen.

1. Öffnen Sie das PDF als ein `Document`.
1. Durchlaufen Sie die Seiten in `document.pages`.
1. Erstelle ein `TableAbsorber` für jede Seite und Aufruf `visit(page)`.
1. Durchlaufen Sie die erkannten Tabellen, Zeilen und Zellen.
1. Lese Textfragmente aus jeder Zelle und setze die extrahierte Zeilenausgabe zusammen.

```python
import aspose.pdf as apdf
from os import path

path_infile = path.join(self.dataDir, infile)

# Open PDF document
document = apdf.Document(path_infile)

# Iterate through each page in the document
for page in document.pages:
    absorber = apdf.text.TableAbsorber()
    absorber.visit(page)

    for table in absorber.table_list:
        print("Table")
        for row in table.row_list:
            row_text = []
            for cell in row.cell_list:
                cell_text = []
                for fragment in cell.text_fragments:
                    cell_text.append("".join(seg.text for seg in fragment.segments))
                row_text.append("|".join(cell_text))
            print("|".join(row_text))
```

## Tabelle im spezifischen Bereich einer PDF-Seite extrahieren

Wenn Sie nur Tabellen extrahieren müssen, die sich in einem markierten Bereich befinden, kombinieren Sie [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) mit einem [SquareAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/). In diesem Beispiel wird das Annotationsrechteck als Grenze verwendet, und es werden nur Tabellen verarbeitet, die vollständig innerhalb dieses Bereichs liegen.

1. Öffnen Sie das PDF als ein `Document`.
1. Wählen Sie die Zielseite aus.
1. Suchen Sie die quadratische Anmerkung, die den Interessensbereich markiert.
1. Erstelle ein `TableAbsorber` und besuchen Sie die Seite.
1. Vergleichen Sie jedes erkannte Tabellenrechteck mit dem Anmerkungsrechteck.
1. Verarbeiten Sie nur die Tabellen, die vollständig innerhalb des markierten Bereichs liegen.

```python
import aspose.pdf as apdf
from os import path

# The path to the documents directory
path_infile = path.join(self.dataDir, infile)

# Open PDF document
document = apdf.Document(path_infile)

# Get the first page (index starts from 1 in Aspose.PDF)
page = document.pages[1]

# Find the first square annotation
square_annotation = next(
    (
        ann
        for ann in page.annotations
        if ann.annotation_type == apdf.annotations.AnnotationType.SQUARE
    ),
    None,
)

if square_annotation is None:
    print("No square annotation found.")
    return

# Initialize the TableAbsorber
absorber = apdf.text.TableAbsorber()
absorber.visit(page)

# Iterate through tables on the page
for table in absorber.table_list:
    table_rect = table.rectangle
    annotation_rect = square_annotation.rect

    # Check if the table is inside the annotation region
    is_in_region = (
        annotation_rect.llx < table_rect.llx
        and annotation_rect.lly < table_rect.lly
        and annotation_rect.urx > table_rect.urx
        and annotation_rect.ury > table_rect.ury
    )

    if is_in_region:
        for row in table.row_list:
            row_text = []
            for cell in row.cell_list:
                cell_text = []
                for fragment in cell.text_fragments:
                    cell_text.append("".join(seg.text for seg in fragment.segments))
                row_text.append("|".join(cell_text))
            print("|".join(row_text))
```

## Tabellendaten aus PDF in CSV exportieren

Wenn Sie die extrahierten Daten in einem tabellenkalkulationsfreundlichen Format benötigen, speichern Sie das PDF mit [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) und setzen Sie das Ausgabeformat auf CSV. Die resultierende Datei kann in Excel, Google Sheets geöffnet oder in Analyse‑Workflows importiert werden.

1. Öffnen Sie das Quell‑PDF als [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Erstelle ein `ExcelSaveOptions` Instanz.
1. Setzen `excel_save.format` zu `ExcelSaveOptions.ExcelFormat.CSV`.
1. Speichern Sie das Dokument im Ziel‑CSV‑Pfad.

```python
import aspose.pdf as apdf
from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

document = apdf.Document(path_infile)
excel_save = apdf.ExcelSaveOptions()
excel_save.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
document.save(path_outfile, excel_save)
```
