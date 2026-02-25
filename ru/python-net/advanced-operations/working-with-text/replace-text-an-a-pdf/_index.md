---
title: Замена текста в PDF с помощью Python
linktitle: Замена текста в PDF
type: docs
weight: 40
url: /ru/python-net/replace-text-in-pdf/
description: Узнайте больше о различных способах замены и удаления текста из библиотеки Aspose.PDF для Python через .NET.
lastmod: "2025-10-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
aliases: 
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Как заменить текст в PDF с помощью Python
Abstract: Статья предоставляет всестороннее руководство по различным методикам манипулирования текстом в PDF‑документах с использованием Aspose.PDF для Python через .NET. В ней рассматриваются несколько стратегий замены текста, включая замену текста на всех страницах, в конкретных областях страниц и с использованием регулярных выражений. Статья также объясняет, как заменить шрифты в PDF, гарантируя удаление неиспользуемых шрифтов, и как управлять заменой текста для автоматической перестройки содержимого страниц. Кроме того, она описывает рендеринг заменяемых символов при создании PDF, включая их использование в областях заголовков/подвалов, для улучшения настройки документа. Наконец, она подробно описывает методы удаления всего текста из PDF‑документа, оптимизируя операции для сценариев, когда требуется полное удаление текста. Каждый раздел сопровождается примерами кода на Python и других поддерживаемых языках для демонстрации практической реализации.
---

Эти примеры демонстрируют, как **модифицировать или удалить текст в существующем PDF**.

## Замена существующего текста

### Замена текста на всех страницах PDF‑документа

{{% alert color="primary" %}}

