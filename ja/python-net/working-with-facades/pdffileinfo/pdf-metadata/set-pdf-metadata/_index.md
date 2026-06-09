---
title: PDF メタデータを設定
type: docs
weight: 50
url: /ja/python-net/set-pdf-metadata/
description: .NET 経由で Aspose.PDF for Python を使用して PDF ドキュメント内のメタデータを変更および保存します。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python 用 Aspose.PDF を使用して PDF メタデータを更新する
Abstract: このガイドでは、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメント内のメタデータを変更および保存する方法について説明します。タイトル、件名、キーワード、作成者などの標準 PDF プロパティと、カスタムメタデータフィールドを更新する方法を示します。最終的には、プログラムで PDF メタデータを更新し、変更を保存できるようになります。
---

PDF ドキュメントには、標準メタデータ (タイトル、件名、キーワード、作成者、作成者) と XMP プロパティとして保存されたカスタムメタデータの両方を含めることができます。Aspose.PDF には Python でこれらのプロパティを変更するための簡単な API が用意されています。このガイドでは、を使用してこれらのフィールドを更新し、変更した PDF ファイルを保存する方法について説明します。 [PDF ファイル情報](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) クラス。

1. PDF ファイルをロードします。
1. 標準メタデータを更新します。
1. カスタムメタデータを追加または更新します。
1. 更新したメタデータを保存します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def set_pdf_metadata(infile, outfile):

    # Get PDF information
    pdf_info = pdf_facades.PdfFileInfo(infile)

    # Set PDF metadata
    pdf_info.subject = "Aspose PDF for Python via .NET"
    pdf_info.title = "Aspose PDF for Python via .NET"
    pdf_info.keywords = "Aspose, PDF, Python, .NET"
    pdf_info.creator = "Aspose Team"

    pdf_info.set_meta_info("CustomKey", "CustomValue")

    # pdf_info.save_new_info(outfile)
    # Is obsolete, use save() method instead

    # Save updated metadata
    pdf_info.save(outfile)
```
