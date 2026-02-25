---
title: PythonでPDFを結合する方法
linktitle: PDFファイルを結合
type: docs
weight: 50
url: /ja/python-net/merge-pdf-documents/
description: このページでは、Python を使用して PDF ドキュメントを単一の PDF ファイルに結合する方法を説明します。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PythonでPDFページを結合
Abstract: 本稿では、複数の PDF ファイルを単一のドキュメントに結合するという一般的なニーズに対処し、PDF コンテンツの整理、ストレージの最適化、共有に役立つプロセスについて説明します。サードパーティライブラリなしでは Python での PDF 結合が困難であることを踏まえ、.NET 経由の Python 用 Aspose.PDF を使用して PDF ファイルを効率的に結合する方法を検討します。この記事では、PDF ファイルの連結手順として、新規ドキュメントの作成、ファイルの結合、結合されたドキュメントの保存というステップバイステップのガイドを提供します。コードスニペットは Aspose.PDF を使用した実装例を示し、ライブラリが結合プロセスを簡素化できる能力を強調しています。さらに、PDF を結合するオンラインツールである Aspose.PDF Merger を紹介し、ユーザーがウェブベースの環境で機能を体験できるようにします。
---

## Pythonで複数のPDFを単一のPDFに結合または統合する

PDF ファイルを結合することはユーザーの間で非常に人気のある検索です。複数の PDF ファイルを 1 つのドキュメントとして共有したり保存したりしたい場合に便利です。

PDF ファイルを結合すると、ドキュメントを整理したり、PC のストレージ領域を確保したり、複数の PDF ファイルを 1 つのドキュメントにまとめて他者と共有したりできます。

.NET 経由で Python で PDF を結合することは、サードパーティライブラリを使用しない限り簡単な作業ではありません。
この記事では、.NET 経由の Python 用 Aspose.PDF を使用して、複数の PDF ファイルを単一の PDF ドキュメントに結合する方法を示します。

## Python と DOM を使用した PDF ファイルの結合

2 つの PDF ファイルを連結するには:

1. 新しいドキュメントを作成します。
1. PDF ファイルを結合します
1. 結合されたドキュメントを保存します

複数の PDF ドキュメントを単一のファイルに結合する:

```python

    import aspose.pdf as apdf
    import aspose.pydrawing as asdrw
    from io import FileIO
    from os import path

    path_infile1 = path.join(self.dataDir, infile1)
    path_infile2 = path.join(self.dataDir, infile2)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document()
    document.merge(files=[path_infile1, path_infile2])
    document.save(path_outfile)
```

## ライブ例

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) は、プレゼンテーション結合機能の動作を調査できるオンラインの無料ウェブアプリケーションです。

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)


