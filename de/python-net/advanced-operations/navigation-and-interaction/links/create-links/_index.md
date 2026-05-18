---
title: PDF-Links in Python erstellen
linktitle: Links erstellen
type: docs
weight: 10
url: /de/python-net/create-links/
description: Erfahren Sie, wie Sie interne, externe und entfernte PDF-Links in Python erstellen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man Links in PDF erstellt
Abstract: Der Aspose.PDF for Python via .NET Leitfaden zum Erstellen von Links bietet Entwicklern praktische Anweisungen zum Hinzufügen interaktiver Hyperlinks zu PDF-Dokumenten mit Python. Er behandelt, wie verschiedene Arten von Links erstellt werden, einschließlich solcher, die externe Anwendungen starten, zu bestimmten Seiten im selben Dokument navigieren oder andere PDF-Dateien öffnen. Die Dokumentation erklärt, wie LinkAnnotation-Objekte verwendet werden, klickbare Bereiche mit Rectangle definiert und Aktionen wie LaunchAction oder GoToRemoteAction zugewiesen werden. Mit klaren Codebeispielen und Schritt‑für‑Schritt‑Anleitungen hilft diese Ressource Entwicklern, die PDF‑Navigation und Interaktivität in ihren Python‑Anwendungen zu verbessern.
---

## Links in PDF-Dokumenten

Gemäß der PDF 1.7 Spezifikation (ISO 32000-1:2008) kann eine **Link annotation** mehrere Arten von Aktionen auslösen, die definieren, was geschieht, wenn die Annotation aktiviert wird. Hier sind die unterstützten Hauptaktionen:

1. **GoTo** – Navigiert zu einem Ziel innerhalb desselben Dokuments.
1. **GoToR** – Springt zu einem Ziel in einer anderen PDF-Datei (Remote-GoTo).
1. **URI** – Öffnet einen Uniform Resource Identifier, typischerweise einen Web-Link.
1. **Launch** – Startet eine Anwendung oder öffnet eine Datei (plattformabhängig und oft aus Sicherheitsgründen eingeschränkt).
1. **Named** – Führt eine vordefinierte Aktion aus, z. B. zum nächsten Blatt gehen oder das Dokument drucken.
1. **JavaScript** – Führt eingebetteten JavaScript‑Code aus (mit Vorsicht zu verwenden wegen Sicherheitsbedenken).
1. **SubmitForm** – Sendet Formulardaten an eine angegebene URL.
1. **ResetForm** – Setzt Formularfelder auf ihre Standardwerte zurück.
1. **ImportData** – Importiert Daten aus einer externen Datei in das Dokument.

Durch das Hinzufügen eines Links zu einer Anwendung in ein Dokument ist es möglich, von einem Dokument aus auf Anwendungen zu verlinken. Das ist nützlich, wenn Sie möchten, dass Leser an einem bestimmten Punkt in einem Tutorial eine bestimmte Aktion ausführen, zum Beispiel, oder um ein funktionsreiches Dokument zu erstellen.

Um einen Anwendungslink mit ‘LaunchAction’ zu erstellen:

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_launch_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    border = ap.annotations.Border(link)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    link.color = ap.Color.green
    link.action = ap.annotations.LaunchAction(document, "sample.pdf")
    page.annotations.append(link)
    document.save(outfile)
```

## PDF-Dokumentlink in einer PDF-Datei erstellen

### Verwendung von GoToRemoteAction

Dieses Code‑Snippet demonstriert, wie man mit einer Python‑PDF‑Bibliothek eine Link‑Annotation zu einer bestimmten Seite eines PDF‑Dokuments hinzufügt.

1. PDF‑Dokument öffnen
1. Wählen Sie die zweite Seite des Dokuments aus (Index 1)
1. Erstellen Sie eine Link-Annotation:
1. Positioniert bei den Koordinaten (10, 580, 120, 600)
1. Grün gefärbt
1. Links zu 'sample.pdf' auf seiner ersten Seite
1. Fügen Sie die Link-Annotation zur Seite hinzu
1. Speichern Sie das modifizierte Dokument im Ausgabedateipfad

Um einen PDF-Dokumentenlink mit 'GoToRemoteAction' zu erstellen:

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_go_to_remote_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    link.color = ap.Color.green
    link.action = ap.annotations.GoToRemoteAction("sample.pdf", 1)
    page.annotations.append(link)
    document.save(outfile)
```

### Verwenden von GoToAction

Dieser Code demonstriert, wie man einer bestimmten Seite eines PDF-Dokuments mithilfe von Aspose.PDF for Python eine Linkannotation hinzufügt. Der Link erscheint als ein grünes, gestricheltes Rechteck und ermöglicht dem Benutzer, zu einer anderen Seite im selben PDF zu navigieren. So erstellen Sie einen PDF-Dokument-Link mithilfe von 'GoToAction':

```python
import aspose.pdf as ap
from os import path
import sys

def create_link_annotation_go_to_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    border = ap.annotations.Border(link)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    link.color = ap.Color.green
    if document.pages.length >= 4:
        link.action = ap.annotations.GoToAction(document.pages[4])
    else:
        link.action = ap.annotations.GoToAction(document.pages[document.pages.length])
    page.annotations.append(link)
    document.save(outfile)
```

### Anwenden von GoToURIAction

Das nächste Beispiel zeigt, wie man einer PDF‑Datei mithilfe von Aspose.PDF for Python eine Link‑Annotation hinzufügt. Der Link erscheint als grüner klickbarer Bereich auf der ersten Seite und öffnet beim Anklicken die Aspose.PDF for Python‑Dokumentation in einem Webbrowser über eine GoToURIAction.

Diese Funktionalität ist nützlich, um hilfreiche externe Referenzen, Dokumentationen oder Support‑Links direkt in Ihre PDFs einzubetten.

1. Laden Sie das PDF Document. Öffnen Sie die vorhandene PDF-Datei mit ap.Document.
1. Greifen Sie auf die erste Seite zu. Verwenden Sie document.pages[1], um die erste Seite zuzugreifen (Aspose verwendet 1-basierte Indizierung).
1. Erstellen Sie eine Link-Annotation. Erstellen Sie ein LinkAnnotation-Objekt und geben Sie den anklickbaren rechteckigen Bereich mit ap.Rectangle an.
1. Legen Sie das Aussehen der Annotation fest. Setzen Sie die Farbe der Annotation auf Grün, indem Sie link.color = ap.Color.green verwenden.
1. Weisen Sie eine URI‑Aktion zu. Verwenden Sie GoToURIAction, um die Annotation mit einer externen URL zu verknüpfen.
1. Fügen Sie die Annotation zur Seite hinzu. Hängen Sie die konfigurierte Link‑Annotation an die Annotationssammlung der ersten Seite an.
1. Speichern Sie das modifizierte Dokument. Speichern Sie das aktualisierte PDF‑Dokument am angegebenen Ausgabepfad.

```python
import aspose.pdf as ap
from os import path
import sys
    
def create_link_annotation_go_to_URI_action(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))
    link.color = ap.Color.green
    link.action = ap.annotations.GoToURIAction("https://docs.aspose.com/pdf/python")
    page.annotations.append(link)
    document.save(outfile)
```

## Verwandte Link-Themen

- [Arbeiten mit PDF-Links in Python](/pdf/de/python-net/links/)
- [Links aus PDF in Python extrahieren](/pdf/de/python-net/extract-links/)
- [Links in PDF mit Python aktualisieren](/pdf/de/python-net/update-links/)