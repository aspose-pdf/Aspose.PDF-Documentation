---
title: Поиск и получение текста со страниц PDF
linktitle: Поиск и получение текста
type: docs
weight: 60
url: /ru/python-net/search-and-get-text-from-pdf/
description: Узнайте, как искать и извлекать текст из PDF‑документов в Python с помощью Aspose.PDF для анализа документов.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как искать и получать текст со страниц в PDF
Abstract: В статье представлено подробное изучение возможностей извлечения и манипуляции текстом в PDF‑документах с использованием библиотеки Aspose.PDF для Python через .NET. Представлен класс TextFragmentAbsorber, позволяющий разработчикам выполнять поиск по всему документу или по отдельным страницам по заданным фразам или регулярным выражениям. На странице описаны различные практические сценарии — такие как получение текста, определение его положения (включая координаты и отступы) и извлечение свойств шрифта, таких как имя, размер, статус внедрения и цвет, из найденных текстовых фрагментов. Подробные примеры кода демонстрируют процесс пошагово, облегчая интеграцию возможностей поиска текста в приложения.
---

## Поиск текста из PDF

Поиск и извлечение текста из определённой прямоугольной области PDF‑документа с помощью класса TextAbsorber. Он использует режим чистого текстового форматирования для получения чистого, неформатированного вывода, что идеально подходит для извлечения содержимого из структурированных областей, таких как заголовки, нижние колонтитулы или таблицы. Комбинируя TextExtractionOptions и TextSearchOptions с прямоугольными ограничениями, этот пример предоставляет точный контроль над тем, где и как текст извлекается из документа.

1. Загрузите PDF‑файл, используя 'ap.Document'.
1. Настройте параметры извлечения текста.
1. Определите область поиска с помощью прямоугольных ограничений.
1. Создайте и настройте TextAbsorber.
1. Обработайте все страницы документа.
1. Получите и отобразите извлечённый текст.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_absorber_search(input_file_path):
    """
    Search and extract text from PDF using TextAbsorber with area constraints.

    Demonstrates basic text extraction from a PDF document using TextAbsorber
    with pure text formatting mode and rectangular boundary constraints.
    Extracts text from all pages within the specified rectangular area.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints extracted text to console.

    Note:
        - Uses PURE text formatting mode for clean text extraction
        - Constrains search to rectangle (0, 0, 842, 250)
        - Processes all pages in the document
        - TextAbsorber provides high-level text extraction capabilities
        - Good for extracting text content without detailed positioning

    Example:
        >>> text_absorber_search("document.pdf")
        # Prints all text found in the specified rectangular area across all pages
    """
    # Open PDF document
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Process all pages
    document.pages.accept(absorber)

    print(f"Text fragments found: {absorber.text}")
```

## Поиск текста на конкретной странице PDF

Поиск и извлечение текста с конкретной страницы и области в PDF с помощью TextAbsorber от Aspose.PDF. Осуществляется поиск на странице 2 документа и извлекается только текст, находящийся в заданной прямоугольной области.
Комбинируя TextExtractionOptions (для управления форматированием) и TextSearchOptions (для ограничения области), вы можете эффективно выполнять точное извлечение текста, специфичное для страницы.

1. Загрузите PDF‑документ.
1. Настройте параметры извлечения текста.
1. Ограничьте извлечение текста конкретной прямоугольной областью на странице.
1. Создайте и настройте TextAbsorber.
1. Обработайте конкретную страницу.
1. Получите и отобразите извлечённый текст.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_absorber_search_page(input_file_path):
    """
    Search and extract text from a specific PDF page using TextAbsorber.

    Demonstrates targeted text extraction from a single page (page 2) using
    TextAbsorber with area constraints. Shows how to limit search scope to
    specific pages and rectangular regions.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints extracted text from page 2 to console.

    Note:
        - Targets only page 2 of the document (document.pages[2])
        - Uses PURE text formatting mode for clean extraction
        - Constrains search to rectangle (0, 0, 842, 250)
        - Useful for page-specific text extraction
        - More efficient than processing entire document when targeting specific pages

    Example:
        >>> text_absorber_search_page("document.pdf")
        # Prints text found in the specified area on page 2 only
    """
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Only page 2
    document.pages[2].accept(absorber)

    print(f"Text fragments found: {absorber.text}")

```

## Анализ и извлечение подробных свойств текстовых фрагментов из PDF

