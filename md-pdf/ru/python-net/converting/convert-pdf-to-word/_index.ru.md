---
title: Конвертировать PDF в документы Microsoft Word на Python
linktitle: Конвертировать PDF в Word 2003/2019
type: docs
weight: 10
url: /python-net/convert-pdf-to-word/
lastmod: "2022-12-23"
description: Узнайте, как написать код на Python для преобразования форматов PDF в Microsoft Word с помощью Aspose.PDF для Python через .NET и настроить преобразование PDF в DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Обзор

Эта статья объясняет, как **конвертировать PDF в документы Microsoft Word с использованием Python**. Она охватывает следующие темы.

_Формат_: **DOC**
- [Python PDF в DOC](#python-pdf-to-doc)
- [Python Конвертировать PDF в DOC](#python-pdf-to-doc)
- [Python Как конвертировать файл PDF в DOC](#python-pdf-to-doc)

_Формат_: **DOCX**
- [Python PDF в DOCX](#python-pdf-to-docx)
- [Python Конвертировать PDF в DOCX](#python-pdf-to-docx)
- [Python Как конвертировать файл PDF в DOCX](#python-pdf-to-docx)

_Формат_: **Word**
- [Python PDF в Word](#python-pdf-to-docx)
- [Python Конвертировать PDF в Word](#python-pdf-to-doc)

- [Python Как конвертировать файл PDF в Word](#python-pdf-to-docx)

## Python PDF to DOC и DOCX Конвертация

Одна из самых популярных функций — это преобразование PDF в Microsoft Word DOC, что упрощает управление контентом. **Aspose.PDF for Python** позволяет конвертировать PDF-файлы не только в DOC, но и в DOCX формат, легко и эффективно.

## Конвертировать PDF в DOC (Word 97-2003) файл

Конвертируйте PDF файл в формат DOC с легкостью и полным контролем. Aspose.PDF for Python гибкий и поддерживает широкий спектр преобразований. Преобразование страниц из PDF-документов в изображения, например, является очень популярной функцией.

Преобразование, которое многие из наших клиентов запрашивают, это PDF в DOC: преобразование PDF файла в документ Microsoft Word. Клиенты хотят этого, потому что PDF файлы не могут быть легко отредактированы, в то время как документы Word могут. Некоторые компании хотят, чтобы их пользователи могли манипулировать текстом, таблицами и изображениями в файлах, которые изначально были PDF.

Сохраняя традицию делать вещи простыми и понятными, Aspose.PDF for Python позволяет преобразовать исходный PDF файл в DOC файл двумя строками кода.
 Чтобы реализовать эту функцию, мы ввели перечисление с именем SaveFormat, и его значение .Doc позволяет сохранить исходный файл в формате Microsoft Word.

Следующий фрагмент кода на Python показывает процесс преобразования файла PDF в формат DOC.

<a name="csharp-pdf-to-doc"><strong>Шаги: Преобразование PDF в DOC на Python</strong></a>

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с исходным PDF-документом.
2. Сохраните его в формате [SaveFormat](https://reference.aspose.com/pdf/python-net/aspose.pdf/saveformat/), вызвав метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_doc.doc"
    # Открыть PDF-документ
    document = ap.Document(input_pdf)
    # Сохранить файл в формате документа MS Word
    document.save(output_pdf, ap.SaveFormat.DOC)
```

### Использование класса DocSaveOptions

Класс [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) предоставляет множество свойств, которые улучшают процесс преобразования PDF-файлов в формат DOC. Среди этих свойств Mode позволяет вам указать режим распознавания для содержимого PDF. Вы можете указать любое значение из перечисления RecognitionMode для этого свойства. Каждое из этих значений имеет определенные преимущества и ограничения:

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.doc"
    # Открыть PDF документ
    document = ap.Document(input_pdf)

    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC
    # Установить режим распознавания как Flow
    save_options.mode = ap.DocSaveOptions.RecognitionMode.FLOW
    # Установить горизонтальную близость как 2.5
    save_options.relative_horizontal_proximity = 2.5
    # Включить значение для распознавания маркеров в процессе конверсии
    save_options.recognize_bullets = True

    # Сохранить файл в формате документа MS Word
    document.save(output_pdf, save_options)
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в DOC онлайн**

Aspose.PDF для Python предоставляет вам бесплатное онлайн-приложение ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), где вы можете попробовать исследовать функциональность и качество его работы.
[![Convert PDF to DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) {{% /alert %}}

## Конвертация PDF в DOCX

Aspose.PDF для Python API позволяет читать и конвертировать PDF-документы в DOCX с использованием Python через .NET. DOCX — это известный формат документов Microsoft Word, структура которого была изменена с простого бинарного на комбинацию XML и бинарных файлов. Файлы DOCX могут быть открыты с помощью Word 2007 и более поздних версий, но не с более ранними версиями MS Word, которые поддерживают расширения файлов DOC.

Следующий фрагмент кода на Python показывает процесс конвертации PDF файла в формат DOCX.

<a name="csharp-pdf-to-docx"><strong>Шаги: Конвертация PDF в DOCX на Python</strong></a>

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) с исходным PDF-документом.

2. Сохраните его в формате [SaveFormat](https://reference.aspose.com/pdf/python-net/aspose.pdf/saveformat/), вызвав метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_docx_options.docx"
    # Открыть PDF документ
    document = ap.Document(input_pdf)

    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    # Установить режим распознавания как Flow
    save_options.mode = ap.DocSaveOptions.RecognitionMode.FLOW
    # Установить горизонтальную близость как 2.5
    save_options.relative_horizontal_proximity = 2.5
    # Включить распознавание маркеров в процессе конвертации
    save_options.recognize_bullets = True

    # Сохранить файл в формате документа MS Word
    document.save(output_pdf, save_options)
```

Класс [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) имеет свойство под названием Format, которое предоставляет возможность указать формат результирующего документа, то есть DOC или DOCX.
 Чтобы преобразовать файл PDF в формат DOCX, передайте значение Docx из перечисления DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**Попробуйте преобразовать PDF в DOCX онлайн**

Aspose.PDF для Python предлагает вам бесплатное онлайн-приложение ["PDF в Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), где вы можете попробовать исследовать функциональность и качество работы.

[![Aspose.PDF Конвертация PDF в Word Бесплатное приложение](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## См. также

Эта статья также охватывает следующие темы. Коды такие же, как выше.

_Формат_: **Word**
- [Python PDF в код Word](#python-pdf-to-docx)
- [Python PDF в Word API](#python-pdf-to-docx)
- [Python PDF в Word программно](#python-pdf-to-docx)
- [Python PDF в библиотеку Word](#python-pdf-to-docx)
- [Python Сохранить PDF как Word](#python-pdf-to-docx)
- [Python Генерация Word из PDF](#python-pdf-to-docx)
- [Python Создать Word из PDF](#python-pdf-to-docx)

- [Python Конвертер PDF в Word](#python-pdf-to-docx)
_Format_: **DOC**
- [Python PDF to DOC Code](#python-pdf-to-doc)
- [Python PDF to DOC API](#python-pdf-to-doc)
- [Python PDF to DOC Programmatically](#python-pdf-to-doc)
- [Python PDF to DOC Library](#python-pdf-to-doc)
- [Python Save PDF as DOC](#python-pdf-to-doc)
- [Python Generate DOC from PDF](#python-pdf-to-doc)
- [Python Create DOC from PDF](#python-pdf-to-doc)
- [Python PDF to DOC Converter](#python-pdf-to-doc)

_Format_: **DOCX**
- [Python PDF to DOCX Code](#python-pdf-to-docx)
- [Python PDF to DOCX API](#python-pdf-to-docx)
- [Python PDF to DOCX Programmatically](#python-pdf-to-docx)
- [Python PDF to DOCX Library](#python-pdf-to-docx)
- [Python Save PDF as DOCX](#python-pdf-to-docx)
- [Python Generate DOCX from PDF](#python-pdf-to-docx)
- [Python Create DOCX from PDF](#python-pdf-to-docx)
- [Python PDF to DOCX Converter](#python-пdf-to-docx)