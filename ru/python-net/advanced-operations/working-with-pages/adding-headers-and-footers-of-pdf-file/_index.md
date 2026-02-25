---
title: Добавление заголовка и нижнего колонтитула в PDF с помощью Python
linktitle: Добавление заголовка и нижнего колонтитула в PDF
type: docs
weight: 50
url: /ru/python-net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for Python via .NET позволяет добавлять заголовки и нижние колонтитулы в ваш PDF‑файл с помощью класса TextStamp.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить заголовок и нижний колонтитул в PDF с помощью Python
Abstract: В статье представлено полное руководство по использованию **Aspose.PDF for Python via .NET** для добавления заголовков и нижних колонтитулов в PDF‑файлы с возможностью включать текст или изображения. Она начинается с описания использования класса `TextStamp` для вставки текста в заголовок PDF‑документа. Ключевые свойства, такие как размер шрифта, стиль и цвет, можно настраивать, а метод добавления текста в заголовок демонстрируется с помощью фрагмента кода на Python. Аналогично статья объясняет, как добавить текст в нижний колонтитул, следуя тем же процедурным шагам. Для добавления изображений используется класс `ImageStamp`, и процесс описан как для заголовков, так и для нижних колонтитулов, также поддерживается примерами кода на Python. Кроме того, в статье рассматривается добавление нескольких заголовков в одном PDF‑файле. Это включает создание нескольких объектов `TextStamp`, каждый с отдельным форматированием, и их применение к разным страницам. Объяснение сопровождается подробным фрагментом кода, демонстрирующим эту функциональность.
---

Эта страница предоставляет краткий обзор добавления заголовков и нижних колонтитулов в PDF‑документы с помощью Aspose.PDF for Python via .NET, охватывая подходы на основе текста, HTML, LaTeX, изображений и таблиц, а также динамичную нумерацию страниц и несколько заголовков на страницу; она объясняет, как создать и оформить объекты [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) (используя [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/), [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/), [`Image`](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/), [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) и т.д.), настроить [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) и [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) для точного размещения и прикрепить результаты к страницам с практическими примерами кода на Python.

