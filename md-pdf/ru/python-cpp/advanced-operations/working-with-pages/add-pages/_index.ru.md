---
title: Добавить Страницы в PDF с помощью Python и C++
linktitle: Добавить Страницы
type: docs
weight: 10
url: /python-cpp/add-pages/
description: Эта статья обучает, как вставить (добавить) страницу в нужное место PDF файла в Python с использованием C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Вставить Пустую Страницу в PDF Файл в Желательное Место

Этот фрагмент кода открывает PDF документ, добавляет в него пустую страницу и сохраняет измененный документ как новый PDF файл.

Чтобы вставить пустую страницу в PDF файл:

1. Откройте PDF документ
1. Добавьте новую пустую страницу в документ
1. Сохраните измененный документ в выходной файл с помощью метода 'document.save'

Следующий фрагмент кода показывает, как вставить страницу в PDF файл:

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # Установите путь к каталогу, где находятся образцы PDF файлов
    dataDir = os.path.join(os.getcwd(), "samples")

    # Установите путь к входному файлу
    input_file = os.path.join(dataDir, "sample0.pdf")

    # Установите путь к выходному файлу
    output_file = os.path.join(dataDir, "results", "blank_pdf_document.pdf")

    # Откройте PDF документ
    document = apw.Document(input_file)

    # Добавьте новую пустую страницу в документ
    document.pages.add()

    # Сохраните измененный документ в выходной файл
    document.save(output_file)
```