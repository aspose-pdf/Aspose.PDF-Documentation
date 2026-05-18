---
title: PDF-Links in Python aktualisieren
linktitle: Links aktualisieren
type: docs
weight: 20
url: /de/python-net/update-links/
description: Erfahren Sie, wie Sie das Aussehen und die Ziele von PDF-Links in Python aktualisieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man Links in PDF aktualisiert
Abstract: Der Aspose.PDF for Python via .NET Leitfaden zum Aktualisieren von Links führt Entwickler durch den Prozess der Änderung des Hyperlink‑Verhaltens in PDF‑Dokumenten mit Python. Er erklärt, wie man Linkziele ändert, um auf bestimmte Seiten, externe Websites oder sogar andere PDF‑Dateien zu verweisen. Die Dokumentation behandelt auch, wie das Aussehen von Linkannotation‑Anmerkungen, einschließlich Textfarbe, angepasst wird, und liefert praktische Codebeispiele für jedes Szenario. Egal, ob Sie veraltete URLs korrigieren oder die Navigation verbessern, bietet diese Ressource einen klaren und effizienten Ansatz zur programmgesteuerten Verwaltung von Links.
---

## LinkAnnotation-Textfarbe aktualisieren

Dieses Beispiel zeigt, wie man alle Link-Annotationen auf der ersten Seite eines PDF mit Aspose.PDF for Python erkennt und dann den Text in der Nähe jedes Links hervorhebt, indem man seine Schriftfarbe auf Rot ändert. Es verwendet TextFragmentAbsorber mit einem leicht erweiterten Bereich um jedes Link‑Rechteck, um nahegelegenen Text zu finden und zu ändern.

Dies kann verwendet werden für:

- Visuelles Markieren von Links in einem Dokument
- Verbesserung der Barrierefreiheit durch Hervorheben verknüpfter Inhalte
- Vorverarbeitung von PDF-Dateien vor der Überprüfung oder dem Export

Für jede dieser Link-Annotationen ruft das Skript die rechteckige Begrenzung ab und erweitert diesen Bereich leicht, um nahegelegenen Text einzuschließen, was eine breitere visuelle Identifizierung ermöglicht. Anschließend wird ein TextFragmentAbsorber über diesem erweiterten Bereich angewendet, um alle darin befindlichen Textfragmente zu extrahieren. Diese erfassten Fragmente werden modifiziert, indem ihre Schriftfarbe auf Rot geändert wird, wodurch der umgebende Text zur Hervorhebung und Überprüfung markiert wird. Nachdem alle diese Aktualisierungen angewendet wurden, wird das modifizierte Dokument im Ausgabepfad gespeichert, wobei die hervorgehobenen Anmerkungen und ihr zugehöriger Text erhalten bleiben.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_text_color(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        ta = ap.text.TextFragmentAbsorber()
        rect = la.rect
        rect.llx -= 2
        rect.lly -= 2
        rect.urx += 2
        rect.ury += 2
        ta.text_search_options = ap.text.TextSearchOptions(rect)
        ta.visit(document.pages[1])
        for textFragment in ta.text_fragments:
            textFragment.text_state.foreground_color = ap.Color.red

    document.save(outfile)
```

## Rand aktualisieren

Das Skript konzentriert sich auf die erste Seite des Dokuments und filtert alle Anmerkungen heraus, wobei nur solche vom Typ LINK ausgewählt werden – diese stellen typischerweise interaktive Elemente wie Hyperlinks oder Navigationsauslöser dar. Für jede dieser Link-Anmerkungen wird im Code die Instanz zum Typ LinkAnnotation umgewandelt und die color-Eigenschaft auf Rot gesetzt, wodurch sie visuell hervorgehoben werden, um sich vom übrigen Inhalt abzuheben. Nachdem alle Link-Anmerkungen geändert wurden, wird das aktualisierte Dokument an dem definierten Ausgabepfad gespeichert und das neue Styling beibehalten.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_border(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        link_annotation = cast(ap.annotations.LinkAnnotation, la)
        link_annotation.color = ap.Color.red

    document.save(outfile)
```

## Webziel aktualisieren

Sobald die Pfade eingerichtet sind, wird das Originaldokument mithilfe der Aspose.PDF-Bibliothek geladen, wodurch sein Inhalt für Änderungen zugänglich wird. Das Skript konzentriert sich dann auf die erste Seite des Dokuments, filtert alle Anmerkungen heraus und wählt nur diejenigen aus, die vom Typ Link sind, typischerweise klickbare Bereiche oder Hyperlinks darstellen. Um Typfehler zu vermeiden und eine sichere Handhabung zu gewährleisten, wird jede Anmerkung mit is_assignable überprüft und dann in den entsprechenden LinkAnnotation-Typ umgewandelt. Wenn der Link mit einer GoToURIAction verknüpft ist, d. h. er verweist auf eine Webadresse, aktualisiert das Skript diese URI, um Benutzer zu "https://www.aspose.com". Schließlich wird das Document, nachdem alle gewünschten Änderungen angewendet wurden, am angegebenen Ausgabepfad gespeichert.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_web_destination(infile, outfile):
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
                action.uri = "https://www.aspose.com"
    document.save(outfile)
```

## Verwandte Link-Themen

- [Arbeiten mit PDF-Links in Python](/pdf/de/python-net/links/)
- [PDF-Links in Python erstellen](/pdf/de/python-net/create-links/)
- [PDF-Links in Python extrahieren](/pdf/de/python-net/extract-links/)