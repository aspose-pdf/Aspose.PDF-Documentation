---
title: Форматирование текста в PDF с использованием Python
linktitle: Форматирование текста в PDF
type: docs
weight: 70
url: /ru/python-net/text-formatting-inside-pdf/
description: Исследуйте варианты форматирования текста в PDF‑файлах на Python с помощью Aspose.PDF для настройки стиля документов.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как редактировать текст в PDF с помощью Python
Abstract: В статье представлено всестороннее руководство по различным техникам форматирования текста в PDF‑документах с использованием Aspose.PDF для Python через .NET. Охватывается ряд возможностей, включая добавление отступов строк, создание границ текста, подчеркивание текста и добавление зачеркивания, и многое другое.
---

## Интервал между строками и символами

### Использование интервала между строками

#### Как форматировать текст с пользовательским межстрочным интервалом в Python — простой пример

Aspose.PDF for Python демонстрирует простой подход к управлению расположением текста и его читаемостью с помощью настройки межстрочного интервала.

Наш фрагмент кода показывает, как управлять межстрочным интервалом в PDF‑документе. Он считывает текст из файла (или использует резервное сообщение), применяет пользовательский размер шрифта и межстрочный интервал и добавляет отформатированный текст на новую страницу PDF.

1. Создать новый PDF‑документ.
1. Загрузить исходный текст.
1. Инициализировать объект TextFragment и присвоить ему загруженный текст.
1. Установить свойства шрифта и интервалов для текста. Эти значения определяют, насколько плотно или свободно выглядят строки текста:
- Размер шрифта: 12 пунктов
- Межстрочный интервал: 16 пунктов
1. Вставить отформатированный фрагмент текста в коллекцию параграфов страницы.
1. Сохранить документ.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def specify_line_spacing_simple_case(outfile):
    """
    Specify custom line spacing for text in a PDF document.

    Creates a PDF document with text that has custom line spacing applied.
    Loads text content from an external file and applies 16-point line spacing
    to improve readability and text layout.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Attempts to load text from "lorem.txt" file in DATA_DIR
        - Falls back to default message if file doesn't exist
        - Font size: 12 points
        - Line spacing: 16 points (increased from default for better readability)
        - Demonstrates basic line spacing control in PDF text formatting

    Example:
        >>> specify_line_spacing_simple_case("line_spacing.pdf")
        # Creates a PDF with custom 16-point line spacing
    """

    document = ap.Document()
    page = document.pages.add()

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )

    text_fragment = ap.text.TextFragment(text)
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.line_spacing = 16
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

#### Как форматировать текст с пользовательским межстрочным интервалом в Python — конкретный пример

Давайте посмотрим, как применять разные режимы межстрочного интервала в PDF‑документе с использованием пользовательского шрифта TrueType (TTF).
Он загружает текст из файла, внедряет определённый шрифт и отрисовывает один и тот же текст дважды на странице PDF — каждый раз используя разный режим межстрочного интервала:

- Режим FONT_SIZE: межстрочный интервал равен размеру шрифта.
- Режим FULL_SIZE: межстрочный интервал учитывает полную высоту шрифта, включая восходящие и нисходящие элементы.

Пример показывает, как поведение межстрочного интервала может различаться в зависимости от выбранного режима.

1. Создать новый PDF‑документ.
1. Указать пути к файлу пользовательского шрифта и файлу исходного текста.
1. Загрузить содержимое текста.
1. Открыть пользовательский шрифт.
1. Создать и настроить первый TextFragment (режим FONT_SIZE). Установить line_spacing в 'TextFormattingOptions.LineSpacingMode.FONT_SIZE', что означает, что межстрочный интервал равен размеру шрифта.
1. Создать и настроить второй TextFragment (режим FULL_SIZE). Установить line_spacing в 'TextFormattingOptions.LineSpacingMode.FULL_SIZE', который использует полную высоту шрифта.
1. Добавить оба текстовых фрагмента на одну страницу PDF.
1. Сохранить готовый документ в указанное место вывода.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def specify_line_spacing_specific_case(outfile):
    """
    Create a PDF document demonstrating different line spacing modes with custom font.
    This function creates a PDF with two text fragments using the same custom TTF font
    but different line spacing modes to demonstrate the visual differences between
    FONT_SIZE and FULL_SIZE line spacing options.
    Args:
        outfile (str): Path where the output PDF file will be saved.
    Notes:
        - Requires 'HPSimplified.ttf' font file in DATA_DIR
        - Requires 'lorem.txt' text file in DATA_DIR for content
        - Falls back to default text if lorem.txt is not found
        - First fragment uses FONT_SIZE line spacing mode
        - Second fragment uses FULL_SIZE line spacing mode
    Dependencies:
        - aspose.pdf (ap) library
        - os module for file path operations
        - DATA_DIR constant must be defined
    """

    document = ap.Document()
    page = document.pages.add()

    font_file = os.path.join(DATA_DIR, "HPSimplified.ttf")
    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )

    with open(font_file, "rb") as font_stream:
        font = ap.text.FontRepository.open_font(font_stream, ap.text.FontTypes.TTF)

        fragment1 = ap.text.TextFragment(text)
        fragment1.text_state.font = font
        fragment1.text_state.formatting_options = ap.text.TextFormattingOptions()
        fragment1.text_state.formatting_options.line_spacing = (
            ap.text.TextFormattingOptions.LineSpacingMode.FONT_SIZE
        )
        page.paragraphs.add(fragment1)

        fragment2 = ap.text.TextFragment(text)
        fragment2.text_state.font = font
        fragment2.text_state.formatting_options = ap.text.TextFormattingOptions()
        fragment2.text_state.formatting_options.line_spacing = (
            ap.text.TextFormattingOptions.LineSpacingMode.FULL_SIZE
        )
        page.paragraphs.add(fragment2)

    document.save(outfile)
