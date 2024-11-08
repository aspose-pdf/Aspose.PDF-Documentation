---
title: Создать или добавить таблицу в PDF с использованием Python
linktitle: Создать или добавить таблицу
type: docs
weight: 10
url: /ru/python-net/add-table-in-existing-pdf-document/
description: Aspose.PDF для Python через .NET - это библиотека, используемая для создания, чтения и редактирования таблиц PDF. Ознакомьтесь с другими расширенными функциями в этой теме.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Создать или добавить таблицу в PDF с использованием Python",
    "alternativeHeadline": "Как добавить таблицу в PDF с помощью Python через .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, python, создать таблицу в pdf, добавить таблицу",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
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
    "url": "/python-net/add-table-in-existing-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-table-in-existing-pdf-document/"
    },
    "dateModified": "2023-02-04",
    "description": "Aspose.PDF для Python через .NET - это библиотека, используемая для создания, чтения и редактирования таблиц PDF. Ознакомьтесь с другими расширенными функциями в этой теме."
}
</script>


## Создание таблицы с использованием Python

Таблицы важны при работе с PDF-документами. Они предоставляют отличные возможности для систематического отображения информации. Пространство имен Aspose.PDF содержит классы с именами [Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/), [Cell](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/) и [Row](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/), которые предоставляют функциональность для создания таблиц при генерации PDF-документов с нуля.

Таблицу можно создать, создав объект класса Table.

```python

    table = ap.Table()
```

### Добавление таблицы в существующий PDF-документ

Чтобы добавить таблицу в существующий PDF-файл с помощью Aspose.PDF для Python через .NET, выполните следующие шаги:

1. Загрузите исходный файл.
1. Инициализируйте таблицу и установите ее столбцы и строки.
1. Установите настройки таблицы (мы установили границы).
1. Заполните таблицу.
1. Добавьте таблицу на страницу.
1. Сохраните файл.

Следующие фрагменты кода показывают, как добавить текст в существующий PDF-файл.

```python

    import aspose.pdf as ap

    # Загрузить исходный PDF документ
    doc = ap.Document(input_file)
    # Инициализирует новый экземпляр таблицы
    table = ap.Table()
    # Установить цвет границы таблицы как LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.from_rgb(apd.Color.light_gray))
    # Установить границу для ячеек таблицы
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 5, ap.Color.from_rgb(apd.Color.light_gray))
    # Создать цикл для добавления 10 строк
    for row_count in range(0, 10):
        # Добавить строку в таблицу
        row = table.rows.add()
        # Добавить ячейки таблицы
        row.cells.add("Колонка (" + str(row_count) + ", 1)")
        row.cells.add("Колонка (" + str(row_count) + ", 2)")
        row.cells.add("Колонка (" + str(row_count) + ", 3)")
    # Добавить объект таблицы на первую страницу входного документа
    doc.pages[1].paragraphs.add(table)
    # Сохранить обновленный документ, содержащий объект таблицы
    doc.save(output_file)
```

### ColSpan и RowSpan в таблицах