В отличие от TextAbsorber, который извлекает необработанный текст, TextFragmentAbsorber предоставляет подробную низкоуровневую информацию о каждом текстовом фрагменте — например, его позицию, атрибуты шрифта, цвет и детали внедрения.

1. Загрузите PDF‑документ.
1. Инициализируйте TextFragmentAbsorber.
1. Обработайте все страницы документа.
1. Переберите извлечённые текстовые фрагменты.
1. Выведите базовую информацию о тексте.
1. Выведите сведения о шрифте и форматировании.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search(input_file_path):
    """
    Search and analyze all text fragments in a PDF with detailed properties.

    Demonstrates comprehensive text fragment analysis using TextFragmentAbsorber
    to extract all text with detailed positioning, font, and formatting information.
    Provides low-level access to text properties for detailed analysis.

    Args:
        input_file_path (str): Path to the input PDF file to analyze.

    Returns:
        None: Prints detailed text fragment information to console.

    Note:
        - Extracts all text fragments from all pages
        - Provides detailed properties: position, font info, colors, sizes
        - Shows font accessibility, embedding, and subset information
        - Useful for detailed text analysis and formatting inspection
        - TextFragmentAbsorber offers more granular control than TextAbsorber

    Example:
        >>> text_fragment_absorber_search("document.pdf")
        # Prints comprehensive details about every text fragment in the document
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    document.pages.accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
        print("XIndent:", fragment.position.x_indent)
        print("YIndent:", fragment.position.y_indent)
        print("Font - Name:", fragment.text_state.font.font_name)
        print("Font - IsAccessible:", fragment.text_state.font.is_accessible)
        print("Font - IsEmbedded:", fragment.text_state.font.is_embedded)
        print("Font - IsSubset:", fragment.text_state.font.is_subset)
        print("Font Size:", fragment.text_state.font_size)
        print("Foreground Color:", fragment.text_state.foreground_color)
```

## Поиск определённой текстовой фразы на одной странице PDF

Поиск определённой текстовой фразы на странице PDF‑документа с помощью TextFragmentAbsorber. В отличие от поиска по всему документу, этот метод ограничивает поиск одной страницей, что делает его более эффективным для подтверждения наличия и местоположения текста в целевых областях, таких как заголовки, нижние колонтитулы или отдельные разделы содержимого.

1. Загрузите PDF‑документ.
1. Инициализируйте TextFragmentAbsorber с поисковой фразой.
1. Примените Absorber к конкретной странице.
1. Переберите найденные фрагменты.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_page(input_file_path):
    """
    Search for specific text phrase on a particular PDF page.

    Demonstrates targeted text search for a specific phrase ("whale") on
    a single page. Shows how to combine phrase searching with page-specific
    scope for efficient and focused text location.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints matching text fragments and their positions to console.

    Note:
        - Searches for the phrase "whale" on page 2 only
        - Returns text fragments with position information
        - More efficient than document-wide search when targeting specific pages
        - Useful for validating content presence in specific document sections
        - Provides exact positioning coordinates for found text

    Example:
        >>> text_fragment_absorber_search_page("document.pdf")
        # Prints all instances of "whale" found on page 2 with their positions
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale")
    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Последовательный постраничный поиск текста с накопительными результатами

Пошаговый поиск текста по нескольким страницам PDF‑документа с использованием TextFragmentAbsorber от Aspose.PDF.
В отличие от одностраничного или глобального поиска, этот метод позволяет обрабатывать страницы последовательно, постепенно собирать результаты и анализировать текстовые фрагменты с учётом контекста конкретной страницы. Метод идеален для больших документов или последовательных процессов обработки.

