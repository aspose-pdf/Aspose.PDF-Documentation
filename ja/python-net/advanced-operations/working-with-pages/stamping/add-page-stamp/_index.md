---
title: Python で PDF にページスタンプを追加する方法
linktitle: ページスタンプの追加
type: docs
weight: 30
url: /ja/python-net/page-stamps-in-the-pdf-file/
description: Python で PDF ページスタンプをオーバーレイまたは背景として追加する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF にページスタンプを追加する方法
Abstract: この記事では、Aspose.PDF for Python を使用して PDF ドキュメントにページスタンプを追加する方法について説明します。ページスタンプを使用すると、ロゴ、透かし、注釈などのコンテンツを PDF の特定のページに重ねたり下に置いたりできます。この例は、既存の PDF を開き、別の PDF ページから PDFPageStamp オブジェクトを作成し、それを背景スタンプとして設定し、特定のページに適用する方法を示しています。その後、スタンプが押された PDF は新しい文書として保存されます。この手法は、自動化された PDF ワークフローでブランディングやウォーターマークを付けたり、ページレベルのコンテンツを強調したりする場合に便利です。
---

.NET 経由の Python Aspose.PDF では、PDF 内の特定のページにページスタンプ (ウォーターマークまたはオーバーレイ) を適用する方法について説明しています [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。ページスタンプは、既存の PDF ページを背景レイヤーまたは前景レイヤーとして使用できます (「」を参照)。 [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/))。これは、ロゴ、透かし、その他の繰り返しの多いページコンテンツを追加する場合に便利です。

1. を使用して PDF ドキュメントを開きます。 `ap.Document()` (参照 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)).
1. を作成 `PdfPageStamp` PDF ページまたはファイルをスタンプとして使用するオブジェクト (「」を参照) [`PdfPageStamp`](https://reference.aspose.com/pdf/python-net/aspose.pdf.pdfpagestamp/)).
1. スタンププロパティを設定します。例: `background = True` コンテンツの背後に置くためです。
1. を使用して特定のページにスタンプを追加します `document.pages[page_number].add_stamp(page_stamp)` (参照 [`Page.add_stamp()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) そして [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)).
1. 変更した PDF を、次の方法で指定の出力ファイルに保存します。 [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python
import sys
import aspose.pdf as ap
from os import path

def add_page_stamp(input_file_name, page_stamp_name, output_file_name):
    # Open PDF document
    document = ap.Document(input_file_name)

    page_stamp = ap.PdfPageStamp(page_stamp_name, 1)
    page_stamp.background = True

    # Add stamp to particular page
    document.pages[1].add_stamp(page_stamp)

    document.save(output_file_name)
```

## スタンピング関連トピック

- [Python で PDF ページにスタンプを付ける](/pdf/ja/python-net/stamping/)
- [Python で PDF にページ番号を追加する方法](/pdf/ja/python-net/add-page-number/)
- [Python で PDF にイメージスタンプを追加する方法](/pdf/ja/python-net/image-stamps-in-pdf-page/)
- [Python で PDF にテキストスタンプを追加する方法](/pdf/ja/python-net/text-stamps-in-the-pdf-file/)