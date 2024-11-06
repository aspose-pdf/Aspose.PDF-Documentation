---
title: Преобразование PDF в документы Microsoft Word на Python
linktitle: Преобразование PDF в Word 2003/2019
type: docs
weight: 10
url: ru/python-java/convert-pdf-to-word/
lastmod: "2023-04-06"
description: Узнайте, как написать код на Python для конвертации PDF в форматы Microsoft Word с помощью Aspose.PDF для Python через .NET, и настройте конвертацию PDF в DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Обзор

Эта статья объясняет, как **конвертировать PDF в документы Microsoft Word с использованием Python**. Она охватывает следующие темы.

_Формат_: **DOC**
- [Python PDF в DOC](#python-pdf-to-doc)
- [Python Преобразование PDF в DOC](#python-pdf-to-doc)
- [Python Как конвертировать файл PDF в DOC](#python-pdf-to-doc)

_Формат_: **DOCX**
- [Python PDF в DOCX](#python-pdf-to-docx)
- [Python Преобразование PDF в DOCX](#python-pdf-to-docx)
- [Python Как конвертировать файл PDF в DOCX](#python-pdf-to-docx)

_Формат_: **Word**
- [Python PDF в Word](#python-pdf-to-docx)
- [Python Преобразование PDF в Word](#python-pdf-to-doc)

- [Python Как конвертировать файл PDF в Word](#python-pdf-to-docx)

## Python PDF to DOC и DOCX Конвертация

Одна из самых популярных функций — это конвертация PDF в Microsoft Word DOC, что упрощает управление контентом. **Aspose.PDF for Python** позволяет конвертировать PDF файлы не только в DOC, но и в DOCX формат, легко и эффективно.

## Конвертация PDF в DOC (Word 97-2003) файл

Конвертируйте PDF файл в формат DOC с легкостью и полным контролем. Aspose.PDF for Python гибок и поддерживает широкий спектр конверсий. Например, конвертация страниц из PDF документов в изображения является очень популярной функцией.

Конвертация, которую запрашивали многие наши клиенты, это PDF в DOC: преобразование PDF файла в документ Microsoft Word. Клиенты хотят это, потому что PDF файлы нельзя легко редактировать, тогда как документы Word можно. Некоторые компании хотят, чтобы их пользователи могли изменять текст, таблицы и изображения в файлах, которые изначально были PDF.

Сохраняя традицию делать вещи простыми и понятными, Aspose.PDF for Python позволяет преобразовать исходный PDF файл в DOC файл с помощью двух строк кода.
 Чтобы реализовать эту функцию, мы ввели перечисление с именем SaveFormat, и его значение .Doc позволяет сохранить исходный файл в формате Microsoft Word.

Следующий фрагмент кода на Python показывает процесс преобразования файла PDF в формат DOC.

<a name="csharp-pdf-to-doc"><strong>Шаги: Конвертация PDF в DOC на Python</strong></a>

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) с исходным PDF-документом.
2. Сохраните его в формате [SaveFormat.Doc](https://reference.aspose.com/pdf/python-java/aspose.pdf/saveformat/), вызвав метод [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods).

```python

from asposepdf import Api

documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/out.doc"
doc.save(documentOutName, Api.SaveFormat.Doc)
```

### Использование класса DocSaveOptions

Класс [DocSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/docsaveoptions/) предоставляет множество свойств, которые улучшают процесс преобразования PDF-файлов в формат DOC. Среди этих свойств Mode позволяет вам указать режим распознавания для содержимого PDF. Вы можете указать любое значение из перечисления RecognitionMode для этого свойства. Каждое из этих значений имеет свои конкретные преимущества и ограничения:

```python

from asposepdf import Api

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.doc"
# Открыть PDF документ
document = Api.Document(input_pdf)

save_options = Api.DocSaveOptions()
save_options.format = Api.DocSaveOptions.DocFormat.Doc
# Установить режим распознавания как Flow
save_options.mode = Api.DocSaveOptions.RecognitionMode.Flow
# Установить горизонтальную близость как 2.5
save_options.relative_horizontal_proximity = 2.5
# Включить опцию распознавания маркеров во время процесса конверсии
save_options.recognize_bullets = True

# Сохранить файл в формате MS Word документа
document.save(output_pdf, save_options)

```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в DOC онлайн**


Aspose.PDF for Python предлагает вам бесплатное онлайн-приложение ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), где вы можете попробовать исследовать функциональность и качество его работы.
[![Convert PDF to DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)  
{{% /alert %}}

## Преобразование PDF в DOCX

Aspose.PDF для Python API позволяет читать и конвертировать PDF-документы в DOCX с помощью Python через .NET. DOCX — это известный формат для документов Microsoft Word, структура которого была изменена с простого бинарного на комбинацию XML и бинарных файлов. Файлы Docx могут быть открыты в Word 2007 и более поздних версиях, но не в более ранних версиях MS Word, которые поддерживают расширения файлов DOC.

Следующий фрагмент кода на Python показывает процесс преобразования файла PDF в формат DOCX.

<a name="csharp-pdf-to-docx"><strong>Шаги: Преобразование PDF в DOCX на Python</strong></a>

1. Создайте экземпляр объекта [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) с исходным PDF-документом.

2. Сохраните его в формате [SaveFormat.DocX](https://reference.aspose.com/pdf/python-java/aspose.pdf/saveformat/), вызвав метод [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods).

```python


from asposepdf import Api

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.docx"
# Открыть PDF документ
document = Api.Document(input_pdf)

save_options = Api.DocSaveOptions()
save_options.format = Api.DocSaveOptions.DocFormat.Docx
# Установить режим распознавания как Flow
save_options.mode = Api.DocSaveOptions.RecognitionMode.Flow
# Установить горизонтальную близость как 2.5
save_options.relative_horizontal_proximity = 2.5
# Включить значение для распознавания маркеров в процессе конверсии
save_options.recognize_bullets = True

# Сохранить файл в формате документа MS Word
document.save(output_pdf, save_options)
```

Класс [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) имеет свойство под названием Format, которое предоставляет возможность указать формат результирующего документа, то есть DOC или DOCX.
 Для того чтобы преобразовать файл PDF в формат DOCX, передайте значение Docx из перечисления DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**Попробуйте преобразовать PDF в DOCX онлайн**

Aspose.PDF для Python предлагает вам бесплатное онлайн-приложение ["PDF в Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), где вы можете попробовать исследовать, как работают его функциональные возможности и качество.

[![Aspose.PDF Конвертация PDF в Word Бесплатное Приложение](/pdf/java/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## См. также

Эта статья также охватывает следующие темы. Коды такие же, как и выше.

_Формат_: **Word**
- [Код для преобразования PDF в Word на Python](#python-pdf-to-docx)
- [API для преобразования PDF в Word на Python](#python-pdf-to-docx)
- [Программное преобразование PDF в Word на Python](#python-pdf-to-docx)
- [Библиотека для преобразования PDF в Word на Python](#python-pdf-to-docx)
- [Сохранение PDF как Word на Python](#python-pdf-to-docx)
- [Генерация Word из PDF на Python](#python-pdf-to-docx)
- [Создание Word из PDF на Python](#python-pdf-to-docx)

- [Конвертер PDF в Word на Python](#python-pdf-to-docx)
_Format_: **DOC**
- [Python PDF to DOC Code](#python-pdf-to-doc)
- [Python PDF to DOC API](#python-pdf-to-doc)
- [Python PDF to DOC Программно](#python-pdf-to-doc)
- [Python Библиотека для PDF в DOC](#python-pdf-to-doc)
- [Python Сохранить PDF как DOC](#python-pdf-to-doc)
- [Python Генерация DOC из PDF](#python-pdf-to-doc)
- [Python Создать DOC из PDF](#python-pdf-to-doc)
- [Python Конвертер PDF в DOC](#python-pdf-to-doc)

_Format_: **DOCX**
- [Python PDF to DOCX Code](#python-pdf-to-docx)
- [Python PDF to DOCX API](#python-pdf-to-docx)
- [Python PDF to DOCX Программно](#python-pdf-to-docx)
- [Python Библиотека для PDF в DOCX](#python-pdf-to-docx)
- [Python Сохранить PDF как DOCX](#python-pdf-to-docx)
- [Python Генерация DOCX из PDF](#python-pdf-to-docx)
- [Python Создать DOCX из PDF](#python-pdf-to-docx)
- [Python Конвертер PDF в DOCX](#python-pdf-to-docx)