1. Загрузите PDF‑документ.
1. Инициализируйте TextFragmentAbsorber и задайте поисковую фразу.
1. Обработайте первую страницу. Поиск только на странице 1. Выводит текст, номер страницы и позицию. Предоставляет изолированные результаты, специфичные для страницы, для наглядности.
1. Обрабатывайте следующую страницу последовательно. Перейдите к странице 2 и при желании продолжайте работу с остальной частью документа. 'absorber.visit()' обеспечивает накопление результатов со всех посещённых страниц. Выводит совокупные результаты поиска, показывая как текст, так и место.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_sequential_search(input_file_path):
    """
    Demonstrate sequential page-by-page text search with cumulative results.

    Shows how to perform incremental text searches across multiple pages,
    accumulating results from each page. Demonstrates both individual page
    processing and document-wide search continuation.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints text fragments from sequential page searches to console.

    Note:
        - Searches for "whale" on page 1, then continues to page 2
        - Uses absorber.visit(document) to process remaining pages
        - Demonstrates incremental search accumulation
        - Shows page numbers for found fragments
        - Useful for progressive document processing and result accumulation

    Example:
        >>> text_fragment_absorber_sequential_search("document.pdf")
        # Prints "whale" instances from page 1, then from all remaining pages
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.phrase = "whale"

    # First page
    document.pages[1].accept(absorber)
    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)

    print("--")

    # Continue to next page
    document.pages[2].accept(absorber)
    absorber.visit(document)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)
```

## Поиск целевой фразы в прямоугольной области

Поиск конкретной фразы в PDF с ограничением области поиска до определённого прямоугольника на одной странице.
Комбинируя поиск фразы с пространственными ограничениями, можно точно находить содержимое в заданных регионах без сканирования всей страницы или документа. Это особенно полезно для форм, заголовков, нижних колонтитулов или структурированных отчётов, где контент появляется в предсказуемых местах.

1. Загрузите PDF‑документ.
1. Инициализируйте TextFragmentAbsorber с фразой и прямоугольными ограничениями
1. Примените Absorber к странице 2. Ограничивает обработку только страницей 2, уменьшая ненужные вычисления. Обеспечивает поиск, специфичный для страницы.
1. Пройдитесь по найденным фрагментам и выведите их

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_phrase(input_file_path):
    """
    Search for specific phrase within a rectangular area constraint.

    Demonstrates targeted phrase searching with both text matching and
    spatial constraints. Combines phrase search with rectangular boundary
    limitations for precise content location.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints matching text fragments and positions to console.

    Note:
        - Searches for "elephant" phrase on page 2
        - Constrains search to rectangle (0, 0, 842, 250)
        - Combines text matching with spatial filtering
        - Useful for finding content in specific document regions
        - More precise than page-wide or document-wide searches

    Example:
        >>> text_fragment_absorber_search_phrase("document.pdf")
        # Prints "elephant" instances found within the specified rectangular area on page 2
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        "elephant", ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Поиск текстовых шаблонов в PDF с использованием регулярных выражений

Поиск текстовых шаблонов в PDF с помощью регулярных выражений. Включив режим regex в TextFragmentAbsorber, можно находить сложные шаблоны, такие как числа, даты, цены, координаты или пользовательские форматы текста. Функция ограничивает поиск конкретной страницей, делая его эффективным для целевого извлечения структурированных данных.

1. Загрузите PDF‑документ.
1. Инициализируйте TextFragmentAbsorber с шаблоном регулярного выражения.
1. Примените Absorber к странице 2. Ограничивает поиск страницей 2 для эффективности и точности. Анализируется только текст на этой странице.
1. Пройдитесь по найденным фрагментам. Выводит совпадающие текстовые фрагменты и их координаты. Предоставляет точную информацию о местоположении извлечённых шаблонов.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_regex(input_file_path):
    """
    Search for text patterns using regular expressions.

    Demonstrates advanced text searching using regular expression patterns
    to find complex text structures like numbers, dates, or custom formats.
    Shows how to enable regex mode in TextFragmentAbsorber.

    Args:
        input_file_path (str): Path to the input PDF file to search.

    Returns:
        None: Prints matching text fragments and positions to console.

    Note:
        - Uses regex pattern r"\\d+\\.\\d+" to find decimal numbers
        - Enables regex mode with is_regular_expression_used=True
        - Searches on page 2 only
        - Powerful for finding formatted data like prices, coordinates, dates
        - Regular expressions provide flexible pattern matching capabilities

    Example:
        >>> text_fragment_absorber_search_regex("document.pdf")
        # Prints all decimal numbers (e.g., "12.34", "0.99") found on page 2
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(r"\d+\.\d+", ap.text.TextSearchOptions(is_regular_expression_used=True))

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Преобразование найденного текста в гиперссылки в PDF с помощью TextFragmentAbsorber

Поиск конкретных текстовых фраз в PDF и их преобразование в кликабельные гиперссылки. С помощью TextFragmentAbsorber и шаблонов regex находятся целевые слова и применяется визуальное оформление (цвет и подчёркивание) вместе с интерактивными ссылками.

1. Загрузите PDF‑документ.
1. Инициализируйте TextFragmentAbsorber с шаблоном регулярного выражения.
1. Примените Absorber к странице 1.
1. Оформите и добавьте гиперссылки к найденным совпадениям.
1. Сохраните изменённый PDF.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_and_add_hyperlink(input_file_path):
    """
    Search for text and convert matches to hyperlinks with styling.

    Demonstrates advanced text processing by finding specific words and
    converting them into clickable hyperlinks with visual styling. Shows
    how to combine text search with document modification.

    Args:
        input_file_path (str): Path to the input PDF file to process.

    Returns:
        None: Saves modified PDF with hyperlinks to output file.

    Note:
        - Searches for "whale|elephant" using regex pattern on page 1
        - Converts found text to Wikipedia hyperlinks
        - Applies blue color and underline styling to hyperlinks
        - Creates new output file with "_out.pdf" suffix
        - Demonstrates practical text enhancement and interactivity
        - Combines search, styling, and hyperlinking in one operation

    Example:
        >>> text_fragment_absorber_search_and_add_hyperlink("document_in.pdf")
        # Creates "document_out.pdf" with "whale" and "elephant" as clickable Wikipedia links
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale|elephant")
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.underline = True
        fragment.hyperlink = ap.WebHyperlink(
            f"https://en.wikipedia.org/wiki/{fragment.text}"
        )

    output = input_file_path.replace("in.pdf", "out.pdf")
    document.save(output)
