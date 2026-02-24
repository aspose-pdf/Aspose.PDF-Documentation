---
title: PythonでPDFにページスタンプを追加する
linktitle: ページスタンプの追加
type: docs
weight: 30
url: /ja/python-net/page-stamps-in-the-pdf-file/
description: Aspose.PDF for Python via .NET を使用すると、PDF ファイルにページスタンプを追加できます。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF にページスタンプを追加する方法
Abstract: この記事では、Aspose.PDF for Python を使用して PDF ドキュメントにページスタンプを追加する方法を説明します。ページスタンプを使用すると、ロゴ、透かし、注釈などのコンテンツを PDF の特定のページにオーバーレイまたはアンダーレイできます。例では、既存の PDF を開き、別の PDF ページから PdfPageStamp オブジェクトを作成し、背景スタンプとして設定し、特定のページに適用する方法を示しています。その後、スタンプを付けた PDF を新しいドキュメントとして保存します。この手法は、ブランディング、透かしの追加、または自動化された PDF ワークフローでページレベルのコンテンツを強調する際に有用です。
---

Aspose.PDF for Python via .NET は、PDF の特定のページにページスタンプ（透かしまたはオーバーレイ）を適用する方法を示します。[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。ページスタンプは、背景または前景レイヤーとして使用できる既存の PDF ページにすることができます（[`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/) を参照）。これは、ロゴ、透かし、またはその他の繰り返し使用されるページコンテンツを追加するのに便利です。

1. `ap.Document()` を使用して PDF ドキュメントを開きます（[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) を参照）。
1. スタンプとして使用する PDF ページまたはファイルを使って `PdfPageStamp` オブジェクトを作成します（[`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/) を参照）。
1. スタンプのプロパティを設定します。例: コンテンツの背後に配置するには `background = True` とします。
1. `document.pages[page_number].add_stamp(page_stamp)` を使用して特定のページにスタンプを追加します（[`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) と [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) を参照）。
1. [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) を使用して、変更された PDF を指定された出力ファイルに保存します。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_stamp(input_file_name, page_stamp_name, output_file_name):
    # Open PDF document
    document = ap.Document(input_file_name)

    page_stamp = ap.PdfPageStamp(page_stamp_name, 1)
    page_stamp.background = True

    # Add stamp to particular page
    document.pages[1].add_stamp(page_stamp)

    document.save(output_file_name)
```