Вы можете попробовать найти и заменить текст в документе, используя Aspose.PDF, и получить результаты онлайн по этой [ссылке](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Замена текста является распространенной задачей при обновлении или исправлении содержимого в существующих PDF‑документах — например, изменении названий продуктов, исправлении опечаток или обновлении терминологии на нескольких страницах.

Aspose.PDF для Python через .NET предлагает мощный и эффективный метод программного поиска и замены текста с помощью класса [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).

Этот пример показывает, как найти все вхождения конкретной фразы (в данном случае, "Black cat") и заменить их новой фразой ("White dog") во всём PDF‑документе.

1. Укажите фразы для поиска и замены. Задайте текст, который нужно найти, и текст, которым его нужно заменить.
1. Загрузите PDF‑документ.
1. Создайте поглотитель текста. TextFragmentAbsorber инициализируется поисковой фразой. Он сканирует документ в поисках всех вхождений данной фразы.
1. Примените поглотитель ко всем страницам. Он проходит по всем страницам и собирает фрагменты текста, соответствующие фразе.
1. Замените каждый найденный фрагмент. Каждое вхождение "Black cat" должно быть заменено на "White dog".
1. Сохраните обновлённый PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_on_all_pages(infile, outfile):
    """
    Replace text on all pages of a PDF document.

    Searches for a specific text phrase throughout all pages of a PDF document
    and replaces all occurrences with a new phrase. This function demonstrates
    global text replacement using TextFragmentAbsorber.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Replaces "Black cat" with "White dog" as demonstration
        - Searches across all pages in the document
        - Preserves original formatting and layout
        - Uses TextFragmentAbsorber for efficient text search

    Example:
        >>> replace_text_on_all_pages("input.pdf", "output.pdf")
        # Replaces all instances of "Black cat" with "White dog"
    """
    search_phrase = "Black cat"
    replace_phrase = "White dog"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### Замена текста в определённой области страницы

Иногда может потребоваться заменить текст только в конкретной области страницы PDF, а не во всём документе — например, обновить заголовок, нижний колонтитул или ячейку таблицы в известном положении.

Библиотека Aspose.PDF для Python через .NET обеспечивает эту возможность, используя [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) в сочетании с поиском текста по области.

Этот пример демонстрирует, как находить и заменять все вхождения целевой фразы в заданном прямоугольном регионе на конкретной странице.

1. Укажите фразы для поиска и замены.
1. Загрузите PDF‑документ.
1. Создайте поглотитель текста для поиска. Инициализируйте TextFragmentAbsorber для нахождения нужного текста.
1. Ограничьте область поиска. Прямоугольник задаёт пределы по осям x и y на странице.
1. Примените поглотитель к конкретной странице. Это выполняет поиск и собирает совпадающие фрагменты текста в указанной области.
1. Замените найденный текст. Каждый пример 'doc' в определённой области будет заменён на 'DOC'.
1. Сохраните обновлённый PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_in_particular_page_region(infile, outfile):
    """
    Replace text in a particular region of a page.

    Performs targeted text replacement within a specific rectangular region
    on the first page of a PDF document. This allows for precise control
    over which text gets replaced based on its location.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Replaces "doc" with "DOC" within the specified region
        - Only affects text within coordinates (300, 442, 500, 742)
        - Uses limit_to_page_bounds for precise region control
        - Only processes the first page (pages[1])

    Example:
        >>> replace_text_in_particular_page_region("input.pdf", "output.pdf")
        # Replaces "doc" with "DOC" only in the specified rectangular area
    """
    search_phrase = "doc"
    replace_phrase = "DOC"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        absorber.text_search_options.limit_to_page_bounds = True
        absorber.text_search_options.rectangle = ap.Rectangle(300, 442, 500, 742, True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### Изменение размера и смещение текста без изменения размера шрифта

При замене текста в PDF иногда требуется вписать или переместить новый текст в конкретную область без изменения размера шрифта.
Aspose.PDF для Python через .NET предоставляет возможности регулировать макет и интервалы текста, сохраняя оригинальный размер шрифта.

1. Загрузите PDF‑документ.
1. Соберите все текстовые фрагменты на странице с помощью 'TextFragmentAbsorber'.
1. Выберите фрагмент для изменения.
1. Сдвиньте и измените размер прямоугольника текста.
1. Настройте интервалы текста. Включите регулирование интервалов, чтобы разместить текст внутри изменённого прямоугольника.
1. Замените текст фрагмента.
1. Сохраните обновлённый PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_shift_without_changing_font_size(infile, outfile):
    """
    Resize and shift text without changing the font size.

    Demonstrates how to replace text content while adjusting its position
    and width within a modified rectangular area. The font size remains
    unchanged, but spacing is adjusted to fit the new content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Targets the second text fragment on the first page
        - Narrows the text rectangle by 50 units on each side
        - Duplicates the original text content
        - Uses ADJUST_SPACE_WIDTH for proper spacing
        - Maintains original font size and style

    Example:
        >>> replace_text_and_resize_and_shift_without_changing_font_size("input.pdf", "output.pdf")
        # Duplicates text in a narrower space with adjusted spacing
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = fragment.rectangle
        rect.llx += 50
        rect.urx -= 50
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Изменение размера и смещение абзаца в PDF

При работе с PDF иногда требуется заменить или расширить абзац, при этом визуально сохранить выравнивание с макетом страницы. Aspose.PDF позволяет изменить размер ограничивающего прямоугольника абзаца и скорректировать интервалы, чтобы разместить новый текст, не меняя размер шрифта.

1. Загрузите PDF‑документ.
1. Используйте 'TextFragmentAbsorber' для сбора всех текстовых фрагментов на странице.
1. Выберите фрагмент для изменения.
1. Измените размер и сместите абзац. Используйте медиакоробку страницы для определения границ и корректировки прямоугольника.
1. Отрегулируйте интервал. Это изменяет расстояние между словами/буквами вместо изменения размера шрифта.
1. Замените текст фрагмента.
1. Сохраните изменённый PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_shift_paragraph(infile, outfile):
    """
    Resize and shift a paragraph in the document.

    Demonstrates paragraph-level text replacement with automatic resizing
    to fit within the page's media box boundaries. Adjusts the text area
    to provide margins while duplicating content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses page media box as base rectangle
        - Adds 20-unit margins on left, right, and top
        - Targets the second text fragment on the first page
        - Duplicates original text content
        - Automatically adjusts space width for proper fit

    Example:
        >>> replace_text_and_resize_and_shift_paragraph("input.pdf", "output.pdf")
        # Resizes paragraph to fit within page margins with duplicated text
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = document.pages[1].media_box
        rect.llx += 20
        rect.urx -= 20
        rect.ury -= 20
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Замена текста и автоматическое расширение шрифта для заполнения целевой области

Замените текст в PDF, автоматически меняя размер и расширяя шрифт, чтобы заполнить определённую прямоугольную область. С помощью библиотеки Aspose.PDF для Python через .NET код динамически корректирует размер шрифта и интервалы так, чтобы новое содержимое текста идеально вписывалось в заданный ограничивающий прямоугольник — без ручных вычислений шрифта.

1. Загрузите PDF.
1. Захватите текстовые фрагменты.
1. Выберите конкретный фрагмент.
1. Определите целевой прямоугольник.
1. Включите параметры корректировки текста.
1. Замените текст.
1. Сохраните документ.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_expand_font(infile, outfile):
    """
    Resize and expand font to fill target area.

    Demonstrates automatic font scaling to fill a specified rectangular area.
    The font size is dynamically adjusted to make the text content fit
    perfectly within the defined target rectangle.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Defines target rectangle at coordinates (100, 300, 512, 692)
        - Uses SCALE_TO_FILL for automatic font size adjustment
        - Duplicates original text content
        - Adjusts space width for optimal text distribution
        - Font size scales up or down to fill the entire rectangle

    Example:
        >>> replace_text_and_resize_and_expand_font("input.pdf", "output.pdf")
        # Scales font to completely fill the specified rectangular area
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = ap.Rectangle(100, 300, 512, 692, True)
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SCALE_TO_FILL
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)

```

### Замена текста и вписание его в прямоугольник

Замените текст в PDF‑документе, обеспечивая, чтобы новое содержимое помещалось в исходную прямоугольную область текста, автоматически уменьшая размер шрифта при необходимости.

Используя библиотеку Aspose.PDF для Python через .NET, эта функция динамически регулирует как макет текста, так и размер шрифта, сохраняя структуру документа и предотвращая переполнение.

1. Создайте объект TextFragmentAbsorber для извлечения всех текстовых фрагментов с первой страницы.
1. Доступ к конкретному текстовому фрагменту.
1. Установите область замены.
1. Настройте параметры коррекции текста. Установите два ключевых параметра замены:
- Регулировка размера шрифта — 'SHRINK_TO_FIT' автоматически уменьшает размер шрифта, если новый текст слишком длинный.
- Регулировка интервала — 'ADJUST_SPACE_WIDTH' сохраняет пропорциональность интервалов.
1. Замените текст.
1. Сохраните изменённый PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_fit_text_into_rectangle(infile, outfile):
    """
    Fit text into a rectangle by adjusting font size.

    Demonstrates how to ensure text content fits within its original
    rectangle by automatically shrinking the font size when the new
    content is longer than the original.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses original text fragment rectangle as target area
        - Employs SHRINK_TO_FIT to reduce font size if needed
        - Duplicates original text content (making it longer)
        - Adjusts space width for proper text distribution
        - Prevents text overflow by automatic font scaling

    Example:
        >>> replace_text_and_fit_text_into_rectangle("input.pdf", "output.pdf")
        # Shrinks font size to fit doubled text content in original space
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = fragment.rectangle
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SHRINK_TO_FIT
        )
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH

        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Автоматическая замена текста‑заполнителя и переупорядочивание макета PDF

Замените текст‑заполнитель внутри PDF (например, шаблоны или формы) на фактические данные, такие как имена или информация о компании.
Он автоматически корректирует макет страницы, чтобы разместить новый текст, применяя пользовательское форматирование (шрифт, цвет, размер).

1. Импортируйте и загрузите PDF.
1. Создайте Text Absorber для заполнителя.
1. Примените Absorber ко всем страницам.
1. Пройдите в цикле найденные текстовые фрагменты.
1. Примените пользовательское форматирование текста.
1. Сохраните обновлённый документ.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def automatically_rearrange_page_contents(input_file, output_file):
    """
    Replace placeholder text in PDF with actual content.

    Demonstrates how to replace long placeholder text with actual content
    and automatically rearrange page layout. Shows dynamic content replacement
    with custom formatting applied to the new text.

    Args:
        input_file (str): Path to the input PDF file containing placeholders.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Searches for "[Long_placeholder_Long_placeholder]" placeholders
        - Replaces with either "John Smith" or extended version with studio info
        - Applies Calibri font, size 12, navy blue color
        - Automatically adjusts page layout to accommodate content changes
        - Demonstrates real-world template filling scenarios

    Example:
        >>> automatically_rearrange_page_contents("template.pdf", "filled.pdf")
        # Replaces placeholders with formatted actual content
    """
    document = ap.Document(input_file)

    absorber = ap.text.TextFragmentAbsorber("[Long_placeholder_Long_placeholder]")
    document.pages.accept(absorber)

    for text_fragment in absorber.text_fragments:
        # text_fragment.text = "John Smith"
        text_fragment.text = "John Smith, South Development Studio"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Calibri")
        text_fragment.text_state.font_size = 12
        text_fragment.text_state.foreground_color = ap.Color.navy

    # Save PDF document
    document.save(output_file)
```

### Замена текста на основе регулярного выражения

При работе с PDF‑документами может потребоваться заменять текст, соответствующий шаблону, а не конкретной фразе — например, номера телефонов, коды или форматы, похожие на даты.

Aspose.PDF для Python через .NET позволяет выполнять такие замены с помощью регулярных выражений (regex) и класса TextFragmentAbsorber.

Этот пример демонстрирует, как находить текстовые шаблоны (в данном случае любой текст, соответствующий формату ####-####, например 1234-5678) и заменять их отформатированной строкой 'ABC1-2XZY'. Он также показывает, как настраивать шрифт, цвет и размер заменённого текста.

Следующий фрагмент кода показывает, как заменить текст на основе регулярного выражения.

1. Загрузите PDF‑документ.
1. Создайте Absorber на основе регулярного выражения. Инициализируйте TextFragmentAbsorber с шаблоном регулярного выражения.
1. Включите режим регулярного выражения. Параметр 'True' активирует режим поиска по регулярному выражению.
1. Примените Absorber к странице. Это сканирует страницу на предмет всех текстовых фрагментов, соответствующих заданному шаблону regex.
1. Замените каждое совпадение новым текстом и примените пользовательское стилизование.
1. Сохраните изменённый документ.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_based_on_regex(infile, outfile):
    """
    Replace text based on a regular expression pattern.

    Demonstrates pattern-based text replacement using regular expressions
    to find and replace text that matches specific formats. Also shows
    how to apply formatting changes to the replaced text.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses regex pattern r"\\d{4}-\\d{4}" to find 4-digit-4-digit patterns
        - Replaces matched patterns with "ABC1-2XZY"
        - Applies custom formatting: Verdana font, size 12, blue text
        - Sets light green background color for replaced text
        - Enables regex mode with TextSearchOptions(True)

    Example:
        >>> replace_text_based_on_regex("input.pdf", "output.pdf")
        # Replaces patterns like "1234-5678" with formatted "ABC1-2XZY"
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(r"\d{4}-\d{4}")
        absorber.text_search_options = ap.text.TextSearchOptions(True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = "ABC1-2XZY"
            fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
            fragment.text_state.font_size = 12
            fragment.text_state.foreground_color = ap.Color.blue
            fragment.text_state.background_color = ap.Color.light_green

        document.save(outfile)
```

## Замена шрифтов или удаление неиспользуемых шрифтов

### Заменить шрифты в существующем PDF-файле

Время от времени вам нужно стандартизировать или обновить шрифты в PDF — например, заменить устаревший или проприетарный шрифт на более доступный. Библиотека Aspose.PDF for Python via .NET позволяет программно обнаруживать и заменять шрифты, обеспечивая согласованность типографии и совместимость документа.

Этот пример демонстрирует, как заменить все вхождения конкретного шрифта (например, 'Arial-BoldMT') на другой шрифт (например, 'Verdana') по всему PDF-документу.

В следующем фрагменте кода показано, как заменить шрифт внутри PDF-документа:

1. Откройте PDF‑документ.
1. Инициализируйте TextFragmentAbsorber.
1. Используйте Absorber для извлечения текстовых фрагментов со всех страниц документа.
1. Определите и замените шрифты. Скрипт проверяет, является ли текущий шрифт фрагмента 'Arial-BoldMT'. Если да, он заменяет его на шрифт 'Verdana' с помощью метода FontRepository.find_font().
1. Сохраните изменённый документ.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_fonts(infile, outfile):
    """
    Replace specific fonts in a PDF document.

    Demonstrates how to find and replace specific fonts throughout a PDF
    document. Searches for text using a particular font and changes it
    to a different font while preserving the text content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Searches for text using "Arial-BoldMT" font
        - Replaces font with "Verdana" while keeping text content
        - Processes all text fragments across all pages
        - Maintains original text size and formatting properties
        - Useful for font standardization across documents

    Example:
        >>> replace_fonts("input.pdf", "output.pdf")
        # Changes all Arial-BoldMT text to use Verdana font instead
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            if fragment.text_state.font.font_name == "Arial-BoldMT":
                fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")

        document.save(outfile)
```

### Удалить неиспользуемые шрифты

Со временем PDF‑документы могут накапливать неиспользуемые или встроенные шрифты, которые увеличивают размер файла и замедляют обработку. Такие неиспользуемые шрифты часто остаются даже после редактирования или замены текста, особенно при работе с большими или сложными PDF.

Библиотека Aspose.PDF for Python via .NET предоставляет эффективный способ удалить такие избыточные шрифты с помощью класса TextEditOptions. Это не только оптимизирует ваш документ, но и гарантирует, что используются только шрифты, действительно применённые к видимому тексту.

Метод 'remove_unused_fonts()' — простой, но мощный способ оптимизировать PDF‑файлы, удаляя избыточные данные шрифтов.

Этот пример демонстрирует, как:

- Просканировать PDF на наличие неиспользуемых шрифтов.
- Безопасно удалить их.
- Переназначить активные текстовые фрагменты на единый шрифт (например, Times New Roman).

1. Откройте PDF‑документ.
1. Настройте параметры редактирования текста. Это указывает движку удалить любые встроенные шрифты, которые сейчас не используются в видимом тексте.
1. Создайте Text Absorber с параметрами. TextFragmentAbsorber извлекает текстовые фрагменты из документа для редактирования.
1. Переназначьте стандартный шрифт. После того как Absorber соберёт все фрагменты, пройдитесь по ним и примените единый шрифт.
1. Сохраните очищенный PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_unused_fonts(input_file, output_file):
    """
    Remove unused fonts from a PDF document.

    Optimizes PDF file size by removing fonts that are embedded but not
    actually used in the document. Also demonstrates how to standardize
    all text to use a specific font family.

    Args:
        input_file (str): Path to the input PDF file to optimize.
        output_file (str): Path where the optimized PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses REMOVE_UNUSED_FONTS option for optimization
        - Changes all text to use TimesNewRoman font
        - Processes all text fragments across the document
        - Reduces file size by eliminating unnecessary font data
        - Useful for PDF optimization and standardization

    Example:
        >>> remove_unused_fonts("input.pdf", "optimized.pdf")
        # Removes unused fonts and standardizes text to TimesNewRoman
    """

    # Open PDF document
    document = ap.Document(input_file)

    # Initialize text edit options to remove unused fonts
    options = ap.text.TextEditOptions(ap.text.TextEditOptions.FontReplace.REMOVE_UNUSED_FONTS)

    # Create a TextFragmentAbsorber with the specified options
    absorber = ap.text.TextFragmentAbsorber(options)
    document.pages.accept(absorber)

    # Iterate through all TextFragments
    for text_fragment in absorber.text_fragments:
        text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")

    # Save the updated PDF document
    document.save(output_file)
```

## Удалить весь текст

### Удалить текст из PDF

Удалить весь текстовый контент из PDF‑файла, сохранив изображения, фигуры и структуру макета.
С помощью TextFragmentAbsorber код эффективно сканирует весь документ и удаляет каждый найденный текстовый фрагмент на каждой странице.

1. Загрузите PDF‑документ.
1. Создаётся объект TextFragmentAbsorber для обнаружения и обработки текстовых фрагментов в PDF.
1. Удалить весь текстовый контент. Метод 'absorber.remove_all_text()' удаляет каждый текстовый элемент из загруженного документа, оставляя нетекстовые компоненты нетронутыми.
1. Сохраните обновлённый документ.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber1(infile, outfile):
    """
    Remove all text from a PDF using TextFragmentAbsorber.

    Demonstrates complete text removal from an entire PDF document,
    leaving only non-text elements like images, shapes, and layout
    structures intact.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the text-free PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes all text content from the entire document
        - Preserves images, graphics, and page structure
        - Uses document-level text removal for complete cleanup
        - Useful for creating templates or removing sensitive text
        - Maintains page layout and non-text elements

    Example:
        >>> remove_all_text_using_absorber1("input.pdf", "no_text.pdf")
        # Creates a PDF with all text removed but graphics preserved
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document)
        document.save(outfile)
