---
title: Добавление текстовых штампов в PDF с помощью Python
linktitle: Текстовые штампы в PDF-файле
type: docs
weight: 20
url: /ru/python-net/text-stamps-in-the-pdf-file/
description: Добавьте текстовый штамп в PDF‑документ, используя класс TextStamp с библиотекой Aspose.PDF для Python.
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить текстовые штампы в PDF с помощью Python
Abstract: В этой статье представлено полное руководство по добавлению текстовых штампов в PDF‑файлы с использованием библиотеки Aspose.PDF для Python. Описывается использование класса `TextStamp` для создания настраиваемых текстовых штампов со свойствами, такими как размер шрифта, стиль, цвет и выравнивание. Статья включает фрагменты кода, демонстрирующие, как добавить простой текстовый штамп, настроить выравнивание текста и применить продвинутые режимы отрисовки, такие как заполненный контурный текст. В первом разделе объясняется создание объектов `Document` и `TextStamp`, установка свойств текста и добавление штампа на определённую страницу. Во втором разделе вводится свойство `text_alignment` для горизонтального и вертикального выравнивания текста, приводится пример кода центрирования текста на странице PDF. В последнем разделе рассматриваются режимы отрисовки, демонстрируя, как добавить заполненный контурный текст с помощью объекта `TextState`, устанавливая цвет контура и режим отрисовки перед привязкой к штампу. Каждый раздел сопровождается практическими примерами для облегчения понимания и внедрения.
---

## Добавление текстового штампа с помощью Python

Вы можете использовать класс [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) для добавления текстового штампа в PDF‑файл. Класс [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) предоставляет свойства, необходимые для создания штампа на основе текста, такие как размер шрифта, стиль шрифта и цвет шрифта и т.д. Чтобы добавить текстовый штамп, вам нужно создать объект Document и объект TextStamp, задав требуемые свойства. После этого вы можете вызвать метод [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) страницы Page, чтобы добавить штамп в PDF. Следующий фрагмент кода показывает, как добавить текстовый штамп в PDF‑файл. Это полезно для добавления аннотаций, водяных знаков или меток на страницы PDF.

1. Откройте PDF‑документ.
1. Создайте объект TextStamp.
1. Задайте поведение фона штампа.
1. Разместите штамп на странице.
1. Поверните штамп при необходимости.
1. Установите свойства текста.
1. Добавьте штамп на страницу.
1. Сохраните изменённый PDF‑документ.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

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
    text_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    text_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    text_stamp.text_state.foreground_color = ap.Color.dark_green
    # Add stamp to particular page
    document.pages[1].add_stamp(text_stamp)

    document.save(output_file_name)
```

