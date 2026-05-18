---
title: Wasserzeichen zu PDF in Python hinzufügen
linktitle: Wasserzeichen hinzufügen
type: docs
weight: 30
url: /de/python-net/add-watermarks/
description: Erfahren Sie, wie Sie Wasserzeichen-Elemente zu PDF-Dateien in Python mithilfe von Aspose.PDF for Python via .NET hinzufügen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man mit Python ein Wasserzeichen zu PDF hinzufügt
Abstract: Der Artikel behandelt die Verwendung von Aspose.PDF for Python via .NET, um Wasserzeichen zu PDF-Dokumenten hinzuzufügen, indem Artefakte verwaltet werden. Er stellt die wichtigsten Klassen zur Handhabung von Artefakten vor – `Artifact` und `ArtifactCollection` – und beschreibt, wie man über die `Artifacts`‑Eigenschaft der Klasse `Page` darauf zugreift. Der Artikel erklärt die Eigenschaften der Klasse `Artifact`, einschließlich der Attribute `contents`, `form`, `image`, `text`, `rectangle`, `rotation` und `opacity`, die eine umfassende Manipulation von Artefakten in PDF-Dateien ermöglichen. Zusätzlich wird ein praktisches Beispiel bereitgestellt, das zeigt, wie man programmgesteuert ein Wasserzeichen zur ersten Seite einer PDF mit Python hinzufügt. Das Code‑Snippet veranschaulicht die Erstellung und Konfiguration eines `WatermarkArtifact`, wobei dessen Text, Ausrichtung, Drehung und Transparenz festgelegt werden, bevor es zu einem PDF‑Dokument hinzugefügt und die Änderungen gespeichert werden.
---

Fügen Sie einem PDF ein Wasserzeichen-Artefakt hinzu [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) unter Verwendung von Aspose.PDF für Python via .NET. Ein Wasserzeichen ist ein visuelles Overlay, das auf Seiten für Markenbildung, Sicherheit oder Informationszwecke angewendet wird. Das Beispiel zeigt, wie man konfiguriert [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) Erscheinungsbild, Positionierung mit [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) und [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/), Drehung, und Transparenz bevor das Wasserzeichen auf ein [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

## Wasserzeichen aus PDF extrahieren

1. Laden Sie das PDF‑Dokument.
1. Zugriff auf Seitenartefakte.
1. Wasserzeichen-Artefakte filtern.
1. Wasserzeichen-Elemente sammeln.
1. Wasserzeichen-Eigenschaften extrahieren.
1. Ausgabe der Wasserzeicheninformationen.

```python
from os import path
import sys
import aspose.pdf as ap

def extract_watermark_from_pdf(infile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            print(f"{watermark.text} {watermark.rectangle}")
```

## Ein Wasserzeichen zu PDF hinzufügen

Fügen Sie ein Textwasserzeichen zu einem PDF-Dokument mit Aspose.PDF for Python hinzu:

1. Laden Sie das PDF‑Dokument.
1. Erstelle einen Textzustand.
1. Erstelle ein Wasserzeichen-Objekt.
1. Setze den Wasserzeichentext und Stil.
1. Konfiguriere Positionierung und Drehung.
1. Setze Deckkraft und Hintergrundverhalten.
1. Füge das Wasserzeichen einer Seite hinzu.
1. Speichern Sie das aktualisierte Dokument.

```python
from os import path
import sys
import aspose.pdf as ap

def add_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        text_state = ap.text.TextState()
        text_state.font_size = 72
        text_state.foreground_color = ap.Color.blue_violet
        text_state.font_style = ap.text.FontStyles.BOLD
        text_state.font = ap.text.FontRepository.find_font("Arial")

        watermark = ap.WatermarkArtifact()
        watermark.set_text_and_state("WATERMARK", text_state)
        watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
        watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
        watermark.rotation = 60
        watermark.opacity = 0.2
        watermark.is_background = True

        document.pages[1].artifacts.append(watermark)
        document.save(outfile)

```

## Wasserzeichen-Artefakte von PDF-Seite entfernen 

Entfernen Sie Wasserzeichen-Artefakte von einer bestimmten Seite in einem PDF-Dokument mithilfe der Aspose.PDF for Python API. Der Ansatz richtet sich auf Wasserzeichen-Elemente, die als Seiten-Artefakte gespeichert sind (insbesondere solche, die als pagination Wasserzeichen-Subtypen klassifiziert sind), iteriert über sie und löscht sie, bevor das aktualisierte Dokument gespeichert wird.

1. Laden Sie das PDF‑Dokument.
1. Zugriff auf Seitenartefakte.
1. Wasserzeichen-Artefakte filtern.
1. Wasserzeichen-Artefakte löschen.
1. Speichern Sie das aktualisierte Dokument.

```python
from os import path
import sys
import aspose.pdf as ap

def delete_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            document.pages[1].artifacts.delete(watermark)

        document.save(outfile)
```

## Verwandte Artefakt-Themen

- [Arbeiten mit PDF-Artefakten in Python](/pdf/de/python-net/artifacts/)
- [PDF-Hintergründe in Python hinzufügen](/pdf/de/python-net/add-backgrounds/)
- [Bates-Nummerierung zu PDF in Python hinzufügen](/pdf/de/python-net/add-bates-numbering/)
- [Zähle Artefakt-Typen in PDF-Dateien](/pdf/de/python-net/counting-artifacts/)