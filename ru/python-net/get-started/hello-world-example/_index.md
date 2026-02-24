---
title: Пример Hello World на Python
linktitle: Пример Hello World
type: docs
weight: 20
url: /ru/python-net/hello-world-example/
description: Этот пример демонстрирует, как создать простой PDF‑документ с текстом Hello World, используя Aspose.PDF для Python через .NET.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Пример Hello World через Python
Abstract: Эта статья предоставляет пример Hello World с использованием библиотеки Aspose.PDF для Python через .NET для создания PDF‑документа. Пример демонстрирует базовые шаги использования Aspose.PDF API путем генерации PDF с текстом "Hello World!". Процесс включает создание объекта `Document`, добавление `Page`, создание объекта `TextFragment`, установку свойств текста, таких как размер шрифта и цвет, а также использование `TextBuilder` для добавления текста на страницу. Полученный PDF затем сохраняется как "HelloWorld_out.pdf". Статья содержит полностью готовый фрагмент кода на Python, иллюстрирующий эти шаги, служит вводным руководством по использованию библиотеки.
---

Пример "Hello World" демонстрирует самый простой синтаксис и самую простую программу на любом языке программирования. Разработчики знакомятся с базовым синтаксисом языка, изучая, как вывести "Hello World" на экран устройства. Поэтому мы традиционно начнём знакомство с нашей библиотекой с него.

В этой статье мы создаём PDF‑документ, содержащий текст "Hello World!". После установки **Aspose.PDF for Python via .NET** в вашей среде вы можете выполнить приведённый ниже пример кода, чтобы увидеть, как работает API Aspose.PDF.

Ниже приведённый фрагмент кода следует этим шагам:

1. Создать объект [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 
1. Добавить [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) к объекту документа
1. Создать объект [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) 
1. Установить цвета текста
1. Создать Text Builder
1. Добавить [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) на страницу
1. [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) результирующий PDF‑документ

Следующий фрагмент кода — программа "Hello World", демонстрирующая функциональность Aspose.PDF для Python через .NET API.

```python

from datetime import timedelta
import aspose.pdf as ap

def run_simple(self):
    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Add text to new page
    textFragment = ap.text.TextFragment("Hello, world!")
    textFragment.position = ap.text.Position(100, 600)

    textFragment.text_state.font_size = 12
    textFragment.text_state.font = ap.text.FontRepository.find_font(
        "TimesNewRoman"
    )
    textFragment.text_state.background_color = ap.Color.blue
    textFragment.text_state.foreground_color = ap.Color.yellow

    # Create TextBuilder object
    textBuilder = ap.text.TextBuilder(page)

    # Append the text fragment to the PDF page
    textBuilder.append_text(textFragment)

    document.save(self.data_dir + "HelloWorld_out.pdf")
```
