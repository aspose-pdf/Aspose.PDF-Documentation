---
title: Bildformate in PDF konvertieren in Python
linktitle: Bilder in PDF konvertieren
type: docs
weight: 60
url: /de/python-net/convert-images-format-to-pdf/
lastmod: "2026-05-18"
description: Erfahren Sie, wie Sie BMP, CGM, DICOM, PNG, TIFF, EMF, SVG und andere Bildformate in PDF mit Python und Aspose.PDF for Python via .NET konvertieren.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Wie man Bilder in PDF mit Python konvertiert
Abstract: Dieser Artikel bietet eine umfassende Anleitung zum Konvertieren verschiedener Bildformate in PDF mit Python, wobei speziell Aspose.PDF for Python via .NET genutzt wird. Der Artikel behandelt eine Reihe von Bildformaten, darunter BMP, CGM, DICOM, EMF, GIF, PNG, SVG und TIFF. Jeder Abschnitt beschreibt die erforderlichen Schritte zur Durchführung der Konvertierung und liefert Code‑Snippets, um den Prozess zu veranschaulichen. Zum Beispiel beinhaltet das Konvertieren von BMP zu PDF das Erstellen eines neuen PDF‑Dokuments, das Definieren der Bildposition, das Einfügen des Bildes und das Speichern des Dokuments. Ebenso werden für Formate wie CGM, DICOM und andere spezifische Ladeoptionen und Verarbeitungsschritte aufgeführt. Der Artikel hebt zudem die Vorteile der Verwendung von Aspose.PDF für solche Aufgaben hervor, wie die Unterstützung verschiedener Codierungsmethoden und die Fähigkeit, sowohl Einzel‑Frames als auch Mehrfach‑Frames zu verarbeiten.
---

## Verwandte Konvertierungen

- [PDF in Bildformate konvertieren](/pdf/de/python-net/convert-pdf-to-images-format/) wenn Sie den umgekehrten Workflow benötigen.
- [HTML in PDF konvertieren](/pdf/de/python-net/convert-html-to-pdf/) für Webinhalte und MHTML-Quellen.
- [Andere Dateiformate in PDF konvertieren](/pdf/de/python-net/convert-other-files-to-pdf/) für EPUB, XPS, Text und andere nicht-Bild-Eingaben.

## Python-Bilder zu PDF-Konvertierungen

**Aspose.PDF for Python via .NET** ermöglicht es Ihnen, verschiedene Bildformate in PDF-Dateien zu konvertieren. Unsere Bibliothek zeigt Code‑Snippets für die Konvertierung der beliebtesten Bildformate, wie - BMP, CGM, DICOM, EMF, JPG, PNG, SVG und TIFF.

## BMP in PDF konvertieren

BMP-Dateien in PDF-Dokument mit der **Aspose.PDF for Python via .NET**-Bibliothek konvertieren.

<abbr title="Bitmap Image File">BMP</abbr> Bilder sind Dateien mit einer Erweiterung. BMP steht für Bitmap-Bilddateien, die zum Speichern von Bitmap-Digitalbildern verwendet werden. Diese Bilder sind unabhängig vom Grafikadapter und werden auch als device independent bitmap (DIB) Dateiformat bezeichnet.

Sie können BMP in PDF-Dateien mit Aspose.PDF for Python via .NET API konvertieren. Daher können Sie die folgenden Schritte befolgen, um BMP-Bilder zu konvertieren:

Schritte zum Konvertieren von BMP zu PDF in Python:

1. Erstellen Sie ein leeres PDF-Dokument.
1. Erstellen Sie die benötigte Seite, zum Beispiel haben wir A4 erstellt, aber Sie können Ihr eigenes Format angeben.
1. Platziert das Bild (aus infile) innerhalb der Seite unter Verwendung des definierten Rechtecks.
1. Speichern Sie das Dokument als PDF.

