---
title: Создать Tagged PDF на Python
linktitle: Создать Tagged PDF
type: docs
weight: 10
url: /python-net/create-tagged-pdf/
description: Узнайте, как создавать Tagged PDF документы на Python с Aspose.PDF for Python via .NET, включая PDF/UA Structure Elements, доступные Form, страницы TOC и автоматическое тегирование.
lastmod: "2026-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Создание Tagged PDF подразумевает добавление (или создание) определённых элементов в документ, которые позволят валидировать документ в соответствии с требованиями PDF/UA. Эти элементы часто называют Structure Elements.

## Создание Tagged PDF (Простой сценарий)

Чтобы создать структурные элементы в Tagged PDF Document, Aspose.PDF предлагает методы создания структурных элементов, используя [ITaggedContent](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/) интерфейса. Этот пример создаёт Tagged PDF документ — PDF с семантической структурой, делая его более доступным и соответствующим стандартам, таким как PDF/UA.
Следующий фрагмент кода демонстрирует, как создать Tagged PDF, содержащий 2 элемента: заголовок и абзац.

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

## Создание Tagged PDF (Продвинутый)

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

Мы получим следующий документ после создания:

![Tagged PDF документ с 2 элементами — Заголовок и Параграф](taggedpdf-01.png)

## Оформление структуры текста

Tagged PDFs — это структурированные документы, которые предоставляют функции доступности и придают содержимому семантическое значение.

Пример создаёт PDF‑документ с функциями доступности, используя структуру тегированного содержимого. Он демонстрирует, как создать элемент‑абзац с пользовательским стилизованием и правильными метаданными документа.

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

## Иллюстрирование Structure Elements

Тегированные PDF являются важными для соблюдения требований доступности и обеспечивают структурированное содержимое, которое может быть правильно интерпретировано скрин-ридерами и другими вспомогательными технологиями. Ниже приведён фрагмент кода, показывающий, как создать тегированный PDF‑документ с внедрённым изображением:

1. Создать Tagged PDF с изображением.
1. Настройте документ.
1. Создать и настроить рисунок.
1. Установить позиционирование.
1. Сохранить документ.

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

## Проверить Tagged PDF

Aspose.PDF for Python via .NET предоставляет возможность проверять PDF/UA Tagged PDF Document. Метод ‘validate_tagged_pdf’ проверяет PDF‑документы в соответствии со стандартом PDF/UA-1, который является частью спецификации ISO 14289 для доступных PDF‑документов. Это гарантирует, что PDF‑файлы доступны пользователям с ограниченными возможностями и вспомогательными технологиями.

- Структура документа. Правильная семантическая разметка и логическая структура.
- Альтернативный текст. Alt‑текст для изображений и нетекстовых элементов.
- Порядок чтения. Логическая последовательность для программ чтения с экрана.
- Цвет и контраст. Достаточные коэффициенты контраста.
- Формы. Доступные поля формы и ярлыки.
- Навигация. Правильные закладки и структура навигации.

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

## Отрегулировать позицию текстовой структуры

Следующий фрагмент кода показывает, как настроить позицию Text Structure в документе Tagged PDF:

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

## Преобразовать PDF в PDF/UA-1 с автоматическим тегированием

Этот фрагмент кода объясняет, как преобразовать стандартный PDF в файл, соответствующий требованиям PDF/UA-1 (Универсальная доступность), используя Aspose.PDF for Python via .NET.

PDF/UA гарантирует, что документы доступны пользователям с ограниченными возможностями и совместимы с вспомогательными технологиями, такими как программы чтения с экрана. При конвертации библиотека может автоматически генерировать логическое дерево структуры и применять семантические теги с помощью встроенного автотегирования и распознавания заголовков.

Настраивая PdfFormatConversionOptions и включая AutoTaggingSettings, вы можете эффективно преобразовывать существующие PDF в доступные документы без ручного редактирования структуры.

1. Загрузите исходный документ.
1. Создать параметры конвертации PDF/UA.
1. Включить автоматическое тегирование.
1. Настройте распознавание заголовков.
1. Присоедините конфигурацию тегирования к параметрам конверсии.
1. Запустите процесс конвертации.
1. Сохранить доступный PDF.

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

## Создать Tagged PDF с доступным полем подписи FormField

1. Создайте новый PDF‑документ.
1. Доступ к тегированному содержимому.
1. Создайте подпись Form field.
1. Добавьте поле в AcroForm.
1. Создайте элемент формы в структуре тегов.
1. Свяжите элемент Structure с полем формы.
1. Добавьте элемент Form в дерево логической структуры.
1. Сохранить документ.

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

## Создать Tagged PDF со страницей оглавления (TOC)

В этом примере показано, как создать тегированный PDF‑документ со структурированной страницей оглавления (TOC) с использованием Aspose.PDF for Python via .NET.

1. Создайте новый PDF‑документ.
1. Создайте отдельную страницу оглавления.
1. Создайте и зарегистрируйте элемент TOC в логическом дереве структуры.
1. Добавьте страницу содержания.
1. Создайте элемент заголовка.
1. Создать элемент /TOCI.
1. Свяжите заголовок с оглавлением.
1. Сохранить документ.

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

## Создайте продвинутый Tagged PDF с иерархическим оглавлением (TOC)

С помощью Aspose.PDF for Python via .NET вы можете создать расширенный, полностью размеченный PDF‑документ со структурированной и иерархической таблицей содержимого (TOC).

1. Создайте документ и включите Tagged content.
1. Добавьте и настройте страницу TOC.
1. Создайте элемент структуры /TOC.
1. Сделайте заголовок страницы оглавления ссылкой на элемент заголовка.
1. Добавьте страницу основного содержимого и первый заголовок.
1. Создайте запись TOC для заголовка.
1. Создайте вложенные подразделы со структурой списка.
1. Добавьте второй раздел верхнего уровня.
1. Сохранить документ.

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

## Связанные темы Tagged PDF

- [Извлечь помеченный контент из Tagged PDFs](/pdf/ru/python-net/extract-tagged-content-from-tagged-pdfs/) просмотреть дерево логической структуры после создания.
- [Настройка свойств Structure Elements](/pdf/ru/python-net/setting-structure-elements-properties/) для уточнения заголовков, языка, альтернативного текста и расширяющего текста.
- [Работа с таблицами в Tagged PDF](/pdf/ru/python-net/working-with-table-in-tagged-pdfs/) когда ваш доступный документ включает структурированные таблицы.