**Aspose.PDF for Python via .NET** позволяет добавлять заголовок и нижний колонтитул в ваш существующий [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Вы можете добавлять изображения или текст в PDF‑документ. Также попробуйте добавить разные заголовки в один PDF‑файл с помощью Python.

## Добавление заголовков и нижних колонтитулов в виде текстовых фрагментов

Добавьте простые текстовые заголовки и нижние колонтитулы на все страницы PDF. Создаются объекты [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/), в которые вставляются элементы [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/), устанавливаются параметры [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) для правильного позиционирования и они прикрепляются к каждой странице документа. В результате получаем PDF, где каждая страница отображает одинаковый текст заголовка и нижнего колонтитула.

Следующий фрагмент кода демонстрирует, как добавить заголовки и нижние колонтитулы в виде текстовых фрагментов в PDF с использованием Python:

1. Создайте текстовые фрагменты для заголовка и нижнего колонтитула.
1. Создайте объекты HeaderFooter и добавьте в них текстовые фрагменты.
1. Определите настройки отступов для контроля размещения заголовка и нижнего колонтитула.
1. Загрузите PDF‑документ из входного файла.
1. Пройдитесь по всем страницам документа.
1. Назначьте заголовок и нижний колонтитул каждой странице.
1. Сохраните изменённый PDF в выходной файл.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_text(input_file, output_file):
    """
    Add simple text headers and footers to all pages of a PDF document.

    Creates basic text-based headers and footers that appear on every page
    of the PDF document. Headers show "header" text and footers show "footer" text.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Adds identical headers and footers to all pages
        - Sets margins of 50 units left and 20 units top
        - Uses simple TextFragment elements for content
        - Headers and footers are created separately for each page

    Example:
        >>> add_header_and_footer_as_text("input.pdf", "output.pdf")
        # Adds text headers and footers to all pages
    """
    # Create header text
    header_text = ap.text.TextFragment("Demo header")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Demo footer")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

Этот метод полезен для добавления одинаковых заголовков, индикаторов страниц или правовых уведомлений в верхнюю и нижнюю часть каждой страницы. Вы также можете расширить его, включив изображения или динамический контент, например нумерацию страниц.

## Добавление заголовков и нижних колонтитулов для нумерации страниц

Добавьте автоматическую нумерацию страниц в заголовки и нижние колонтитулы PDF‑документа с помощью Aspose.PDF for Python. С помощью встроенных переменных $p (номер текущей страницы) и $P (общее количество страниц) скрипт динамически вставляет нумерацию на каждую страницу. В заголовках отображается формат «Page X from Y», а в нижних колонтитулах — «Page X / Y». [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) обеспечивает правильное размещение на каждой странице.

1. Создайте TextFragment для заголовка, используя "Page $p from $P" для отображения текущей и общей количества страниц.
1. Создайте объект HeaderFooter и добавьте в него текст заголовка.
1. Создайте TextFragment для нижнего колонтитула, используя "Page $p / $P" как альтернативный стиль нумерации.
1. Создайте объект Footer и добавьте в него текст нижнего колонтитула.
1. Определите настройки отступов (left = 50, top = 20) и примените их к заголовку и нижнему колонтитулу.
1. Откройте PDF‑документ из входного файла.
1. Пройдите по всем страницам и назначьте заголовок и нижний колонтитул каждой странице.
1. Сохраните обновлённый PDF по указанному пути.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def using_header_and_footer_for_page_numbering(input_file, output_file):
    """
    Add page numbering headers and footers to all pages of a PDF document.

    Creates headers and footers with dynamic page numbering using special variables.
    The $p variable represents the current page number and $P represents the total
    number of pages in the document.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses $p for current page number and $P for total pages
        - Header shows "Page X from Y" format
        - Footer shows "Page X / Y" format
        - Variables are automatically replaced by Aspose.PDF
        - Sets margins of 50 units left and 20 units top
        - Page numbering updates dynamically for each page

    Example:
        >>> using_header_and_footer_for_page_numbering("input.pdf", "output.pdf")
        # Adds page numbering headers and footers to all pages
    """
    # Create header text
    header_text = ap.text.TextFragment("Page $p from $P")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Page $p / $P")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Create margins
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20

    # Set header margin
    header.margin = margin
    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Добавление заголовков и нижних колонтитулов в виде HTML‑фрагментов

Примените заголовки и нижние колонтитулы, отформатированные в HTML, к каждой странице PDF‑документа с помощью Aspose.PDF for Python. Используя [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), скрипт позволяет отображать богатое текстовое форматирование — например, жирный и курсивный — в заголовке и нижнем колонтитуле. Применяется [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) для правильного позиционирования, и те же отформатированные элементы прикрепляются к каждой странице документа.

Следующий фрагмент кода демонстрирует, как добавить заголовки и нижние колонтитулы в виде HTML‑фрагментов в PDF с использованием Python:

1. Создайте HTML‑заголовок с помощью HtmlFragment, включающий стилизованный текст, например '<strong>' для жирного.
1. Создайте объект HeaderFooter и добавьте в него HTML‑заголовок.
1. Создайте HTML‑нижний колонтитул, используя '<i>' для курсивного оформления.
1. Создайте объект Footer и добавьте в него HTML‑нижелний колонтитул.
1. Настройте отступы (left = 50, top = 20) и назначьте их как заголовку, так и нижнему колонтитулу.
1. Загрузите PDF‑документ, используя 'ap.Document()'.
1. Пройдите по всем страницам и назначьте заголовок и нижний колонтитул каждому.
1. Сохраните изменённый PDF по указанному пути вывода.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_html(input_file, output_file):
    """
    Add HTML-formatted headers and footers to all pages of a PDF document.

    Creates rich HTML-based headers and footers with formatting like bold
    and italic text. Demonstrates how to use HtmlFragment for styled content.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses HtmlFragment for rich text formatting
        - Header includes HTML with <strong> tag for bold text
        - Footer includes HTML with <i> tag for italic text
        - Sets margins of 50 units left and 20 units top
        - HTML tags are rendered properly in the PDF

    Example:
        >>> add_header_and_footer_as_html("input.pdf", "output.pdf")
        # Adds HTML-formatted headers and footers to all pages
    """
    # Create header HTML
    header_html = ap.HtmlFragment("This is an HTML <strong>Header</strong>")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_html)

    # Create footer HTML
    footer_html = ap.HtmlFragment("Powered by <i>Aspose.PDF</i>")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_html)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

