---
title: Tagged PDF in Python erstellen
linktitle: Tagged PDF erstellen
type: docs
weight: 10
url: /de/python-net/create-tagged-pdf/
description: Erfahren Sie, wie Sie in Python mit Aspose.PDF for Python via .NET tagge PDF-Dokumente erstellen, einschließlich PDF/UA-Strukturelemente, barrierefreie Formulare, TOC-Seiten und automatisches Tagging.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Ein Tagged PDF zu erstellen bedeutet, bestimmte Elemente zum Dokument hinzuzufügen (oder zu erzeugen), die es ermöglichen, das Dokument gemäß den PDF/UA-Anforderungen zu validieren. Diese Elemente werden häufig Struktur‑Elemente genannt.

## Erstellung von Tagged PDF (Einfaches Szenario)

Um Strukturelemente in einem Tagged PDF Document zu erstellen, bietet Aspose.PDF Methoden zum Erstellen von Strukturelementen mithilfe von [ITaggedContent](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/) Schnittstelle. Dieses Beispiel erstellt ein Tagged PDF‑Dokument — ein PDF mit semantischer Struktur, das es zugänglicher macht und konform mit Standards wie PDF/UA ist.
Das folgende Code‑Snippet zeigt, wie man ein Tagged PDF erstellt, das 2 Elemente enthält: Header und Absatz.

```python
import aspose.pdf as ap
import sys
from os import path

def create_tagged_pdf_document_simple(outfile):

    # Create PDF Document
    with ap.Document() as document:
        # Get Content for working with TaggedPdf
        tagged_content = document.tagged_content
        root_element = tagged_content.root_element

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")
        main_header = tagged_content.create_header_element()
        main_header.set_text("Main Header")
        paragraph_element = tagged_content.create_paragraph_element()
        paragraph_element.set_text(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
            + "Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. "
            + "Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet "
            + "nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. "
            + "Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat "
            + "sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper "
            + "pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus "
            + "ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus, "
            + "ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus."
        )
        root_element.append_child(main_header, True)
        root_element.append_child(paragraph_element, True)

        # Save Tagged PDF Document
        document.save(outfile)
```

## Erstellung von Tagged PDF (Erweitert)

```python
import aspose.pdf as ap
import sys
from os import path

def create_tagged_pdf_document_adv(outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get Content for working with TaggedPdf
        tagged_content = document.tagged_content
        root_element = tagged_content.root_element

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Create Header Level 1
        header1 = tagged_content.create_header_element(1)
        header1.set_text("Header Level 1")

        # Create Paragraph with Quotes
        paragraph_with_quotes = tagged_content.create_paragraph_element()
        paragraph_with_quotes.structure_text_state.font = (
            ap.text.FontRepository.find_font("Arial")
        )
        position_settings = ap.tagged.PositionSettings()
        position_settings.margin = ap.MarginInfo(10, 5, 10, 5)
        paragraph_with_quotes.adjust_position(position_settings)

        # Create Span Element
        span_element1 = tagged_content.create_span_element()
        span_element1.set_text(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. "
            "Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, "
            "luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada "
            "fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus "
            "condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae "
            "lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non "
            "lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit."
        )

        # Create Quote Element
        quote_element = tagged_content.create_quote_element()
        quote_element.set_text(
            "Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa."
        )
        quote_element.structure_text_state.font_style = (
            ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
        )

        # Create Another Span Element
        span_element2 = tagged_content.create_span_element()
        span_element2.set_text(" Sed non consectetur elit.")

        # Append Children to Paragraph
        paragraph_with_quotes.append_child(span_element1, True)
        paragraph_with_quotes.append_child(quote_element, True)
        paragraph_with_quotes.append_child(span_element2, True)

        # Append Header and Paragraph to Root Element
        root_element.append_child(header1, True)
        root_element.append_child(paragraph_with_quotes, True)

        # Save Tagged PDF Document
        document.save(outfile)
```

