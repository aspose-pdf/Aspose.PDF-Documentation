---
title: Добавить колонтитулы в PDF в Python
linktitle: Добавление колонтитулов в PDF
type: docs
weight: 50
url: /python-net/add-headers-and-footers-of-pdf-file/
description: Узнайте, как добавить верхние и нижние колонтитулы в PDF‑файлы с помощью Python, используя текст, изображения и структурированное содержимое.
lastmod: "2026-05-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавьте верхние и нижние колонтитулы в PDF‑файлы с помощью Python.
Abstract: В этой статье показано, как добавить заголовки и нижние колонтитулы в PDF‑документы с помощью Aspose.PDF for Python via .NET. Охватываются текст, нумерация страниц, HTML, изображения, таблицы и контент заголовков и нижних колонтитулов на основе LaTeX.
---

Используйте эту страницу, чтобы добавить единый контент заголовка и нижнего колонтитула на все страницы PDF с помощью **Aspose.PDF for Python via .NET**.

Вы можете создавать колонтитулы с помощью [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/), [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/), [`Image`](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/), и [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) объекты, затем примените их через [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) на каждой странице.

## Добавление верхних и нижних колонтитулов в виде текстовых фрагментов

Добавьте простые текстовые заголовки и нижние колонтитулы на все страницы PDF. Он создает [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) объекты, вставки [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) элементы в них, наборы [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) для правильного позиционирования и прикрепляет их к каждой странице документа. Результат — PDF, в котором каждая страница отображает одинаковый текст верхнего и нижнего колонтитула.

Следующий фрагмент кода демонстрирует, как добавить заголовки и нижние колонтитулы в виде текстовых фрагментов в PDF с использованием Python:

1. Создайте текстовые фрагменты для заголовка и нижнего колонтитула.
1. Создайте объекты HeaderFooter и добавьте к ним текстовые фрагменты.
1. Определите настройки полей, чтобы контролировать размещение заголовка и нижнего колонтитула.
1. Загрузите PDF-документ из входного файла.
1. Переберите все страницы в документе.
1. Назначьте заголовок и нижний колонтитул каждой странице.
1. Сохраните изменённый PDF в выходной файл.

```python
import aspose.pdf as ap

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

Этот метод полезен для добавления одинаковых заголовков, индикаторов страниц или юридических отказов от ответственности в верхней и нижней части каждой страницы. Вы также можете расширить его, включив изображения или динамический контент, такой как номера страниц.

## Добавление заголовков и колонтитулов для нумерации страниц

Добавьте автоматическую нумерацию страниц в заголовки и колонтитулы PDF-документа с помощью Aspose.PDF for Python. Используя встроенные переменные $p (текущий номер страницы) и $P (общее количество страниц), скрипт динамически вставляет нумерацию страниц на каждую страницу. В заголовках отображается формат 'Page X from Y', а в нижних колонтитулах — 'Page X / Y'. The [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) обеспечивает правильное размещение на каждой странице.

1. Создайте TextFragment для заголовка, используя "Page $p from $P" для отображения текущей и общей страниц.
1. Создайте объект HeaderFooter и добавьте в него текст заголовка.
1. Создайте TextFragment для нижнего колонтитула, используя "Page $p / $P" в качестве альтернативного стиля нумерации.
1. Создайте объект Footer и добавьте текст нижнего колонтитула.
1. Определите настройки полей (left = 50, top = 20) и примените их к заголовку и нижнему колонтитулу.
1. Откройте PDF документ из входного файла.
1. Пройдите по всем страницам и назначьте заголовок и нижний колонтитул каждой странице.
1. Сохраните обновлённый PDF в путь вывода.

```python
import aspose.pdf as ap

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

Применить HTML-оформленные заголовки и нижние колонтитулы к каждой странице PDF-документа с использованием Aspose.PDF for Python. С помощью [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), скрипт позволяет стилизацию форматированного текста—например, полужирный и курсив—отображаться в заголовке и нижнем колонтитуле. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) применяется для правильного размещения, и те же отформатированные элементы прикрепляются к каждой странице документа.

Следующий фрагмент кода демонстрирует, как добавить заголовки и нижние колонтитулы в виде HTML‑фрагментов в PDF с использованием Python:

1. Создайте HTML‑заголовок с использованием HtmlFragment—включая стилизованный текст, такой как '<strong>' для жирного.
1. Создайте объект HeaderFooter и добавьте к нему HTML‑заголовок.
1. Создайте HTML‑футерный фрагмент, используя '<i>' для курсивного оформления.
1. Создайте объект Footer и добавьте в него HTML нижнего колонтитула.
1. Настройте поля (слева = 50, сверху = 20) и примените их к заголовку и нижнему колонтитулу.
1. Загрузите PDF‑документ, используя 'ap.Document()'.
1. Переберите все страницы и назначьте заголовок и нижний колонтитул каждой из них.
1. Сохраните изменённый PDF в указанный путь вывода.

