---
title: Конвертировать PDF в EPUB, Text, XPS и другие форматы на Python
linktitle: Конвертировать PDF в другие форматы
type: docs
weight: 90
url: /python-net/convert-pdf-to-other-files/
lastmod: "2026-04-14"
description: Узнайте, как конвертировать PDF‑файлы в EPUB, LaTeX, Markdown, текст, XPS и MobiXML в Python с помощью Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true 
AlternativeHeadline: Как конвертировать PDF в другие форматы в Python
Abstract: В статье представлено всестороннее руководство по конвертации PDF‑файлов в различные форматы с использованием Aspose.PDF for Python. Описывается конвертация PDF в форматы EPUB, LaTeX/TeX, Text, XPS и XML. Каждый раздел начинается с приглашения попробовать бесплатные онлайн‑приложения, предоставляемые Aspose, для конвертации PDF в соответствующие форматы, подчёркивая простоту использования и качество этих инструментов.
---

## Конвертировать PDF в EPUB

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в EPUB онлайн**

Aspose.PDF for Python представляет вам онлайн бесплатное приложение ["PDF в EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), где вы можете попытаться исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в EPUB с бесплатным приложением](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> является бесплатным и открытым стандартом электронных книг от Международного форума цифровой публикации (IDPF). Файлы имеют расширение .epub.
EPUB разработан для переоформляемого контента, что означает, что читалка EPUB может оптимизировать текст под конкретное устройство отображения. EPUB также поддерживает контент фиксированной верстки. Формат предназначен как единый формат, который издатели и компании по конвертации могут использовать внутри компании, а также для распространения и продажи. Он заменяет стандарт Open eBook.

Aspose.PDF for Python также поддерживает функцию преобразования PDF-документов в формат EPUB. Aspose.PDF for Python имеет класс с именем \u0027EpubSaveOptions\u0027, который может использоваться в качестве второго аргумента к [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод для создания файла EPUB.
Пожалуйста, попробуйте использовать следующий фрагмент кода, чтобы выполнить это требование с помощью Python.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

document = ap.Document(path_infile)
save_options = ap.EpubSaveOptions()
save_options.content_recognition_mode = ap.EpubSaveOptions.RecognitionMode.FLOW
document.save(path_outfile, save_options)

print(infile + " converted into " + outfile)
```

## Связанные преобразования

- [Конвертировать PDF в Word](/pdf/ru/python-net/convert-pdf-to-word/) для редактируемого вывода офисного документа.
- [Конвертировать PDF в HTML](/pdf/ru/python-net/convert-pdf-to-html/) для вывода, ориентированного на браузер.
- [Конвертировать PDF в PDF/A, PDF/E и PDF/X](/pdf/ru/python-net/convert-pdf-to-pdf_x/) для архивных и соответствующих стандартам процессов конвертации.

## Преобразовать PDF в LaTeX/TeX

**Aspose.PDF for Python via .NET** поддерживает конвертацию PDF в LaTeX/TeX.
Формат файла LaTeX — это текстовый формат с особой разметкой, используемый в системе подготовки документов на основе TeX для высококачественного набора.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в LaTeX/TeX онлайн**

Aspose.PDF for Python представляет вам онлайн бесплатное приложение ["PDF в LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), где вы можете попытаться исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в LaTeX/TeX с бесплатным приложением](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Для преобразования PDF‑файлов в TeX, Aspose.PDF имеет класс [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) который предоставляет свойство OutDirectoryPath для сохранения временных изображений во время процесса конвертации.

Следующий фрагмент кода показывает процесс преобразования PDF‑файлов в формат TEX с помощью Python.

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

## Преобразовать PDF в текст

**Aspose.PDF for Python** поддерживает преобразование полного PDF‑документа и отдельной страницы в текстовый файл. Вы можете конвертировать PDF‑документ в TXT‑файл, используя класс 'TextDevice'. Следующий фрагмент кода объясняет, как извлечь текст со всех страниц.

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
**Попробуйте конвертировать PDF в текст онлайн**

Aspose.PDF for Python представляет вам онлайн бесплатное приложение ["PDF в Текст"](https://products.aspose.app/pdf/conversion/pdf-to-txt), где вы можете попытаться исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в Текст с бесплатным приложением](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Конвертировать PDF в XPS

**Aspose.PDF for Python** предоставляет возможность конвертировать PDF‑файлы в формат XPS. Попробуем использовать представленный фрагмент кода для конвертации PDF‑файлов в формат XPS с помощью Python.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в XPS онлайн**

Aspose.PDF for Python представляет вам онлайн бесплатное приложение [PDF в XPS](https://products.aspose.app/pdf/conversion/pdf-to-xps), где вы можете попытаться исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в XPS с бесплатным приложением](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

Тип файла XPS в первую очередь связан со спецификацией XML Paper Specification корпорации Microsoft. XML Paper Specification (XPS), ранее codenamed Metro и включающая маркетинговую концепцию Next Generation Print Path (NGPP), является инициативой Microsoft\u0027s по интеграции создания и просмотра документов в операционную систему Windows.

Для преобразования PDF‑файлов в XPS, Aspose.PDF имеет класс [XpsSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/) который используется в качестве второго аргумента к [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод для генерации файла XPS.

Следующий фрагмент кода показывает процесс преобразования файла PDF в формат XPS.

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

## Конвертировать PDF в MD

Aspose.PDF имеет класс ‘MarkdownSaveOptions()’, который преобразует PDF‑документ в формат Markdown (MD), сохраняя изображения и ресурсы.

1. Загрузите исходный PDF, используя 'ap.Document'.
1. Создайте экземпляр 'MarkdownSaveOptions'.
1. Установите 'resources_directory_name' в 'images' – извлечённые изображения будут сохраняться в этой папке.
1. Сохраните преобразованный документ Markdown, используя настроенные параметры.
1. Выведите сообщение подтверждения после преобразования.

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

Markdown‑файл с текстом и связанными изображениями, хранящимися в указанной папке images.

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
