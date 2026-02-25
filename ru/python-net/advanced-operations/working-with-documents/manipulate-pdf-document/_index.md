---
title: Манипулирование PDF‑документом в Python через .NET
linktitle: Манипулирование PDF‑документом
type: docs
weight: 20
url: /ru/python-net/manipulate-pdf-document/
description: В этой статье содержится информация о том, как проверять PDF‑документ на соответствие стандарту PDF A с помощью Python, как работать с оглавлением (TOC), как установить срок действия PDF и т.д.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Руководство по работе с PDF‑документами с использованием Python
Abstract: В этой статье представлено подробное руководство по работе с PDF‑документами в Python, в частности с использованием библиотеки Aspose.PDF. Описываются различные функции, включая проверку PDF‑документов на соответствие требованиям PDF/A‑1a и PDF/A‑1b с помощью метода `validate` класса `Document`. Также подробно рассматривается добавление, настройка и управление оглавлением (TOC) в PDF‑файлах, такое как установка разных типов TabLeaderType, скрытие номеров страниц и настройка нумерации страниц с префиксом. Кроме того, статья объясняет, как установить дату окончания действия PDF‑документа, внедряя JavaScript для ограничения доступа, а также как «сплющить» заполняемые формы в PDF, делая их недоступными для редактирования. Каждый раздел снабжен фрагментами кода, демонстрирующими реализацию этих возможностей с помощью Aspose.PDF в Python.
---

## Манипулирование PDF‑документом в Python

## Проверка PDF‑документа на соответствие стандарту PDF A (A 1A и A 1B)

Чтобы проверить PDF‑документ на совместимость с PDF/A‑1a или PDF/A‑1b, используйте метод [validate](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Этот метод позволяет указать имя файла, в который будет сохранён результат, и требуемый тип проверки из перечисления PdfFormat: PDF_A_1A или PDF_A_1B.

Следующий фрагмент кода показывает, как проверить PDF‑документ на соответствие PDF/A‑1A.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Validate PDF for PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1A)
```

Следующий фрагмент кода показывает, как проверить PDF‑документ на соответствие PDF/A‑1b.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Validate PDF for PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1B)
```

## Работа с оглавлением (TOC)

### Добавить оглавление в существующий PDF

TOC в PDF означает "Table of Contents" (Оглавление). Это функция, позволяющая пользователям быстро перемещаться по документу, предоставляя обзор его разделов и заголовков.

Чтобы добавить TOC в существующий PDF‑файл, используйте класс Heading в пространстве имён [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/). Пространство имён [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) позволяет как создавать новые, так и изменять существующие PDF‑файлы. Для добавления TOC в существующий PDF используйте пространство имён Aspose.Pdf. Следующий фрагмент кода показывает, как создать оглавление внутри существующего PDF‑файла с помощью Python через .NET.

```python

    import aspose.pdf as ap

    # Load an existing PDF files
    doc = ap.Document(input_pdf)

    # Get access to first page of PDF file
    tocPage = doc.pages.insert(1)

    # Create object to represent TOC information
    tocInfo = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD

    # Set the title for TOC
    tocInfo.title = title
    tocPage.toc_info = tocInfo

    # Create string objects which will be used as TOC elements
    titles = ["First page", "Second page", "Third page", "Fourth page"]
    for i in range(0, 2):
        # Create Heading object
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = tocPage
        heading2.segments.append(segment2)

        # Specify the destination page for heading object
        heading2.destination_page = doc.pages[i + 2]

        # Destination page
        heading2.top = doc.pages[i + 2].rect.height

        # Destination coordinate
        segment2.text = titles[i]

        # Add heading to page containing TOC
        tocPage.paragraphs.add(heading2)

    # Save the updated document
    doc.save(output_pdf)
```

### Установить различный TabLeaderType для разных уровней TOC

Aspose.PDF для Python также позволяет задавать разные TabLeaderType для разных уровней TOC. Необходимо установить свойство [line_dash](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) класса [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/).

