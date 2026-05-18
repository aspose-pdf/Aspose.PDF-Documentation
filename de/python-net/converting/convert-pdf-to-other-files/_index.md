---
title: PDF in EPUB, Text, XPS und mehr in Python konvertieren
linktitle: PDF in andere Formate konvertieren
type: docs
weight: 90
url: /de/python-net/convert-pdf-to-other-files/
lastmod: "2026-05-18"
description: Erfahren Sie, wie Sie PDF-Dateien in Python mit Aspose.PDF for Python via .NET zu EPUB, LaTeX, Markdown, Text, XPS und MobiXML konvertieren.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Wie man PDF in andere Formate in Python konvertiert
Abstract: Der Artikel bietet eine umfassende Anleitung zum Konvertieren von PDF-Dateien in verschiedene Formate mit Aspose.PDF for Python. Er behandelt die Konvertierung von PDFs in die Formate EPUB, LaTeX/TeX, Text, XPS und XML. Jeder Abschnitt beginnt mit einer Einladung, die von Aspose bereitgestellten Online-Anwendungen zum Konvertieren von PDFs in das jeweilige Format auszuprobieren, wobei die Benutzerfreundlichkeit und Qualität dieser Werkzeuge hervorgehoben wird.
---

## PDF in EPUB konvertieren

{{% alert color="success" %}}
**Versuchen Sie, PDF online in EPUB zu konvertieren**

