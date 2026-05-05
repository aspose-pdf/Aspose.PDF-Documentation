---
title: Добавить заголовки и нижние колонтитулы PDF в Python
linktitle: Добавление заголовка и нижнего колонтитула в PDF
type: docs
weight: 50
url: /ru/python-net/add-headers-and-footers-of-pdf-file/
description: Узнайте, как добавить колонтитулы в PDF‑файлы на Python, используя текст, изображения и структурированное содержимое.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить заголовок и нижний колонтитул в PDF с помощью Python
Abstract: Статья предоставляет исчерпывающее руководство по использованию **Aspose.PDF for Python via .NET** для добавления верхних и нижних колонтитулов в PDF‑файлы с возможностью включения текста или изображений. В начале подробно рассматривается использование класса `TextStamp` для вставки текста в верхний колонтитул PDF‑документа. Ключевые свойства, такие как размер шрифта, стиль и цвет, могут быть настроены, и метод добавления текста в верхний колонтитул демонстрируется с помощью фрагмента кода на Python. В статье также объясняется, как добавить текст в нижний колонтитул, следуя тем же процедурным шагам. Для добавления изображений используется класс `ImageStamp`, процесс описан как для верхних, так и для нижних колонтитулов, опять же с примерами кода на Python. Кроме того, в статье рассматривается добавление нескольких верхних колонтитулов в один PDF‑файл. Это включает создание нескольких объектов `TextStamp`, каждый из которых имеет отдельное форматирование, и их применение к различным страницам. Объяснение дополнено подробным фрагментом кода, демонстрирующим эту функциональность.
---

Эта страница предоставляет краткий обзор добавления верхних и нижних колонтитулов в PDF‑документы с использованием Aspose.PDF for Python via .NET, охватывая подходы, основанные на тексте, HTML, LaTeX, изображениях и таблицах, а также динамичную нумерацию страниц и несколько колонтитулов на страницу; она объясняет, как создавать и оформлять [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) объекты (используя [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/), [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/), [`Image`](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/), [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/), и т.д.), скорректировать [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) и [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) для точного размещения и прикрепления результатов к страницам с практическими примерами кода на Python.

**Aspose.PDF for Python via .NET** позволяет добавлять заголовок и нижний колонтитул в ваш существующий [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Вы можете добавить изображения или текст в PDF документ. Также попробуйте добавить разные заголовки в один PDF‑файл с помощью Python.

Используйте эту страницу, когда нужно добавить повторяющийся брендинг, метки страниц, заголовки документов или содержание нижнего колонтитула на всех страницах PDF в Python.

## Добавление заголовков и нижних колонтитулов в виде текстовых фрагментов

Добавьте простые текстовые заголовки и колонтитулы на все страницы PDF. Он создает [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) объекты, вставки [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) элементы в них, наборы [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) для правильного позиционирования и прикрепляет их к каждой странице документа. В результате получаем PDF, где каждая страница отображает одинаковый текст заголовка и нижнего колонтитула.

Следующий фрагмент кода демонстрирует, как добавить заголовки и колонтитулы в виде текстовых фрагментов в PDF с использованием Python:

1. Создайте текстовые фрагменты для заголовка и нижнего колонтитула.
1. Создайте объекты HeaderFooter и добавьте к ним текстовые фрагменты.
1. Определите настройки полей, чтобы управлять размещением заголовка и нижнего колонтитула.
1. Загрузите PDF‑документ из входного файла.
1. Переберите все страницы в документе.
1. Назначьте верхний и нижний колонтитулы каждой странице.
1. Сохраните изменённый PDF в выходной файл.

```python
import sys
import aspose.pdf as ap
from os import path

def add_header_and_footer_as_text(input_file, output_file):
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

Этот метод полезен для добавления одинаковых заголовков, индикаторов страниц или юридических отказов в верхней и нижней части каждой страницы. Вы также можете расширить его, включив изображения или динамический контент, например номера страниц.

## Добавление заголовков и нижних колонтитулов для нумерации страниц

Добавьте автоматическую нумерацию страниц в заголовки и нижние колонтитулы PDF‑документа с помощью Aspose.PDF for Python. Используя встроенные переменные $p (текущий номер страницы) и $P (общее количество страниц), скрипт динамически вставляет нумерацию на каждую страницу. В заголовках отображается формат 'Page X from Y', а в нижних колонтитулах — 'Page X / Y'. The [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) обеспечивает правильное размещение на каждой странице.

1. Создайте TextFragment для заголовка, используя "Page $p from $P", чтобы показать текущую страницу и общее количество страниц.
1. Создайте объект HeaderFooter и добавьте в него текст заголовка.
1. Создайте TextFragment для нижнего колонтитула, используя "Page $p / $P" для альтернативного стиля нумерации.
1. Создайте объект Footer и добавьте текст нижнего колонтитула.
1. Определите настройки полей (левый = 50, верхний = 20) и примените их к верхнему и нижнему колонтитулу.
1. Откройте PDF-документ из входного файла.
1. Пройдите по всем страницам и назначьте заголовок и нижний колонтитул каждой странице.
1. Сохраните обновлённый PDF в путь вывода.

```python
import sys
import aspose.pdf as ap
from os import path

def using_header_and_footer_for_page_numbering(input_file, output_file):
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

Примените HTML-форматированные заголовки и колонтитулы к каждой странице PDF‑документа с использованием Aspose.PDF for Python. Используя [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), скрипт позволяет стилизацию форматированного текста — например, полужирный и курсив — отображать в заголовке и нижнем колонтитуле. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) применяется для правильного размещения, и те же отформатированные элементы прикрепляются к каждой странице документа.