```

![PDF‑документ, отображающий текст с пользовательским межстрочным интервалом, демонстрирующий 16‑пунктовый интервал между строками для улучшенной читаемости и форматирования расположения текста](line_spacing.png)

### Использование межсимвольного интервала

#### Как управлять межсимвольным интервалом в PDF‑тексте с помощью класса TextFragment

Межсимвольный интервал определяет расстояние между отдельными символами в строке текста — полезно для точной настройки внешнего вида текста или достижения определённых типографических эффектов.

1. Инициализирует новый объект Document и добавляет чистую страницу для размещения текста.
1. Определить генератор фрагментов. Реализует вспомогательную функцию make_fragment(spacing):
- создать TextFragment с образцовым текстом.
- установить шрифт.
1. Добавить текстовые фрагменты с разными значениями интервала.
1. Сохранить документ.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def character_spacing_using_text_fragment(outfile):
    """
    Demonstrate character spacing control using TextFragment objects.

    Creates a PDF document showing different character spacing values applied
    to text fragments. Each line demonstrates progressively increased character
    spacing to illustrate the visual effect on text appearance.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates multiple TextFragment objects with varying character spacing
        - Character spacing values: 0, 1, 2, 3, and 4 points
        - Font: Times Roman, 12 points
        - Each fragment is positioned on a new line for comparison
        - Character spacing affects only horizontal letter spacing
        - Higher values create more space between individual characters

    Example:
        >>> character_spacing_using_text_fragment("char_spacing_fragment.pdf")
        # Creates a PDF showing progressive character spacing effects
    """
    document = ap.Document()
    page = document.pages.add()

    def make_fragment(spacing):
        fragment = ap.text.TextFragment("Sample Text with character spacing")
        fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
        fragment.text_state.font_size = 14
        fragment.text_state.character_spacing = spacing
        return fragment

    page.paragraphs.add(make_fragment(2.0))
    page.paragraphs.add(make_fragment(1.0))
    page.paragraphs.add(make_fragment(0.75))

    document.save(outfile)
```

![PDF документ, показывающий три строки одинакового текста Sample Text с изменением межсимвольного интервала, демонстрирующий постепенно более плотный интервал от верхней к нижней строке: первая строка имеет более широкий интервал между буквами, средняя — умеренный, а нижняя — самый тесный, иллюстрируя визуальный эффект разных значений межсимвольного интервала в форматировании текста PDF](character_spacing_simple.png)

#### Как управлять межсимвольным интервалом в тексте PDF с помощью TextParagraph и TextBuilder

Aspose.PDF позволяет применять пользовательский межсимвольный интервал при добавлении текста в PDF‑документ с использованием TextParagraph и TextBuilder.
Он определяет конкретную область на странице, настраивает перенос текста и отображает фрагмент текста с отрегулированным межсимвольным интервалом.

Использование TextParagraph идеально, когда требуется точный контроль над размещением текста и его макетом, например при построении структурированных или много колонных блоков текста.

