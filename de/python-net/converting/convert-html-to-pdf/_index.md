---
title: HTML in PDF in Python konvertieren
linktitle: HTML in PDF-Datei konvertieren
type: docs
weight: 40
url: /de/python-net/convert-html-to-pdf/
lastmod: "2026-05-18"
description: Erfahren Sie, wie Sie HTML und MHTML in PDF in Python mit Aspose.PDF for Python via .NET konvertieren, einschließlich CSS-Medieneinstellungen, eingebetteter Schriften und Tagged PDF-Ausgabe.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Wie man HTML in Python mit Aspose.PDF in PDF konvertiert.
Abstract: Dieser Artikel erklärt, wie man HTML- und MHTML-Dateien mithilfe von Aspose.PDF for Python via .NET in PDF konvertiert. Er behandelt den grundlegenden HTML-zu-PDF‑Workflow und zeigt, wie die Darstellung mit Medientypen, der Priorität von CSS‑Seitenregeln, eingebetteten Schriften, einseitiger Ausgabe und der Erzeugung einer logischen Struktur für barrierefreie, getaggte PDFs gesteuert werden kann.
---

## Python HTML zu PDF-Konvertierung

**Aspose.PDF for Python via .NET** ermöglicht es Ihnen, vorhandene HTML-Dokumente in PDF zu konvertieren, mit flexiblen Rendering-Optionen. Sie können die Ausgabe feinabstimmen, um sie an Ihr Layout, Styling, Ihre Barrierefreiheit und Archivierungsanforderungen anzupassen.

## HTML in PDF konvertieren

Das folgende Python-Beispiel zeigt den grundlegenden Arbeitsablauf zum Konvertieren eines HTML-Dokuments in PDF.

