---
title: Python (via .NET) でベーツ番号付与アーティファクトを追加する
linktitle: ベーツ番号付与の追加
type: docs
weight: 10
url: /ja/python-net/add-bates-numbering/
description: Aspose.PDF for Python via .NET を使用すると、PDF にベーツ番号付与を追加できます。
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python でベーツ番号付与を追加
Abstract: ベーツ番号付与は、法務、医療、ビジネス文書のワークフローにおいて重要な機能であり、セット内の各ページに一意で連続した識別子を付与し、信頼できる参照を可能にします。本記事では、Aspose.PDF for Python via .NET が柔軟な API を通じてベーツ番号付与の自動化をどのように簡素化するかを示します。BatesNArtifact クラスを使用すると、桁数、プレフィックス、サフィックス、配置、余白などの番号付与動作を構成でき、ドキュメント全体にプログラムで適用できます。直接アーティファクトを適用する方法からデリゲートベースの構成まで、複数のアプローチが提示され、静的および動的な制御を提供します。さらに、API は単一のメソッド呼び出しでベーツ番号を完全に削除でき、ページ付与アーティファクトのライフサイクル管理を実現します。明確なステップバイステップのコード例が、ベーツ番号付与の追加、カスタマイズ、削除方法を示し、文書処理ワークフローの効率化を目指す開発者に実用的なリソースを提供します。
---

ベーツ番号付与は、法務、医療、ビジネスのワークフローで広く使用され、文書セット内のページに一意で連続した識別子を割り当てます。Aspose.PDF for Python via .NET は、このプロセスを自動化するためのシンプルで柔軟な API を提供し、任意の PDF に標準化されたベーツ番号をプログラムで適用できます。

`BatesNArtifact` クラスを使用すると、開始番号、桁数、プレフィックスとサフィックス、配置、余白など、番号付与の動作を完全にカスタマイズできます。設定が完了したら、[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) に対して、[`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) の `add_bates_numbering` メソッドを通じてアーティファクトを適用するか、[`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/) オブジェクトのリストの一部として追加できます。Aspose.PDF はデリゲートベースの構成スタイルもサポートし、実行時にアーティファクト設定を動的に制御できます。

ベーツ番号の作成に加えて、API は `delete_bates_numbering` を使用して簡単に削除でき、文書処理ワークフローで完全な柔軟性を提供します。

本記事では、Aspose.PDF for Python via .NET を使用して PDF にベーツ番号付与を追加および削除する複数の方法を示し、アーティファクトの構成、適用、削除の明確な例を提供します。

## ベーツ番号付与アーティファクトの追加

この例では、Aspose.PDF for Python via .NET を使用して、PDF 文書にベーツ番号付与をプログラムで追加する方法を示します。目的の設定で [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) を構成し、文書のページに適用することで、各ページに標準化された識別子を追加するプロセスを自動化できます。

[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) にベーツ番号付与アーティファクトを追加するには、[`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) の `AddBatesNumbering(BatesNArtifact)` 拡張メソッドを呼び出し、パラメータとして [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/) インスタンスを渡します。

```python

import aspose.pdf as ap

def add_bates_numbering(path_outfile):
    # Create a new or empty PDF document
    with ap.Document() as document:

        # Add 10 blank pages
        for _ in range(10):
            document.pages.add()

        # Create Bates numbering artifact
        bates = ap.BatesNArtifact(
            start_page=1,
            end_page=0,  # 0 = apply until last page
            subset=ap.Subset.ALL,
            number_of_digits=6,
            start_number=1,
            prefix="",
            suffix="",
            artifact_vertical_alignment=ap.VerticalAlignment.BOTTOM,
            artifact_horizontal_alignment=ap.HorizontalAlignment.RIGHT,
            right_margin=72,
            left_margin=72,
            top_margin=36,
            bottom_margin=36
        )

        # Add Bates numbering to all pages
        document.pages.add_bates_numbering(bates)

        # Save the resulting PDF
        document.save(path_outfile)
```

または、[`PaginationArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/paginationartifact/) オブジェクトのコレクションを渡すこともできます。

```python

import aspose.pdf as ap

def add_bates_numbering_collection(path_outfile):
    with ap.Document() as document:

        # Add 10 pages
        for _ in range(10):
            document.pages.add()

        # Create Bates artifact
        bates = ap.BatesNArtifact(
            start_page=1,
            end_page=0,
            subset=ap.Subset.ALL,
            number_of_digits=6,
            start_number=1,
            prefix="",
            suffix="",
            artifact_vertical_alignment=ap.VerticalAlignment.BOTTOM,
            artifact_horizontal_alignment=ap.HorizontalAlignment.RIGHT,
            right_margin=72,
            left_margin=72,
            top_margin=36,
            bottom_margin=36
        )

        # Add as a pagination artifact list
        document.pages.add_pagination([bates])

        # Save document
        document.save(path_outfile)
```

アクションデリゲートを使用してベーツ番号付与アーティファクトを追加する：

```python

import aspose.pdf as ap

def add_bates_numbering_delegate(path_outfile):
    def configure_bates(b):
        """Configure Bates numbering artifact with desired settings."""
        b.start_page = 1
        b.end_page = 0
        b.subset = ap.Subset.ALL
        b.number_of_digits = 6
        b.start_number = 1
        b.prefix = ""
        b.suffix = ""
        b.artifact_vertical_alignment = ap.VerticalAlignment.BOTTOM
        b.artifact_horizontal_alignment = ap.HorizontalAlignment.RIGHT
        b.right_margin = 72
        b.left_margin = 72
        b.top_margin = 36
        b.bottom_margin = 36
        b.text_state.font_size = 10
    
    with ap.Document() as document:

        # Add 10 pages
        for _ in range(10):
            document.pages.add()

        # Use delegate function to configure Bates artifact
        document.pages.add_bates_numbering(configure_bates)

        # Save output PDF
        document.save(path_outfile)
```

## ベーツ番号付与の削除

[`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) からベーツ番号付与を削除するには、[`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) の `delete_bates_numbering()` メソッドを使用します。

```python

import aspose.pdf as ap

def delete_bates_numbering(path_infile, path_outfile):
    with ap.Document(path_infile) as document:

        # Remove Bates numbering from all pages
        document.pages.delete_bates_numbering()

        # Save updated document
        document.save(path_outfile)
```
