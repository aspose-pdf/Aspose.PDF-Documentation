---
title: Преобразование PDF в EPUB, LaTeX, Text, XPS на Python
linktitle: Преобразование PDF в другие форматы
type: docs
weight: 90
url: ru/python-net/convert-pdf-to-other-files/
lastmod: "2022-12-23"
keywords: преобразование, PDF, EPUB, LaTeX, Text, XPS, Python
description: Эта тема показывает, как преобразовать PDF файл в другие форматы, такие как EPUB, LaTeX, Text, XPS и т.д., используя Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Преобразование PDF в EPUB

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в EPUB онлайн**

Aspose.PDF для Python предлагает вам бесплатное онлайн-приложение ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), где вы можете попробовать исследовать функциональность и качество работы.

[![Aspose.PDF Преобразование PDF в EPUB с бесплатным приложением](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Электронная публикация">EPUB</abbr>** — это бесплатный и открытый стандарт электронных книг от Международного форума цифровых публикаций (IDPF).
 Файлы имеют расширение .epub.  
EPUB предназначен для контента с возможностью перелистывания, что означает, что EPUB-ридер может оптимизировать текст для конкретного устройства отображения. EPUB также поддерживает контент с фиксированной компоновкой. Формат предназначен как единый формат, который издатели и конверсионные дома могут использовать внутри компании, а также для распространения и продажи. Он заменяет стандарт Open eBook.

Aspose.PDF для Python также поддерживает функцию преобразования PDF-документов в формат EPUB. Aspose.PDF для Python имеет класс с именем 'EpubSaveOptions', который может быть использован в качестве второго аргумента для метода [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods), чтобы создать файл EPUB.  
Пожалуйста, попробуйте использовать следующий фрагмент кода для выполнения этого требования с помощью Python.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_epub.epub"
    # Открыть PDF-документ
    document = ap.Document(input_pdf)

    # Создать экземпляр параметров сохранения Epub
    save_options = ap.EpubSaveOptions()

    # Указать компоновку для содержимого
    save_options.content_recognition_mode = ap.EpubSaveOptions.RecognitionMode.FLOW

    # Сохранить документ ePUB
    document.save(output_pdf, save_options)
```

## Конвертировать PDF в LaTeX/TeX

**Aspose.PDF для Python через .NET** поддерживает конвертацию PDF в LaTeX/TeX. Формат файла LaTeX — это текстовый формат файла со специальной разметкой, используемый в системе подготовки документов на основе TeX для высококачественной верстки.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в LaTeX/TeX онлайн**

Aspose.PDF для Python предлагает вам бесплатное онлайн-приложение ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в LaTeX/TeX с бесплатным приложением](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Для конвертации PDF файлов в TeX, Aspose.PDF имеет класс [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/), который предоставляет свойство OutDirectoryPath для сохранения временных изображений в процессе конвертации.

Следующий фрагмент кода демонстрирует процесс конвертации PDF файлов в формат TEX с использованием Python.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_tex.tex"
    # Открыть PDF документ
    document = ap.Document(input_pdf)
    # Создать экземпляр объекта LaTeXSaveOptions
    saveOptions = ap.LaTeXSaveOptions()
    document.save(output_pdf, saveOptions)
```

## Конвертировать PDF в текст

**Aspose.PDF for Python** поддерживает преобразование всего PDF документа и отдельной страницы в текстовый файл.

### Конвертировать PDF документ в текстовый файл

Вы можете конвертировать PDF документ в TXT файл, используя класс 'TextDevice'.

Следующий фрагмент кода объясняет, как извлечь текст со всех страниц.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_txt.txt"
    # Открыть PDF документ
    document = ap.Document(input_pdf)

    # Создать текстовое устройство
    textDevice = ap.devices.TextDevice()

    # Преобразовать конкретную страницу и сохранить
    textDevice.process(document.pages[1], output_pdf)
```
 **Попробуйте конвертировать PDF в текст онлайн**
{{% alert color="success" %}}

Aspose.PDF для Python предлагает вам бесплатное онлайн-приложение ["PDF в текст"](https://products.aspose.app/pdf/conversion/pdf-to-txt), где вы можете попробовать оценить функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в текст с бесплатным приложением](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Конвертировать PDF в XPS

**Aspose.PDF для Python** предоставляет возможность конвертировать PDF файлы в формат <abbr title="XML Paper Specification">XPS</abbr>. Попробуйте использовать приведенный код для конвертации PDF файлов в формат XPS с помощью Python.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в XPS онлайн**

Aspose.PDF для Python предлагает вам бесплатное онлайн-приложение ["PDF в XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), где вы можете попробовать оценить функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в XPS с бесплатным приложением](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

Тип файла XPS в первую очередь ассоциируется с XML Paper Specification от Microsoft Corporation. XML Paper Specification (XPS), ранее имевший кодовое название Metro и включающий в себя концепцию маркетинга Next Generation Print Path (NGPP), является инициативой Microsoft по интеграции создания и просмотра документов в операционную систему Windows.

Для конвертации PDF файлов в XPS, Aspose.PDF имеет класс [XpsSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/), который используется в качестве второго аргумента метода [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) для генерации файла XPS.

Следующий фрагмент кода показывает процесс конвертации PDF файла в формат XPS.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xps.xps"
    # Открыть PDF документ
    document = ap.Document(input_pdf)

    # Создать экземпляр параметров сохранения XPS
    save_options = ap.XpsSaveOptions()

    # Сохранить XPS документ
    document.save(output_pdf, save_options)
```

## Конвертировать PDF в XML

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в XML онлайн**

Aspose.PDF для Python представляет вам бесплатное онлайн-приложение ["PDF to XML"](https://products.aspose.app/pdf/conversion/pdf-to-xml), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в XML с бесплатным приложением](pdf_to_xml.png)](https://products.aspose.app/pdf/conversion/pdf-to-xml)
{{% /alert %}}

<abbr title="Extensible Markup Language">XML</abbr> — это язык разметки и формат файла для хранения, передачи и восстановления произвольных данных.

Aspose.PDF для Python также поддерживает функцию конвертации PDF-документов в формат XML. Aspose.PDF для Python имеет класс с именем 'XmlSaveOptions', который можно использовать в качестве второго аргумента для метода [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods), чтобы сгенерировать XML-файл. Пожалуйста, попробуйте использовать следующий фрагмент кода, чтобы выполнить это требование с помощью Python.

```python

    import aspose.pdf as ap

    def convert_pdf_to_xml(self, infile, outfile):
        path_infile = self.dataDir + infile
        path_outfile = self.dataDir + outfile

        # Открыть PDF документ

        document = ap.Document(path_infile)

        # Создать экземпляр параметров сохранения XML
        save_options = ap.XmlSaveOptions()

        # Сохранить XML документ
        document.save(path_outfile, save_options)
        print(infile + " конвертирован в " + outfile)
```