---
title: Преобразование PDF в текст на Python
linktitle: Преобразование PDF в другие форматы
type: docs
weight: 90
url: /ru/python-cpp/convert-pdf-to-other-files/
lastmod: "2022-12-23"
description: Эта тема показывает, как преобразовать PDF файл в другие форматы файлов, такие как текст, используя Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Преобразование PDF в текст

**Aspose.PDF for Python** поддерживает преобразование всего PDF документа и отдельной страницы в текстовый файл.

### Преобразование PDF документа в текстовый файл

Вы можете преобразовать PDF документ в TXT файл, используя класс 'TextDevice'.

1. Создание путей к входному и выходному файлам
1. Создание экземпляра фасада извлечения PDF с помощью [extractor_create](https://reference.aspose.com/pdf/python-cpp/core/extractor_create/)
1. Привязка PDF файла к извлекателю с помощью [extractor_bind_pdf](https://reference.aspose.com/pdf/python-cpp/core/extractor_bind_pdf/)

1. Извлечение текста из PDF-файла с использованием [extractor_extract_text](https://reference.aspose.com/pdf/python-cpp/core/extractor_extract_text/)
1. Запись извлеченного текста в выходной файл
1. Сохранение выходного PDF с методом 'document.save'.

Следующий фрагмент кода объясняет, как извлечь текст со всех страниц.

```python

    from AsposePdfPython import *

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_txt.txt"

    extactor = extractor_create()
    extractor_bind_pdf(extactor,input_pdf)
    text = extractor_extract_text(extactor)

    with open(output_pdf, 'w') as f:
        f.write(text)
```