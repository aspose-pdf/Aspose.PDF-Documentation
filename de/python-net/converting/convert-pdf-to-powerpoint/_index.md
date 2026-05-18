---
title: PDF in PowerPoint mit Python konvertieren
linktitle: PDF in PowerPoint konvertieren
type: docs
weight: 30
url: /de/python-net/convert-pdf-to-powerpoint/
description: Erfahren Sie, wie Sie PDF‑Dateien in Python mit Aspose.PDF for Python via .NET zu PowerPoint konvertieren, einschließlich bearbeitbarer PPTX‑Folien und bildbasierter Folienaussgabe.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man PDF in PowerPoint mit Python konvertiert
Abstract: Dieser Artikel bietet eine umfassende Anleitung zur Konvertierung von PDF-Dateien in PowerPoint-Präsentationen mithilfe von Python, wobei der Fokus speziell auf das PPTX-Format liegt. Er führt die Verwendung von Aspose.PDF for Python via .NET ein, das den Konvertierungsprozess erleichtert, indem es ermöglicht, PDF-Seiten in einzelne Folien einer PPTX-Datei zu verwandeln. Der Artikel beschreibt die notwendigen Schritte für die Konvertierung, einschließlich der Erstellung von Instanzen der Klassen Document und PptxSaveOptions sowie der Verwendung der Save‑Methode. Zusätzlich wird eine Funktion hervorgehoben, mit der PDFs in PPTX konvertiert werden können, wobei die Folien als Bilder vorliegen, indem eine bestimmte Eigenschaft in PptxSaveOptions gesetzt wird. Code‑Snippets werden bereitgestellt, um den Konvertierungsprozess zu veranschaulichen. Der Artikel verweist außerdem auf eine Online‑Anwendung zum Testen der PDF‑zu‑PPTX‑Konvertierungsfunktion, die den Benutzern ein praktisches Erlebnis bietet. Darüber hinaus listet er verschiedene verwandte Themen und Funktionalitäten auf, die in diesem Kontext verfügbar sind, und betont die Vielseitigkeit sowie den programmatischen Ansatz für die Handhabung von PDF‑zu‑PowerPoint‑Konvertierungen mit Python.
---

## Python PDF zu PowerPoint und PPTX-Konvertierung

**Aspose.PDF for Python via .NET** ermöglicht Ihnen, den Fortschritt der PDF-zu-PPTX-Konvertierung zu verfolgen.

Wir haben eine API namens Aspose.Slides, die die Funktion bietet, PPT/PPTX-Präsentationen zu erstellen und zu bearbeiten. Diese API bietet auch die Funktion, zu konvertieren <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr> Dateien in PDF-Format. Während dieser Konvertierung werden die einzelnen Seiten der PDF-Datei in separate Folien in der PPTX-Datei konvertiert.

Während der PDF-zu-PPTX-Konvertierung wird der Text als Text gerendert, den Sie auswählen/aktualisieren können. Bitte beachten Sie, dass Aspose.PDF zur Konvertierung von PDF-Dateien in das PPTX-Format eine Klasse mit dem Namen bereitstellt. [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/). Ein Objekt der PptxSaveOptions-Klasse wird als zweites Argument an die [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)Das folgende Code-Snippet zeigt den Vorgang, PDF‑Dateien in das PPTX‑Format zu konvertieren.

Diese Konvertierung ist besonders nützlich, wenn Sie PDF‑Berichte, Folienpräsentationen oder Handouts in bearbeitbare Präsentationsdateien umwandeln möchten.

## Einfache Konvertierung von PDF zu PowerPoint mit Python und Aspose.PDF for Python via .NET

Um PDF in PPTX zu konvertieren, empfiehlt Aspose.PDF for Python die folgenden Code‑Schritte zu verwenden.

Schritte: PDF in PowerPoint mit Python konvertieren

1. Erstelle eine Instanz von [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Klasse.
1. Erstelle eine Instanz von [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) Klasse.
1. Rufen Sie die [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) Methode.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    document.save(outfile, save_options)
```

## PDF in PPTX mit Folien als Bilder konvertieren

{{% alert color="success" %}}
**Versuchen Sie, PDF online in PowerPoint zu konvertieren**

Aspose.PDF präsentiert Ihnen die Online-Anwendung ["PDF zu PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), wo Sie versuchen können, die Funktionalität und die Qualität, mit der es funktioniert, zu untersuchen.


[![Aspose.PDF-Konvertierung PDF zu PPTX mit App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

Falls Sie ein durchsuchbares PDF in PPTX als Bilder anstelle von auswählbarem Text konvertieren müssen, bietet Aspose.PDF diese Funktion über [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) class. Um dies zu erreichen, setzen Sie die Eigenschaft [slides_as_images](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) von [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) Klasse zu 'true', wie im folgenden Codebeispiel gezeigt.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX_slides_as_images(infile, outfile):

    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    save_options.slides_as_images = True

    document.save(outfile, save_options)
```

## PDF zu PPTX mit benutzerdefinierter Bildauflösung konvertieren

Diese Methode konvertiert ein PDF-Dokument in eine PowerPoint‑Datei (PPTX), wobei eine benutzerdefinierte Bildauflösung (300 DPI) für verbesserte Qualität festgelegt wird.

1. Laden Sie das PDF in ein 'ap.Document'-Objekt.
1. Erstellen Sie eine 'PptxSaveOptions'-Instanz.
1. Setzen Sie die Eigenschaft 'image_resolution' auf 300 DPI für eine hochqualitative Darstellung.
1. Speichern Sie die PDF-Datei als PPTX-Datei unter Verwendung der definierten Speicheroptionen.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX_image_resolution(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    save_options.image_resolution = 300

    document.save(outfile, save_options)
```

## Verwandte Konvertierungen

- [PDF in Word konvertieren](/pdf/de/python-net/convert-pdf-to-word/) für editierbare Dokumentausgabe anstelle von Folien.
- [PDF in Excel konvertieren](/pdf/de/python-net/convert-pdf-to-excel/) wenn die Quell-PDF umfangreiche tabellarische Geschäftsdaten enthält.
- [PDF in HTML konvertieren](/pdf/de/python-net/convert-pdf-to-html/) für browserbereite Veröffentlichungs-Workflows.