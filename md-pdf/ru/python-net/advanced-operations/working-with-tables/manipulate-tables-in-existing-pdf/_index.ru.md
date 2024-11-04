---
title: Манипуляция таблицами в существующем PDF
linktitle: Манипуляция таблицами
type: docs
weight: 40
url: /python-net/manipulate-tables-in-existing-pdf/
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Манипуляция таблицами в существующем PDF",
    "alternativeHeadline": "Как обновить содержимое таблиц в существующем PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация pdf документов",
    "keywords": "pdf, python, манипуляция таблицами",
    "wordcount": "302",
    "proficiencyLevel":"Начальный",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/manipulate-tables-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/manipulate-tables-in-existing-pdf/"
    },
    "dateModified": "2023-02-04",
    "description": ""
}
</script>


## Манипуляция с таблицами в существующем PDF

Одной из самых ранних функций, поддерживаемых Aspose.PDF для Python через .NET, является работа с таблицами, и она предоставляет отличную поддержку для добавления таблиц в PDF-файлы, создаваемые с нуля или в любые существующие PDF-файлы. В этом новом выпуске мы реализовали новую функцию поиска и разбора простых таблиц, которые уже существуют на странице PDF-документа. Новый класс с именем [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) предоставляет эти возможности. Использование TableAbsorber очень похоже на существующий класс [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/). Следующий код показывает шаги по обновлению содержимого в конкретной ячейке таблицы.

```python

    import aspose.pdf as ap

    # Загрузить существующий PDF файл
    pdf_document = ap.Document(input_file)
    # Создать объект TableAbsorber для поиска таблиц
    absorber = ap.text.TableAbsorber()
    # Посетить первую страницу с абсорбером
    absorber.visit(pdf_document.pages[1])
    # Получить доступ к первой таблице на странице, их первой ячейке и текстовым фрагментам в ней
    fragment = absorber.table_list[0].row_list[0].cell_list[0].text_fragments[1]
    # Изменить текст первого текстового фрагмента в ячейке
    fragment.text = "hi world"
    pdf_document.save(output_file)
```


## Заменить старую таблицу на новую в PDF документе

Если вам нужно найти конкретную таблицу и заменить ее на нужную, вы можете использовать метод [replace()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods) класса [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) для этого. Следующий пример демонстрирует функциональность замены таблицы внутри PDF документа:

```python

    import aspose.pdf as ap

    # Загрузить существующий PDF документ
    pdf_document = ap.Document(input_file)
    # Создать объект TableAbsorber для поиска таблиц
    absorber = ap.text.TableAbsorber()
    # Посетить первую страницу с абсорбером
    absorber.visit(pdf_document.pages[1])
    # Получить первую таблицу на странице
    table = absorber.table_list[0]
    # Создать новую таблицу
    new_table = ap.Table()
    new_table.column_widths = "100 100 100"
    new_table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 1)

    row = new_table.rows.add()
    row.cells.add("Колонка 1")
    row.cells.add("Колонка 2")
    row.cells.add("Колонка 3")

    # Заменить таблицу на новую
    absorber.replace(pdf_document.pages[1], table, new_table)
    # Сохранить документ
    pdf_document.save(output_file)
```


## Как определить, будет ли таблица разрываться на текущей странице

Этот код генерирует PDF-документ, содержащий таблицу, вычисляет пространство, доступное на странице, и проверяет, приведет ли добавление дополнительных строк в таблицу к разрыву страницы из-за ограничений пространства. Результат сохраняется в выходной файл.