Der folgende Codeausschnitt folgt diesen Schritten und zeigt, wie man BMP mit Python in PDF konvertiert:

```python
import aspose.pdf as ap
from os import path
import sys

def convert_BMP_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Versuchen Sie, BMP online in PDF zu konvertieren**

Aspose präsentiert Ihnen die Online-Anwendung ["BMP zu PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), wo Sie versuchen können, die Funktionalität und die Qualität, mit der es funktioniert, zu untersuchen.

[![Aspose.PDF Konvertierung BMP zu PDF mit App](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## CGM in PDF konvertieren

Konvertieren Sie ein CGM (Computer Graphics Metafile) in PDF (oder ein anderes unterstütztes Format) mit Aspose.PDF for Python via .NET.

<abbr title="Computer Graphics Metafile">CGM</abbr> ist eine Dateierweiterung für ein Computer Graphics Metafile-Format, das häufig in CAD (Computer-Aided Design) und Präsentationsgrafik-Anwendungen verwendet wird. CGM ist ein Vektorformat, das drei verschiedene Kodierungsmethoden unterstützt: binär (am besten für die Lesegeschwindigkeit des Programms), zeichenbasiert (erzeugt die kleinste Dateigröße und ermöglicht schnellere Datenübertragungen) oder Klartextkodierung (ermöglicht es Benutzern, die Datei mit einem Texteditor zu lesen und zu bearbeiten).

Überprüfen Sie das nächste Codebeispiel zur Konvertierung von CGM-Dateien in das PDF-Format.

Schritte zum Konvertieren von CGM in PDF mit Python:

1. Dateipfade definieren
1. Ladeoptionen für CGM festlegen.
1. CGM in PDF konvertieren
1. Druckkonvertierungsnachricht

```python
import aspose.pdf as ap
from os import path
import sys

