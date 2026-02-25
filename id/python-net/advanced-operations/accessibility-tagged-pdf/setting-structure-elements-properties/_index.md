---
title: Mengatur Properti Elemen Struktur
linktitle: Mengatur Properti Elemen Struktur
type: docs
weight: 30
url: /id/python-net/setting-structure-elements-properties/
description: Anda dapat mengatur properti elemen struktur yang berbeda dalam dokumen PDF dengan Aspose.PDF untuk Python melalui .NET.
lastmod: "2025-06-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

Untuk mengatur properti elemen struktur dalam Dokumen PDF yang Ditandai, Aspose.PDF menawarkan metode [create_sect_element()](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/#methods) dan [create_header_element()](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/#methods) dari antarmuka [ITaggedContent](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/).

Potongan kode berikut menunjukkan cara mengatur properti elemen struktur dari Dokumen PDF yang Ditandai:

```python

    import aspose.pdf as ap

    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Properties StructTreeRootElement and RootElement are used for access to
        # StructTreeRoot object of pdf document and to root structure element (Document structure element).
        struct_tree_root_element = tagged_content.struct_tree_root_element
        root_element = tagged_content.root_element
```

## Mengatur Elemen Struktur Teks

Untuk mengatur elemen struktur teks dalam Dokumen PDF yang Ditandai, Aspose.PDF menawarkan kelas [ParagraphElement](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/paragraphelement/). Potongan kode berikut menunjukkan cara mengatur elemen struktur teks dari Dokumen PDF yang Ditandai:

```python

    import aspose.pdf as ap

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
        document.save(path_outfile)
```

## Mengatur Elemen Struktur Blok Teks

Contoh Python ini menggunakan Aspose.PDF untuk membuat PDF yang Ditandai yang mencakup hierarki terstruktur dari header dan paragraf, meningkatkan fitur semantik dan aksesibilitas dokumen.

Untuk mengatur elemen struktur blok teks dalam Dokumen PDF yang Ditandai, Aspose.PDF menawarkan kelas [HeaderElement](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/headerelement/) dan [ParagraphElement](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/paragraphelement/). Anda dapat menambahkan objek-objek kelas ini sebagai anak dari objek [StructureElement](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/structureelement/).
Potongan kode berikut menunjukkan cara mengatur elemen struktur blok teks dari Dokumen PDF yang Ditandai:

```python

    import aspose.pdf as ap

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
        p.set_text("P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
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
                    "vitae posuere risus odio id massa. Cras sed venenatis lacus.")
        root_element.append_child(p, True)
        # Save Tagged PDF Document
        document.save(path_outfile)
```

## Mengatur Elemen Struktur Inline

Untuk mengatur elemen struktur inline dalam Dokumen PDF yang Ditandai, Aspose.PDF menawarkan kelas [SpanElement](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/spanelement/) dan [ParagraphElement](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/paragraphelement/). Anda dapat menambahkan objek-objek kelas ini sebagai anak dari objek [StructureElement](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/structureelement/). Potongan kode berikut menunjukkan cara mengatur elemen struktur inline dari Dokumen PDF yang Ditandai:

```python

    import aspose.pdf as ap

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
        span_element_1.set_text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. ")
        paragraph_element.append_child(span_element_1, True)
        span_element_2 = tagged_content.create_span_element()
        span_element_2.set_text("Aenean nec lectus ac sem faucibus imperdiet. ")
        paragraph_element.append_child(span_element_2, True)
        span_element_3 = tagged_content.create_span_element()
        span_element_3.set_text("Sed ut erat ac magna ullamcorper hendrerit. ")
        paragraph_element.append_child(span_element_3, True)
        span_element_4 = tagged_content.create_span_element()
        span_element_4.set_text("Cras pellentesque libero semper, gravida magna sed, luctus leo. ")
        paragraph_element.append_child(span_element_4, True)
        span_element_5 = tagged_content.create_span_element()
        span_element_5.set_text("Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. ")
        paragraph_element.append_child(span_element_5, True)
        span_element_6 = tagged_content.create_span_element()
        span_element_6.set_text("Interdum et malesuada fames ac ante ipsum primis in faucibus. ")
        paragraph_element.append_child(span_element_6, True)
        span_element_7 = tagged_content.create_span_element()
        span_element_7.set_text(
            "Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. ")
        paragraph_element.append_child(span_element_7, True)
        span_element_8 = tagged_content.create_span_element()
        span_element_8.set_text(
            "Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. ")
        paragraph_element.append_child(span_element_8, True)
        span_element_9 = tagged_content.create_span_element()
        span_element_9.set_text(
            "Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ")
        paragraph_element.append_child(span_element_9, True)
        span_element_10 = tagged_content.create_span_element()
        span_element_10.set_text(
            "Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.")
        paragraph_element.append_child(span_element_10, True)

        # Save Tagged PDF Document
        document.save(path_outfile)
```

## Mengatur Nama Tag Kustom

Untuk mengatur nama tag kustom pada elemen-elemen Dokumen PDF yang Ditandai, Aspose.PDF menawarkan metode [set_tag](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/structureelement/#methods) dari kelas [StructureElement](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/structureelement/) untuk elemen.

Potongan kode berikut menunjukkan cara mengatur nama tag kustom:

```python

    import aspose.pdf as ap

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
        document.save(path_outfile)
```

## Menambahkan Elemen Struktur ke dalam Elemen

**Fitur ini didukung oleh versi 19.4 atau lebih tinggi.**

Untuk mengatur elemen struktur tautan dalam Dokumen PDF yang Ditandai, Aspose.PDF menawarkan metode [LinkElement](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/linkelement/) dari antarmuka [ITaggedContent](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/). Potongan kode berikut menunjukkan cara mengatur elemen struktur dalam paragraf dengan teks Dokumen PDF yang Ditandai:

```python

    import aspose.pdf as ap

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
            "The multiline link: Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google")
        link_element_4.alternate_descriptions = "Link to Google (multiline)"

        paragraph_element_5 = tagged_content.create_paragraph_element()
        root_element.append_child(paragraph_element_5, True)
        link_element_5 = tagged_content.create_link_element()
        paragraph_element_5.append_child(link_element_5, True)
        link_element_5.hyperlink = ap.WebHyperlink("http://google.com")
        figure_element_5 = tagged_content.create_figure_element()
        figure_element_5.set_image(path_imagefile, 1200)
        figure_element_5.alternative_text = "Google icon"
        link_layout_attributes = link_element_5.attributes.get_attributes(ap.logicalstructure.AttributeOwnerStandard.LAYOUT)
        placement_attribute = ap.logicalstructure.StructureAttribute(ap.logicalstructure.AttributeKey.PLACEMENT)
        placement_attribute.set_name_value(ap.logicalstructure.AttributeName.PLACEMENT_BLOCK)
        link_layout_attributes.set_attribute(placement_attribute)
        link_element_5.append_child(figure_element_5, True)
        link_element_5.alternate_descriptions = "Link to Google"

        # Save Tagged PDF Document
        document.save(path_outfile)

    # Check PDF/UA compliance
    with ap.Document(path_outfile) as document:
        is_pdf_ua_compliance = document.validate(path_logfile, ap.PdfFormat.PDF_UA_1)
        print(f"PDF/UA compliance: {is_pdf_ua_compliance}")
```

## Mengatur Elemen Struktur Tautan

Aspose.PDF untuk Python melalui .NET API juga memungkinkan Anda menambahkan elemen struktur tautan.

Potongan kode berikut menunjukkan cara menambahkan elemen struktur tautan ke dalam Dokumen PDF yang Ditandai:

```python

    import aspose.pdf as ap

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
        document.save(path_outfile)

    # Check PDF/UA compliance
    with ap.Document(path_outfile) as document:
        is_pdf_ua_compliance = document.validate(path_logfile, ap.PdfFormat.PDF_UA_1)
        print(f"PDF/UA compliance: {is_pdf_ua_compliance}")
```

## Mengatur Elemen Struktur Catatan

Aspose.PDF untuk Python melalui .NET API juga memungkinkan Anda menambahkan [NoteElement](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/noteelement/) dalam dokumen PDF yang ditandai. Potongan kode berikut menunjukkan cara menambahkan elemen catatan dalam Dokumen PDF yang Ditandai:

```python

    import aspose.pdf as ap

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
        document.save(path_outfile)

    # Check PDF/UA compliance
    with ap.Document(path_outfile) as document:
        is_pdf_ua_compliance = document.validate(path_logfile, ap.PdfFormat.PDF_UA_1)
        print(f"PDF/UA compliance: {is_pdf_ua_compliance}")
```

## Mengatur Bahasa dan Judul

Aspose.PDF untuk Python melalui .NET API juga memungkinkan Anda mengatur bahasa dan judul untuk sebuah dokumen sesuai spesifikasi PDF/UA. Bahasa dapat diatur baik untuk seluruh dokumen maupun untuk elemen struktural terpisahnya. Potongan kode berikut menunjukkan cara menetapkan bahasa dan judul dalam Dokumen PDF yang Ditandai:

```python

    import aspose.pdf as ap

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
        document.save(path_outfile)
```
