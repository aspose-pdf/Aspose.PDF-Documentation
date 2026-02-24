---
title: Повернуть текст в PDF с помощью Python
linktitle: Повернуть текст в PDF
type: docs
weight: 50
url: /ru/python-net/rotate-text-inside-pdf/
description: Изучите, как повернуть текст внутри PDF‑документа на Python для гибкого форматирования документов с Aspose.PDF для Python.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как повернуть текст в PDF с помощью Python
Abstract: Статья предоставляет подробное руководство по повороту текста внутри PDF‑документа с использованием библиотеки Aspose.PDF для Python через .NET. Описывается использование свойства `Rotation` класса `TextFragment` для поворота текста под разными углами, что полезно в различных сценариях генерации документов. Демонстрируется создание текстовых фрагментов с заданными углами вращения и добавление их на страницу PDF с помощью `TextBuilder`. Показано, как добавить повернутые текстовые фрагменты к `TextParagraph` и затем добавить абзац на страницу PDF. Показано, как добавить повернутые текстовые фрагменты непосредственно в коллекцию абзацев страницы. Описывается вращение целого абзаца с несколькими текстовыми фрагментами.
---

Поверните текстовые фрагменты в PDF‑документе с помощью Aspose.PDF для Python через .NET. Показано, как точно контролировать позицию и вращение отдельных текстовых элементов, сочетая классы 'TextFragment', 'TextState' и 'TextBuilder'. Регулируя угол поворота для каждого текстового фрагмента, вы можете создавать визуально динамичные макеты, такие как диагональные заголовки, вертикальные метки или повернутые аннотации.

## Поворот текстовых фрагментов с помощью TextBuilder в PDF

Создаёт PDF‑файл с именем rotated_fragments.pdf, содержащий три текстовых фрагмента, выровненных горизонтально:

- первый текст без поворота
- второй повернут на 45°
- третий повернут на 90°