```

## Поиск и идентификация стилизованного текста в PDF с помощью TextFragmentAbsorber

Поиск текстовых фрагментов в PDF на основе их свойств форматирования, а не содержания. С помощью TextFragmentAbsorber определяется текст с определёнными стилями, например жирный.

1. Загрузите PDF‑документ.
1. Инициализируйте TextFragmentAbsorber.
1. Примените Absorber к странице 1.
1. Проверьте текстовые фрагменты на основе форматирования. Проверяется стиль шрифта на жирность.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_styled_text(input_file_path):
    """
    Search and identify text based on formatting properties.

    Demonstrates how to find text fragments based on their formatting
    characteristics rather than content. Shows detection of bold text
    and invisible text within the document.

    Args:
        input_file_path (str): Path to the input PDF file to analyze.

    Returns:
        None: Prints formatted text findings to console.

    Note:
        - Searches all text fragments on page 1
        - Identifies text with FontStyles.BOLD formatting
        - Detects invisible/hidden text using text_state.invisible
        - Useful for formatting analysis and hidden content detection
        - Demonstrates text property-based filtering capabilities

    Example:
        >>> text_fragment_absorber_search_styled_text("document.pdf")
        # Prints all bold text and any hidden/invisible text found on page 1
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.font_style == ap.text.FontStyles.BOLD:
            print(f"Bold: {fragment.text}")
```

Обнаруживает скрытый или невидимый текст в PDF‑документе, анализируя свойства форматирования текста:

1. Загрузите PDF‑документ.
1. Инициализируйте TextFragmentAbsorber.
1. Примените Absorber к странице 1.
1. Проверьте текстовые фрагменты на основе форматирования. Проверьте 'fragment.text_state.invisible' для обнаружения скрытого текста.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_styled_text(input_file_path):
    """
    Search and identify text based on formatting properties.

    Demonstrates how to find text fragments based on their formatting
    characteristics rather than content. Shows detection of bold text
    and invisible text within the document.

    Args:
        input_file_path (str): Path to the input PDF file to analyze.

    Returns:
        None: Prints formatted text findings to console.

    Note:
        - Searches all text fragments on page 1
        - Identifies text with FontStyles.BOLD formatting
        - Detects invisible/hidden text using text_state.invisible
        - Useful for formatting analysis and hidden content detection
        - Demonstrates text property-based filtering capabilities

    Example:
        >>> text_fragment_absorber_search_styled_text("document.pdf")
        # Prints all bold text and any hidden/invisible text found on page 1
    """
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.invisible:
            print(f"Invisible: {fragment.text}")
