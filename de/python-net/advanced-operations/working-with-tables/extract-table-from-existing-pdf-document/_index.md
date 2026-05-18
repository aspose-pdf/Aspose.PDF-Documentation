---
title: Tabellen aus PDF in Python extrahieren
linktitle: Tabelle extrahieren
type: docs
weight: 20
url: /de/python-net/extracting-table/
description: Erfahren Sie, wie Sie Tabellendaten aus bestehenden PDF-Dokumenten in Python extrahieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tabellendaten aus PDF-Dateien mit Python extrahieren
Abstract: Dieser Artikel erklärt, wie man Tabellen aus PDF-Dokumenten mit Aspose.PDF for Python via .NET extrahiert. Er zeigt, wie man `TableAbsorber` verwendet, um Tabellen pro Seite zu erkennen, Zeilen und Zellen zu iterieren und den Zelltext für Analysen und nachgelagerte Datenverarbeitung abzurufen.
---

## Tabelle aus PDF extrahieren

Das Extrahieren von Tabellen aus PDFs ist nützlich für Reporting, Datenmigration und Analyse-Workflows. Mit Aspose.PDF for Python via .NET können Sie Tabellendaten aus bestehenden PDF-Dokumenten effizient erkennen und lesen.

Dieser Codeausschnitt öffnet eine bestehende PDF-Datei, durchsucht jede Seite nach Tabellen und extrahiert den Textinhalt der Zellen. Es verwendet `TableAbsorber` um Tabellen zu erkennen und dann durch Zeilen und Zellen zu iterieren, um den extrahierten Text auszugeben.

1. Lädt das PDF in ein ap.Document-Objekt.
1. Durchlaufen Sie die Seiten.
1. Erstellt ein TableAbsorber-Objekt.
1. Iterieren Sie durch Tabellen.
1. Durchlaufe Zeilen und Zellen.
1. Extrahiere und drucke Text aus Zellen.

Dieses Beispiel liest ein PDF, findet alle Tabellen und gibt deren Zellinhalte Zeile für Zeile aus.

```python
import aspose.pdf as ap
from os import path
import sys

def extract(infile: str) -> None:
    """Extract and print all tables from a PDF file."""
    document = ap.Document(infile)
    for page in document.pages:
        absorber = ap.text.TableAbsorber()
        absorber.visit(page)
        for table in absorber.table_list:
            print("Table ----")
            for row in table.row_list:
                print("Row:")
                row_txt = ""
                for cell in row.cell_list:
                    cell_txt = ""
                    text_fragment_collection = cell.text_fragments
                    for fragment in text_fragment_collection:
                        for seg in fragment.segments:
                            cell_txt += seg.text
                    row_txt += " | "
                    row_txt += cell_txt
                print(row_txt)
```

## Verwandte Tabellenthemen

- [Tabellen in PDF mit Python bearbeiten](/pdf/de/python-net/working-with-tables/)
- [Tabellen zu PDF mit Python hinzufügen](/pdf/de/python-net/adding-tables/)
- [PDF-Tabellen mit Datenquellen integrieren](/pdf/de/python-net/integrate-table/)
- [Tabellen aus vorhandenen PDFs entfernen](/pdf/de/python-net/removing-tables/)