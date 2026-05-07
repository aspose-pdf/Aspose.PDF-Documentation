---
title: Удалить изображения из PDF‑файла с помощью Python
linktitle: Удалить изображения
type: docs
weight: 20
url: /python-net/delete-images-from-pdf-file/
description: Узнайте, как удалить конкретные или все изображения из PDF‑файлов с помощью Python.
lastmod: "2026-05-05"
TechArticle: true
AlternativeHeadline: Удалить изображения из PDF‑файлов с помощью Python
Abstract: В этой статье показано, как удалять изображения из PDF‑документов с помощью Aspose.PDF for Python via .NET. Описывается удаление конкретного ресурса изображения и удаление всех изображений с выбранной страницы.
---

Используйте эту страницу, когда нужно удалить ненужную графику, уменьшить размер PDF или очистить конфиденциальный визуальный контент из документа.

## Удалить изображения из PDF‑файла

Выполните следующие шаги, чтобы удалить одно изображение со страницы:

1. Загрузите исходный PDF с помощью `ap.Document(infile)`.
1. Выберите страницу и индекс ресурса изображения.
1. Удалите изображение с `resources.images.delete(index)`.
1. Сохраните обновлённый PDF.

```python
import aspose.pdf as ap


def delete_image(infile, outfile):
    document = ap.Document(infile)
    document.pages[1].resources.images.delete(1)
    document.save(outfile)
```

## Удалить все изображения со страницы

Используйте этот пример, чтобы удалить каждое изображение с конкретной страницы.

```python
import aspose.pdf as ap


def delete_all_images_from_page(infile, outfile, page_number):
    document = ap.Document(infile)
    page = document.pages[page_number]

    while len(page.resources.images) != 0:
        page.resources.images.delete(1)

    document.save(outfile)
```

## Связанные темы изображений

- [Работа с изображениями в PDF с использованием Python](/pdf/ru/python-net/working-with-images/)
- [Замена изображений в существующих PDF‑файлах](/pdf/ru/python-net/replace-image-in-existing-pdf-file/)
- [Извлечение изображений из PDF‑файлов](/pdf/ru/python-net/extract-images-from-pdf-file/)
- [Добавление изображений в существующие PDF‑файлы](/pdf/ru/python-net/add-image-to-existing-pdf-file/)