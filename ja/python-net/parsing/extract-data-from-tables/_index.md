---
title: PythonでPDFの表からデータを抽出する
linktitle: 表からデータを抽出
type: docs
weight: 40
url: /ja/python-net/extract-data-from-table-in-pdf/
description: Aspose.PDF for Python を使用して PDF から表形式のデータを抽出する方法を学びます
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: PythonでPDFの表からデータを抽出する方法
Abstract: この記事では、Python ライブラリである Aspose.PDF を使用して PDF 文書から表をプログラムで抽出・処理するための包括的なガイドを提供します。記事では、PDF 文書を開き、各ページを反復し、`TableAbsorber` クラスを利用して表を抽出する Python スクリプトを紹介します。抽出された表データは構造化され、さらなる分析のために出力されます。このセクションでは、四角形の注釈で囲まれた領域など、PDF 内の特定のマーキングされた領域から表を抽出する方法を説明します。スクリプトはこれらの注釈を特定し、`TableAbsorber` を初期化し、表が注釈領域内にあるかどうかを確認した上でデータを抽出・出力します。最後のセクションでは、抽出した表データを CSV ファイル形式に変換する方法を詳述します。
---

## PDFから表をプログラムで抽出する

このコードは PDF の表を抽出し、PDF ファイルから取得した表形式データを読みやすく構造化された形式に変換して、さらなる処理や分析に利用できるようにします。

1. PDF 文書を開く
1. PDF ページを反復処理する
1. 表データを抽出する

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    # Iterate through each page in the document
    for page in document.pages:
        absorber = apdf.text.TableAbsorber()
        absorber.visit(page)

        for table in absorber.table_list:
            print("Table")
            for row in table.row_list:
                row_text = []
                for cell in row.cell_list:
                    cell_text = []
                    for fragment in cell.text_fragments:
                        cell_text.append(
                            "".join(seg.text for seg in fragment.segments)
                        )
                    row_text.append("|".join(cell_text))
                print("|".join(row_text))
```

## PDF ページの特定領域から表を抽出する

このコードスニペットは、ハイライトされたボックスや特定の注釈など、PDF の特定のマーキングされた領域から表形式データを抽出します。

1. PDF 文書を開く
1. 最初のページを取得する
1. 最初の四角形注釈を見つける
1. TableAbsorber を初期化する
1. ページ上の表を反復処理する
1. 表が注釈領域内にあるか確認する

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    # The path to the documents directory
    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    # Get the first page (index starts from 1 in Aspose.PDF)
    page = document.pages[1]

    # Find the first square annotation
    square_annotation = next(
        (
            ann
            for ann in page.annotations
            if ann.annotation_type == apdf.annotations.AnnotationType.SQUARE
        ),
        None,
    )

    if square_annotation is None:
        print("No square annotation found.")
        return

    # Initialize the TableAbsorber
    absorber = apdf.text.TableAbsorber()
    absorber.visit(page)

    # Iterate through tables on the page
    for table in absorber.table_list:
        table_rect = table.rectangle
        annotation_rect = square_annotation.rect

        # Check if the table is inside the annotation region
        is_in_region = (
            annotation_rect.llx < table_rect.llx
            and annotation_rect.lly < table_rect.lly
            and annotation_rect.urx > table_rect.urx
            and annotation_rect.ury > table_rect.ury
        )

        if is_in_region:
            for row in table.row_list:
                row_text = []
                for cell in row.cell_list:
                    cell_text = []
                    for fragment in cell.text_fragments:
                        cell_text.append(
                            "".join(seg.text for seg in fragment.segments)
                        )
                    row_text.append("|".join(cell_text))
                print("|".join(row_text))
```

## PDF から表データを抽出し、Excel ファイルに保存する

以下のコードスニペットは PDF から表形式データを抽出し、Excel や Google Sheets などのスプレッドシートアプリケーションでのさらなる分析や操作のために CSV ファイルとしてエクスポートします。

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    excel_save = apdf.ExcelSaveOptions()
    excel_save.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
    document.save(path_outfile, excel_save)
```

