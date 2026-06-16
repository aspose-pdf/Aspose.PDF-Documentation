---
title: PDF バージョンを取得
type: docs
weight: 20
url: /ja/python-net/get-pdf-version/
description: Aspose.PDF for Python を使用して PDF ドキュメントのバージョンをプログラム的に判断する方法を学びましょう。このチュートリアルでは、PDFFileInfo クラスを使用してファイルの PDF バージョンを確認する方法を示します。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python 用 Aspose.PDF を使用して PDF バージョンを取得する
Abstract: PDF ドキュメントには、サポートしている機能と仕様を示すバージョン番号が付いています (1.4、1.7、2.0 など)。PDF のバージョンを知ることは、互換性、機能のサポート、および文書処理ワークフローにとって重要です。このガイドでは、Aspose.PDF for Python の PDFFileInfo クラスを使用してプログラムで PDF バージョンを取得する方法を学習します。
---

PDF バージョンは、フォームフィールド、暗号化、注釈、圧縮など、ドキュメントでサポートされる機能を定義します。複数の PDF を扱う開発者は、バージョンを確認して、これらのファイルを処理するツール、ライブラリ、またはワークフローとの互換性を確認してください。

Aspose.PDF for Python を使用すると、PDF バージョンを簡単に調べることができます。 [PDF ファイル情報](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) クラス。

1. PDF ドキュメントをロードします。
1. その PDF バージョンを取得します。
1. コンソールにバージョンを表示します。

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_pdf_version(input_file_name):

    pdf_metadata = pdf_facades.PdfFileInfo(input_file_name)
    version = pdf_metadata.get_pdf_version()
    print(f"\nPDF Version: {version}")
```