Использование HtmlFragment позволяет применять богатое форматирование с помощью встроенных стилей или HTML‑разметки, предоставляя большую гибкость дизайна по сравнению с обычным текстом.

## Добавление заголовков и нижних колонтитулов в виде изображений

Добавьте заголовки и нижние колонтитулы на основе изображений на каждую страницу PDF‑документа с помощью Aspose.PDF for Python. Один и тот же файл изображения используется как для заголовка, так и для нижнего колонтитула на каждой странице. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) позиционирует изображения, а изображение автоматически подстраивается под область заголовка/нижнего колонтитула.

Следующий фрагмент кода демонстрирует, как добавить заголовки и нижние колонтитулы в виде изображений в PDF с использованием Python:

1. Загрузите изображение в объект 'ap.Image' и подготовьте его для использования в качестве заголовка.
1. Создайте объект HeaderFooter и прикрепите к нему изображение заголовка.
1. Снова загрузите то же изображение для использования в качестве нижнего колонтитула.
1. Создайте объект Footer и добавьте к нему изображение нижнего колонтитула.
1. Загрузите входной PDF‑документ, используя 'ap.Document()'.
1. Пройдитесь по всем страницам документа.
1. Примените отступы (left = 50) для позиционирования как заголовка, так и нижнего колонтитула.
1. Назначьте заголовок и нижний колонтитул каждой странице PDF.
1. Сохраните обновлённый PDF в указанный файл вывода.

Эта техника идеально подходит для брендинга документов с логотипами или водяными знаками в области заголовка/нижнего колонтитула.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_image(input_file, image_file, output_file):
    """
    Add image-based headers and footers to all pages of a PDF document.

    Creates headers and footers using image files. The same image is used
    for both header and footer positioning on each page.

    Args:
        input_file (str): Path to the input PDF file.
        image_file (str): Path to the image file to use for headers and footers.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses the same image file for both header and footer
        - Creates separate Image objects for header and footer
        - Sets margin of 50 units left for positioning
        - Image files should be in supported formats (PNG, JPG, etc.)
        - Images are automatically sized to fit header/footer areas

    Example:
        >>> add_header_and_footer_as_image("input.pdf", "logo.png", "output.pdf")
        # Adds image headers and footers using logo.png
    """

    # Create header image
    header_image = ap.Image()
    header_image.file = image_file
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_image)

    # Create footer image
    footer_image = ap.Image()
    footer_image.file = image_file

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_image)

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Set header margin
            margin = ap.MarginInfo()
            margin.left = 50
            header.margin = margin

            # Set footer margin
            footer.margin = margin

            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Добавление заголовков и нижних колонтитулов в виде таблицы

Добавьте структурированные заголовки и нижние колонтитулы на основе таблиц ко всем страницам PDF‑документа с использованием Aspose.PDF для Python. Объекты [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) обеспечивают лучшую управляемость макетом, выравниванием и согласованным форматированием сложных заголовков и нижних колонтитулов. Текст заголовка центрируется, а текст нижнего колонтитула выравнивается по левому краю, оба используют шрифт Arial 12 pt. Ширины столбцов рассчитываются динамически исходя из размеров страницы, чтобы обеспечить правильное размещение.

Этот фрагмент кода добавляет заголовки и нижние колонтитулы (с использованием таблиц) на каждую страницу PDF‑документа с помощью Aspose.PDF для Python через .NET.

