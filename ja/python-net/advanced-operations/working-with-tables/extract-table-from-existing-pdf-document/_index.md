---
title: PDFドキュメントからテーブルを抽出する
linktitle: テーブルを抽出
type: docs
weight: 20
url: /ja/python-net/extracting-table/
description: Aspose.PDF for Python via .NET を使用すると、PDF ドキュメントに含まれるテーブルに対してさまざまな操作を行うことが可能です。
lastmod: "2025-09-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF からテーブルを抽出する方法
Abstract: この記事では、Python を使用して PDF ドキュメントからテーブルを抽出する手順について説明します。特に Aspose.PDF for Python via .NET ライブラリを活用します。コード例では、PDF ドキュメントを読み込み、ページを反復処理し、`TableAbsorber` クラスを使用してテーブルデータを特定・抽出する方法を示しています。コードは各テーブル、行、セルを走査し、テキストフラグメントを収集して抽出されたテキストを出力します。この手法は、PDF 内の表形式データの抽出や分析タスクにおいて強力なツールとして強調されています。
---

## PDFからテーブルを抽出する

Python を使用して PDF からテーブルを抽出することは、データ抽出や分析に非常に役立ちます。Aspose.PDF for Python via .NET ライブラリを利用すれば、PDF ドキュメントに埋め込まれたテーブルを効率的に操作し、さまざまなデータ関連タスクに活用できます。

このコードスニペットは既存の PDF ファイルを開き、各ページをスキャンしてテーブルを検出し、セルのテキスト内容を抽出します。'TableAbsorber' を使用してテーブルを検出し、行とセルを反復して内部のテキストを出力します。

1. PDF を ap.Document オブジェクトに読み込みます。
1. ページをループします。
1. TableAbsorber オブジェクトを作成します。
1. テーブルを反復処理します。
1. 行とセルを反復処理します。
1. セルからテキストを抽出し、出力します。

この例では PDF を読み取り、すべてのテーブルを見つけ、セルの内容を行ごとに出力します。

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    document = ap.Document(path_infile)
    for page in document.pages:
        absorber = ap.text.TableAbsorber()
        absorber.visit(page)
        for table in absorber.table_list:
            print("Table ----")
            for row in table.row_list:
                print("Row")
                for cell in row.cell_list:
                    text_fragment_collection = cell.text_fragments
                    for fragment in text_fragment_collection:
                        txt = ""
                        for seg in fragment.segments:
                            txt += seg.text
                        print(txt)
```


