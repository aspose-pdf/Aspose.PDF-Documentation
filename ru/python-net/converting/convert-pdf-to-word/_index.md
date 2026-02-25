---
title: Преобразовать PDF в документы Microsoft Word на Python
linktitle: Преобразовать PDF в Word
type: docs
weight: 10
url: /ru/python-net/convert-pdf-to-word/
lastmod: "2025-09-27"
description: Узнайте, как преобразовать PDF‑документы в формат Word на Python с помощью Aspose.PDF для удобного редактирования документов.
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как преобразовать PDF в Word на Python
Abstract: Эта статья предоставляет всестороннее руководство по преобразованию PDF‑файлов в форматы Microsoft Word (DOC и DOCX) с помощью Python, конкретно используя библиотеку Aspose.PDF. В ней изложены преимущества преобразования PDF в редактируемые документы Word, позволяющие легче манипулировать содержимым, таким как текст, таблицы и изображения. Статья подробно описывает процесс конвертации PDF в DOC (формат Word 97‑2003) и DOCX, включая фрагменты кода, демонстрирующие эти преобразования на Python. Процесс включает создание объекта `Document` из PDF и сохранение его в требуемом формате с помощью метода `save()` и перечисления `SaveFormat`. Кроме того, она знакомит с классом `DocSaveOptions`, который позволяет дополнительно настраивать процесс конвертации, например, указывая режимы распознавания. В статье также подчёркнуты онлайн‑приложения, предоставляемые Aspose.PDF для проверки качества и функциональности конвертации. Содержание включает структурированный обзор и ссылки на соответствующие разделы для каждого формата.
---

## Преобразовать PDF в DOC

Одна из самых популярных функций – преобразование PDF в Microsoft Word DOC, что упрощает управление контентом. **Aspose.PDF for Python via .NET** позволяет конвертировать PDF‑файлы не только в DOC, но и в формат DOCX, легко и эффективно.

Класс [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) предоставляет множество свойств, улучшающих процесс конвертации PDF‑файлов в формат DOC. Среди этих свойств свойство Mode позволяет указать режим распознавания содержимого PDF. Для этого свойства можно задать любое значение из перечисления RecognitionMode. Каждое из этих значений имеет свои преимущества и ограничения:

Шаги: преобразовать PDF в DOC на Python

1. Загрузите PDF в объект 'ap.Document'.
1. Создайте экземпляр 'DocSaveOptions'.
1. Установите свойство format в 'DocFormat.DOC', чтобы обеспечить вывод в формате .doc (старый формат Word).
1. Сохраните PDF как документ Word, используя указанные параметры сохранения.
1. Выведите сообщение подтверждения.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.DocSaveOptions()
    save_options.format = apdf.DocSaveOptions.DocFormat.DOC
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в DOC онлайн**

Aspose.PDF for Python предлагает вам бесплатное онлайн‑приложение [\"PDF в DOC\"](https://products.aspose.app/pdf/conversion/pdf-to-doc), где вы можете проверить его функции и качество работы.

[![Преобразовать PDF в DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Преобразовать PDF в DOCX

Aspose.PDF for Python API позволяет читать и преобразовывать PDF‑документы в DOCX с помощью Python via .NET. DOCX — известный формат документов Microsoft Word, структура которого была изменена с простого бинарного на комбинацию XML‑ и бинарных файлов. Файлы Docx можно открывать в Word 2007 и последующих версиях, но не в более ранних версиях MS Word, поддерживающих расширения файлов DOC.

Следующий фрагмент кода на Python демонстрирует процесс преобразования PDF‑файла в формат DOCX.

Шаги: преобразовать PDF в DOCX на Python

1. Загрузите исходный PDF, используя 'ap.Document'.
1. Создайте экземпляр 'DocSaveOptions'.
1. Установите свойство format в 'DocFormat.DOC_X', чтобы создать файл .docx (современный формат Word).
1. Сохраните PDF как файл DOCX, используя настроенные параметры сохранения.
1. Выведите сообщение подтверждения после конвертации.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.DocSaveOptions()
    save_options.format = apdf.DocSaveOptions.DocFormat.DOC_X
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

Класс [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) имеет свойство Format, которое позволяет задать формат получаемого документа, то есть DOC или DOCX. Чтобы преобразовать PDF‑файл в формат DOCX, укажите значение Docx из перечисления DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**Попробуйте преобразовать PDF в DOCX онлайн**

Aspose.PDF for Python предлагает вам бесплатное онлайн‑приложение [\"PDF в Word\"](https://products.aspose.app/pdf/conversion/pdf-to-docx), где вы можете проверить его функции и качество работы.

[![Бесплатное приложение Aspose.PDF Конвертация PDF в Word](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