Wir erhalten das folgende Dokument nach der Erstellung:

![Tagged PDF-Dokument mit 2 Elementen – Header und Paragraph](taggedpdf-01.png)

## Styling Textstruktur

Tagged PDFs sind strukturierte Dokumente, die Zugänglichkeitsfunktionen und semantische Bedeutung für den Inhalt bereitstellen.

Das Beispiel erstellt ein PDF-Dokument mit Barrierefreiheitsfunktionen, indem es eine getaggte Inhaltsstruktur verwendet. Es demonstriert, wie man ein Absatz-Element mit benutzerdefiniertem Styling und korrekten Dokumenten-Metadaten erstellt.

```python
import aspose.pdf as ap
import sys
from os import path

def add_style(outfile):

    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with TaggedPdf
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        paragraph_element = tagged_content.create_paragraph_element()
        tagged_content.root_element.append_child(paragraph_element, True)

        paragraph_element.structure_text_state.font_size = 18.0
        paragraph_element.structure_text_state.foreground_color = ap.Color.red
        paragraph_element.structure_text_state.font_style = ap.text.FontStyles.ITALIC

        paragraph_element.set_text("Red italic text.")

        # Save Tagged PDF Document
        document.save(outfile)
```

## Darstellung von Structure Elements

Tagged PDFs sind essentiell für die Einhaltung von Barrierefreiheitsanforderungen und bieten strukturierte Inhalte, die von Screenreadern und anderen unterstützenden Technologien korrekt interpretiert werden können. Das folgende Code‑Snippet zeigt, wie man ein Tagged PDF‑Dokument mit einem eingebetteten Bild erstellt:

1. Erstelle ein Tagged PDF mit Bild.
1. Dokument konfigurieren.
1. Figur erstellen und konfigurieren.
1. Positionierung festlegen.
1. Dokument speichern.

```python
import aspose.pdf as ap
import sys
from os import path

def illustrate_structure_elements(imagefile, outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with TaggedPdf
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")
        figure1 = tagged_content.create_figure_element()
        tagged_content.root_element.append_child(figure1, True)
        figure1.alternative_text = "Figure One"
        figure1.title = "Image 1"
        figure1.set_tag("Fig1")
        figure1.set_image(imagefile, 300)
        # Adjust position
        position_settings = ap.tagged.PositionSettings()
        margin_info = ap.MarginInfo()
        margin_info.left = 50
        margin_info.top = 20
        position_settings.margin = margin_info
        figure1.adjust_position(position_settings)

        # Save Tagged PDF Document
        document.save(outfile)
```

## Tagged PDF validieren

Aspose.PDF for Python via .NET bietet die Möglichkeit, ein PDF/UA Tagged PDF Document zu validieren. Die 'validate_tagged_pdf' Methode validiert PDF-Dokumente gegen den PDF/UA-1 Standard, der Teil der ISO 14289 Spezifikation für barrierefreie PDF-Dokumente ist. Dies stellt sicher, dass PDFs für Benutzer mit Behinderungen und assistiven Technologien zugänglich sind.

- Dokumentenstruktur. Korrekte semantische Kennzeichnung und logische Struktur.
- Alternativtext. Alt-Text für Bilder und Nicht-Text-Elemente.
- Lesereihenfolge. Logische Reihenfolge für Screenreader.
- Farbe und Kontrast. Ausreichende Kontrastverhältnisse.
- Formulare. Barrierefreie Formularfelder und Beschriftungen.
- Navigation. Richtige Lesezeichen und Navigationsstruktur.

```python
import aspose.pdf as ap
import sys
from os import path

def validate_tagged_pdf(infile, logfile):
    # Open PDF document
    with ap.Document(infile) as document:
        is_valid = document.validate(logfile, ap.PdfFormat.PDF_UA_1)
    print(f"Is Valid: {is_valid}")
```

