---
title: Конвертировать HTML в PDF с помощью Python
linktitle: Конвертировать HTML в PDF‑файл
type: docs
weight: 40
url: /python-net/convert-html-to-pdf/
lastmod: "2026-04-14"
description: Узнайте, как преобразовать HTML и MHTML в PDF на Python с помощью Aspose.PDF for Python via .NET, включая настройки CSS media, встроенные шрифты и вывод Tagged PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true 
AlternativeHeadline: Как преобразовать HTML в PDF на Python с помощью Aspose.PDF
Abstract: Эта статья объясняет, как преобразовать файлы HTML и MHTML в PDF с использованием Aspose.PDF for Python via .NET. Она охватывает базовый процесс преобразования HTML в PDF и показывает, как управлять рендерингом с помощью медиа‑типов, приоритета правил CSS page, встроенных шрифтов, вывода в один лист и генерации логической структуры для доступных помеченных PDF.
---

## Конвертация HTML в PDF с помощью Python

**Aspose.PDF for Python via .NET** позволяет конвертировать существующие HTML‑документы в PDF с гибкими параметрами рендеринга. Вы можете точно настроить процесс создания вывода, чтобы он соответствовал вашим требованиям к макету, стилизации, доступности и архивированию.

## Преобразовать HTML в PDF

Следующий пример на Python показывает основной рабочий процесс преобразования HTML‑документа в PDF.

1. Создать экземпляр [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) класс.
1. Инициализировать [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) объект с исходным HTML-файлом.
1. Сохраните выходной PDF‑документ, вызвав `document.save()`.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_HTML_to_PDF(infile, outfile):
    load_options = ap.HtmlLoadOptions()
    load_options.page_layout_option = ap.HtmlPageLayoutOption.SCALE_TO_PAGE_WIDTH
    document = ap.Document(infile, load_options)
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Связанные преобразования

- [Преобразовать PDF в HTML](/pdf/ru/python-net/convert-pdf-to-html/) когда вам нужен веб‑готовый вывод из существующих PDF‑файлов.
- [Преобразовать другие форматы файлов в PDF](/pdf/ru/python-net/convert-other-files-to-pdf/) для рабочих процессов конвертации EPUB, XPS, текста и PostScript.
- [Преобразовать изображения в PDF](/pdf/ru/python-net/convert-images-format-to-pdf/) когда ваш исходный контент основан на изображениях, а не на HTML-разметке.

{{% alert color="success" %}}
**Попробуйте конвертировать HTML в PDF онлайн**

Aspose представляет онлайн‑приложение [HTML в PDF](https://products.aspose.app/html/en/conversion/html-to-pdf), где вы можете проверить качество конверсии и вывод.

[![Aspose.PDF Конвертация HTML в PDF с помощью приложения](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## Конвертировать HTML в PDF, используя тип медиа

Этот пример показывает, как преобразовать HTML‑файл в PDF с использованием конкретных параметров рендеринга.

1. Создать экземпляр [HtmlLoadOptions()](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) класс.
1. Установить `html_media_type` для применения правил CSS, предназначенных для экранных или печатных макетов, например `HtmlMediaType.SCREEN` или `HtmlMediaType.PRINT`.
1. Загрузите HTML в `ap.Document` используя параметры загрузки.
1. Сохраните документ в формате PDF.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_HTML_to_PDF_media_type(infile, outfile):
    load_options = ap.HtmlLoadOptions()
    load_options.html_media_type = ap.HtmlMediaType.SCREEN
    document = ap.Document(infile, load_options)
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Отдать приоритет CSS `@page` правило при преобразовании HTML в PDF

Некоторые документы используют [{"translatedText":""} `@page` правило](https://developer.mozilla.org/en-US/docs/Web/CSS/@page) для макета страницы. Если эти стили конфликтуют с другими настройками, вы можете управлять приоритетом с помощью `is_priority_css_page_rule`.

1. Создать экземпляр [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) класс.
1. Установить `is_priority_css_page_rule = False` чтобы позволить другим стилям иметь приоритет `@page` правила.
1. Загрузите HTML в `ap.Document` с настроенными параметрами.
1. Сохраните документ в формате PDF.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_HTML_to_PDF_priority_css_page_rule(infile, outfile):
    load_options = ap.HtmlLoadOptions()
    load_options.is_priority_css_page_rule = False
    document = ap.Document(infile, load_options)
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Конвертировать HTML в PDF с внедрёнными шрифтами

Этот пример показывает, как преобразовать HTML‑файл в PDF с внедрением шрифтов. Если вам требуется, чтобы итоговый PDF сохранял оригинальную типографику, установите `is_embed_fonts` к `True`.

1. Создать `HtmlLoadOptions()` для настройки преобразования HTML в PDF.
1. Установить `is_embed_fonts = True` встраивать шрифты, использованные в HTML, напрямую в PDF.
1. Загрузите HTML в `ap.Document` с этими параметрами.
1. Сохраните документ в формате PDF.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_HTML_to_PDF_embed_fonts(infile, outfile):
    load_options = ap.HtmlLoadOptions()
    load_options.is_embed_fonts = True
    document = ap.Document(infile, load_options)
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Отобразить HTML‑контент на одной странице PDF

Этот пример демонстрирует, как преобразовать HTML‑файл в одностраничный PDF с использованием Aspose.PDF for Python via .NET. Используйте `is_render_to_single_page` свойство, когда вы хотите, чтобы весь HTML‑контент отображался на одной непрерывной странице.

1. Создать экземпляр `HtmlLoadOptions()` для настройки процесса конвертации.
1. Включить `is_render_to_single_page` отобразить весь HTML‑контент на одной странице.
1. Загрузите документ с настроенными параметрами в `ap.Document`.
1. Сохраните результат как PDF‑файл.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_HTML_to_PDF_render_content_to_same_page(infile, outfile):
    options = ap.HtmlLoadOptions()
    options.is_render_to_single_page = True

    doc = ap.Document(infile, options)
    doc.save(outfile)
```

## Преобразовать MHTML в PDF

В этом примере показано, как преобразовать файл MHT или MHTML в PDF документ, используя Aspose.PDF for Python via .NET, с конкретными размерами страниц.

1. Создать экземпляр `ap.MhtLoadOptions()` для настройки обработки файлов MHTML.
1. Установите различные параметры, такие как размер страницы.
1. Инициализировать документ с входным файлом и настроенными параметрами загрузки.
1. Сохраните полученный документ в формате PDF.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_MHTML_to_PDF(infile, outfile):
    load_options = ap.MhtLoadOptions()
    load_options.page_info.width = 842
    load_options.page_info.height = 1191
    document = ap.Document(infile, load_options)
    document.save(outfile)
    print(infile + " converted into " + outfile)
```
