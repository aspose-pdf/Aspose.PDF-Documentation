---
title: Добавление номера страницы в PDF с помощью Python
linktitle: Добавление номера страницы
type: docs
weight: 30
url: /ru/python-net/add-page-number/
description: Aspose.PDF for Python via .NET позволяет добавить штамп номера страницы в ваш PDF‑файл с помощью класса PageNumber Stamp.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить номер страницы в PDF с помощью Python
Abstract: В этой статье рассматривается важность добавления номеров страниц в документы для упрощения навигации и представлена библиотека Aspose.PDF for Python via .NET как инструмент для реализации этого в PDF‑файлах. Библиотека использует класс PageNumberStamp, который предоставляет свойства для настройки штампа номера страницы, включая формат, отступы, выравнивание и начальный номер. Процесс включает создание объекта Document и объекта PageNumberStamp, настройку требуемых свойств и применение штампа к страницам PDF с помощью метода add_stamp(). В статье приведён пример кода на Python, демонстрирующий, как настроить и применить штампы номеров страниц с настраиваемыми атрибутами шрифта.
---

Все документы должны содержать номера страниц. Номера страниц упрощают читателю поиск различных частей документа.

**Aspose.PDF for Python via .NET** позволяет добавлять номера страниц с помощью [PageNumberStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/).

## Добавление штампа номера страницы в PDF

Добавьте динамические штампы номеров страниц в PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с помощью Aspose.PDF for Python. Объект [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/) позволяет автоматически отображать текущий номер страницы вместе с общим числом страниц. В примере показано, как создать штамп номера страницы, настроить его внешний вид (шрифт, размер, стиль, цвет, выравнивание и отступы) с помощью [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/), и применить его к конкретной [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) в PDF через метод [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods). Значения выравнивания берутся из перечисления [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/), а цвет/шрифт/стиль доступны через [`Color`](https://reference.aspose.com/pdf/python-net/aspose.pdf/color/) и [`FontStyles`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontstyles/) (шрифты обнаруживаются через [`FontRepository.find_font()`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/fontrepository/#methods)). Эта функциональность полезна для создания профессиональных нумерованных документов и автоматизации нумерации страниц в PDF‑рабочих процессах.

1. Откройте PDF‑документ.
1. Создайте штамп номера страницы.
1. Установите свойства штампа.
1. Настройте стиль текста.
1. Примените штамп к странице.
1. Сохраните изменённый PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

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
    page_number_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    page_number_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    page_number_stamp.text_state.foreground_color = ap.Color.blue_violet

    # Add stamp to particular page
    document.pages[1].add_stamp(page_number_stamp)

    # Save output document
    document.save(output_file_name)
```

## Добавление римских номеров страниц в PDF

Добавьте номера страниц в формате римских цифр ко всем страницам PDF‑документа. Номера страниц добавляются в виде штампов с помощью [`PageNumberStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagenumberstamp/), с настраиваемыми шрифтом, размером, стилем, цветом и выравниванием. Используйте перечисление [`NumberingStyle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/numberingstyle/) для выбора римских цифр или других схем нумерации. Нумерация также может начинаться с любого указанного значения.

1. Откройте PDF‑документ.
1. Создайте штамп номера страницы.
1. Настройте свойства штампа.
1. Установите внешний вид текста.
1. Примените штамп ко всем страницам.
1. Сохраните изменённый PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

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

## Живой пример

[Добавить номера страниц PDF](https://products.aspose.app/pdf/page-number) — это онлайн‑бесплатное веб‑приложение, которое позволяет изучить, как работает функция добавления номеров страниц.

[![Как добавить номер страницы в pdf с помощью Python](page_number.png)](https://products.aspose.app/pdf/page-number)


