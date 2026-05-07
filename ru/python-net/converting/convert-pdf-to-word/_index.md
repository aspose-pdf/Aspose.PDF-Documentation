---
title: Конвертировать PDF в Word в Python
linktitle: Конвертировать PDF в Word
type: docs
weight: 10
url: /python-net/convert-pdf-to-word/
lastmod: "2026-04-14"
description: Узнайте, как конвертировать PDF‑файлы в DOC и DOCX в Python с помощью Aspose.PDF for Python via .NET для более простого редактирования и повторного использования документов.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Как конвертировать PDF в Word в Python
Abstract: Эта статья предоставляет исчерпывающее руководство по конвертации PDF‑файлов в форматы Microsoft Word (DOC и DOCX) с использованием Python, в частности библиотеки Aspose.PDF. В ней изложены преимущества преобразования PDF в редактируемые документы Word, позволяющие легче манипулировать содержимым, таким как текст, таблицы и изображения. Статья подробно описывает процесс конвертации PDF в DOC (формат Word 97‑2003) и DOCX, с примерами кода, демонстрирующими эти преобразования на Python. Процесс включает создание объекта `Document` из PDF и сохранение его в нужном формате с помощью метода `save()` и перечисления `SaveFormat`. Кроме того, вводится класс `DocSaveOptions`, который позволяет дополнительно настраивать процесс конвертации, например указывать режимы распознавания. Статья также подчёркивает онлайн‑приложения, предоставляемые Aspose.PDF для тестирования качества и функциональности конвертации. Содержание включает структурированный обзор и ссылки на соответствующие разделы для каждого формата.
---

## Преобразовать PDF в DOC

Одна из самых популярных функций — преобразование PDF в документ Microsoft Word DOC, что упрощает управление контентом. **Aspose.PDF for Python via .NET** позволяет конвертировать PDF‑файлы не только в DOC, но и в формат DOCX, быстро и эффективно.

Используйте преобразование в Word, когда необходимо редактировать текст, повторно использовать контент в офисных рабочих процессах или перенести содержимое PDF в редактируемые документы DOC или DOCX.

Эта [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) класс предоставляет многочисленные свойства, которые улучшают процесс преобразования PDF‑файлов в формат DOC. Среди этих свойств свойство Mode позволяет указать режим распознавания содержимого PDF. Для этого свойства можно задать любое значение из перечисления RecognitionMode. Каждое из этих значений имеет определённые преимущества и ограничения:

Шаги: Конвертировать PDF в DOC в Python

1. Загрузите PDF в объект 'ap.Document' объект.
1. Создайте экземпляр 'DocSaveOptions'.
1. Установите свойство format в значение 'DocFormat.DOC', чтобы гарантировать, что вывод будет в формате .doc (старый формат Word).
1. Сохраните PDF как документ Word, используя указанные параметры сохранения.
1. Выведите сообщение подтверждения.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOC(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в DOC онлайн**

Aspose.PDF for Python представляет вам онлайн приложение ["PDF в DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), где вы можете попробовать исследовать функциональность и качество, с которым он работает.

[![Преобразовать PDF в DOC](/pdf/ru/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Конвертировать PDF в DOCX

Aspose.PDF for Python API позволяет читать и конвертировать PDF‑документы в DOCX с помощью Python via .NET. DOCX — это широко известный формат для документов Microsoft Word, структура которого была изменена от простого бинарного к комбинации XML и бинарных файлов. Файлы Docx можно открывать в Word 2007 и последующих версиях, но не в более ранних версиях MS Word, которые поддерживают расширения файлов DOC.

Следующий фрагмент кода на Python показывает процесс конвертации PDF‑файла в формат DOCX.

Шаги: Конвертировать PDF в DOCX с помощью Python

1. Загрузите исходный PDF, используя 'ap.Document'.
1. Создайте экземпляр 'DocSaveOptions'.
1. Установите свойство format в значение 'DocFormat.DOC_X', чтобы создать файл .docx (современный формат Word).
1. Сохраните PDF как файл DOCX с настроенными параметрами сохранения.
1. Выведите сообщение подтверждения после преобразования.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOCX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    document.save(outfile, save_options)
```

## Преобразовать PDF в DOCX с расширенным распознаванием разметки

Конвертировать PDF‑документ в файл DOCX (Word) с использованием Python и Aspose.PDF с расширенными настройками распознавания. Используется режим улучшенного потока для сохранения структуры документа, делая вывод более редактируемым и ближе к исходному макету.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOCX_advanced(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    save_options.mode = ap.DocSaveOptions.RecognitionMode.ENHANCED_FLOW
    document.save(outfile, save_options)
```

Эта [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) У класса есть свойство под названием Format, которое позволяет указать формат результирующего документа, то есть DOC или DOCX. Для конвертации PDF‑файла в формат DOCX, пожалуйста, передайте значение Docx из перечисления DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**Попробуйте онлайн конвертировать PDF в DOCX**

Aspose.PDF for Python представляет вам онлайн приложение ["PDF в Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), где вы можете попробовать исследовать функциональность и качество, с которым он работает.

[![Aspose.PDF Convertion PDF в Word приложение](/pdf/ru/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Связанные преобразования

- [Преобразовать PDF в Excel](/pdf/ru/python-net/convert-pdf-to-excel/) для экспорта, ориентированного на электронные таблицы.
- [Преобразовать PDF в PowerPoint](/pdf/ru/python-net/convert-pdf-to-powerpoint/) когда вам нужны слайды презентации вместо вывода из текстового процессора.
- [Преобразовать PDF в HTML](/pdf/ru/python-net/convert-pdf-to-html/) для веб‑публикации и браузерных рабочих процессов.
