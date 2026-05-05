---
title: Конвертировать PDF в HTML на Python
linktitle: Конвертировать PDF в формат HTML
type: docs
weight: 50
url: /ru/python-net/convert-pdf-to-html/
lastmod: "2026-04-14"
description: Узнайте, как конвертировать PDF в HTML на Python с помощью Aspose.PDF for Python via .NET, включая многостраничный вывод, внешние изображения, обработку SVG и многослойную отрисовку HTML.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true 
AlternativeHeadline: Как конвертировать PDF в HTML на Python
Abstract: В этой статье представлено всестороннее руководство по преобразованию файлов PDF в HTML с использованием Python, в частности через библиотеку Aspose.PDF for Python via .NET. Описаны необходимые шаги для выполнения этого преобразования программно, с акцентом на создание объекта `Document` из исходного PDF и использование `HtmlSaveOptions` для сохранения документа в формате HTML. В статье включён лаконичный фрагмент кода на Python, демонстрирующий процесс преобразования. Кроме того, представлена онлайн‑утилита, приложение Aspose.PDF «PDF to HTML», позволяющая пользователям ознакомиться с функциями и качеством преобразования. Структура статьи охватывает различные сопутствующие темы, обеспечивая полное понимание использования Python для преобразования PDF в HTML.
---

## Конвертировать PDF в HTML

**Aspose.PDF for Python via .NET** предоставляет множество возможностей для преобразования различных форматов файлов в PDF‑документы и преобразования PDF‑файлов в различные форматы вывода. Эта статья рассматривает, как преобразовать PDF‑файл в <abbr title="HyperText Markup Language">HTML</abbr>. Вы можете использовать всего пару строк кода Python для преобразования PDF в HTML. Возможно, вам понадобится конвертировать PDF в HTML, если вы хотите создать веб-сайт или добавить контент на онлайн-форум. Один из способов конвертировать PDF в HTML — программно использовать Python.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в HTML онлайн**

