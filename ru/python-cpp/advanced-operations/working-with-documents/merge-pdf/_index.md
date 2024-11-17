---
title: Как объединить PDF с использованием Python через C++
linktitle: Объединение PDF файлов
type: docs
weight: 10
url: /ru/python-cpp/merge-pdf-documents/
description: Эта страница объясняет, как объединить PDF документы в один файл PDF с помощью Python.
lastmod: "2024-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Объединение или комбинирование нескольких PDF в один PDF с использованием Python через C++

Используя Python и библиотеку C++ от Aspose, вы можете эффективно объединять несколько PDF файлов в один PDF с легкостью.

Чтобы объединить два PDF файла:

1. Откройте первый документ
1. Затем добавьте страницы второго документа к первому
1. Сохраните объединенный файл, используя метод 'document.save'.

Следующий фрагмент кода показывает, как объединить PDF файлы.

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    dataDir = os.path.join(os.getcwd(), "samples")
    input_file = os.path.join(dataDir , "sample0.pdf")
    output_file = os.path.join(dataDir , "results", "concatenated-files.pdf")

    # Открыть первый документ
    document1 = apw.Document(inputFile)
    document2 = apw.Document(inputFile)

    # Добавить страницы второго документа к первому
    document1.pages.add(document2.pages)

    # Сохранить объединенный файл
    document1.save(output_file)
```