---
title: Tabellen aus vorhandenen PDF-Dokumenten entfernen
linktitle: Tabellen entfernen
description: Erfahren Sie, wie Sie eine oder mehrere Tabellen aus vorhandenen PDF-Dokumenten in Python entfernen.
lastmod: "2026-05-18"
type: docs
weight: 50
url: /de/python-net/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Löschen Sie eine oder mehrere Tabellen aus PDF-Dateien mit Python
Abstract: Dieser Artikel erklärt, wie man Tabellen aus vorhandenen PDF-Dokumenten mithilfe von Aspose.PDF for Python via .NET entfernt. Er führt `TableAbsorber` zum Auffinden von Tabellen ein und demonstriert, wie man eine einzelne Tabelle löscht oder alle erkannten Tabellen von einer Seite entfernt.
---

## Tabelle aus PDF-Dokument entfernen

Aspose.PDF for Python ermöglicht das Entfernen einer Tabelle aus einer PDF. Es öffnet eine vorhandene PDF, erkennt die erste Tabelle auf der ersten Seite mit `TableAbsorber`, löscht diese Tabelle mit `remove()`, und speichert das aktualisierte PDF in einer neuen Datei.

Verwenden Sie diese Seite, wenn Sie tabellenlastige PDFs bereinigen, veraltete tabellarische Inhalte entfernen oder Dokumente vor der Weiterverteilung vereinfachen müssen.

```python
import aspose.pdf as ap
from os import path
import sys

def remove_one_table(infile: str, outfile: str) -> None:
    # Load existing PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    # Get first table on the page
    table = absorber.table_list[0]
    # Remove the table
    absorber.remove(table)
    # Save PDF
    document.save(outfile)
```

## Alle Tabellen aus dem PDF-Dokument entfernen

Mit unserer Bibliothek können Sie alle Tabellen von einer bestimmten Seite in einem PDF entfernen. Der Code öffnet ein vorhandenes PDF, erkennt alle Tabellen auf der zweiten Seite mit TableAbsorber, iteriert über die erkannten Tabellen, entfernt jede einzelne und speichert das modifizierte PDF anschließend in einer neuen Datei. Das ist nützlich, wenn Sie Tabellen einer Seite massenhaft entfernen müssen, während der übrige PDF‑Inhalt unverändert bleibt.

```python
import aspose.pdf as ap
from os import path
import sys

def remove_all_tables(infile: str, outfile: str) -> None:
    # Load existing PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    #  Loop through the copy of collection and removing tables
    tables = list(absorber.table_list)
    for table in tables:
        absorber.remove(table)

    # Save document
    document.save(outfile)
```

## Verwandte Tabellenthemen

- [Tabellen in PDF mit Python bearbeiten](/pdf/de/python-net/working-with-tables/)
- [Tabellen zu PDF mit Python hinzufügen](/pdf/de/python-net/adding-tables/)
- [Tabellen aus PDF-Dokumenten extrahieren](/pdf/de/python-net/extracting-table/)
- [Tabellen in bestehenden PDFs manipulieren](/pdf/de/python-net/manipulating-tables/)