Aspose.PDF for Python präsentiert Ihnen die Online-Anwendung ["PDF zu EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), wo Sie versuchen können, die Funktionalität und die Qualität, mit der es funktioniert, zu untersuchen.

[![Aspose.PDF Konvertierung PDF zu EPUB mit App](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> ist ein freier und offener E-Book-Standard des International Digital Publishing Forum (IDPF). Dateien haben die Erweiterung .epub.
EPUB ist für fließbaren Inhalt konzipiert, was bedeutet, dass ein EPUB‑Reader den Text für ein bestimmtes Anzeigegerät optimieren kann. EPUB unterstützt auch feste Layout‑Inhalte. Das Format ist als ein einheitliches Format gedacht, das Verlage und Konvertierungsunternehmen intern sowie für Vertrieb und Verkauf nutzen können. Es ersetzt den Open‑eBook‑Standard.

Aspose.PDF for Python unterstützt auch die Funktion, PDF‑Dokumente in das EPUB‑Format zu konvertieren. Aspose.PDF for Python verfügt über eine Klasse namens 'EpubSaveOptions', die als zweites Argument verwendet werden kann, um [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) Methode, um eine EPUB-Datei zu erzeugen.
Bitte versuchen Sie, das folgende Code‑Snippet zu verwenden, um diese Anforderung mit Python zu erfüllen.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_EPUB(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.EpubSaveOptions()
    save_options.content_recognition_mode = ap.EpubSaveOptions.RecognitionMode.FLOW
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Verwandte Konvertierungen

- [PDF in Word konvertieren](/pdf/de/python-net/convert-pdf-to-word/) für editierbare Office-Dokumentausgabe.
- [PDF in HTML konvertieren](/pdf/de/python-net/convert-pdf-to-html/) für browserorientierte Ausgabe.
- [PDF in PDF/A, PDF/E und PDF/X konvertieren](/pdf/de/python-net/convert-pdf-to-pdf_x/) für archivierungs- und standardkonforme Konvertierungs‑Workflows.

## PDF in LaTeX/TeX konvertieren

**Aspose.PDF for Python via .NET** unterstützt die Konvertierung von PDF nach LaTeX/TeX.
Das LaTeX-Dateiformat ist ein Textdateiformat mit spezieller Auszeichnung und wird in TeX-basierten Dokumentenerstellungssystemen für hochwertige Satzsetzung verwendet.

{{% alert color="success" %}}
**Versuchen Sie, PDF online in LaTeX/TeX zu konvertieren**

Aspose.PDF for Python präsentiert Ihnen die Online-Anwendung [PDF zu LaTeX](https://products.aspose.app/pdf/conversion/pdf-to-tex), wo Sie versuchen können, die Funktionalität und die Qualität, mit der es funktioniert, zu untersuchen.

[![Aspose.PDF-Konvertierung PDF zu LaTeX/TeX mit App](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Um PDF-Dateien in TeX zu konvertieren, verfügt Aspose.PDF über die Klasse [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) die die Eigenschaft OutDirectoryPath zum Speichern temporärer Bilder während des Konvertierungsprozesses bereitstellt.

Das folgende Code‑Snippet zeigt den Vorgang, PDF‑Dateien mit Python in das TEX‑Format zu konvertieren.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_TeX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.LaTeXSaveOptions()
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## PDF in Text umwandeln

**Aspose.PDF for Python** unterstützt die Konvertierung des gesamten PDF-Dokuments und einzelner Seiten in eine Textdatei. Sie können ein PDF-Dokument mit der Klasse 'TextDevice' in eine TXT-Datei konvertieren. Das folgende Code‑Snippet erklärt, wie man die Texte von allen Seiten extrahiert.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_TXT(infile, outfile):
    document = ap.Document(infile)
    device = ap.devices.TextDevice()
    device.process(document.pages[1], outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Versuchen Sie, PDF in Text online zu konvertieren**

Aspose.PDF for Python präsentiert Ihnen die Online-Anwendung ["PDF zu Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt), wo Sie versuchen können, die Funktionalität und die Qualität, mit der es funktioniert, zu untersuchen.

[![Aspose.PDF Konvertierung PDF zu Text mit App](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## PDF in XPS konvertieren

**Aspose.PDF for Python** bietet die Möglichkeit, PDF‑Dateien in das XPS‑Format zu konvertieren. Versuchen wir, den vorgestellten Code‑Abschnitt zu verwenden, um PDF‑Dateien mit Python in das XPS‑Format zu konvertieren.

{{% alert color="success" %}}
**Versuchen Sie, PDF online in XPS zu konvertieren**

Aspose.PDF for Python präsentiert Ihnen die Online-Anwendung ["PDF zu XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), wo Sie versuchen können, die Funktionalität und die Qualität, mit der es funktioniert, zu untersuchen.

[![Aspose.PDF Konvertierung PDF zu XPS mit App](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

Der XPS-Dateityp ist hauptsächlich mit der XML Paper Specification von Microsoft Corporation verbunden. Die XML Paper Specification (XPS), früher unter dem Codenamen Metro und das Next Generation Print Path (NGPP)-Marketingkonzept einschließend, ist Microsofts Initiative, die Dokumentenerstellung und -anzeige in das Windows-Betriebssystem zu integrieren.

Um PDF-Dateien in XPS zu konvertieren, verfügt Aspose.PDF über die Klasse [XpsSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/) die als zweites Argument an die [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) Methode zum Erzeugen der XPS-Datei.

Das folgende Code‑Snippet zeigt den Vorgang der Konvertierung einer PDF‑Datei in das XPS‑Format.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_XPS(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.XpsSaveOptions()
    save_options.use_new_imaging_engine = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## PDF in MD konvertieren

Aspose.PDF hat die Klasse 'MarkdownSaveOptions()', die ein PDF-Dokument in das Markdown (MD)-Format konvertiert und dabei Bilder und Ressourcen beibehält.

1. Laden Sie das Quell-PDF mit 'ap.Document'.
1. Erstellen Sie eine Instanz von 'MarkdownSaveOptions'.
1. Setzen Sie 'resources_directory_name' auf 'images' – extrahierte Bilder werden in diesem Ordner gespeichert.
1. Speichern Sie das konvertierte Markdown-Dokument mit den konfigurierten Optionen.
1. Geben Sie nach der Konvertierung eine Bestätigungsnachricht aus.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_MD(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.MarkdownSaveOptions()
    save_options.resources_directory_name = "images"
    save_options.use_image_html_tag = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

Eine Markdown-Datei mit Text und verlinkten Bildern, die im angegebenen Bilderordner gespeichert sind.

## PDF in MobiXML konvertieren

Diese Methode konvertiert ein PDF-Dokument in das MOBI (MobiXML)-Format, das häufig für eBooks auf Kindle-Geräten verwendet wird.

1. Laden Sie das Quell-PDF-Dokument mit 'ap.Document'.
1. Speichern Sie das Dokument im Format 'ap.SaveFormat.MOBI_XML'.
1. Geben Sie eine Bestätigungsnachricht aus, sobald die Konvertierung abgeschlossen ist.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_MobiXML(infile, outfile):
    document = ap.Document(infile)
    document.save(outfile, ap.SaveFormat.MOBI_XML)

    print(infile + " converted into " + outfile)
```
