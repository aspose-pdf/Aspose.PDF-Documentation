---
title: Извлечение изображений из PDF с помощью Python
linktitle: Извлечение изображений из PDF
type: docs
weight: 20
url: /ru/python-net/extract-images-from-the-pdf-file/
description: Как извлечь часть изображения из PDF с помощью Aspose.PDF для Python
lastmod: "2023-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как извлечь изображения из PDF через Python
Abstract: Эта статья предоставляет краткое руководство по извлечению вложенных изображений из PDF‑документа с помощью Python. Процесс включает три основных шага — загрузку PDF‑документа, доступ к ресурсу изображения и сохранение изображения в файл. Фрагмент кода использует библиотеку Aspose.PDF для выполнения этих операций. Сначала PDF‑документ загружается из указанного пути, затем нужное изображение извлекается из ресурсов первой страницы. Наконец, изображение сохраняется в указанный выходной файл с помощью операции ввода‑вывода файла, что позволяет проводить дальнейший анализ, редактирование или повторное использование в других документах.
---

Этот фрагмент кода извлекает вложенные изображения из PDF‑документа для отдельного анализа, редактирования или повторного использования в других документах:

1. Загрузка PDF‑документа
1. Доступ к ресурсу изображения
1. Сохранение изображения в файл

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```