## Position der Textstruktur anpassen

Der folgende Codeabschnitt zeigt, wie man die Textstrukturposition im Tagged PDF-Dokument anpasst:

```python
import aspose.pdf as ap
import sys
from os import path

def adjust_position(outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with TaggedPdf
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Create paragraph
        paragraph = tagged_content.create_paragraph_element()
        tagged_content.root_element.append_child(paragraph, True)
        paragraph.set_text("Text.")

        # Adjust position
        position_settings = ap.tagged.PositionSettings()
        margin_info = ap.MarginInfo()
        margin_info.left = 300
        margin_info.top = 20
        margin_info.right = 0
        margin_info.bottom = 0
        position_settings.margin = margin_info
        position_settings.horizontal_alignment = ap.HorizontalAlignment.NONE
        position_settings.vertical_alignment = ap.VerticalAlignment.NONE
        position_settings.is_first_paragraph_in_column = False
        position_settings.is_kept_with_next = False
        position_settings.is_in_new_page = False
        position_settings.is_in_line_paragraph = False
        paragraph.adjust_position(position_settings)

        # Save Tagged PDF Document
        document.save(outfile)
```

## PDF nach PDF/UA-1 mit automatischer Tagging konvertieren

Dieses Codebeispiel erklärt, wie man ein Standard-PDF mit Aspose.PDF for Python via .NET in eine PDF/UA-1 (Universal Accessibility) konforme Datei umwandelt.

PDF/UA stellt sicher, dass Dokumente für Nutzer mit Behinderungen zugänglich sind und mit unterstützenden Technologien wie Bildschirmlesern kompatibel sind. Während der Konvertierung kann die Bibliothek automatisch den logischen Strukturbaum erzeugen und semantische Tags mithilfe der integrierten Auto‑Tagging‑ und Überschriftenerkennung anwenden.

Durch das Konfigurieren von PdfFormatConversionOptions und das Aktivieren von AutoTaggingSettings können Sie vorhandene PDFs effizient in barrierefreie Dokumente umwandeln, ohne die Struktur manuell zu bearbeiten.

1. Laden Sie das Quelldokument.
1. PDF/UA-Konvertierungsoptionen erstellen.
1. Automatisches Tagging aktivieren.
1. Überschriftenerkennung konfigurieren.
1. Fügen Sie die Tagging-Konfiguration den Konvertierungsoptionen hinzu.
1. Führen Sie den Konvertierungsprozess aus.
1. Speichern Sie das barrierefreie PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def convert_to_pdf_ua_with_automatic_tagging(infile, outfile, logfile):
    # Create PDF Document
    with ap.Document(infile) as document:
        # Create conversion options
        options = ap.PdfFormatConversionOptions(
            logfile, ap.PdfFormat.PDF_UA_1, ap.ConvertErrorAction.DELETE
        )
        # Create auto-tagging settings
        # aspose.pdf.AutoTaggingSettings.default may be used to set the same settings as given below
        auto_tagging_settings = ap.AutoTaggingSettings()
        # Enable auto-tagging during the conversion process
        auto_tagging_settings.enable_auto_tagging = True
        # Use the heading recognition strategy that's optimal for the given document structure
        auto_tagging_settings.heading_recognition_strategy = (
            ap.HeadingRecognitionStrategy.AUTO
        )
        # Assign auto-tagging settings to be used during the conversion process
        options.auto_tagging_settings = auto_tagging_settings
        # During the conversion, the document logical structure will be automatically created
        document.convert(options)
        # Save PDF document
        document.save(outfile)
```

## Erstellen Sie ein Tagged PDF mit einem barrierefreien Signature FormField

1. Erstelle ein neues PDF-Dokument.
1. Zugriff auf getaggte Inhalte.
1. Erstellen Sie ein Signatur-Formularfeld.
1. Fügen Sie das Feld zum AcroForm hinzu.
1. Erstellen Sie ein Form-Element in der Tag-Struktur.
1. Verknüpfen Sie das Structure-Element mit dem Form-Feld.
1. Fügen Sie das Form-Element dem logischen Strukturbaum hinzu.
1. Speichern Sie das Dokument.

```python
import aspose.pdf as ap
import sys
from os import path

