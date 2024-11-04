---
title: Создание сложного PDF
linktitle: Создание сложного PDF
type: docs
weight: 30
url: /python-net/complex-pdf-example/
description: Aspose.PDF для Python через .NET позволяет создавать более сложные документы, содержащие изображения, текстовые фрагменты и таблицы в одном документе.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Пример [Hello, World](/pdf/python-net/hello-world-example/) показал простые шаги по созданию PDF-документа с использованием Python и Aspose.PDF. В этой статье мы рассмотрим создание более сложного документа с использованием Aspose.PDF для Python. В качестве примера мы возьмем документ от вымышленной компании, которая занимается пассажирскими паромными перевозками. Наш документ будет содержать изображение, два текстовых фрагмента (заголовок и абзац) и таблицу.

Если мы создаем документ с нуля, нам нужно следовать определенным шагам:

1. Создайте объект [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). На этом шаге мы создадим пустой PDF-документ с некоторыми метаданными, но без страниц.
1. Добавьте [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) к объекту документа. Теперь у нашего документа будет одна страница.
1. Добавьте [Image](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/) на страницу.
1. Создайте [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) для заголовка. Для заголовка мы будем использовать шрифт Arial с размером 24pt и выравниванием по центру.
1. Добавьте заголовок в [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) страницы.
1. Создайте [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) для описания. Для описания мы будем использовать шрифт Arial с размером 24pt и выравниванием по центру.
1. Добавьте (описание) в Paragraphs страницы.
1. Создайте таблицу, добавьте свойства таблицы.

1. Добавить (таблицу) на страницу [параграфы](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. Сохранить документ "Complex.pdf".

```python

    import aspose.pdf as ap

    # Инициализация объекта документа
    document = ap.Document()
    # Добавить страницу
    page = document.pages.add()

    # Добавить изображение
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))

    # Добавить заголовок
    header = ap.text.TextFragment("Новые маршруты паромов осенью 2020")
    header.text_state.font = ap.text.FontRepository.find_font("Arial")
    header.text_state.font_size = 24
    header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    header.position = ap.text.Position(130, 720)
    page.paragraphs.add(header)

    # Добавить описание
    descriptionText = "Посетители должны покупать билеты онлайн, и количество билетов ограничено до 5,000 в день. \
    Паромное сообщение работает на половину мощности и по сокращенному графику. Ожидайте очереди."
    description = ap.text.TextFragment(descriptionText)
    description.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # Добавить таблицу
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray)
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.BOX, 0.5, ap.Color.black)
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font("Helvetica")

    headerRow = table.rows.add()
    headerRow.cells.add("Отправляется из города")
    headerRow.cells.add("Отправляется с острова")

    i = 0
    while i < headerRow.cells.count:
        headerRow.cells[i].background_color = ap.Color.gray
        headerRow.cells[i].default_cell_text_state.foreground_color = ap.Color.white_smoke
        i += 1

    time = timedelta(hours=6, minutes=0)
    incTime = timedelta(hours=0, minutes=30)

    i = 0
    while i < 10:
        dataRow = table.rows.add()
        dataRow.cells.add(str(time))
        time = time.__add__(incTime)
        dataRow.cells.add(str(time))
        i += 1

    page.paragraphs.add(table)

    document.save(output_pdf)
```