Aspose.PDF for Python представляет вам онлайн бесплатное приложение [PDF в HTML](https://products.aspose.app/pdf/conversion/pdf-to-html), где вы можете попытаться исследовать его функциональность и качество.

[![Aspose.PDF Конвертация PDF в HTML с бесплатным приложением](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Шаги: Конвертировать PDF в HTML в Python

1. Создать экземпляр [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) объект с исходным PDF документом.
1. Сохранить в [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/) вызывая [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод.

```python
from os import path
import aspose.pdf as apdf

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
document = apdf.Document(path_infile)
save_options = apdf.HtmlSaveOptions()
document.save(path_outfile, save_options)

print(infile + " converted into " + outfile)
```

## Связанные преобразования

- [Конвертировать HTML в PDF](/pdf/ru/python-net/convert-html-to-pdf/) когда вам требуется обратный процесс веб‑в‑документ.
- [Конвертировать PDF в Word](/pdf/ru/python-net/convert-pdf-to-word/) если вывод редактируемого документа более полезен, чем HTML.
- [Конвертировать PDF в форматы изображений](/pdf/ru/python-net/convert-pdf-to-images-format/) для сценариев растрового экспорта.

### Конвертировать PDF в HTML с сохранением изображений в указанную папку

Эта функция преобразует файл PDF в формат HTML с использованием Aspose.PDF for Python via .NET. Все извлечённые изображения сохраняются в указанной папке вместо встраивания их в HTML‑файл.

1. Настройте параметры сохранения HTML.
1. Сохранить как HTML с внешними изображениями.

```python
from os import path
import aspose.pdf as apdf

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
document = apdf.Document(path_infile)
save_options = apdf.HtmlSaveOptions()
save_options.special_folder_for_all_images = self.data_dir
document.save(path_outfile, save_options)

print(infile + " converted into " + outfile)
```

### Преобразовать PDF в многостраничный HTML

Эта функция преобразует файл PDF в многостраничный HTML, где каждая страница PDF экспортируется в отдельный HTML‑файл. Это делает вывод проще для навигации и уменьшает время загрузки больших PDF‑файлов.

1. Загрузите исходный PDF, используя 'ap.Document'.
1. Создать 'HtmlSaveOptions' и 'set split_into_pages'.
1. Сохраните документ в формате HTML с разбивкой страниц на отдельные файлы.
1. Вывести сообщение подтверждения.

```python
from os import path
import aspose.pdf as apdf

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
document = apdf.Document(path_infile)
save_options = apdf.HtmlSaveOptions()
save_options.split_into_pages = True
document.save(path_outfile, save_options)

print(infile + " converted into " + outfile)
```

### Преобразовать PDF в HTML с сохранением SVG‑изображений в указанный каталог

Эта функция преобразует PDF в формат HTML, при этом сохраняет все изображения в виде SVG‑файлов в указанной папке, вместо того чтобы внедрять их напрямую в HTML.

1. Загрузите исходный PDF, используя 'ap.Document'.
1. Создайте 'HtmlSaveOptions' и установите 'special_folder_for_svg_images' в целевую папку.
1. Сохраните документ в формате HTML с внешними SVG‑изображениями.
1. Вывести сообщение подтверждения.

```python
from os import path
import aspose.pdf as apdf

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
document = apdf.Document(path_infile)
save_options = apdf.HtmlSaveOptions()
save_options.special_folder_for_svg_images = self.data_dir
document.save(path_outfile, save_options)

print(infile + " converted into " + outfile)
```

### Преобразовать PDF в HTML и сохранять сжатые SVG‑изображения

Этот фрагмент кода конвертирует PDF в формат HTML, сохраняет все изображения как SVG‑файлы в указанной папке и сжимает их, чтобы уменьшить размер файла.

1. Загрузите PDF-документ, используя 'ap.Document'.
1. Создайте 'HtmlSaveOptions' и:
   - Установите 'special_folder_for_svg_images', чтобы хранить SVG‑изображения внешне.
   - Включите 'compress_svg_graphics_if_any', чтобы сжать SVG изображения.
1. Сохраните документ в формате HTML с сжатыми внешними SVG‑изображениями.
1. Вывести сообщение подтверждения.

```python
from os import path
import aspose.pdf as apdf

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
document = apdf.Document(path_infile)
save_options = apdf.HtmlSaveOptions()
save_options.special_folder_for_svg_images = self.data_dir
save_options.compress_svg_graphics_if_any = True
document.save(path_outfile, save_options)

print(infile + " converted into " + outfile)
```

### Преобразовать PDF в HTML с контролем встроенных растровых изображений

Этот фрагмент кода преобразует PDF в формат HTML, встраивая растровые изображения в качестве фоновых PNG‑страниц. Такой подход сохраняет качество изображений и макет страниц в HTML.

1. Загрузите PDF-документ, используя 'ap.Document'.
1. Создайте 'HtmlSaveOptions' и 'set raster_images_saving_mode' в 'AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND'.
1. Сохраните документ в формате HTML с внедрёнными растровыми изображениями.
1. Вывести сообщение подтверждения.

```python
from os import path
import aspose.pdf as apdf

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
document = apdf.Document(path_infile)
save_options = apdf.HtmlSaveOptions()
save_options.raster_images_saving_mode = (
    apdf.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
)
document.save(path_outfile, save_options)

print(infile + " converted into " + outfile)
```

### Преобразовать PDF в HTML‑страницу, содержащую только тело

Эта функция преобразует PDF в формат HTML, генерируя только содержимое тела ('body-only') без дополнительных тегов 'html' или 'head', и разбивает вывод на отдельные страницы.

1. Загрузите PDF-документ, используя 'ap.Document'.
1. Создайте 'HtmlSaveOptions' и настройте:
   - 'html_markup_generation_mode = WRITE_ONLY_BODY_CONTENT' для генерации только содержимого 'body'.
   - 'split_into_pages' для создания отдельных HTML‑файлов для каждой страницы PDF.
1. Сохраните документ в формате HTML с указанными параметрами.
1. Вывести сообщение подтверждения.

```python
from os import path
import aspose.pdf as apdf

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
document = apdf.Document(path_infile)
save_options = apdf.HtmlSaveOptions()
save_options.html_markup_generation_mode = (
    apdf.HtmlSaveOptions.HtmlMarkupGenerationModes.WRITE_ONLY_BODY_CONTENT
)
save_options.split_into_pages = True
document.save(path_outfile, save_options)

print(infile + " converted into " + outfile)
```

### Преобразовать PDF в HTML с прозрачным отображением текста

Эта функция преобразует PDF в формат HTML, отображая весь текст как прозрачный, включая затенённый текст, что сохраняет визуальную достоверность при возможности гибкой стилизации в результирующем HTML.

1. Загрузите PDF-документ, используя 'ap.Document'.
1. Создайте 'HtmlSaveOptions' и настройте:
    - 'save_transparent_texts' для рендеринга обычного текста как прозрачного.
    - 'save_shadowed_texts_as_transparent_texts' для отображения затенённого текста как прозрачного.
1. Сохраните документ в формате HTML с прозрачным отображением текста.
1. Вывести сообщение подтверждения.

```python
from os import path
import aspose.pdf as apdf

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
document = apdf.Document(path_infile)
save_options = apdf.HtmlSaveOptions()
save_options.save_transparent_texts = True
save_options.save_shadowed_texts_as_transparent_texts = True
document.save(path_outfile, save_options)

print(infile + " converted into " + outfile)
```

### Конвертировать PDF в HTML с рендерингом слоёв Document

Эта функция преобразует PDF в формат HTML, сохраняя слои документа, преобразуя помеченный контент в отдельные слои в выводимом HTML. Это позволяет точно отобразить слоистые элементы (например, аннотации, фоновые изображения и наложения).

1. Загрузите PDF-документ, используя 'ap.Document'.
1. Создайте 'HtmlSaveOptions' и включите 'convert_marked_content_to_layers', чтобы сохранить слои.
1. Сохраните документ в формате HTML с многослойным содержимым.
1. Вывести сообщение подтверждения.

```python
from os import path
import aspose.pdf as apdf

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
document = apdf.Document(path_infile)
save_options = apdf.HtmlSaveOptions()
save_options.convert_marked_content_to_layers = True
document.save(path_outfile, save_options)

print(infile + " converted into " + outfile)
```