Следующий фрагмент кода демонстрирует, как добавить заголовки и колонтитулы в виде HTML‑фрагментов в PDF с помощью Python:

1. Создайте фрагмент заголовка HTML с использованием HtmlFragment — включая стилизованный текст, например ‘<strong>' для жирного.
1. Создайте объект HeaderFooter и добавьте к нему HTML‑заголовок.
1. Создайте фрагмент HTML‑подвала, используя '<i>' для курсивного оформления.
1. Создайте объект Footer и добавьте в него HTML нижнего колонтитула.
1. Настройте поля (left = 50, top = 20) и назначьте их как для верхнего, так и для нижнего колонтитула.
1. Загрузите PDF‑документ, используя 'ap.Document()'.
1. Переберите все страницы и присвойте каждой заголовок и нижний колонтитул.
1. Сохраните изменённый PDF в указанный путь вывода.

```python
import sys
import aspose.pdf as ap
from os import path

def add_header_and_footer_as_html(input_file, output_file):
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

Использование HtmlFragment позволяет применять богато оформленное форматирование с встроенными стилями или разметкой HTML, предоставляя большую гибкость дизайна по сравнению с обычным текстом.

## Добавление заголовков и нижних колонтитулов в виде изображений

Добавьте заголовки и нижние колонтитулы на основе изображений на каждую страницу PDF‑документа с помощью Aspose.PDF for Python. Один и тот же файл изображения используется как в заголовке, так и в нижнем колонтитуле на каждой странице. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) размещает изображения, и изображение автоматически подгоняется, чтобы поместиться в область заголовка/нижнего колонтитула.

Следующий фрагмент кода демонстрирует, как добавить заголовки и колонтитулы в виде изображений в PDF с помощью Python:

1. Загрузите изображение в объект 'ap.Image' и подготовьте его для использования в качестве заголовка.
1. Создайте объект HeaderFooter и прикрепите к нему изображение заголовка.
1. Загрузите то же изображение ещё раз для использования в качестве нижнего колонтитула.
1. Создайте объект Footer и добавьте к нему изображение нижнего колонтитула.
1. Загрузите входной PDF‑документ, используя 'ap.Document()'.
1. Перебрать все страницы документа.
1. Применить отступы (левый = 50) для позиционирования как заголовка, так и нижнего колонтитула.
1. Назначьте заголовок и нижний колонтитул каждой странице PDF.
1. Сохраните обновлённый PDF в указанный файл вывода.

Эта техника идеальна для брендирования документов логотипами или водяными знаками в области верхнего/нижнего колонтитула.

```python
import sys
import aspose.pdf as ap
from os import path

