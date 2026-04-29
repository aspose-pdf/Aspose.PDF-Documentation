---
title: Сохранить PDF‑документ программно
linktitle: Сохранить PDF
type: docs
weight: 30
url: /python-net/save-pdf-document/
description: Узнайте, как сохранить файл PDF в Python с использованием библиотеки Aspose.PDF for Python via .NET. Сохраните PDF‑документ в файловую систему, в поток и в веб‑приложениях.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Сохранение PDF‑документов с использованием библиотеки Aspose.PDF в Python
Abstract: Статья предоставляет рекомендации по сохранению PDF‑документов с использованием библиотеки Aspose.PDF в Python. В ней описываются три основных метода сохранения PDF — в файловую систему, в поток и в специфических форматах, таких как PDF/A или PDF/X. Метод `save()` класса `Document` является центральным для этих операций. Чтобы сохранить PDF в файловую систему, документ может быть создан или изменён, например, добавив новую страницу, и затем сохранён непосредственно по указанному пути. При сохранении в поток перегрузки метода `Save` позволяют записать документ в объект потока. Кроме того, статья объясняет, как сохранять документы в форматах PDF/A или PDF/X, которые являются стандартами для долгосрочного архивирования и обмена графикой соответственно. Этот процесс требует подготовки документа с помощью метода `convert` перед сохранением. Приведённые фрагменты кода на Python демонстрируют каждый подход, илстрируя практическое применение этих методов.
---

## Сохранить PDF-документ в файловую систему

Вы можете сохранить созданный или обработанный PDF-документ в файловую систему, используя [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) класс.

```python
import aspose.pdf as ap

def save_document_to_file(infile, outfile):
    document = ap.Document(infile)
    # make some manipulation, e.g. add new empty page
    document.pages.add()
    document.save(outfile)
```

## Сохранить PDF-документ в поток

Вы также можете сохранить созданный или изменённый PDF‑документ в поток, используя перегрузки `Save` методы.

```python
import aspose.pdf as ap
import io

def save_document_to_stream(infile, outfile):
    document = ap.Document(infile)
    # make some manipulation, e.g. add new empty page
    document.pages.add()
    with io.FileIO(outfile, 'w') as stream:
        document.save(stream)
```

## Сохранить формат PDF/A или PDF/X

Вы можете легко сохранить документ в конкретной версии PDF, например PDF/A или PDF/X. В этом случае нам нужно вызвать метод convert перед сохранением документа.

PDF/A — это версия Portable Document Format (PDF), стандартизированная ISO, предназначенная для архивирования и длительного сохранения электронных документов.
PDF/A отличается от PDF тем, что запрещает функции, не подходящие для длительного архивирования, такие как связывание шрифтов (в отличие от встраивания шрифтов) и шифрование. Требования ISO к просмотрщикам PDF/A включают руководства по управлению цветом, поддержку встраиваемых шрифтов и пользовательский интерфейс для чтения встроенных аннотаций.

PDF/X является подмножеством стандарта PDF ISO. Цель PDF/X — облегчить обмен графикой, поэтому у него есть ряд требований, связанных с печатью, которые не применяются к стандартным PDF‑файлам.

В обоих случаях, [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод используется для хранения документов, в то время как документы должны быть подготовлены с использованием [конвертировать](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод.

```python
import aspose.pdf as ap
import io


def save_document_as_standard(infile, outfile, logfile):
    document = ap.Document(infile)
    document.pages.add()
    document.convert(logfile, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```