def create_pdf_with_tagged_form_field(outfile):
    # Create PDF document
    with ap.Document() as document:
        document.pages.add()
        # Get Content for work with TaggedPdf
        tagged_content = document.tagged_content
        root_element = tagged_content.root_element
        # Create a visible signature form field (AcroForm)
        signature_field = ap.forms.SignatureField(
            document.pages[1], ap.Rectangle(50, 50, 100, 100, True)
        )
        signature_field.partial_name = "Signature1"
        signature_field.alternate_name = "signature 1"

        # Add the signature field to the document's AcroForm
        document.form.add(signature_field)

        # Create a /Form structure element in the tag tree
        form = tagged_content.create_form_element()
        form.alternative_text = "form 1"

        # Link the /Form tag to the signature field via an /OBJR reference
        form.tag(signature_field)

        # Add the /Form structure element to the document’s logical structure tree
        root_element.append_child(form, True)

        # Save PDF document
        document.save(outfile)
```

## Erstelle ein Tagged PDF mit einer Inhaltsverzeichnis‑Seite (TOC)

Dieses Beispiel zeigt, wie man ein Tagged PDF Document mit einer strukturierten Table of Contents (TOC)-Seite erstellt, wobei Aspose.PDF for Python via .NET verwendet wird.

1. Erstelle ein neues PDF-Dokument.
1. Erstelle eine dedizierte Inhaltsverzeichnis-Seite.
1. Erstellen und registrieren Sie das TOC-Element im logischen Strukturbaum.
1. Fügen Sie eine Inhaltsseite hinzu.
1. Erstelle ein Header-Element.
1. Erstelle ein /TOCI-Element.
1. Verlinken Sie die Überschrift mit dem TOC.
1. Speichern Sie das Dokument.

```python
import aspose.pdf as ap
import sys
from os import path