def add_header_and_footer_as_image(input_file, image_file, output_file):
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

Добавьте структурированные, основанные на таблицах, заголовки и нижние колонтитулы на все страницы PDF‑документа с использованием Aspose.PDF для Python. [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) Объекты обеспечивают более точный контроль макета, выравнивание и последовательное форматирование сложных заголовков и нижних колонтитулов. Текст заголовка центрирован, а текст нижнего колонтитула выровнен по левому краю, оба используют шрифт Arial 12 пунктов. Ширина столбцов рассчитывается динамически на основе размеров страницы, чтобы гарантировать правильное размещение.

Этот фрагмент кода добавляет заголовки и колонтитулы (с использованием таблиц) на каждую страницу PDF‑документа с помощью Aspose.PDF for Python via .NET.

1. Определите стили текста, используя [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) для заголовка и колонтитула (шрифт, размер, выравнивание).
1. Создать [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) объекты для верхнего и нижнего колонтитула.
1. Создать заголовок [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) с единственной строкой и ячейкой, содержащей текст заголовка.
1. Создать нижний колонтитул [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) с одной строкой и ячейкой, содержащей текст нижнего колонтитула.
1. Добавьте таблицы к соответствующим [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) объекты.
1. Установить нижний колонтитул [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) для правильного горизонтального позиционирования.
1. Откройте [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) используя соответствующие методы.
1. Пройдите по всем страницам и присвойте каждой странице заголовок и нижний колонтитул, основанные на таблице.
1. Сохраните изменённый [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) в выходной файл.

```python
import sys
import aspose.pdf as ap
from os import path

def add_header_and_footer_as_table(input_file, output_file):
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

## Добавление заголовков и нижних колонтитулов в LaTeX

Добавьте заголовки и колонтитулы, содержащие контент в формате LaTeX, на все страницы PDF‑документа с использованием Aspose.PDF for Python. LaTeX позволяет отображать математические символы, даты, знаки авторского права и другое сложное форматирование. В заголовке отображается динамическая дата, а в колонтитуле — символ авторского права вместе с текущим номером страницы и общим количеством страниц.

Следующий фрагмент кода показывает, как использовать [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) в заголовках и нижних колонтитулах PDF с использованием Aspose.PDF for Python via .NET.

1. Откройте [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) используя соответствующие методы.
1. Определите общее количество страниц для использования в динамических колонтитулах.
1. Перебрать все страницы документа.
1. Создайте [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) объект для заголовка.
1. Создайте [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) для текста заголовка, содержащего команды LaTeX (например, `\\today\\`).
1. Создайте [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) объект для нижнего колонтитула.
1. Создайте [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) для текста нижнего колонтитула, включая символы LaTeX и нумерацию страниц.
1. Добавить [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) к соответствующему объекту колонтитула.
1. Привяжите заголовок и нижний колонтитул к текущей странице.
1. Сохраните изменённый [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) в выходной файл.

```python
import sys
import aspose.pdf as ap
from os import path

def add_header_and_footer_as_latex(input_file, output_file):
    # Open PDF document
    with ap.Document(input_file) as document:
        page_count = len(document.pages)
        for i in range(1, page_count + 1):
            # Create header
            header = ap.HeaderFooter()
            h_latex_text = "This is a LaTeX Header. \\today\\"
            h_l_text = ap.TeXFragment(h_latex_text, True)
            # Create footer
            footer = ap.HeaderFooter()
            f_latex_text = (
                f"\\copyright\\ 2025 My Company -- Page \\thepage\\ is {page_count}"
            )
            f_l_text = ap.TeXFragment(f_latex_text, True)

            header.paragraphs.add(h_l_text)
            footer.paragraphs.add(f_l_text)
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Связанные темы страницы

- [Работа с PDF-страницами в Python](/pdf/ru/python-net/working-with-pages/)
- [Добавить номера страниц в PDF с помощью Python](/pdf/ru/python-net/add-page-number/)
- [Нанести штамп на страницы PDF в Python](/pdf/ru/python-net/stamping/)
- [Форматировать PDF‑документы в Python](/pdf/ru/python-net/formatting-pdf-document/)