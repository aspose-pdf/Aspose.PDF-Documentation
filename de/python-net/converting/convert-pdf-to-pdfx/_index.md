---
title: PDF in PDF/A, PDF/E und PDF/X in Python konvertieren
linktitle: PDF in PDF/A, PDF/E und PDF/X konvertieren
type: docs
weight: 120
url: /de/python-net/convert-pdf-to-pdf_x/
lastmod: "2026-05-18"
description: Erfahren Sie, wie Sie PDF-Dateien in PDF/A, PDF/E und PDF/X in Python mit Aspose.PDF for Python via .NET für Archivierungs‑, Zugänglichkeits‑ und Druck‑Workflows konvertieren.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Wie man PDF in PDF/X-Formate konvertiert
Abstract: Der Artikel bietet eine umfassende Anleitung zur Konvertierung von PDF in die Formate PDF/A, PDF/E und PDF/X mithilfe von Aspose.PDF für Python.
---

**PDF-zu-PDF/x-Format bedeutet die Fähigkeit, PDF in zusätzliche Formate zu konvertieren, nämlich PDF/A, PDF/E und PDF/X.**

## PDF in PDF/A konvertieren

**Aspose.PDF for Python** ermöglicht es Ihnen, eine PDF-Datei in ein <abbr title="Portable Document Format / A">PDF/A</abbr> konforme PDF-Datei. Vorher muss die Datei validiert werden. Dieses Thema erklärt, wie.

{{% alert color="primary" %}}

Bitte beachten Sie, dass wir Adobe Preflight zur Validierung der PDF/A-Konformität verwenden. Alle Werkzeuge auf dem Markt haben ihre eigene „Darstellung“ der PDF/A-Konformität. Bitte prüfen Sie diesen Artikel zu PDF/A-Validierungstools zur Referenz. Wir haben Adobe-Produkte ausgewählt, um zu überprüfen, wie Aspose.PDF PDF-Dateien erzeugt, weil Adobe im Zentrum von allem steht, was mit PDF zu tun hat.

{{% /alert %}}

Konvertieren Sie die Datei mithilfe der Convert-Methode der Document-Klasse. Bevor Sie das PDF in eine PDF/A-konforme Datei konvertieren, validieren Sie das PDF mit der Validate-Methode. Das Validierungsergebnis wird in einer XML-Datei gespeichert und anschließend an die Convert-Methode übergeben. Sie können auch die Aktion für die Elemente festlegen, die nicht konvertiert werden können, indem Sie die ConvertErrorAction-Aufzählung verwenden.

{{% alert color="success" %}}
**Versuchen Sie, PDF online in PDF/A zu konvertieren**

