---
title: PDF-Kopf- und Fußzeilen mit Python verwalten
linktitle: PDF-Kopf- und Fußzeilen verwalten
type: docs
weight: 70
url: /de/python-net/artifacts-header-footer/
description: Erfahren Sie, wie Sie Kopf- und Fußzeilen in PDF-Dokumenten mit Python und Aspose.PDF verwalten.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man PDF-Kopf- und Fußzeilen mit Python hinzufügt, anpasst und entfernt
Abstract: Die Verwaltung von Kopf- und Fußzeilen ist eine gängige Anforderung bei der Arbeit mit PDF-Dokumenten in Geschäfts-, Verlags- und Automatisierungsabläufen. Dieser Artikel zeigt, wie man Aspose.PDF for Python verwendet, um professionell aussehende Kopf- und Fußzeilen mit benutzerdefiniertem Styling wie Schriftart, Größe, Farbe und Ausrichtung hinzuzufügen. Er zeigt außerdem, wie man vorhandene Seitennummerierungsartefakte wie Kopf- und Fußzeilen auf einer PDF-Seite erkennt und entfernt. Mit wiederverwendbaren Funktionen und klaren Beispielen können Entwickler diese Funktionen schnell in Dokumentenverarbeitungssysteme für Branding, Berichterstellung oder Dateibereinigung integrieren.
---

## Erstelle formatierte Textartefakte

Diese Hilfsfunktion erklärt, wie man ein wiederverwendbares Text‑Artefakt für PDF‑Seiten mit Aspose.PDF for Python erstellt. Sie ist dafür konzipiert, formatierte Kopf‑ oder Fußzeilen mit einheitlicher Formatierung zu erzeugen, einschließlich Schriftart‑Einstellungen, Farbe, Größe und Ausrichtung. Die Funktion abstrahiert die Artefakterstellung, sodass sie für verschiedene seitenbezogene Textdekorationen wiederverwendet werden kann.

1. Instanziieren Sie das Artefakt‑Objekt.
1. Legen Sie den Textinhalt des Artefakts fest.
1. Wenden Sie die Textformatierung an.
1. Ausrichtung festlegen.
1. Konfiguriertes Artefakt zurückgeben.

```python
from os import path
import aspose.pdf as ap
import sys

def _create_text_artifact(artifact_class, text):
    """Create a text artifact (header/footer) with common styling."""
    artifact = artifact_class()
    artifact.text = text
    artifact.text_state.font_size = 14
    artifact.text_state.font = ap.text.FontRepository.find_font("Arial")
    artifact.text_state.foreground_color = ap.Color.navy
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    return artifact

```

## Header zum PDF hinzufügen

1. Öffnen Sie das Eingabe-PDF.
1. Erstelle ein HeaderArtifact mit dem Text \"Sample Header\".
1. Füge es der ersten Seite hinzu.
1. Speichere das aktualisierte PDF.

```python
from os import path
import aspose.pdf as ap
import sys

def add_header_artifact(infile, outfile):
    """Add a header artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        header = _create_text_artifact(ap.HeaderArtifact, "Sample Header")
        document.pages[1].artifacts.append(header)
        document.save(outfile)
```

## Fußzeile zum PDF hinzufügen

1. Öffnen Sie das Eingabe-PDF.
1. Erstellen Sie ein FooterArtifact mit dem Text "Sample Footer".
1. Füge es der ersten Seite hinzu.
1. Speichern Sie die Ausgabedatei.

```python
from os import path
import aspose.pdf as ap
import sys

def add_footer_artifact(infile, outfile):
    """Add a footer artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        footer = _create_text_artifact(ap.FooterArtifact, "Sample Footer")
        document.pages[1].artifacts.append(footer)
        document.save(outfile)
```

## Kopf‑ oder Fußzeilen‑Artefakte löschen

1. Öffnen Sie das PDF.
1. Finde Artefakte, die als Seitenkopf- oder -fußzeilen markiert sind.
1. Entferne sie von der ersten Seite.
1. Speichere das bereinigte Dokument.

```python
from os import path
import aspose.pdf as ap
import sys

def delete_header_footer_artifact(infile, outfile):
    with ap.Document(infile) as document:
        header_footers = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and (
                artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER
                or artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER
            )
        ]

        for art in header_footers:
            document.pages[1].artifacts.delete(art)

        document.save(outfile)
```

## Verwandte Artefakt-Themen

- [Arbeiten mit PDF-Artefakten in Python](/pdf/de/python-net/artifacts/)
- [PDF-Hintergründe in Python hinzufügen](/pdf/de/python-net/add-backgrounds/)
- [Bates-Nummerierung zu PDF in Python hinzufügen](/pdf/de/python-net/add-bates-numbering/)
- [Zähle Artefakt-Typen in PDF-Dateien](/pdf/de/python-net/counting-artifacts/)