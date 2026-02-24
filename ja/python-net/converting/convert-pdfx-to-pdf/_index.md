---
title: PythonでPDF/xをPDF形式に変換する
linktitle: PDF/xをPDF形式に変換
type: docs
weight: 120
url: /ja/python-net/convert-pdf_x-to-pdf/
lastmod: "2025-09-27"
description: このトピックでは、Aspose.PDF for Python via .NET を使用して PDF/x を PDF 形式に変換する方法を示します。
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: PDF/x を PDF 形式に変換する方法
Abstract: この記事は、Aspose.PDF for Python を使用して PDF/UA および PDF/A を PDF ファイルに変換する包括的なガイドを提供します。
---

**PDF/x を PDF 形式に変換することは、PDF/UA および PDF/A を PDF ファイルに変換できることを意味します。**

## PDF/A を PDF に変換

1. 'ap.Document' を使用して PDF ドキュメントを読み込みます。
1. 'remove_pdfa_compliance()' を呼び出して、PDF/A に関連するすべてのコンプライアンス設定とメタデータを削除します。
1. 結果の PDF を出力パスに保存します。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.remove_pdfa_compliance()
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## PDF/UA コンプライアンスの削除

この関数は、2 段階の変換プロセスを示します。まず PDF/UA（ユニバーサルアクセシビリティ）コンプライアンスを削除し、次に結果の PDF を自動タグ付けによりアクセシビリティと意味構造を備えた PDF/A-1B 形式に変換します。

1. 'ap.Document()' を使用して PDF ドキュメントを読み込みます。
1. 'document.remove_pdfa_compliance()' を呼び出して、PDF/A の制限やコンプライアンス設定をすべて削除します。
1. 修正された PDF を 'path_outfile' に保存します。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.remove_pdfa_compliance()
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```
