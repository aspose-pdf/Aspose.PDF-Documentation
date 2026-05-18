---
title: PDF-Links in Python extrahieren
linktitle: Links extrahieren
type: docs
weight: 30
url: /de/python-net/extract-links/
description: Erfahren Sie, wie Sie Link-Annotationen und Hyperlinks aus PDF-Dokumenten in Python extrahieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man Links aus PDF extrahiert
Abstract: Der Leitfaden Aspose.PDF for Python via .NET zum Extrahieren von Links erklärt, wie Hyperlink-Annotationen programmgesteuert aus PDF‑Dokumenten mit Python abgerufen werden können. Die Dokumentation enthält praktische Codebeispiele und verdeutlicht, wie diese Funktionalität für Aufgaben wie Link‑Audit, Navigationsanalyse oder den Aufbau interaktiver Dokumenten‑Features genutzt werden kann. Unabhängig davon, ob Sie mit einseitigen PDFs arbeiten oder große Stapel verarbeiten, bietet dieser Leitfaden einen klaren und effizienten Ansatz zur Hyperlink‑Extraktion.
---

## Links aus der PDF-Datei extrahieren

Dieses Beispiel demonstriert, wie man mit Aspose.PDF for Python durch alle Link-Annotationen auf der ersten Seite eines PDFs iteriert. Es filtert Annotationen, um solche vom Typ LinkAnnotation zu identifizieren, wirft sie sicher um und gibt dann ihren Seitenindex sowie ihre rechteckige Position auf der Seite aus.

Dies kann für Debugging, Analysen oder automatisierte Aktualisierungen vorhandener Link-Annotationen in einem PDF verwendet werden.

1. Laden Sie das PDF-Dokument. Verwenden Sie ap.Document(path_infile), um die Datei zu öffnen.
1. Greifen Sie auf Annotationen der ersten Seite zu. Verwenden Sie document.pages[1].annotations, um alle Annotationen abzurufen.
1. Filtern Sie nur nach LinkAnnotation-Typen. Prüfen Sie den annotation_type jeder Annotation.
1. Wandeln Sie LinkAnnotations um und verarbeiten Sie sie. Verwenden Sie is_assignable() und cast(), um einen sicheren Zugriff auf die Eigenschaften von LinkAnnotation zu gewährleisten.
1. Drucken Sie Anmerkungsdetails. Geben Sie den Seitenindex und das Rechteck (Position) jedes Links aus.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def extract_link_annotation(infile):

    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        if is_assignable(la, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, la)
            print(f"Page: {annotation.page_index}, location: {annotation.rect}")
```

## HyperLinks aus der PDF-Datei extrahieren

Dieser Code demonstriert, wie man alle LinkAnnotation-Objekte von der ersten Seite eines PDF-Dokuments mithilfe von Aspose.PDF for Python extrahiert und anschließend diejenigen identifiziert, die eine GoToURIAction enthalten. Für jeden solchen Link gibt er den Seitenindex und die Ziel-URI aus.

Dies ist nützlich für Aufgaben wie:

- Überprüfung externer Links in einem PDF
- Extrahieren von Dokumentations- oder Support-URLs
- Erkennen von defekten oder veralteten Hyperlinks

1. Laden Sie das PDF-Dokument. Öffnen Sie die Datei mit ap.Document.
1. Alle Link-Annotationen von der ersten Seite abrufen. Annotationen filtern, um nur solche mit dem Typ AnnotationType.LINK einzuschließen.
1. Typ prüfen und zu LinkAnnotation casten. Sicherstellen, dass jede Annotation tatsächlich eine LinkAnnotation ist, bevor auf ihre Eigenschaften zugegriffen wird.
1. Den Aktionstyp des Links prüfen. Filtern nach Links, die eine GoToURIAction verwenden (d. h. Links zu einer Web-URL).
1. URI und Seitenindex extrahieren und ausgeben. Verwenden Sie .uri, um den externen Link zu erhalten, und .page_index für den Kontext.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def extract_hyperlinks(infile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        if is_assignable(la, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, la)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                action = cast(ap.annotations.GoToURIAction, annotation.action)
                print(f"Page {annotation.page_index}, URI:{action.uri}")
```

## Verwandte Link-Themen

- [Arbeiten mit PDF-Links in Python](/pdf/de/python-net/links/)
- [PDF-Links in Python erstellen](/pdf/de/python-net/create-links/)
- [Links in PDF mit Python aktualisieren](/pdf/de/python-net/update-links/)