Aspose.PDF for Python präsentiert Ihnen die Online-Anwendung ["PDF zu PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), wo Sie versuchen können, die Funktionalität und die Qualität, mit der es funktioniert, zu untersuchen.

[![Aspose.PDF Konvertierung PDF zu PDF/A mit App](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

Die Methode 'document.validate()' überprüft, ob eine PDF-Datei dem PDF/A-1B-Standard entspricht (eine ISO‑standardisierte Version von PDF, die für die Langzeitarchivierung entwickelt wurde). Die Validierungsergebnisse werden in einer Protokolldatei gespeichert.

### PDF in PDF/A-1B konvertieren

Der folgende Codeausschnitt zeigt, wie man PDF-Dateien in das PDF/A-1B-Format konvertiert:

1. Laden Sie das PDF-Dokument mit 'ap.Document'.
1. Rufen Sie die convert-Methode mit den folgenden Parametern auf:
    - Protokolldateipfad - speichert die Details des Konvertierungsprozesses und der Compliance‑Prüfungen.
    - Ziel-Format - 'ap.PdfFormat.PDF_A_1B' (Archivstandard).
    - Fehleraktion - 'ap.ConvertErrorAction.DELETE' — entfernt automatisch Elemente, die die Konformität verhindern.
1. Speichern Sie die konvertierte PDF/A‑konforme Datei im Ausgabepfad.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA(infile, outfile):
    """Convert PDF to PDF/A-1B format."""

    document = ap.Document(infile)
    document.convert(
        outfile.replace(".pdf", "-log.xml"),
        ap.PdfFormat.PDF_A_1B,
        ap.ConvertErrorAction.DELETE,
    )
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

### PDF in PDF 2.0 und PDF/A-4 konvertieren

Dieses Beispiel zeigt, wie man ein PDF-Dokument in neuere standardisierte Formate konvertiert: PDF 2.0 und PDF/A-4.
Beide Konvertierungen helfen, die Einhaltung moderner Spezifikationen und Archivierungsanforderungen sicherzustellen.

1. Laden Sie das Eingabedokument mithilfe von ap.Document.
1. Führen Sie die erste Konvertierung zu PDF 2.0 durch, indem Sie document.convert mit aufrufen:
    - Logdatei-Pfad für Konvertierungsdetails.
    - Zielformat - 'ap.PdfFormat.V_2_0'.
    - Fehleraktion - 'ap.ConvertErrorAction.DELETE' zum Entfernen nicht konformer Elemente.
1. Führen Sie eine zweite Konvertierung zu PDF/A-4 mit derselben Methode durch und stellen Sie sicher, dass die Datei ebenfalls den Archivierungsstandards entspricht.
1. Speichern Sie das resultierende Dokument im angegebenen Ausgabepfad.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA4(infile, outfile):
    logfile = outfile.replace(".pdf", "_log.xml")

    document = ap.Document(infile)
    document.convert(logfile, ap.PdfFormat.V_2_0, ap.ConvertErrorAction.DELETE)
    document.convert(logfile, ap.PdfFormat.PDF_A_4, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```

### PDF in PDF/A-3A mit eingebetteten Dateien konvertieren

Der nächste Codeabschnitt demonstriert, wie externe Dateien in ein PDF eingebettet und das PDF anschließend in das PDF/A-3A-Format konvertiert wird, das Anhänge unterstützt und für die langfristige Archivierung mit eingebettetem Inhalt geeignet ist.

1. Laden Sie das Eingabe-PDF mit 'ap.Document'.
1. Erstellen Sie ein 'FileSpecification'-Objekt, das auf die einzubindende Datei verweist (z. B. "aspose-logo.jpg") mit einer Beschreibung.
1. Fügen Sie die Dateispezifikation zur 'embedded_files'-Sammlung des PDFs hinzu.
1. Konvertieren Sie das Dokument zu PDF/A-3A mit 'document.convert', wobei Sie angeben:
    - Protokolldateipfad.
    - Zielformat - 'ap.PdfFormat.PDF_A_3A'.
    - Fehleraktion - 'ap.ConvertErrorAction.DELETE' zum Entfernen nicht konformer Elemente.
1. Speichern Sie das konvertierte PDF im Ausgabepfad.
1. Geben Sie eine Bestätigungsnachricht aus.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_with_attachment(infile, attachement_file, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")
    document = ap.Document(infile)

    fileSpecification = ap.FileSpecification(attachement_file, "Large Image file")
    document.embedded_files.add(fileSpecification)
    document.convert(
        logfile, ap.PdfFormat.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE
    )
    document.save(outfile)
```

### PDF in PDF/A-1B konvertieren mit Schriftart-Substitution

Diese Funktion konvertiert ein PDF in das PDF/A-1B-Format und behandelt fehlende Schriftarten, indem sie sie durch verfügbare ersetzt. Dadurch bleibt das konvertierte PDF visuell konsistent und entspricht den Archivierungsstandards.

1. Laden Sie das PDF mit 'ap.Document'.
1. Konvertieren Sie das PDF zu PDF/A-1B mit 'document.convert' und geben Sie Folgendes an:
    - Protokolldateipfad.
    - Zielformat - 'ap.PdfFormat.PDF_A_1B'.
    - Fehleraktion - 'ap.ConvertErrorAction.DELETE' zum Entfernen nicht konformer Elemente.
1. Speichern Sie das konvertierte PDF im Ausgabepfad.
1. Geben Sie eine Bestätigungsnachricht aus.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_replace_missing_fonts(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")
    try:
        ap.text.FontRepository.find_font("AgencyFB")

    except ap.FontNotFoundException:
        font_substitution = ap.text.SimpleFontSubstitution("AgencyFB", "Arial")
        ap.text.FontRepository.Substitutions.append(font_substitution)

    document = ap.Document(infile)
    document.convert(logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```

### PDF in PDF/A-1B mit automatischer Tagging konvertieren

Diese Funktion konvertiert ein PDF-Dokument in das PDF/A-1B-Format, wobei der Inhalt automatisch für Barrierefreiheit und strukturelle Konsistenz getaggt wird. Das automatische Tagging verbessert die Benutzerfreundlichkeit des Dokuments für Screenreader und gewährleistet eine korrekte semantische Struktur.

1. Laden Sie das PDF mit 'ap.Document'.
1. Erstelle 'PdfFormatConversionOptions' mit Angabe:
    - Protokolldateipfad.
    - Zielformat - 'ap.PdfFormat.PDF_A_1B'.
    - Fehleraktion - 'ap.ConvertErrorAction.DELETE' zum Entfernen nicht konformer Elemente.
1. Konfigurieren 'AutoTaggingSettings':
    - Aktivieren 'enable_auto_tagging = True'.
    - Setze 'heading_recognition_strategy = AUTO' um Überschriften automatisch zu erkennen.
1. Weisen Sie die Auto-Tagging-Einstellungen den Konvertierungsoptionen zu.
1. Konvertieren Sie das PDF mit 'document.convert(options)'.
1. Speichern Sie das konvertierte PDF im Ausgabepfad.
1. Geben Sie eine Bestätigungsnachricht aus.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_with_automatic_tagging(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE
    )

    auto_tagging_settings = ap.AutoTaggingSettings()
    auto_tagging_settings.enable_auto_tagging = True

    auto_tagging_settings.heading_recognition_strategy = (
        ap.HeadingRecognitionStrategy.AUTO
    )

    options.auto_tagging_settings = auto_tagging_settings
    document.convert(options)
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## PDF in PDF/E konvertieren

Dieses Code‑Snippet demonstriert, wie ein PDF‑Dokument in das PDF/E‑1‑Format konvertiert wird, das ein ISO‑Standard ist, der speziell für Ingenieur‑ und technische Dokumentation entwickelt wurde. Dieses Format bewahrt das präzise Layout, die Grafiken und Metadaten, die für ingenieurtechnische Arbeitsabläufe erforderlich sind.

1. Laden Sie das Quell-PDF mit 'ap.Document'.
1. Erstelle 'PdfFormatConversionOptions' mit Angabe:
    - Pfad der Protokolldatei zur Verfolgung von Konvertierungsproblemen.
    - Ziel-Format - 'ap.PdfFormat.PDF_E_1'.
    - Fehleraktion - 'ap.ConvertErrorAction.DELETE' zum Entfernen nicht konformer Elemente.
1. Konvertieren Sie das PDF mit 'document.convert(options)'.
1. Speichern Sie das konvertierte PDF am angegebenen Ausgabepfad.
1. Geben Sie eine Bestätigungsnachricht aus.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDF_E(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_E_1, ap.ConvertErrorAction.DELETE
    )

    document.convert(options)

    # Save PDF document
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## PDF in PDF/X konvertieren

Der nächste Codeabschnitt konvertiert ein PDF-Dokument in das PDF/X-4-Format, einen ISO-Standard, der häufig in der Druck- und Verlagsbranche verwendet wird. PDF/X-4 gewährleistet Farbgenauigkeit, erhält Transparenz und bettet ICC-Profile ein, um eine konsistente Ausgabe über verschiedene Geräte hinweg zu gewährleisten.

1. Laden Sie das Quell-PDF mit 'ap.Document'.
1. Erstelle 'PdfFormatConversionOptions' mit Angabe:
    - Protokolldateipfad.
    - Zielformat - 'ap.PdfFormat.PDF_X_4'.
    - Fehleraktion - 'ap.ConvertErrorAction.DELETE' zum Entfernen nicht konformer Elemente.
1. Stellen Sie die **ICC-Profildatei** für die Farbverwaltung über 'icc_profile_file_name' bereit.
1. Geben Sie einen **OutputIntent** mit einem Bedingungskennzeichen (z. B. „FOGRA39“) für Druckanforderungen an.
1. Konvertieren Sie das PDF mit 'document.convert()'.
1. Speichern Sie das konvertierte PDF am angegebenen Ausgabepfad.
1. Geben Sie eine Bestätigungsnachricht aus.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDF_X(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_X_4, ap.ConvertErrorAction.DELETE
    )

    # Provide the name of the external ICC profile file (optional)
    options.icc_profile_file_name = path.join(
        path.dirname(infile), "ISOcoated_v2_eci.icc"
    )
    # Provide an output condition identifier and other necessary OutputIntent properties (optional)
    options.output_intent = ap.OutputIntent("FOGRA39")

    document.convert(options)

    # Save PDF document
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Verwandte Konvertierungen

- [PDF in Word konvertieren](/pdf/de/python-net/convert-pdf-to-word/) für editierbare Inhalts-Workflows nach der Validierung von Standards.
- [PDF in HTML konvertieren](/pdf/de/python-net/convert-pdf-to-html/) wenn Ihre Zielausgabe web‑bereit statt standardbasierter PDF ist.
