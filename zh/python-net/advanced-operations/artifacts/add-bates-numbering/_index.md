---
title: 在 Python via .NET 中添加 Bates 编号工件
linktitle: 添加 Bates 编号
type: docs
weight: 10
url: /zh/python-net/add-bates-numbering/
description: Aspose.PDF for Python via .NET 允许您向 PDF 添加 Bates 编号。
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 通过 Python 添加 Bates 编号
Abstract: Bates 编号是法律、医疗和商业文档工作流中的关键功能，确保集合中的每页都获得唯一的顺序标识，以便可靠引用。本文演示了 Aspose.PDF for Python via .NET 如何通过其灵活的 API 简化 Bates 编号的自动化。使用 BatesNArtifact 类，开发者可以配置编号行为——包括位数、前缀、后缀、对齐方式和边距——并在整个文档中以编程方式应用。本文提供了多种方法，从直接应用工件到基于委托的配置，提供静态和动态控制。除此之外，API 还支持通过单一方法调用完整删除 Bates 编号，实现分页工件的全生命周期管理。清晰的分步代码示例展示了如何添加、定制和删除 Bates 编号，使本指南成为开发者简化文档处理工作流的实用资源。
---

Bates 编号在法律、医疗和商业工作流中被广泛使用，以为文档集合中的页面分配唯一的顺序标识符。Aspose.PDF for Python via .NET 提供了简洁且灵活的 API 来自动化此过程，使您能够在任何 PDF 上以编程方式应用标准化的 Bates 编号。

使用 [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) 类，开发者可以全面自定义编号行为——包括起始号码、位数、前缀和后缀、对齐方式以及边距。配置完成后，可通过 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 上的 `add_bates_numbering` 方法，将该工件应用于 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)，或将其作为 [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/) 对象列表的一部分添加。Aspose.PDF 还支持基于委托的配置方式，允许运行时动态控制工件设置。

除了创建 Bates 编号外，API 还提供了使用 `delete_bates_numbering` 删除编号的简便方法，为文档处理工作流提供了完全的灵活性。

本文展示了使用 Aspose.PDF for Python via .NET 在 PDF 中添加和删除 Bates 编号的多种方法，并提供了工件配置、应用和移除的清晰示例。

## 添加 Bates 编号工件

本示例展示了如何使用 Aspose.PDF for Python via .NET 以编程方式向 PDF 文档添加 Bates 编号。通过配置具有所需设置的 [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) 并将其应用于文档的页面，您可以自动化向每页添加标准化标识符的过程。

要向 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 添加 Bates 编号工件，请在 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 上调用 `AddBatesNumbering(BatesNArtifact)` 扩展方法，并将一个 [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) 实例作为参数传入：

```python

import aspose.pdf as ap

def add_bates_numbering(path_outfile):
    # Create a new or empty PDF document
    with ap.Document() as document:

        # Add 10 blank pages
        for _ in range(10):
            document.pages.add()

        # Create Bates numbering artifact
        bates = ap.BatesNArtifact(
            start_page=1,
            end_page=0,  # 0 = apply until last page
            subset=ap.Subset.ALL,
            number_of_digits=6,
            start_number=1,
            prefix="",
            suffix="",
            artifact_vertical_alignment=ap.VerticalAlignment.BOTTOM,
            artifact_horizontal_alignment=ap.HorizontalAlignment.RIGHT,
            right_margin=72,
            left_margin=72,
            top_margin=36,
            bottom_margin=36
        )

        # Add Bates numbering to all pages
        document.pages.add_bates_numbering(bates)

        # Save the resulting PDF
        document.save(path_outfile)
```

或者，您可以传入一个由 [`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/) 对象组成的集合：

```python

import aspose.pdf as ap

def add_bates_numbering_collection(path_outfile):
    with ap.Document() as document:

        # Add 10 pages
        for _ in range(10):
            document.pages.add()

        # Create Bates artifact
        bates = ap.BatesNArtifact(
            start_page=1,
            end_page=0,
            subset=ap.Subset.ALL,
            number_of_digits=6,
            start_number=1,
            prefix="",
            suffix="",
            artifact_vertical_alignment=ap.VerticalAlignment.BOTTOM,
            artifact_horizontal_alignment=ap.HorizontalAlignment.RIGHT,
            right_margin=72,
            left_margin=72,
            top_margin=36,
            bottom_margin=36
        )

        # Add as a pagination artifact list
        document.pages.add_pagination([bates])

        # Save document
        document.save(path_outfile)
```

使用动作委托添加 Bates 编号工件：

```python

import aspose.pdf as ap

def add_bates_numbering_delegate(path_outfile):
    def configure_bates(b):
        """Configure Bates numbering artifact with desired settings."""
        b.start_page = 1
        b.end_page = 0
        b.subset = ap.Subset.ALL
        b.number_of_digits = 6
        b.start_number = 1
        b.prefix = ""
        b.suffix = ""
        b.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
        b.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
        b.right_margin = 72
        b.left_margin = 72
        b.top_margin = 36
        b.bottom_margin = 36
        b.text_state.font_size = 10
    
    with ap.Document() as document:

        # Add 10 pages
        for _ in range(10):
            document.pages.add()

        # Use delegate function to configure Bates artifact
        document.pages.add_bates_numbering(configure_bates)

        # Save output PDF
        document.save(path_outfile)
```

## 删除 Bates 编号

要从 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 中删除 Bates 编号，请在 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 上使用 `delete_bates_numbering()` 方法：

```python

import aspose.pdf as ap

def delete_bates_numbering(path_infile, path_outfile):
    with ap.Document(path_infile) as document:

        # Remove Bates numbering from all pages
        document.pages.delete_bates_numbering()

        # Save updated document
        document.save(path_outfile)
```
