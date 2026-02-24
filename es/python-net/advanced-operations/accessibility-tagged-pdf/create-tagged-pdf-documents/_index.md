---
title: Crear PDF etiquetado usando Python
linktitle: Crear PDF etiquetado
type: docs
weight: 10
url: /es/python-net/create-tagged-pdf/
description: Este artículo explica cómo crear los elementos de la estructura para un documento PDF etiquetado de forma programática usando Aspose.PDF para Python a través de .NET.
lastmod: "2025-06-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

Crear un PDF etiquetado significa añadir (o crear) ciertos elementos al documento que permitirán que el documento sea validado de acuerdo con los requisitos de PDF/UA. Estos elementos se llaman a menudo Elementos de Estructura.

## Crear PDF etiquetado (Escenario simple)

Para crear elementos de estructura en un documento PDF etiquetado, Aspose.PDF ofrece métodos para crear elementos de estructura usando la interfaz [ITaggedContent](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/). Este ejemplo crea un documento PDF etiquetado — un PDF con estructura semántica, haciéndolo más accesible y conforme a estándares como PDF/UA.
El siguiente fragmento de código muestra cómo crear un PDF etiquetado que contiene 2 elementos: encabezado y párrafo.

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

Obtendremos el siguiente documento después de la creación:

![Documento PDF etiquetado con 2 elementos - Encabezado y Párrafo](taggedpdf-01.png)

## Estilizando la estructura de texto

Los PDF etiquetados son documentos estructurados que proporcionan características de accesibilidad y significado semántico al contenido.

El ejemplo crea un documento PDF con características de accesibilidad utilizando una estructura de contenido etiquetado. Demuestra cómo crear un elemento de párrafo con estilo personalizado y metadatos de documento adecuados.

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

## Ilustrando los elementos de estructura

Los PDF etiquetados son esenciales para el cumplimiento de accesibilidad y proporcionan contenido estructurado que puede ser interpretado correctamente por lectores de pantalla y otras tecnologías de asistencia. El siguiente fragmento de código muestra cómo crear un documento PDF etiquetado con una imagen incrustada:

1. Crear PDF etiquetado con imagen.
1. Configurar documento.
1. Crear y configurar la figura.
1. Establecer la posición.
1. Guardar documento.

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

## Validar PDF etiquetado

Aspose.PDF para Python a través de .NET proporciona la capacidad de validar un documento PDF/UA etiquetado. El método 'validate_tagged_pdf' valida documentos PDF contra el estándar PDF/UA-1, que forma parte de la especificación ISO 14289 para documentos PDF accesibles. Esto garantiza que los PDFs sean accesibles para usuarios con discapacidades y tecnologías de asistencia.

- Estructura del documento. Etiquetado semántico adecuado y estructura lógica.
- Texto alternativo. Texto alternativo para imágenes y elementos no textuales.
- Orden de lectura. Secuencia lógica para lectores de pantalla.
- Color y contraste. Ratios de contraste suficientes.
- Formularios. Campos y etiquetas de formulario accesibles.
- Navegación. Marcadores y estructura de navegación adecuados.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        is_valid = document.validate(path_logfile, ap.PdfFormat.PDF_UA_1)
```

## Ajustar la posición de la estructura de texto

El siguiente fragmento de código muestra cómo ajustar la posición de la estructura de texto en el documento PDF etiquetado:

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

## Creación automática de PDF etiquetado con conversión a PDF/UA-1

Aspose.PDF permite la generación automática de marcado de estructura lógica básica al convertir un documento a PDF/UA-1. Los usuarios pueden luego mejorar manualmente esta estructura lógica básica, proporcionando información adicional sobre el contenido del documento.

El fragmento de código convierte un documento PDF existente al formato PDF/UA-1, que es una norma ISO (ISO 14289-1) que garantiza que los documentos PDF sean accesibles para usuarios con discapacidades. La conversión incluye el etiquetado automático de los elementos del documento para crear una estructura lógica.

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