1. Создать новый PDF‑документ.
1. Вставить новую страницу для размещения повернутого текста.
1. Создать первый текстовый фрагмент — без поворота.
1. Создать второй текстовый фрагмент — вращение 45°.
1. Создать третий текстовый фрагмент — вращение 90°.
1. Добавить текстовые фрагменты с помощью TextBuilder.
1. Сохранить документ.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_1(outfile):
    """
    Implement text rotation using TextFragment and TextBuilder.

    Demonstrates basic text rotation techniques by creating multiple text
    fragments with different rotation angles. Shows how to position and
    rotate individual text elements using TextBuilder for precise control.

    Args:
        outfile (str): Path where the PDF with rotated text will be saved.

    Returns:
        None: The function creates and saves a PDF file with rotated text fragments.

    Note:
        - Creates three text fragments with 0°, 45°, and 90° rotations
        - Uses Position class for precise text placement
        - Applies TimesNewRoman font with 12pt size
        - TextBuilder provides low-level control over text placement
        - Demonstrates individual fragment rotation capabilities

    Example:
        >>> rotate_text_inside_pdf_1("rotated_fragments.pdf")
        # Creates a PDF with text fragments at different rotation angles
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        text_fragment_1.position = ap.text.Position(100, 600)
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create rotated text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        text_fragment_2.position = ap.text.Position(200, 600)
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        text_fragment_2.text_state.rotation = 45
        # Create rotated text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        text_fragment_3.position = ap.text.Position(300, 600)
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        text_fragment_3.text_state.rotation = 90
        # create TextBuilder object
        builder = ap.text.TextBuilder(page)
        # Append the text fragment to the PDF page
        builder.append_text(text_fragment_1)
        builder.append_text(text_fragment_2)
        builder.append_text(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## Поворот отдельных текстовых фрагментов внутри абзаца в PDF

Поворот отдельных текстовых фрагментов внутри абзаца. Показано, как построить многострочный абзац (TextParagraph), содержащий несколько фрагментов (TextFragment), каждый со своим углом вращения. Этот приём полезен для создания визуально насыщенных документов, комбинирующих горизонтальный и диагональный текст — например, стилизованные заголовки, диаграммы или аннотированные метки.

Создаёт PDF с именем rotated_paragraph_fragments.pdf, содержащий абзац с тремя строками текста, каждая строка повернута по‑разному:

- первая строка повернута на 45°
- вторая строка остаётся горизонтальной (0°)
- третья строка повернута на -45°

1. Создать новый PDF‑документ.
1. Добавить пустую страницу, где будет отображаться повертый текст.
1. Создать TextParagraph.
1. Создать и настроить первый текстовый фрагмент — вращение 45°.
1. Создать второй текстовый фрагмент — без поворота.
1. Создать третий текстовый фрагмент — вращение 45°.
1. Добавить текстовые фрагменты к абзацу.
1. Добавить абзац на страницу с помощью TextBuilder.
1. Сохранить документ.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_2(outfile):
    """
    Implement text rotation using TextParagraph and TextBuilder with rotated fragments.

    Demonstrates how to create multi-line paragraphs containing individually
    rotated text fragments. Shows the combination of paragraph structure
    with fragment-level rotation control.

    Args:
        outfile (str): Path where the PDF with rotated paragraph fragments will be saved.

    Returns:
        None: The function creates and saves a PDF file with a paragraph containing rotated fragments.

    Note:
        - Creates a TextParagraph containing multiple text fragments
        - Individual fragments have different rotations: 45°, 0°, and -45°
        - Uses append_line to structure fragments within the paragraph
        - Demonstrates mixed rotation within a single paragraph
        - TextBuilder handles paragraph-level placement and rendering

    Example:
        >>> rotate_text_inside_pdf_2("rotated_paragraph_fragments.pdf")
        # Creates a PDF with a paragraph containing individually rotated text fragments
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        paragraph = ap.text.TextParagraph()
        paragraph.position = ap.text.Position(200, 600)
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_1.text_state.rotation = 45
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("another rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_3.text_state.rotation = -45
        # Append the text fragments to the paragraph
        paragraph.append_line(text_fragment_1)
        paragraph.append_line(text_fragment_2)
        paragraph.append_line(text_fragment_3)
        # Create TextBuilder object
        text_builder = ap.text.TextBuilder(page)
        # Append the text paragraph to the PDF page
        text_builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```

## Поворот текста с использованием абзацев страницы в PDF

Упрощённый метод поворота текста внутри PDF с помощью Aspose.PDF для Python через .NET.
В отличие от низкоуровневых подходов с TextBuilder или TextParagraph, этот метод добавляет повернутые текстовые фрагменты напрямую в коллекцию абзацев страницы (page.paragraphs). Он идеален для случаев, когда требуется базовый поворот текста без необходимости точного позиционирования или структуры абзаца. Этот подход упрощает создание макета, автоматически управляя размещением текста на странице, при этом позволяя контролировать вращение отдельных текстовых элементов.

Создаёт файл с именем 'simple_rotated_text.pdf', содержащий:

- основной горизонтальный текстовый фрагмент, вращение 0°
- фрагмент, повернутый на 315°
- фрагмент, повернутый на 270°

1. Инициализировать новый PDF‑документ.
1. Создать страницу, где будет размещён повернутый текст.
1. Создать первый фрагмент текста — без вращения.
1. Создать второй фрагмент текста — вращение 315°.
1. Создать третий фрагмент текста — вращение 270°.
1. Добавить фрагменты текста непосредственно в абзацы страницы.
1. Сохранить PDF‑документ.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_3(outfile):
    """
    Implement text rotation using TextFragment and Page.Paragraphs.

    Demonstrates a simplified approach to text rotation by adding rotated
    text fragments directly to the page's paragraph collection. Shows
    high-level text placement without TextBuilder complexity.

    Args:
        outfile (str): Path where the PDF with rotated text will be saved.

    Returns:
        None: The function creates and saves a PDF file with rotated text using page paragraphs.

    Note:
        - Uses Page.Paragraphs for direct text fragment addition
        - Creates fragments with 0°, 315°, and 270° rotations
        - Simpler approach compared to TextBuilder method
        - Demonstrates automatic layout with rotated text elements
        - Good for basic rotation without precise positioning needs

    Example:
        >>> rotate_text_inside_pdf_3("simple_rotated_text.pdf")
        # Creates a PDF with rotated text using the simplified page paragraphs approach
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_2.text_state.rotation = 315
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_3.text_state.rotation = 270
        page.paragraphs.add(text_fragment_1)
        page.paragraphs.add(text_fragment_2)
        page.paragraphs.add(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## Поворот целых абзацев в PDF

Библиотека демонстрирует продвинутый поворот текста на уровне абзаца в PDF. В отличие от поворота на уровне фрагментов (когда каждый фрагмент текста вращается отдельно), этот метод вращает целые абзацы как единые блоки под разными углами.
Каждый абзац содержит несколько стилизованных фрагментов текста, и весь абзац вращается под определёнными углами — позволяя выполнять сложные и согласованные трансформации макета.
Это идеально подходит для художественных макетов, водяных знаков или PDF с насыщенным дизайном, где полностью текстовые секции должны быть ориентированы в разных направлениях.

Создаёт 'rotated_paragraphs.pdf', содержащий четыре полностью стилизованных и повернутых абзаца:

- каждый повёрнут под уникальным углом (45°, 135°, 225° и 315°)
- каждый абзац состоит из трёх строк текста с цветными фонами, подчёркиванием и единообразным стилем

1. Создать новый PDF‑документ.
1. Добавить пустую страницу для размещения повернутых абзацев.
1. Выполнить итерацию для создания нескольких абзацев.
1. Создать и разместить абзац.
1. Создать фрагменты текста с форматированием.
1. Применить форматирование текста.
1. Добавить фрагменты текста в абзац.
1. Добавить абзац на страницу с помощью TextBuilder.
1. Повторить для всех четырёх вращений.
1. Сохранить PDF‑документ.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_4(outfile):
    """
    Implement whole paragraph rotation using TextParagraph and TextBuilder.

    Demonstrates advanced text rotation by rotating entire paragraphs at
    different angles. Creates multiple styled paragraphs with comprehensive
    formatting and rotates each paragraph as a complete unit.

    Args:
        outfile (str): Path where the PDF with rotated paragraphs will be saved.

    Returns:
        None: The function creates and saves a PDF file with fully rotated paragraphs.

    Note:
        - Creates 4 paragraphs rotated at 45°, 135°, 225°, and 315°
        - Each paragraph contains multiple formatted text fragments
        - Applies comprehensive styling: colors, backgrounds, underlines
        - Demonstrates paragraph-level rotation vs. fragment-level rotation
        - Shows complex multi-line content with consistent rotation
        - Uses loop to create systematic rotation pattern

    Example:
        >>> rotate_text_inside_pdf_4("rotated_paragraphs.pdf")
        # Creates a PDF with complete paragraphs rotated at different angles
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        for i in range(4):
            paragraph = ap.text.TextParagraph()
            paragraph.position = ap.text.Position(200, 600)
            # Specify rotation
            paragraph.rotation = i * 90 + 45
            # Create text fragment
            text_fragment_1 = ap.text.TextFragment("Paragraph Text")
            # Create text fragment
            text_fragment_1.text_state.font_size = 12
            text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_1.text_state.background_color = ap.Color.light_gray
            text_fragment_1.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_2 = ap.text.TextFragment("Second line of text")
            # Set text properties
            text_fragment_2.text_state.font_size = 12
            text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_2.text_state.background_color = ap.Color.light_gray
            text_fragment_2.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_3 = ap.text.TextFragment("And some more text...")
            # Set text properties
            text_fragment_3.text_state.font_size = 12
            text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_3.text_state.background_color = ap.Color.light_gray
            text_fragment_3.text_state.foreground_color = ap.Color.blue
            text_fragment_3.text_state.underline = True
            paragraph.append_line(text_fragment_1)
            paragraph.append_line(text_fragment_2)
            paragraph.append_line(text_fragment_3)
            # Create TextBuilder object
            builder = ap.text.TextBuilder(page)
            # Append the text fragment to the PDF page
            builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```
