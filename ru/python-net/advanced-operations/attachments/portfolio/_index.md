---
title: Создайте PDF‑портфолио на Python
linktitle: Портфолио
type: docs
weight: 20
url: /python-net/portfolio/
description: Узнайте, как создавать и управлять PDF‑портфолио на Python с помощью Aspose.PDF for Python via .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создавайте и редактируйте PDF‑портфолио со встроенными файлами на Python
Abstract: В этой статье объясняется, как создавать и управлять PDF‑портфолио с использованием Aspose.PDF for Python via .NET. Узнайте, как объединять несколько типов файлов в одно PDF‑портфолио, добавлять файлы в коллекцию документов и программно удалять элементы портфолио с помощью Python.
---

Создание PDF‑портфолио позволяет консолидировать и архивировать различные типы файлов в едином, согласованном документе. Такой документ может включать текстовые файлы, изображения, электронные таблицы, презентации и другие материалы, обеспечивая хранение и организацию всех соответствующих данных в одном месте.

PDF‑портфель поможет продемонстрировать вашу презентацию в высоком качестве, где бы вы её ни использовали. В целом, создание PDF‑портфеля — это очень актуальная и современная задача.

Используйте PDF‑портфель, когда хотите распределить набор связанных файлов вместе, сохранив каждый файл в его исходном формате внутри одного PDF‑контейнера.

## Как создать PDF‑портфель

Aspose.PDF for Python via .NET позволяет создавать документы PDF‑портфеля, используя [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class. Добавьте файл в объект document.collection после получения его с помощью [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) class. После добавления файлов используйте Document class' [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод для сохранения документа портфеля.

В следующем примере используется файл Microsoft Excel, документ Word и файл изображения для создания PDF‑портфеля.

Код ниже приводит к следующему портфолио.

### PDF‑портфолио, созданное с помощью Aspose.PDF for Python

![PDF‑портфолио, созданное с помощью Aspose.PDF for Python](working-with-pdf-portfolio_1.jpg)

```python
import aspose.pdf as ap

def create_pdf_portfolio(input_files, outfile):
    # Instantiate Document Object
    document = ap.Document()

    # Instantiate document Collection object
    document.collection = ap.Collection()

    # Get Files to add to Portfolio
    excel = ap.FileSpecification(input_files[0])
    word = ap.FileSpecification(input_files[1])
    image = ap.FileSpecification(input_files[2])

    # Provide description of the files
    excel.description = "Excel File"
    word.description = "Word File"
    image.description = "Image File"

    # Add files to document collection
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Save Portfolio document
    document.save(outfile)
```

## Удалить файлы из PDF Portfolio

Чтобы удалить файлы из PDF‑портфеля, попробуйте использовать следующие строки кода.

```python
import aspose.pdf as ap

def remove_files_from_pdf_portfolio(infile, outfile):
    # Open document
    document = ap.Document(infile)
    document.collection.delete()

    # Save updated file
    document.save(outfile)
```

## Связанные темы вложений

- [Работа с вложениями PDF в Python](/pdf/ru/python-net/attachments/)
- [Добавить вложения в PDF с помощью Python](/pdf/ru/python-net/add-attachment-to-pdf-document/)
- [Удалить вложения из PDF в Python](/pdf/ru/python-net/removing-attachment-from-an-existing-pdf/)