```python

    import aspose.pdf as ap

    # Создать экземпляр объекта класса PDF
    pdf = ap.Document()
    # Добавить раздел в коллекцию разделов PDF-документа
    page = pdf.pages.add()
    # Создать объект таблицы
    table1 = ap.Table()
    table1.margin.top = 300
    # Добавить таблицу в коллекцию параграфов нужного раздела
    page.paragraphs.add(table1)
    # Установить ширину столбцов таблицы
    table1.column_widths = "100 100 100"
    # Установить границу ячеек по умолчанию с использованием объекта BorderInfo
    table1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # Установить границу таблицы с использованием другого настраиваемого объекта BorderInfo
    table1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # Создать объект MarginInfo и задать его отступы слева, снизу, справа и сверху
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # Установить отступ ячеек по умолчанию в объект MarginInfo
    table1.default_cell_padding = margin
    # Если увеличить счетчик до 17, таблица разорвется
    # Потому что она больше не может быть размещена на этой странице
    for row_counter in range(0, 17):
        # Создать строки в таблице, а затем ячейки в строках
        row1 = table1.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
    # Получить информацию о высоте страницы
    page_height = pdf.page_info.height
    # Получить общую информацию о высоте верхнего и нижнего отступов страницы,
    # верхнего отступа таблицы и высоты таблицы.
    total_objects_height = page.page_info.margin.top + page.page_info.margin.bottom + table1.margin.top + \
                           table1.get_height(None)
    # Отобразить информацию о высоте страницы, высоте таблицы, верхнем отступе таблицы, а также
    # информацию о верхнем и нижнем отступах страницы
    print("Высота PDF-документа = " + str(pdf.page_info.height) + "\nИнформация о верхнем отступе = " + str(page.page_info.margin.top)
          + "\nИнформация о нижнем отступе = " + str(page.page_info.margin.bottom) + "\n\nИнформация о верхнем отступе таблицы = "
          + str(table1.margin.top) + "\nСредняя высота строки = " + str(table1.rows[0].min_row_height) + " \nВысота таблицы "
          + str(table1.get_height(None)) + "\n ----------------------------------------" + "\nОбщая высота страницы ="
          + str(page_height) + "\nСовокупная высота, включая таблицу =" + str(total_objects_height))
    # Проверить, если вычесть сумму верхнего отступа страницы + нижнего отступа страницы
    # + верхнего отступа таблицы и высоты таблицы из высоты страницы и это меньше
    # чем 10 (средняя строка может быть больше 10)
    if (page_height - total_objects_height) <= 10:
        # Если значение меньше 10, отобразить сообщение.
        # Которое показывает, что еще одна строка не может быть размещена, и если мы добавим новую
        # строку, таблица разорвется. Это зависит от значения высоты строки.
        print("Высота страницы - высота объектов < 10, поэтому таблица разорвется")
    # Сохранить PDF-документ
    pdf.save(output_file)
```


## Добавление повторяющегося столбца в таблицу

В классе [Aspose.Pdf.Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) вы можете установить [repeating_rows_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties), который будет повторять строки, если таблица слишком длинная по вертикали и переходит на следующую страницу. Однако в некоторых случаях таблицы слишком широкие, чтобы поместиться на одной странице, и их необходимо продолжить на следующей странице. Для этого мы реализовали свойство [repeating_columns_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) в классе [Aspose.Pdf.Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/). Установка этого свойства приведет к тому, что таблица будет разбиваться на следующую страницу по столбцам и повторять заданное количество столбцов в начале следующей страницы. Следующий фрагмент кода показывает использование свойства [repeating_columns_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties):

```python

    import aspose.pdf as ap

    # Создать новый документ
    doc = ap.Document()
    page = doc.pages.add()
    # Создать внешний таблицу, занимающую всю страницу
    outer_table = ap.Table()
    outer_table.column_widths = "100%"
    outer_table.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # Создать объект таблицы, который будет вложен внутрь outerTable и будет разрываться внутри той же страницы
    my_table = ap.Table()
    my_table.broken = ap.TableBroken.VERTICAL_IN_SAME_PAGE
    my_table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    # Добавить outerTable в абзацы страницы
    # Добавить my_table в outerTable
    page.paragraphs.add(outer_table)
    body_row = outer_table.rows.add()
    body_cell = body_row.cells.add()
    body_cell.paragraphs.add(my_table)
    my_table.repeating_columns_count = 5
    page.paragraphs.add(my_table)
    # Добавить строку заголовка
    row = my_table.rows.add()
    row.cells.add("header 1")
    row.cells.add("header 2")
    row.cells.add("header 3")
    row.cells.add("header 4")
    row.cells.add("header 5")
    row.cells.add("header 6")
    row.cells.add("header 7")
    row.cells.add("header 11")
    row.cells.add("header 12")
    row.cells.add("header 13")
    row.cells.add("header 14")
    row.cells.add("header 15")
    row.cells.add("header 16")
    row.cells.add("header 17")
    for row_counter in range(0, 6):
        # Создать строки в таблице, а затем ячейки в строках
        row1 = my_table.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
        row1.cells.add("col " + str(row_counter) + ", 4")
        row1.cells.add("col " + str(row_counter) + ", 5")
        row1.cells.add("col " + str(row_counter) + ", 6")
        row1.cells.add("col " + str(row_counter) + ", 7")
        row1.cells.add("col " + str(row_counter) + ", 11")
        row1.cells.add("col " + str(row_counter) + ", 12")
        row1.cells.add("col " + str(row_counter) + ", 13")
        row1.cells.add("col " + str(row_counter) + ", 14")
        row1.cells.add("col " + str(row_counter) + ", 15")
        row1.cells.add("col " + str(row_counter) + ", 16")
        row1.cells.add("col " + str(row_counter) + ", 17")
    doc.save(output_file)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для Python через .NET библиотека",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "продажи",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для работы с PDF для Python через .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>