1. Erstellen Sie eine Instanz von [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) Klasse.
1. Initialisiere ein [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Objekt mit der Quell-HTML-Datei.
1. Speichern Sie das Ausgabedokument als PDF, indem Sie aufrufen `document.save()`.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.page_layout_option = ap.HtmlPageLayoutOption.SCALE_TO_PAGE_WIDTH
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Verwandte Konvertierungen

- [PDF in HTML konvertieren](/pdf/de/python-net/convert-pdf-to-html/) wenn Sie webbereite Ausgabe aus vorhandenen PDF-Dateien benötigen.
- [Andere Dateiformate in PDF konvertieren](/pdf/de/python-net/convert-other-files-to-pdf/) für EPUB-, XPS-, Text- und PostScript-Konvertierungs-Workflows.
- [Bilder in PDF konvertieren](/pdf/de/python-net/convert-images-format-to-pdf/) wenn Ihr Quellinhalt bildbasiert ist anstelle von HTML-Markup.

{{% alert color="success" %}}
**Versuchen Sie, HTML online in PDF zu konvertieren**

Aspose präsentiert die Online-Anwendung ["HTML zu PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), wo Sie die Konvertierungsqualität und die Ausgabe testen können.

[![Aspose.PDF Konvertierung HTML zu PDF mit App](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## HTML in PDF mit Medientyp konvertieren

Dieses Beispiel zeigt, wie man eine HTML-Datei mithilfe bestimmter Rendering-Optionen in PDF konvertiert.

1. Erstellen Sie eine Instanz von [HtmlLoadOptions()](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) Klasse.
1. Setzen `html_media_type` um CSS-Regeln anzuwenden, die für Bildschirm- oder Drucklayouts vorgesehen sind, wie zum Beispiel `HtmlMediaType.SCREEN` oder `HtmlMediaType.PRINT`.
1. Lade das HTML in ein `ap.Document` mit den Ladeoptionen.
1. Speichern Sie das Dokument als PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.html_media_type = ap.HtmlMediaType.SCREEN
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Priorisieren Sie das CSS `@page` Regel während der HTML-zu-PDF-Konvertierung

Einige Dokumente verwenden [der `@page` Regel](https://developer.mozilla.org/en-US/docs/Web/CSS/@page) für das Seitenlayout. Wenn diese Stile mit anderen Einstellungen in Konflikt stehen, können Sie die Priorität steuern mit `is_priority_css_page_rule`.

1. Erstellen Sie eine Instanz von [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) Klasse.
1. Setzen `is_priority_css_page_rule = False` anderen Stilen Vorrang geben `@page` Regeln.
1. Lade das HTML in ein `ap.Document` mit den konfigurierten Optionen.
1. Speichern Sie das Dokument als PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
# load_options.is_priority_css_page_rule = False
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## HTML in PDF mit eingebetteten Schriftarten konvertieren

Dieses Beispiel zeigt, wie man eine HTML-Datei in PDF konvertiert, während Schriftarten eingebettet werden. Wenn Sie benötigen, dass das ausgegebene PDF die ursprüngliche Typografie beibehält, setzen Sie `is_embed_fonts` zu `True`.

1. Erstellen `HtmlLoadOptions()` um die HTML-zu-PDF-Konvertierung zu konfigurieren.
1. Setzen `is_embed_fonts = True` die in HTML verwendeten Schriftarten direkt in das PDF einzubetten.
1. Lade das HTML in ein `ap.Document` mit diesen Optionen.
1. Speichern Sie das Dokument als PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.is_embed_fonts = True
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## HTML-Inhalt auf einer einzigen PDF-Seite rendern

Dieses Beispiel demonstriert, wie man eine HTML-Datei in ein einseitiges PDF mit Aspose.PDF for Python via .NET konvertiert. Verwenden Sie das `is_render_to_single_page` Eigenschaft, wenn Sie den gesamten HTML-Inhalt auf einer durchgehenden Seite rendern möchten.

1. Erstelle eine Instanz von `HtmlLoadOptions()` den Konvertierungsprozess zu konfigurieren.
1. Aktivieren `is_render_to_single_page` um den vollständigen HTML-Inhalt auf einer Seite darzustellen
1. Laden Sie das Dokument mit den konfigurierten Optionen in ein `ap.Document`.
1. Speichern Sie das Ergebnis als PDF-Datei.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

options = ap.HtmlLoadOptions()
options.is_render_to_single_page = True

doc = ap.Document(path_infile, options)
doc.save(path_outfile)
```

## Erstelle logische Struktur aus HTML-Tags

Die logische Struktur, auch als Tagged PDF bezeichnet, bewahrt die semantische Hierarchie des ursprünglichen HTML, wie Überschriften, Absätze und Listen. Dadurch wird das resultierende PDF zugänglicher, durchsuchbarer und für strukturierte Dokumenten-Workflows geeignet.

Durch das Aktivieren der logischen Struktur während der Konvertierung wird das HTML-DOM in einen PDF-Tag-Baum abgebildet, anstatt nur als visueller Inhalt gerendert zu werden.

Um die Barrierefreiheitsanforderungen zu erfüllen, sollte ein PDF logische Strukturelemente enthalten, die die Lesereihenfolge definieren, alternativen Text für Screenreader bereitstellen und die Hierarchie des Inhalts bewahren.

> Die Qualität der logischen Struktur im Ausgabe‑PDF hängt direkt von der Qualität des ursprünglichen HTML‑Markups ab. Schlecht strukturierter oder ungültiger HTML‑Code kann zu unvollständiger oder ungenauer Markierung im konvertierten PDF führen.

1. Erstellen Sie eine HtmlLoadOptions-Instanz, um zu steuern, wie das HTML konvertiert wird.
1. Aktivieren Sie das semantische Tagging, damit das PDF strukturierte Elemente enthält.
1. Öffnen Sie die HTML-Datei mit den konfigurierten Optionen.
1. Speichern Sie das strukturierte PDF.

```python
import aspose.pdf as ap

# Path to the source HTML
input_html_path = "input.html"
# Path for the Logical Structure PDF
output_pdf_path = "output_logical_structure.pdf"
# Initialize HtmlLoadOptions
options = ap.HtmlLoadOptions()
# Convert HTML markup to PDF logical structure elements
options.create_logical_structure = True
# Open PDF document
with ap.Document(input_html_path, options) as document:
    # Save PDF document
    document.save(output_pdf_path)
```

## MHTML in PDF konvertieren

Dieses Beispiel zeigt, wie Sie eine MHT- oder MHTML-Datei mit Aspose.PDF for Python via .NET in ein PDF-Dokument mit bestimmten Seitenabmessungen konvertieren.

1. Erstelle eine Instanz von `ap.MhtLoadOptions()` um die Verarbeitung von MHTML-Dateien zu konfigurieren.
1. Legen Sie verschiedene Parameter fest, beispielsweise die Seitengröße.
1. Initialisieren Sie das Dokument mit der Eingabedatei und den konfigurierten Ladeoptionen.
1. Speichern Sie das resultierende Dokument als PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
load_options = ap.MhtLoadOptions()
load_options.page_info.width = 842
load_options.page_info.height = 1191
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```
