---
title: 在Python中拆分PDF文件
linktitle: 拆分PDF文件
type: docs
weight: 60
url: /zh/python-net/split-pdf-document/
description: 了解如何在 Python 中将 PDF 文件拆分为单独页面、等分部分、固定大小的分组、自定义页面范围以及奇数或偶数页。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 将 PDF 拆分为页面和页面范围
Abstract: 本文展示了如何使用 Aspose.PDF for Python via .NET 对 PDF 文件进行拆分。它涵盖了将 PDF 拆分为单独页面、两个相等部分、固定大小的页面组、自定义页面范围、具名页面组、稳定的文件名，以及奇数页或偶数页文件。
---

此页面展示了如何使用 Aspose.PDF for Python via .NET **在 Python 中拆分 PDF 文件**。

当您需要将大型PDF拆分为单页文件、等分部分、固定大小的组、自定义页范围，或奇偶页集合，以进行分发、审阅或下游处理时，请使用这些示例。

## 在线拆分 PDF 示例

[Aspose.PDF 拆分器](https://products.aspose.app/pdf/splitter) 是一个在线网页应用程序，可让您测试 PDF 拆分功能。

[![Aspose 拆分 PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

在 Python 中将 PDF 页面拆分为单页 PDF 文件，请按以下步骤操作：

1. 循环遍历 PDF 文档的页面 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的 [页面集合](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 集合
1. 对于每次迭代，创建一个新的 Document 对象并添加单个 [页面](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 对象放入空文档
1. 使用以下方法保存新 PDF [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法

## 在 Python 中将 PDF 拆分为多个文件

以下 Python 代码片段展示了如何将 PDF 页面拆分为单独的 PDF 文件。

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents(infile, outdir):
    document = ap.Document(infile)
    for page_num in range(1, len(document.pages) + 1):
        with ap.Document() as new_document:
            new_document.pages.add(document.pages[page_num])
            new_document.save(path.join(outdir, f"Page_{page_num}.pdf"))
```

## 将 PDF 拆分为两个等分

1. 加载 PDF 文档。
1. 确定总页数。
1. 计算中点。
1. 创建第一个输出文档。
1. 从第一个文档中删除后半部分的页面。
1. 保存第一部分。
1. 创建第二个输出文档。
1. 删除第二个文档的前半页。
1. 保存第二部分。

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_into_two_parts(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    mid_point = total_pages // 2

    # First part
    with ap.Document(infile) as first_document:
        first_part_range = range(mid_point + 1, total_pages + 1)
        first_document.pages.delete(first_part_range)
        first_document.save(path.join(outdir, "Part_1.pdf"))

    # Second part
    with ap.Document(infile) as second_document:
        second_part_range = range(1, mid_point + 1)
        second_document.pages.delete(second_part_range)
        second_document.save(path.join(outdir, "Part_2.pdf"))
```

## 将 PDF 拆分为每 N 页的多个文件

使用 Aspose.PDF for Python 将 PDF 文档按固定页数拆分为多个较小的文件。

1. 加载 PDF 文档。
1. 确定总页数。
1. 为每个部分定义页数。
1. 逐块遍历文档。
1. 计算每个部分的页面范围。
1. 为每个部分创建一个新文档。
1. 将页面复制到新文档中。
1. 保存拆分文档。
1. 重复执行，直到所有页面都处理完。

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_every_n_pages(infile, outdir, pages_per_part=3):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    part_index = 1
    for start_page in range(1, total_pages + 1, pages_per_part):
        end_page = min(start_page + pages_per_part - 1, total_pages)

        with ap.Document() as part_document:
            for page_num in range(start_page, end_page + 1):
                part_document.pages.add(document.pages[page_num])
            part_document.save(
                path.join(outdir, f"Every_{pages_per_part}_Part_{part_index}.pdf")
            )

        part_index += 1
```

## 按自定义页面范围拆分 PDF

使用 Aspose.PDF for Python 将 PDF 文档根据自定义页面范围拆分为多个文件。

1. 加载 PDF 文档。
1. 确定总页数。
1. 创建一个元组列表，表示 (start_page, end_page) 范围。
1. 遍历已定义的范围。
1. 验证起始页。
1. 调整结束页。
1. 验证有效范围。
1. 为每个范围创建一个新文档。
1. 将页面复制到新文档中。
1. 保存每个拆分的文档。

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_by_page_ranges(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    # Define ranges as (start_page, end_page). Use None to indicate last page.
    ranges = [(1, 3), (4, 6), (7, None)]

    for index, (start_page, end_page) in enumerate(ranges, start=1):
        if start_page > total_pages:
            continue

        effective_end = total_pages if end_page is None else min(end_page, total_pages)
        if start_page > effective_end:
            continue

        with ap.Document() as range_document:
            for page_num in range(start_page, effective_end + 1):
                range_document.pages.add(document.pages[page_num])
            range_document.save(
                path.join(outdir, f"Range_{index}_{start_page}_to_{effective_end}.pdf")
            )
```

## 将 PDF 拆分为第一页和剩余页面

使用 Aspose.PDF for Python 将 PDF 文档的第一页与其余页面分离。

1. 加载 PDF 文档。
1. 确定总页数。
1. 检查文档是否为空。
1. 为第一页创建文档。
1. 添加第一页。
1. 保存第一页文档。
1. 检查是否有其他页面。
1. 为剩余页面创建文档。
1. 复制剩余的页面。
1. 保存剩余页面的文档。

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_first_page_and_rest(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    with ap.Document() as first_page_document:
        first_page_document.pages.add(document.pages[1])
        first_page_document.save(path.join(outdir, "First_Page.pdf"))

    if total_pages == 1:
        return

    with ap.Document() as remaining_pages_document:
        for page_num in range(2, total_pages + 1):
            remaining_pages_document.pages.add(document.pages[page_num])
        remaining_pages_document.save(path.join(outdir, "Remaining_Pages.pdf"))
```

## 将 PDF 拆分为最后一页和前面的页面

使用 Aspose.PDF for Python 提取 PDF 文档的最后一页，并将其从其余页面中分离。

1. 加载 PDF 文档。
1. 确定总页数。
1. 检查文档是否为空。
1. 为最后一页创建文档。
1. 添加最后一页。
1. 保存最后一页文档。
1. 检查单页文档。
1. 从原始文档中删除最后一页。
1. 保存剩余的页面。

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_last_page_and_rest(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    with ap.Document() as last_page_document:
        last_page_document.pages.add(document.pages[total_pages])
        last_page_document.save(path.join(outdir, "Last_Page.pdf"))

    if total_pages == 1:
        return

    document.pages.delete(total_pages)  # Remove last page from original document
    document.save(path.join(outdir, "Previous_Pages.pdf"))
```

## 将 PDF 拆分为三部分

使用 Aspose.PDF for Python 将 PDF 文档拆分为三个独立部分。

1. 加载 PDF 文档。
1. 确定总页数。
1. 检查文档是否为空。
1. 计算部件大小。
1. 遍历三个部分。
1. 确定每个部分的页码范围。
1. 验证页面范围。
1. 为每个部分创建一个新文档。
1. 将页面复制到部件文档中。
1. 保存每个部分。

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_into_three_parts(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    part_size = max(1, (total_pages + 2) // 3)

    for part_index in range(3):
        start_page = part_index * part_size + 1
        end_page = min((part_index + 1) * part_size, total_pages)

        if start_page > total_pages:
            break

        with ap.Document() as part_document:
            for page_num in range(start_page, end_page + 1):
                part_document.pages.add(document.pages[page_num])
            part_document.save(path.join(outdir, f"Three_Parts_{part_index + 1}.pdf"))
```

## 自定义 PDF 页面拆分器

使用 Aspose.PDF for Python 将 PDF 文档拆分为多个文件，依据自定义的页面分组。

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_custom_page_groups(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    groups = [
        [1, 2, 5],
        [3, 4, 6, 7],
    ]

    for group_index, group in enumerate(groups, start=1):
        valid_pages = [page_num for page_num in group if 1 <= page_num <= total_pages]
        if not valid_pages:
            continue

        with ap.Document() as group_document:
            for page_num in valid_pages:
                group_document.pages.add(document.pages[page_num])
            group_document.save(path.join(outdir, f"Custom_Group_{group_index}.pdf"))
```

## 将 PDF 拆分为单独页面并使用稳定的文件名

使用 Aspose.PDF for Python 将 PDF 文档拆分为单独的页面，并使用稳定的文件名保存它们。

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_with_stable_filenames(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    for page_num in range(1, total_pages + 1):
        with ap.Document() as new_document:
            new_document.pages.add(document.pages[page_num])
            new_document.save(path.join(outdir, f"Page_{page_num:03d}.pdf"))
```

## 将 PDF 拆分为奇数页和偶数页

使用 Aspose.PDF for Python 将 PDF 文档拆分为两个独立的文件，分别包含奇数页和偶数页。

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_odd_even_pages(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    # Odd pages document
    with ap.Document(infile) as document:
        with ap.Document() as odd_document:
            for page_num in range(1, total_pages + 1, 2):
                odd_document.pages.add(document.pages[page_num])
            odd_document.save(path.join(outdir, "Odd_Pages.pdf"))

        with ap.Document() as even_document:
            for page_num in range(2, total_pages + 1, 2):
                even_document.pages.add(document.pages[page_num])
            even_document.save(path.join(outdir, "Even_Pages.pdf"))
```

## 相关文档主题

- [使用 Python 处理 PDF 文档](/pdf/zh/python-net/working-with-documents/)
- [在 Python 中合并 PDF 文件](/pdf/zh/python-net/merge-pdf-documents/)
- [在 Python 中优化 PDF 文件](/pdf/zh/python-net/optimize-pdf/)
- [在 Python 中操作 PDF 文档](/pdf/zh/python-net/manipulate-pdf-document/)

