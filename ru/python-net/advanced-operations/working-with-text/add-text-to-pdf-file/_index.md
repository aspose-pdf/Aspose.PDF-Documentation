---
title: Добавление текста в PDF
linktitle: Добавить текст в PDF
type: docs
weight: 10
url: /ru/python-net/add-text-to-pdf-file/
description: В этой статье описаны различные аспекты работы с текстом в Aspose.PDF. Узнайте, как добавить текст в PDF, добавить HTML‑фрагменты или использовать пользовательские шрифты OTF.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление текста в PDF с помощью Python
Abstract: В этой статье представлено подробное руководство по работе с PDF‑документами с использованием библиотеки Aspose.PDF в Python. Описаны различные методы добавления и форматирования текста, включая установку свойств текста, таких как размер шрифта, тип, цвет и позиционирование.
---

Это руководство объясняет, как добавить текстовое содержимое в PDF‑документы с помощью Aspose.PDF для Python через .NET. Вы изучите основные техники вставки текста — от размещения простого текстового фрагмента в определённой позиции до его стилизации (шрифт, размер, цвет, стиль), обработки языков с письмом справа налево (RTL), встраивания гиперссылок и работы с макетами абзацев, списками и эффектами прозрачности. Статья также охватывает продвинутые сценарии, такие как использование HTML‑или LaTeX‑фрагментов, пользовательских шрифтов и опций форматирования текста, например межстрочного и межсимвольного интервала.

Независимо от того, создаёте ли вы простые аннотации или сложные типографические макеты, этот ресурс предоставляет вам базовые строительные блоки для работы с текстом в PDF‑файлах с помощью Aspose.PDF.

## Базовая вставка текста

Aspose.PDF для Python через .NET предоставляет мощный и гибкий API для работы с текстом внутри PDF‑файлов.
Нужны ли вам простые статические метки, богато отформатированное содержание, многоязычный текст или интерактивные гиперссылки — набор инструментов позволяет выполнить всё это с помощью лаконичного кода на Python.

### Добавление текста: простой случай

Aspose.PDF для Python через .NET демонстрирует, как добавить простой текстовый фрагмент в определённую позицию на странице. Вы узнаете, как создать новый PDF‑документ, добавить страницу, вставить текст в заданные координаты и сохранить полученный файл.

