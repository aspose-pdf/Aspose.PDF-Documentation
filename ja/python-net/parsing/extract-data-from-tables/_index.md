---
title: Python を使用して PDF 内のテーブルからデータを抽出する
linktitle: テーブルからデータを抽出
type: docs
weight: 40
url: /ja/python-net/extract-data-from-table-in-pdf/
description: Aspose.PDF for Python を使用して PDF ファイルからテーブルデータを抽出し、その結果をエクスポートしてさらに処理する方法を学びます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF のテーブルからデータを抽出する方法
Abstract: この記事では、Aspose.PDF for Python を使用して PDF ドキュメントからテーブルデータを抽出して処理する方法について説明します。TableAbsorber を使用して各ページをスキャンする方法、検出されたテーブルから行とセルを読み取る方法、抽出を特定の注釈付き領域に限定する方法、PDF コンテンツを CSV 形式にエクスポートしてスプレッドシートツールやダウンストリーム処理で使用する方法を示します。
---

## プログラムで PDF から表を抽出

使用 [テーブルアブソーバー](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) aの各ページにあるテーブルを検出します [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。ページにアクセスした後、繰り返し処理する `table_list`次に、各行とセルを確認して、テーブルの内容を読みやすいテキスト形式で再構成します。

1. PDF をとして開く `Document`.
1. 内のページを繰り返し処理する `document.pages`.
1. を作成 `TableAbsorber` 各ページと呼び出しについて `visit(page)`.
1. 検出されたテーブル、行、およびセルをループ処理します。
1. 各セルからテキストフラグメントを読み取り、抽出された行出力をアセンブルします。

```python
import aspose.pdf as apdf
from os import path

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
                    cell_text.append("".join(seg.text for seg in fragment.segments))
                row_text.append("|".join(cell_text))
            print("|".join(row_text))
```

## PDF ページの特定の領域にテーブルを抽出

マークされた領域内にあるテーブルのみを抽出する必要がある場合は、組み合わせてください [テーブルアブソーバー](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) と [スクエア・アノテーション](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/)。この例では、注釈長方形が境界線として使用され、その領域内に完全に含まれているテーブルのみが処理されます。

1. PDF をとして開く `Document`.
1. ターゲットページを選択します。
1. 関心領域を示す四角形の注釈を探します。
1. を作成 `TableAbsorber` そしてページにアクセスしてください。
1. 検出された各テーブル長方形を注釈長方形と比較します。
1. マークされた領域に完全に収まるテーブルのみを処理します。

```python
import aspose.pdf as apdf
from os import path

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
                    cell_text.append("".join(seg.text for seg in fragment.segments))
                row_text.append("|".join(cell_text))
            print("|".join(row_text))
```

## テーブルデータを PDF から CSV にエクスポート

抽出したデータをスプレッドシートに適した形式で保存する必要がある場合は、次の方法でPDFを保存します。 [Excel 保存オプション](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) 出力形式を CSV に設定します。生成されたファイルは Excel や Google スプレッドシートで開くことも、アナリティクスのワークフローにインポートすることもできます。

1. ソース PDF をとして開きます [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. を作成 `ExcelSaveOptions` インスタンス。
1. セット `excel_save.format` に `ExcelSaveOptions.ExcelFormat.CSV`.
1. 文書をターゲット CSV パスに保存します。

```python
import aspose.pdf as apdf
from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

document = apdf.Document(path_infile)
excel_save = apdf.ExcelSaveOptions()
excel_save.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
document.save(path_outfile, excel_save)
```
