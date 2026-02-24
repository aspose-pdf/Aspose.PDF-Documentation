---
title: Buat Tagged PDF menggunakan Python
linktitle: Buat Tagged PDF
type: docs
weight: 10
url: /id/python-net/create-tagged-pdf/
description: Artikel ini menjelaskan cara membuat elemen struktur untuk dokumen Tagged PDF secara programatis menggunakan Aspose.PDF untuk Python via .NET.
lastmod: "2025-06-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

Membuat Tagged PDF berarti menambahkan (atau membuat) elemen tertentu ke dokumen yang akan memungkinkan dokumen divalidasi sesuai dengan persyaratan PDF/UA. Elemen-elemen ini biasanya disebut Elemen Struktur.

## Membuat Tagged PDF (Skenario Sederhana)

Untuk membuat elemen struktur dalam Dokumen Tagged PDF, Aspose.PDF menawarkan metode untuk membuat elemen struktur menggunakan antarmuka [ITaggedContent](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/). Contoh ini membuat dokumen Tagged PDF — PDF dengan struktur semantik, menjadikannya lebih mudah diakses dan sesuai dengan standar seperti PDF/UA.
Cuplikan kode berikut menunjukkan cara membuat Tagged PDF yang berisi 2 elemen: header dan paragraf.

```python

    import aspose.pdf as ap

    # Create PDF Document
    document = ap.Document()

    # Get Content for working with TaggedPdf
    tagged_content = document.tagged_content
    root_element = tagged_content.root_element

    # Set Title and Language for Document
    tagged_content.set_title("Tagged Pdf Document")
    tagged_content.set_language("en-US")
    main_header = tagged_content.create_header_element()
    main_header.set_text("Main Header")
    paragraph_element = tagged_content.create_paragraph_element()
    paragraph_element.set_text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. " +
                                "Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. " +
                                "Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet" +
                                "nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus." +
                                "Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat" +
                                "sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper" +
                                "pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus" +
                                "ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus," +
                                "ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.")
    root_element.append_child(main_header, True)
    root_element.append_child(paragraph_element, True)

    # Save Tagged PDF Document
    document.save(path_outfile)
```

```python

    import aspose.pdf as ap

    # Create PDF Document
    document = ap.Document()

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
    paragraph_with_quotes.structure_text_state.font = ap.text.FontRepository.find_font("Calibri")
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
        "lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit.")

    # Create Quote Element
    quote_element = tagged_content.create_quote_element()
    quote_element.set_text(
        "Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa.")
    quote_element.structure_text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC

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
    document.save(path_outfile)
```

Kami akan mendapatkan dokumen berikut setelah pembuatan:

![Dokumen Tagged PDF dengan 2 elemen - Header dan Paragraf](taggedpdf-01.png)

## Menata Struktur Teks

Tagged PDF adalah dokumen terstruktur yang menyediakan fitur aksesibilitas dan makna semantik pada konten.

Contoh ini membuat dokumen PDF dengan fitur aksesibilitas menggunakan struktur konten ber-tag. Ini menunjukkan cara membuat elemen paragraf dengan gaya khusus dan metadata dokumen yang tepat.

```python

    import aspose.pdf as ap

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
        document.save(path_outfile)
```

## Mengilustrasikan Elemen Struktur

Tagged PDF penting untuk kepatuhan aksesibilitas dan menyediakan konten terstruktur yang dapat diinterpretasikan dengan tepat oleh pembaca layar dan teknologi bantu lainnya. Cuplikan kode berikut menunjukkan cara membuat dokumen Tagged PDF dengan gambar tersemat:

1. Buat Tagged PDF dengan gambar.
1. Konfigurasikan dokumen.
1. Buat dan konfigurasikan gambar.
1. Atur posisi.
1. Simpan dokumen.

```python

    import aspose.pdf as ap

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
        figure1.set_image(path_imagefile, 300)
        # Adjust position
        position_settings = ap.tagged.PositionSettings()
        margin_info = ap.MarginInfo()
        margin_info.left = 50
        margin_info.top = 20
        position_settings.margin = margin_info
        figure1.adjust_position(position_settings)

        # Save Tagged PDF Document
        document.save(path_outfile)
```

## Validasi Tagged PDF

Aspose.PDF for Python via .NET menyediakan kemampuan untuk memvalidasi Dokumen PDF/UA Tagged PDF. Metode 'validate_tagged_pdf' memvalidasi dokumen PDF terhadap standar PDF/UA-1, yang merupakan bagian dari spesifikasi ISO 14289 untuk dokumen PDF yang dapat diakses. Ini memastikan bahwa PDF dapat diakses oleh pengguna dengan disabilitas dan teknologi bantu.

- Struktur Dokumen. Penandaan semantik yang tepat dan struktur logis.
- Teks Alternatif. Teks alt untuk gambar dan elemen non-teks.
- Urutan Membaca. Urutan logis untuk pembaca layar.
- Warna dan Kontras. Rasio kontras yang cukup.
- Formulir. Bidang dan label formulir yang dapat diakses.
- Navigasi. Bookmark dan struktur navigasi yang tepat.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        is_valid = document.validate(path_logfile, ap.PdfFormat.PDF_UA_1)
```

## Sesuaikan posisi Struktur Teks

Cuplikan kode berikut menunjukkan cara menyesuaikan posisi Struktur Teks dalam dokumen Tagged PDF:

```python

    import aspose.pdf as ap

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
        document.save(path_outfile)
```

## Membuat Tagged PDF secara otomatis dengan konversi PDF/UA-1

Aspose.PDF memungkinkan pembuatan otomatis markup struktur logis dasar saat mengonversi dokumen ke PDF/UA-1. Pengguna kemudian dapat meningkatkan secara manual struktur logis dasar ini, memberikan wawasan tambahan mengenai isi dokumen.

Cuplikan kode mengonversi dokumen PDF yang ada ke format PDF/UA-1, yang merupakan standar ISO (ISO 14289-1) yang memastikan dokumen PDF dapat diakses oleh pengguna dengan disabilitas. Konversi ini mencakup penandaan otomatis elemen dokumen untuk membuat struktur logis.

```python

    import aspose.pdf as ap

    # Create PDF Document
    with ap.Document(path_infile) as document:
        # Create conversion options
        options = ap.PdfFormatConversionOptions(path_logfile, ap.PdfFormat.PDF_UA_1, ap.ConvertErrorAction.DELETE)
        # Create auto-tagging settings
        # aspose.pdf.AutoTaggingSettings.default may be used to set the same settings as given below
        auto_tagging_settings = ap.AutoTaggingSettings()
        # Enable auto-tagging during the conversion process
        auto_tagging_settings.enable_auto_tagging = True
        # Use the heading recognition strategy that's optimal for the given document structure
        auto_tagging_settings.heading_recognition_strategy = ap.HeadingRecognitionStrategy.AUTO
        # Assign auto-tagging settings to be used during the conversion process
        options.auto_tagging_settings = auto_tagging_settings
        # During the conversion, the document logical structure will be automatically created
        document.convert(options)
        # Save PDF document
        document.save(path_outfile)
```
