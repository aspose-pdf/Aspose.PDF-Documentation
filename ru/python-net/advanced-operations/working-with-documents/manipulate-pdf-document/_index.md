---
title: Манипулировать PDF-документами в Python
linktitle: Манипулировать PDF-документом
type: docs
weight: 20
url: /ru/python-net/manipulate-pdf-document/
description: Узнайте, как проверять, структурировать и изменять PDF‑документы в Python, включая управление TOC и проверки PDF/A.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Руководство по работе с PDF‑документами с использованием Python
Abstract: Эта статья предоставляет комплексное руководство по манипулированию PDF‑документами с использованием Python, конкретно с библиотекой Aspose.PDF. В ней рассматриваются несколько функций, включая проверку PDF‑документов на соответствие PDF/A-1a и PDF/A-1b с помощью метода `validate` класса `Document`. Также подробно описывается, как добавить, настроить и управлять оглавлением (Table of Contents (TOC)) в PDF‑файлах, например установка различных TabLeaderTypes, скрытие номеров страниц и настройка нумерации страниц с префиксом. Кроме того, статья объясняет, как установить дату истечения срока действия PDF‑документа, внедрив JavaScript для ограничения доступа, и как уплощать заполняемые формы в PDF, делая их не редактируемыми. Каждый раздел сопровождается фрагментами кода, демонстрирующими реализацию этих возможностей с использованием Aspose.PDF в Python.
---

Эта страница полезна, когда вам нужно проверять соответствие PDF требованиям, создавать или настраивать таблицу содержимого, задавать поведение истечения срока действия документа или уплощать заполняемые PDF в рабочих процессах Python.

## Манипулировать PDF документом в Python

## Проверить PDF‑документ на соответствие стандарту PDF/A (A 1A и A 1B)

