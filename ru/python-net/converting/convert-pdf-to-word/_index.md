---
title: Конвертировать PDF в Word с помощью Python
linktitle: Конвертировать PDF в Word
type: docs
weight: 10
url: /ru/python-net/convert-pdf-to-word/
lastmod: "2026-04-14"
description: Узнайте, как конвертировать файлы PDF в DOC и DOCX в Python с помощью Aspose.PDF for Python via .NET для более простого редактирования и повторного использования документов.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Как конвертировать PDF в Word с помощью Python
Abstract: В этой статье предоставлено всестороннее руководство по конвертации файлов PDF в форматы Microsoft Word (DOC и DOCX) с использованием Python, конкретно библиотеки Aspose.PDF. Описаны преимущества преобразования PDF в редактируемые документы Word, позволяющие проще работать с содержимым, таким как текст, таблицы и изображения. В статье подробно описан процесс преобразования PDF в DOC (формат Word 97‑2003) и DOCX, с примерами кода, демонстрирующими эти конверсии на Python. Процесс включает создание объекта `Document` из PDF и сохранение его в нужном формате с помощью метода `save()` и перечисления `SaveFormat`. Кроме того, представляется класс `DocSaveOptions`, который позволяет дополнительно настраивать процесс конвертации, например указывать режимы распознавания. Статья также выделяет онлайн‑приложения, предоставляемые Aspose.PDF, для тестирования качества и функциональности конверсии. Содержимое включает структурированный обзор и ссылки на соответствующие разделы для каждого формата.
---

## Конвертировать PDF в DOC

Одна из самых популярных функций — конвертация PDF в Microsoft Word DOC, которая упрощает управление контентом. **Aspose.PDF for Python via .NET** позволяет конвертировать PDF‑файлы не только в DOC, но и в формат DOCX, легко и эффективно.

Используйте конвертацию в Word, когда необходимо редактировать текст, повторно использовать контент в офисных рабочих процессах или переместить содержимое PDF в редактируемые документы DOC или DOCX.

Эта [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) класс предоставляет множество свойств, которые улучшают процесс преобразования PDF‑файлов в формат DOC. Среди этих свойств свойство Mode позволяет задать режим распознавания содержимого PDF. Для этого свойства можно указать любое значение из перечисления RecognitionMode. Каждое из этих значений имеет определённые преимущества и ограничения:

Шаги: Конвертировать PDF в DOC с помощью Python

1. Загрузите PDF в объект 'ap.Document'.
1. Создайте экземпляр 'DocSaveOptions'.
1. Установите свойство format в значение 'DocFormat.DOC', чтобы гарантировать, что вывод будет в формате .doc (старый формат Word).
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
**Попробуйте конвертировать PDF в DOC онлайн**

Aspose.PDF for Python представляет вам бесплатное онлайн‑приложение ["PDF в DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), где вы можете попытаться исследовать функциональность и качество его работы.

[![Конвертировать PDF в DOC](/pdf/ru/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Конвертировать PDF в DOCX

Aspose.PDF for Python API позволяет читать и конвертировать PDF‑документы в DOCX, используя Python через .NET. DOCX — это широко известный формат документов Microsoft Word, структура которого была изменена с обычного бинарного на комбинацию XML и бинарных файлов. Файлы DOCX можно открывать в Word 2007 и более поздних версиях, но не в более ранних версиях MS Word, которые поддерживают расширения файлов DOC.

Следующий фрагмент кода на Python демонстрирует процесс преобразования PDF‑файла в формат DOCX.

Шаги: преобразовать PDF в DOCX с помощью Python

1. Загрузите исходный PDF, используя 'ap.Document'.
1. Создайте экземпляр 'DocSaveOptions'.
1. Установите свойство format в значение 'DocFormat.DOC_X', чтобы создать файл .docx (современный формат Word).
1. Сохраните PDF как файл DOCX, используя настроенные параметры сохранения.
1. Выведите подтверждающее сообщение после конвертации.

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

Эта [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) класс имеет свойство с именем Format, которое предоставляет возможность указать формат результирующего документа, то есть DOC или DOCX. Чтобы преобразовать файл PDF в формат DOCX, передайте значение Docx из перечисления DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**Попробуйте конвертировать PDF в DOCX онлайн**

Aspose.PDF for Python представляет вам бесплатное онлайн‑приложение [“PDF в Word”](https://products.aspose.app/pdf/conversion/pdf-to-docx), где вы можете попытаться исследовать функциональность и качество его работы.

[![Aspose.PDF Convertion PDF в Word Бесплатное приложение](/pdf/ru/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Связанные преобразования

- [Преобразовать PDF в Excel](/pdf/ru/python-net/convert-pdf-to-excel/) для экспортов, ориентированных на электронные таблицы.
- [Преобразовать PDF в PowerPoint](/pdf/ru/python-net/convert-pdf-to-powerpoint/) когда вам нужны слайды презентации вместо вывода в виде текстового документа.
- [Преобразовать PDF в HTML](/pdf/ru/python-net/convert-pdf-to-html/) для веб‑публикации и браузерных рабочих процессов с контентом.
