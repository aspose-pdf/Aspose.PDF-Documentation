---
title: Establecer propiedades de elementos de estructura en PDF etiquetados en Python
linktitle: Propiedades de elementos de estructura
type: docs
weight: 30
url: /es/python-net/setting-structure-elements-properties/
description: Aprenda a establecer propiedades de elementos de estructura en PDF etiquetados en Python con Aspose.PDF para Python a través de .NET, incluido el título, el idioma, el texto real, el texto alternativo y el texto de expansión.
lastmod: "2026-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Los elementos de estructura definen la jerarquía semántica de un documento PDF, como secciones, encabezados, párrafos o tablas. Al establecer propiedades como `title`, `language`, `alternative_text`, `actual_text` y `expansion_text`, mejora la accesibilidad y el significado semántico del PDF para tecnologías de asistencia como los lectores de pantalla.

El siguiente fragmento de código muestra cómo establecer las propiedades de los elementos de estructura de un documento Tagged PDF:

1. Cree un nuevo documento Tagged PDF.
1. Establecer los metadatos del documento.
1. Crear elementos de estructura.
1. Establecer propiedades de accesibilidad.
1. Guardar el PDF etiquetado.

```python
import aspose.pdf as ap


# region Setting Structure Elements Properties
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

## Configuración de elementos de estructura de texto

Para establecer elementos de estructura de texto de un Documento Tagged PDF, Aspose.PDF ofrece [Elemento de párrafo](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/paragraphelement/) clase. El siguiente fragmento de código muestra cómo establecer los elementos de estructura de texto de un Tagged PDF Document:

```python
import aspose.pdf as ap


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

## Configuración de elementos de estructura de bloque de texto

Este ejemplo de Python utiliza Aspose.PDF para crear un Tagged PDF que incluye una jerarquía estructurada de encabezados y un párrafo, mejorando las características semánticas y de accesibilidad del documento.

1. Cree un nuevo documento Tagged PDF.
1. Establecer los metadatos del documento.
1. Acceda al elemento de estructura raíz.
1. Crear encabezados de varios niveles.
1. Agregar encabezados a la estructura raíz.
1. Crear un elemento de párrafo.
1. Agregar párrafo a la estructura raíz.
1. Guardar el PDF etiquetado.

El siguiente fragmento de código muestra cómo establecer los elementos de estructura de bloque de texto de un Tagged PDF Document:

```python
import aspose.pdf as ap


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

## Configuración de elementos de estructura en línea

Crear elementos de texto en línea (/Span) dentro de encabezados y párrafos en un Tagged PDF usando Aspose.PDF for Python via .NET.

El siguiente fragmento de código muestra cómo establecer elementos de estructura en línea de un Documento Tagged PDF:

```python
import aspose.pdf as ap


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

## Configuración del nombre de etiqueta personalizado

Establecer nombres de etiquetas personalizados para los elementos de estructura y en línea en un PDF etiquetado usando Aspose.PDF para Python.

El siguiente fragmento de código muestra cómo establecer un nombre de etiqueta personalizado:

1. Cree un nuevo documento Tagged PDF.
1. Establecer los metadatos del documento.
1. Crear un elemento de sección.
1. Crea elementos de párrafo con etiquetas personalizadas.
1. Crear elementos span en línea con etiquetas personalizadas.
1. Guardar el PDF etiquetado.

```python
import aspose.pdf as ap


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

## Agregar Elemento de Estructura a los Elementos

**Esta función es compatible con la versión 19.4 o superior.**

Crear enlaces y elementos de imagen en un PDF etiquetado usando Aspose.PDF for Python via .NET.

El siguiente fragmento de código muestra cómo establecer elementos de estructura en un párrafo con texto de un documento Tagged PDF:

```python
import aspose.pdf as ap


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

## Configuración del elemento de enlace de estructura

Aspose.PDF for Python via .NET API también permite agregar elementos de estructura de enlace.

El siguiente fragmento de código muestra cómo agregar un elemento de estructura de enlace en un documento Tagged PDF:

```python
import aspose.pdf as ap


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

## Configuración del elemento de estructura de nota

Aspose.PDF for Python via .NET API también permite agregar [ElementoNota](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/noteelement/) en un documento PDF etiquetado. El siguiente fragmento de código muestra cómo agregar un elemento de nota en un documento PDF etiquetado:

```python
import aspose.pdf as ap


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

## Cómo establecer el idioma y el título

Aspose.PDF for Python via .NET API también permite establecer el idioma y el título de un documento según la especificación PDF/UA. El idioma puede configurarse tanto para todo el documento como para sus elementos estructurales separados. El siguiente fragmento de código muestra cómo establecer el idioma y el título en un Documento PDF etiquetado:

1. Cree un nuevo documento Tagged PDF.
1. Establecer el título del documento y el idioma.
1. Crear un elemento de encabezado.
1. Agregar párrafos con idiomas específicos.
1. Guardar el PDF etiquetado.

```python
import aspose.pdf as ap


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

## Temas relacionados de Tagged PDF

- [Crear Tagged PDF](/pdf/es/python-net/create-tagged-pdf/) para generar los elementos de estructura antes de actualizar sus propiedades.
- [Extraer contenido etiquetado de PDFs etiquetados](/pdf/es/python-net/extract-tagged-content-from-tagged-pdfs/) para inspeccionar los nodos de estructura existentes y los metadatos.
- [Trabajando con Table en Tagged PDFs](/pdf/es/python-net/working-with-table-in-tagged-pdfs/) si necesitas aplicar propiedades accesibles a las estructuras de tabla.
