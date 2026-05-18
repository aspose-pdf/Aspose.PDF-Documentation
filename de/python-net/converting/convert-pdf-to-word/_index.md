---
title: PDF nach Word in Python konvertieren
linktitle: PDF in Word konvertieren
type: docs
weight: 10
url: /de/python-net/convert-pdf-to-word/
lastmod: "2026-05-18"
description: Erfahren Sie, wie Sie PDF-Dateien in Python mit Aspose.PDF for Python via .NET in DOC und DOCX konvertieren, um die Dokumentenbearbeitung und Wiederverwendung zu erleichtern.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Wie man PDF nach Word in Python konvertiert
Abstract: Dieser Artikel bietet eine umfassende Anleitung zur Konvertierung von PDF-Dateien in Microsoft-Word-Formate (DOC und DOCX) mit Python, wobei speziell die Aspose.PDF-Bibliothek verwendet wird. Er beschreibt die Vorteile der Umwandlung von PDFs in editierbare Word-Dokumente, die eine einfachere Inhaltsbearbeitung wie Text, Tabellen und Bilder ermöglichen. Der Artikel erläutert den Vorgang der Konvertierung von PDF zu DOC (Word 97‑2003‑Format) und DOCX, einschließlich Code‑Snippets, die diese Konvertierungen mit Python demonstrieren. Der Prozess beinhaltet das Erstellen eines `Document`‑Objekts aus dem PDF und das Speichern in das gewünschte Format mithilfe der `save()`‑Methode und der `SaveFormat`‑Aufzählung. Zusätzlich wird die Klasse `DocSaveOptions` vorgestellt, die weitere Anpassungen des Konvertierungsprozesses ermöglicht, z. B. die Angabe von Erkennungsmodi. Der Artikel hebt außerdem die von Aspose.PDF bereitgestellten Online‑Anwendungen hervor, um die Konvertierungsqualität und -funktionalität zu testen. Der Inhalt enthält einen strukturierten Überblick und Links zu den jeweiligen Abschnitten für jedes Format.
---

## PDF in DOC konvertieren

Eine der beliebtesten Funktionen ist die PDF-zu-Microsoft-Word-DOC-Konvertierung, die das Inhaltsmanagement erleichtert. **Aspose.PDF for Python via .NET** ermöglicht es Ihnen, PDF-Dateien nicht nur in DOC, sondern auch in das DOCX-Format zu konvertieren, einfach und effizient.

Verwenden Sie die Word‑Konvertierung, wenn Sie Text überarbeiten, Inhalte in Büroabläufen wiederverwenden oder PDF‑Inhalte in bearbeitbare DOC‑ oder DOCX‑Dokumente übertragen müssen.

Der [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) Die Klasse bietet zahlreiche Eigenschaften, die den Vorgang der Konvertierung von PDF‑Dateien in das DOC‑Format verbessern. Unter diesen Eigenschaften ermöglicht Mode die Angabe des Erkennungsmodus für PDF‑Inhalte. Für diese Eigenschaft können Sie jeden Wert aus der Aufzählung RecognitionMode angeben. Jeder dieser Werte hat spezifische Vorteile und Einschränkungen:

Schritte: PDF in DOC mit Python konvertieren

1. Laden Sie das PDF in ein 'ap.Document'-Objekt.
1. Erstellen Sie eine 'DocSaveOptions'-Instanz.
1. Setzen Sie die format‑Eigenschaft auf 'DocFormat.DOC', um sicherzustellen, dass die Ausgabe im .doc-Format (älteres Word-Format) erfolgt.
1. Speichern Sie das PDF als Word-Dokument unter Verwendung der angegebenen Speicheroptionen.
1. Geben Sie eine Bestätigungsnachricht aus.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOC(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Versuchen Sie, PDF online in DOC zu konvertieren**

Aspose.PDF for Python präsentiert Ihnen die Online-Anwendung ["PDF zu DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), wo Sie versuchen können, die Funktionalität und die Qualität, mit der es funktioniert, zu untersuchen.

[![PDF in DOC konvertieren](/pdf/de/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## PDF in DOCX konvertieren

Aspose.PDF for Python API ermöglicht das Lesen und Konvertieren von PDF-Dokumenten in DOCX mithilfe von Python über .NET. DOCX ist ein bekanntes Format für Microsoft-Word-Dokumente, dessen Struktur von rein binär zu einer Kombination aus XML- und Binärdateien geändert wurde. Docx-Dateien können mit Word 2007 und späteren Versionen geöffnet werden, jedoch nicht mit den vorherigen Versionen von MS Word, die DOC-Dateierweiterungen unterstützen.

Das folgende Python-Code-Snippet zeigt den Vorgang der Konvertierung einer PDF-Datei in das DOCX-Format.

Schritte: PDF in DOCX mit Python konvertieren

1. Laden Sie das Quell-PDF mit 'ap.Document'.
1. Erstellen Sie eine Instanz von 'DocSaveOptions'.
1. Setzen Sie die Format‑Eigenschaft auf 'DocFormat.DOC_X', um eine .docx‑Datei (modernes Word‑Format) zu erzeugen.
1. Speichern Sie das PDF als DOCX‑Datei mit den konfigurierten Speicheroptionen.
1. Geben Sie nach der Konvertierung eine Bestätigungsnachricht aus.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOCX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    document.save(outfile, save_options)
```

## PDF in DOCX mit erweiterter Layout-Erkennung konvertieren

Konvertieren Sie ein PDF-Dokument mithilfe von Python und Aspose.PDF in eine DOCX‑(Word‑)Datei mit erweiterten Erkennungseinstellungen. Es verwendet den erweiterten Flow‑Modus, um die Dokumentstruktur zu erhalten, wodurch die Ausgabe besser editierbar und dem ursprünglichen Layout näher kommt.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOCX_advanced(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    save_options.mode = ap.DocSaveOptions.RecognitionMode.ENHANCED_FLOW
    document.save(outfile, save_options)
```

Der [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) Klasse hat eine Eigenschaft namens Format, die die Möglichkeit bietet, das Format des resultierenden Dokuments anzugeben, also DOC oder DOCX. Um eine PDF-Datei in das DOCX-Format zu konvertieren, übergeben Sie bitte den Wert Docx aus der Aufzählung DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**Versuchen Sie, PDF online in DOCX zu konvertieren**

Aspose.PDF for Python präsentiert Ihnen die Online-Anwendung ["PDF zu Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), wo Sie versuchen können, die Funktionalität und die Qualität, mit der es funktioniert, zu untersuchen.

[![Aspose.PDF Konvertierung PDF zu Word App](/pdf/de/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Verwandte Konvertierungen

- [PDF in Excel konvertieren](/pdf/de/python-net/convert-pdf-to-excel/) für tabellenkalkulationsorientierte Exporte.
- [PDF in PowerPoint konvertieren](/pdf/de/python-net/convert-pdf-to-powerpoint/) wenn Sie Präsentationsfolien anstelle von Textverarbeitungs-Ausgabe benötigen.
- [PDF in HTML konvertieren](/pdf/de/python-net/convert-pdf-to-html/) für Web-Publishing und browserbasierte Content-Workflows.