def convert_CGM_to_PDF(infile, outfile):
    options = ap.CgmLoadOptions()
    document = ap.Document(infile, options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## DICOM in PDF konvertieren

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> format ist der medizinische Industrienstandard für die Erstellung, Speicherung, Übertragung und Visualisierung digitaler medizinischer Bilder und Dokumente von untersuchten Patienten.

**Aspose.PDF for Python** ermöglicht es Ihnen, DICOM- und SVG-Bilder zu konvertieren, aber aus technischen Gründen müssen Sie beim Hinzufügen von Bildern den Dateityp angeben, der dem PDF hinzugefügt werden soll.

Das folgende Code‑Snippet zeigt, wie man DICOM‑Dateien mit Aspose.PDF in das PDF‑Format konvertiert. Sie sollten das DICOM‑Bild laden, das Bild auf einer Seite in einer PDF‑Datei platzieren und die Ausgabe als PDF speichern. Wir verwenden die zusätzliche pydicom‑Bibliothek, um die Abmessungen dieses Bildes festzulegen. Wenn Sie das Bild auf der Seite positionieren möchten, können Sie dieses Code‑Snippet überspringen.

1. Laden Sie die DICOM-Datei.
1. Bildabmessungen extrahieren.
1. Bildgröße drucken.
1. Erstellen Sie ein neues PDF-Dokument.
1. Bereiten Sie das DICOM-Bild für PDF vor.
1. PDF‑Seitengröße und -Ränder festlegen.
1. Fügen Sie das Bild zur Seite hinzu.
1. Speichern Sie das PDF.
1. Druckkonvertierungsnachricht.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_DICOM_to_PDF(infile, outfile):
    # Load the DICOM file
    import pydicom

    dicom_file = pydicom.dcmread(infile)

    # Get the dimensions of the image
    rows = dicom_file.Rows
    columns = dicom_file.Columns

    # Print the dimensions
    print(f"DICOM image size: {rows} x {columns} pixels")

    # Initialize new Document
    document = ap.Document()
    page = document.pages.add()
    image = ap.Image()
    image.file_type = ap.ImageFileType.DICOM
    image.file = infile

    # Set page dimensions
    page.page_info.height = rows
    page.page_info.width = columns
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0
    page.page_info.margin.right = 0
    page.page_info.margin.left = 0
    page.paragraphs.add(image)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Versuchen Sie, DICOM online in PDF zu konvertieren**

Aspose präsentiert Ihnen die Online-Anwendung ["DICOM zu PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), wo Sie versuchen können, die Funktionalität und die Qualität, mit der es funktioniert, zu untersuchen.

[![Aspose.PDF Konvertierung DICOM zu PDF mit App](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## EMF in PDF konvertieren

<abbr title="Enhanced metafile format">EMF</abbr> speichert grafische Bilder geräteunabhängig. EMF‑Metadateien bestehen aus variablen Längerecords in chronologischer Reihenfolge, die das gespeicherte Bild nach dem Parsen auf jedem Ausgabegerät rendern können.

Der folgende Codeabschnitt zeigt, wie man ein EMF mit Python in PDF konvertiert:

```python

import aspose.pdf as ap
from os import path
import sys

def convert_EMF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    # add image to new pdf page
    page.add_image(infile, rectangle)

    # Save the file into PDF format
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Versuchen Sie, EMF online in PDF zu konvertieren**

Aspose präsentiert Ihnen die Online-Anwendung ["EMF zu PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), wo Sie versuchen können, die Funktionalität und die Qualität, mit der es funktioniert, zu untersuchen.

[![Aspose.PDF Konvertierung EMF zu PDF mit App](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## GIF in PDF konvertieren

Konvertieren Sie GIF-Dateien in ein PDF-Dokument mit der **Aspose.PDF for Python via .NET** Bibliothek.

<abbr title="Graphics Interchange Format">GIF</abbr> ist in der Lage, komprimierte Daten ohne Qualitätsverlust in einem Format mit höchstens 256 Farben zu speichern. Das hardwareunabhängige GIF-Format wurde 1987 (GIF87a) von CompuServe entwickelt, um Bitmap-Bilder über Netzwerke zu übertragen.

Der folgende Codeausschnitt folgt diesen Schritten und zeigt, wie man BMP mit Python in PDF konvertiert:

```python

import aspose.pdf as ap
from os import path
import sys

def convert_GIF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Versuchen Sie, GIF online in PDF zu konvertieren**

Aspose präsentiert Ihnen die Online-Anwendung ["GIF zu PDF"](https://products.aspose.app/pdf/conversion/gif-to-pdf/), wo Sie versuchen können, die Funktionalität und die Qualität, mit der es funktioniert, zu untersuchen.

[![Aspose.PDF Konvertierung GIF zu PDF mit App](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## PNG in PDF konvertieren

**Aspose.PDF for Python via .NET** unterstützt die Funktion, PNG‑Bilder in das PDF‑Format zu konvertieren. Prüfen Sie das nächste Code‑Snippet, um Ihre Aufgabe zu realisieren.

<abbr title="Portable Network Graphics">PNG</abbr> Bezieht sich auf einen Typ von Rasterbild-Dateiformat, das verlustfreie Kompression verwendet und dadurch bei seinen Benutzern beliebt ist.

Sie können PNG in ein PDF‑Bild konvertieren, indem Sie die folgenden Schritte ausführen:

1. Erstelle ein neues PDF-Dokument.
1. Bildplatzierung definieren.
1. Speichern Sie das PDF.
1. Druckkonvertierungsnachricht.

Außerdem zeigt das nachstehende Code‑Snippet, wie man PNG mit Python in PDF umwandelt:

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PNG_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Versuchen Sie, PNG online in PDF zu konvertieren**

Aspose präsentiert Ihnen die Online-Anwendung ["PNG zu PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), wo Sie versuchen können, die Funktionalität und die Qualität, mit der es funktioniert, zu untersuchen.

[![Aspose.PDF Konvertierung PNG zu PDF mit App](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## SVG in PDF konvertieren

**Aspose.PDF for Python via .NET** erklärt, wie man SVG‑Bilder in das PDF‑Format konvertiert und wie man die Abmessungen der Quell‑SVG‑Datei ermittelt.

Scalable Vector Graphics (SVG) ist eine Familie von Spezifikationen eines XML-basierten Dateiformats für zweidimensionale Vektorgrafiken, sowohl statisch als auch dynamisch (interaktiv oder animiert). Die SVG‑Spezifikation ist ein offener Standard, der seit 1999 vom World Wide Web Consortium (W3C) entwickelt wird.

<abbr title="Scalable Vector Graphics">SVG</abbr> Bilder und ihr Verhalten werden in XML-Textdateien definiert. Das bedeutet, dass sie durchsucht, indiziert, geskriptet und bei Bedarf komprimiert werden können. Als XML-Dateien können SVG-Bilder mit jedem Texteditor erstellt und bearbeitet werden, aber es ist oft praktischer, sie mit Zeichenprogrammen wie Inkscape zu erstellen.

{{% alert color="success" %}}
**Versuchen Sie, das SVG-Format online in PDF zu konvertieren**

Aspose.PDF for Python via .NET präsentiert Ihnen eine Online-Anwendung ["SVG zu PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), wo Sie versuchen können, die Funktionalität und die Qualität, mit der es funktioniert, zu untersuchen.

[![Aspose.PDF Konvertierung SVG zu PDF mit App](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

Das folgende Codebeispiel zeigt den Prozess der Konvertierung einer SVG-Datei in das PDF-Format mit Aspose.PDF for Python.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_SVG_to_PDF(infile, outfile):
    load_options = ap.SvgLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## TIFF in PDF konvertieren

**Aspose.PDF** Dateiformat unterstützt, sei es ein einzelnes oder mehrrahmeniges TIFF-Bild. Das bedeutet, dass Sie das TIFF-Bild in PDF konvertieren können.

TIFF oder TIF, Tagged Image File Format, repräsentiert Rasterbilder, die für die Nutzung auf einer Vielzahl von Geräten gedacht sind, die diesen Dateiformatstandard einhalten. Ein TIFF‑Bild kann mehrere Frames mit unterschiedlichen Bildern enthalten. Das Aspose.PDF‑Dateiformat wird ebenfalls unterstützt, sei es ein einzelner Frame oder ein Mehr‑Frame‑TIFF‑Bild.

Sie können TIFF zu PDF auf die gleiche Weise wie die übrigen Rasterdateiformate konvertieren:

```python
import aspose.pdf as ap
from os import path
import sys

def convert_TIFF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## CDR in PDF konvertieren

Das folgende Code‑Snippet zeigt, wie man eine CorelDRAW‑(CDR‑)Datei lädt und sie mit 'CdrLoadOptions' in Aspose.PDF for Python via .NET als PDF speichert.

1. Erstellen Sie 'CdrLoadOptions()', um zu konfigurieren, wie die CDR-Datei geladen werden soll.
1. Initialisieren Sie ein Document-Objekt mit der CDR-Datei und den Ladeoptionen.
1. Speichern Sie das Dokument als PDF.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_CDR_to_PDF(infile, outfile):
    load_options = ap.CdrLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## JPEG in PDF konvertieren

Dieses Beispiel zeigt, wie man JPEG in eine PDF‑Datei konvertiert, wobei Aspose.PDF for Python via .NET verwendet wird.

1. Erstellen Sie ein neues PDF-Dokument.
1. Füge eine neue Seite hinzu.
1. Definieren Sie das Platzierungsrechteck (A4-Größe: 595x842 Punkte).
1. Fügen Sie das Bild in die Seite ein.
1. Speichern Sie das PDF.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_JPEG_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```