1. Создайте новый PDF‑документ.
1. Инициализируйте экземпляр TextBuilder для страницы.
1. Создайте и настройте TextParagraph.
- Установите режим переноса слов в 'TextFormattingOptions.WordWrapMode.BY_WORDS'.
1. Создайте TextFragment с пользовательским межсимвольным интервалом.
- Создайте новый TextFragment и задайте его текст (например, "Sample Text with character spacing").
- Укажите атрибуты шрифта, такие как Arial и размер шрифта 14 pt.
- Примените межсимвольный интервал = 2.0, что увеличивает расстояние между символами.
1. Добавьте TextFragment в TextParagraph.
1. Добавьте TextParagraph на страницу.
1. Сохраните PDF‑документ.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def character_spacing_using_text_paragraph(outfile):
    """
    Demonstrate character spacing control using TextParagraph objects.

    Creates a PDF document with text paragraph that has custom character spacing
    applied. Shows how to set character spacing at the paragraph level and
    demonstrates the visual effect on text layout.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses TextParagraph for paragraph-level formatting
        - Character spacing: 2.0 points
        - Font: Times Roman, 12 points
        - Demonstrates paragraph-based character spacing control
        - Character spacing applies to all text within the paragraph
        - Alternative approach to fragment-based character spacing

    Example:
        >>> character_spacing_using_text_paragraph("char_spacing_paragraph.pdf")
        # Creates a PDF with paragraph-level character spacing
    """
    document = ap.Document()
    page = document.pages.add()

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(100, 700, 500, 750, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    fragment = ap.text.TextFragment("Sample Text with character spacing")
    fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment.text_state.font_size = 14
    fragment.text_state.character_spacing = 2.0

    paragraph.append_line(fragment)
    builder.append_paragraph(paragraph)
    document.save(outfile)
```

## Создание списков

Работая с PDF‑файлами, вам может потребоваться отображать структурированную информацию, например списки — будь то маркированные, нумерованные или оформленные с помощью HTML или LaTeX.
Aspose.PDF for Python via .NET предоставляет несколько гибких способов создания и форматирования списков непосредственно в ваших PDF‑документах, предоставляя полный контроль над макетом, шрифтом и стилем.

В этой статье демонстрируются различные подходы к созданию списков в PDF, от простого текстового форматирования до продвинутого рендеринга HTML и LaTeX. Каждый метод подходит для определённых задач — будь то точный программный контроль или удобное стилизование на основе разметки.

К концу статьи вы узнаете, как:

- Создавать пользовательские маркированные и нумерованные списки с помощью TextParagraph и TextBuilder.

- Использовать HTML‑фрагменты (HtmlFragment) для простого отображения списков '<ul>' и '<ol>' в PDF.

- Использовать LaTeX‑фрагменты (TeXFragment) для форматирования списков в математических или научных документах.

- Управлять переносом текста, стилями шрифтов и позиционированием макета на странице.

- Понять разницу между ручным построением списка и подходами, основанными на разметке.

### Создание маркированного списка

Создайте пользовательский маркированный список в PDF с помощью TextParagraph и TextBuilder, без использования форматирования HTML или LaTeX.
Каждый элемент списка начинается с символа маркера (•) и добавляется как отдельный TextFragment.

1. Инициализируйте объект Document и добавьте пустую страницу.
1. Определите список строк Python, который будет преобразован в маркированные пункты.
1. Создайте TextBuilder и TextParagraph.
1. Используйте 'TextBuilder' для добавления настроенного абзаца на страницу.
1. Сохраните PDF‑документ.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list(outfile):
    """
    Create a PDF document with a bullet list using plain text formatting.
    This function generates a PDF document containing a bullet list with predefined items.
    The list is formatted with bullet points, uses Times New Roman font, and includes
    text wrapping behavior for longer items.
    Args:
        outfile (str): The file path where the PDF document will be saved.
    Returns:
        None: The function saves the document to the specified file path.
    Note:
        The bullet list is positioned within a rectangle at coordinates (80, 200, 400, 800)
        and uses word wrapping mode for text formatting.
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(80, 200, 400, 800, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    for item in items:
        fragment = ap.text.TextFragment("• " + item)
        fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
        fragment.text_state.font_size = 12
        paragraph.append_line(fragment)

    builder.append_paragraph(paragraph)
    document.save(outfile)
```

### Создание нумерованного списка

Создайте пользовательский нумерованный (упорядоченный) список в PDF с помощью TextParagraph и TextBuilder, без использования форматирования HTML или LaTeX.
Каждый элемент списка предваряется его номером (например, 1., 2.) и добавляется как отдельный TextFragment.

1. Инициализируйте объект Document и добавьте пустую страницу.
1. Определите список строк Python, который будет преобразован в нумерованные пункты списка.
1. Создайте TextBuilder и TextParagraph.
1. Добавьте каждый элемент как TextFragment с номером.
1. Используйте TextBuilder для добавления настроенного абзаца на страницу.
1. Сохраните PDF‑документ.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list(outfile):
    """
    Create a numbered list in a PDF document using plain text formatting.
    This function generates a PDF document containing a numbered list with predefined
    items. The list is formatted with Times New Roman font and includes text wrapping
    by words within a specified rectangular area on the page.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified file path but does
              not return any value.
    Note:
        - Uses Aspose.PDF library (imported as 'ap')
        - List items are hardcoded within the function
        - Font: Times New Roman, size 12
        - Text wrapping: BY_WORDS mode
        - Rectangle bounds: (80, 200, 400, 800)
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(80, 200, 400, 800, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    for i, item in enumerate(items):
        fragment = ap.text.TextFragment(f"{i + 1}. {item}")
        fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
        fragment.text_state.font_size = 12
        paragraph.append_line(fragment)

    builder.append_paragraph(paragraph)
    document.save(outfile)
```

### Создание HTML‑версии маркированного списка

Наша библиотека показывает, как создать маркированный (неупорядоченный) список в PDF‑документе с помощью HTML‑фрагментов. Она преобразует список строк Python в HTML‑элемент `<ul>` и вставляет его на страницу PDF как HtmlFragment. Использование HTML‑фрагментов позволяет воспользоваться возможностями HTML‑форматирования (например, списками, жирным, курсивом) непосредственно в PDF.

1. Создайте новый PDF‑документ и добавьте страницу.
1. Подготовьте элементы списка.
1. Преобразуйте список в неупорядоченный HTML‑список.
- Используйте тег `<ul>` для неупорядоченного (маркированного) списка.
- Оберните каждый элемент тегами 'li' с помощью list comprehension.
1. Создать HtmlFragment. Преобразовать строку HTML в объект HtmlFragment, который можно добавить на страницу PDF.
1. Вставить HtmlFragment в коллекцию абзацев страницы.
1. Сохранить PDF‑документ.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list_html_version(outfile):
    """
    Create a bulleted list using HTML formatting in a PDF document.

    Generates a PDF with an unordered (bulleted) list created using HTML markup.
    Demonstrates how to use HtmlFragment to embed HTML list structures directly
    into PDF documents with proper formatting and styling.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <ul> and <li> tags for list structure
        - Items are predefined with sample content
        - HtmlFragment automatically handles HTML rendering
        - Lists maintain proper bullet formatting and indentation
        - Simpler alternative to manual list creation with TextFragments
        - Supports nested lists and HTML styling if needed

    Example:
        >>> create_bullet_list_html_version("bullet_list_html.pdf")
        # Creates a PDF with HTML-formatted bulleted list
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    html_list = "<ul>" + "".join([f"<li>{item}</li>" for item in items]) + "</ul>"
    html_fragment = ap.HtmlFragment(html_list)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![Маркированный список, отображенный в PDF‑документе, показывающий четыре элемента: Первый элемент в списке, Второй элемент с более длинным текстом для демонстрации переноса, Третий элемент и Четвёртый элемент. Каждый элемент предваряется стандартным маркером и демонстрирует рендеринг списка в формате HTML внутри структуры PDF с правильными отступами и интервалами](bullet_list_html.png)

### Создать нумерованный список, версия HTML

Создать нумерованный (упорядоченный) список в PDF‑документе с использованием HTML‑фрагментов. Он преобразует список строк Python в HTML‑элемент `<ol>` и вставляет его на страницу PDF в виде HtmlFragment.

Использование HTML‑фрагментов позволяет интегрировать функции форматирования на основе HTML, такие как нумерованные списки, полужирный шрифт, курсив и другие, непосредственно в ваш PDF.

1. Создать новый PDF‑документ и добавить страницу.
1. Подготовить элементы списка.
1. Преобразовать список в упорядоченный HTML‑список.
- Использовать тег `<ol>` для нумерованного списка.
- Обернуть каждый элемент тегами `li`, используя генератор списка.
1. Преобразовать строку HTML в объект HtmlFragment, который можно добавить на страницу PDF.
1. Вставить HtmlFragment в коллекцию абзацев страницы.
1. Сохранить PDF‑документ.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list_html_version(outfile):
    """
    Create a numbered list using HTML formatting in a PDF document.

    Generates a PDF with an ordered (numbered) list created using HTML markup.
    Demonstrates how to use HtmlFragment to embed HTML ordered list structures
    directly into PDF documents with automatic numbering and formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses HTML <ol> and <li> tags for ordered list structure
        - Items are predefined with sample content
        - HtmlFragment automatically handles HTML rendering and numbering
        - Lists maintain proper numeric formatting and indentation
        - Numbers are automatically generated (1, 2, 3, etc.)
        - Supports nested lists and custom numbering styles if needed

    Example:
        >>> create_numbered_list_html_version("numbered_list_html.pdf")
        # Creates a PDF with HTML-formatted numbered list
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    html_list = "<ol>" + "".join([f"<li>{item}</li>" for item in items]) + "</ol>"
    html_fragment = ap.HtmlFragment(html_list)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![Нумерованный список, отображенный в PDF‑документе, показывающий четыре автоматически пронумерованных элемента: 1. Первый элемент в списке, 2. Второй элемент с более длинным текстом для демонстрации переноса, 3. Третий элемент и 4. Четвёртый элемент. Список демонстрирует рендеринг упорядоченного списка в формате HTML внутри структуры PDF с правильной последовательностью номеров, отступами и интервалами между элементами](numbered_list_html.png)

### Создать маркированный список, версия LaTeX

Создать маркированный (неупорядоченный) список в PDF с использованием LaTeX‑фрагментов (TeXFragment). Он преобразует список строк Python в среду LaTeX `itemize` и вставляет её на страницу PDF. Использование LaTeX‑фрагментов идеально подходит, когда необходимо отобразить математические формулы, символы или структурированные списки с точным форматированием.

1. Создать новый PDF‑документ и добавить страницу.
1. Определить список строк Python, которые станут маркерами в среде LaTeX `itemize`.
1. Преобразовать список в среду LaTeX `itemize`:
- Обернуть элементы с помощью \begin{itemize} и \end{itemize}.
- Каждый элемент предваряется \item с использованием генератора списка.
1. Преобразовать строку LaTeX в объект TeXFragment, который можно отобразить в PDF.
1. Добавить LaTeX‑фрагмент на страницу.
1. Сохранить PDF‑документ.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_bullet_list_latex_version(outfile):
    """
    Create a bulleted list using LaTeX formatting in a PDF document.

    Generates a PDF with an unordered list created using LaTeX markup.
    Demonstrates how to use TeXFragment to embed LaTeX itemize environments
    directly into PDF documents with proper mathematical and scientific formatting.

    Args:
        outfile (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Uses LaTeX \\begin{itemize} and \\item commands
        - TeXFragment handles LaTeX compilation and rendering
        - Supports mathematical expressions and scientific notation
        - Lists maintain proper bullet formatting and indentation
        - More powerful than HTML for mathematical content
        - Can include LaTeX math modes and special symbols

    Example:
        >>> create_bullet_list_latex_version("bullet_list_latex.pdf")
        # Creates a PDF with LaTeX-formatted bulleted list
    """

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    tex_list = (
        "Lists are easy to create: \\begin{itemize}"
        + "".join([f"\\item {i}" for i in items])
        + "\\end{itemize}"
    )
    tex_fragment = ap.TeXFragment(tex_list)
    page.paragraphs.add(tex_fragment)
    document.save(outfile)
```

![Маркированный список, отображенный в PDF, показывающий форматирование, отрендеренное LaTeX, с текстом «Списки легко создавать:», за которым следуют четыре пункта с маркерами: Первый элемент, Второй элемент с более длинным текстом для демонстрации переноса, Третий элемент и Четвёртый элемент. Список демонстрирует профессиональную наборку LaTeX с правильным оформлением маркеров, одинаковыми интервалами и возможностями переноса текста в чистом макете PDF‑документа](bullet_list_latex.png)

### Создать нумерованный список, версия LaTeX

Создать нумерованный (упорядоченный) список в PDF с использованием LaTeX‑фрагментов (TeXFragment). Он преобразует список строк Python в среду LaTeX `enumerate` и вставляет её на страницу PDF. Использование LaTeX‑фрагментов идеально подходит, когда требуется точное форматирование, структурированные списки или математические обозначения в PDF.

1. Создать новый PDF‑документ и добавить страницу.
1. Определить список строк Python, которые станут нумерованными элементами в среде LaTeX `enumerate`.
1. Преобразовать список в среду LaTeX `enumerate`.
1. Преобразовать строку LaTeX в объект TeXFragment, который можно отобразить в PDF.
1. Добавить LaTeX‑фрагмент на страницу.
1. Сохранить PDF‑документ.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_numbered_list_latex_version(outfile):
    """Create a numbered list using LaTeX."""

    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    tex_list = (
        "Lists are easy to create: \\begin{enumerate}"
        + "".join([f"\\item {i}" for i in items])
        + "\\end{enumerate}"
    )
    tex_fragment = ap.TeXFragment(tex_list)
    page.paragraphs.add(tex_fragment)
    document.save(outfile)
```

![Нумерованный список, отображенный в PDF, показывающий форматирование, отрендеренное LaTeX, с элементами 1. Первый элемент, 2. Второй элемент с более длинным текстом для демонстрации переноса, 3. Третий элемент и 4. Четвёртый элемент, предваряемый текстом «Списки легко создавать»](numbered_list_latex.png)

## Сноски и концевые сноски

### Добавить сноски

Сноски используются для ссылки на примечания внутри текста документа, размещая последовательные верхние индексы рядом с соответствующим фрагментом. Эти номера соответствуют подробным примечаниям, которые обычно отступают и расположены внизу той же страницы, предоставляя дополнительный контекст, ссылки или комментарии.

Добавьте сноску к текстовому фрагменту в PDF‑документе с помощью Aspose.PDF для Python через .NET. Сноски полезны для предоставления дополнительной информации, ссылок или разъяснений без захламления основного содержания. Этот метод гарантирует, что сноски визуально и структурно интегрированы в макет PDF.

1. Создать новый документ.
1. Создать TextFragment с основным содержимым.
1. Добавить встроенный текст. Создать другой TextFragment, который продолжается в том же абзаце.
1. Сохранить документ.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote(outfile):
    """Add footnote to a PDF document."""

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.foot_note = ap.Note("This is the footnote content.")
    page.paragraphs.add(text_fragment)

    inline_text = ap.text.TextFragment(
        " This is another text after footnote in the same paragraph."
    )
    inline_text.is_in_line_paragraph = True
    inline_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    inline_text.text_state.font_size = 14
    page.paragraphs.add(inline_text)

    document.save(outfile)
```

### Добавить сноску с пользовательским оформлением в PDF

1. Инициализировать новый PDF‑документ и добавить пустую страницу.
1. Создать основной текстовый фрагмент.
1. Создать и оформить сноску (шрифт, размер, цвет, стиль).
1. Вставить оформленный текстовый фрагмент с сноской на страницу.
1. Добавить еще один текстовый фрагмент без сноски.
1. Сохранить документ.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_custom_text_style(outfile):
    """Add footnote with custom text style."""

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14

    note = ap.Note("This is the footnote content with custom text style.")
    note.text_state = ap.text.TextState()
    note.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    note.text_state.font_size = 10
    note.text_state.foreground_color = ap.Color.red
    note.text_state.font_style = ap.text.FontStyles.ITALIC
    text_fragment.foot_note = note

    page.paragraphs.add(text_fragment)

    another_text = ap.text.TextFragment(" This is another text without footnote.")
    another_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    another_text.text_state.font_size = 14
    page.paragraphs.add(another_text)

    document.save(outfile)
```

### Добавить сноски с пользовательскими символами в PDF

Добавьте сноски к текстовым фрагментам в PDF-документе с помощью Aspose.PDF for Python via .NET, с возможностью настройки символа маркера сноски.

1. Создать PDF‑документ и страницу.
1. Добавить первый текстовый фрагмент с пользовательским символом сноски.
1. Добавить другой текстовый фрагмент, продолжающий абзац без сноски.
1. Добавить второй текстовый фрагмент со стандартной сноской.
1. Сохранить документ.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_custom_text(outfile):
    """
    Add footnote with custom text marker to a PDF document.
    Creates a PDF document with text fragments that include footnotes with custom
    styling. The function demonstrates how to add footnotes with custom text markers
    and standard footnotes to different text fragments within the same document.
    Args:
        outfile (str): The output file path where the PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        add_footnote_custom_text("output_with_footnotes.pdf")
    Note:
        The document will contain:
        - Text with a custom footnote marker ("*")
        - Text without footnotes
        - Text with a standard footnote
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14

    note = ap.Note("This is the footnote content with custom text style.")
    note.text = "*"
    text_fragment.foot_note = note
    page.paragraphs.add(text_fragment)

    another_text = ap.text.TextFragment(" This is another text without footnote.")
    another_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    another_text.text_state.font_size = 14
    page.paragraphs.add(another_text)

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.foot_note = ap.Note("This is the footnote content.")
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

### Добавить сноски с пользовательским стилем линии в PDF

Настройте визуальный вид линий сносок в PDF‑документе с помощью библиотеки Python. Настройка линий сносок повышает визуальную чёткость и обеспечивает стилистическую согласованность в таких документах, как отчёты, академические статьи и аннотированные публикации.

1. Создать новый PDF‑документ и добавить страницу.
1. Определить пользовательский стиль линии для соединителей сносок (цвет, ширина и шаблон пунктирной линии).
1. Добавить несколько текстовых фрагментов с сносками.
1. Сохранить окончательный документ.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_with_custom_line_style(outfile):
    """
    Add footnotes with custom line style to a PDF document.
    Creates a PDF document with text fragments that have footnotes and applies
    a custom line style for the footnote separator line. The custom style includes
    red color, increased line width, and dashed pattern.
    Args:
        outfile (str): Path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        >>> add_footnote_with_custom_line_style("output.pdf")
        # Creates a PDF with footnoted text and custom separator line styling
    """

    document = ap.Document()
    page = document.pages.add()

    # Define custom line style
    graph_info = ap.GraphInfo()
    graph_info.line_width = 2
    graph_info.color = ap.Color.red
    graph_info.dash_array = [3]
    graph_info.dash_phase = 1
    page.note_line_style = graph_info

    # First text fragment with footnote
    text1 = ap.text.TextFragment("This is a sample text with a footnote.")
    text1.foot_note = ap.Note("foot note for text 1")
    page.paragraphs.add(text1)

    # Second text fragment with footnote
    text2 = ap.text.TextFragment("This is yet another sample text with a footnote.")
    text2.foot_note = ap.Note("foot note for text 2")
    page.paragraphs.add(text2)

    document.save(outfile)
```

### Добавить сноски с изображением и таблицей в PDF

Как обогатить сноски в PDF‑документе, внедрив изображения, стилизованный текст и таблицы с помощью Aspose.PDF for Python via .NET?

1. Создать новый PDF‑документ и добавить страницу.
1. Добавить текстовый фрагмент с прикреплённой сноской.
1. Встроить изображение, стилизованный текст и таблицу в сноску.
1. Сохранить документ.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_footnote_with_image_and_table(outfile):
    """
    Add a footnote containing an image and table to a PDF document.
    Creates a new PDF document with sample text that includes a footnote. The footnote
    contains three elements: an image (logo.jpg), descriptive text, and a simple table
    with two cells. The image is resized to 20x20 pixels and the footnote text uses
    a 20pt font size.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Note:
        - Requires the logo.jpg file to be present in the DATA_DIR directory
        - Uses the Aspose.PDF library (imported as 'ap')
        - The footnote is attached to the main text fragment on the page
    """

    document = ap.Document()
    page = document.pages.add()

    text = ap.text.TextFragment("This is a sample text with a footnote.")
    page.paragraphs.add(text)

    note = ap.Note()

    # Add image
    image_note = ap.Image()
    image_note.file = os.path.join(DATA_DIR, "logo.jpg")
    image_note.fix_height = 20
    image_note.fix_width = 20
    note.paragraphs.add(image_note)

    # Add text
    text_note = ap.text.TextFragment("This is the footnote content.")
    text_note.text_state.font_size = 20
    text_note.is_in_line_paragraph = True
    note.paragraphs.add(text_note)

    # Add table
    table = ap.Table()
    table.rows.add().cells.add("Cell 1,1")
    table.rows.add().cells.add("Cell 1,2")
    note.paragraphs.add(table)

    text.foot_note = note

    document.save(outfile)
```

### Добавление концевых сносок в PDF‑документы

Концевая сноска — это тип цитаты, который направляет читателей к определённому разделу в конце документа, где они могут найти полную ссылку на цитату, перефразированную идею или резюмированный материал. При использовании концевых сносок надстрочный номер размещается сразу после ссылки, указывая читателю на соответствующую заметку в конце работы.

Этот фрагмент кода демонстрирует, как добавить концевую сноску к текстовому фрагменту в PDF‑документе. В отличие от сносок, которые размещаются рядом с ссылочным текстом, концевые сноски обычно находятся в конце документа или раздела. Этот метод также моделирует более длинный документ, чтобы показать, как концевые сноски работают в расширенном содержимом.

1. Создать PDF‑документ и страницу.
1. Добавить текстовый фрагмент с концевой сноской.
1. Загрузить внешний текстовый контент.
1. Смоделировать длинный документ. Добавить загруженный текст несколько раз, чтобы имитировать более длинный документ.
1. Сохранить документ.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_endnote(outfile):
    """Add endnote to a PDF document.
    Creates a new PDF document with a text fragment containing an endnote,
    followed by additional lorem ipsum content to simulate a longer document.
    The endnote is attached to the first text fragment and will be displayed
    according to the PDF viewer's endnote handling.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        This function requires the aspose-pdf library and assumes the existence
        of a DATA_DIR variable pointing to a directory containing 'lorem.txt'.
        If the lorem.txt file is not found, fallback text will be used.
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    page.paragraphs.add(text_fragment)

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text_content = (
        open(lorem_path, encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum sample text not found."
    )

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

### Добавить концевые сноски с пользовательским текстом маркера в PDF

Добавьте концевую сноску к текстовому фрагменту в PDF‑документе, используя пользовательский символ маркера (например, "***"). Концевые сноски обычно размещаются в конце документа или раздела и полезны для предоставления дополнительного контекста, ссылок или комментариев.

1. Создать PDF‑документ и страницу.
1. Добавить стилизованный текстовый фрагмент с концевой сноской.
1. Настроить текст маркера концевой сноски.
1. Загрузить внешний контент из файла .txt.
1. Смоделировать длинный контент, чтобы проиллюстрировать расположение концевой сноски.
1. Сохранить PDF‑документ.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def add_endnote_custom_text(outfile):
    """
    Add endnote with custom text marker to a PDF document.
    Creates a PDF document with a text fragment that contains an endnote with
    a custom marker ("***"). The document is populated with sample text content
    from a lorem.txt file, repeated multiple times to simulate a longer document.
    Args:
        outfile (str): Path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file path.
    Note:
        - Requires lorem.txt file in DATA_DIR for sample content
        - Falls back to default text if lorem.txt is not found
        - Uses Arial font with 14pt size for all text elements
        - The endnote marker is set to "***" instead of default numbering
    """

    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    text_fragment.end_note.text = "***"
    page.paragraphs.add(text_fragment)

    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    text_content = (
        open(lorem_path, encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum sample text not found."
    )

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

## Макет и контроль страниц

### Принудительно начать таблицу на новой странице в PDF

Добавьте определённый контент, который будет начинаться на новой странице PDF‑документа, используя Aspose.PDF for Python via .NET.
Установив свойство 'is_in_new_page', вы можете точно контролировать макет и структуру страниц, гарантируя, что определённые разделы (например, таблицы, отчёты или резюме) всегда начинаются на новой странице — это идеально для форматирования документов, готовых к печати, или для упорядоченного создания вывода.

1. Создать и настроить таблицу.
1. Добавить данные в таблицу.
1. Принудительно начать таблицу на новой странице. Это гарантирует, что таблица начнётся вверху новой страницы, даже если на текущей уже есть содержимое.
1. Добавить таблицу на страницу. Используйте 'page.paragraphs.add()', чтобы включить таблицу в макет PDF.
1. Сохранить документ.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def force_new_page(output_file_name):
    """
    Create a PDF document demonstrating forced page breaks with tables.

    Creates a PDF document with a table that is forced to start on a new page
    using the is_in_new_page property. This is useful for controlling page layout
    and ensuring specific content starts on fresh pages.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Creates a 3-column table with 5 rows of sample data
        - Table uses uniform column widths of 150 units each
        - All cells have borders for clear visual separation
        - is_in_new_page=True forces the table to start on a new page
        - Useful for reports, documents with sections, or content organization

    Example:
        >>> force_new_page("new_page_table.pdf")
        # Creates a PDF with a table that starts on a new page
    """
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create a table
    table = ap.Table()
    table.column_widths = "150 150 150"
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL)

    # Add rows with sample data
    for i in range(5):
        row = table.rows.add()
        row.cells.add(f"Row {i + 1} - Col 1")
        row.cells.add(f"Row {i + 1} - Col 2")
        row.cells.add(f"Row {i + 1} - Col 3")

    # --- Key part: force table to start on a new PDF page ---
    table.is_in_new_page = True

    # Add table to page
    page.paragraphs.add(table)

    # Save the PDF
    document.save(output_file_name)
```

### Использование свойства Inline Paragraph в PDF

Наша библиотека позволяет использовать свойство 'is_in_line_paragraph' для контроля потока текста и изображений внутри PDF.
Обычно, когда вы добавляете новые элементы (например, текстовые фрагменты или изображения), каждый из них начинается с новой строки или нового абзаца.
Установив 'is_in_line_paragraph = True', вы можете разместить элементы на одной строке или в одном абзаце, создавая плавные встроенные макеты — идеально для комбинирования текста и изображений в строке, например, добавления логотипов, иконок или символов внутри предложений.

Первый текстовый фрагмент, изображение и второй текстовый фрагмент находятся на одной строке, образуя непрерывный встроенный абзац.
Третий фрагмент текста начинает новый абзац, демонстрируя поведение разрыва строки по умолчанию.

1. Создать новый PDF документ.
1. Добавить первый фрагмент текста.
1. Вставить встроенное изображение.
1. Добавить больше встроенного текста.
1. Добавить новый абзац.
1. Сохранить PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def using_inline_paragraph_property(output_file_name):
    """
    Demonstrate inline paragraph behavior in PDF document layout.

    Creates a PDF document showing how the is_in_line_paragraph property affects
    the flow of text and images. Elements with this property continue the flow
    of the previous paragraph instead of starting a new one.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - First text fragment starts a new paragraph
        - Image with is_in_line_paragraph=True continues the same line
        - Second text fragment also continues the same paragraph line
        - Third text fragment starts a new paragraph (default behavior)
        - Demonstrates inline flow control for mixed content (text + images)
        - Image is resized to 30x30 pixels and flows inline with text

    Example:
        >>> using_inline_paragraph_property("inline_paragraph.pdf")
        # Creates a PDF demonstrating inline paragraph flow
    """
    # Create a PDF document
    document = ap.Document()
    page = document.pages.add()

    # --- First text fragment (normal paragraph) ---
    fragment1 = ap.text.TextFragment("This is the first part of the paragraph. ")
    fragment1.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment1.text_state.font_size = 14
    page.paragraphs.add(fragment1)

    # --- Inline image (continues same paragraph flow) ---
    image = ap.Image()
    image.is_in_line_paragraph = True  # Makes image inline with previous paragraph
    image.file = os.path.join(DATA_DIR, "logo.jpg")
    image.fix_height = 30
    image.fix_width = 30
    page.paragraphs.add(image)

    # --- Second inline text fragment (keeps same paragraph flow) ---
    fragment2 = ap.text.TextFragment("This is the second part of the same paragraph.")
    fragment2.is_in_line_paragraph = True
    fragment2.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment2.text_state.font_size = 14
    page.paragraphs.add(fragment2)

    # --- Third fragment (starts new paragraph automatically) ---
    fragment3 = ap.text.TextFragment("This is a new paragraph.")
    fragment3.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment3.text_state.font_size = 14
    page.paragraphs.add(fragment3)

    # Save PDF
    document.save(output_file_name)
```

### Создать PDF с несколькими колонками

Создайте макет PDF в стиле газет с несколькими колонками, используя Aspose.PDF для Python через .NET.
Показывает, как объединить текст, HTML-форматирование и графику внутри FloatingBox, обеспечивая расширенный контроль макета, похожий на дизайн многоколоночных журналов или бюллетеней.

1. Инициализировать PDF документ.
1. Добавить горизонтальную разделительную линию вверху.
1. Добавить стилизованный HTML заголовок.
1. Создать FloatingBox для управления макетом.
1. Настроить макет с несколькими колонками.
1. Добавить информацию об авторе.
1. Нарисовать еще одну внутреннюю горизонтальную линию.
1. Добавить текст статьи.
1. Сохранить конечный PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def create_multi_column_pdf(output_file_name):
    """
    Create a PDF document with multi-column layout using FloatingBox.

    Creates a professional-looking PDF with a multi-column newspaper-style layout.
    Demonstrates advanced layout techniques including floating boxes, column
    configuration, and mixed content with graphics and text.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Document margins: 40 points left and right
        - Top horizontal line for visual separation
        - HTML-formatted heading with custom styling
        - FloatingBox with 2-column layout (105 units wide each)
        - Column spacing: 5 units between columns
        - Includes author attribution with italic styling
        - Internal horizontal line within the floating box
        - Long text content automatically flows between columns
        - Demonstrates professional document layout techniques

    Example:
        >>> create_multi_column_pdf("multi_column_layout.pdf")
        # Creates a PDF with newspaper-style multi-column layout
    """
    # Create PDF document
    document = ap.Document()

    # Set margins
    document.page_info.margin.left = 40
    document.page_info.margin.right = 40

    page = document.pages.add()

    #
    # Draw horizontal line at the top
    #
    graph1 = ap.drawing.Graph(500.0, 2.0)
    page.paragraphs.add(graph1)

    pos_arr = [1.0, 2.0, 500.0, 2.0]
    line1 = ap.drawing.Line(pos_arr)
    graph1.shapes.add(line1)

    #
    # Add HTML heading text
    #
    html = "<span style=\"font-family: 'Times New Roman'; font-size: 18px;\"><strong>How to Steer Clear of money scams</strong></span>"
    heading_text = ap.HtmlFragment(html)
    page.paragraphs.add(heading_text)

    #
    # Floating box: enables multi-column layout
    #
    box = ap.FloatingBox()

    box.column_info.column_count = 2  # Two columns
    box.column_info.column_spacing = "5"  # Space between columns
    box.column_info.column_widths = "105 105"  # Width of each column

    #
    # Add title text to the FloatingBox
    #
    text1 = ap.text.TextFragment("By A Googler (The Official Google Blog)")
    text1.text_state.font_size = 8
    text1.text_state.line_spacing = 2
    box.paragraphs.add(text1)

    text1.text_state.font_size = 10
    text1.text_state.font_style = ap.text.FontStyles.ITALIC

    #
    # Add another horizontal line inside the box
    #
    graph2 = ap.drawing.Graph(50.0, 10.0)

    pos_arr2 = [1.0, 10.0, 100.0, 10.0]
    line2 = ap.drawing.Line(pos_arr2)
    graph2.shapes.add(line2)

    box.paragraphs.add(graph2)

    #
    # Add long text content
    #
    lorem_path = os.path.join(DATA_DIR, "lorem.txt")
    lorem_text = (
        open(lorem_path, "r", encoding="utf-8").read()
        if os.path.exists(lorem_path)
        else "Lorem ipsum text not found."
    )
    text2 = ap.text.TextFragment(lorem_text * 5)
    box.paragraphs.add(text2)

    page.paragraphs.add(box)

    # Save PDF
    document.save(output_file_name)
```

### Пользовательские позиции табуляции для выравнивания текста в PDF

Создайте табличный макет текста в PDF, используя пользовательские позиции табуляции — без использования табличных структур.
Определяя позиции табуляции, выравнивания и стили лидеров, вы можете точно выравнивать текст по колонкам. Это полезно для счетов, отчетов или структурированных текстовых данных.

1. Создать новый PDF документ.
1. Определить пользовательские позиции табуляции.
1. Использовать заполнители #$TAB в тексте.
1. Добавить текст в PDF.
1. Сохранить PDF.

```python

import aspose.pdf as ap
from aspose.pdf import Color
from aspose.pdf.drawing import Graph, Line
import os

# Global configuration
DATA_DIR = "your path here"

def custom_tab_stops(output_file_name):
    """
    Create a PDF document demonstrating custom tab stops for table-like formatting.

    Creates a PDF document that uses custom tab stops to format text in a table-like
    structure without using actual table elements. This demonstrates advanced text
    formatting with precise positioning and leader styles.

    Args:
        output_file_name (str): The file path where the generated PDF document will be saved.

    Returns:
        None: The function saves the document to the specified output file.

    Note:
        - Tab stop 1: Position 100, right-aligned, solid leader line
        - Tab stop 2: Position 200, center-aligned, dashed leader line
        - Tab stop 3: Position 300, left-aligned, dotted leader line
        - Uses #$TAB placeholder for tab positions in text
        - Creates table-like structure with headers and data rows
        - Demonstrates mixing TextFragment and TextSegment approaches
        - Leader lines provide visual guides between columns
        - Alternative to HTML tables for precise text positioning

    Example:
        >>> custom_tab_stops("custom_tabs.pdf")
        # Creates a PDF with custom tab stop formatting
    """
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Define tab stops
    tab_stops = ap.text.TabStops()

    tab_stop1 = tab_stops.add(100)
    tab_stop1.alignment_type = ap.text.TabAlignmentType.RIGHT
    tab_stop1.leader_type = ap.text.TabLeaderType.SOLID

    tab_stop2 = tab_stops.add(200)
    tab_stop2.alignment_type = ap.text.TabAlignmentType.CENTER
    tab_stop2.leader_type = ap.text.TabLeaderType.DASH

    tab_stop3 = tab_stops.add(300)
    tab_stop3.alignment_type = ap.text.TabAlignmentType.LEFT
    tab_stop3.leader_type = ap.text.TabLeaderType.DOT

    # Create TextFragments with tab placeholders
    header = ap.text.TextFragment(
        "This is an example of forming table with TAB stops", tab_stops
    )
    text0 = ap.text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", tab_stops)
    text1 = ap.text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", tab_stops)

    text2 = ap.text.TextFragment("#$TABdata21 ", tab_stops)
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data22 "))
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data23"))

    # Add text fragments to page
    page.paragraphs.add(header)
    page.paragraphs.add(text0)
    page.paragraphs.add(text1)
    page.paragraphs.add(text2)

    # Save PDF document
    document.save(output_file_name)
```
