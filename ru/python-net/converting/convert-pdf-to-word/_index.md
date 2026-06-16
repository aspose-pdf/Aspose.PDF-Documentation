---
title: Конвертировать PDF в Word в Python
linktitle: Конвертировать PDF в Word
type: docs
weight: 10
url: /ru/python-net/convert-pdf-to-word/
lastmod: "2026-04-14"
description: Узнайте, как конвертировать PDF в Word с помощью Python, включая PDF в DOC, PDF в DOCX и продвинутое распознавание макета с Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Конвертировать PDF в DOC и DOCX в Python
Abstract: В этой статье показано, как конвертировать PDF‑файлы в форматы Microsoft Word с помощью Aspose.PDF for Python via .NET. Охвачены конвертация PDF в DOC, PDF в DOCX и расширенные параметры распознавания макета для создания редактируемых документов Word из PDF‑контента.
---

Эта страница показывает, как **конвертировать PDF в Word на Python**. Используйте эти примеры, когда вам нужен редактируемый вывод DOC или DOCX из PDF‑файла для правки, повторного использования или офисных рабочих процессов с документами.

## Конвертировать PDF в DOC на Python

Одна из самых популярных функций — конвертация PDF в Microsoft Word DOC, что упрощает управление контентом. **Aspose.PDF for Python via .NET** позволяет конвертировать PDF‑файлы не только в DOC, но и в формат DOCX легко и эффективно.

Используйте конвертацию в Word, когда вам нужно редактировать текст, повторно использовать контент в офисных рабочих процессах или переместить содержимое PDF в редактируемые документы DOC или DOCX.

The [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) Класс DocSaveOptions предоставляет множество свойств, которые улучшают процесс конвертации файлов PDF в формат DOC. Среди этих свойств свойство Mode позволяет указать режим распознавания содержимого PDF. Вы можете задать любое значение из перечисления RecognitionMode для этого свойства. Каждое из этих значений имеет конкретные преимущества и ограничения:

Шаги: конвертировать PDF в DOC на Python

1. Загрузите PDF в объект 'ap.Document'.
1. Создайте экземпляр 'DocSaveOptions'.
1. Установите свойство format в значение 'DocFormat.DOC', чтобы гарантировать, что вывод будет в формате .doc (старый формат Word).
1. Сохраните PDF как документ Word, используя указанные параметры сохранения.
1. Выведите подтверждающее сообщение.

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

Aspose.PDF for Python представляет вам онлайн‑приложение ["PDF в DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), где вы можете попытаться исследовать функциональность и качество, как это работает.

[![Конвертировать PDF в DOC](/pdf/ru/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Конвертировать PDF в DOCX на Python

Aspose.PDF for Python API позволяет читать и конвертировать PDF‑документы в DOCX с помощью Python через .NET. DOCX — это широко известный формат для документов Microsoft Word, структура которого была изменена с простого бинарного на комбинацию XML‑ и бинарных файлов. Файлы DOCX можно открывать в Word 2007 и последующих версиях, но не в более ранних версиях MS Word, поддерживающих расширения файлов DOC.

Следующий фрагмент кода на Python демонстрирует процесс конвертации PDF‑файла в формат DOCX.

Шаги: Конвертировать PDF в DOCX с помощью Python

1. Загрузите исходный PDF, используя 'ap.Document'.
1. Создайте экземпляр 'DocSaveOptions'.
1. Установите свойство format в значение 'DocFormat.DOC_X', чтобы сгенерировать файл .docx (современный формат Word).
1. Сохраните PDF как файл DOCX с использованием настроенных параметров сохранения.
1. Выведите сообщение подтверждения после конвертации.

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

## Преобразовать PDF в DOCX с расширенным распознаванием макета

Преобразовать PDF‑документ в файл DOCX (Word) с помощью Python и Aspose.PDF, используя расширенные настройки распознавания. Он использует улучшенный режим потока для сохранения структуры документа, делая вывод более редактируемым и ближе к оригинальному макету.

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

The [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) класс имеет свойство под названием Format, которое предоставляет возможность указать формат результирующего документа, то есть DOC или DOCX. Чтобы преобразовать файл PDF в формат DOCX, передайте значение Docx из перечисления DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**Попробуйте конвертировать PDF в DOCX онлайн**

Aspose.PDF for Python представляет вам онлайн‑приложение ["PDF в Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), где вы можете попытаться исследовать функциональность и качество, как это работает.

[![Aspose.PDF Конвертация PDF в Word приложение](/pdf/ru/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Связанные конвертации

- [Конвертировать PDF в Excel](/pdf/ru/python-net/convert-pdf-to-excel/) для экспорта, ориентированного на электронные таблицы.
- [Конвертировать PDF в PowerPoint](/pdf/ru/python-net/convert-pdf-to-powerpoint/) когда вам нужны слайды презентации вместо вывода для обработки текста.
- [Конвертировать PDF в HTML](/pdf/ru/python-net/convert-pdf-to-html/) для веб‑публикации и рабочих процессов, основанных на браузерах.
