---
title: Добавить нумерацию страниц в PDF с помощью Python
linktitle: Добавление номера страницы
type: docs
weight: 30
url: /ru/python-net/add-page-number/
description: Узнайте, как добавить штампы с номерами страниц в PDF‑документы с помощью Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить номер страницы в PDF с использованием Python
Abstract: В этой статье обсуждается важность добавления номеров страниц в документы для облегчения навигации и представлена библиотека Aspose.PDF for Python via .NET как инструмент для реализации этого в PDF‑файлах. Библиотека использует класс PageNumberStamp, который предоставляет свойства для настройки штампа номера страницы, включая формат, отступы, выравнивание и начальный номер. Процесс включает создание объекта Document и объекта PageNumberStamp, настройку нужных свойств и применение штампа к страницам PDF с помощью метода add_stamp(). В статье приведён пример кода на Python, демонстрирующий, как настроить и применить штампы с номерами страниц с настраиваемыми атрибутами шрифта.
---

Во всех документах должны присутствовать номера страниц. Номер страницы упрощает читателю поиск различных частей документа.

**Aspose.PDF for Python via .NET** позволяет вам добавлять номера страниц с [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/).

## Добавление штампа номера страницы в PDF

Добавьте динамические штампы нумерации страниц в PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) используя Aspose.PDF for Python. The [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) объект позволяет автоматически отображать текущий номер страницы вместе с общим количеством страниц. В примере показано, как создать штамп номера страницы, настроить его внешний вид (шрифт, размер, стиль, цвет, выравнивание и отступы) используя [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/), а также применить его к конкретному [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) в PDF через [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) метод. Значения выравнивания берутся из [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) перечисление, а также цвет/шрифт/стиль доступны через [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) и [`FontStyles`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontstyles/) (шрифты обнаружены через [`FontRepository.find_font()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontrepository/#methods)). Эта функция полезна для создания профессиональных нумерованных документов и автоматизации пагинации в PDF‑рабочих процессах.

1. Откройте PDF‑документ.
1. Создайте штамп номера страницы.
1. Установите свойства штампа.
1. Настройте стиль текста.
1. Примените штамп к странице.
1. Сохраните изменённый PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def add_page_num_stamp(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Create page number stamp
    page_number_stamp = ap.PageNumberStamp()
    # Whether the stamp is background
    page_number_stamp.background = False
    page_number_stamp.format = "Page # of " + str(len(document.pages))
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 1
    # Set text properties
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    document.pages[1].add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## Добавление римской нумерации страниц в PDF

Добавьте номера страниц в формате римских цифр ко всем страницам PDF‑документа. Номера страниц добавляются в виде штампов, используя [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/), с настраиваемыми шрифтом, размером, стилем, цветом и выравниванием. Используйте [`NumberingStyle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/numberingstyle/) enum для выбора римских цифр или других схем нумерации. Нумерация также может начинаться с любого указанного значения.

1. Откройте PDF‑документ.
1. Создайте штамп номера страницы.
1. Настройте свойства штампа.
1. Установите внешний вид текста.
1. Примените штамп ко всем страницам.
1. Сохраните изменённый PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def add_page_num_stamp_roman(input_file_name, output_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Create page number stamp
    page_number_stamp = ap.PageNumberStamp()
    # Whether the stamp is background
    page_number_stamp.background = False
    page_number_stamp.bottom_margin = 10
    page_number_stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    page_number_stamp.starting_number = 42
    page_number_stamp.numbering_style = ap.NumberingStyle.NUMERALS_ROMAN_UPPERCASE

    # Set text properties
    page_number_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    page_number_stamp.text_state.font_size = 14.0
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    for page in document.pages:
        page.add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## Пример

[Добавить номера страниц PDF](https://products.aspose.app/pdf/page-number) это бесплатное онлайн‑веб‑приложение, которое позволяет исследовать, как работает функциональность добавления номеров страниц.

[![Как добавить номер страницы в PDF с помощью Python](page_number.png)](https://products.aspose.app/pdf/page-number)

## Связанные темы штампования

- [Нанести штамп на страницы PDF в Python](/pdf/ru/python-net/stamping/)
- [Добавить штампы страниц в PDF на Python](/pdf/ru/python-net/page-stamps-in-the-pdf-file/)
- [Добавить штампы изображений в PDF на Python](/pdf/ru/python-net/image-stamps-in-pdf-page/)
- [Добавить текстовые штампы в PDF на Python](/pdf/ru/python-net/text-stamps-in-the-pdf-file/)