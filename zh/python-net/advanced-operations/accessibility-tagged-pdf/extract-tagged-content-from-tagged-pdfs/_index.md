---
title: 在 Python 中从 PDF 中提取带标签的内容
linktitle: 提取带标签的内容
type: docs
weight: 20
url: /zh/python-net/extract-tagged-content-from-tagged-pdfs/
description: 学习如何通过 .NET 使用 Aspose.PDF for Python 在 Python 中提取带标签的 PDF 内容，包括访问带标签的内容、根结构和子结构元素。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

在本文中，您将学习如何使用 Python 从 PDF 文档中提取带标签的内容。

当您需要检查带标签的 PDF、阅读逻辑结构树或验证结构元素是否为无障碍工作流程正确创建时，请使用这些示例。

## 获取带标签的 PDF 内容

为了获取带有标签文本的 PDF 文档的内容，Aspose.PDF 提供 [已标记内容](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 的财产 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 班级。

使用结构化和分层的目录 (TOC) 创建高级、带完整标签的 PDF 文档：

1. 创建新的 Document 对象。
1. 访问 tagged_content 属性。
1. 使用 “set_title ()” 设置文档标题。
1. 使用 “set_language ()” 设置文档语言。
1. 保存文档。

```python
import aspose.pdf as ap
from aspose.pycore import cast
import sys
from os import path

# region Extract Tagged Content from PDF
def get_tagged_content(outfile):
    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Work with Tagged PDF content
        # Set Title and Language for Document
        tagged_content.set_title("Simple Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Save Tagged PDF Document
        document.save(outfile)
```

## 获取根结构

带标签的 PDF 包含定义文档语义结构的逻辑结构树。StructTreeRoot 代表该逻辑树的根，而 rootElement 则提供了与文档的顶级结构元素进行交互的接口。

以下代码片段显示了如何获取带标签的 PDF 文档的根结构：

1. 创建新的带标签的 PDF 文档。
1. 访问带标签的内容并设置元数据。
1. 访问 StructTreeRoot 和 rootElement。
1. 保存带标签的 PDF。

```python
import aspose.pdf as ap
from aspose.pycore import cast
import sys
from os import path

def get_root_structure(outfile):

    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Properties StructTreeRootElement and RootElement are used for access to
        # StructTreeRoot object of pdf document and to root structure element (Document structure element).
        struct_tree_root_element = tagged_content.struct_tree_root_element
        root_element = tagged_content.root_element

        print(f"StructTreeRootElement: {struct_tree_root_element}")
        print(f"RootElement: {root_element}")

        # Save Tagged PDF Document
        document.save(outfile)
```

## 访问子元素

带标签的 PDF 包含逻辑结构树，用于定义文档的语义层次结构（标题、段落、表单、列表等）。访问和修改这些结构元素允许您：

- 检查元数据，例如标题、语言、actual_text 和无障碍相关属性
- 更新属性以改善可访问性或本地化
- 以编程方式调整逻辑文档结构以符合 PDF/UA

 以下代码片段显示了如何访问带标签的 PDF 文档的子元素：

```python
import aspose.pdf as ap
from aspose.pycore import cast
import sys
from os import path

def access_child_elements(infile, outfile):

    # Open PDF Document
    with ap.Document(infile) as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Access to root element(s)
        element_list = tagged_content.struct_tree_root_element.child_elements

        for element in element_list:
            if isinstance(element, ap.logicalstructure.StructureElement):
                structure_element = cast(ap.logicalstructure.StructureElement, element)
                # Get properties
                print(
                    "StructureElement properties - "
                    f"title: {structure_element.title}, "
                    f"language: {structure_element.language}, "
                    f"actual_text: {structure_element.actual_text}, "
                    f"expansion_text: {structure_element.expansion_text}, "
                    f"alternative_text: {structure_element.alternative_text}"
                )

        # Access to child elements of first element in root element
        element_list = tagged_content.root_element.child_elements[1].child_elements
        for element in element_list:
            if isinstance(element, ap.logicalstructure.StructureElement):
                structure_element = element

                # Set properties
                structure_element.title = "title"
                structure_element.language = "fr-FR"
                structure_element.actual_text = "actual text"
                structure_element.expansion_text = "exp"
                structure_element.alternative_text = "alt"

        # Save Tagged PDF Document
        document.save(outfile)
```

## 相关标签 PDF 主题

- [创建带标签的 PDF](/pdf/zh/python-net/create-tagged-pdf/) 在检查其结构之前构建可访问的带标签的文档。
- [设置结构元素的属性](/pdf/zh/python-net/setting-structure-elements-properties/) 在提取结构元素后更新语义属性。
- [在带标签的 PDF 中使用表格](/pdf/zh/python-net/working-with-table-in-tagged-pdfs/) 用于标记表的可访问性工作流程。