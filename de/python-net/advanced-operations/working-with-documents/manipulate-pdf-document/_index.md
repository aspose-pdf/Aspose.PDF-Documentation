---
title: PDF-Dokumente in Python manipulieren
linktitle: PDF-Dokument manipulieren
type: docs
weight: 20
url: /de/python-net/manipulate-pdf-document/
description: Erfahren Sie, wie Sie PDF-Dokumente in Python validieren, strukturieren und ändern, einschließlich der TOC-Verwaltung und PDF/A‑Prüfungen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Anleitung zur Manipulation von PDF-Dokumenten mit Python
Abstract: Dieser Artikel bietet eine umfassende Anleitung zur Manipulation von PDF-Dokumenten mit Python, speziell mit der Aspose.PDF-Bibliothek. Er behandelt mehrere Funktionalitäten, darunter die Validierung von PDF-Dokumenten auf PDF/A-1a- und PDF/A-1b-Konformität mithilfe der `validate`‑Methode der `Document`‑Klasse. Er erläutert zudem, wie man ein Table of Contents (TOC) in PDF-Dateien hinzufügt, anpasst und verwaltet, zum Beispiel durch das Festlegen verschiedener TabLeaderTypes, das Ausblenden von Seitenzahlen und das Anpassen der Seitennummerierung mit einem Präfix. Zusätzlich erklärt der Artikel, wie man ein Ablaufdatum für ein PDF-Dokument festlegt, indem man JavaScript für Zugriffsbeschränkungen einbettet, und wie man ausfüllbare Formulare in einem PDF flacht, um sie nicht bearbeitbar zu machen. Jeder Abschnitt wird von Code‑Snippets begleitet, die die Implementierung dieser Funktionen mit Aspose.PDF in Python demonstrieren.
---

Diese Seite ist nützlich, wenn Sie PDF-Konformität validieren, ein Inhaltsverzeichnis erstellen oder anpassen, das Ablaufverhalten von Dokumenten festlegen oder ausfüllbare PDFs in Python-Workflows flachlegen müssen.

## PDF-Dokument in Python manipulieren

## PDF-Dokument auf PDF‑A‑Standard (A‑1A und A‑1B) validieren

Um ein PDF-Dokument auf PDF/A-1a- oder PDF/A-1b-Kompatibilität zu prüfen, verwenden Sie die [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) Klasse [validieren](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) Methode. Diese Methode ermöglicht es Ihnen, den Namen der Datei anzugeben, in der das Ergebnis gespeichert werden soll, sowie den erforderlichen Validierungstyp der PdfFormat‑Aufzählung: PDF_A_1A oder PDF_A_1B.

Das folgende Code‑Snippet zeigt Ihnen, wie Sie ein PDF‑Dokument für PDF/A‑1A validieren.

```python
import sys
from os import path
import aspose.pdf as ap


def validate_pdfa_standard_a1a(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.validate(output_pdf, ap.PdfFormat.PDF_A_1A)
```

Der folgende Codeausschnitt zeigt Ihnen, wie Sie ein PDF-Dokument für PDF/A-1b validieren.

```python
import sys
from os import path
import aspose.pdf as ap


def validate_pdfa_standard_a1b(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.validate(output_pdf, ap.PdfFormat.PDF_A_1B)
```

## Arbeiten mit TOC

### TOC zu vorhandenem PDF hinzufügen

TOC in PDF steht für "Inhaltsverzeichnis." Es ist eine Funktion, die es Benutzern ermöglicht, schnell durch ein Dokument zu navigieren, indem sie einen Überblick über dessen Abschnitte und Überschriften bietet. 

Um ein TOC zu einer bestehenden PDF-Datei hinzuzufügen, verwenden Sie die Heading-Klasse in [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) Namespace. Der [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) namespace kann sowohl neue PDF-Dateien erstellen als auch vorhandene PDF-Dateien manipulieren. Um einem bestehenden PDF ein TOC hinzuzufügen, verwenden Sie den Aspose.Pdf-namespace. Der folgende Codeabschnitt zeigt, wie man mithilfe von Python via .NET ein Inhaltsverzeichnis in einer bestehenden PDF-Datei erstellt.

```python
import sys
from os import path
import aspose.pdf as ap


def add_table_of_contents(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.insert(1)
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_page.toc_info = toc_info

    titles = ["First page", "Second page"]
    for index, title_text in enumerate(titles[:2]):
        heading = ap.Heading(1)
        segment = ap.text.TextSegment(title_text)
        heading.toc_page = toc_page
        heading.segments.append(segment)
        destination_page = document.pages[index + 2]
        heading.destination_page = destination_page
        heading.top = destination_page.rect.height
        toc_page.paragraphs.add(heading)

    document.save(output_pdf)
```

### Legen Sie unterschiedliche TabLeaderType für verschiedene TOC-Ebenen fest

Aspose.PDF for Python ermöglicht ebenfalls das Festlegen unterschiedlicher TabLeaderType für verschiedene TOC‑Ebenen. Sie müssen festlegen [line_dash](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) Eigentum von [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/).

