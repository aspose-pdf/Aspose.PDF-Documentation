---
title: Установка размера PDF с использованием Python через C++
linktitle: Установка размера PDF
type: docs
weight: 30
url: /python-cpp/get-and-set-page-properties/
description: Этот раздел показывает, как получить или установить свойства страницы PDF, такие как размер документа, с использованием Python через C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Установка размера PDF файла

Aspose.PDF для Python через C++ позволяет вам читать и устанавливать свойства страниц в PDF файле в ваших Python приложениях.

Следующий фрагмент кода открывает PDF файл, изменяет размер первой страницы, регулируя **Область обрезки** (область обрезки - это размер "страницы", при котором ваш PDF документ отображается в Adobe Acrobat), и сохраняет измененный документ в новый файл.

1. Создайте объект документа из входного файла
1. Получите коллекцию страниц из документа, используя [document_get_pages](https://reference.aspose.com/pdf/python-cpp/core/document_get_pages/)

1. Получите первую страницу из коллекции страниц с помощью [page_collection_get_page](https://reference.aspose.com/pdf/python-cpp/core/page_collection_get_page/)
1. Получите прямоугольник обрезки со страницы, используя [page_get_rectangle](https://reference.aspose.com/pdf/python-cpp/core/page_get_rectangle/)
1. Рассчитайте новые координаты для обрезки
1. Обновите координаты обрезки с новыми значениями
1. Сохраните измененный документ в выходной файл с помощью метода 'document.save'

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # Получите текущий рабочий каталог и создайте путь к директории "samples"
    dataDir = os.path.join(os.getcwd(), "samples")

    # Создайте пути для входного и выходного файлов
    input_file = os.path.join(dataDir, "sample0.pdf")
    output_file = os.path.join(dataDir, "results", "resized_document.pdf")

    # Создайте объект документа из входного файла
    doc = apCore.document_create_from_file(inputFile)

    # Получите коллекцию страниц из документа
    pages = apCore.document_get_pages(doc)

    # Получите первую страницу из коллекции страниц
    page = apCore.page_collection_get_page(pages, 1)

    # Получите прямоугольник обрезки со страницы
    crop_box = apCore.page_get_rectangle(page)

    # Рассчитайте новые координаты для обрезки
    LLX = apCore.rectangle_get_LLX(crop_box) + 10
    LLY = apCore.rectangle_get_LLY(crop_box) + 10
    URX = apCore.rectangle_get_URX(crop_box) - 10
    URY = apCore.rectangle_get_URY(crop_box) - 10

    # Обновите координаты обрезки с новыми значениями
    apCore.rectangle_set_LLX(crop_box, LLX)
    apCore.rectangle_set_LLY(crop_box, LLY)
    apCore.rectangle_set_URX(crop_box, URX)
    apCore.rectangle_set_URY(crop_box, URY)

    # Сохраните измененный документ в выходной файл
    apCore.document_save(doc, output_file)

    # Закройте дескриптор документа
    apCore.close_handle(doc)
```