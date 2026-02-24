---
title: Преобразовать PDF в HTML с помощью Python
linktitle: Преобразовать PDF в формат HTML
type: docs
weight: 50
url: /ru/python-net/convert-pdf-to-html/
lastmod: "2025-09-27"
description: Эта тема покажет вам, как преобразовать PDF‑файл в формат HTML с помощью библиотеки Aspose.PDF для Python через .NET.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Как преобразовать PDF в HTML с помощью Python
Abstract: Эта статья предоставляет комплексное руководство по преобразованию PDF‑файлов в HTML с использованием Python, конкретно через библиотеку Aspose.PDF для Python через .NET. В ней изложены необходимые шаги для выполнения этой конверсии программно, с акцентом на создание объекта `Document` из исходного PDF и использование `HtmlSaveOptions` для сохранения документа в формате HTML. Статья включает лаконичный фрагмент кода на Python, демонстрирующий процесс конверсии. Кроме того, представляется онлайн‑инструмент, приложение Aspose.PDF "PDF to HTML", позволяющее пользователям изучить функциональность и качество преобразования. Статья структурирована так, чтобы охватить различные связанные темы, обеспечивая полное понимание использования Python для конвертации PDF в HTML.
---

## Преобразовать PDF в HTML

**Aspose.PDF for Python via .NET** предоставляет множество функций для преобразования различных форматов файлов в PDF‑документы и конвертации PDF‑файлов в различные форматы вывода. Эта статья обсуждает, как преобразовать PDF‑файл в <abbr title="HyperText Markup Language">HTML</abbr>. Вы можете использовать всего несколько строк кода на Python для конвертации PDF в HTML. Возможно, вам понадобится преобразовать PDF в HTML, если вы хотите создать веб‑сайт или добавить контент на онлайн‑форум. Один из способов преобразования PDF в HTML — программно использовать Python.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в HTML онлайн**

Aspose.PDF for Python представляет вам бесплатное онлайн‑приложение ["PDF в HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), где вы можете попробовать исследовать его функциональность и качество работы.

[![Aspose.PDF Конвертация PDF в HTML с бесплатным приложением](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Шаги: преобразование PDF в HTML на Python

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с исходным PDF‑документом.
1. Сохраните его в [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/), вызвав метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

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

### Преобразовать PDF в HTML с сохранением изображений в указанную папку

Эта функция преобразует PDF‑файл в формат HTML с использованием Aspose.PDF для Python через .NET. Все извлечённые изображения сохраняются в указанной папке, а не встраиваются в HTML‑файл.

1. Настройте параметры сохранения HTML.
1. Сохраните как HTML с внешними изображениями.

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

Эта функция преобразует PDF‑файл в многостраничный HTML, при этом каждая страница PDF экспортируется в отдельный HTML‑файл. Это упрощает навигацию по результату и уменьшает время загрузки больших PDF‑файлов.

1. Загрузите исходный PDF, используя 'ap.Document'.
1. Создайте 'HtmlSaveOptions' и задайте 'split_into_pages'.
1. Сохраните документ как HTML с разделением страниц на отдельные файлы.
1. Выведите подтверждающее сообщение.

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

### Преобразовать PDF в HTML с сохранением SVG‑изображений в указанную папку

Эта функция преобразует PDF в формат HTML, сохраняя все изображения как SVG‑файлы в указанной папке, вместо их непосредственного внедрения в HTML.

1. Загрузите исходный PDF, используя 'ap.Document'.
1. Создайте 'HtmlSaveOptions' и задайте 'special_folder_for_svg_images' в целевую папку.
1. Сохраните документ как HTML с внешними SVG‑изображениями.
1. Выведите подтверждающее сообщение.

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

Этот фрагмент кода преобразует PDF в формат HTML, сохраняя все изображения как SVG‑файлы в указанной папке и сжимая их для уменьшения размера файла.

1. Загрузите PDF‑документ, используя 'ap.Document'.
1. Создайте 'HtmlSaveOptions' и:
- Установите 'special_folder_for_svg_images' для внешнего хранения SVG‑изображений.
- Включите 'compress_svg_graphics_if_any' для сжатия SVG‑изображений.
1. Сохраните документ как HTML с сжатыми внешними SVG‑изображениями.
1. Выведите подтверждающее сообщение.

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

Этот фрагмент кода преобразует PDF в формат HTML, встраивая растровые изображения как PNG‑фоновые изображения страниц. Этот подход сохраняет качество изображений и макет страниц в HTML.

1. Загрузите PDF‑документ, используя 'ap.Document'.
1. Создайте 'HtmlSaveOptions' и установите 'raster_images_saving_mode' в 'AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND'.
1. Сохраните документ в формате HTML с встроенными растровыми изображениями.
1. Выведите подтверждающее сообщение.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.raster_images_saving_mode = apdf.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Преобразовать PDF в HTML‑страницу только с содержимым тела

Эта функция преобразует PDF в формат HTML, создавая контент только с тегом 'body' без лишних тегов 'html' или 'head', и разбивает результат на отдельные страницы.

1. Загрузите PDF‑документ с помощью 'ap.Document'.
1. Создайте 'HtmlSaveOptions' и настройте:
- 'html_markup_generation_mode = WRITE_ONLY_BODY_CONTENT' для генерации только содержимого 'body'.
- 'split_into_pages' для создания отдельных HTML‑файлов для каждой страницы PDF.
1. Сохраните документ в формате HTML с указанными параметрами.
1. Выведите подтверждающее сообщение.

```python

from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.html_markup_generation_mode = apdf.HtmlSaveOptions.HtmlMarkupGenerationModes.WRITE_ONLY_BODY_CONTENT
    save_options.split_into_pages = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Преобразовать PDF в HTML с прозрачным отображением текста

Эта функция преобразует PDF в формат HTML, отображая весь текст как прозрачный, включая текст с тенью, что сохраняет визуальную точность и позволяет гибко стилизовать полученный HTML.

1. Загрузите PDF‑документ с помощью 'ap.Document'.
1. Создайте 'HtmlSaveOptions' и настройте:
- 'save_transparent_texts' для отображения обычного текста как прозрачного.
- 'save_shadowed_texts_as_transparent_texts' для отображения текста с тенью как прозрачного.
1. Сохраните документ в формате HTML с прозрачным отображением текста.
1. Выведите подтверждающее сообщение.

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

### Преобразовать PDF в HTML с отображением слоёв документа

Эта функция преобразует PDF в формат HTML, сохраняя слои документа, преобразуя отмеченный контент в отдельные слои в результирующем HTML. Это позволяет точно отображать слоистые элементы (например, аннотации, фон и наложения).

1. Загрузите PDF‑документ с помощью 'ap.Document'.
1. Создайте 'HtmlSaveOptions' и включите 'convert_marked_content_to_layers' для сохранения слоёв.
1. Сохраните документ в формате HTML с многослойным содержимым.
1. Выведите подтверждающее сообщение.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    document = apdf.Document(path_infile)
    save_options = apdf.HtmlSaveOptions()
    save_options.convert_marked_content_to_layers  = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```


