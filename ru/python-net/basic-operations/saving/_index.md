---
title: Сохранить PDF‑документ программно
linktitle: Сохранить PDF
type: docs
weight: 30
url: /ru/python-net/save-pdf-document/
description: Узнайте, как сохранять PDF‑файлы в Python с помощью библиотеки Aspose.PDF для Python через .NET. Сохраняйте PDF‑документ в файловую систему, в поток и в веб‑приложениях.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Сохранение PDF‑документов с помощью библиотеки Aspose.PDF в Python
Abstract: В статье даются рекомендации по сохранению PDF‑документов с использованием библиотеки Aspose.PDF в Python. Описываются три основных метода сохранения PDF — в файловую систему, в поток и в специфических форматах, таких как PDF/A или PDF/X. Метод `save()` класса `Document` является центральным для этих операций. Чтобы сохранить PDF в файловую систему, можно создать или изменить документ, например добавить новую страницу, а затем сохранить его непосредственно по пути. Для сохранения в поток перегрузки метода `Save` позволяют записать документ в объект потока. Кроме того, в статье объясняется, как сохранять документы в форматах PDF/A или PDF/X, которые являются стандартами для долгосрочного архивирования и обмена графикой соответственно. Этот процесс требует подготовки документа с помощью метода `convert` перед сохранением. Предоставленные фрагменты кода на Python демонстрируют каждый подход, показывая практическое применение этих методов.
---

## Сохранить PDF‑документ в файловую систему

Вы можете сохранить созданный или изменённый PDF‑документ в файловую систему, используя метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # make some manipation, i.g add new empty page
    document.pages.add()
    document.save(output_pdf)
```

## Сохранить PDF‑документ в поток

Вы также можете сохранить созданный или изменённый PDF‑документ в поток, используя перегрузки методов `Save`.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # make some manipation, i.g add new empty page
    document.pages.add()
    document.save(io.FileIO(output_pdf, 'w'))
```

## Сохранить формат PDF/A или PDF/X

PDF/A — это версия формата Portable Document Format (PDF), стандартизированная ISO, предназначенная для архивирования и длительного сохранения электронных документов.
PDF/A отличается от PDF тем, что запрещает функции, неподходящие для длительного архивирования, такие как связывание шрифтов (в отличие от внедрения шрифтов) и шифрование. Требования ISO к средствам просмотра PDF/A включают рекомендации по управлению цветом, поддержку встроенных шрифтов и пользовательский интерфейс для чтения встроенных аннотаций.

PDF/X является подмножеством стандарта PDF ISO. Цель PDF/X — облегчить обмен графикой, поэтому он содержит ряд требований, связанных с печатью, которые не применяются к обычным PDF‑файлам.

В обоих случаях для сохранения документов используется метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods), при этом документы должны быть подготовлены с помощью метода [convert](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    document.pages.add()
    document.convert(output_log, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(output_pdf)
```

