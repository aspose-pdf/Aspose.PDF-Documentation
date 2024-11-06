---
title: PythonでPDFサイズを最適化、圧縮、または縮小
linktitle: PDFの最適化
type: docs
weight: 30
url: ja/python-cpp/optimize-pdf/
keywords: "optimize pdf Python"
description: PDFファイルを最適化し、すべての画像を縮小し、サイズを縮小し、フォントを埋め込まないようにし、Pythonで未使用のオブジェクトを削除します。
lastmod: "2023-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

PDFドキュメントには追加のデータが含まれることがあります。PDFファイルのサイズを縮小することで、ネットワーク転送とストレージを最適化するのに役立ちます。これは、ウェブページでの公開、ソーシャルネットワークでの共有、電子メールでの送信、またはストレージでのアーカイブに特に便利です。PDFを最適化するためにいくつかの技術を使用できます：

- オンラインブラウジング用にページコンテンツを最適化する
- すべての画像を縮小または圧縮する
- ページコンテンツの再利用を可能にする
- 重複するストリームをマージする
- フォントを埋め込まない
- 未使用のオブジェクトを削除する
- フォームフィールドの平坦化を削除する
- 注釈を削除または平坦化する

{{% alert color="primary" %}}

最適化方法の詳細な説明は、「最適化方法の概要」ページで見つけることができます。

{{% /alert %}}

## ウェブ用にPDFドキュメントを最適化する

ウェブ用の最適化、または直線化とは、PDFファイルをウェブブラウザを使用したオンライン閲覧に適した状態にするプロセスを指します。ファイルをウェブ表示用に最適化するには:


以下のコードスニペットは、ウェブ用にPDFドキュメントを最適化する方法を示しています。

```python

    import AsposePDFPythonWrappers as ap

    # ドキュメントディレクトリへのパス。
    dataDir = "..."

    # ドキュメントを開く
    document = ap.Document(dataDir + "OptimizeDocument.pdf")

    # ウェブ用に最適化する
    document.optimize()

    dataDir = dataDir + "OptimizeDocument_out.pdf"

    # 出力ドキュメントを保存する
    document.Save(dataDir)
```