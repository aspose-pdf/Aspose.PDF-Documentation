---
title: PDF-Hintergründe in Python hinzufügen
linktitle: Hintergründe hinzufügen
type: docs
weight: 20
url: /de/python-net/add-backgrounds/
description: Erfahren Sie, wie Sie ein Hintergrundbild zu PDF‑Seiten in Python hinzufügen, indem Sie die BackgroundArtifact‑Klasse in Aspose.PDF for Python via .NET verwenden.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man mit Python einen Hintergrund zu PDF hinzufügt
Abstract: Dieser Artikel behandelt die Verwendung von Hintergrundbildern in PDF-Dokumenten mit Aspose.PDF for Python via .NET. Er hebt die Möglichkeit hervor, Wasserzeichen oder dezente Designs zu Dokumenten hinzuzufügen, indem die Klasse `BackgroundArtifact` verwendet wird, die die Einbindung von Hintergrundbildern in einzelne Seitenobjekte ermöglicht. Der Artikel liefert ein praktisches Codebeispiel, das zeigt, wie diese Funktion implementiert wird. Der Vorgang besteht darin, ein neues PDF-Dokument zu erstellen, eine Seite hinzuzufügen, ein `BackgroundArtifact`-Objekt zu erstellen, ein Hintergrundbild festzulegen und das Hintergrund‑Artifact zur Artefakte‑Sammlung der Seite hinzuzufügen. Schließlich wird das modifizierte Dokument als PDF-Datei gespeichert. Diese Technik ermöglicht eine verbesserte visuelle Darstellung von PDF-Dokumenten.
---

## Hintergrundbild zu einem PDF hinzufügen

Hintergrundbilder können verwendet werden, um ein Wasserzeichen oder ein anderes dezentes Design zu Dokumenten hinzuzufügen. In Aspose.PDF for Python via .NET ist jedes PDF-Dokument eine Sammlung von Seiten und jede Seite enthält eine Sammlung von Artefakten. Der [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/) Klasse kann verwendet werden, um ein Hintergrundbild zu einem Seitenobjekt hinzuzufügen.

Dieser Ansatz ist nützlich, wenn Sie ein dekoratives Bild hinter dem Haupt-PDF-Inhalt platzieren müssen, ohne es in durchsuchbaren Dokumenttext umzuwandeln.

Das folgende Code‑Snippet zeigt, wie man mit Python ein Hintergrundbild zu PDF‑Seiten mithilfe des BackgroundArtifact‑Objekts hinzufügt.

1. Laden Sie das PDF‑Dokument.
1. Erstellen Sie ein Hintergrund‑Artefakt.
1. Laden Sie die Bilddatei.
1. Das Artefakt an eine Seite anhängen.
1. Speichern Sie das aktualisierte Dokument.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_image_to_pdf(infile, imagefile, outfile):
    """Add a background image to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Fügen Sie einem PDF ein Hintergrundbild mit Deckkraft hinzu

Fügen Sie einer PDF‑Seite ein halbtransparentes Hintergrundbild mithilfe von Aspose.PDF for Python hinzu.

Durch das Anwenden von Deckkraft wird das Hintergrundbild teilweise transparent, sodass der ursprüngliche Seiteninhalt (Text, Bilder usw.) deutlich sichtbar bleibt. Dies ist besonders nützlich für:

- Wasserzeichen
- Branding-Overlays
- Subtile Designverbesserungen

Der Hintergrund wird als Artefakt hinzugefügt, wodurch er hinter allen Seiteninhalten bleibt.

1. Laden Sie das PDF‑Dokument.
1. Erstellen Sie ein Hintergrund‑Artefakt.
1. Laden Sie die Bilddatei.
1. Legen Sie den Deckkraftwert fest.
1. Das Artefakt an eine Seite anhängen.
1. Speichern Sie das aktualisierte Dokument.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_image_with_opacity_to_pdf(infile, imagefile, outfile):
    """Add a background image with opacity to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        artifact.opacity = 0.5
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Füge eine Hintergrundfarbe zu einem PDF hinzu

Wenden Sie eine einfarbige Hintergrundfarbe auf eine PDF‑Seite mithilfe von Aspose.PDF for Python an.

1. Laden Sie das PDF‑Dokument.
1. Erstellen Sie ein Hintergrund‑Artefakt.
1. Legen Sie die Hintergrundfarbe fest.
1. Das Artefakt an eine Seite anhängen.
1. Speichern Sie das aktualisierte Dokument.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_color_to_pdf(infile, outfile):
    """Add a solid color background to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_color = ap.Color.dark_khaki
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Hintergrund aus einem PDF entfernen

Entfernen von Hintergrund-Artefakten aus einer PDF‑Seite unter Verwendung von Aspose.PDF for Python.
Hintergründe in PDFs werden häufig als Artefakte gespeichert, und diese Methode identifiziert selektiv und entfernt nur jene Artefakte, die als Hintergrund‑Elemente klassifiziert sind.

1. Laden Sie das PDF‑Dokument.
1. Zugriff auf Seitenartefakte.
1. Hintergrundartefakte filtern.
1. Hintergrundelemente sammeln.
1. Hintergrundartefakte löschen.
1. Speichern Sie das aktualisierte Dokument.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def remove_background(infile, outfile):
    with ap.Document(infile) as document:
        backgrounds = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND
        ]

        for background in backgrounds:
            document.pages[1].artifacts.delete(background)

        document.save(outfile)
```

## Verwandte Artefakt-Themen

- [Arbeiten mit PDF-Artefakten in Python](/pdf/de/python-net/artifacts/)
- [Wasserzeichen zu PDF in Python hinzufügen](/pdf/de/python-net/add-watermarks/)
- [Bates-Nummerierung zu PDF in Python hinzufügen](/pdf/de/python-net/add-bates-numbering/)
- [Zähle Artefakt-Typen in PDF-Dateien](/pdf/de/python-net/counting-artifacts/)