---
title: Извлеките шрифты из PDF с помощью Python
linktitle: Извлеките шрифты из PDF
type: docs
weight: 30
url: /ru/python-net/extract-fonts-from-pdf/
description: Используйте библиотеку Aspose.PDF for Python для извлечения всех встроенных шрифтов из PDF-документа.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как извлечь шрифты из PDF с помощью Python
Abstract: Эта статья объясняет, как анализировать шрифты, используемые в PDF-документе, с помощью Aspose.PDF for Python. В ней показано, как открыть PDF через класс Document, вызвать `font_utilities.get_all_fonts()`, чтобы получить доступные объекты Font, и перебрать результаты, чтобы прочитать имена шрифтов для анализа, аудита или рабочих процессов обработки документов.
---

Используйте [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), чтобы открыть PDF, и вызовите `font_utilities.get_all_fonts()`, чтобы получить все объекты [Font](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/font/), на которые ссылается документ. Это полезно при аудите встроенных шрифтов, проверке доступности шрифтов перед конвертацией или анализе ресурсов документа.

1. Откройте исходный PDF как `Document`.
1. Вызовите `document.font_utilities.get_all_fonts()`, чтобы получить коллекцию шрифтов.
1. Переберите возвращённые объекты `Font`.
1. Прочитайте и выведите каждое значение `font.font_name`.

```python

    import aspose.pdf as apdf
    from os import path

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    fonts = document.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```
