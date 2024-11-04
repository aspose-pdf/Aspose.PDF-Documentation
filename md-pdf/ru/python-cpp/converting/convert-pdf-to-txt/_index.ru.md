---
title: Конвертация PDF в TXT на Python
linktitle: Конвертация PDF в TXT
type: docs
weight: 20
url: /python-cpp/convert-pdf-to-txt/
lastmod: "2024-04-23"
description: Aspose.PDF for Python via C++ позволяет конвертировать PDF в формат TXT с использованием Python.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Конвертация PDF в TXT

Aspose.PDF for Python via C++ поддерживает конвертацию PDF документа в текстовый файл, следуя следующим шагам:

1. Создание пути для входного и выходного файла
1. Создание экземпляра фасада извлечения PDF с помощью [extractor_create](https://reference.aspose.com/pdf/python-cpp/core/extractor_create/)
1. Привязка PDF файла к извлекателю с помощью [extractor_bind_pdf](https://reference.aspose.com/pdf/python-cpp/core/extractor_bind_pdf/)
1. Извлечение текста из PDF файла с помощью [extractor_extract_text](https://reference.aspose.com/pdf/python-cpp/core/extractor_extract_text/)
1. Запись извлеченного текста в выходной файл
1. Сохранение выходного PDF с методом 'document.save'.

Пример кода ниже показывает, как конвертировать изображение JPG в PDF с помощью Python через C++:

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # Создание пути к каталогу данных
    dataDir = os.path.join(os.getcwd(), "samples")

    # Создание пути к входному файлу
    input_file = os.path.join(dataDir, "sample.pdf")

    # Создание пути к выходному файлу
    output_file = os.path.join(dataDir, "results", "pdf-to-txt.txt")

    # Создание экземпляра фасада извлечения PDF
    extactor = apCore.facades_pdf_extractor_create()

    # Привязка PDF файла к извлекателю
    apCore.facades_facade_bind_pdf(extactor, input_file)

    # Извлечение текста из PDF файла
    text = apCore.facades_pdf_extractor_extract_text(extactor)

    # Запись извлеченного текста в выходной файл
    with open(output_file, 'w') as f:
        f.write(text)
```