1. Определите стили текста с помощью [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) для заголовка и нижнего колонтитула (шрифт, размер, выравнивание).
1. Создайте объекты [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) для заголовка и нижнего колонтитула.
1. Сформируйте заголовок [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) с одной строкой и ячейкой, содержащей текст заголовка.
1. Сформируйте нижний колонтитул [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) с одной строкой и ячейкой, содержащей текст нижнего колонтитула.
1. Добавьте таблицы к соответствующим объектам [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/).
1. Установите для нижнего колонтитула [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) правильное горизонтальное позиционирование.
1. Откройте [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с помощью соответствующих методов.
1. Пройдитесь по всем страницам и назначьте заголовок и нижний колонтитул на основе таблиц каждой странице.
1. Сохраните изменённый [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) в файл вывода.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_table(input_file, output_file):
    """
    Add table-based headers and footers to all pages of a PDF document.

    Creates headers and footers using table structures for better layout
    control and alignment. Demonstrates advanced formatting with text states.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses Table objects for structured layout
        - Header table has centered Arial 12pt text
        - Footer table has left-aligned Arial 12pt text
        - Column width calculated based on page width minus margins
        - Provides more precise control over text positioning

    Example:
        >>> add_header_and_footer_as_table("input.pdf", "output.pdf")
        # Adds table-structured headers and footers to all pages
    """
    text_state_header = ap.text.TextState()
    text_state_header.font = ap.text.FontRepository.find_font("Arial")
    text_state_header.font_size = 12
    text_state_header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    text_state_footer = ap.text.TextState()
    text_state_footer.font = ap.text.FontRepository.find_font("Arial")
    text_state_footer.font_size = 12
    text_state_footer.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # Create header
    header = ap.HeaderFooter()
    # Create footer
    footer = ap.HeaderFooter()
    # Create header Table
    table_header = ap.Table()
    table_header.column_widths = str(594 - header.margin.left - header.margin.right)
    header_row = table_header.rows.add()
    header_row.cells.add("This is a Table Header", text_state_header)
    # Create footer Table
    table = ap.Table()
    table.column_widths = str(594 - footer.margin.left - footer.margin.right)
    table.rows.add().cells.add("Powered by Aspose.PDF", text_state_footer)
    header.paragraphs.add(table_header)
    footer.paragraphs.add(table)
    # Set footer margin
    footer.margin.left = 150

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Добавление заголовков и нижних колонтитулов в виде LaTeX

Добавьте заголовки и нижние колонтитулы, содержащие контент, отформатированный с помощью LaTeX, ко всем страницам PDF‑документа с использованием Aspose.PDF для Python. LaTeX позволяет отображать математические символы, даты, знаки авторского права и другое продвинутое форматирование. В заголовке отображается динамическая дата, а в нижнем колонтитуле — символ © вместе с номером текущей страницы и общим количеством страниц.

Следующий фрагмент кода показывает, как использовать [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) в заголовках и нижних колонтитулах PDF с помощью Aspose.PDF для Python через .NET.

1. Откройте [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с помощью соответствующих методов.
1. Определите общее количество страниц для использования в динамических нижних колонтитулах.
1. Пройдитесь по всем страницам документа.
1. Создайте объект [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) для заголовка.
1. Создайте [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) для текста заголовка, содержащего команды LaTeX (например, `\\today\\`).
1. Создайте объект [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) для нижнего колонтитула.
1. Создайте [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) для текста нижнего колонтитула, включающего символы LaTeX и нумерацию страниц.
1. Добавьте [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) в соответствующий объект заголовка/нижнего колонтитула.
1. Привяжите заголовок и нижний колонтитул к текущей странице.
1. Сохраните изменённый [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) в файл вывода.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_latex(input_file, output_file):
    """
    Add LaTeX-formatted headers and footers to all pages of a PDF document.

    Creates headers and footers using LaTeX markup for mathematical expressions,
    symbols, and advanced formatting. Demonstrates TeXFragment usage.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses TeXFragment for LaTeX rendering
        - Header includes LaTeX date command (\\today\\)
        - Footer includes copyright symbol and page numbering
        - LaTeX commands are processed and rendered properly
        - Page count is dynamically calculated and inserted

    Example:
        >>> add_header_and_footer_as_latex("input.pdf", "output.pdf")
        # Adds LaTeX-formatted headers and footers with symbols and page numbers
    """
    # Open PDF document
    with ap.Document(input_file) as document:
        page_count = len(document.pages)
        for i in range(1, page_count + 1):
            # Create header
            header = ap.HeaderFooter()
            h_latex_text = "This is a LaTex Header. \\today\\"
            h_l_text = ap.TeXFragment(h_latex_text, True)
            # Create footer
            footer = ap.HeaderFooter()
            f_latex_text = f"\\copyright\\ 2025 My Company -- Page \\thepage\\ is {page_count}"
            f_l_text = ap.TeXFragment(f_latex_text, True)

            header.paragraphs.add(h_l_text)
            footer.paragraphs.add(f_l_text)
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```
