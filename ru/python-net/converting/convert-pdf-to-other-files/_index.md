---
title: Конвертировать PDF в EPUB, LaTeX, Текст, XPS с помощью Python
linktitle: Конвертировать PDF в другие форматы
type: docs
weight: 90
url: /ru/python-net/convert-pdf-to-other-files/
lastmod: "2025-09-27"
description: Эта тема показывает, как конвертировать PDF‑файл в другие форматы, такие как EPUB, LaTeX, Текст, XPS и др., используя Python.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Как конвертировать PDF в другие форматы с помощью Python
Abstract: Статья предоставляет полноценное руководство по конвертации PDF‑файлов в различные форматы с использованием Aspose.PDF для Python. В ней рассматривается преобразование PDF в форматы EPUB, LaTeX/TeX, Текст, XPS и XML. Каждый раздел начинается с приглашения попробовать онлайн‑бесплатные приложения, предоставленные Aspose, для конвертации PDF в соответствующие форматы, подчеркивая простоту использования и качество этих инструментов.
---

## Конвертировать PDF в EPUB

{{% alert color="success" %}}
**Попробовать конвертировать PDF в EPUB онлайн**

Aspose.PDF for Python представляет вам онлайн‑бесплатное приложение ["PDF в EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), где вы можете проверить функциональность и качество работы.

[![Конвертация Aspose.PDF PDF в EPUB с бесплатным приложением](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> — бесплатный и открытый стандарт электронных книг от Международного форума цифровой публикации (IDPF). Файлы имеют расширение .epub.
EPUB разработан для контента с динамичной версткой, что означает, что ридер EPUB может оптимизировать текст под конкретное устройство отображения. EPUB также поддерживает фиксированную раскладку. Формат предназначен как единый стандарт, который издатели и конверсионные компании могут использовать внутри организации, а также для распространения и продажи. Он заменил стандарт Open eBook.

Aspose.PDF for Python также поддерживает возможность конвертации PDF‑документов в формат EPUB. Aspose.PDF for Python имеет класс с именем 'EpubSaveOptions', который можно использовать в качестве второго аргумента метода [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) для создания файла EPUB.
Пожалуйста, попробуйте использовать следующий фрагмент кода, чтобы выполнить эту задачу с помощью Python.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.EpubSaveOptions()
    save_options.content_recognition_mode = (
        ap.EpubSaveOptions.RecognitionMode.FLOW
    )
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Конвертировать PDF в LaTeX/TeX

**Aspose.PDF for Python via .NET** поддерживает конвертацию PDF в LaTeX/TeX.
Формат файлов LaTeX — это текстовый формат с специальной разметкой, используемый в системе подготовки документов на основе TeX для высококачественной верстки.

{{% alert color="success" %}}
**Попробовать конвертировать PDF в LaTeX/TeX онлайн**

Aspose.PDF for Python представляет вам онлайн‑бесплатное приложение ["PDF в LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), где вы можете проверить функциональность и качество работы.

[![Конвертация Aspose.PDF PDF в LaTeX/TeX с бесплатным приложением](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Для конвертации PDF‑файлов в TeX Aspose.PDF использует класс [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/), который предоставляет свойство OutDirectoryPath для сохранения временных изображений в процессе конвертации.

Следующий фрагмент кода показывает процесс конвертации PDF‑файлов в формат TEX с помощью Python.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.LaTeXSaveOptions()

    document.save(path_outfile, save_options)
    print(infile + " converted into " + outfile)
```

## Конвертировать PDF в Текст

**Aspose.PDF for Python** поддерживает конвертацию всего PDF‑документа и отдельной страницы в файл Текст. Вы можете конвертировать PDF‑документ в TXT‑файл, используя класс 'TextDevice'. Следующий фрагмент кода объясняет, как извлечь тексты со всех страниц.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    device = ap.devices.TextDevice()
    device.process(document.pages[1], path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Попробовать конвертировать PDF в Текст онлайн**

Aspose.PDF for Python представляет вам онлайн‑бесплатное приложение ["PDF в Текст"](https://products.aspose.app/pdf/conversion/pdf-to-txt), где вы можете проверить функциональность и качество работы.

[![Конвертация Aspose.PDF PDF в Текст с бесплатным приложением](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Конвертировать PDF в XPS

**Aspose.PDF for Python** дает возможность конвертировать PDF‑файлы в формат XPS. Попробуйте использовать представленный фрагмент кода для конвертации PDF‑файлов в формат XPS с помощью Python.

{{% alert color="success" %}}
**Попробовать конвертировать PDF в XPS онлайн**

Aspose.PDF for Python представляет вам онлайн‑бесплатное приложение ["PDF в XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), где вы можете проверить функциональность и качество работы.

[![Конвертация Aspose.PDF PDF в XPS с бесплатным приложением](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

Тип файла XPS в основном связан со спецификацией XML Paper Specification от Microsoft Corporation. Спецификация XML Paper Specification (XPS), ранее codenamed Metro и включающая концепцию Next Generation Print Path (NGPP), является инициативой Microsoft по интеграции создания и просмотра документов в операционную систему Windows.

Для конвертации PDF‑файлов в XPS Aspose.PDF использует класс [XpsSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/), который применяется в качестве второго аргумента метода [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) для создания файла XPS.

Следующий фрагмент кода показывает процесс конвертации PDF‑файла в формат XPS.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.XpsSaveOptions()
    save_options.use_new_imaging_engine = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Преобразовать PDF в MD

Aspose.PDF имеет класс 'MarkdownSaveOptions()', который преобразует PDF‑документ в формат Markdown (MD), сохраняя изображения и ресурсы.

1. Загрузите исходный PDF, используя 'ap.Document'.
1. Создайте экземпляр 'MarkdownSaveOptions'.
1. Установите 'resources_directory_name' в 'images' — извлечённые изображения будут сохранены в этой папке.
1. Сохраните преобразованный Markdown‑документ, используя настроенные параметры.
1. Выведите подтверждающее сообщение после конвертации.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.MarkdownSaveOptions()
    # save_options.extract_vector_graphics = True
    save_options.resources_directory_name = "images"
    save_options.use_image_html_tag = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

Файл Markdown с текстом и связанными изображениями, сохранёнными в указанной папке images.

## Преобразовать PDF в MobiXML

Этот метод преобразует PDF‑документ в формат MOBI (MobiXML), который обычно используется для электронных книг на устройствах Kindle.

1. Загрузите исходный PDF‑документ, используя 'ap.Document'.
1. Сохраните документ в формате 'ap.SaveFormat.MOBI_XML'.
1. Выведите подтверждающее сообщение после завершения конвертации.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.save(path_outfile, ap.SaveFormat.MOBI_XML)

    print(infile + " converted into " + outfile)
```
