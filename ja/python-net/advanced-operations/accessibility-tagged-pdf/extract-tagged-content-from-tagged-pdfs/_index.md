---
title: PDFからタグ付けされたコンテンツを抽出
linktitle: タグ付けされたコンテンツを抽出
type: docs
weight: 20
url: /ja/python-net/extract-tagged-content-from-tagged-pdfs/
description: この記事では、Aspose.PDF for Python via .NET を使用して PDF ドキュメントからタグ付けされたコンテンツを抽出する方法を説明します。
lastmod: "2025-06-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

この記事では、Python を使用して PDF ドキュメントからタグ付けされたコンテンツを抽出する方法を学びます。

## タグ付けされた PDF コンテンツの取得

タグ付けされたテキストを含む PDF ドキュメントのコンテンツを取得するには、Aspose.PDF は [tagged_content](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) プロパティ（[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラス）を提供します。

以下のコードスニペットは、タグ付けされたテキストを含む PDF ドキュメントのコンテンツを取得する方法を示しています。

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

## ルート構造の取得

タグ付けされた PDF ドキュメントのルート構造を取得するには、Aspose.PDF は [struct_tree_root_element](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/#properties) プロパティ（[ITaggedContent](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/) インターフェイス）と [root_element](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/#properties) を提供します。

以下のコードスニペットは、タグ付けされた PDF ドキュメントのルート構造を取得する方法を示しています。

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

## 子要素へのアクセス

タグ付けされた PDF ドキュメントの子要素にアクセスするには、Aspose.PDF は [ElementList](https://reference.aspose.com/pdf/python-net/aspose.pdf.logicalstructure/elementlist/) クラスを提供します。以下のコードスニペットは、タグ付けされた PDF ドキュメントの子要素にアクセスする方法を示しています。

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
