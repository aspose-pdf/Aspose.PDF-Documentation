---
title: PythonでPDFからタグ付けされたコンテンツを抽出する
linktitle: タグ付けされたコンテンツを抽出
type: docs
weight: 20
url: /ja/python-net/extract-tagged-content-from-tagged-pdfs/
description: Aspose.PDF for Python via .NET を使用して、Pythonでタグ付けされたPDFコンテンツを抽出する方法を学びます。タグ付けコンテンツ、ルート構造、子構造要素へのアクセスを含みます。
lastmod: "2026-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

この記事では、Pythonを使用してPDFドキュメントからタグ付けされたコンテンツを抽出する方法を学びます。

タグ付き PDF を検査したり、論理構造ツリーを読み取ったり、アクセシビリティ ワークフローのために構造要素が正しく作成されたかを検証する必要がある場合は、これらの例を使用してください。

## タグ付き PDF コンテンツの取得

タグ付きテキストを含む PDF ドキュメントのコンテンツを取得するために、Aspose.PDF は提供します。 [tagged_content](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) のプロパティ [ドキュメント](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラス。

構造化され階層的な目次（TOC）を持つ、高度で完全にタグ付けされた PDF ドキュメントを作成します:

1. 新しい Document オブジェクトを作成します。
1. tagged_content プロパティにアクセスします。
1. 'set_title()' を使用してドキュメントのタイトルを設定します。
1. 'set_language()' を使用してドキュメントの言語を設定します。
1. ドキュメントを保存します。

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

## ルート構造の取得

Tagged PDF は、文書の意味構造を定義する論理構造ツリーを含みます。StructTreeRoot はこの論理ツリーのルートを表し、RootElement は文書のトップレベル構造要素とやり取りするためのインターフェイスを提供します。

以下のコードスニペットは、Tagged PDF ドキュメントのルート構造を取得する方法を示しています。

1. 新しいタグ付けされた PDF ドキュメントを作成します。
1. タグ付けされたコンテンツにアクセスし、メタデータを設定します。
1. StructTreeRoot と RootElement にアクセスします。
1. タグ付けされた PDF を保存します。

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

## 子要素へのアクセス

Tagged PDFs には、文書の意味的階層（見出し、段落、forms、リストなど）を定義する論理構造ツリーが含まれます。これらの構造要素にアクセスし、変更することで、以下が可能になります：

- title、language、actual_text などのメタデータや、アクセシビリティ関連プロパティを検査する
- アクセシビリティまたはローカリゼーションを向上させるためにプロパティを更新する
- PDF/UA 準拠のために論理文書構造をプログラムで調整する

 以下のコードスニペットは、Tagged PDF ドキュメントの子要素にアクセスする方法を示しています:

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

## 関連するタグ付け PDF のトピック

- [Tagged PDFを作成する](/pdf/ja/python-net/create-tagged-pdf/) 構造を検査する前に、アクセシブルなタグ付き文書を作成します。
- [Structure Elements のプロパティ設定](/pdf/ja/python-net/setting-structure-elements-properties/) 構造要素を抽出した後にセマンティックプロパティを更新する
- [Tagged PDF のテーブルの操作](/pdf/ja/python-net/working-with-table-in-tagged-pdfs/) タグ付けされたテーブルのアクセシビリティワークフロー向けに。