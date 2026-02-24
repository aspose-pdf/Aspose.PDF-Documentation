---
title: Работа с портфолио в PDF с использованием Python
linktitle: Портфолио
type: docs
weight: 20
url: /ru/python-net/portfolio/
description: Как создать PDF‑портфолио с помощью Python. Для создания PDF‑портфолио следует использовать файл Microsoft Excel, документ Word и файл изображения.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как работать с портфолио в PDF с помощью Python
Abstract: В этой статье рассматривается создание и управление PDF‑портфолио с использованием Aspose.PDF for Python via .NET. PDF‑портфолио облегчает консолидирование различных типов файлов — таких как текстовые файлы, изображения, таблицы и презентации — в один упорядоченный документ, обеспечивая совместное хранение всех необходимых материалов. В статье описывается процесс создания PDF‑портфолио, с акцентом на использование класса `Document` и класса `FileSpecification` для добавления файлов в коллекцию документов. Приведен пример, демонстрирующий включение файла Microsoft Excel, документа Word и файла изображения в PDF‑портфолио. Кроме того, в статье содержатся фрагменты кода как для создания портфолио, так и для удаления из него файлов, иллюстрирующие простоту и эффективность управления PDF‑портфолио с помощью Aspose.PDF for Python.
---

Создание PDF‑портфолио позволяет консолидировать и архивировать различные типы файлов в один единый документ. Такой документ может включать текстовые файлы, изображения, электронные таблицы, презентации и другие материалы, обеспечивая хранение и организацию всех необходимых данных в одном месте.

PDF‑портфолио поможет демонстрировать вашу презентацию в высоком качестве, где бы вы её ни использовали. В целом, создание PDF‑портфолио — актуальная и современная задача.

## Как создать PDF‑портфолио

Aspose.PDF for Python via .NET позволяет создавать документы PDF‑Portfolio с использованием класса [Документ](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) . Добавьте файл в объект document.collection после получения его с помощью класса [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) . После добавления файлов используйте метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) класса Document для сохранения документа портфолио.

В следующем примере используется файл Microsoft Excel, документ Word и файл изображения для создания PDF‑портфолио.

Код ниже приводит к следующему портфолио.

### PDF‑портфолио, созданное с помощью Aspose.PDF for Python

![PDF‑портфолио, созданное с помощью Aspose.PDF for Python](working-with-pdf-portfolio_1.jpg)

```python

    import aspose.pdf as ap

    # Instantiate Document Object
    document = ap.Document()

    # Instantiate document Collection object
    document.collection = ap.Collection()

    # Get Files to add to Portfolio
    excel = ap.FileSpecification(input_excel)
    word = ap.FileSpecification(input_doc)
    image = ap.FileSpecification(input_jpg)

    # Provide description of the files
    excel.description = "Excel File"
    word.description = "Word File"
    image.description = "Image File"

    # Add files to document collection
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Save Portfolio document
    document.save(output_pdf)
```

## Удаление файлов из PDF‑портфолио

Чтобы удалить файлы из PDF‑портфолио, попробуйте использовать следующие строки кода.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    document.collection.delete()

    # Save updated file
    document.save(output_pdf)
```