```

## Визуальное выделение текста на страницах PDF

Эта функция объединяет распознавание текста и его рендеринг в едином рабочем процессе. Она не только извлекает текст, но и визуализирует его, выделяя фрагменты, сегменты и символы цветными прямоугольниками на PNG‑изображениях каждой страницы.

Наш пример выполняет расширенную визуализацию текста в PDF, используя:

- поиск всех видимых текстовых фрагментов с помощью регулярных выражений
- рендеринг каждой страницы PDF в изображение PNG высокого разрешения
- отрисовку цветных прямоугольников вокруг текстовых фрагментов, сегментов и отдельных символов

1. Установите разрешение выходного изображения. Каждая страница PDF преобразуется в PNG‑изображение с разрешением 150 DPI.
1. Откройте PDF и инициализируйте Text Absorber.
1. Обрабатывайте каждую страницу. Применяйте absorber к каждой странице. Собирайте все обнаруженные текстовые фрагменты и их геометрические позиции.
1. Преобразуйте страницу в поток PNG.
1. Подготовьте объект Graphics для рисования.
1. Примените преобразование координат. Преобразуйте координаты PDF в пиксели изображения.
1. Нарисуйте прямоугольники для текстовых элементов.
1. Сохраните результат.

```python

import io
import os
import re
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing

# Global configuration
DATA_DIR = "your path here"

def text_fragment_absorber_search_and_highlight(infile):
    """
    Search text and create visual highlighting with PNG output.

    Advanced function that combines text search with visual highlighting.
    Converts PDF pages to PNG images and draws colored rectangles around
    found text fragments, segments, and individual characters.

    Args:
        infile (str): Path to the input PDF file to process.

    Returns:
        None: Saves highlighted PNG images for each page.

    Note:
        - Uses regex pattern r"[\\S]+" to find all non-whitespace sequences
        - Converts each page to 150 DPI PNG image using PngDevice
        - Draws yellow rectangles around text fragments
        - Draws green rectangles around text segments
        - Draws black rectangles around individual characters
        - Creates detailed visual analysis of text structure
        - Output files named with page numbers: "filename1_out.png", etc.
        - Complex coordinate transformation for proper overlay positioning

    Example:
        >>> text_fragment_absorber_search_and_highlight("document_in.pdf")
        # Creates PNG files with visual highlighting of all text elements
    """
    resolution = 150
    png_device = ap.devices.PngDevice(ap.devices.Resolution(resolution, resolution))

    # Open PDF document
    document = ap.Document(infile)
    absorber = ap.text.TextFragmentAbsorber(r"[\S]+")
    absorber.text_search_options.is_regular_expression_used = True

    for page in document.pages:
        page.accept(absorber)
        stream = io.BytesIO()
        png_device.process(page, stream)
        with drawing.Bitmap.from_stream(stream) as bmp:
            with drawing.Graphics.from_image(bmp) as gr:
                scale = resolution / 72
                gr.transform = drawing.drawing2d.Matrix(
                    float(scale),
                    float(0),
                    float(0),
                    float(-scale),
                    float(0),
                    float(bmp.height),
                )
                text_fragment_collection = absorber.text_fragments
                # Loop through the fragments
                for text_fragment in text_fragment_collection:
                    gr.draw_rectangle(
                        drawing.Pens.yellow,
                        float(text_fragment.position.x_indent),
                        float(text_fragment.position.y_indent),
                        float(text_fragment.rectangle.width),
                        float(text_fragment.rectangle.height),
                    )
                    for seg_num in range(1, len(text_fragment.segments) + 1):
                        segment = text_fragment.segments[seg_num]
                        for char_num in range(1, len(segment.characters) + 1):
                            character_info = segment.characters[char_num]
                            rect = page.get_page_rect(True)
                            print(
                                f"TextFragment = {text_fragment.text}"
                                + f" Page URY = {rect.ury}"
                                + f" TextFragment URY = {text_fragment.rectangle.ury}"
                            )
                            gr.draw_rectangle(
                                drawing.Pens.black,
                                float(character_info.rectangle.llx),
                                float(character_info.rectangle.lly),
                                float(character_info.rectangle.width),
                                float(character_info.rectangle.height),
                            )
                        gr.draw_rectangle(
                            drawing.Pens.green,
                            float(segment.rectangle.llx),
                            float(segment.rectangle.lly),
                            float(segment.rectangle.width),
                            float(segment.rectangle.height),
                        )

                # Save result
                bmp.save(
                    infile.replace("_in.pdf", str(page.number) + "_out.png"),
                    drawing.imaging.ImageFormat.png,
                )
```