```python
import sys
from os import path
import aspose.pdf as ap


def set_toc_levels(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.add()
    toc_info = ap.TocInfo()
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 30
    toc_info.title = title
    toc_page.toc_info = toc_info

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    toc_info.format_array[1].margin.left = 10
    toc_info.format_array[1].margin.right = 30
    toc_info.format_array[1].line_dash = 3
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].margin.left = 20
    toc_info.format_array[2].margin.right = 30
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].line_dash = ap.text.TabLeaderType.SOLID
    toc_info.format_array[3].margin.left = 30
    toc_info.format_array[3].margin.right = 30
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    page = document.pages.add()
    for level in range(1, 5):
        heading = ap.Heading(level)
        heading.is_auto_sequence = True
        heading.toc_page = toc_page
        heading.text_state.font = ap.text.FontRepository.find_font("Arial")
        segment = ap.text.TextSegment(f"Sample Heading{level}")
        heading.segments.append(segment)
        heading.is_in_list = True
        page.paragraphs.add(heading)

    document.save(output_pdf)
```

### Seitenzahlen im Inhaltsverzeichnis ausblenden

Falls Sie keine Seitenzahlen zusammen mit den Überschriften im TOC anzeigen möchten, können Sie [ist_seitenzahlen_anzeigen](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) Eigentum von [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) Klasse als falsch. Bitte prüfen Sie den folgenden Codeausschnitt, um Seitenzahlen im Inhaltsverzeichnis zu verbergen:

```python
import sys
from os import path
import aspose.pdf as ap


def hide_page_numbers_in_toc(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_info.is_show_page_numbers = False
    toc_page.toc_info = toc_info

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    page = document.pages.add()
    for level in range(1, 2):
        heading = ap.Heading(level)
        heading.toc_page = toc_page
        heading.is_auto_sequence = True
        heading.is_in_list = True
        segment = ap.text.TextSegment(f"this is heading of level {level}")
        heading.segments.append(segment)
        page.paragraphs.add(heading)

    document.save(output_pdf)
```

### Seitenzahlen beim Hinzufügen des Inhaltsverzeichnisses anpassen

Es ist üblich, die Seitennummerierung im TOC beim Hinzufügen eines TOC in einem PDF-Dokument anzupassen. Beispielsweise können wir ein Präfix vor der Seitennummer hinzufügen, wie P1, P2, P3 usw. In einem solchen Fall bietet Aspose.PDF for Python [seitenzahlen_präfix](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) Eigentum von [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) Klasse, die verwendet werden kann, um Seitenzahlen anzupassen, wie im folgenden Codebeispiel gezeigt.

```python
import sys
from os import path
import aspose.pdf as ap


def customize_page_numbers_in_toc(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.insert(1)
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info

    for index, page in enumerate(document.pages, start=1):
        heading = ap.Heading(1)
        heading.toc_page = toc_page
        heading.destination_page = page
        heading.top = page.rect.height
        segment = ap.text.TextSegment(f"Page {index}")
        heading.segments.append(segment)
        toc_page.paragraphs.add(heading)

    document.save(output_pdf)
```

## Wie man das Ablaufdatum eines PDFs festlegt

Wir wenden Zugriffsberechtigungen auf PDF-Dateien an, damit eine bestimmte Benutzergruppe auf bestimmte Funktionen/Objekte von PDF-Dokumenten zugreifen kann. Um den Zugriff auf die PDF-Datei zu beschränken, verwenden wir in der Regel Verschlüsselung und können die Anforderung haben, ein Ablaufdatum für die PDF-Datei festzulegen, sodass der Benutzer, der das Dokument accessing/viewing aufruft, eine gültige Meldung zum PDF-Datei-Ablauf erhält.

```python
import sys
from os import path
import aspose.pdf as ap


def set_pdf_expiry_date(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.pages.add()
    document.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
    script = ap.annotations.JavascriptAction(
        "var year=2017;"
        "var month=5;"
        "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        "expiry = new Date(year, month);"
        "if (today.getTime() > expiry.getTime())"
        "app.alert('The file is expired. You need a new one.');"
    )
    document.open_action = script
    document.save(output_pdf)
```

## Ausfüllbares PDF in Python flachlegen

PDF-Dokumente enthalten häufig Formulare mit interaktiven ausfüllbaren Widgets wie Optionsschaltern, Kontrollkästchen, Textfeldern, Listen usw. Um sie für verschiedene Anwendungszwecke nicht editierbar zu machen, müssen wir die PDF-Datei flachlegen.
Aspose.PDF bietet die Funktion, Ihr PDF in Python mit nur wenigen Codezeilen zu flachzulegen:

```python
import sys
from os import path
import aspose.pdf as ap


def flatten_fillable_pdf(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    if document.form and document.form.fields:
        for field in document.form.fields:
            field.flatten()
    document.save(output_pdf)
```

## Verwandte Dokumentthemen

- [Arbeiten mit PDF-Dokumenten in Python](/pdf/de/python-net/working-with-documents/)
- [PDF-Dokumente in Python formatieren](/pdf/de/python-net/formatting-pdf-document/)
- [Erstelle PDF-Dateien in Python](/pdf/de/python-net/create-pdf-document/)
- [PDF‑Dateien in Python optimieren](/pdf/de/python-net/optimize-pdf/)
