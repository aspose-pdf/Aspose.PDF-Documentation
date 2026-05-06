---
title: Добавление текста в PDF
linktitle: Добавить текст в PDF
type: docs
weight: 10
url: /ru/python-net/add-text-to-pdf-file/
description: Изучите, как добавить текст, HTML‑фрагменты, списки, ссылки и пользовательские шрифты в PDF‑документы на Python.
lastmod: "2026-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление текста в PDF с помощью Python
Abstract: Эта статья предоставляет всеобъемлющее руководство по работе с PDF‑документами с использованием библиотеки Aspose.PDF для Python. В ней рассматриваются различные методы добавления и форматирования текста, включая установку свойств текста, таких как размер Font, тип, цвет и позиционирование.
---

Это руководство объясняет, как добавлять текстовое содержимое в PDF‑документы с помощью Aspose.PDF for Python via .NET. Вы узнаете основные методы вставки текста — от размещения простого текстового фрагмента в определённой позиции до стилизации его (шрифт, размер, цвет, стиль), обработки языков с письмом справа налево (RTL), внедрения гиперссылок и работы с макетами абзацев, списками и эффектами прозрачности. Статья также охватывает расширенные сценарии, такие как использование HTML или LaTeX фрагментов, пользовательских шрифтов и опций форматирования текста, например межстрочного и межсимвольного интервалов.

Независимо от того, создаете ли вы простые аннотации или сложные типографские макеты, этот ресурс предоставляет вам базовые строительные блоки для работы с текстом в PDF с использованием Aspose.PDF.

## Базовые операции по вставке текста

Aspose.PDF for Python via .NET предоставляет мощный и гибкий API для обработки текста в PDF-файлах.
Независимо от того, нужны ли вам простые статические метки, богато отформатированный контент, многоязычный текст или интерактивные гиперссылки, набор инструментов позволяет сделать всё это с помощью лаконичного кода на Python.

### Добавить текст простой пример

Aspose.PDF for Python via .NET показывает, как добавить простой фрагмент текста в определённое положение на странице. Вы узнаете, как создать новый PDF‑документ, добавить страницу, вставить текст в заданных координатах и сохранить полученный файл.

