---
title: Конвертировать PDF в HTML на Python
linktitle: Конвертировать PDF в формат HTML
type: docs
weight: 50
url: /python-net/convert-pdf-to-html/
lastmod: "2026-04-14"
description: Узнайте, как конвертировать PDF в HTML на Python с помощью Aspose.PDF for Python via .NET, включая многостраничный вывод, внешние изображения, обработку SVG и слоистый рендеринг HTML.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Как конвертировать PDF в HTML на Python
Abstract: Эта статья представляет собой всестороннее руководство по конвертации PDF‑файлов в HTML с использованием Python, конкретно через библиотеку Aspose.PDF for Python via .NET. В ней описаны необходимые шаги для выполнения этой конверсии программно, с акцентом на создание объекта `Document` из исходного PDF и использование `HtmlSaveOptions` для сохранения документа в формате HTML. Статья включает краткий фрагмент кода на Python, демонстрирующий процесс конвертации. Кроме того, она представляет онлайн‑инструмент, приложение Aspose.PDF’s "PDF to HTML", позволяющее пользователям изучить функции и качество конверсии. Статья структурирована так, чтобы охватить различные связанные темы, обеспечивая полное понимание использования Python для конвертации PDF в HTML.
---

## Преобразовать PDF в HTML

**Aspose.PDF for Python via .NET** предоставляет множество функций для преобразования различных форматов файлов в PDF‑документы и преобразования PDF‑файлов в различные форматы вывода. Эта статья рассматривает, как конвертировать PDF‑файл в <abbr title="HyperText Markup Language">HTML</abbr>. Вы можете использовать всего несколько строк кода Python для преобразования PDF в HTML. Возможно, вам потребуется конвертировать PDF в HTML, если вы хотите создать веб‑сайт или добавить контент на онлайн‑форум. Один из способов преобразовать PDF в HTML — программно использовать Python.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в HTML онлайн**

