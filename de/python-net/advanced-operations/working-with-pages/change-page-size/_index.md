---
title: PDF-Seitengröße in Python ändern
linktitle: Seitengröße ändern
type: docs
weight: 40
url: /de/python-net/change-page-size/
description: Erfahren Sie, wie Sie PDF‑Seitendimensionen in Python lesen und ändern.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Seitengröße mit Python ändern
Abstract: Dieser Artikel zeigt, wie man PDF‑Seitengrößen mit Aspose.PDF ausliest und ändert. Das Beispiel Get Page Size ermittelt die Breite und Höhe einer bestimmten PDF‑Seite, sodass Benutzer das Layout der Seite prüfen, die Formatierung validieren oder die Dokumentenstruktur analysieren können. Das Beispiel Set Page Size zeigt, wie man die Abmessungen einer Seite ändert – beispielsweise die erste Seite in A4‑Größe konvertiert – und gleichzeitig die Box‑Eigenschaften (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) vor und nach der Modifikation anzeigt.
---

Aspose.PDF for Python via .NET ermöglicht das Ändern der PDF‑Seitengröße mit einfachen Codezeilen. Dieses Thema zeigt, wie man Seitenabmessungen mit der [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) und [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) APIs.

Verwenden Sie dieses Handbuch, wenn Sie vorhandene PDF‑Seiten skalieren, Dokumentabmessungen normalisieren oder die Seiteneinstellungen der Boxen in Python prüfen müssen.

{{% alert color="primary" %}}

Bitte beachten Sie, dass die Eigenschaften Höhe und Breite Punkte als Basiseinheit verwenden, wobei 1 Zoll = 72 Punkte und 1 cm = 1/2,54 Zoll = 0,3937 Zoll = 28,3 Punkte.

{{% /alert %}}

## Setzen Sie die Seitengröße einer PDF‑Seite auf A4

Das Beispiel aktualisiert die Größe der ersten Seite eines PDF‑Dokuments auf die Standard‑A4‑Abmessungen. Es gibt außerdem die Box‑Abmessungen der Seite (CropBox, TrimBox, ArtBox, BleedBox, MediaBox) vor und nach der Größenänderung aus, sodass Sie die Änderungen überprüfen können.

Der folgende Codeabschnitt zeigt, wie Sie die PDF‑Seitenabmessungen auf die Größe A4 ändern:

1. Greifen Sie auf das erste zu [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) des [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Zeigen Sie die Boxgrößen der Seite vor der Änderung an (CropBox, TrimBox, ArtBox, BleedBox, MediaBox).
1. Wenden Sie A4‑Abmessungen (597.6 × 842.4 Punkte) mithilfe der page API an.
1. Anzeige der aktualisierten Seitenboxgrößen.
1. Speichern Sie das modifizierte [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) zum angegebenen Ausgabepfad.

```python
import aspose.pdf as ap

def set_page_size(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]

    # Set the page size as A4 (8.3 x 11.7 in) and in Aspose.Pdf, 1 inch = 72 points
    # So A4 dimensions in points will be (597.6, 842.4) for portrait orientation
    print("Before set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    page.set_page_size(597.6, 842.4)
    print("After set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Save the updated document
    document.save(output_file_name)
```

## PDF-Seitengröße abrufen

Dieses Snippet liest ein PDF und ermittelt die Abmessungen (Breite und Höhe) der ersten Seite. Es verwendet das [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) API, um die Begrenzung der Seite zu extrahieren [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) und gibt deren Größe in der Konsole aus. Dies ist nützlich, um das Seitenlayout zu inspizieren, Formate zu überprüfen oder Dokumente für die weitere Verarbeitung vorzubereiten.

1. Lade das PDF als [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Greifen Sie auf das erste zu [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Ermitteln Sie das Begrenzungsrechteck der Seite mit `get_page_rect()`.
1. Extrahiere die Breiten- und Höhenwerte.
1. Gib die Seitenmaße aus.

```python
import aspose.pdf as ap

def get_page_size(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    # Get particular page
    page = document.pages[1]
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

### PDF‑Seitengröße vor und nach der Drehung ermitteln

Abrufen der Abmessungen einer PDF-Seite vor und nach Anwendung einer 90°-Drehung. Dies demonstriert, wie die Drehung Breite und Höhe beeinflusst und wie man es verwendet `get_page_rect()` mit oder ohne Berücksichtigung der Rotation.

1. Öffnen Sie das PDF als ein [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Greifen Sie auf das erste zu [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Wenden Sie eine 90°-Drehung an `page.rotate = ap.Rotation.ON90` (siehe die [`Rotation`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rotation/) enum).
1. Rufen Sie das Seitenrechteck ohne Rotation ab `get_page_rect(False)` und drucke seine Breite und Höhe.
1. Rufen Sie das Seitenrechteck unter Berücksichtigung der Drehung ab `get_page_rect(True)` und drucke seine Breite und Höhe.
1. Vergleichen Sie, wie sich die Abmessungen durch die Rotation ändern.

```python
import aspose.pdf as ap

def get_page_size_rotation(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]
    page.rotate = ap.Rotation.ON90
    rectangle = page.get_page_rect(False)
    print(f"{rectangle.width} : {rectangle.height}")
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

## Verwandte Seitenthemen

- [Arbeiten Sie mit PDF-Seiten in Python](/pdf/de/python-net/working-with-pages/)
- [PDF‑Seiten in Python zuschneiden](/pdf/de/python-net/crop-pages/)
- [PDF‑Seiteneigenschaften in Python abrufen und festlegen](/pdf/de/python-net/get-and-set-page-properties/)
- [PDF‑Seiten in Python drehen](/pdf/de/python-net/rotate-pages/)