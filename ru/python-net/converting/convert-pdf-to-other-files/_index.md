---
title: Конвертировать PDF в EPUB, Text, XPS и другие форматы в Python
linktitle: Конвертировать PDF в другие форматы
type: docs
weight: 90
url: /python-net/convert-pdf-to-other-files/
lastmod: "2026-04-14"
description: Узнайте, как конвертировать файлы PDF в EPUB, LaTeX, Markdown, текст, XPS и MobiXML на Python с помощью Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true 
AlternativeHeadline: Как конвертировать PDF в другие форматы в Python
Abstract: Статья предоставляет всестороннее руководство по конвертации PDF‑файлов в различные форматы с использованием Aspose.PDF for Python. Она охватывает преобразование PDF в форматы EPUB, LaTeX/TeX, Text, XPS и XML. Каждый раздел начинается с приглашения попробовать онлайн приложения, предоставляемые Aspose для конвертации PDF в соответствующие форматы, подчёркивая простоту использования и качество этих инструментов.
---

## Преобразовать PDF в EPUB

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в EPUB онлайн**

Aspose.PDF for Python представляет вам онлайн приложение ["PDF в EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), где вы можете попытаться исследовать функциональность и качество её работы.

[![Aspose.PDF Конвертация PDF в EPUB с приложением](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> является бесплатным и открытым стандартом электронных книг от International Digital Publishing Forum (IDPF). Файлы имеют расширение .epub.
EPUB разработан для контента с плавающей разметкой, что означает, что читалка EPUB может оптимизировать текст под конкретное устройство отображения. EPUB также поддерживает контент фиксированного макета. Формат предназначен как единый формат, который издатели и компании, занимающиеся конвертацией, могут использовать внутри своей организации, а также для распространения и продажи. Он заменил стандарт Open eBook.

Aspose.PDF for Python также поддерживает возможность конвертировать PDF документы в формат EPUB. Aspose.PDF for Python имеет класс под названием 'EpubSaveOptions', который можно использовать в качестве второго аргумента к [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод, для создания файла EPUB.
Пожалуйста, попробуйте использовать следующий фрагмент кода, чтобы выполнить это требование с помощью Python.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_EPUB(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.EpubSaveOptions()
    save_options.content_recognition_mode = ap.EpubSaveOptions.RecognitionMode.FLOW
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Связанные преобразования

- [Преобразовать PDF в Word](/pdf/ru/python-net/convert-pdf-to-word/) для вывода редактируемого офисного документа.
- [Конвертировать PDF в HTML](/pdf/ru/python-net/convert-pdf-to-html/) для браузерного вывода.
- [Конвертировать PDF в PDF/A, PDF/E и PDF/X](/pdf/ru/python-net/convert-pdf-to-pdf_x/) для архивных и соответствующих стандартам рабочих процессов конвертации.

## Преобразовать PDF в LaTeX/TeX

**Aspose.PDF for Python via .NET** поддерживает преобразование PDF в LaTeX/TeX.
Формат файла LaTeX — это текстовый формат файла со специальной разметкой, используемый в системе подготовки документов на основе TeX для высококачественной наборной печати.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в LaTeX/TeX онлайн**

Aspose.PDF for Python представляет вам онлайн приложение ["PDF в LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), где вы можете попытаться исследовать функциональность и качество её работы.

[![Конвертация PDF в LaTeX/TeX с приложением Aspose.PDF](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Для конвертации PDF‑файлов в TeX Aspose.PDF имеет класс [Параметры сохранения LaTeX](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) который предоставляет свойство OutDirectoryPath для сохранения временных изображений во время процесса конвертации.

Следующий фрагмент кода показывает процесс преобразования PDF‑файлов в формат TEX с помощью Python.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_TeX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.LaTeXSaveOptions()
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Конвертировать PDF в текст

**Aspose.PDF for Python** поддерживает конвертацию всего PDF‑документа и отдельной страницы в текстовый файл. Вы можете конвертировать PDF‑документ в TXT‑файл, используя класс 'TextDevice'. Следующий фрагмент кода объясняет, как извлечь текст со всех страниц.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_TXT(infile, outfile):
    document = ap.Document(infile)
    device = ap.devices.TextDevice()
    device.process(document.pages[1], outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в текст онлайн**

Aspose.PDF for Python представляет вам онлайн приложение ["PDF в Текст"](https://products.aspose.app/pdf/conversion/pdf-to-txt), где вы можете попытаться исследовать функциональность и качество её работы.

[![Aspose.PDF Конвертация PDF в Текст с приложением](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Конвертировать PDF в XPS

**Aspose.PDF for Python** предоставляет возможность конвертировать PDF файлы в формат XPS. Давайте попробуем использовать представленный фрагмент кода для конвертации PDF файлов в формат XPS с помощью Python.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в XPS онлайн**

Aspose.PDF for Python представляет вам онлайн приложение ["PDF в XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), где вы можете попытаться исследовать функциональность и качество её работы.

[![Aspose.PDF Конвертация PDF в XPS с приложением](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

Тип файла XPS в первую очередь связан со спецификацией XML Paper Specification, разработанной корпорацией Microsoft. Спецификация XML Paper Specification (XPS), ранее имевшая кодовое название Metro и включающая концепцию маркетинга Next Generation Print Path (NGPP), является инициативой Microsoft по интеграции создания и просмотра документов в операционную систему Windows.

Чтобы преобразовать PDF-файлы в XPS, Aspose.PDF имеет класс [XpsSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/) который используется в качестве второго аргумента к [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод создания XPS‑файла.

Следующий фрагмент кода демонстрирует процесс преобразования PDF‑файла в формат XPS.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_XPS(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.XpsSaveOptions()
    save_options.use_new_imaging_engine = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Преобразовать PDF в MD

Aspose.PDF имеет класс ‘MarkdownSaveOptions()’, который преобразует PDF‑документ в формат Markdown (MD), сохраняя изображения и ресурсы.

1. Загрузите исходный PDF, используя 'ap.Document'.
1. Создайте экземпляр 'MarkdownSaveOptions'.
1. Установите 'resources_directory_name' в значение 'images' – извлечённые изображения будут сохраняться в этой папке.
1. Сохраните преобразованный документ Markdown, используя настроенные параметры.
1. Выведите сообщение подтверждения после конвертации.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_MD(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.MarkdownSaveOptions()
    save_options.resources_directory_name = "images"
    save_options.use_image_html_tag = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

Markdown‑файл с текстом и связанными изображениями, хранящимися в указанной папке images.

## Конвертировать PDF в MobiXML

Этот метод преобразует документ PDF в формат MOBI (MobiXML), который обычно используется для электронных книг на устройствах Kindle.

1. Загрузите исходный PDF-документ, используя 'ap.Document'.
1. Сохраните документ в формате 'ap.SaveFormat.MOBI_XML'.
1. Выведите подтверждающее сообщение после завершения преобразования.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_MobiXML(infile, outfile):
    document = ap.Document(infile)
    document.save(outfile, ap.SaveFormat.MOBI_XML)

    print(infile + " converted into " + outfile)
```