1. Создать новый [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) объект.
1. Использовать `document.pages.add()` создать новый пустой [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. Создать [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) с текстовым содержимым.
1. Установите позицию текста, используя [`Position`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/position/) класс. Если вы укажете `Position`, текст будет расположен в вашем документе слева направо и смещён вниз.
1. Настройте внешний вид текста. Вы можете установить размер шрифта, цвет, стиль шрифта и многое другое через [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/).
1. Добавьте `TextFragment` к коллекции абзацев страницы с `page.paragraphs.add(text_fragment)`.
1. Сохраните документ.

Следующий фрагмент кода показывает, как добавить текст в существующий PDF‑файл:

```python
import math
import sys
import os
import aspose.pdf as ap

# region Basic text insertion
def add_text_simple_case(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

В этом примере кода используется TextFragment. Но вы также можете добавить текст на страницу PDF, используя TextParagraph. Давайте изучим разницу.
Этот **[TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)** — это отдельный кусок текста. TextFragment представляет собой единичную часть текста — по сути, одну строку текста, которую можно размещать, стилизовать и позиционировать независимо. Он идеален, когда необходимо добавить простой, небольшой объём текста.

Этот **[TextParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/)** — это группа TextFragments. Она может добавлять несколько строк текста. TextParagraph — это контейнер или коллекция из одного или более объектов TextFragment. Он идеален, когда нужно сгруппировать несколько фрагментов — например, чтобы создать блок текста с несколькими строками, словами или отформатированными элементами.
TextParagraph также управляет выравниванием текста, межстрочным интервалом и автоматическим размещением на странице. Использование красной линии возможно только с TextParagraph.

Для получения дополнительной информации о Working with Text, пожалуйста, проверьте [Форматирование текста в PDF](/pdf/ru/python-net/text-formatting-inside-pdf/) и [Извлечение текста из PDF с помощью Python](/pdf/ru/python-net/extract-text-from-pdf/) разделы документации.

### Добавить текст с помощью TextParagraph

Aspose.PDF for Python via .NET может добавить абзац текста, используя [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) и [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) с параметрами обтекания.

1. Создать новый [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) и пустой [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) используя `document.pages.add()`.
1. Прочитать текст из файла или использовать текст по умолчанию.
1. Создать [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) добавить контент уровня абзаца с управлением разметкой и переносом.
1. Создать [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) и установить режим переноса (пример использует `DISCRETIONARY_HYPHENATION`).
1. Создать [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/), применить стили, и добавить фрагмент к абзацу.
1. Добавьте абзац на страницу, используя `TextBuilder`.
1. Сохраните документ.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_paragraph(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = LOREM_PATH
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

    document.save(output_file_name)
```

![Добавить текст с помощью TextParagraph](text_paragraph.png)

### Добавить абзацы с отступами в PDF

Следующий фрагмент кода показывает, как создать новый PDF‑документ и добавить два абзаца текста с разными стилями отступов:

- Первый абзац демонстрирует отступ первой строки (отступ делается только у первой строки).
- Во втором абзаце демонстрируется отступ последующих строк (все строки после первой имеют отступ).

Он использует классы ‘TextParagraph’, ‘TextBuilder’ и ‘TextFragment’ из Aspose.PDF для точного контроля макета и форматирования.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_paragraphs_indents(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = LOREM_PATH
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

### Добавить новую строку текста в PDF

Aspose.PDF for Python via .NET позволяет вставлять многострочный текст в PDF‑документ, используя классы TextFragment, TextParagraph и TextBuilder.

1. Создайте новый документ.
1. Определите TextFragment, содержащий символ новой строки.
1. Установить стиль текста.
1. Добавьте фрагмент в абзац.
1. Расположите абзац.
1. Отобразить абзац на странице.
1. Сохраните документ.

```python
import math
import sys
import os
import aspose.pdf as ap

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

### Определить разрывы строк и фиксировать уведомления в PDF

Показано, как создать PDF‑документ, содержащий несколько текстовых фрагментов, и включить журнал уведомлений Aspose.PDF для мониторинга событий компоновки — таких как разрывы строк и переносы текста — во время рендеринга.

1. Создайте новый PDF документ.
1. Включить журналирование уведомлений.
1. Используйте document.pages.add() для создания первой страницы.
1. Добавьте несколько фрагментов текста.
1. Используйте page.paragraphs.add(text) для отображения каждого фрагмента текста.
1. Сохраните документ.

```python
import math
import sys
import os
import aspose.pdf as ap

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

### Динамически измерять ширину текста в PDF

Динамически измерять ширину символов и строк в определённом шрифте с помощью Aspose.PDF for Python via .NET. Используются методы 'Font.measure_string()' и 'TextState.measure_string()', чтобы проверить, что измеренные ширины строк согласованы и точны.

1. Используйте 'FontRepository.find_font()', чтобы получить объект шрифта Arial из репозитория.
1. Создайте объект TextState для управления свойствами шрифта.
1. Измерять отдельные символы.
1. Сравните результаты обоих методов для всех символов от 'A' до 'z'.
1. Убедитесь, что оба подхода измерения дают одинаковые результаты.

```python
import math
import sys
import os
import aspose.pdf as ap

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

### Добавить текст с гиперссылками

Добавьте кликабельные гиперссылки в текст PDF с использованием Aspose.PDF for Python via .NET. Наша библиотека демонстрирует, как добавить несколько текстовых сегментов внутри одного TextFragment и применить гиперссылку к конкретному сегменту, а также стилизовать текстовые сегменты индивидуально (например, цвет, курсивный шрифт).

1. Создайте новый документ и страницу, используя 'Document()', и 'document.pages.add()', чтобы добавить пустую страницу.
1. Создать TextFragment.
1. Добавьте несколько объектов TextSegment. Каждый сегмент может иметь собственное содержимое и стилизацию. Например, обычный текст или гиперссылка.
1. Примените гиперссылку к сегменту. Создайте объект WebHyperlink с нужным URL.
1. Оформите сегмент. Настройте цвет, стиль шрифта, размер и т.д., используя text_state.
1. Добавьте фрагмент на страницу, используя 'page.paragraphs.add()'.
1. Сохранить PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_hyperlink(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Sample Text Fragment")

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
    document.save(output_file_name)
```

![Текстовый фрагмент, отображённый в PDF, показывающий смешанное содержание с Sample Text Fragment, за которым следует Text Segment 1, затем синяя гиперссылка с надписью Link to Aspose (ссылка на https://products.aspose.com/pdf), и заканчивается TextSegment без гиперссылки в обычном черном форматировании текста](hyperlink_text.png)

### Добавить текст справа налево (RTL) в PDF‑документ

RTL (от Right To Left) — это свойство, указывающее направление написания текста, при котором текст пишется справа налево.
Aspose.PDF for Python via .NET демонстрирует, как добавить текст справа налево (RTL), например арабский или иврит, в PDF‑документ.

1. Создайте новый документ и страницу, используя 'Document()', и 'document.pages.add()', чтобы добавить пустую страницу.
1. Создайте TextFragment с RTL‑содержимым. Вставьте ваш арабский, иврит или другой текст на RTL‑языке в качестве содержимого фрагмента.
Установите шрифт и стилизацию. Выберите шрифт, который поддерживает сценарий RTL (например, Tahoma, Arial Unicode MS). Установите font_size и foreground_color по необходимости.
1. Установите горизонтальное выравнивание по правому краю, используя 'text_fragment.horizontal_alignment'.
1. Добавьте фрагмент текста на страницу.
1. Сохранить PDF‑документ.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_rtl_text(output_file_name):
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
    document.save(output_file_name)
```

![Текст справа налево](rtl_text.png)

## Стилизация текста

### Добавить текст со стилизацией шрифта

Это более продвинутый пример, демонстрирующий стилизацию текста, настройку шрифтов и смешанный формат текста (используя субскриптные сегменты). Aspose.PDF объясняет, как применять свойства шрифта, такие как семейство шрифта, размер, цвет, полужирный, курсив и подчеркивание, к фрагменту текста.
Кроме того, этот фрагмент кода демонстрирует, как использовать несколько текстовых сегментов в одном фрагменте для создания сложных текстовых выражений — например, включающих символы нижнего или верхнего индекса, часто требуемые в формулах или научных обозначениях.

1. Создайте новый документ и страницу, используя 'Document()', и 'document.pages.add()', чтобы добавить пустую страницу.
1. Создайте TextFragment для простого стилизованного текста.
1. Определить текстовое содержимое.
1. Установите позицию, используя координаты Position(x, y).
1. Примените стилизацию через свойство 'text_state' — шрифт, font_size, foreground_color, font_style, underline.
1. Создайте сложное выражение с несколькими объектами TextSegment. Каждый TextSegment представляет собой часть текста, которой можно задать собственный стиль. Это позволяет создавать выражения, такие как математические или химические формулы.
1. Определите несколько объектов TextState. Один для основного текста (text_state_letters). Другой — для текста в виде нижнего или верхнего индекса (text_state_index).
1. Объедините текстовые сегменты. Добавьте каждый сегмент к 'TextFragment', используя 'segments.append()'.
1. Добавьте оба текстовых объекта на страницу. Используйте 'page.paragraphs.add()' для размещения их в документе.
1. Сохраните окончательный Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_font_styling(output_file_name):
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
    document.save(output_file_name)
```

![Текстовый фрагмент отображается с синим курсивным шрифтом Arial, содержащим текст Hello, Aspose! за которым следует математическая формула, показывающая S = a subscript 2n + a subscript 2n+1 + a subscript 2n+2, при этом основной текст синего цвета, а подстрочный — красного цвета.](styled_text.png)

## Добавить прозрачный текст

Добавьте полупрозрачные фигуры и текст в PDF-документ, используя Aspose.PDF for Python.
Он создает цветной прямоугольник с частичной непрозрачностью и накладывает TextFragment с прозрачным цветом переднего плана.

1. Инициализируйте объект Document и добавьте пустую страницу для рисования содержимого.
1. Используйте 'ap.drawing.Graph' для создания холста, который позволяет рисовать фигуры.
1. Добавьте прямоугольник с полупрозрачной заливкой.
1. Предотвратить смещение позиции холста.
1. Добавьте холст на страницу. Вставьте графические фигуры в коллекцию абзацев страницы.
1. Создайте прозрачный текстовый фрагмент.
1. Вставьте текстовый фрагмент в коллекцию абзацев страницы.
1. Сохранить PDF‑документ.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_transparent(output_file_name):
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

    document.save(output_file_name)
```

### Добавить невидимый текст в PDF

В этом примере показано, как создать PDF‑документ, содержащий как видимый, так и невидимый текст. Невидимый текст остаётся частью структуры документа, но скрыт от просмотра, что делает его полезным для встраивания метаданных, тегов доступности или поискового контента без изменения макета.

1. Создать PDF Document и Page.
1. Создайте текстовый фрагмент с повторяющимся видимым содержимым.
1. Добавьте второй фрагмент текста и пометьте его как невидимый.
1. Сохранить Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_invisible(output_file_name):
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Add visible text
    text1 = ap.text.TextFragment(
        "This is the visible text. This is the visible text. This is the visible text."
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

    document.save(output_file_name)
```

### Добавить текст с оформлением границы в PDF

Библиотека Aspose.PDF показывает, как создать PDF‑документ, содержащий стилизованный фрагмент текста с видимой границей. Метод применяет цвета фона и переднего плана, настройки шрифта и обводку (границу) вокруг прямоугольника текста для усиления визуального акцента.

1. Создайте PDF Document и Page.
1. Создайте и разместите текстовый фрагмент. Добавьте текстовый фрагмент с сообщением и установите его позицию.
1. Применить стили текста. Установить шрифт Times New Roman, размер 12. Применить светло-серый фон и красный цвет переднего плана (текст).
1. Настройте стили границы.
1. Добавить текст на страницу. Используйте TextBuilder, чтобы добавить стилизованный текст на страницу.
1. Сохранить Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_border(output_file_name):
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

### Добавить перечёркнутый текст в PDF

Добавьте форматирование зачеркивания (strikeout) к фрагменту текста в PDF‑документе. Зачеркнутый текст полезен для указания удалений, исправлений или акцента в аннотированных документах.

1. Создайте новый документ и страницу, используя 'Document()', и 'document.pages.add()', чтобы добавить пустую страницу.
1. Создать и оформить текстовый фрагмент.
1. Применить форматирование цвета и зачеркивания. Установить фон светло-серым, цвет текста красным и включить зачеркивание.
1. Расположите текст.
1. Используйте 'TextBuilder', чтобы добавить стилизованный текст на страницу.
1. Сохранить Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_strikeout_text(output_file_name):
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

### Применение осевого градиента к тексту в PDF

Aspose.PDF for Python via .NET демонстрирует, как применить линейный градиент к тексту в PDF‑документе. Аксиальный градиент плавно переходит от красного к синему по всему тексту, создавая визуально эффектный заголовок. Эта техника идеальна для стилизованных названий, брендинга или декоративных элементов в макете PDF‑документов.

1. Инициализировать новый документ и добавить пустую страницу.
1. Создайте и оформите фрагмент текста. Добавьте заголовок, задайте позицию, шрифт и размер.
1. Примените осевое градиентное затенение с помощью ‘GradientAxialShading’. Установите основной цвет, используя GradientAxialShading, от красного к синему.
1. Добавить стиль подчеркивания.
1. Вставьте стилизованный фрагмент текста на страницу.
1. Сохранить Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def apply_gradient_axial_shading_to_text(output_file_name):
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

Радиальный градиент создаёт круговой переход цвета, который излучается наружу от центра текста, предлагая визуально динамичную стилизацию для заголовков, подзаголовков или декоративных элементов.

1. Инициализировать новый документ и добавить пустую страницу.
1. Создайте и оформите фрагмент текста. Добавьте заголовок, задайте позицию, шрифт и размер.
1. Примените радиальный градиент с помощью 'GradientRadialShading'. Установите цвет переднего плана, используя GradientRadialShading, от красного к синему.
1. Добавить стиль подчеркивания.
1. Вставьте стилизованный фрагмент текста на страницу.
1. Сохранить Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def apply_gradient_radial_shading_to_text(output_file_name):
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

### Добавить HTML-текст в PDF-документ

Библиотека Aspose.PDF for Python via .NET позволяет вставлять контент в формате HTML в PDF‑документ с помощью класса HtmlFragment. Используя HTML‑теги, вы можете отобразить стилизованный, структурированный или похожий на формулу текст непосредственно в PDF.

1. Создайте новый документ и страницу, используя 'Document()', и 'document.pages.add()', чтобы добавить пустую страницу.
1. Создайте экземпляр класса HtmlFragment и передайте вашу строку HTML в качестве параметра.
1. Добавьте фрагмент на страницу, используя ‘page.paragraphs.add()’, чтобы вставить HTML‑контент.
1. Сохранить PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_html_fragment(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.HtmlFragment("<pre>S=a<sub>2n</sub>+a<sup>2</sup><pre>")

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![Добавить HTML‑текст в PDF‑документ](html_fragment.png)

### Добавьте стилизованный HTML‑фрагмент с различным форматированием в PDF‑документ

Мы можем определить HTML‑фрагмент и задать стиль текста непосредственно с помощью HTML‑тегов. Внедрить стилизованный HTML‑контент в PDF‑документ. Этот фрагмент кода создаёт новый PDF‑файл, добавляет страницу, вставляет HTML‑фрагмент с различными элементами форматирования (заголовки, абзацы, ссылки и встроенные стили) и сохраняет результат по указанному пути.

1. Инициализирует новый объект Document для представления PDF.
1. Добавляет пустую страницу к документу, на которой будет размещён HTML‑контент.
1. Подготовьте HTML‑контент. Строка HTML содержит заголовок h1, зелёный абзац с полужирным, курсивным и подчёркнутым текстом, а также гиперссылку на веб‑сайт с увеличенным размером шрифта.
1. Создайте HTML-фрагмент. Оберните строку HTML в объект HtmlFragment.
1. Вставить HTML в Page. Добавляет фрагмент HTML в коллекцию абзацев страницы, отображая HTML как нативный PDF‑контент.
1. Сохранить Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_html_fragment(output_file_name):
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
    document.save(output_file_name)
```

![Добавить HTML‑контент в PDF‑документ](html_content.png)

### Добавить HTML‑фрагмент с переопределённым состоянием текста

Как мы видели в предыдущем примере, можно задавать стили непосредственно в HTML‑коде. Это имеет свои преимущества, но и некоторые недостатки. Предположим, мы работаем с HTML клиента и хотим унифицировать внешний вид нашего вывода.
В этом случае мы можем переопределить стилизацию клиента, используя наш собственный TextState, как показано в следующем примере.

1. Создайте новый документ и страницу, используя 'Document()', и 'document.pages.add()', чтобы добавить пустую страницу.
1. Подготовьте HTML‑контент. Строка HTML содержит заголовок h1 с шрифтом Verdana, зелёный абзац с полужирным, курсивным и подчёркнутым текстом, а также гиперссылку на веб‑сайт с более крупным размером шрифта.
1. Создайте HTML-фрагмент. Оберните строку HTML в объект HtmlFragment.
1. Переопределите форматирование текста. Создайте объект TextState и установите Font, Font Size и Text Color.
1. Добавьте HTML fragment в коллекцию абзацев страницы.
1. Сохранить Document.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_html_fragment_override_text_state(output_file_name):
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
    document.save(output_file_name)
```

![Добавить состояние переопределения текста HTML‑фрагмента](html_override.png)

### Добавить LaTeX-текст в PDF Document

Добавьте математические выражения в формате LaTeX в PDF‑документ, используя класс TeXFragment в Aspose.PDF for Python via .NET.
LaTeX — мощная система наборa, широко используемая для создания научных и математических документов. С помощью TeXFragment вы можете напрямую отображать математические обозначения и символы LaTeX внутри страницы PDF.

1. Создайте новый документ и страницу, используя 'Document()', и 'document.pages.add()', чтобы добавить пустую страницу.
1. Используйте класс TeXFragment для прямого рендеринга синтаксиса LaTeX.
1. Добавьте содержимое LaTeX в макет PDF с помощью 'page.paragraphs.add()'.
1. Сохранить PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_latex_fragment(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.TeXFragment(
        "\\underbrace{\\overbrace{a+b}^6 \\cdot \\overbrace{c+d}^7}_\\text{example of text} = 42"
    )

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![Сложное математическое выражение, отображённое в PDF, показывающее формулу LaTeX с обозначением overbrace над (a+b)⁶, обозначением underbrace под всей выражением (a+b)⁶ · (c+d)⁷, помеченное как пример текста, и равное 42. Формула демонстрирует продвинутый набор математических формул с правильными интервалами и стилизацией скобок, характерной для рендеринга LaTeX.](latex_fragment.png)

## Пользовательские шрифты

### Использовать пользовательский Font из файла

Этот пример позволяет добавить текст в PDF‑файл, используя пользовательский шрифт OpenType в Aspose.PDF for Python via .NET. Он показывает, как создать новый PDF‑документ, точно позиционировать текст на странице и применить пользовательское форматирование, такое как тип шрифта, размер, цвет и курсивный стиль.

1. Создайте новый PDF документ и добавьте страницу.
1. Определите текстовое содержание, которое вы хотите добавить в PDF.
1. Установите позицию текста.
1. Добавьте TextFragment на страницу.
1. Сохранить PDF‑документ.

Эта функция работает не только с шрифтами OTF, но и с шрифтами TTF.

```python
import math
import sys
import os
import aspose.pdf as ap

def use_custom_font_from_file(output_file_name):
    font_path = os.path.join(FONT_DIR, "BriosoPro Italic.otf")
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Hello, Aspose!")
    fragment.position = ap.text.Position(100, 600)
    fragment.text_state.font = ap.text.FontRepository.open_font(font_path)
    fragment.text_state.font_size = 24
    fragment.text_state.foreground_color = ap.Color.blue
    fragment.text_state.font_style = ap.text.FontStyles.ITALIC

    page.paragraphs.add(fragment)
    document.save(output_file_name)
```

![Фрагмент текста, отображаемый в документе PDF, показывающий Hello, Aspose! отображённый синим курсивным шрифтом BriosoPro, демонстрирующий интеграцию пользовательского шрифта OpenType и возможности стилизации в форматировании текста PDF.](custom_font.png)

### Использовать пользовательский Font из потока

Этот фрагмент кода демонстрирует, как добавить текст в PDF‑документ, используя пользовательский встроенный шрифт OpenType (OTF) с Aspose.PDF for Python via .NET. Он показывает, как открыть файл шрифта как поток, встроить его в PDF, чтобы обеспечить доступность шрифта на разных системах, и применить форматирование текста, такое как размер шрифта, цвет и курсивный стиль. Такой подход идеален для создания визуально согласованных PDF‑файлов, сохраняющих типографику даже при совместном использовании или просмотре на устройствах без установленного шрифта.

1. Загрузите файл шрифта как бинарный поток.
1. Откройте и встрайте шрифт, используя 'FontRepository.open_font'.
1. Создайте новый PDF документ и добавьте страницу.
1. Добавьте стилизованный текстовый фрагмент с:
    - Встроенный пользовательский шрифт.
    - Курсивный стиль и синий цвет.
    - Конкретный размер шрифта и положение.
1. Сохраните окончательный документ в указанный путь вывода.

```python
import math
import sys
import os
import aspose.pdf as ap

def use_custom_font_from_stream(output_file_name):
    font_path = os.path.join(FONT_DIR, "BriosoPro Italic.otf")
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
        document.save(output_file_name)
```

Встраивание шрифтов обеспечивает согласованное отображение на разных платформах, что делает этот подход идеальным для брендинга, точности дизайна и поддержки многоязычности.

## Связанные темы текста

- [Работа с текстом в PDF с помощью Python](/pdf/ru/python-net/working-with-text/)
- [Форматировать текст PDF с помощью Python](/pdf/ru/python-net/text-formatting-inside-pdf/)
- [Заменить текст в PDF с помощью Python](/pdf/ru/python-net/replace-text-in-pdf/)
- [Поиск и извлечение текста PDF в Python](/pdf/ru/python-net/search-and-get-text-from-pdf/)