Aspose.PDF for Python представляет вам онлайн‑приложение ["PDF в HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), где вы можете попытаться исследовать функциональность и качество, с которым он работает.

[![Aspose.PDF Конвертация PDF в HTML с приложением](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Шаги: Преобразовать PDF в HTML на Python

1. Создать экземпляр [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) объект с исходным PDF документом.
1. Сохранить в [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/) вызовом [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Связанные преобразования

- [Конвертировать HTML в PDF](/pdf/ru/python-net/convert-html-to-pdf/) когда вам нужен обратный рабочий процесс web-to-document.
- [Конвертировать PDF в Word](/pdf/ru/python-net/convert-pdf-to-word/) если вывод редактируемого документа полезнее, чем HTML.
- [Конвертировать PDF в форматы изображений](/pdf/ru/python-net/convert-pdf-to-images-format/) для сценариев экспорта растра.

### Конвертировать PDF в HTML с сохранением изображений в указанную папку

Эта функция преобразует PDF‑файл в формат HTML с использованием Aspose.PDF for Python via .NET. Все извлечённые изображения сохраняются в указанной папке вместо встраивания их в HTML‑файл.

1. Настройте параметры сохранения HTML.
1. Сохранить как HTML с внешними изображениями.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_storing_images(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "images")
    save_options.special_folder_for_all_images = images_path
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Преобразовать PDF в многостраничный HTML

Эта функция конвертирует файл PDF в многостраничный HTML, где каждая страница PDF экспортируется в отдельный HTML‑файл. Это делает вывод более удобным для навигации и уменьшает время загрузки больших PDF‑файлов.

1. Загрузите исходный PDF, используя 'ap.Document'.
1. Создайте 'HtmlSaveOptions' и установите `split_into_pages`.
1. Сохраните документ как HTML с разбивкой страниц на отдельные файлы.
1. Вывести подтверждающее сообщение.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_multi_page(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.split_into_pages = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Преобразовать PDF в HTML с сохранением SVG‑изображений в указанную папку

Эта функция преобразует PDF в формат HTML, при этом сохраняет все изображения как файлы SVG в указанной папке, вместо того чтобы внедрять их непосредственно в HTML.

1. Загрузите исходный PDF, используя 'ap.Document'.
1. Создайте 'HtmlSaveOptions' и установите `special_folder_for_svg_images` в целевую папку.
1. Сохраните документ как HTML с внешними SVG‑изображениями.
1. Вывести подтверждающее сообщение.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_storing_svg(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "svg_images")
    save_options.special_folder_for_svg_images = images_path
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Преобразование PDF в HTML и сохранение сжатых SVG‑изображений

Этот фрагмент кода преобразует PDF в формат HTML, сохраняет все изображения в виде SVG‑файлов в указанную папку и сжимает их для уменьшения размера файла.

1. Загрузите PDF-документ, используя 'ap.Document'.
1. Создайте 'HtmlSaveOptions' и:
   - Установите 'special_folder_for_svg_images' для внешнего хранения SVG‑изображений.
   - Включите \u0027compress_svg_graphics_if_any\u0027 для сжатия SVG‑изображений.
1. Сохраните документ как HTML с сжатыми внешними SVG‑изображениями.
1. Вывести подтверждающее сообщение.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_compress_svg(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "svg_images")
    save_options.special_folder_for_svg_images = images_path
    save_options.compress_svg_graphics_if_any = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Преобразовать PDF в HTML с управлением встроенными растровыми изображениями

Этот фрагмент кода преобразует PDF в формат HTML, встраивая растровые изображения в качестве фоновых PNG‑изображений страниц. Этот подход сохраняет качество изображений и макет страниц в HTML.

1. Загрузите PDF-документ, используя 'ap.Document'.
1. Создайте 'HtmlSaveOptions' и установите 'raster_images_saving_mode' в значение 'AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND'.
1. Сохранить документ в формате HTML с внедрёнными растровыми изображениями.
1. Вывести подтверждающее сообщение.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_PNG_background(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.raster_images_saving_mode = ap.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Преобразовать PDF в HTML‑страницу только с содержимым тела

Эта функция преобразует PDF в формат HTML, генерируя контент 'body-only' без дополнительных тегов 'html' или 'head', и разбивает вывод на отдельные страницы.

1. Загрузите PDF-документ, используя 'ap.Document'.
1. Создайте 'HtmlSaveOptions' и настройте:
   - 'html_markup_generation_mode = WRITE_ONLY_BODY_CONTENT' для генерации только содержания 'body'.
   - 'split_into_pages' для создания отдельных HTML‑файлов для каждой страницы PDF.
1. Сохраните документ в формате HTML с указанными параметрами.
1. Вывести подтверждающее сообщение.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_body_content(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.html_markup_generation_mode = (
        ap.HtmlSaveOptions.HtmlMarkupGenerationModes.WRITE_ONLY_BODY_CONTENT
    )
    save_options.split_into_pages = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Конвертировать PDF в HTML с прозрачным отображением текста

Эта функция преобразует PDF в формат HTML, отображая весь текст как прозрачный, включая тексты с тенями, что сохраняет визуальную достоверность, позволяя при этом гибко стилизовать полученный HTML.

1. Загрузите PDF-документ, используя 'ap.Document'.
1. Создайте 'HtmlSaveOptions' и настройте:
    - 'save_transparent_texts' для отображения обычного текста как прозрачного.
    - 'save_shadowed_texts_as_transparent_texts' для отображения теневого текста как прозрачного.
1. Сохраните документ в формате HTML с прозрачным отображением текста.
1. Вывести подтверждающее сообщение.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_transparent_text_rendering(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.save_transparent_texts = True
    save_options.save_shadowed_texts_as_transparent_texts = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Преобразовать PDF в HTML с рендерингом слоёв документа

Эта функция конвертирует PDF в формат HTML, сохраняет слои документа, преобразуя отмеченное содержимое в отдельные слои в результирующем HTML. Это позволяет точно отображать слоистые элементы (например, аннотации, фоновые изображения и наложения).

1. Загрузите PDF-документ, используя 'ap.Document'.
1. Создайте 'HtmlSaveOptions' и включите 'convert_marked_content_to_layers', чтобы сохранить слои.
1. Сохраните документ как HTML с многослойным содержимым.
1. Вывести подтверждающее сообщение.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_document_layers_rendering(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.convert_marked_content_to_layers = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

