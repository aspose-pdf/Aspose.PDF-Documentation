---
title: Schriftarten aus PDF mit Python extrahieren
linktitle: Schriftarten aus PDF extrahieren
type: docs
weight: 30
url: /de/python-net/extract-fonts-from-pdf/
description: Verwenden Sie die Aspose.PDF for Python-Bibliothek, um alle eingebetteten Schriftarten aus Ihrem PDF-Dokument zu extrahieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man Schriftarten aus PDF mit Python extrahiert
Abstract: Dieser Artikel erklärt, wie man die in einem PDF-Dokument verwendeten Schriftarten mit Aspose.PDF for Python inspiziert. Er zeigt, wie man ein PDF mit der Document-Klasse öffnet, font_utilities.get_all_fonts() aufruft, um die verfügbaren Schriftobjekte abzurufen, und durch die Ergebnisse iteriert, um Schriftnamen für Analyse, Prüfung oder Dokumentenverarbeitungs‑Workflows zu lesen.
---

Verwenden [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) um das PDF zu öffnen und aufzurufen `font_utilities.get_all_fonts()` alle verfügbaren abrufen [Font](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/font/) Objekte, auf die das Dokument verweist. Dies ist nützlich beim Prüfen eingebetteter Schriften, beim Überprüfen der Schriftverfügbarkeit vor der Konvertierung oder bei der Analyse von Dokumentressourcen.

1. Öffnen Sie das Quell‑PDF als `Document`.
1. Anruf `document.font_utilities.get_all_fonts()` um die Font-Sammlung zu erhalten.
1. Durch das Zurückgegebene iterieren `Font` Objekte.
1. Lese und drucke jedes `font.font_name` Wert.

```python

    import aspose.pdf as apdf
    from os import path

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    fonts = document.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```
