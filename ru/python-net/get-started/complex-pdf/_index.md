---
title: Создание сложного PDF
linktitle: Создание сложного PDF
type: docs
weight: 30
url: /ru/python-net/complex-pdf-example/
description: Aspose.PDF for Python via .NET позволяет создавать более сложные документы, содержащие изображения, фрагменты текста и таблицы в одном документе.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создать сложный PDF с использованием Python
Abstract: В этой статье расширяется базовый процесс создания PDF, продемонстрированный в примере \"Привет, мир\", показывая, как создать более сложный PDF‑документ с использованием Python и Aspose.PDF. Примерный документ разработан для вымышленной компании, предоставляющей услуги пассажирских паромных перевозок, и включает изображение, два фрагмента текста (заголовок и абзац) и таблицу. Процесс включает несколько шагов — создание объекта `Document` для создания пустого PDF, добавление `Page`, а затем вставку `Image` на страницу. Для заголовка создаётся `TextFragment` с шрифтом Arial размером 24 pt и выравниванием по центру, который затем добавляется к абзацам страницы. Второй `TextFragment` добавляется для описания, используя шрифт Times New Roman размером 14 pt и выравнивание по левому краю. Затем создаётся таблица и форматируется с конкретными ширинами столбцов, границами и отступами. Таблица включает строку заголовка с выделенными ячейками и несколько строк данных, генерируемых в процессе итерации
---

Пример [Привет, мир](/pdf/python-net/hello-world-example/) показал простые шаги по созданию PDF‑документа с использованием Python и Aspose.PDF. В этой статье мы рассмотрим создание более сложного документа с Aspose.PDF для Python. В качестве примера возьмём документ вымышленной компании, занимающейся пассажирскими паромными перевозками. Наш документ будет содержать изображение, два фрагмента текста (заголовок и абзац) и таблицу.

Если мы создаём документ с нуля, нам необходимо следовать определённым шагам:

1. Создать объект [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). На этом этапе мы создадим пустой PDF‑документ с некоторыми метаданными, но без страниц.
1. Добавить [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) к объекту документа. Теперь наш документ будет содержать одну страницу.
1. Добавить [Image](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/) на страницу.
1. Создать [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) для заголовка. Для заголовка мы будем использовать шрифт Arial размером 24 pt и выравнивание по центру.
1. Добавить заголовок в страницу [абзацы](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. Создать [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) для описания. Для описания мы будем использовать шрифт Arial размером 24 pt и выравнивание по центру.
1. Добавить (description) в абзацы страницы.
1. Создать и оформить таблицу. Установить ширину столбцов, границы, отступы и шрифт.
1. Добавить (table) в страницу [абзацы](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. Сохранить документ "Complex.pdf".

```python

from datetime import timedelta
import aspose.pdf as ap

def run_complex(self):

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()

    # Add image
    imageFileName = self.data_dir + "logo.png"
    page.add_image(imageFileName, ap.Rectangle(20, 730, 120, 830, True))

    # Add Header
    header = ap.text.TextFragment("New ferry routes in Fall 2029")
    header.text_state.font = ap.text.FontRepository.find_font("Arial")
    header.text_state.font_size = 24
    header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    header.position = ap.text.Position(130, 720)
    page.paragraphs.add(header)

    # Add description
    descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. \
    Ferry service is operating at half capacity and on a reduced schedule. Expect lineups."
    description = ap.text.TextFragment(descriptionText)
    description.text_state.font = ap.text.FontRepository.find_font(
        "Times New Roman"
    )
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # Add table
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(
        ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray
    )
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOX, 0.5, ap.Color.black
    )
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font(
        "Helvetica"
    )

    headerRow = table.rows.add()
    headerRow.cells.add("Departs City")
    headerRow.cells.add("Departs Island")

    i = 0
    while i < headerRow.cells.count:
        headerRow.cells[i].background_color = ap.Color.gray
        headerRow.cells[i].default_cell_text_state.foreground_color = (
            ap.Color.white_smoke
        )
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

    document.save(self.data_dir + "Complex.pdf")
```