```python
import aspose.pdf as ap

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

Использование HtmlFragment позволяет применять богатое форматирование с помощью встроенных стилей или HTML‑разметки, обеспечивая большую гибкость дизайна по сравнению с обычным текстом.

## Добавление заголовков и нижних колонтитулов в виде изображений

Добавьте в каждую страницу PDF‑документа заголовки и нижние колонтитулы на основе изображения, используя Aspose.PDF for Python. Один и тот же файл изображения используется как для заголовка, так и для нижнего колонтитула на каждой странице. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) размещает изображения, и изображение автоматически подгоняется, чтобы вписаться в область верхнего/нижнего колонтитула.

Следующий фрагмент кода демонстрирует, как добавить заголовки и колонтитулы в виде изображений в PDF с использованием Python:

1. Загрузите изображение в объект 'ap.Image' и подготовьте его к использованию в качестве заголовка.
1. Создайте объект HeaderFooter и прикрепите к нему изображение заголовка.
1. Загрузите то же изображение снова для использования в качестве нижнего колонтитула.
1. Создайте объект Footer и добавьте к нему изображение нижнего колонтитула.
1. Загрузите входной PDF‑документ, используя 'ap.Document()'.
1. Итерируйте все страницы документа.
1. Примените отступы (слева = 50) для позиционирования как верхнего, так и нижнего колонтитулов.
1. Назначьте заголовок и нижний колонтитул каждой странице PDF.
1. Сохраните обновлённый PDF в указанный выходной файл.

Эта техника идеально подходит для брендирования документов логотипами или водяными знаками в области верхнего/нижнего колонтитула.

```python
import aspose.pdf as ap

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

Добавьте структурированные, основанные на таблице, заголовки и колонтитулы на все страницы PDF‑документа с использованием Aspose.PDF for Python. [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) Объекты обеспечивают лучший контроль макета, выравнивание и согласованное форматирование сложных верхних и нижних колонтитулов. Текст заголовка центрирован, а текст нижнего колонтитула выровнен по левому краю, оба используют шрифт Arial 12pt. Ширины столбцов вычисляются динамически на основе размеров страницы, чтобы обеспечить правильное размещение.

Этот фрагмент кода добавляет заголовки и колонтитулы (используя таблицы) к каждой странице PDF‑документа с Aspose.PDF for Python via .NET.

1. Определите стили текста с помощью [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) для верхнего и нижнего колонтитулов (шрифт, размер, выравнивание).
1. Создайте [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) объекты для заголовка и нижнего колонтитула.
1. Создайте заголовок [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) с одной строкой и ячейкой, содержащей заголовочный текст.
1. Создайте нижний колонтитул [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) с единственной строкой и ячейкой, содержащей текст нижнего колонтитула.
1. Добавьте таблицы к соответствующим [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) объекты.
1. Установите нижний колонтитул [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) для правильного горизонтального позиционирования.
1. Откройте [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) используя соответствующие методы.
1. Пройдитесь по всем страницам и назначьте заголовок и нижний колонтитул, основанные на таблице, для каждой страницы.
1. Сохраните изменённое [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) в файл вывода.

```python
import aspose.pdf as ap

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

## Добавление заголовков и колонтитулов в LaTeX

Добавьте в заголовки и нижние колонтитулы, содержащие контент в формате LaTeX, на всех страницах PDF-документа, используя Aspose.PDF for Python. LaTeX позволяет отображать математические символы, даты, символы копирайта и другое расширенное форматирование. В заголовке присутствует динамическая дата, а в нижнем колонтитуле отображается символ копирайта вместе с текущим номером страницы и общим количеством страниц.

Следующий фрагмент кода показывает, как использовать [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) в заголовках и нижних колонтитулах PDF с использованием Aspose.PDF for Python via .NET.

1. Откройте [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) используя соответствующие методы.
1. Определите общее количество страниц для использования в динамических нижних колонтитулах.
1. Итерируйте все страницы документа.
1. Создайте [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) объект для заголовка.
1. Создайте [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) для текста заголовка, содержащего команды LaTeX (например, `\\today\\`).
1. Создайте [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) объект для нижнего колонтитула.
1. Создайте [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) для текста нижнего колонтитула, включая символы LaTeX и нумерацию страниц.
1. Добавьте [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) к соответствующему объекту заголовка/нижнего колонтитула.
1. Привязать заголовок и нижний колонтитул к текущей странице.
1. Сохраните изменённое [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) в файл вывода.

```python
import aspose.pdf as ap

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

## Темы, связанные со страницей

- [Работа со страницами PDF в Python](/pdf/ru/python-net/working-with-pages/)
- [Добавить номера страниц в PDF с помощью Python](/pdf/ru/python-net/add-page-number/)
- [Поставить штамп на страницы PDF в Python](/pdf/ru/python-net/stamping/)
- [Форматировать PDF‑документы в Python](/pdf/ru/python-net/formatting-pdf-document/)