def create_pdf_with_toc_page(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get tagged content for the PDF structure
        content = document.tagged_content
        root_element = content.root_element
        content.set_language("en-US")
        # Add the table of contents (TOC) page
        toc_page = document.pages.add()
        toc_page.toc_info = ap.TocInfo()
        # Create a TOC structure element
        toc_element = content.create_toc_element()
        # Add the TOC element to the document structure tree
        root_element.append_child(toc_element, True)
        # Add a content page
        document.pages.add()
        # Create a header element and set its text
        header = content.create_header_element(1)
        header.set_text("1. Header")
        # Add the header to the document structure
        root_element.append_child(header, True)
        # Create a TOC item (TOCI) element
        toci = content.create_toci_element()
        # Add the TOCI element to the TOC element
        toc_element.append_child(toci, True)
        # Add an entry to the TOC page and link it to the TOCI element
        header.add_entry_to_toc_page(toc_page, toci)
        # Add a logical reference to the header within the TOCI element
        toci.add_ref(header)
        # Save PDF document
        document.save(outfile)
```

## Erstellen Sie ein erweitertes Tagged PDF mit hierarchischem Inhaltsverzeichnis (TOC)

Mit Aspose.PDF for Python via .NET können Sie ein fortschrittliches, vollständig getaggtes PDF-Dokument mit einem strukturierten und hierarchischen Inhaltsverzeichnis (TOC) erstellen.

1. Erstellen Sie das Dokument und aktivieren Sie Tagged content.
1. Fügen Sie die TOC-Seite hinzu und konfigurieren Sie sie.
1. Erstelle das /TOC-Strukturelement.
1. Verlinken Sie den TOC‑Seitentitel mit einem Header‑Element.
1. Füge Hauptinhaltseite und erste Überschrift hinzu.
1. Erstellen Sie einen TOC-Eintrag für die Überschrift.
1. Erstellen Sie verschachtelte Unterabschnitte mit Listenstruktur.
1. Fügen Sie einen zweiten Top-Level-Abschnitt hinzu.
1. Speichern Sie das Dokument.

```python
import aspose.pdf as ap
import sys
from os import path

def create_pdf_with_toc_page_advanced(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get tagged content for the PDF structure
        content = document.tagged_content
        root_element = content.root_element
        content.set_language("en-US")
        # Add the table of contents (TOC) page
        toc_page = document.pages.add()
        toc_page.toc_info = ap.TocInfo()
        toc_page.toc_info.title = ap.text.TextFragment("Table of Contents")
        # Create a TOC structure element
        toc_element = content.create_toc_element()
        # Create a header element for the TOC page title
        header_for_toc_page_title = content.create_header_element(1)
        toc_element.link_toc_page_title_to_header_element(
            toc_page, header_for_toc_page_title
        )
        # Add the TOC page title header and TOC element to the document structure tree
        root_element.append_child(header_for_toc_page_title, True)
        root_element.append_child(toc_element, True)
        # Add a content page
        document.pages.add()
        # Create a header element and set its text
        header = content.create_header_element(1)
        header.set_text("1. Header")
        # Add the header to the document structure
        root_element.append_child(header, True)
        # Create a TOC item (TOCI) element
        toci = content.create_toci_element()
        # Add the TOCI element to the TOC element
        toc_element.append_child(toci, True)
        # Add an entry to the TOC page and link it to the TOCI element
        header.add_entry_to_toc_page(toc_page, toci)
        # Add a logical reference to the header within the TOCI element
        toci.add_ref(header)
        # Create a list element for TOCI subitems
        list_element = content.create_list_element()
        for i in range(1, 4):
            # Create a list item (LI) element
            li = content.create_list_li_element()
            # Add the list item to the list element
            list_element.append_child(li, True)
            # Create a sub-header element and set its properties
            sub_header = content.create_header_element(2)
            sub_header.structure_text_state.font_size = 14
            sub_header.language = "en-US"
            sub_header.set_text(f"1.{i} subheader ")
            # Add an entry to the TOC page and link it to the LI element
            sub_header.add_entry_to_toc_page(toc_page, li)
            # Add a logical reference to the subheader element
            li.add_ref(sub_header)
            # Create a paragraph element and set its text and language
            p = content.create_paragraph_element()
            p.set_text(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
            )
            p.language = "en-US"
            # Add the sub-header and paragraph to the document structure
            root_element.append_child(sub_header, True)
            root_element.append_child(p, True)
        # Add the list element as a child to the TOCI element
        toci.append_child(list_element, True)
        # --- Additional TOC header example ---
        # Create a second header element (see comments above for header 1)
        header2 = content.create_header_element(1)
        header2.set_text("2. Header")
        root_element.append_child(header2, True)

        toci2 = content.create_toci_element()
        toc_element.append_child(toci2, True)

        header2.add_entry_to_toc_page(toc_page, toci2)
        toci2.add_ref(header2)
        # Save the PDF document
        document.save(outfile)
```

## Verwandte Tagged PDF-Themen

- [Extrahiere Tagged Content aus Tagged PDFs](/pdf/de/python-net/extract-tagged-content-from-tagged-pdfs/) um den logischen Strukturbaum nach der Erstellung zu inspizieren.
- [Einstellen der Structure Elements-Eigenschaften](/pdf/de/python-net/setting-structure-elements-properties/) um Titel, Sprache, Alt-Text und Erweiterungstext zu verfeinern.
- [Arbeiten mit Tabelle in Tagged PDFs](/pdf/de/python-net/working-with-table-in-tagged-pdfs/) wenn Ihr barrierefreies Dokument strukturierte Tabellen enthält.
