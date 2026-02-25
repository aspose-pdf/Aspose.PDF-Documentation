---
title: 从 PDF 中提取标签内容
linktitle: 提取标签内容
type: docs
weight: 20
url: /zh/python-net/extract-tagged-content-from-tagged-pdfs/
description: 本文解释了如何使用 Aspose.PDF for Python via .NET 提取带标签的 PDF 文档内容
lastmod: "2025-06-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

在本文中，您将学习如何使用 Python 提取带标签的 PDF 文档内容。

## 获取带标签的 PDF 内容

为了获取带标签文本的 PDF 文档内容，Aspose.PDF 提供了 [tagged_content](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 属性，属于 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类。

以下代码片段展示了如何获取带标签文本的 PDF 文档内容：

```python

    import aspose.pdf as ap

    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Work with Tagged PDF content
        # Set Title and Language for Document
        tagged_content.set_title("Simple Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Save Tagged PDF Document
        document.save(path_outfile)
```

## 获取根结构

为了获取带标签 PDF 文档的根结构，Aspose.PDF 提供了 [struct_tree_root_element](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/#properties) 属性，属于 [ITaggedContent](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/) 接口，以及 [root_element](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/#properties)。

以下代码片段展示了如何获取带标签 PDF 文档的根结构：

```python

    import aspose.pdf as ap

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
```

## 访问子元素

为了访问带标签 PDF 文档的子元素，Aspose.PDF 提供了 [ElementList](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/elementlist/) 类。以下代码片段展示了如何访问带标签 PDF 文档的子元素：

```python

    import aspose.pdf as ap
    from aspose.pycore import *

    # Open PDF Document
    with ap.Document(path_infile) as document:
        # Get Content for work with Tagged PDF
        tagged_content = document.tagged_content

        # Access to root element(s)
        element_list = tagged_content.struct_tree_root_element.child_elements

        for element in element_list:
            if isinstance(element, ap.logicalstructure.StructureElement):
                structure_element = cast(ap.logical_structure.StructureElement, element)

                # Get properties
                title = structure_element.title
                language = structure_element.language
                actual_text = structure_element.actual_text
                expansion_text = structure_element.expansion_text
                alternative_text = structure_element.alternative_text

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
        document.save(path_outfile)
```
