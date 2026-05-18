---
title: Festlegen von Tagged PDF‑Strukturelementeigenschaften in Python
linktitle: Einstellen der Structure Elements-Eigenschaften
type: docs
weight: 30
url: /de/python-net/setting-structure-elements-properties/
description: Erfahren Sie, wie Sie Tagged PDF‑Strukturelementeigenschaften in Python mit Aspose.PDF for Python via .NET festlegen, einschließlich Titel, Sprache, tatsächlicher Text, alternativer Text und Erweiterungstext.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Structure Elements definieren die semantische Hierarchie eines PDF-Dokuments, wie Abschnitte, Überschriften, Absätze oder Tabellen. Durch das Festlegen von Eigenschaften wie title, language, alternative_text, actual_text und expansion_text verbessern Sie die Barrierefreiheit und die semantische Bedeutung des PDFs für unterstützende Technologien wie Screenreader.

Das folgende Code‑Snippet zeigt, wie man die Eigenschaften von Structure Elements eines Tagged PDF‑Dokuments festlegt:

1. Erstellen Sie ein neues Tagged PDF-Dokument.
1. Dokumentmetadaten festlegen.
1. Strukturelemente erstellen.
1. Zugänglichkeitseigenschaften festlegen.
1. Speichern Sie das Tagged PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def set_properties(outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Create Structure Elements
        root_element = tagged_content.root_element

        section_element = tagged_content.create_sect_element()
        root_element.append_child(section_element, True)

        header_element = tagged_content.create_header_element(1)
        section_element.append_child(header_element, True)
        header_element.set_text("The Header")

        header_element.title = "Title"
        header_element.language = "en-US"
        header_element.alternative_text = "Alternative Text"
        header_element.expansion_text = "Expansion Text"
        header_element.actual_text = "Actual Text"

        # Save Tagged PDF Document
        document.save(outfile)
```

## Festlegen von Text Structure Elements

Um Textstruktur-Elemente eines Tagged PDF Document festzulegen, bietet Aspose.PDF [AbsatzElement](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/paragraphelement/) Klasse. Der folgende Codeabschnitt zeigt, wie man Texte-Strukturelemente eines Tagged PDF Document festlegt:

```python
import aspose.pdf as ap
import sys
from os import path

def set_text_elements(outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Get Root Structure Elements
        root_element = tagged_content.root_element

        paragraph_element = tagged_content.create_paragraph_element()

        # Set Text to Text Structure Element
        paragraph_element.set_text("Paragraph.")
        root_element.append_child(paragraph_element, True)

        # Save Tagged PDF Document
        document.save(outfile)

```

## Einstellen von Textblock-Strukturelementen

Dieses Python‑Beispiel verwendet Aspose.PDF, um ein Tagged PDF zu erstellen, das eine strukturierte Hierarchie von Überschriften und einen Absatz enthält und die semantischen sowie Barrierefreiheits‑Merkmale des Dokuments verbessert.

1. Erstellen Sie ein neues Tagged PDF-Dokument.
1. Dokumentmetadaten festlegen.
1. Greifen Sie auf das Root-Strukturelement zu.
1. Mehrstufige Überschriften erstellen.
1. Header an die Wurzelstruktur anhängen.
1. Erstelle ein Absatz-Element.
1. Absatz zur Wurzelstruktur hinzufügen.
1. Speichern Sie das Tagged PDF.

Das folgende Code‑Snippet zeigt, wie man Textblock‑Strukturelemente eines Tagged PDF Document festlegt:

```python
import aspose.pdf as ap
import sys
from os import path

def set_text_block_elements(outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content
        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")
        # Get Root Structure Element
        root_element = tagged_content.root_element
        h1 = tagged_content.create_header_element(1)
        h2 = tagged_content.create_header_element(2)
        h3 = tagged_content.create_header_element(3)
        h4 = tagged_content.create_header_element(4)
        h5 = tagged_content.create_header_element(5)
        h6 = tagged_content.create_header_element(6)
        h1.set_text("H1. Header of Level 1")
        h2.set_text("H2. Header of Level 2")
        h3.set_text("H3. Header of Level 3")
        h4.set_text("H4. Header of Level 4")
        h5.set_text("H5. Header of Level 5")
        h6.set_text("H6. Header of Level 6")
        root_element.append_child(h1, True)
        root_element.append_child(h2, True)
        root_element.append_child(h3, True)
        root_element.append_child(h4, True)
        root_element.append_child(h5, True)
        root_element.append_child(h6, True)
        p = tagged_content.create_paragraph_element()
        p.set_text(
            "P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
            "Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit."
            " Cras pellentesque libero semper, gravida magna sed, luctus leo. "
            "Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. "
            "Interdum et malesuada fames ac ante ipsum primis in faucibus. "
            "Aliquam lacinia sit amet elit ac consectetur. "
            "Donec cursus condimentum ligula, vitae volutpat sem tristique eget. "
            "Nulla in consectetur massa. Vestibulum vitae lobortis ante. "
            "Nulla ullamcorper pellentesque justo rhoncus accumsan. "
            "Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. "
            "Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, "
            "vitae posuere risus odio id massa. Cras sed venenatis lacus."
        )
        root_element.append_child(p, True)
        # Save Tagged PDF Document
        document.save(outfile)
```

## Inline Structure Elements festlegen

Erstellen Sie Inline-Text-Elemente (/Span) innerhalb von Überschriften und Absätzen in einem Tagged PDF mithilfe von Aspose.PDF für Python via .NET.

Das folgende Code‑Snippet zeigt, wie man Inline‑Strukturelemente eines Tagged PDF Document setzt:

```python
import aspose.pdf as ap
import sys
from os import path

def set_inline_elements(outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Get Root Structure Element
        root_element = tagged_content.root_element

        header_element_h1 = tagged_content.create_header_element(1)
        header_element_h2 = tagged_content.create_header_element(2)
        header_element_h3 = tagged_content.create_header_element(3)
        header_element_h4 = tagged_content.create_header_element(4)
        header_element_h5 = tagged_content.create_header_element(5)
        header_element_h6 = tagged_content.create_header_element(6)
        root_element.append_child(header_element_h1, True)
        root_element.append_child(header_element_h2, True)
        root_element.append_child(header_element_h3, True)
        root_element.append_child(header_element_h4, True)
        root_element.append_child(header_element_h5, True)
        root_element.append_child(header_element_h6, True)

        span_element_h11 = tagged_content.create_span_element()
        span_element_h11.set_text("H1. ")
        header_element_h1.append_child(span_element_h11, True)
        span_element_h12 = tagged_content.create_span_element()
        span_element_h12.set_text("Level 1 Header")
        header_element_h1.append_child(span_element_h12, True)

        span_element_h21 = tagged_content.create_span_element()
        span_element_h21.set_text("H2. ")
        header_element_h2.append_child(span_element_h21, True)
        span_element_h22 = tagged_content.create_span_element()
        span_element_h22.set_text("Level 2 Header")
        header_element_h2.append_child(span_element_h22, True)

        span_element_h31 = tagged_content.create_span_element()
        span_element_h31.set_text("H3. ")
        header_element_h3.append_child(span_element_h31, True)
        span_element_h32 = tagged_content.create_span_element()
        span_element_h32.set_text("Level 3 Header")
        header_element_h3.append_child(span_element_h32, True)

        span_element_h41 = tagged_content.create_span_element()
        span_element_h41.set_text("H4. ")
        header_element_h4.append_child(span_element_h41, True)
        span_element_h42 = tagged_content.create_span_element()
        span_element_h42.set_text("Level 4 Header")
        header_element_h4.append_child(span_element_h42, True)

        span_element_h51 = tagged_content.create_span_element()
        span_element_h51.set_text("H5. ")
        header_element_h5.append_child(span_element_h51, True)
        span_element_h52 = tagged_content.create_span_element()
        span_element_h52.set_text("Level 5 Header")
        header_element_h5.append_child(span_element_h52, True)

        span_element_h61 = tagged_content.create_span_element()
        span_element_h61.set_text("H6. ")
        header_element_h6.append_child(span_element_h61, True)
        span_element_h62 = tagged_content.create_span_element()
        span_element_h62.set_text("Level 6 Header")
        header_element_h6.append_child(span_element_h62, True)

        paragraph_element = tagged_content.create_paragraph_element()
        paragraph_element.set_text("P. ")
        root_element.append_child(paragraph_element, True)
        span_element_1 = tagged_content.create_span_element()
        span_element_1.set_text(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        )
        paragraph_element.append_child(span_element_1, True)
        span_element_2 = tagged_content.create_span_element()
        span_element_2.set_text("Aenean nec lectus ac sem faucibus imperdiet. ")
        paragraph_element.append_child(span_element_2, True)
        span_element_3 = tagged_content.create_span_element()
        span_element_3.set_text("Sed ut erat ac magna ullamcorper hendrerit. ")
        paragraph_element.append_child(span_element_3, True)
        span_element_4 = tagged_content.create_span_element()
        span_element_4.set_text(
            "Cras pellentesque libero semper, gravida magna sed, luctus leo. "
        )
        paragraph_element.append_child(span_element_4, True)
        span_element_5 = tagged_content.create_span_element()
        span_element_5.set_text(
            "Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. "
        )
        paragraph_element.append_child(span_element_5, True)
        span_element_6 = tagged_content.create_span_element()
        span_element_6.set_text(
            "Interdum et malesuada fames ac ante ipsum primis in faucibus. "
        )
        paragraph_element.append_child(span_element_6, True)
        span_element_7 = tagged_content.create_span_element()
        span_element_7.set_text(
            "Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. "
        )
        paragraph_element.append_child(span_element_7, True)
        span_element_8 = tagged_content.create_span_element()
        span_element_8.set_text(
            "Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. "
        )
        paragraph_element.append_child(span_element_8, True)
        span_element_9 = tagged_content.create_span_element()
        span_element_9.set_text(
            "Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. "
        )
        paragraph_element.append_child(span_element_9, True)
        span_element_10 = tagged_content.create_span_element()
        span_element_10.set_text(
            "Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus."
        )
        paragraph_element.append_child(span_element_10, True)

        # Save Tagged PDF Document
        document.save(outfile)
```

## Benutzerdefinierten Tag-Namen festlegen

Benutzerdefinierte Tag-Namen für Struktur- und Inline-Elemente in einem Tagged PDF mit Aspose.PDF für Python festlegen.

Der folgende Codeabschnitt zeigt, wie man einen benutzerdefinierten Tag-Namen festlegt:

1. Erstellen Sie ein neues Tagged PDF-Dokument.
1. Dokumentmetadaten festlegen.
1. Erstelle ein Section-Element.
1. Erstelle Absatz-Elemente mit benutzerdefinierten Tags.
1. Erstelle Inline-Span-Elemente mit benutzerdefinierten Tags.
1. Speichern Sie das Tagged PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def set_tag_name(outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Create Logical Structure Elements
        section_element = tagged_content.create_sect_element()
        tagged_content.root_element.append_child(section_element, True)

        paragraph_element1 = tagged_content.create_paragraph_element()
        paragraph_element2 = tagged_content.create_paragraph_element()
        paragraph_element3 = tagged_content.create_paragraph_element()
        paragraph_element4 = tagged_content.create_paragraph_element()

        paragraph_element1.set_text("P1. ")
        paragraph_element2.set_text("P2. ")
        paragraph_element3.set_text("P3. ")
        paragraph_element4.set_text("P4. ")

        paragraph_element1.set_tag("P1")
        paragraph_element2.set_tag("Para")
        paragraph_element3.set_tag("Para")
        paragraph_element4.set_tag("Paragraph")

        section_element.append_child(paragraph_element1, True)
        section_element.append_child(paragraph_element2, True)
        section_element.append_child(paragraph_element3, True)
        section_element.append_child(paragraph_element4, True)

        span_element1 = tagged_content.create_span_element()
        span_element2 = tagged_content.create_span_element()
        span_element3 = tagged_content.create_span_element()
        span_element4 = tagged_content.create_span_element()

        span_element1.set_text("Span 1.")
        span_element2.set_text("Span 2.")
        span_element3.set_text("Span 3.")
        span_element4.set_text("Span 4.")

        span_element1.set_tag("SPAN")
        span_element2.set_tag("Sp")
        span_element3.set_tag("Sp")
        span_element4.set_tag("TheSpan")

        paragraph_element1.append_child(span_element1, True)
        paragraph_element2.append_child(span_element2, True)
        paragraph_element3.append_child(span_element3, True)
        paragraph_element4.append_child(span_element4, True)

        # Save Tagged PDF Document
        document.save(outfile)
```

## Strukturelement in Elemente einfügen

**Dieses Feature wird ab Version 19.4 oder höher unterstützt.**

Erstellen Sie Links und Bildelemente in einem Tagged PDF mit Aspose.PDF for Python via .NET.

Das folgende Code‑Snippet zeigt, wie man Strukturelemente in einem Absatz mit dem Text eines Tagged PDF‑Dokuments festlegt:

```python
import aspose.pdf as ap
import sys
from os import path

def set_elements(imagefile, outfile):
    # Create PDF document
    with ap.Document() as document:
        tagged_content = document.tagged_content

        # Setting Title and Nature Language for document
        tagged_content.set_title("Link Elements Example")
        tagged_content.set_language("en-US")

        # Getting Root structure element (Document structure element)
        root_element = tagged_content.root_element

        paragraph_element_1 = tagged_content.create_paragraph_element()
        root_element.append_child(paragraph_element_1, True)
        link_element_1 = tagged_content.create_link_element()
        paragraph_element_1.append_child(link_element_1, True)
        link_element_1.hyperlink = ap.WebHyperlink("http://google.com")
        link_element_1.set_text("Google")
        link_element_1.alternate_descriptions = "Link to Google"

        paragraph_element_2 = tagged_content.create_paragraph_element()
        root_element.append_child(paragraph_element_2, True)
        link_element_2 = tagged_content.create_link_element()
        paragraph_element_2.append_child(link_element_2, True)
        link_element_2.hyperlink = ap.WebHyperlink("http://google.com")
        span_element_2 = tagged_content.create_span_element()
        span_element_2.set_text("Google")
        link_element_2.append_child(span_element_2, True)
        link_element_2.alternate_descriptions = "Link to Google"

        paragraph_element_3 = tagged_content.create_paragraph_element()
        root_element.append_child(paragraph_element_3, True)
        link_element_3 = tagged_content.create_link_element()
        paragraph_element_3.append_child(link_element_3, True)
        link_element_3.hyperlink = ap.WebHyperlink("http://google.com")
        span_element_31 = tagged_content.create_span_element()
        span_element_31.set_text("G")
        span_element_32 = tagged_content.create_span_element()
        span_element_32.set_text("Google")
        link_element_3.append_child(span_element_31, True)
        link_element_3.set_text("-")
        link_element_3.append_child(span_element_32, True)
        link_element_3.alternate_descriptions = "Link to Google"

        paragraph_element_4 = tagged_content.create_paragraph_element()
        root_element.append_child(paragraph_element_4, True)
        link_element_4 = tagged_content.create_link_element()
        paragraph_element_4.append_child(link_element_4, True)
        link_element_4.hyperlink = ap.WebHyperlink("http://google.com")
        link_element_4.set_text(
            "The multiline link: Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google"
        )
        link_element_4.alternate_descriptions = "Link to Google (multiline)"

        paragraph_element_5 = tagged_content.create_paragraph_element()
        root_element.append_child(paragraph_element_5, True)
        link_element_5 = tagged_content.create_link_element()
        paragraph_element_5.append_child(link_element_5, True)
        link_element_5.hyperlink = ap.WebHyperlink("http://google.com")
        figure_element_5 = tagged_content.create_figure_element()
        figure_element_5.set_image(imagefile, 1200)
        figure_element_5.alternative_text = "Google icon"
        link_layout_attributes = link_element_5.attributes.get_attributes(
            ap.logicalstructure.AttributeOwnerStandard.LAYOUT
        )
        placement_attribute = ap.logicalstructure.StructureAttribute(
            ap.logicalstructure.AttributeKey.PLACEMENT
        )
        placement_attribute.set_name_value(
            ap.logicalstructure.AttributeName.PLACEMENT_BLOCK
        )
        link_layout_attributes.set_attribute(placement_attribute)
        link_element_5.append_child(figure_element_5, True)
        link_element_5.alternate_descriptions = "Link to Google"

        # Save Tagged PDF Document
        document.save(outfile)
```

## Link-Strukturelement festlegen

Aspose.PDF for Python via .NET API ermöglicht es Ihnen auch, Link‑Strukturelemente hinzuzufügen.

Der folgende Codeabschnitt zeigt, wie man ein Link‑Strukturelement zu einem Tagged PDF Document hinzufügt:

```python
import aspose.pdf as ap
import sys
from os import path

def add_link_element(outfile):
    # Create PDF document
    with ap.Document() as document:
        tagged_content = document.tagged_content

        # Setting Title and Nature Language for document
        tagged_content.set_title("Text Elements Example")
        tagged_content.set_language("en-US")

        # Getting Root structure element (Document structure element)
        root_element = tagged_content.root_element

        paragraph_element_1 = tagged_content.create_paragraph_element()
        root_element.append_child(paragraph_element_1, True)
        span_element_11 = tagged_content.create_span_element()
        span_element_11.set_text("Span_11")
        span_element_12 = tagged_content.create_span_element()
        span_element_12.set_text(" and Span_12.")
        paragraph_element_1.set_text("Paragraph with ")
        paragraph_element_1.append_child(span_element_11, True)
        paragraph_element_1.append_child(span_element_12, True)

        paragraph_element_2 = tagged_content.create_paragraph_element()
        root_element.append_child(paragraph_element_2, True)
        span_element_21 = tagged_content.create_span_element()
        span_element_21.set_text("Span_21")
        span_element_22 = tagged_content.create_span_element()
        span_element_22.set_text("Span_22.")
        paragraph_element_2.append_child(span_element_21, True)
        paragraph_element_2.set_text(" and ")
        paragraph_element_2.append_child(span_element_22, True)

        paragraph_element_3 = tagged_content.create_paragraph_element()
        root_element.append_child(paragraph_element_3, True)
        span_element_31 = tagged_content.create_span_element()
        span_element_31.set_text("Span_31")
        span_element_32 = tagged_content.create_span_element()
        span_element_32.set_text(" and Span_32")
        paragraph_element_3.append_child(span_element_31, True)
        paragraph_element_3.append_child(span_element_32, True)
        paragraph_element_3.set_text(".")

        paragraph_element_4 = tagged_content.create_paragraph_element()
        root_element.append_child(paragraph_element_4, True)
        span_element_41 = tagged_content.create_span_element()
        span_element_411 = tagged_content.create_span_element()
        span_element_411.set_text("Span_411, ")
        span_element_41.set_text("Span_41, ")
        span_element_41.append_child(span_element_411, True)
        span_element_42 = tagged_content.create_span_element()
        span_element_421 = tagged_content.create_span_element()
        span_element_421.set_text("Span 421 and ")
        span_element_42.append_child(span_element_421, True)
        span_element_42.set_text("Span_42")
        paragraph_element_4.append_child(span_element_41, True)
        paragraph_element_4.append_child(span_element_42, True)
        paragraph_element_4.set_text(".")

        # Save Tagged PDF Document
        document.save(outfile)
```

## Note-Strukturelement festlegen

Aspose.PDF for Python via .NET API ermöglicht Ihnen auch, hinzuzufügen [HinweisElement](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/noteelement/) in einem getaggten PDF-Dokument. Der folgende Codeabschnitt zeigt, wie man ein Notiz-Element in Tagged PDF Document hinzufügt:

```python
import aspose.pdf as ap
import sys
from os import path

def set_note_element(outfile):
    # Create PDF Document
    with ap.Document() as document:
        tagged_content = document.tagged_content

        tagged_content.set_title("Sample of Note Elements")
        tagged_content.set_language("en-US")

        # Add Paragraph Element
        paragraph_element = tagged_content.create_paragraph_element()
        tagged_content.root_element.append_child(paragraph_element, True)

        # Add NoteElement
        note_element_1 = tagged_content.create_note_element()
        paragraph_element.append_child(note_element_1, True)
        note_element_1.set_text("Note with auto generate ID. ")

        # Add NoteElement
        note_element_2 = tagged_content.create_note_element()
        paragraph_element.append_child(note_element_2, True)
        note_element_2.set_text("Note with ID = 'note_002'. ")
        note_element_2.set_id("note_002")

        # Add NoteElement
        note_element_3 = tagged_content.create_note_element()
        paragraph_element.append_child(note_element_3, True)
        note_element_3.set_text("Note with ID = 'note_003'. ")
        note_element_3.set_id("note_003")

        # Must throw exception - Aspose.Pdf.Tagged.TaggedException : Structure element with ID='note_002' already exists
        # note_element_3.set_id("note_002")

        # Resultant document does not compliance to PDF/UA If ClearId() used for Note Structure Element
        # note_element_3.clear_id()

        # Save Tagged PDF Document
        document.save(outfile)
```

## Wie man Sprache und Titel festlegt

Aspose.PDF for Python via .NET API ermöglicht es Ihnen auch, die Sprache und den Titel für ein Document gemäß der Spezifikation PDF/UA festzulegen. Die Sprache kann sowohl für das gesamte Document als auch für seine separaten strukturellen Elemente festgelegt werden. Der folgende Codeabschnitt zeigt, wie man die Sprache und den Titel in einem Tagged PDF Document festlegt:

1. Erstellen Sie ein neues Tagged PDF-Dokument.
1. Dokumenttitel und Sprache festlegen.
1. Erstelle ein Header-Element.
1. Fügen Sie Absätze mit spezifischen Sprachen hinzu.
1. Speichern Sie das Tagged PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def set_language_and_title(outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get TaggedContent
        tagged_content = document.tagged_content

        # Set Title and Language
        tagged_content.set_title("Example Tagged Document")
        tagged_content.set_language("en-US")

        # Header (en-US, inherited from document)
        header_element = tagged_content.create_header_element(1)
        header_element.set_text("Phrase on different languages")
        tagged_content.root_element.append_child(header_element, True)

        # Paragraph (English)
        paragraph_element_en = tagged_content.create_paragraph_element()
        paragraph_element_en.set_text("Hello, World!")
        paragraph_element_en.language = "en-US"
        tagged_content.root_element.append_child(paragraph_element_en, True)

        # Paragraph (German)
        paragraph_element_de = tagged_content.create_paragraph_element()
        paragraph_element_de.set_text("Hallo Welt!")
        paragraph_element_de.language = "de-DE"
        tagged_content.root_element.append_child(paragraph_element_de, True)

        # Paragraph (French)
        paragraph_element_fr = tagged_content.create_paragraph_element()
        paragraph_element_fr.set_text("Bonjour le monde!")
        paragraph_element_fr.language = "fr-FR"
        tagged_content.root_element.append_child(paragraph_element_fr, True)

        # Paragraph (Spanish)
        paragraph_element_sp = tagged_content.create_paragraph_element()
        paragraph_element_sp.set_text("¡Hola Mundo!")
        paragraph_element_sp.language = "es-ES"
        tagged_content.root_element.append_child(paragraph_element_sp, True)

        # Save Tagged PDF Document
        document.save(outfile)
```

## Verwandte Tagged PDF-Themen

- [Tagged PDF erstellen](/pdf/de/python-net/create-tagged-pdf/) um die Strukturelemente zu erzeugen, bevor deren Eigenschaften aktualisiert werden.
- [Extrahiere Tagged Content aus Tagged PDFs](/pdf/de/python-net/extract-tagged-content-from-tagged-pdfs/) um vorhandene Strukturknoten und Metadaten zu inspizieren.
- [Arbeiten mit Tabelle in Tagged PDFs](/pdf/de/python-net/working-with-table-in-tagged-pdfs/) wenn Sie barrierefreie Eigenschaften auf Tabellenstrukturen anwenden müssen.
