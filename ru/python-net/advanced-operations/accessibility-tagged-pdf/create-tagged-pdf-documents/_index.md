---
title: Создать помеченный PDF с помощью Python
linktitle: Создать помеченный PDF
type: docs
weight: 10
url: /ru/python-net/create-tagged-pdf/
description: В этой статье объясняется, как программно создавать элементы структуры для помеченного PDF-документа с использованием Aspose.PDF for Python via .NET.
lastmod: "2025-06-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

Создание помеченного PDF означает добавление (или создание) определенных элементов в документ, которые позволят документу быть проверенным в соответствии с требованиями PDF/UA. Эти элементы часто называют элементами структуры.

## Создание помеченного PDF (простой сценарий)

Чтобы создать элементы структуры в помеченном PDF-документе, Aspose.PDF предлагает методы создания элементов структуры с использованием интерфейса [ITaggedContent](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/). Этот пример создает помеченный PDF-документ — PDF с семантической структурой, делая его более доступным и соответствующим стандартам, таким как PDF/UA.
Следующий фрагмент кода показывает, как создать помеченный PDF, содержащий 2 элемента: заголовок и абзац.

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

Мы получим следующий документ после создания:

![PDF‑документ с 2 элементами — заголовок и абзац](taggedpdf-01.png)

## Стилизация текстовой структуры

Помеченные PDF — это структурированные документы, которые предоставляют функции доступности и семантическое значение содержимому.

В примере создается PDF-документ с функциями доступности, используя структуру помеченного содержимого. Он демонстрирует, как создать элемент абзаца с пользовательским оформлением и правильными метаданными документа.

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

## Иллюстрация элементов структуры

Помеченные PDF необходимы для соответствия требованиям доступности и предоставляют структурированное содержимое, которое может быть корректно интерпретировано программами чтения с экрана и другими вспомогательными технологиями. Следующий фрагмент кода показывает, как создать помеченный PDF-документ с вложенным изображением:

1. Создать помеченный PDF с изображением.
1. Настроить документ.
1. Создать и настроить рисунок.
1. Установить позиционирование.
1. Сохранить документ.

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

## Проверка помеченного PDF

Aspose.PDF for Python via .NET предоставляет возможность проверять помеченный PDF/UA документ. Метод 'validate_tagged_pdf' проверяет PDF-документы в соответствии со стандартом PDF/UA-1, который является частью спецификации ISO 14289 для доступных PDF-документов. Это гарантирует, что PDF доступны пользователям с ограниченными возможностями и вспомогательным технологиям.

- Структура документа. Правильное семантическое тегирование и логическая структура.
- Альтернативный текст. Alt‑текст для изображений и небуквенных элементов.
- Порядок чтения. Логическая последовательность для программ чтения с экрана.
- Цвет и контраст. Достаточные коэффициенты контрастности.
- Формы. Доступные поля форм и подписи.
- Навигация. Правильные закладки и структура навигации.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        is_valid = document.validate(path_logfile, ap.PdfFormat.PDF_UA_1)
```

## Регулировка положения текстовой структуры

Следующий фрагмент кода показывает, как отрегулировать позицию текстовой структуры в помеченном PDF-документе:

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

## Автоматическое создание помеченного PDF с конвертацией в PDF/UA-1

Aspose.PDF позволяет автоматически генерировать базовую разметку логической структуры при конвертации документа в PDF/UA-1. Пользователи могут затем вручную улучшать эту базовую логическую структуру, предоставляя дополнительные сведения о содержимом документа.

Этот фрагмент кода конвертирует существующий PDF-документ в формат PDF/UA-1, который является стандартом ISO (ISO 14289-1) и гарантирует, что PDF-документы доступны пользователям с ограниченными возможностями. Конверсия включает автоматическое тегирование элементов документа для создания логической структуры.

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