1. Создайте новый объект [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Используйте `document.pages.add()`, чтобы создать новую пустую [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Создайте [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) с текстовым содержимым.
1. Установите позицию текста с помощью класса [`Position`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/position/). Если указать `Position`, текст будет располагаться в документе слева направо и смещён вниз.
1. Настройте внешний вид текста. Вы можете установить размер шрифта, цвет, стиль шрифта и многое другое через [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/).
1. Добавьте `TextFragment` в коллекцию абзацев страницы с помощью `page.paragraphs.add(text_fragment)`.
1. Сохраните документ.

Следующий фрагмент кода показывает, как добавить текст в существующий PDF‑файл:

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_simple_case(outfile):
    """
    Add simple text to a PDF document.
    Creates a new PDF document with a single page and adds a text fragment
    "Hello, Aspose!" at position (100, 600) on the page.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        >>> add_text_simple_case("output.pdf")
        # Creates a PDF file named "output.pdf" with "Hello, Aspose!" text
    """

    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

В этом примере кода используется TextFragment. Но вы также можете добавить текст на страницу PDF с помощью TextParagraph. Давайте рассмотрим различия.
Элемент **[TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)** представляет собой отдельный кусок текста. TextFragment — это единица текста, по сути одна строка, которую можно размещать, стилизовать и позиционировать независимо. Он идеален, когда нужно добавить простой, небольшой объём текста.

Элемент **[TextParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/)** представляет собой группу TextFragment‑ов. Он позволяет добавлять несколько строк текста. TextParagraph является контейнером или коллекцией из одного или более объектов TextFragment. Он идеален, когда необходимо сгруппировать несколько фрагментов — например, создать блок текста из нескольких строк, слов или форматированных элементов.
TextParagraph также управляет выравниванием текста, межстрочным интервалом и автоматической разметкой на странице. Использование красной линии возможно только с TextParagraph.

Для получения дополнительной информации о работе с текстом посетите разделы документации [Форматирование текста внутри PDF](/pdf/python-net/text-formatting-inside-pdf/) и [Извлечение текста из PDF с помощью Python](/pdf/python-net/extract-text-from-pdf/).

### Добавление текста с помощью TextParagraph

Aspose.PDF для Python через .NET может добавить абзац текста с помощью [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) и [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) с параметрами переноса.

1. Создайте новый [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) и пустую [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) с помощью `document.pages.add()`.
1. Считайте текст из файла или используйте текст по умолчанию.
1. Создайте [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) для добавления содержимого уровня абзаца с управлением разметкой и переносом.
1. Создайте [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) и задайте режим переноса (в примере используется `DISCRETIONARY_HYPHENATION`).
1. Создайте [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/), примените стили и добавьте фрагмент в абзац.
1. Добавьте абзац на страницу с помощью `TextBuilder`.
1. Сохраните документ.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_paragraph(outfile):
    """
    Add formatted text paragraph with indentation and wrapping to a PDF document.

    Creates a PDF document with a text paragraph that demonstrates advanced text
    formatting including first line indentation, text wrapping with discretionary
    hyphenation, and loading text content from an external file.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Attempts to load text from "lorem.txt" file in DATA_DIR
        - Falls back to default message if file doesn't exist
        - Uses Times New Roman font at 12pt size
        - First line indent: 20 points
        - Rectangle bounds: (80, 800, 400, 200)
        - Text wrapping: DISCRETIONARY_HYPHENATION mode for better line breaks

    Example:
        >>> add_text_paragraph("paragraph_text.pdf")
        # Creates a PDF with formatted paragraph text
    """
    document = ap.Document()
    page = document.pages.add()

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    if os.path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        text = "Lorem ipsum sample text not found."

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.first_line_indent = 20
    paragraph.rectangle = ap.Rectangle(80, 800, 400, 200, True)
    # paragraph.formatting_options.wrap_mode = TextFormattingOptions.WordWrapMode.BY_WORDS
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.DISCRETIONARY_HYPHENATION
    )

    fragment = ap.text.TextFragment(text)
    fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment.text_state.font_size = 12

    paragraph.append_line(fragment)
    builder.append_paragraph(paragraph)

    document.save(outfile)
```

![Добавление текста с помощью TextParagraph](text_paragraph.png)

### Добавление абзацев с отступами в PDF

Следующий фрагмент кода демонстрирует, как создать новый PDF‑документ и добавить два абзаца текста с различными стилями отступов:

- Первый абзац демонстрирует отступ первой строки (отступ только у первой строки).

- Второй абзац демонстрирует отступ последующих строк (все строки после первой имеют отступ).

Он использует классы 'TextParagraph', 'TextBuilder' и 'TextFragment' из Aspose.PDF для точного управления разметкой и форматированием.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_paragraphs_indents(output_file_name):
    """Add text with indents to a PDF document.
    Creates a PDF document with two text paragraphs demonstrating different
    indent styles. The first paragraph uses first line indent, while the
    second paragraph uses subsequent lines indent. Text content is loaded
    from a lorem.txt file if available, otherwise uses a fallback message.
    Args:
        output_file_name (str): The file path where the PDF document will be saved.
    Returns:
        None: The function saves the PDF document to the specified output file.
    Note:
        - Uses Times New Roman font at 12pt size
        - Text wrapping is set to wrap by words
        - First paragraph: 20pt first line indent, positioned at (80, 800, 300, 50)
        - Second paragraph: 20pt subsequent lines indent, positioned at (320, 800, 500, 50)
    """

    document = ap.Document()
    page = document.pages.add()

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    if os.path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        text = "Lorem ipsum sample text not found."

    fragment = ap.text.TextFragment(text)
    fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment.text_state.font_size = 12

    builder = ap.text.TextBuilder(page)
    paragraph1 = ap.text.TextParagraph()
    paragraph1.first_line_indent = 20
    paragraph1.rectangle = ap.Rectangle(80, 800, 300, 50, True)
    paragraph1.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    paragraph1.append_line(fragment)
    builder.append_paragraph(paragraph1)

    paragraph2 = ap.text.TextParagraph()
    paragraph2.subsequent_lines_indent = 20
    paragraph2.rectangle = ap.Rectangle(320, 800, 500, 50, True)
    paragraph2.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    paragraph2.append_line(fragment)
    builder.append_paragraph(paragraph2)
    document.save(output_file_name)
```

### Добавление новой строки текста в PDF

Aspose.PDF для Python через .NET позволяет вставлять многострочный текст в PDF‑документ с помощью классов TextFragment, TextParagraph и TextBuilder.

1. Создайте новый документ.
1. Определите TextFragment, содержащий символ новой строки.
1. Установите стиль текста.
1. Добавьте фрагмент в абзац.
1. Установите позицию абзаца.
1. Отобразите абзац на странице.
1. Сохраните документ.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_new_line(output_file):
    """Add a new line of text to a PDF document."""
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Initialize new TextFragment with text containing required newline markers
    text_fragment = ap.text.TextFragment("Applicant Name: " + os.linesep + " Joe Smoe")

    # Set text fragment properties if necessary
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red

    # Create TextParagraph object
    par = ap.text.TextParagraph()

    # Add new TextFragment to paragraph
    par.append_line(text_fragment)

    # Set paragraph position
    par.position = ap.text.Position(100, 600)

    # Create TextBuilder object
    text_builder = ap.text.TextBuilder(page)

    # Add the TextParagraph using TextBuilder
    text_builder.append_paragraph(par)

    # Save PDF document
    document.save(output_file)
```

### Определение разрывов строк и регистрация уведомлений в PDF

Показывается, как создать PDF‑документ, содержащий несколько текстовых фрагментов, и включить журналирование уведомлений Aspose.PDF для отслеживания событий разметки — таких как разрывы строк и перенос текста — во время рендеринга.

1. Создайте новый PDF‑документ.
1. Включите журналирование уведомлений.
1. Используйте document.pages.add() для создания первой страницы.
1. Добавьте несколько текстовых фрагментов.
1. Используйте page.paragraphs.add(text) для отображения каждого текстового фрагмента.
1. Сохраните документ.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def determine_line_break(output_file):
    """Create a PDF document with multiple text fragments and log notifications."""
    # Create PDF document
    document = ap.Document()

    # Enable notification logging
    document.enable_notification_logging = True

    page = document.pages.add()

    for i in range(4):
        text = ap.text.TextFragment(
            "Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, "
            "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
            "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
            "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
            "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
            "culpa qui officia deserunt mollit anim id est laborum."
        )
        text.text_state.font_size = 20
        page.paragraphs.add(text)

    # Save PDF document
    document.save(output_file)

    notifications = document.pages[1].get_notifications()
    print(notifications)
```

### Динамическое измерение ширины текста в PDF

Динамически измеряйте ширину символов и строк в определённом шрифте с помощью Aspose.PDF for Python via .NET. Используются методы 'Font.measure_string()' и 'TextState.measure_string()', чтобы убедиться, что измеренные ширины строк согласованы и точны.

1. Используйте 'FontRepository.find_font()', чтобы получить объект шрифта Arial из репозитория.
1. Создайте объект TextState для управления свойствами шрифта.
1. Измерьте отдельные символы.
1. Сравните результаты обоих методов для всех символов от 'A' до 'z'.
1. Убедитесь, что оба подхода измерения дают одинаковые результаты.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_text_width_dynamically(output_file):

    font = ap.text.FontRepository.find_font("Arial")
    ts = ap.text.TextState()
    ts.font = font
    ts.font_size = 14

    if math.fabs(font.measure_string("A", 14) - 9.337) > 0.001:
        print("Unexpected font string measure!")

    if math.fabs(ts.measure_string("z") - 7.0) > 0.001:
        print("Unexpected font string measure!")

    c_code = ord("A")
    while c_code <= ord("z"):
        c = chr(c_code)

        fn_measure = font.measure_string(str(c), 14)
        ts_measure = ts.measure_string(str(c))

        if math.fabs(fn_measure - ts_measure) > 0.001:
            print("Font and state string measuring doesn't match!")

        c_code += 1
```

### Добавление текста с гиперссылками

Добавьте кликабельные гиперссылки в текст PDF с помощью Aspose.PDF for Python via .NET. Наша библиотека демонстрирует, как добавить несколько текстовых сегментов в один TextFragment, применить гиперссылку к конкретному сегменту и стилизовать отдельные сегменты текста (например, цвет, курсивный шрифт).

1. Создайте новый документ и страницу, используя 'Document()', и выполните 'document.pages.add()', чтобы добавить пустую страницу.
1. Создайте TextFragment.
1. Добавьте несколько объектов TextSegment. Каждый сегмент может иметь собственное содержание и стилизацию. Например, обычный текст или текст с гиперссылкой.
1. Примените гиперссылку к сегменту. Создайте объект WebHyperlink с нужным URL.
1. Оформите сегмент. Настройте цвет, стиль шрифта, размер и т. д., используя text_state.
1. Добавьте фрагмент на страницу, используя 'page.paragraphs.add()'.
1. Сохраните PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_with_hyperlink(outfile):
    """
    Add text with embedded hyperlinks to a PDF document.

    Creates a PDF document with a text fragment containing multiple segments,
    including one with a hyperlink to Aspose. Demonstrates how to create
    clickable links within PDF text content with different formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates 4 text segments within a single text fragment
        - One segment contains a hyperlink to "https://products.aspose.com/pdf"
        - Hyperlinked text is styled in blue italic font
        - Other segments are regular text without links

    Example:
        >>> add_text_with_hyperlink("hyperlink_text.pdf")
        # Creates a PDF with clickable Aspose link in the text
    """

    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment(
        "Sample Text Fragment"
    )

    segment = ap.text.TextSegment(" ... Text Segment 1...")
    fragment.segments.append(segment)

    segment = ap.text.TextSegment("Link to Aspose")
    fragment.segments.append(segment)
    segment.hyperlink = ap.WebHyperlink("https://products.aspose.com/pdf")
    segment.text_state.foreground_color = ap.Color.blue
    segment.text_state.font_style = ap.text.FontStyles.ITALIC

    segment = ap.text.TextSegment("TextSegment without hyperlink")
    fragment.segments.append(segment)

    page.paragraphs.add(fragment)
    document.save(outfile)
```

![Текстовый фрагмент, отображаемый в PDF, показывающий смешанное содержание с Sample Text Fragment, затем Text Segment 1, затем синий гиперссылочный текст Link to Aspose (ссылка https://products.aspose.com/pdf), и завершающий TextSegment без гиперссылки обычным черным текстом](hyperlink_text.png)

### Добавление текста справа налево (RTL) в PDF‑документ

RTL (Right To Left, справа налево) — это свойство, указывающее направление написания текста, когда текст пишется справа налево.
Aspose.PDF for Python via .NET демонстрирует, как добавить текст справа налево (RTL), например арабский или иврит, в PDF‑документ.

1. Создайте новый документ и страницу, используя 'Document()', и выполните 'document.pages.add()', чтобы добавить пустую страницу.
1. Создайте TextFragment с RTL‑содержимым. Вставьте ваш арабский, ивритный или другой RTL‑текст в качестве содержимого фрагмента.
Установите шрифт и стили. Выберите шрифт, поддерживающий RTL‑скрипт (например, Tahoma, Arial Unicode MS). При необходимости задайте font_size и foreground_color.
1. Установите горизонтальное выравнивание по правому краю с помощью 'text_fragment.horizontal_alignment'.
1. Добавьте текстовый фрагмент на страницу.
1. Сохраните PDF‑документ.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_with_rtl_text(outfile):
    """
    Add right-to-left (RTL) text to a PDF document.

    Creates a PDF document with Arabic text that demonstrates right-to-left text
    rendering and alignment. The text uses the Tahoma font which supports Arabic
    characters and is aligned to the right side of the page.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses Tahoma font at 14pt size for proper Arabic character support
        - Text color is set to blue
        - Horizontal alignment is set to RIGHT for proper RTL display
        - The Arabic text describes Nasreddin Hodja, a folklore character

    Example:
        >>> add_text_with_rtl_text("arabic_text.pdf")
        # Creates a PDF with right-to-left Arabic text
    """

    document = ap.Document()
    page = document.pages.add()
    # Styled text fragment
    text_fragment = ap.text.TextFragment(
        "يعتبر خوجا نصر الدين شخصية فولكلورية من الشرق الإسلامي وبعض شعوب البحر الأبيض المتوسط ​​والبلقان، وهو بطل القصص والحكايات القصيرة الفكاهية والساخرة، وأحيانًا الحكايات اليومية."
    )
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Tahoma")
    text_fragment.text_state.font_size = 14
    text_fragment.text_state.foreground_color = ap.Color.blue
    text_fragment.horizontal_alignment = ap.HorizontalAlignment.RIGHT

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

![Текст справа налево](rtl_text.png)

## Стилизация текста

### Добавление текста со стилями шрифта

Это более продвинутый пример, демонстрирующий стилизацию текста, настройку шрифта и смешанный формат текста (с использованием нижних индексов). Aspose.PDF объясняет, как применять свойства шрифта, такие как семейство, размер, цвет, полужирный, курсив и подчеркивание, к текстовому фрагменту.
Кроме того, этот фрагмент кода показывает, как использовать несколько текстовых сегментов в одном фрагменте для создания сложных текстовых выражений — например, включая символы нижних или верхних индексов, часто требуемые в формулах или научных обозначениях.

1. Создайте новый документ и страницу, используя 'Document()', и выполните 'document.pages.add()', чтобы добавить пустую страницу.
1. Создайте TextFragment для простого стилизованного текста.
1. Определите содержание текста.
1. Установите позицию, используя координаты Position(x, y).
1. Применяйте стилизацию через свойство 'text_state' — шрифт, font_size, foreground_color, font_style, underline.
1. Создайте сложное выражение с несколькими объектами TextSegment. Каждый TextSegment представляет часть текста, которой можно задать собственный стиль. Это позволяет формировать выражения, такие как математические или химические формулы.
1. Определите несколько объектов TextState. Один для основного текста (text_state_letters). Другой для нижних или верхних индексов (text_state_index).
1. Объедините текстовые сегменты. Добавляйте каждый сегмент в 'TextFragment' с помощью 'segments.append()'.
1. Добавьте оба текстовых объекта на страницу. Используйте 'page.paragraphs.add()' для размещения их в документе.
1. Сохраните окончательный документ.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_with_font_styling(outfile):
    """
    Add styled text fragments to a PDF document.
    Creates a new PDF document with a single page and adds a styled text fragment
    "Hello, Aspose!" at position (100, 600) and a formula with styled segments at position (100, 500).
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        >>> add_text_with_font_styling("styled_text.pdf")
        # Creates a PDF file named "styled_text.pdf" with styled text and a formula
    """

    document = ap.Document()
    page = document.pages.add()

    # Initialize an empty TextFragment to build a formula using segments
    formula = ap.text.TextFragment()
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.text_state.foreground_color = ap.Color.blue
    text_fragment.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    text_fragment.text_state.underline = True
    text_fragment.horizontal_alignment = ap.HorizontalAlignment.LEFT

    text_state_letters = ap.text.TextState()
    text_state_letters.font = ap.text.FontRepository.find_font("Arial")
    text_state_letters.font_size = 14
    text_state_letters.foreground_color = ap.Color.blue
    text_state_letters.font_style = ap.text.FontStyles.BOLD

    text_state_index = ap.text.TextState()
    text_state_index.font = ap.text.FontRepository.find_font("Arial")
    text_state_index.font_size = 14
    text_state_index.foreground_color = ap.Color.dark_red
    # text_state_index.superscript = True
    text_state_index.subscript = True

    position = ap.text.Position(100, 500)

    # Helper function to add segments
    def add_segment(text, state):
        seg = ap.text.TextSegment(text)
        seg.text_state = state
        seg.position = position
        formula.segments.append(seg)

    add_segment("S = a", text_state_letters)
    add_segment("2n", text_state_index)
    add_segment(" + a", text_state_letters)
    add_segment("2n+1", text_state_index)
    add_segment(" + a", text_state_letters)
    add_segment("2n+2", text_state_index)
    formula.horizontal_alignment = ap.HorizontalAlignment.LEFT

    page.paragraphs.add(text_fragment)
    page.paragraphs.add(formula)
    document.save(outfile)
```

![Текстовый фрагмент отображён с синим курсивным шрифтом Arial, содержащим текст Hello, Aspose! и за ним математической формулой S = a subscript 2n + a subscript 2n+1 + a subscript 2n+2 с синим основным текстом и красным форматированием нижнего индекса](styled_text.png)

## Добавить прозрачный текст

Добавьте полупрозрачные фигуры и текст в PDF‑документ с помощью Aspose.PDF для Python.
Он создаёт цветной прямоугольник с частичной непрозрачностью и накладывает TextFragment с прозрачным цветом переднего плана.

1. Инициализируйте объект Document и добавьте пустую страницу для рисования содержимого.
1. Используйте 'ap.drawing.Graph' для создания холста, позволяющего рисовать фигуры.
1. Добавьте прямоугольник с полупрозрачным заполнением.
1. Предотвратите сдвиг позиции холста.
1. Добавьте холст на страницу. Вставьте графические фигуры в коллекцию абзацев страницы.
1. Создайте прозрачный текстовый фрагмент.
1. Вставьте текстовый фрагмент в коллекцию абзацев страницы.
1. Сохраните PDF‑документ.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_transparent(outfile):
    """
    Add transparent text over a semi-transparent background to a PDF document.

    Creates a PDF document with a semi-transparent filled rectangle as background
    and transparent green text overlaid on top. This demonstrates how to create
    transparency effects in PDF documents using ARGB color values.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Background rectangle: 128 alpha, light purple color (0xC5, 0xB5, 0xFF)
        - Text transparency: 30 alpha, green color (0, 255, 0)
        - The canvas is set to not change position to prevent layout shifts

    Example:
        >>> add_text_transparent("transparent_output.pdf")
        # Creates a PDF with transparent text effects
    """

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create Graph object
    canvas = ap.drawing.Graph(100.0, 400.0)

    # Create rectangle with semi-transparent fill
    rect = ap.drawing.Rectangle(100, 100, 400, 400)
    rect.graph_info.fill_color = ap.Color.from_argb(128, 0xC5, 0xB5, 0xFF)
    canvas.shapes.add(rect)

    # Prevent position shift
    canvas.is_change_position = False
    page.paragraphs.add(canvas)

    # Create transparent text
    text = ap.text.TextFragment(
        "This is the transparent text. "
        "This is the transparent text. "
        "This is the transparent text."
    )
    text.text_state.foreground_color = ap.Color.from_argb(30, 0, 255, 0)
    page.paragraphs.add(text)

    document.save(outfile)
```

### Добавить невидимый текст в PDF

В этом примере показано, как создать PDF‑документ, содержащий как видимый, так и невидимый текст. Невидимый текст остаётся частью структуры документа, но скрыт от просмотра, что делает его полезным для встраивания метаданных, тегов доступности или индексируемого контента без изменения макета.

1. Создайте PDF‑документ и страницу.
1. Создайте текстовый фрагмент с повторяющимся видимым содержимым.
1. Добавьте второй текстовый фрагмент и пометьте его как невидимый.
1. Сохраните документ.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_invisible(outfile):
    """
    Creates a PDF document with both visible and invisible text.
    This function generates a PDF file containing two text fragments:
    one visible text that will be displayed normally, and one invisible
    text that will be hidden from view but still present in the document.
    Args:
        outfile (str): The file path where the PDF document will be saved.
    Returns:
        None: The function saves the PDF to the specified file path.
    Example:
        add_text_invisible("output.pdf")
    """

    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Add visible text
    text1 = ap.text.TextFragment(
        "This is the visible text. "
        "This is the visible text. "
        "This is the visible text."
    )
    page.paragraphs.add(text1)

    # Create transparent text
    text2 = ap.text.TextFragment(
        "This is the invisible text. "
        "This is the invisible text. "
        "This is the invisible text."
    )
    text2.text_state.invisible = True
    page.paragraphs.add(text2)

    document.save(outfile)
```

### Добавить текст с оформлением границы в PDF

Библиотека Aspose.PDF демонстрирует, как создать PDF‑документ с текстовым фрагментом, оформленным видимой границей. Метод применяет цвета фона и переднего плана, настройки шрифта и обводку (границу) вокруг прямоугольника текста для усиления визуального акцента.

1. Создайте PDF‑документ и страницу.
1. Создайте и разместите текстовый фрагмент. Добавьте текстовый фрагмент с сообщением и задайте его позицию.
1. Примените стилизацию текста. Установите шрифт Times New Roman, размер 12. Примените светло-серый фон и красный цвет переднего плана (текста).
1. Настройте оформление границы.
1. Добавьте текст на страницу. Используйте TextBuilder для добавления стилизованного текста на страницу.
1. Сохраните документ.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_border(output_file_name):
    """
    Add text with border styling to a PDF document.

    Creates a PDF document with a text fragment that has border styling applied.
    The text includes background color, foreground color, and a configurable
    border (stroke) around the text rectangle.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "This is sample text with border."
        - Font: Times New Roman, 12pt
        - Background: Light gray
        - Foreground: Red text
        - Border: Dark red stroke around text rectangle
        - Position: (10, 700)
        - Border is only visible when draw_text_rectangle_border is True

    Example:
        >>> add_text_border("bordered_text.pdf")
        # Creates a PDF with bordered text styling
    """
    # Create PDF document
    document = ap.Document()
    # Get particular page
    page = document.pages.add()
    # Create text fragment
    text_fragment = ap.text.TextFragment("This is sample text with border.")
    text_fragment.position = ap.text.Position(10, 700)

    # Set text properties
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red
    # Set StrokingColor property for drawing border (stroking) around text rectangle.
    # Note: This only affects the border if draw_text_rectangle_border is set to True.
    text_fragment.text_state.stroking_color = ap.Color.dark_red
    # Enable drawing of the text rectangle border
    text_fragment.text_state.draw_text_rectangle_border = True

    text_builder = ap.text.TextBuilder(page)
    text_builder.append_text(text_fragment)

    # Save PDF document
    document.save(output_file_name)
```

### Добавить текст с зачеркиванием в PDF

Добавьте форматирование зачеркивания (strikeout) к текстовому фрагменту в PDF‑документе. Текст с зачеркиванием полезен для указания удалений, исправлений или акцента в аннотированных документах.

1. Создайте новый документ и страницу с помощью 'Document()', и 'document.pages.add()' для добавления пустой страницы.
1. Создайте и оформите текстовый фрагмент.
1. Примените цвет и форматирование зачеркивания. Установите светло-серый фон, красный цвет текста и включите зачеркивание.
1. Разместите текст.
1. Используйте 'TextBuilder' для добавления стилизованного текста на страницу.
1. Сохраните документ.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_strikeout_text(output_file_name):
    """
    Add text with strikeout (strikethrough) formatting to a PDF document.

    Creates a PDF document with a text fragment that has strikeout formatting applied.
    The text appears with a line through it, along with additional styling including
    background color, foreground color, and bold font style.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "This is sample strikeout text."
        - Font: Times New Roman, 12pt, Bold
        - Background: Light gray
        - Foreground: Red text
        - Strikeout: Enabled (line through text)
        - Position: (100, 600)

    Example:
        >>> add_strikeout_text("strikeout_text.pdf")
        # Creates a PDF with strikethrough text formatting
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create text fragment
    text_fragment = ap.text.TextFragment("This is sample strikeout text.")
    # Set text properties
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red
    text_fragment.text_state.strike_out = True
    text_fragment.text_state.font_style = ap.text.FontStyles.BOLD
    text_fragment.position = ap.text.Position(100, 600)

    # Create TextBuilder object
    text_builder = ap.text.TextBuilder(page)
    text_builder.append_text(text_fragment)

    # Save PDF document
    document.save(output_file_name)
```

## Продвинутые цветовые эффекты

### Применение аксиального градиента к тексту в PDF

Aspose.PDF для Python через .NET демонстрирует, как применить линейный градиент к тексту в PDF‑документе. Аксиальный градиент плавно переходит от красного к синему по всей длине текста, создавая визуально эффектный заголовок. Эта техника идеальна для стилизованных названий, брендинга или декоративных элементов в макетах PDF‑документов.

1. Инициализируйте новый документ и добавьте пустую страницу.
1. Создайте и оформите текстовый фрагмент. Добавьте заголовок, задайте позицию, шрифт и размер.
1. Примените аксиальное градиентное затенение с помощью 'GradientAxialShading'. Установите цвет переднего плана, используя GradientAxialShading от красного к синему.
1. Добавьте оформление подчеркивания.
1. Вставьте стилизованный текстовый фрагмент на страницу.
1. Сохраните документ.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def apply_gradient_axial_shading_to_text(output_file_name):
    """
    Apply axial gradient shading to text in a PDF document.

    Creates a PDF document with large title text that has an axial (linear) gradient
    effect applied. The gradient transitions from red to blue in a linear fashion
    across the text. This demonstrates advanced text styling with gradient effects.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "PDF TITLE"
        - Font: Arial Bold, 36pt
        - Position: (100, 600)
        - Gradient: Linear gradient from red to blue
        - Additional styling: Underlined text
        - Uses GradientAxialShading for linear gradient effect

    Example:
        >>> apply_gradient_axial_shading_to_text("gradient_axial.pdf")
        # Creates a PDF with linear gradient text effect
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("PDF TITLE")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font_size = 36
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial Bold")

    text_fragment.text_state.foreground_color = ap.Color()
    text_fragment.text_state.foreground_color.pattern_color_space = (
        ap.drawing.GradientAxialShading(ap.Color.red, ap.Color.blue)
    )
    text_fragment.text_state.underline = True

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

### Применение радиального градиента к тексту в PDF

Радиальный градиент создаёт круглой переход цвета, распространяющийся от центра текста наружу, предлагая визуально динамичную вариацию стиля для заголовков, подзаголовков или декоративных элементов.

1. Инициализировать новый документ и добавить пустую страницу.
1. Создать и оформить фрагмент текста. Добавить заголовок, задать позицию, шрифт и размер.
1. Применить радиальный градиент с помощью 'GradientRadialShading'. Установить цвет переднего плана, используя GradientRadialShading от красного к синему.
1. Добавить подчеркивание.
1. Вставить оформленный фрагмент текста на страницу.
1. Сохранить документ.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def apply_gradient_radial_shading_to_text(output_file_name):
    """
    Apply radial gradient shading to text in a PDF document.

    Creates a PDF document with large title text that has a radial (circular) gradient
    effect applied. The gradient radiates from the center outward, transitioning from
    red to blue. This demonstrates advanced text styling with radial gradient effects.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Text: "PDF TITLE"
        - Font: Arial Bold, 36pt
        - Position: (100, 600)
        - Gradient: Radial gradient from red to blue
        - Additional styling: Underlined text
        - Uses GradientRadialShading for circular gradient effect

    Example:
        >>> apply_gradient_radial_shading_to_text("gradient_radial.pdf")
        # Creates a PDF with radial gradient text effect
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("PDF TITLE")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font_size = 36
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial Bold")

    # Apply radial gradient shading (red to blue)
    text_fragment.text_state.foreground_color = ap.Color()
    text_fragment.text_state.foreground_color.pattern_color_space = (
        ap.drawing.GradientRadialShading(ap.Color.red, ap.Color.blue)
    )
    text_fragment.text_state.underline = True

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![Применить радиальное градиентное затенение](gradient_radial_shading.png)

## HTML и LaTeX фрагменты

### Добавить HTML‑текст в PDF‑документ

Библиотека Aspose.PDF for Python via .NET позволяет вставлять контент в формате HTML в PDF‑документ с помощью класса HtmlFragment. Используя HTML‑теги, можно напрямую отобразить стилизованный, структурированный или похожий на формулу текст в PDF.

1. Создать новый документ и страницу с помощью 'Document()', и 'document.pages.add()', чтобы добавить пустую страницу.
1. Создать экземпляр класса HtmlFragment и передать в него вашу HTML‑строку в качестве параметра.
1. Добавить фрагмент на страницу с помощью 'page.paragraphs.add()', чтобы вставить HTML‑контент.
1. Сохранить PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_html_fragment(outfile):
    """
    Add HTML fragment with mathematical notation to a PDF document.

    Creates a PDF document containing an HTML fragment that displays mathematical
    notation using HTML tags including subscript and superscript elements.
    This demonstrates how to embed formatted HTML content directly into PDF.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <pre> tags to preserve formatting
        - Includes <sub> for subscript (2n) and <sup> for superscript (2)
        - Formula displayed: S=a₂ₙ+a²
        - HTML is rendered as formatted content within the PDF

    Example:
        >>> add_text_html_fragment("html_math.pdf")
        # Creates a PDF with HTML mathematical notation
    """

    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.HtmlFragment("<pre>S=a<sub>2n</sub>+a<sup>2</sup><pre>")

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

![Добавить HTML‑текст в PDF‑документ](html_fragment.png)

### Добавить оформленный HTML‑фрагмент с различным форматированием в PDF‑документ

Мы можем определить HTML‑фрагмент и задать стиль текста непосредственно с помощью HTML‑тегов. Встроить оформленный HTML‑контент в PDF‑документ. Этот фрагмент кода создаёт новый PDF‑файл, добавляет страницу, вставляет HTML‑фрагмент с различными элементами форматирования (заголовки, абзацы, ссылки и встроенные стили) и сохраняет результат по указанному пути.

1. Инициализировать новый объект Document для представления PDF.
1. Добавить пустую страницу в документ, где будет размещён HTML‑контент.
1. Подготовить HTML‑контент. HTML‑строка содержит заголовок h1, абзац зелёного цвета с жирным, курсивным и подчёркнутым текстом, а также гиперссылку на веб‑сайт с увеличенным размером шрифта.
1. Создать HTML‑фрагмент. Обернуть HTML‑строку в объект HtmlFragment.
1. Вставить HTML на страницу. Добавить HTML‑фрагмент в коллекцию абзацев страницы, отобразив HTML как нативный PDF‑контент.
1. Сохранить документ.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_html_fragment(outfile):
    """
    Add styled HTML fragment with various formatting to a PDF document.

    Creates a PDF document containing rich HTML content including headings,
    paragraphs with inline formatting, colored text, and hyperlinks.
    Demonstrates comprehensive HTML rendering capabilities in PDF.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Includes HTML heading (h1) with blue color styling
        - Contains paragraph with bold, italic, and underlined text
        - Features green-colored paragraph text
        - Includes styled hyperlink to Aspose website
        - All HTML styling is preserved in the PDF output

    Example:
        >>> add_html_fragment("rich_html.pdf")
        # Creates a PDF with various HTML formatting elements
    """

    document = ap.Document()
    page = document.pages.add()
    html_content = """
        <h1 style='color:blue;'>Hello, Aspose!</h1>
        <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
        <p style='color:green;'>This paragraph is green.</p>
        <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
    """
    html_fragment = ap.HtmlFragment(html_content)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![Добавить HTML‑контент в PDF‑документ](html_content.png)

### Добавить HTML‑фрагмент с переопределённым состоянием текста

Как мы увидели в предыдущем примере, можно задавать стили непосредственно в HTML‑коде. Это имеет свои преимущества, но также и недостатки. Представьте, что мы работаем с HTML заказчика и хотим унифицировать внешний вид нашего результата.
В этом случае мы можем переопределить стили заказчика, используя наш собственный TextState, как показано в следующем примере.

1. Создать новый документ и страницу с помощью 'Document()', и 'document.pages.add()', чтобы добавить пустую страницу.
1. Подготовить HTML‑контент. HTML‑строка содержит заголовок h1 с шрифтом Verdana, абзац зелёного цвета с жирным, курсивным и подчёркнутым текстом, а также гиперссылку на веб‑сайт с большим размером шрифта.
1. Создать HTML‑фрагмент. Обернуть HTML‑строку в объект HtmlFragment.
1. Переопределить форматирование текста. Создать объект TextState и задать шрифт, размер шрифта и цвет текста.
1. Добавить HTML‑фрагмент в коллекцию абзацев страницы.
1. Сохранить документ.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_html_fragment_override_text_state(outfile):
    """
    Add HTML fragment with overridden text styling to a PDF document.

    Creates a PDF document with HTML content where the default text styling
    is overridden using TextState properties. This demonstrates how to apply
    global text formatting that supersedes HTML styling for consistent appearance.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - HTML includes heading, paragraphs, and links with original styling
        - TextState override applies: Arial font, 14pt size, red color
        - Override styling takes precedence over HTML inline styles
        - Useful for enforcing consistent document-wide text appearance
        - Original HTML styling is replaced by the TextState properties

    Example:
        >>> add_html_fragment_override_text_state("html_override.pdf")
        # Creates a PDF where HTML styling is overridden with red Arial text
    """

    document = ap.Document()
    page = document.pages.add()
    html_content = """
        <h1 style='color:blue;font-family:Verdana'>Hello, Aspose!</h1>
        <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
        <p style='color:green;'>This paragraph is green.</p>
        <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
    """
    html_fragment = ap.HtmlFragment(html_content)
    html_fragment.text_state = ap.text.TextState()
    html_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    html_fragment.text_state.font_size = 14
    html_fragment.text_state.foreground_color = ap.Color.red

    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![Добавить HTML‑фрагмент с переопределённым состоянием текста](html_override.png)

### Добавить LaTeX‑текст в PDF‑документ

Добавить математические выражения в формате LaTeX в PDF‑документ с помощью класса TeXFragment в Aspose.PDF for Python via .NET.
LaTeX — мощная система наборa, широко используемая для создания научных и математических документов. С помощью TeXFragment можно напрямую отрисовывать LaTeX‑нотацию и символы внутри PDF‑страницы.

1. Создать новый документ и страницу с помощью 'Document()', и 'document.pages.add()', чтобы добавить пустую страницу.
1. Использовать класс TeXFragment для прямого отображения синтаксиса LaTeX.
1. Добавить LaTeX‑контент в макет PDF с помощью 'page.paragraphs.add()'.
1. Сохранить PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_text_latex_fragment(outfile):
    """
    Add LaTeX mathematical expression to a PDF document.

    Creates a PDF document containing a complex mathematical expression rendered
    from LaTeX markup. This demonstrates advanced mathematical typesetting
    capabilities using LaTeX syntax within PDF documents.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses LaTeX TeXFragment for mathematical expression rendering
        - Expression includes overbrace and underbrace notation
        - Formula: (a+b)⁶ · (c+d)⁷ with braces and labels = 42
        - LaTeX commands: \\overbrace, \\underbrace, \\text, \\cdot
        - Provides professional mathematical typography

    Example:
        >>> add_text_latex_fragment("latex_math.pdf")
        # Creates a PDF with complex LaTeX mathematical expression
    """

    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.TeXFragment(
        "\\underbrace{\\overbrace{a+b}^6 \\cdot \\overbrace{c+d}^7}_\\text{example of text} = 42"
    )

    page.paragraphs.add(text_fragment)
    document.save(outfile)
```

![Сложное математическое выражение, отображённое в PDF, показывающее LaTeX‑формулу с надкруглой скобкой над (a+b)⁶, нижней скобкой под всей формулой (a+b)⁶ · (c+d)⁷, помеченной как пример текста, и равной 42. Формула демонстрирует продвинутый набор математических выражений с правильными отступами и стилизацией скобок, типичной для рендеринга LaTeX](latex_fragment.png)

## Пользовательские шрифты

### Использовать пользовательский шрифт из файла

Этот пример позволяет добавить текст в PDF‑файл с использованием пользовательского OpenType‑шрифта в Aspose.PDF for Python via .NET. Он показывает, как создать новый PDF‑документ, точно разместить текст на странице и применить пользовательское форматирование, такое как тип шрифта, размер, цвет и курсив.

1. Создать новый PDF‑документ и добавить страницу.
1. Определить текстовое содержание, которое вы хотите добавить в PDF.
1. Установить позицию текста.
1. Добавить TextFragment на страницу.
1. Сохраните PDF‑документ.

Эта функция работает не только с OTF, но и с TTF шрифтами.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def use_custom_font_from_file(outfile):
    """
    Creates a PDF document with text using a custom font loaded from a file.
    This function demonstrates how to load a custom OpenType font (.otf) from the file system
    and apply it to text in a PDF document. The text is styled with blue color, italic style,
    and positioned at specific coordinates on the page.
    Args:
        outfile (str): The output file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        - Requires the "BriosoPro Italic.otf" font file to be present in the DATA_DIR directory
        - Uses Aspose.PDF library for PDF generation and text manipulation
        - The text fragment is positioned at coordinates (100, 600) on the page
        - Font size is set to 24 points with blue foreground color and italic style
    """

    font_path = os.path.join(DATA_DIR, "BriosoPro Italic.otf")
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Hello, Aspose!")
    fragment.position = ap.text.Position(100, 600)
    fragment.text_state.font = ap.text.FontRepository.open_font(font_path)
    fragment.text_state.font_size = 24
    fragment.text_state.foreground_color = ap.Color.blue
    fragment.text_state.font_style = ap.text.FontStyles.ITALIC

    page.paragraphs.add(fragment)
    document.save(outfile)
```

![Фрагмент текста, отображаемый в PDF‑документе, показывающий Hello, Aspose! в синем курсивном шрифте BriosoPro, демонстрирующий интеграцию пользовательского OpenType‑шрифта и возможности стилизации в форматировании текста PDF](custom_font.png)

### Использовать пользовательский шрифт из потока

Этот фрагмент кода демонстрирует, как добавить текст в PDF‑документ, используя пользовательский встроенный шрифт OpenType (OTF) с Aspose.PDF для Python через .NET. Он показывает, как открыть файл шрифта как поток, встроить его в PDF, чтобы обеспечить доступность шрифта на разных системах, и применить форматирование текста, такое как размер шрифта, цвет и курсив. Такой подход идеален для создания визуально согласованных PDF‑файлов, сохраняющих типографику даже при совместном использовании или просмотре на устройствах без установленного шрифта.

1. Загрузите файл шрифта как двоичный поток.
1. Откройте и встроите шрифт, используя 'FontRepository.open_font'.
1. Создайте новый PDF‑документ и добавьте страницу.
1. Добавьте стилизованный фрагмент текста с:
- Встроенный пользовательский шрифт.
- Курсивный стиль и синий цвет.
- Определённый размер шрифта и позиция.
1. Сохраните окончательный документ в указанный путь вывода.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def use_custom_font_from_stream(outfile):
    """Use custom font from stream."""

    font_path = os.path.join(DATA_DIR, "BriosoPro Italic.otf")
    with open(font_path, "rb") as font_stream:
        font = ap.text.FontRepository.open_font(font_stream, ap.text.FontTypes.OTF)
        font.is_embedded = True

        document = ap.Document()
        page = document.pages.add()

        fragment = ap.text.TextFragment("Hello, Aspose!")
        fragment.position = ap.text.Position(100, 600)
        fragment.text_state.font = font
        fragment.text_state.font_size = 14
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.font_style = ap.text.FontStyles.ITALIC

        page.paragraphs.add(fragment)
        document.save(outfile)
```

Встраивание шрифтов обеспечивает одинаковое отображение на разных платформах, делая этот подход идеальным для брендинга, точности дизайна и поддержки нескольких языков.

