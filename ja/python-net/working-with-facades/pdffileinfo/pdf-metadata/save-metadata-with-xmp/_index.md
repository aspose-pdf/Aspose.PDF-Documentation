---
title: XMP でメタデータを保存
type: docs
weight: 30
url: /ja/python-net/save-metadata-with-xmp/
description: XMP を使用して PDF メタデータを.NET 経由で Python 用 Aspose.PDF で保存する
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python 用 Aspose.PDF を使って XMP で PDF メタデータを保存する
Abstract: このガイドでは、XMP (拡張メタデータプラットフォーム) を使用して PDF メタデータを.NET 経由で Aspose.PDF for Python で保存する方法を示します。XMP では、標準メタデータとカスタムメタデータの両方が標準化された XML 形式で PDF 内に埋め込まれるため、アプリケーションやワークフロー間の互換性が向上します。
---

PDF メタデータは複数の方法で保存できます。XMP は、PDF ファイル内にメタデータを埋め込むための最新の標準化された方法です。Aspose.PDF を使用すると、「タイトル」、「件名」、「キーワード」、「作成者」などの標準フィールドを更新し、それらを XMP 形式で保存することで、互換性を高め、将来的にも使用できるようにすることができます。この方法は、従来のメタデータ保存方法よりも推奨されます。

1. PDF ファイルをロードします。
1. 標準メタデータフィールドを設定します。
1. メタデータを XMP 形式で保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def save_info_with_xmp(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Set PDF metadata
    pdf_info.subject = "Aspose PDF for Python via .NET"
    pdf_info.title = "Aspose PDF for Python via .NET"
    pdf_info.keywords = "Aspose, PDF, Python, .NET"
    pdf_info.creator = "Aspose Team"

    # Save updated metadata
    pdf_info.save_new_info_with_xmp(outfile)
```
