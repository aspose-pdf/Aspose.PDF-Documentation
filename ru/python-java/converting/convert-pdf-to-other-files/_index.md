---
title: Преобразование PDF в EPUB, LaTeX, Text, XPS на Python
linktitle: Преобразование PDF в другие форматы
type: docs
weight: 90
url: /ru/python-java/convert-pdf-to-other-files/
lastmod: "2023-04-06"
description: Эта тема показывает, как преобразовать PDF файл в другие форматы файлов, такие как EPUB, LaTeX, Text, XPS и т.д. с использованием Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Преобразование PDF в EPUB

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в EPUB онлайн**

Aspose.PDF для Python предлагает бесплатное онлайн-приложение ["PDF в EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Преобразование PDF в EPUB с бесплатным приложением](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Электронное издание">EPUB</abbr>** — это бесплатный и открытый стандарт для электронных книг от Международного форума цифровых публикаций (IDPF).
 Файлы имеют расширение .epub.  
EPUB предназначен для контента с возможностью повторного форматирования, что означает, что читалка EPUB может оптимизировать текст для конкретного устройства отображения. EPUB также поддерживает контент с фиксированной компоновкой. Формат предназначен как единый формат, который издатели и компании по конвертации могут использовать внутри компании, а также для распространения и продажи. Он заменяет стандарт Open eBook.

Aspose.PDF для Python также поддерживает функцию преобразования PDF-документов в формат EPUB. Aspose.PDF для Python имеет класс под названием 'EpubSaveOptions', который можно использовать в качестве второго аргумента в методе [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods), чтобы создать файл EPUB. Пожалуйста, попробуйте использовать следующий фрагмент кода для выполнения этого требования с помощью Python.

```python

from asposepdf import Api

# инициализация лицензии
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# Преобразование в Epub
documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.epub"
doc.save(documentOutName, Api.SaveFormat.Epub)
```

## Convert PDF to LaTeX/TeX

**Aspose.PDF для Python через Java** поддерживает преобразование PDF в LaTeX/TeX. Формат файла LaTeX - это текстовый формат файла с специальной разметкой, используемый в системе подготовки документов на основе TeX для высококачественной вёрстки.

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в LaTeX/TeX онлайн**

Aspose.PDF для Python предлагает вам бесплатное онлайн-приложение ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), где вы можете попробовать исследовать функциональность и качество работы.

[![Aspose.PDF Конвертация PDF в LaTeX/TeX с бесплатным приложением](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Для преобразования PDF-файлов в TeX, Aspose.PDF имеет класс [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/latexsaveoptions/), который предоставляет свойство OutDirectoryPath для сохранения временных изображений в процессе конвертации.

Следующий фрагмент кода показывает процесс преобразования PDF-файлов в формат TEX с использованием Python.

```python
from asposepdf import Api

documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.tex"
doc.save(documentOutName, Api.SaveFormat.TeX)
```

## Конвертировать PDF в текст

**Aspose.PDF для Python** поддерживает конвертацию всего PDF документа и отдельной страницы в текстовый файл.

### Конвертировать PDF документ в текстовый файл

Вы можете конвертировать PDF документ в TXT файл, используя класс 'TextDevice'.

Следующий фрагмент кода объясняет, как извлечь текст со всех страниц.

```python

from asposepdf import Api, Device

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_text"
# Открыть PDF документ
document = Api.Document(input_pdf)

device = Device.TextDevice()

for i in range(0, document.getPages.size):
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.txt"
    # Конвертировать определенную страницу и сохранить как текстовый файл
    device.process(document.getPages.getPage(i + 1), imageFileName)
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в текст онлайн**

Aspose.PDF для Python предлагает вам бесплатное онлайн-приложение ["PDF в текст"](https://products.aspose.app/pdf/conversion/pdf-to-txt), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в текст с бесплатным приложением](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Конвертировать PDF в XPS

**Aspose.PDF для Python** предоставляет возможность конвертировать файлы PDF в формат <abbr title="XML Paper Specification">XPS</abbr>. Давайте попробуем использовать представленный код для конвертации файлов PDF в формат XPS с помощью Python.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в XPS онлайн**

Aspose.PDF для Python предлагает вам бесплатное онлайн-приложение ["PDF в XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в XPS с бесплатным приложением](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

Тип файла XPS в основном ассоциируется с XML Paper Specification от компании Microsoft. XML Paper Specification (XPS), ранее имевшая кодовое название Metro и включающая маркетинговую концепцию Next Generation Print Path (NGPP), является инициативой Microsoft по интеграции создания и просмотра документов в операционную систему Windows.

Для преобразования файлов PDF в XPS, Aspose.PDF имеет класс [XpsSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/xpssaveoptions/), который используется в качестве второго аргумента метода [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) для генерации файла XPS.

Следующий фрагмент кода показывает процесс преобразования PDF-файла в формат XPS.

```python

from asposepdf import Api

documentName = "../../testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "../../testout/out.xps"
doc.save(documentOutName, Api.SaveFormat.Xps)

```