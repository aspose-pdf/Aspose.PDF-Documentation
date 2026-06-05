---
title: Конвертировать PDF в PowerPoint на Python
linktitle: Конвертировать PDF в PowerPoint
type: docs
weight: 30
url: /ru/python-net/convert-pdf-to-powerpoint/
description: Узнайте, как конвертировать PDF в PowerPoint на Python, включая PDF в PPTX, слайды в виде изображений и пользовательское разрешение изображений с помощью Aspose.PDF.
lastmod: "2026-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Конвертировать PDF в слайды PowerPoint PPTX на Python
Abstract: В этой статье показано, как преобразовать PDF‑файлы в презентации PowerPoint с помощью Aspose.PDF for Python via .NET. Рассмотрены преобразование PDF в PPTX, преобразование слайдов в изображения и настройка разрешения изображений для вывода презентации.
---

## Конвертировать PDF в PowerPoint на Python

**Aspose.PDF for Python via .NET** позволяет преобразовывать PDF‑файлы в презентации PowerPoint PPTX из кода Python.

Используйте этот рабочий процесс, когда необходимо переиспользовать PDF‑отчёты, наборы слайдов, брошюры или раздаточные материалы в виде файлов PowerPoint. При конвертации отдельные страницы PDF преобразуются в отдельные слайды в файле PPTX.

Во время преобразования PDF в PPTX текст может быть отрендерен как выделяемый текст, который можно обновлять в PowerPoint. Чтобы преобразовать PDF‑файлы в формат PPTX, Aspose.PDF предоставляет the [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) класс. Передайте a `PptxSaveOptions` объект в качестве второго аргумента к [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) методу.

## Конвертировать PDF в PPTX с помощью Python

Для конвертации PDF в PPTX используйте следующие шаги кода.

Шаги: Конвертировать PDF в PowerPoint с помощью Python

1. Создайте экземпляр [Документ](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) класс.
1. Создайте экземпляр [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) класс.
1. Вызовите [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) методу.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    document.save(outfile, save_options)
```

## Конвертировать PDF в PPTX со слайдами в виде изображений

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в PowerPoint онлайн**

Aspose.PDF предоставляет онлайн ["PDF в PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx) приложение, в котором вы можете проверить качество конвертации.


[![Конвертация Aspose.PDF PDF в PPTX с приложением](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

Если вам нужно преобразовать поисковый PDF в PPTX в виде изображений вместо выделяемого текста, Aspose.PDF предоставляет такую возможность через [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) класс. Чтобы достичь этого, установите свойство [slides_as_images](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) из [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) class в 'true', как показано в следующем примере кода.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX_slides_as_images(infile, outfile):

    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    save_options.slides_as_images = True

    document.save(outfile, save_options)
```

## Конвертировать PDF в PPTX с пользовательским разрешением изображений

Этот метод конвертирует PDF‑документ в файл PowerPoint (PPTX), задавая пользовательское разрешение изображения (300 DPI) для улучшенного качества.

1. Загрузите PDF в объект 'ap.Document'.
1. Создайте экземпляр 'PptxSaveOptions'.
1. Установите свойство 'image_resolution' в значение 300 DPI для рендеринга высокого качества.
1. Сохраните PDF как файл PPTX, используя определённые параметры сохранения.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PPTX_image_resolution(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.PptxSaveOptions()
    save_options.image_resolution = 300

    document.save(outfile, save_options)
```

## Связанные преобразования

- [Конвертировать PDF в Word](/pdf/ru/python-net/convert-pdf-to-word/) для получения редактируемого вывода документа вместо слайдов.
- [Конвертировать PDF в Excel](/pdf/ru/python-net/convert-pdf-to-excel/) когда исходный PDF содержит бизнес-данные, насыщенные таблицами.
- [Преобразовать PDF в HTML](/pdf/ru/python-net/convert-pdf-to-html/) для публикационных процессов, готовых к работе в браузере.