```

### Удалить весь текст с конкретной страницы

Удалить весь текст с одной страницы PDF‑документа с помощью класса TextFragmentAbsorber в Aspose.PDF.
В отличие от удаления во всём документе, этот метод выполняет очистку текста на уровне страницы, удаляя текст только с выбранной страницы, оставляя остальные страницы нетронутыми.

1. Загрузите PDF‑файл.
1. Создайте экземпляр TextFragmentAbsorber.
1. Удалите весь текст с первой страницы.
1. Сохраните изменённый PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber2(infile, outfile):
    """
    Remove all text from page using TextFragmentAbsorber.

    Demonstrates text removal from a specific page while leaving text
    on other pages intact. Useful for selective text cleanup or
    creating mixed-content documents.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes text only from the first page (pages[1])
        - Preserves text content on all other pages
        - Maintains page structure and non-text elements
        - Useful for page-specific text removal operations
        - Images and graphics on the target page remain intact

    Example:
        >>> remove_all_text_using_absorber2("input.pdf", "first_page_clean.pdf")
        # Removes all text from first page only
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1])
        document.save(outfile)
```

### Удалить весь текст из определённой области на странице PDF

Удалить весь текст из конкретного прямоугольного региона на странице с помощью TextFragmentAbsorber библиотеки Aspose.PDF.
Вместо очистки всей страницы, этот метод выполняет целевое удаление текста, позволяя точно контролировать, какая часть страницы будет затронута.

