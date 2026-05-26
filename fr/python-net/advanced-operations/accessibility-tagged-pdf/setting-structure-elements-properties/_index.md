---
title: Définir les propriétés des éléments de structure Tagged PDF en Python
linktitle: Définir les propriétés des éléments de structure
type: docs
weight: 30
url: /fr/python-net/setting-structure-elements-properties/
description: Apprenez comment définir les propriétés des éléments de structure Tagged PDF en Python avec Aspose.PDF for Python via .NET, y compris le titre, la langue, le texte réel, le texte alternatif et le texte d'extension.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Les Structure Elements définissent la hiérarchie sémantique d’un document PDF, comme les sections, les en‑têtes, les paragraphes ou les tableaux. En définissant des propriétés telles que title, language, alternative_text, actual_text et expansion_text, vous améliorez l’accessibilité et la signification sémantique du PDF pour les technologies d’assistance comme les lecteurs d’écran.

L'extrait de code suivant montre comment définir les propriétés des éléments de structure d'un Tagged PDF Document :

1. Créez un nouveau document PDF balisé.
1. Définir les métadonnées du document.
1. Créer des éléments de structure.
1. Définir les propriétés d'accessibilité.
1. Enregistrez le PDF balisé.

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

## Définition des éléments de structure du texte

Afin de définir les éléments de structure de texte d'un Tagged PDF Document, Aspose.PDF propose [ParagraphElement](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/paragraphelement/) classe. Le fragment de code suivant montre comment définir les éléments de structure texte d'un Document PDF balisé :

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

## Définition du bloc de texte Structure Elements

Cet exemple Python utilise Aspose.PDF pour créer un Tagged PDF qui inclut une hiérarchie structurée d'en-têtes et d'un paragraphe, améliorant les caractéristiques sémantiques et d'accessibilité du document.

1. Créez un nouveau document PDF balisé.
1. Définir les métadonnées du document.
1. Accéder à l'élément de structure racine.
1. Créer des en-têtes à plusieurs niveaux.
1. Ajouter des en-têtes à la structure racine.
1. Créer un élément de paragraphe.
1. Ajouter un paragraphe à la structure racine.
1. Enregistrez le PDF balisé.

L'extrait de code suivant montre comment définir les éléments de structure de bloc de texte d'un Document PDF balisé :

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

## Définition des éléments de structure en ligne

Créer des éléments de texte en ligne (/Span) dans les en-têtes et les paragraphes d’un PDF balisé en utilisant Aspose.PDF for Python via .NET.

L'extrait de code suivant montre comment définir les éléments de structure en ligne d'un Document Tagged PDF :

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

## Définir le nom de balise personnalisé

Définir des noms de balises personnalisés pour les éléments de structure et en ligne dans un PDF balisé à l'aide d'Aspose.PDF for Python.

Le fragment de code suivant montre comment définir un nom de balise personnalisé :

1. Créez un nouveau document PDF balisé.
1. Définir les métadonnées du document.
1. Créer un élément de section.
1. Créer des éléments de paragraphe avec des balises personnalisées.
1. Créer des éléments span en ligne avec des balises personnalisées.
1. Enregistrez le PDF balisé.

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

## Ajout d'un élément de structure dans les éléments

**Cette fonctionnalité est prise en charge à partir de la version 19.4 ou supérieure.**

Créer des liens et des éléments d'image dans un PDF balisé à l'aide d'Aspose.PDF for Python via .NET.

L'extrait de code suivant montre comment définir des éléments de structure dans un paragraphe avec le texte d'un Document PDF balisé :

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

## Configuration de l'élément de structure de lien

L'API Aspose.PDF for Python via .NET permet également d'ajouter des éléments de structure de lien.

L'extrait de code suivant montre comment ajouter un élément de structure de lien dans un Document Tagged PDF :

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

## Configuration de l'élément de structure de note

Aspose.PDF for Python via .NET API permet également d'ajouter [NoteElement](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/noteelement/) dans un document Tagged PDF. Le fragment de code suivant montre comment ajouter un élément de note dans le Document Tagged PDF :

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

## Comment définir la langue et le titre

Aspose.PDF for Python via .NET API permet également de définir la langue et le titre d'un document conformément à la spécification PDF/UA. La langue peut être définie à la fois pour l'ensemble du document et pour ses éléments structurels séparés. Le fragment de code suivant montre comment définir la langue et le titre dans un document Tagged PDF :

1. Créez un nouveau document PDF balisé.
1. Définir le titre du document et la langue.
1. Créer un élément d'en-tête.
1. Ajouter des paragraphes avec des langues spécifiques.
1. Enregistrez le PDF balisé.

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

## Sujets liés aux PDF balisés

- [Créer Tagged PDF](/pdf/fr/python-net/create-tagged-pdf/) générer les éléments de structure avant de mettre à jour leurs propriétés.
- [Extraire le contenu balisé des Tagged PDFs](/pdf/fr/python-net/extract-tagged-content-from-tagged-pdfs/) pour inspecter les nœuds de structure existants et les métadonnées.
- [Travailler avec la Table dans Tagged PDFs](/pdf/fr/python-net/working-with-table-in-tagged-pdfs/) si vous devez appliquer des propriétés d'accessibilité aux structures de tableau.
