---
title: Конвертировать HTML в PDF на Python
linktitle: Конвертировать HTML в PDF файл
type: docs
weight: 40
url: /ru/python-net/convert-html-to-pdf/
lastmod: "2025-09-27"
description: Узнайте, как конвертировать HTML‑контент в PDF‑документ с помощью Aspose.PDF for Python via .NET
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Как конвертировать HTML в PDF с помощью Aspose.PDF for Python
Abstract: Aspose.PDF for Python via .NET предоставляет надёжное решение для создания PDF‑файлов из веб‑страниц и исходного HTML‑кода в приложениях. Эта статья представляет руководство по конвертации HTML в PDF с использованием Python, описывая применение Aspose.PDF for Python, API для работы с PDF, которое обеспечивает беспроблемную конвертацию HTML‑документов в формат PDF. Процесс конвертации можно при необходимости настроить. В статье приведён пример кода на Python, демонстрирующий процесс конвертации, который включает создание экземпляра класса HtmlLoadOptions, инициализацию объекта Document и сохранение полученного PDF‑документа с помощью метода Document.Save(). Кроме того, Aspose предлагает онлайн‑инструмент для конвертации HTML в PDF, позволяющий пользователям ознакомиться с функциональностью и качеством процесса конвертации.
---

## Конвертация HTML в PDF с помощью Python

**Aspose.PDF for Python** — это API для работы с PDF, позволяющее без проблем конвертировать любые существующие HTML‑документы в PDF. Процесс конвертации HTML в PDF можно гибко настроить.

## Конвертация HTML в PDF

Ниже приведён пример кода на Python, показывающий, как конвертировать HTML‑документ в PDF.

1. Создайте экземпляр класса [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/).
1. Инициализируйте объект [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Сохраните полученный PDF‑документ, вызвав метод **document.save()**.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.page_layout_option = ap.HtmlPageLayoutOption.SCALE_TO_PAGE_WIDTH
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Попробуйте конвертировать HTML в PDF онлайн**

Aspose предлагает вам бесплатное онлайн‑приложение ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), где вы можете проверить его функциональность и качество работы.

[![Конвертация Aspose.PDF HTML в PDF с помощью бесплатного приложения](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## Конвертация HTML в PDF с использованием media type

Этот пример показывает, как конвертировать HTML‑файл в PDF с помощью Aspose.PDF for Python via .NET, используя конкретные параметры рендеринга.

1. Создайте экземпляр класса [HtmlLoadOptions()](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/). Свойство 'html_media_type' применяет CSS‑правила, предназначенные для отображения на экране. Свойство 'html_media_type' может принимать несколько значений. Вы можете установить его в HtmlMediaType.SCREEN или HtmlMediaType.PRINT.
1. Загрузите HTML в ap.Document, используя параметры загрузки.
1. Сохраните документ в формате PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.html_media_type = ap.HtmlMediaType.SCREEN
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Конвертация HTML в PDF с приоритетным правилом CSS @page

Некоторые документы могут содержать настройки макета, использующие [правило Page](https://developer.mozilla.org/en-US/docs/Web/CSS/@page), что может создавать неоднозначность при генерации макета. Вы можете управлять приоритетом с помощью свойства 'is_priority_css_page_rule'. Если это свойство установлено в 'True', правило CSS применяется первым.

1. Создайте экземпляр класса [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/).
1. Установите 'is_priority_css_page_rule = False', чтобы отключить приоритетность правил CSS @page, позволяя другим стилям иметь приоритет.
1. Загрузите HTML в ap.Document с настроенными параметрами.
1. Сохраните документ в формате PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    # load_options.is_priority_css_page_rule = False
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Конвертация HTML в PDF с внедрёнными шрифтами

Этот пример показывает, как конвертировать HTML‑файл в PDF с внедрением шрифтов. Если вам нужен PDF‑документ со встроенными шрифтами, следует установить 'is_embed_fonts' в True.

1. Создайте 'HtmlLoadOptions()' для настройки конвертации HTML в PDF.
1. Установите 'is_embed_fonts = True', чтобы гарантировать, что все шрифты, использованные в HTML, будут встроены непосредственно в PDF, сохраняя визуальную точность.
1. Загрузите HTML в ap.Document с этими параметрами.
1. Сохраните документ в формате PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.is_embed_fonts = True
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Отображение содержимого на одной странице при конвертации HTML в PDF

Этот пример демонстрирует, как конвертировать HTML‑файл в одностраничный PDF с использованием Aspose.PDF for Python.
Вы можете отобразить всё содержимое на одной странице, используя свойство 'is_render_to_single_page'.

1. Создайте экземпляр 'HtmlLoadOptions()' для настройки процесса конвертации.
1. Включите 'is_render_to_single_page', чтобы отрендерить весь HTML‑контент на одной непрерывной странице PDF.
1. Загрузите документ с настроенными параметрами в 'ap.Document'.
1. Сохраните результат в виде PDF‑файла.

```python
    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    options = ap.HtmlLoadOptions()
    options.is_render_to_single_page = True

    doc = ap.Document(path_infile, options)
    doc.save(path_outfile)
```

## Конвертация MHTML в PDF

Этот пример показывает, как преобразовать файл MHT (MHTML) в документ PDF с использованием Aspose.PDF for Python с заданными размерами страниц.

1. Создайте экземпляр ap.MhtLoadOptions() для настройки обработки файла MHT.
1. Установите различные параметры, такие как размер страницы.
1. Инициализируйте документ с входным файлом и настроенными параметрами загрузки.
1. Сохраните полученный документ в формате PDF.

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    load_options = ap.MhtLoadOptions()
    load_options.page_info.width = 842
    load_options.page_info.height= 1191
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```
