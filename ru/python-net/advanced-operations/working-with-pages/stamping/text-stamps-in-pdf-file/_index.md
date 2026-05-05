---
title: Добавить текстовые штампы в PDF на Python
linktitle: Текстовые штампы в PDF-файле
type: docs
weight: 20
url: /ru/python-net/text-stamps-in-the-pdf-file/
description: Узнайте, как добавлять текстовые штампы в PDF‑документы на Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить текстовые штампы в PDF с помощью Python
Abstract: В этой статье представлено полное руководство по добавлению текстовых штампов в PDF‑файлы с использованием библиотеки Aspose.PDF для Python. Описывается использование класса `TextStamp` для создания настраиваемых текстовых штампов со свойствами, такими как размер шрифта, стиль, цвет и выравнивание. В статье включены фрагменты кода, демонстрирующие, как добавить простой текстовый штамп, настроить выравнивание текста и применить расширенные режимы рендеринга, такие как заливка обводкой текста. Первый раздел объясняет создание объектов `Document` и `TextStamp`, установку свойств текста и добавление штампа на конкретную страницу. Во втором разделе представлено свойство `text_alignment` для горизонтального и вертикального выравнивания текста, с примером кода, показывающим центрирование текста на странице PDF. Последний раздел рассматривает режимы рендеринга, демонстрируя, как добавить текст с заливкой и обводкой с помощью объекта `TextState`, задающего цвет обводки и режим рендеринга перед привязкой к штампу. Каждый раздел сопровождается практическими примерами для облегчения понимания и внедрения.
---

## Добавление текстового штампа с помощью Python

Вы можете использовать [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) класс для добавления текстовой печати в файл PDF. [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) класс предоставляет свойства, необходимые для создания печати на основе текста, такие как размер шрифта, стиль шрифта и цвет шрифта и т.д. Чтобы добавить текстовую печать, вам нужно создать объект Document и объект TextStamp, используя требуемые свойства. После этого вы можете вызвать [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) метод Page для добавления печати в PDF. Следующий фрагмент кода показывает, как добавить текстовую печать в файл PDF. Это полезно для добавления аннотаций, водяных знаков или меток на страницы PDF.

1. Откройте PDF‑документ.
1. Создайте объект TextStamp.
1. Задайте поведение фона штампа.
1. Разместите штамп на странице.
1. Поверните штамп при необходимости.
1. Установите свойства текста.
1. Добавьте штамп на страницу.
1. Сохраните измененный PDF-документ.

```python
import sys
import aspose.pdf as ap
from os import path

def add_text_stamp(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    # Create text stamp
    text_stamp = ap.TextStamp("Sample Stamp")
    # Set whether stamp is background
    text_stamp.background = True
    # Set origin
    text_stamp.x_indent = 100
    text_stamp.y_indent = 100
    # Rotate stamp
    text_stamp.rotate = ap.Rotation.ON90
    # Set text properties
    text_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_stamp.text_state.font_size = 14.0
    text_stamp.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    text_stamp.text_state.foreground_color = ap.Color.dark_green
    # Add stamp to particular page
    document.pages[1].add_stamp(text_stamp)

    document.save(output_file_name)
```

## Связанные темы штампования

- [Нанести штамп на страницы PDF в Python](/pdf/ru/python-net/stamping/)
- [Добавить штампы страниц в PDF на Python](/pdf/ru/python-net/page-stamps-in-the-pdf-file/)
- [Добавить штампы изображений в PDF на Python](/pdf/ru/python-net/image-stamps-in-pdf-page/)
- [Добавить номера страниц в PDF с помощью Python](/pdf/ru/python-net/add-page-number/)