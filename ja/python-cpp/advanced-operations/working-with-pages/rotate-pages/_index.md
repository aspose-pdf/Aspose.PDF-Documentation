---
title: PDFページを回転させる方法 (Python via C++)
linktitle: PDFページを回転する
type: docs
weight: 20
url: /ja/python-cpp/rotate-pages/
description: このトピックでは、Python経由でC++を使用して既存のPDFファイルのページの向きをプログラムで回転させる方法について説明します。
lastmod: "2024-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

時には、スキャンや作成の問題によりPDFページの向きが誤っていることがあります。ページを回転させることで、より読みやすく、表示しやすいように正しい向きで表示されるようにします。
PDFページを回転させることで、異なるデバイスやプラットフォームでも一貫した表示体験を維持できます。

PDFページを回転させることで、注釈やコメント、署名を追加するなどの編集作業が容易になります。ページを希望の向きに回転させることで、編集およびレビューのプロセスをより効率的に行うことができます。

また、PDFドキュメントを印刷する際には、ページが正しく向いていることを確認し、位置ずれや切り取りの問題を避けることが重要です。
 印刷前に必要に応じてページを回転させることで、印刷出力を最適化し、コンテンツが意図した通りに表示されるようにします。  
PDF ページを回転させることは、文書の可読性、一貫性、プレゼンテーションをさまざまな文脈や目的において改善するのに役立つ便利な機能です。

このトピックでは、Python を使用して既存の PDF ファイル内のページの向きをプログラムで更新または変更する方法について説明します。

## ページの向きを変更する

Aspose.PDF for Python via C++ は、ページの向きを変更するなどの優れた機能をサポートしています。

1. 入力ファイルからドキュメントオブジェクトを作成します
1. 'apCore.document_get_pages' を使用して、ドキュメントからページコレクションを取得します
1. 'apCore.page_collection_get_page' を使用して、ページコレクションから最初のページを取得します
1. 'apCore.page_set_rotate' を使用してページを時計回りに90度回転させます
1. 'document.save' メソッドを使用して、変更されたドキュメントを出力ファイルに保存します

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # サンプルファイルを含むディレクトリへのパスを作成する
    dataDir = os.path.join(os.getcwd(), "samples")

    # 入力ファイルと出力ファイルへのパスを作成する
    input_file = os.path.join(dataDir, "sample0.pdf")
    output_file = os.path.join(dataDir, "results", "rotated_document.pdf")

    # 入力ファイルを読み込んでドキュメントオブジェクトを作成する
    doc = apCore.document_create_from_file(inputFile)

    # ドキュメント内のページのコレクションを取得する
    pages = apCore.document_get_pages(doc)

    # コレクションから最初のページを取得する
    page = apCore.page_collection_get_page(pages, 1)

    # ページを時計回りに90度回転させる
    apCore.page_set_rotate(page, apCore.Rotation(apCore.on90))

    # 変更されたドキュメントを出力ファイルに保存する
    apCore.document_save(doc, output_file)

    # リソースを解放するためにドキュメントハンドルを閉じる
    apCore.close_handle(doc)
```