```python

    import aspose.pdf as ap

    doc = ap.Document()
    tocPage = doc.pages.add()
    toc_info = ap.TocInfo()

    # set LeaderType
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 30
    toc_info.title = title

    # Add the list section to the sections collection of the Pdf document
    tocPage.toc_info = toc_info
    # Define the format of the four levels list by setting the left margins
    # and
    # text format settings of each level

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
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

    # Create a section in the Pdf document
    page = doc.pages.add()

    # Add four headings in the section
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        heading2.toc_page = tocPage
        segment2.text = "Sample Heading" + str(Level)
        heading2.text_state.font = ap.text.FontRepository.find_font("Arial")

        # Add the heading into Table Of Contents.
        heading2.is_in_list = True
        page.paragraphs.add(heading2)

    # save the Pdf
    doc.save(output_pdf)
```

### Скрыть номера страниц в TOC

Если вы не хотите отображать номера страниц вместе с заголовками в TOC, можно установить свойство [is_show_page_numbers](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) класса [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) в значение false. Ниже приведён пример кода для скрытия номеров страниц в оглавлении:

```python

    import aspose.pdf as ap

    doc = ap.Document()
    toc_page = doc.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    # Add the list section to the sections collection of the Pdf document
    toc_page.toc_info = toc_info
    # Define the format of the four levels list by setting the left margins and
    # text format settings of each level

    toc_info.is_show_page_numbers = False
    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD
    page = doc.pages.add()
    # Add four headings in the section
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        segment2.text = "this is heading of level " + str(Level)
        heading2.is_in_list = True
        page.paragraphs.add(heading2)
    doc.save(output_pdf)

```

### Настройка номеров страниц при добавлении TOC

Часто требуется настроить нумерацию страниц в TOC при её добавлении в PDF‑документ. Например, может потребоваться добавить префикс перед номером страницы, такой как P1, P2, P3 и т.д. В этом случае Aspose.PDF для Python предоставляет свойство [page_numbers_prefix](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) класса [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/), которое можно использовать для настройки номеров страниц, как показано в следующем примере кода.

```python

    import aspose.pdf as ap

    # Load an existing PDF files
    doc = ap.Document(input_pdf)
    # Get access to first page of PDF file
    toc_page = doc.pages.insert(1)
    # Create object to represent TOC information
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    # Set the title for TOC
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info
    for i in range(len(doc.pages)):
        # Create Heading object
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        # Specify the destination page for heading object
        heading2.destination_page = doc.pages[i + 1]
        # Destination page
        heading2.top = doc.pages[i + 1].rect.height
        # Destination coordinate
        segment2.text = "Page " + str(i)
        # Add heading to page containing TOC
        toc_page.paragraphs.add(heading2)

    # Save the updated document
    doc.save(output_pdf)

```

## Как установить срок действия PDF

Мы применяем привилегии доступа к PDF‑файлам, чтобы определённая группа пользователей могла использовать определённые функции/объекты PDF‑документов. Чтобы ограничить доступ к PDF‑файлу, обычно применяется шифрование, и иногда возникает необходимость установить срок действия PDF‑файла, чтобы пользователь, открывающий/просматривающий документ, получал корректное сообщение о конце срока действия файла.

```python

    import aspose.pdf as ap

    # Instantiate Document object
    doc = ap.Document()
    # Add page to pages collection of PDF file
    doc.pages.add()
    # Add text fragment to paragraphs collection of page object
    doc.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
    # Create JavaScript object to set PDF expiry date
    javaScript = ap.annotations.JavascriptAction(
        "var year=2017;"
        + "var month=5;"
        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        + "expiry = new Date(year, month);"
        + "if (today.getTime() > expiry.getTime())"
        + "app.alert('The file is expired. You need a new one.');"
    )
    # Set JavaScript as PDF open action
    doc.open_action = javaScript

    # Save PDF Document
    doc.save(output_pdf)
```

## Преобразование заполняемого PDF в плоский в Python

PDF‑документы часто включают формы с интерактивными заполняемыми элементами, такими как переключатели, флажки, текстовые поля, списки и т.д. Чтобы сделать их недоступными для редактирования в различных приложениях, необходимо «сплющить» (flatten) PDF‑файл.
Aspose.PDF предоставляет функцию для «сплющивания» вашего PDF в Python всего несколькими строками кода:

```python

    import aspose.pdf as ap

    # Load source PDF form
    doc = ap.Document(input_pdf)

    # Flatten Flatten Fillable PDF
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(output_pdf)
```


