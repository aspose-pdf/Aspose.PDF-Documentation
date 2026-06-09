---
title: 在 Python 中为 PDF 添加贝茨编号
linktitle: 添加贝茨编号
type: docs
weight: 10
url: /zh/python-net/add-bates-numbering/
description: 了解如何使用 Python 通过 Aspose.PDF for Python via .NET 在 PDF 文档中添加和删除贝茨编号。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 通过 Python 添加贝茨编号
Abstract: Bates numbering 是法律、医疗和商业文档工作流中的关键功能，确保一组中的每页都获得唯一的、顺序的标识符，以便可靠引用。本文演示了 Aspose.PDF for Python via .NET 如何通过其灵活的 API 简化 Bates 编号的自动化。使用 BatesNArtifact 类，开发者可以配置编号行为——包括数字位数、前缀、后缀、对齐方式和页边距——并在整个文档中以编程方式应用。本文提供了多种方法，从直接应用工件到基于委托的配置，提供静态和动态两种控制方式。此外，API 支持通过一次方法调用即可完整移除 Bates 编号，实现分页工件的全生命周期管理。清晰的分步代码示例展示了如何添加、定制和删除 Bates 编号，使本指南成为希望简化文档处理工作流的开发者的实用资源。
---

Bates 编号广泛用于法律、医疗和商务工作流中，为文档集中的页面分配唯一的、顺序的标识符。Aspose.PDF for Python via .NET 提供了简洁且灵活的 API 来自动化此过程，使您能够以编程方式在任何 PDF 上应用标准化的 Bates 编号。

使用 [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) 类，开发者可以完全自定义编号行为——包括起始号码、位数、前缀和后缀、对齐方式以及边距。配置完成后，artifact 可以应用于 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 通过 `add_bates_numbering` 方法 在 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 或作为列表的一部分添加 [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/) objects. Aspose.PDF 也支持基于委托的配置风格，允许在运行时动态控制工件设置。

除了创建 Bates 编号之外，API 还提供了一种简便的方法来删除它们 `delete_bates_numbering`，在文档处理工作流中提供完全的灵活性。

本文展示了使用 Aspose.PDF for Python via .NET 在 PDF 中添加和删除 Bates 编号的多种方法，并提供了关于工件配置、应用和移除的清晰示例。

## 添加 Bates 编号工件

此示例演示如何使用 Aspose.PDF for Python via .NET 以编程方式向 PDF 文档添加 Bates 编号。通过配置一个 [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) 使用所需的设置并将其应用于文档的页面，您可以实现自动化，为每页添加标准化标识符的过程。

要向一个 Bates 编号工件添加 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)，调用 `AddBatesNumbering(BatesNArtifact)` 扩展方法 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)，传入一个 [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) 实例作为参数：

```python
import sys
from os import path
import aspose.pdf as ap

def _create_bates_artifact():
    """Create a Bates numbering artifact with default settings."""
    artifact = ap.BatesNArtifact()
    artifact.start_page = 1
    artifact.end_page = 0
    artifact.subset = ap.Subset.ALL
    artifact.number_of_digits = 6
    artifact.start_number = 1
    artifact.prefix = ""
    artifact.suffix = ""
    artifact.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
    artifact.right_margin = 72
    artifact.left_margin = 72
    artifact.top_margin = 36
    artifact.bottom_margin = 36
    return artifact
```

```python
import sys
from os import path
import aspose.pdf as ap

def add_bates_n_artifact(infile, outfile):
    """Add Bates numbering artifact to a PDF document."""
    with ap.Document(infile) as document:
        for _ in range(2):
            document.pages.add()

        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_bates_numbering(document.pages, bates_artifact)
        document.save(outfile)
```

## 使用分页工件添加贝茨编号

使用 Aspose.PDF for Python 中的分页工件集合为 PDF 添加贝茨编号：

1. 加载 PDF 文档。
1. 在应用页码之前，如有需要插入额外的页面。
1. 创建一个 Bates 工件。
1. 配置工件属性。
1. 将该工件添加到分页集合中。
1. 对页面应用分页。
1. 保存更新后的文档。

```python
import sys
from os import path
import aspose.pdf as ap

def add_bates_n_artifact_pagination(infile, outfile):
    """Add Bates numbering using pagination artifacts collection."""
    with ap.Document(infile) as document:
        for _ in range(2):
            document.pages.add()

        bates_artifact = _create_bates_artifact()
        ap.PageCollectionExtensions.add_pagination(document.pages, [bates_artifact])
        document.save(outfile)
```

## 删除 Bates 编号

要从 a 中删除 Bates 编号 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)，使用 `delete_bates_numbering()` 方法 在 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/):

```python
import sys
from os import path
import aspose.pdf as ap

def delete_bates_numbering(infile, outfile):
    """Delete Bates numbering from a PDF document."""
    with ap.Document(infile) as document:
        ap.PageCollectionExtensions.delete_bates_numbering(document.pages)
        document.save(outfile)
```

## 相关工件主题

- [在 Python 中使用 PDF 工件](/pdf/zh/python-net/artifacts/)
- [在 Python 中为 PDF 添加水印](/pdf/zh/python-net/add-watermarks/)
- [在 Python 中添加 PDF 背景](/pdf/zh/python-net/add-backgrounds/)
- [统计 PDF 文件中的工件类型](/pdf/zh/python-net/counting-artifacts/)