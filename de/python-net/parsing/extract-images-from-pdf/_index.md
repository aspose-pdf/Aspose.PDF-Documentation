---
title: Bilder aus PDF mit Python extrahieren
linktitle: Bilder aus PDF extrahieren
type: docs
weight: 20
url: /de/python-net/extract-images-from-the-pdf-file/
description: Erfahren Sie, wie Sie eingebettete Bilder aus PDF-Dateien mit Aspose.PDF for Python extrahieren.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man Bilder aus PDF via Python extrahiert
Abstract: Dieser Artikel erklärt, wie man eingebettete Bilder aus einem PDF-Dokument mit Aspose.PDF for Python extrahiert. Er behandelt das Öffnen des Quell-PDFs mit der Document-Klasse, das Zugreifen auf ein Bild aus der Page‑Ressourcen‑Sammlung und das Speichern des extrahierten XImage in einer externen Datei zur Wiederverwendung, Inspektion oder Weiterverarbeitung.
---

Verwenden [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) um das PDF zu öffnen, dann auf die Seitenressourcen zuzugreifen, um ein [XImage](https://reference.aspose.com/pdf/python-net/aspose.pdf/ximage/) Objekt und speichere es als separate Datei. Dieser Ansatz ist nützlich, wenn Sie Bilder wiederverwenden, extrahierte Ressourcen untersuchen oder Bildverarbeitungs‑Workflows aus PDF‑Inhalten erstellen müssen.

1. Öffnen Sie das PDF als ein `Document`.
1. Greifen Sie auf die Bildressource der Zielseite zu.
1. Rufen Sie das Erforderliche ab `XImage` aus der Bildsammlung der Seite.
1. Speichern Sie das extrahierte Bild in einer Ausgabedatei.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```
