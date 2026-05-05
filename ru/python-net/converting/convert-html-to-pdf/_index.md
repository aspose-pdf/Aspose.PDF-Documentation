---
title: Конвертировать HTML в PDF в Python
linktitle: Конвертировать HTML в PDF файл
type: docs
weight: 40
url: /ru/python-net/convert-html-to-pdf/
lastmod: "2026-04-14"
description: Узнайте, как конвертировать HTML и MHTML в PDF в Python с помощью Aspose.PDF for Python via .NET, включая настройки медиа CSS, встроенные шрифты и вывод Tagged PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true 
AlternativeHeadline: Как конвертировать HTML в PDF в Python с помощью Aspose.PDF
Abstract: В этой статье объясняется, как конвертировать файлы HTML и MHTML в PDF с использованием Aspose.PDF for Python via .NET. Описывается базовый рабочий процесс преобразования HTML в PDF и показано, как управлять рендерингом с помощью типов носителей, приоритета правил CSS page, встроенных шрифтов, вывода в виде одной страницы и генерации логической структуры для доступных помеченных PDF.
---

## Преобразование HTML в PDF с помощью Python

**Aspose.PDF for Python via .NET** позволяет конвертировать существующие HTML‑документы в PDF с гибкими параметрами рендеринга. Вы можете тонко настроить процесс генерации вывода, чтобы он соответствовал требованиям к макету, стилям, доступности и архивированию.

## Преобразовать HTML в PDF

Следующий пример на Python демонстрирует базовый процесс конвертации HTML‑документа в PDF.

1. Создайте экземпляр [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) класс.
1. Инициализировать a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) объект с исходным HTML‑файлом.
1. Сохраните выходной PDF документ, вызвав `document.save()`.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.page_layout_option = ap.HtmlPageLayoutOption.SCALE_TO_PAGE_WIDTH
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Связанные преобразования

- [Преобразовать PDF в HTML](/pdf/ru/python-net/convert-pdf-to-html/) когда вам нужен веб‑готовый вывод из существующих PDF‑файлов.
- [Конвертировать другие форматы файлов в PDF](/pdf/ru/python-net/convert-other-files-to-pdf/) для рабочих процессов конвертации EPUB, XPS, текста и PostScript.
- [Конвертировать изображения в PDF](/pdf/ru/python-net/convert-images-format-to-pdf/) когда ваш исходный контент основан на изображениях, а не на HTML-разметке.

{{% alert color="success" %}}
**Попробуйте конвертировать HTML в PDF онлайн**

Aspose представляет бесплатное онлайн‑приложение [HTML в PDF](https://products.aspose.app/html/en/conversion/html-to-pdf), где вы можете проверить качество преобразования и вывод.

[![Aspose.PDF Конвертация HTML в PDF с помощью бесплатного приложения](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## Конвертировать HTML в PDF, используя тип медиа

В этом примере показано, как преобразовать HTML‑файл в PDF, используя определённые параметры рендеринга.

1. Создайте экземпляр [HtmlLoadOptions()](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) класс.
1. Установить `html_media_type` для применения CSS-правил, предназначенных для экранных или печатных макетов, таких как `HtmlMediaType.SCREEN` или `HtmlMediaType.PRINT`.
1. Загрузите HTML в `ap.Document` используя параметры загрузки.
1. Сохраните документ в формате PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.html_media_type = ap.HtmlMediaType.SCREEN
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Отдавайте приоритет CSS `@page` правило во время конвертации HTML в PDF

Некоторые документы используют [the `@page` rule](https://developer.mozilla.org/en-US/docs/Web/CSS/@page) для макета страниц. Если эти стили конфликтуют с другими настройками, вы можете управлять приоритетом с помощью `is_priority_css_page_rule`.

1. Создайте экземпляр [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) класс.
1. Установить `is_priority_css_page_rule = False` чтобы другие стили имели приоритет над `@page` правила.
1. Загрузите HTML в `ap.Document` с настроенными параметрами.
1. Сохраните документ в формате PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
# load_options.is_priority_css_page_rule = False
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Конвертировать HTML в PDF с внедрёнными шрифтами

Этот пример показывает, как преобразовать HTML‑файл в PDF с внедрением шрифтов. Если вам нужно, чтобы полученный PDF сохранял оригинальную типографику, установите `is_embed_fonts` в `True`.

1. Создать `HtmlLoadOptions()` для настройки конвертации HTML в PDF.
1. Установить `is_embed_fonts = True` встроить шрифты, используемые в HTML, непосредственно в PDF.
1. Загрузите HTML в `ap.Document` с этими параметрами.
1. Сохраните документ в формате PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.is_embed_fonts = True
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Отобразить HTML‑контент на одной странице PDF

Этот пример демонстрирует, как преобразовать HTML‑файл в одностраничный PDF с помощью Aspose.PDF for Python via .NET. Используйте `is_render_to_single_page` свойство, когда вы хотите, чтобы весь HTML‑контент был отрендерен на одной непрерывной странице.

1. Создать экземпляр `HtmlLoadOptions()` для настройки процесса конвертации.
1. Включить `is_render_to_single_page` отобразить весь HTML‑контент на одной странице.
1. Загрузите документ с настроенными параметрами в `ap.Document`.
1. Сохраните результат в виде PDF‑файла.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

options = ap.HtmlLoadOptions()
options.is_render_to_single_page = True

doc = ap.Document(path_infile, options)
doc.save(path_outfile)
```

## Создать логическую структуру из тегов HTML

Логическая структура, также называемая тегированным PDF, сохраняет семантическую иерархию исходного HTML, такую как заголовки, абзацы и списки. Это делает полученный PDF более доступным, удобным для поиска и подходящим для рабочих процессов со структурированными документами.

Включив логическую структуру при конвертации, HTML‑DOM отображается в дерево тегов PDF, а не только как визуальный контент.

Чтобы соответствовать требованиям доступности, PDF должен включать логические элементы структуры, определяющие порядок чтения, предоставлять альтернативный текст для экранных считывателей и сохранять иерархию содержимого.

> Качество логической структуры в создаваемом PDF напрямую зависит от качества исходной разметки HTML. Плохо структурированный или некорректный HTML может привести к неполному или неточному тегированию в конвертированном PDF.

1. Создайте экземпляр HtmlLoadOptions, чтобы контролировать, как происходит преобразование HTML.
1. Активировать семантическую разметку, чтобы PDF содержал структурированные элементы.
1. Откройте HTML‑файл, используя настроенные параметры.
1. Сохранить структурированный PDF.

```python
import aspose.pdf as ap

# Path to the source HTML
input_html_path = "input.html"
# Path for the Logical Structure PDF
output_pdf_path = "output_logical_structure.pdf"
# Initialize HtmlLoadOptions
options = ap.HtmlLoadOptions()
# Convert HTML markup to PDF logical structure elements
options.create_logical_structure = True
# Open PDF document
with ap.Document(input_html_path, options) as document:
    # Save PDF document
    document.save(output_pdf_path)
```

## Конвертировать MHTML в PDF

В этом примере показано, как преобразовать файл MHT или MHTML в PDF‑документ с использованием Aspose.PDF for Python via .NET с указанием конкретных размеров страницы.

1. Создать экземпляр `ap.MhtLoadOptions()` для настройки обработки файлов MHTML.
1. Установите различные параметры, такие как размер страницы.
1. Инициализируйте документ с входным файлом и настроенными параметрами загрузки.
1. Сохраните полученный документ в формате PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
load_options = ap.MhtLoadOptions()
load_options.page_info.width = 842
load_options.page_info.height = 1191
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```
