---
title: Извлечение изображений из PDF с помощью Python
linktitle: Извлечение изображений из PDF
type: docs
weight: 20
url: /ru/python-net/extract-images-from-the-pdf-file/
description: Узнайте, как извлекать встроенные изображения из PDF-файлов с помощью Aspose.PDF for Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как извлечь изображения из PDF через Python
Abstract: Эта статья объясняет, как извлекать встроенные изображения из PDF-документа с помощью Aspose.PDF for Python. В ней рассматривается открытие исходного PDF через класс Document, получение изображения из коллекции ресурсов страницы и сохранение извлечённого XImage во внешний файл для повторного использования, проверки или последующей обработки.
---

Используйте [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), чтобы открыть PDF, затем обратитесь к ресурсам страницы для получения объекта [XImage](https://reference.aspose.com/pdf/python-net/aspose.pdf/ximage/) и сохраните его как отдельный файл. Такой подход полезен, когда нужно повторно использовать изображения, проверять извлечённые ресурсы или строить процессы обработки изображений на основе PDF-контента.

1. Откройте PDF как `Document`.
1. Получите ресурс изображения с целевой страницы.
1. Извлеките нужный `XImage` из коллекции изображений страницы.
1. Сохраните извлечённое изображение в выходной файл.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```