Aspose.PDF для Python через .NET предоставляет свойство [col_span](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/#properties) для объединения столбцов в таблице и свойство [row_span](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/#properties) для объединения строк.


Мы используем свойство `col_span` или `row_span` объекта `Cell`, который создает ячейку таблицы. После применения необходимых свойств созданная ячейка может быть добавлена в таблицу.

```python

    import aspose.pdf as ap

    # Инициализировать объект Document, вызвав его пустой конструктор
    pdf_document = ap.Document()
    pdf_document.pages.add()
    # Инициализировать новый экземпляр Table
    table = ap.Table()
    # Установить цвет границы таблицы как LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # Установить границу для ячеек таблицы
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.5, ap.Color.black)
    # Добавить 1-й ряд в таблицу
    row1 = table.rows.add()
    for cellCount in range(1, 5):
        # Добавить ячейки таблицы
        row1.cells.add("Тест 1" + str(cellCount))

    # Добавить 2-й ряд в таблицу
    row2 = table.rows.add()
    row2.cells.add("Тест 2 1")
    cell = row2.cells.add("Тест 2 2")
    cell.col_span = 2
    row2.cells.add("Тест 2 4")

    # Добавить 3-й ряд в таблицу
    row3 = table.rows.add()
    row3.cells.add("Тест 3 1")
    row3.cells.add("Тест 3 2")
    row3.cells.add("Тест 3 3")
    row3.cells.add("Тест 3 4")

    # Добавить 4-й ряд в таблицу
    row4 = table.rows.add()
    row4.cells.add("Тест 4 1")
    cell = row4.cells.add("Тест 4 2")
    cell.row_span = 2
    row4.cells.add("Тест 4 3")
    row4.cells.add("Тест 4 4")

    # Добавить 5-й ряд в таблицу
    row5 = table.rows.add()
    row5.cells.add("Тест 5 1")
    row5.cells.add("Тест 5 3")
    row5.cells.add("Тест 5 4")

    # Добавить объект таблицы на первую страницу входного документа
    pdf_document.pages[1].paragraphs.add(table)
    # Сохранить обновленный документ, содержащий объект таблицы
    pdf_document.save(output_file)
```


Результат выполнения кода ниже — таблица, изображенная на следующем рисунке:

![Демо ColSpan и RowSpan](colspan_rowspan.png)

## Работа с границами, отступами и полями

Обратите внимание, что также поддерживается возможность установки стиля границы, отступов и полей ячеек для таблиц. Прежде чем углубляться в технические детали, важно понять концепции границ, отступов и полей, которые представлены ниже на диаграмме:

![Границы, отступы и поля](set-border-style-margins-and-padding-of-table_1.png)

На приведенной выше диаграмме видно, что границы таблицы, строки и ячейки перекрываются. Используя Aspose.PDF, таблица может иметь отступы, а ячейки могут иметь поля. Чтобы установить поля ячеек, необходимо установить отступы ячеек.

### Границы

Чтобы установить границы объектов [Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/), [Row](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/) и [Cell](https://reference.aspose.com/pdf/python-net/aspose.pdf/cell/), используйте свойства Table.border, Row.border и Cell.border.
 Границы ячеек также могут быть установлены с помощью свойства [Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) или [Row](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) класса `default_cell_border`. Все свойства, связанные с границами, обсужденные выше, назначаются экземпляру класса Row, который создается путем вызова его конструктора. Класс Row имеет множество перегрузок, которые принимают почти все параметры, необходимые для настройки границы.

### Поля или Отступы

Отступы ячеек могут управляться с помощью свойства [Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/row/#properties) класса `default_cell_padding`. Все свойства, связанные с отступами, назначаются экземпляру класса [MarginInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/), который принимает информацию о параметрах `left`, `right`, `top` и `bottom` для создания пользовательских полей.
В следующем примере ширина границы ячейки установлена на 0.1 пункта, ширина границы таблицы установлена на 1 пункт, а отступ в ячейке установлен на 5 пунктов.

![Margin and Border in PDF Table](margin-border.png)

```python

    import aspose.pdf as ap

    # Создать экземпляр объекта Document, вызвав его пустой конструктор
    doc = ap.Document()
    page = doc.pages.add()
    # Создать экземпляр объекта таблицы
    tab1 = ap.Table()
    # Добавить таблицу в коллекцию абзацев нужного раздела
    page.paragraphs.add(tab1)
    # Установить ширину столбцов таблицы
    tab1.column_widths = "50 50 50"
    # Установить границу ячейки по умолчанию с помощью объекта BorderInfo
    tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # Установить границу таблицы с использованием другого настраиваемого объекта BorderInfo
    tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # Создать объект MarginInfo и установить его отступы слева, снизу, справа и сверху
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # Установить отступ ячейки по умолчанию в объект MarginInfo
    tab1.default_cell_padding = margin
    # Создать строки в таблице, а затем ячейки в строках
    row1 = tab1.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add()
    my_text = ap.text.TextFragment("col3 with large text string")
    # Row1.Cells.Add("col3 с длинной строкой текста, чтобы поместить внутри ячейки")
    row1.cells[2].paragraphs.add(my_text)
    row1.cells[2].is_word_wrapped = False
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # Сохранить Pdf
    doc.save(output_file)
```


Чтобы создать таблицу с закругленными углами, используйте значение [rounded_border_radius](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/#properties) класса [BorderInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) и установите стиль углов таблицы на круглый.

```python
    
    import aspose.pdf as ap
    
    tab1 = ap.Table()
    graph = ap.GraphInfo()
    graph.color = ap.Color.red
    # Создать пустой объект BorderInfo
    b_info = ap.BorderInfo(ap.BorderSide.ALL, graph)
    # Установить границу закругленной с радиусом закругления 15
    b_info.rounded_border_radius = 15
    # Установить стиль углов таблицы как круглый
    tab1.corner_style = ap.BorderCornerStyle.ROUND
    # Установить информацию о границе таблицы
    tab1.border = b_info
```

## Применение различных настроек AutoFit к таблице

При создании таблицы с использованием визуального инструмента, такого как Microsoft Word, вы часто будете использовать одну из функций AutoFit, чтобы удобно настроить размер таблицы до нужной ширины.
 Например, вы можете использовать опцию "AUTO_FIT_TO_WINDOW", чтобы подогнать ширину таблицы к странице, или AUTO_FIT_TO_CONTENT. По умолчанию, при использовании Aspose.Pdf для создания новой таблицы, применяется [column_adjustment](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) со значением "Customized". В следующем фрагменте кода мы устанавливаем параметры объектов [MarginInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) и [BorderInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/borderinfo/) в таблице. Протестируйте пример и оцените результат.

```python

    import aspose.pdf as ap

    # Создайте объект Pdf, вызвав его пустой конструктор
    doc = ap.Document()
    # Создайте секцию в объекте Pdf
    sec1 = doc.pages.add()
    # Создайте объект таблицы
    tab1 = ap.Table()
    # Добавьте таблицу в коллекцию абзацев нужной секции
    sec1.paragraphs.add(tab1)
    # Установите ширину колонок таблицы
    tab1.column_widths = "50 50 50"
    tab1.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_WINDOW
    # Установите границу ячейки по умолчанию с использованием объекта BorderInfo
    tab1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # Установите границу таблицы, используя другой настраиваемый объект BorderInfo
    tab1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # Создайте объект MarginInfo и установите его отступы слева, снизу, справа и сверху
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # Установите отступы ячейки по умолчанию в объект MarginInfo
    tab1.default_cell_padding = margin
    # Создайте строки в таблице, а затем ячейки в строках
    row1 = tab1.rows.add()
    row1.cells.add("col1")
    row1.cells.add("col2")
    row1.cells.add("col3")
    row2 = tab1.rows.add()
    row2.cells.add("item1")
    row2.cells.add("item2")
    row2.cells.add("item3")
    # Сохраните обновленный документ, содержащий объект таблицы
    doc.save(output_file)
```

### Получение Ширины Таблицы

Иногда требуется динамически получить ширину таблицы. Класс Aspose.PDF.Table имеет метод [get_width()](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#methods) для этой цели. Например, вы не установили ширину столбцов таблицы явно и установили [column_adjustment](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) на 'AUTO_FIT_TO_CONTENT'. В этом случае вы можете получить ширину таблицы следующим образом.

```python

    import aspose.pdf as ap

    # Создать новый документ
    doc = ap.Document()
    # Добавить страницу в документ
    page = doc.pages.add()
    # Инициализировать новую таблицу
    table = ap.Table()
    table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    # Добавить строку в таблицу
    row = table.rows.add()
    # Добавить ячейку в таблицу
    cell = row.cells.add("Текст ячейки 1")
    cell = row.cells.add("Текст ячейки 2")
    # Получить ширину таблицы
    print(table.get_width())
```

## Добавление SVG Изображения в Ячейку Таблицы

Aspose.PDF для Python через .NET предоставляет возможность вставлять ячейки таблицы в PDF файл.
 При создании таблицы вы можете включать как текст, так и изображения в эти ячейки. Кроме того, API предлагает функциональность для преобразования файлов SVG в формат PDF. Используя эти функции вместе, вы можете загрузить SVG-изображение и разместить его в ячейке таблицы.

Следующий фрагмент кода демонстрирует процесс создания объекта таблицы и встраивания SVG-изображения в одну из ее ячеек.

```python

    import aspose.pdf as ap

    # Создать экземпляр объекта Document
    doc = ap.Document()
    # Создать экземпляр изображения
    img = ap.Image()
    # Установить тип изображения как SVG
    img.file_type = ap.ImageFileType.SVG
    # Путь к исходному файлу
    img.file = DIR_INPUT_TABLE + "SVGToPDF.svg"
    # Установить ширину для экземпляра изображения
    img.fix_width = 50
    # Установить высоту для экземпляра изображения
    img.fix_height = 50
    # Создать экземпляр таблицы
    table = ap.Table()
    # Установить ширину для ячеек таблицы
    table.column_widths = "100 100"
    # Создать объект строки и добавить его в экземпляр таблицы
    row = table.rows.add()
    # Создать объект ячейки и добавить его в экземпляр строки
    cell = row.cells.add()
    # Добавить текстовый фрагмент в коллекцию параграфов объекта ячейки
    cell.paragraphs.add(ap.text.TextFragment("First cell"))
    # Добавить другую ячейку в объект строки
    cell = row.cells.add()
    # Добавить SVG-изображение в коллекцию параграфов недавно добавленного экземпляра ячейки
    cell.paragraphs.add(img)
    # Создать объект страницы и добавить его в коллекцию страниц экземпляра документа
    page = doc.pages.add()
    # Добавить таблицу в коллекцию параграфов объекта страницы
    page.paragraphs.add(table)
    # Сохранить PDF-файл
    doc.save(output_file)
```

## Вставить разрыв страницы между строками таблицы

По умолчанию, когда вы создаете таблицу в PDF-файле, таблица будет распространяться на несколько страниц, если она выходит за пределы нижнего поля таблицы. Однако бывают ситуации, когда необходимо вставить разрывы страниц после добавления определенного количества строк в таблицу. В следующем фрагменте кода описан процесс вставки разрыва страницы после добавления 10 строк в таблицу.

```python

    import aspose.pdf as ap

    # Создать экземпляр класса Document
    doc = ap.Document()
    # Добавить страницу в коллекцию страниц PDF-файла
    doc.pages.add()
    # Создать экземпляр таблицы
    tab = ap.Table()
    # Установить стиль границы для таблицы
    tab.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)
    # Установить стиль границы по умолчанию для таблицы с красным цветом границы
    tab.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.red)
    # Указать ширину столбцов таблицы
    tab.column_widths = "100 100"
    # Создать цикл для добавления 200 строк в таблицу
    for counter in range(0, 201):
        row = ap.Row()
        tab.rows.add(row)
        cell1 = ap.Cell()
        cell1.paragraphs.add(ap.text.TextFragment("Ячейка " + str(counter) + ", 0"))
        row.cells.add(cell1)
        cell2 = ap.Cell()
        cell2.paragraphs.add(ap.text.TextFragment("Ячейка " + str(counter) + ", 1"))
        row.cells.add(cell2)
        # Когда добавлено 10 строк, отобразить новую строку на новой странице
        if counter % 10 == 0 and counter != 0:
            row.is_in_new_page = True
    # Добавить таблицу в коллекцию абзацев PDF-файла
    doc.pages[1].paragraphs.add(tab)
    # Сохранить PDF-документ
    doc.save(output_file)
```


## Отображение таблицы на новой странице

По умолчанию параграфы добавляются в коллекцию параграфов объекта страницы. Однако можно отобразить таблицу на новой странице вместо того, чтобы добавлять ее непосредственно после ранее добавленного объекта на уровне параграфа на странице.

### Пример: Как отобразить таблицу на новой странице с использованием Python

Чтобы отобразить таблицу на новой странице, используйте свойство [is_in_new_page](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) в классе [BaseParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf/baseparagraph/). Следующий фрагмент кода показывает, как это сделать.

```python

    import aspose.pdf as ap

    doc = ap.Document()
    page_info = doc.page_info
    margin_info = page_info.margin

    margin_info.left = 37
    margin_info.right = 37
    margin_info.top = 37
    margin_info.bottom = 37

    page_info.is_landscape = True

    table = ap.Table()
    table.column_widths = "50 100"
    # Добавлена страница.
    cur_page = doc.pages.add()
    for i in range(1, 121):
        row = table.rows.add()
        row.fixed_row_height = 15
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("Content 1"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("HHHHH"))
    paragraphs = cur_page.paragraphs
    paragraphs.add(table)

    table1 = ap.Table()
    table1.column_widths = "100 100"
    for i in range(1, 11):
        row = table1.rows.add()
        cell1 = row.cells.add()
        cell1.paragraphs.add(ap.text.TextFragment("LAAAAAAA"))
        cell2 = row.cells.add()
        cell2.paragraphs.add(ap.text.TextFragment("LAAGGGGGG"))
    table1.is_in_new_page = True
    # Я хочу оставить таблицу 1 на следующей странице, пожалуйста...
    paragraphs.add(table1)
    doc.save(output_file)
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для Python через .NET библиотеку",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "applicationCategory": "Библиотека для манипуляции PDF для Python через .NET",
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