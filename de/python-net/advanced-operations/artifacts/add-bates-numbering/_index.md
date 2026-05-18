---
title: Bates-Nummerierung zu PDF in Python hinzufügen
linktitle: Bates-Nummerierung hinzufügen
type: docs
weight: 10
url: /de/python-net/add-bates-numbering/
description: Erfahren Sie, wie Sie Bates-Nummerierung in PDF-Dokumenten mit Python und Aspose.PDF for Python via .NET hinzufügen und entfernen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Bates-Nummerierung über Python hinzufügen
Abstract: Die Bates-Nummerierung ist ein kritisches Merkmal in juristischen, medizinischen und geschäftlichen Dokumenten‑Workflows und stellt sicher, dass jede Seite in einem Satz eine eindeutige, fortlaufende Kennung für zuverlässige Verweise erhält. Dieser Artikel zeigt, wie Aspose.PDF for Python via .NET die Automatisierung der Bates-Nummerierung durch seine flexible API vereinfacht. Mit der Klasse BatesNArtifact können Entwickler das Nummerierungsverhalten – einschließlich Ziffernanzahl, Präfixe, Suffixe, Ausrichtung und Ränder – konfigurieren und programmgesteuert auf gesamte Dokumente anwenden. Es werden mehrere Ansätze vorgestellt, von der direkten Anwendung des Artifacts bis zur delegatenbasierten Konfiguration, die sowohl statische als auch dynamische Kontrolle bietet. Zusätzlich unterstützt die API das vollständige Entfernen von Bates‑Nummern mit einem einzigen Methodenaufruf, wodurch ein vollständiges Lifecycle‑Management von Seitennummerierungs‑Artifacts ermöglicht wird. Klare, Schritt‑für‑Schritt‑Codebeispiele zeigen, wie man Bates‑Nummerierung hinzufügt, anpasst und löscht, und machen diese Anleitung zu einer praktischen Ressource für Entwickler, die die Dokumentenverarbeitungs‑Workflows optimieren möchten.
---

Bates-Nummerierung wird in rechtlichen, medizinischen und geschäftlichen Arbeitsabläufen häufig eingesetzt, um eindeutige, fortlaufende Kennungen den Seiten innerhalb eines Dokumentensatzes zuzuweisen. Aspose.PDF for Python via .NET bietet eine einfache und flexible API zur Automatisierung dieses Vorgangs, mit der Sie standardisierte Bates-Nummern programmgesteuert auf jede PDF anwenden können.

Verwenden Sie die [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) Klasse, Entwickler können das Nummerierungsverhalten vollständig anpassen—einschließlich der Startnummer, der Stellenanzahl, Präfixe und Suffixe, Ausrichtung und Ränder. Nach der Konfiguration kann das Artefakt auf das [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) durch die `add_bates_numbering` Methode auf dem [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) oder hinzugefügt als Teil einer Liste von [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/) Objekte. Aspose.PDF unterstützt ebenfalls einen delegatbasierten Konfigurationsstil, der eine dynamische Steuerung der Artefakteinstellungen zur Laufzeit ermöglicht.

Zusätzlich zum Erstellen von Bates-Nummern bietet die API eine einfache Möglichkeit, sie zu entfernen, indem man `delete_bates_numbering`, die komplette Flexibilität in Dokumentverarbeitungs-Workflows bietet.

Dieser Artikel zeigt mehrere Methoden zum Hinzufügen und Entfernen von Bates-Nummern in einer PDF mit Aspose.PDF for Python via .NET, mit klaren Beispielen für die Artefaktkonfiguration, -anwendung und -entfernung.

## Hinzufügen eines Bates-Nummerierungsartefakts

Dieses Beispiel zeigt, wie man programmgesteuert Bates-Nummerierung zu einem PDF-Dokument hinzufügt, indem man Aspose.PDF for Python via .NET verwendet. Durch Konfigurieren eines [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) mit den gewünschten Einstellungen und der Anwendung auf die Seiten des Dokuments können Sie den Vorgang automatisieren, standardisierte Kennungen zu jeder Seite hinzuzufügen.

Um ein Bates-Nummerierungs-Artefakt zu einem [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), rufen Sie die `AddBatesNumbering(BatesNArtifact)` Erweiterungsmethode für die [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/), übergeben Sie ein [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) Instanz als Parameter:

```python
import sys
from os import path
import aspose.pdf as ap

def _create_bates_artifact():
    """Create a Bates numbering artifact with default settings."""
    artifact = ap.BatesNArtifact()
    artifact.start_page = 1
    artifact.end_page = 0
    artifact.subset = ap.Subset.ALL
    artifact.number_of_digits = 6
    artifact.start_number = 1
    artifact.prefix = ""
    artifact.suffix = ""
    artifact.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
    artifact.right_margin = 72
    artifact.left_margin = 72
    artifact.top_margin = 36
    artifact.bottom_margin = 36
    return artifact
```

```python
import sys
from os import path
import aspose.pdf as ap

def add_bates_n_artifact(infile, outfile):
    """Add Bates numbering artifact to a PDF document."""
    with ap.Document(infile) as document:
        for _ in range(2):
            document.pages.add()

        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_bates_numbering(document.pages, bates_artifact)
        document.save(outfile)
```

## Bates-Nummerierung mit Paginierungsartefakten hinzufügen

Fügen Sie einer PDF eine Bates-Nummerierung hinzu, indem Sie die Paginierungsartefakte-Sammlung in Aspose.PDF for Python verwenden:

1. Laden Sie das PDF‑Dokument.
1. Fügen Sie bei Bedarf zusätzliche Seiten ein, bevor Sie die Nummerierung anwenden.
1. Erstellen Sie ein Bates‑Artefakt.
1. Konfigurieren Sie die Artefakt‑Eigenschaften.
1. Fügen Sie das Artefakt zur Paginierungs‑Sammlung hinzu.
1. Paginierung auf Seiten anwenden.
1. Speichern Sie das aktualisierte Dokument.

```python
import sys
from os import path
import aspose.pdf as ap

def add_bates_n_artifact_pagination(infile, outfile):
    """Add Bates numbering using pagination artifacts collection."""
    with ap.Document(infile) as document:
        for _ in range(2):
            document.pages.add()

        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_pagination(document.pages, [bates_artifact])
        document.save(outfile)
```

## Bates-Nummerierung löschen

Um die Bates-Nummerierung von einem [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), verwenden Sie das `delete_bates_numbering()` Methode auf dem [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/):

```python
import sys
from os import path
import aspose.pdf as ap

def delete_bates_numbering(infile, outfile):
    """Delete Bates numbering from a PDF document."""
    with ap.Document(infile) as document:
        ap.PageCollectionExtensions.delete_bates_numbering(document.pages)
        document.save(outfile)
```

## Verwandte Artefakt-Themen

- [Arbeiten mit PDF-Artefakten in Python](/pdf/de/python-net/artifacts/)
- [Wasserzeichen zu PDF in Python hinzufügen](/pdf/de/python-net/add-watermarks/)
- [PDF-Hintergründe in Python hinzufügen](/pdf/de/python-net/add-backgrounds/)
- [Zähle Artefakt-Typen in PDF-Dateien](/pdf/de/python-net/counting-artifacts/)