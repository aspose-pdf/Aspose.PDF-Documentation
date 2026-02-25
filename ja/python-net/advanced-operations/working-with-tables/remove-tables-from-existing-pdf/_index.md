---
title: 既存のPDFからテーブルを削除する
linktitle: テーブルを削除
type: docs
weight: 50
url: /ja/python-net/removing-tables/
lastmod: "2025-09-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Pythonを使用してPDFからテーブルを削除する方法
Abstract: この文章では、.NET 経由の Python 用 Aspose.PDF の機能について、特に PDF ドキュメント内のテーブルの操作に焦点を当てて説明します。このライブラリでは、新規および既存の PDF ファイルにテーブルを挿入または作成したり、既存の PDF からテーブルを操作または削除したりすることができます。記事では、PDF 内のテーブルを特定し操作するために重要な `TableAbsorber` クラスを紹介します。テーブルの削除を可能にする新しいメソッド `remove()` が追加されました。本文では、PDF から単一のテーブルを削除する例と、複数のテーブルを削除する例の 2 つのコードスニペットを提供しています。これらの例は、`TableAbsorber` クラスを実用的に使用して PDF ドキュメントからテーブルを削除する方法を示しています。
---

## PDF ドキュメントからテーブルを削除する

Aspose.PDF for Python を使用すると、PDF からテーブルを削除できます。既存の PDF を開き、TableAbsorber を使用して最初のページの最初のテーブルを検出し、[remove_one_table](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods) を使用してそのテーブルを削除します。その後、更新された PDF を新しいファイルに保存します。

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    # Load existing PDF document
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    # Get first table on the page
    table = absorber.table_list[0]
    # Remove the table
    absorber.remove(table)
    # Save PDF
    document.save(path_outfile)
```

## PDF ドキュメントからすべてのテーブルを削除する

当社のライブラリを使用すると、PDF の特定のページからすべてのテーブルを削除できます。コードは既存の PDF を開き、TableAbsorber を使用して2ページ目のすべてのテーブルを検出し、検出されたテーブルを順に処理してそれぞれを削除し、変更された PDF を新しいファイルに保存します。ページ内のテーブルを一括で削除し、PDF の他のコンテンツはそのまま保持したい場合に便利です。

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    # Load existing PDF document
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit second page with absorber
    absorber.visit(document.pages[1])
    #  Loop through the copy of collection and removing tables
    tables = list(absorber.table_list)
    for table in tables:
        absorber.remove(table)

    # Save document
    document.save(path_outfile)
```


