---
title: PDF メタデータをクリア
type: docs
weight: 10
url: /ja/python-net/clear-pdf-metadata/
description: .NET 経由の Python 用 Aspose.PDF を使用して PDF ドキュメントからすべてのメタデータを削除します。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python 用 Aspose.PDF を使用して PDF メタデータをクリアする
Abstract: このガイドでは、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントからすべてのメタデータを削除する方法について説明します。標準メタデータフィールドとカスタムメタデータフィールドの両方をクリアし、サニタイズされた PDF を保存する方法を学習します。これは、プライバシー、セキュリティ、または一般公開用の PDF の準備に役立ちます。
---

PDF には、多くの場合、タイトル、作成者、キーワード、作成日、カスタムフィールドなどのメタデータが含まれています。シナリオによっては、たとえば配布やアーカイブの前など、PDF からすべてのメタデータを削除したい場合があります。Aspose.PDF には、すべてのメタデータを簡単に削除するための clear_info () メソッドが用意されています。クリアしたら、save () メソッドを使用して PDF を保存できます。

1. PDF ファイルをロードします。
1. すべてのメタデータを消去します。
1. クリーンな PDF を保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def clear_pdf_metadata(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Clear PDF metadata
    pdf_info.clear_info()

    # Save updated metadata
    pdf_info.save(outfile)
```
