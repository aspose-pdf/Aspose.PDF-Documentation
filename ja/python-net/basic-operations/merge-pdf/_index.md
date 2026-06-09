---
title: Python で PDF ファイルをマージする
linktitle: PDF ファイルの結合
type: docs
weight: 50
url: /ja/python-net/merge-pdf/
description: Python で複数の PDF ファイルを 1 つの文書に結合する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF ページを結合する
Abstract: この記事では、複数のPDFファイルを1つの文書に結合するという一般的なニーズについて説明します。これは、PDFコンテンツの保存と共有を整理および最適化するうえで役立つプロセスです。Python での PDF の結合は、サードパーティーのライブラリがないと難しい場合があることを認識しながら、.NET 経由で Aspose.PDF for Python を使用して PDF ファイルを効率的に結合する方法を説明します。この記事では、PDF ファイルを連結する方法、つまり新しい文書を作成し、ファイルを結合し、結合した文書を保存する方法を順を追って説明します。コードスニペットは Aspose.PDF を使った実装を示しており、統合プロセスを効率化するライブラリの機能を強調しています。さらに、PDF を結合するためのオンラインツールである Aspose.PDF Merger も紹介されています。これにより、ユーザーは Web ベースの環境で機能を調べることができます。
---

## Python と DOM を使用して PDF ファイルを結合する

2 つの PDF ファイルを連結するには:

1. 新しい文書を作成します。
1. PDF ファイルの結合
1. 結合した文書を保存する

複数の PDF 文書を 1 つのファイルに結合:

```python
import sys
import aspose.pdf as ap
from os import path

def merge_two_documents(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    document1.pages.add(document2.pages)
    document1.save(outfile)
```

## ライブサンプル

[Aspose.PDF 合併](https://products.aspose.app/pdf/merger) は、プレゼンテーションのマージ機能がどのように機能するかを調べることができるオンラインの無料ウェブアプリケーションです。

[![Aspose.PDF 合併](merger.png)](https://products.aspose.app/pdf/merger)

