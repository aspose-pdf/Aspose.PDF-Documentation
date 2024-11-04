---
title: Программное сохранение PDF документа
linktitle: Сохранение PDF
type: docs
weight: 30
url: /python-net/save-pdf-document/
description: Узнайте, как сохранить PDF файл в библиотеке Python Aspose.PDF для Python через .NET. Сохраните PDF документ в файловой системе, в поток и в веб-приложениях.
lastmod: "2022-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Сохранение PDF документа в файловую систему

Вы можете сохранить созданный или измененный PDF документ в файловую систему, используя метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # выполните некоторые изменения, например, добавьте новую пустую страницу
    document.pages.add()
    document.save(output_pdf)
```

## Сохранение PDF документа в поток

Вы также можете сохранить созданный или измененный PDF документ в поток, используя перегрузки методов `Save`.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # выполните некоторые изменения, например, добавьте новую пустую страницу
    document.pages.add()
    document.save(io.FileIO(output_pdf, 'w'))
```


## Сохранить в формате PDF/A или PDF/X

PDF/A — это версия формата Portable Document Format (PDF), стандартизированная ISO для использования в архивировании и длительном хранении электронных документов. PDF/A отличается от PDF тем, что запрещает функции, не подходящие для долгосрочного архивирования, такие как связывание шрифтов (в отличие от встраивания шрифтов) и шифрование. Требования ISO для просмотров PDF/A включают в себя рекомендации по управлению цветом, поддержку встроенных шрифтов и интерфейс пользователя для чтения встроенных аннотаций.

PDF/X — это подмножество стандарта ISO для PDF. Цель PDF/X заключается в упрощении обмена графикой, и поэтому он имеет ряд требований, связанных с печатью, которые не применяются к стандартным PDF-файлам.

В обоих случаях метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) используется для сохранения документов, при этом документы должны быть подготовлены с использованием метода [convert](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    document.pages.add()
    document.convert(output_log, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(output_pdf)
```