Чтобы проверить PDF‑документ на совместимость с PDF/A‑1a или PDF/A‑1b, используйте [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) класс [validate](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод. Этот метод позволяет указать имя файла, в котором будет сохранён результат, и требуемый тип проверки PdfFormat enumeration : PDF_A_1A или PDF_A_1B.

Следующий фрагмент кода показывает, как проверить PDF‑документ на соответствие PDF/A-1A.

```python
import sys
from os import path
import aspose.pdf as ap


def validate_pdfa_standard_a1a(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.validate(output_pdf, ap.PdfFormat.PDF_A_1A)
```

Следующий фрагмент кода показывает, как проверить PDF‑документ на соответствие PDF/A‑1b.

```python
import sys
from os import path
import aspose.pdf as ap


def validate_pdfa_standard_a1b(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.validate(output_pdf, ap.PdfFormat.PDF_A_1B)
```

## Работа с TOC

### Добавить TOC в существующий PDF

TOC в PDF обозначает "Table of Contents". Это функция, позволяющая пользователям быстро перемещаться по документу, предоставляя обзор его разделов и заголовков. 

Чтобы добавить TOC в существующий PDF‑файл, используйте класс Heading в [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) пространство имён. Это [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) пространство имён может как создавать новые, так и изменять существующие PDF‑файлы. Чтобы добавить TOC в существующий PDF, используйте пространство имён Aspose.Pdf. Следующий фрагмент кода показывает, как создать оглавление внутри существующего PDF‑файла с помощью Python via .NET.

```python
import sys
from os import path
import aspose.pdf as ap


def add_table_of_contents(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.insert(1)
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_page.toc_info = toc_info

    titles = ["First page", "Second page"]
    for index, title_text in enumerate(titles[:2]):
        heading = ap.Heading(1)
        segment = ap.text.TextSegment(title_text)
        heading.toc_page = toc_page
        heading.segments.append(segment)
        destination_page = document.pages[index + 2]
        heading.destination_page = destination_page
        heading.top = destination_page.rect.height
        toc_page.paragraphs.add(heading)

    document.save(output_pdf)
```

### Установить разный TabLeaderType для разных уровней TOC

Aspose.PDF for Python также позволяет устанавливать разные TabLeaderType для разных уровней TOC. Вам нужно установить [line_dash](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) свойство [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/).

```python
import sys
from os import path
import aspose.pdf as ap


def set_toc_levels(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.add()
    toc_info = ap.TocInfo()
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 30
    toc_info.title = title
    toc_page.toc_info = toc_info

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    toc_info.format_array[1].margin.left = 10
    toc_info.format_array[1].margin.right = 30
    toc_info.format_array[1].line_dash = 3
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].margin.left = 20
    toc_info.format_array[2].margin.right = 30
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].line_dash = ap.text.TabLeaderType.SOLID
    toc_info.format_array[3].margin.left = 30
    toc_info.format_array[3].margin.right = 30
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    page = document.pages.add()
    for level in range(1, 5):
        heading = ap.Heading(level)
        heading.is_auto_sequence = True
        heading.toc_page = toc_page
        heading.text_state.font = ap.text.FontRepository.find_font("Arial")
        segment = ap.text.TextSegment(f"Sample Heading{level}")
        heading.segments.append(segment)
        heading.is_in_list = True
        page.paragraphs.add(heading)

    document.save(output_pdf)
```

### Скрыть номера страниц в оглавлении

В случае, если вы не хотите отображать номера страниц вместе с заголовками в TOC, вы можете использовать [is_show_page_numbers](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) свойство [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) Class как false. Пожалуйста, проверьте следующий фрагмент кода, чтобы скрыть номера страниц в оглавлении:

```python
import sys
from os import path
import aspose.pdf as ap


def hide_page_numbers_in_toc(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_info.is_show_page_numbers = False
    toc_page.toc_info = toc_info

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    page = document.pages.add()
    for level in range(1, 2):
        heading = ap.Heading(level)
        heading.toc_page = toc_page
        heading.is_auto_sequence = True
        heading.is_in_list = True
        segment = ap.text.TextSegment(f"this is heading of level {level}")
        heading.segments.append(segment)
        page.paragraphs.add(heading)

    document.save(output_pdf)
```

### Настройте номера страниц при добавлении TOC

Обычно настраивают нумерацию страниц в оглавлении при добавлении оглавления в PDF‑документ. Например, может потребоваться добавить префикс перед номером страницы, такой как P1, P2, P3 и так далее. В таком случае Aspose.PDF for Python предоставляет [page_numbers_prefix](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) свойство [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) класс, который может использоваться для настройки нумерации страниц, как показано в следующем примере кода.

```python
import sys
from os import path
import aspose.pdf as ap


def customize_page_numbers_in_toc(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.insert(1)
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info

    for index, page in enumerate(document.pages, start=1):
        heading = ap.Heading(1)
        heading.toc_page = toc_page
        heading.destination_page = page
        heading.top = page.rect.height
        segment = ap.text.TextSegment(f"Page {index}")
        heading.segments.append(segment)
        toc_page.paragraphs.add(heading)

    document.save(output_pdf)
```

## Как установить дату истечения срока действия PDF

Мы применяем привилегии доступа к PDF‑файлам, чтобы определённая группа пользователей могла получать доступ к конкретным функциям/объектам PDF‑документов. Для ограничения доступа к PDF‑файлам мы обычно используем шифрование и можем иметь требование установить срок действия PDF‑файла, чтобы пользователь, получающий доступ/просматривающий документ, получил корректное уведомление о сроке истечения действия PDF‑файла.

```python
import sys
from os import path
import aspose.pdf as ap


def set_pdf_expiry_date(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.pages.add()
    document.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
    script = ap.annotations.JavascriptAction(
        "var year=2017;"
        "var month=5;"
        "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        "expiry = new Date(year, month);"
        "if (today.getTime() > expiry.getTime())"
        "app.alert('The file is expired. You need a new one.');"
    )
    document.open_action = script
    document.save(output_pdf)
```

## Уплощение заполняемого PDF в Python

PDF‑документы часто включают формы с интерактивными заполняемыми элементами, такими как radio buttons, checkboxes, text boxes, lists и т. д. Чтобы сделать их недоступными для редактирования в различных приложениях, необходимо выполнить уплощение (flatten) PDF‑файла.
Aspose.PDF предоставляет функцию для уплощения вашего PDF в Python всего несколькими строками кода:

```python
import sys
from os import path
import aspose.pdf as ap


def flatten_fillable_pdf(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    if document.form and document.form.fields:
        for field in document.form.fields:
            field.flatten()
    document.save(output_pdf)
```

## Связанные темы Document

- [Работа с PDF документами в Python](/pdf/ru/python-net/working-with-documents/)
- [Форматировать PDF документы в Python](/pdf/ru/python-net/formatting-pdf-document/)
- [Создайте PDF-файлы в Python](/pdf/ru/python-net/create-pdf-document/)
- [Оптимизировать PDF файлы в Python](/pdf/ru/python-net/optimize-pdf/)
