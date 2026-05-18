---
title: PDF-Seiten in Python drehen
linktitle: PDF-Seiten drehen
type: docs
weight: 110
url: /de/python-net/rotate-pages/
description: Erfahren Sie, wie Sie PDF-Seiten drehen und die Seitenausrichtung in Python ändern.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man Seiten in PDF mit Python dreht
Abstract: Dieser Artikel bietet eine Anleitung, wie man die Seitenausrichtung von Seiten in einer bestehenden PDF‑Datei programmgesteuert mit Python aktualisiert oder ändert. Durch die Nutzung von Aspose.PDF for Python via .NET können Benutzer einfach zwischen Quer- und Hochformat wechseln, indem sie die MediaBox‑Eigenschaften der Seite anpassen. Der Artikel enthält ein Python‑Code‑Snippet, das demonstriert, wie man durch die Seiten eines PDF‑Dokuments iteriert, deren MediaBox‑Abmessungen und -Positionen ändert und bei Bedarf die CropBox anpasst. Zusätzlich erklärt er, wie man den Rotationswinkel der Seiten mit der „rotate“-Methode festlegt, um die gewünschte Ausrichtung zu erreichen. Der Vorgang endet mit dem Speichern der aktualisierten PDF‑Datei.
---

Dieses Thema beschreibt, wie man die Seitenausrichtung von Seiten in einer bestehenden PDF‑Datei programmgesteuert mit Python aktualisiert oder ändert.

Verwenden Sie diese Seite, wenn Sie Seiten zwischen Hochformat und Querformat umschalten oder Rotationswinkel auf vorhandene PDF‑Inhalte anwenden müssen.

## Seitenorientierung ändern

Diese Funktion dreht jede Seite eines PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 90 Grad im Uhrzeigersinn mit Aspose.PDF for Python.
Sie ist nützlich, um Probleme mit der Seitenorientierung zu korrigieren, beispielsweise gescannte Dokumente, die seitlich liegen. Das ursprüngliche PDF bleibt unverändert, und die gedrehte Version wird als neue Datei gespeichert.

```python
import sys
import aspose.pdf as ap
from os import path

def rotate_page(infile, outfile):
    document = ap.Document(infile)
    for page in document.pages:
        page.rotate = ap.Rotation.ON90

    document.save(outfile)
```

## Verwandte Seitenthemen

- [Arbeiten Sie mit PDF-Seiten in Python](/pdf/de/python-net/working-with-pages/)
- [PDF-Seitengröße in Python ändern](/pdf/de/python-net/change-page-size/)
- [PDF‑Seiten in Python zuschneiden](/pdf/de/python-net/crop-pages/)
- [PDF‑Seiteneigenschaften in Python abrufen und festlegen](/pdf/de/python-net/get-and-set-page-properties/)