---
title: 使用 Python 删除 PDF 文件中的图像
linktitle: 删除图像
type: docs
weight: 20
url: /zh/python-net/delete-images-from-pdf-file/
description: 了解如何在 Python 中从 PDF 文件中删除特定图像或全部图像。
lastmod: "2026-06-08"
TechArticle: true
AlternativeHeadline: 使用 Python 删除 PDF 文件中的图像
Abstract: 本文展示了如何使用 Aspose.PDF for Python via .NET 从 PDF 文档中删除图像。它涵盖了删除特定图像资源以及从选定页面删除所有图像的操作。
---

当您需要删除不必要的图形、减小 PDF 大小或清除文档中敏感的视觉内容时，请使用此页面。

## 从 PDF 文件中删除图像

使用以下步骤从页面中删除单个图像：

1. 使用加载源 PDF `ap.Document(infile)`.
1. 选择页面和图像资源索引。
1. 删除图像 `resources.images.delete(index)`.
1. 保存更新后的 PDF。

```python
import aspose.pdf as ap


def delete_image(infile, outfile):
    document = ap.Document(infile)
    document.pages[1].resources.images.delete(1)
    document.save(outfile)
```

## 删除页面上的所有图像

使用此示例从特定页面中删除所有图像。

```python
import aspose.pdf as ap


def delete_all_images_from_page(infile, outfile, page_number):
    document = ap.Document(infile)
    page = document.pages[page_number]

    while len(page.resources.images) != 0:
        page.resources.images.delete(1)

    document.save(outfile)
```

## 相关图像主题

- [使用 Python 处理 PDF 中的图像](/pdf/zh/python-net/working-with-images/)
- [替换现有 PDF 文件中的图像](/pdf/zh/python-net/replace-image-in-existing-pdf-file/)
- [从 PDF 文件中提取图像](/pdf/zh/python-net/extract-images-from-pdf-file/)
- [向现有 PDF 文件添加图像](/pdf/zh/python-net/add-image-to-existing-pdf-file/)