1. Загрузите PDF‑документ.
1. Создайте TextFragmentAbsorber.
1. Определите целевую область (прямоугольник).
1. Удалите текст из указанного региона.
1. Сохраните остальную часть документа.
1. Сохраните изменённый PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber3(infile, outfile):
    """
    Remove all text from particular area on PDF page using TextFragmentAbsorber.

    Demonstrates precise text removal from a specific rectangular region
    on a page. Allows for surgical text removal while preserving text
    outside the target area.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes text only within rectangle (10, 200, 120, 600)
        - Targets the first page only (pages[1])
        - Preserves text outside the specified rectangle
        - Maintains all non-text elements in the region
        - Useful for removing watermarks, headers, or specific sections

    Example:
        >>> remove_all_text_using_absorber3("input.pdf", "region_clean.pdf")
        # Removes text only from the specified rectangular area
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1], ap.Rectangle(10, 200, 120, 600))
        document.save(outfile)
```

### Удалить весь скрытый текст из PDF‑документа

Удалить весь текст из конкретного прямоугольного региона на странице с помощью TextFragmentAbsorber библиотеки Aspose.PDF.
Вместо очистки всей страницы, этот метод выполняет целевое удаление текста, позволяя точно контролировать, какая часть страницы будет затронута.

1. Загрузите PDF‑документ.
1. Создайте TextFragmentAbsorber.
1. Определите целевую область (прямоугольник).
1. Удалите текст из указанного региона.
1. Сохраните остальную часть документа.
1. Сохраните изменённый PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_hidden_text(infile, outfile):
    """
    Remove all hidden (invisible) text from a PDF document.

    Identifies and removes text that has been marked as invisible while
    preserving all visible text content. Useful for cleaning documents
    that may contain hidden tracking text or metadata.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the cleaned PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Detects text fragments with invisible text state
        - Replaces hidden text with empty strings
        - Uses NONE replacement adjustment to prevent layout shifts
        - Preserves all visible text and document structure
        - Useful for privacy and security document cleanup

    Example:
        >>> remove_hidden_text("input.pdf", "no_hidden_text.pdf")
        # Removes all invisible text while keeping visible content intact
    """
    # Open PDF document
    with ap.Document(infile) as document:
        text_absorber = ap.text.TextFragmentAbsorber()
        # This option can be used to prevent other text fragments from moving after hidden text replacement
        text_absorber.text_replace_options = ap.text.TextReplaceOptions(ap.text.TextReplaceOptions.ReplaceAdjustment.NONE)
        document.pages.accept(text_absorber)
        # Remove hidden text
        for fragment in text_absorber.text_fragments:
            if fragment.text_state.invisible:
                fragment.text = ""
        # Save PDF document
        document.save(outfile)
```
