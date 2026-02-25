---
title: Python を使用したベクトルグラフィックスの操作
linktitle: ベクトルグラフィックスの操作
type: docs
weight: 100
url: /ja/python-net/working-with-vector-graphics/
description: この記事では、Python を使用した GraphicsAbsorber ツールの機能について説明します。
lastmod: "2025-05-17"
TechArticle: true
AlternativeHeadline: Python で PDF に GraphicsAbsorber ツールを使用する
Abstract: Aspose.PDF for Python via .NET の「Working with Vector Graphics」記事のドキュメントは、GraphicsAbsorber クラスを使用して PDF ドキュメント内のベクトルグラフィックを操作したい開発者向けに包括的なガイドを提供します。このクラスは、ベクトルグラフィック要素の抽出、移動、削除、複製を PDF ページ間で容易にします。
---

この章では、強力な `GraphicsAbsorber` クラスを使用して PDF ドキュメント内のベクトルグラフィックとやり取りする方法を探ります。グラフィックの移動、削除、追加が必要な場合でも、このガイドはそれらのタスクを効果的に実行する方法を示します。

## はじめに

ベクトルグラフィックは多くの PDF ドキュメントで重要な要素であり、画像、形状、その他のグラフィカル要素を表すために使用されます。Aspose.PDF は `GraphicsAbsorber` クラスを提供し、開発者がプログラムでこれらのグラフィックにアクセスし操作できるようにします。`GraphicsAbsorber` の `Visit` メソッドを使用することで、指定ページからベクトルグラフィックを抽出し、移動、削除、他のページへのコピーなどさまざまな操作を実行できます。

## グラフィックの抽出

ベクトルグラフィックを扱う最初のステップは、PDF ドキュメントからそれらを抽出することです。以下は `GraphicsAbsorber` クラスを使用して行う方法です：

1. PDF ドキュメントを開く。
1. GraphicsAbsorber を初期化する。
1. 対象ページを選択する。
1. ページからグラフィックを抽出する。
1. 抽出された要素を反復処理して表示する。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Select the first page of the document
            page = document.pages[1]
            # Use the `Visit` method to extract graphics from the page
            graphics_absorber.visit(page)
            # Display information about the extracted elements
            for element in graphics_absorber.elements:
                print(f"Page Number: {element.source_page.number}")
                print(f"Position: ({element.position.x}, {element.position.y})")
                print(f"Number of Operators: {element.operators.length}")
```

GraphicsAbsorber クラスは aspose.pdf.vector 名前空間の一部であり、PDF ドキュメント内のベクトルグラフィックとやり取りするために特別に設計されています。

## グラフィックの移動

グラフィックを抽出したら、同じページ上の別の位置に移動できます。以下はその実装方法です：

1. PDF ドキュメントを開く。
1. GraphicsAbsorber を初期化する。
1. 対象ページを選択する。
1. グラフィック要素を抽出する。
1. パフォーマンス向上のために更新を一時停止する。
1. グラフィック要素の位置を変更する。
1. 更新を再開し、変更を適用する。
1. 更新されたドキュメントを保存する。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create a GraphicsAbsorber instance
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Select the first page of the document
            page = document.pages[1]
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Temporarily suspend updates to improve performance
            graphics_absorber.suppress_update()
            # Loop through each extracted graphic element and shift its position
            for element in graphics_absorber.elements:
                position = element.position
                # Move graphics by shifting its X and Y coordinates
                element.position = ap.Point(position.x + 150, position.y - 10)
            # Resume updates and apply changes
            graphics_absorber.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

## グラフィックの削除

ページから特定のグラフィックを削除したい場合があります。Aspose.PDF for Python ではこれを実現するための 2 つの方法が提供されています：

### 方法 1: 矩形境界の使用

次の例は、Aspose.PDF for Python via .NET ライブラリを使用して、PDF ドキュメントの 1 ページ目の特定の矩形領域内にあるベクトルグラフィック要素を削除する方法を示します。このプロセスでは、定義された矩形内のグラフィック要素を特定し、PDF コンテンツを整理または変更するために削除します。

1. PDF ドキュメントを開く。
1. GraphicsAbsorber を初期化する。
1. 対象ページを選択する。
1. グラフィック要素を抽出する。
1. 対象矩形を定義する。
1. パフォーマンス向上のために更新を一時停止する。
1. 矩形内のグラフィック要素を削除する。
1. 更新を再開し、変更を適用する。
1. 更新されたドキュメントを保存する。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first page of the document
            page = document.pages[1]
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Define the rectangle where graphics will be removed
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            # Temporarily suspend updates for better performance
            graphics_absorber.suppress_update()
            # Iterate through the extracted graphic elements and remove elements inside the rectangle
            for element in graphics_absorber.elements:
                # Check if the graphic's position falls within the rectangle
                if rectangle.contains(element.position, False):
                    # Remove the graphic element
                    element.remove()
            # Resume updates and apply changes
            graphics_absorber.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

### 方法 2: 削除された要素のコレクションを使用する

次の例は、Aspose.PDF for Python via .NET ライブラリを使用して、PDF ドキュメントの 1 ページ目の特定の矩形領域内にあるベクトルグラフィック要素を削除する方法を示します。このプロセスでは、定義された矩形内のグラフィック要素を特定し、PDF コンテンツを整理または変更するために削除します。

1. PDF ドキュメントを開く。
1. GraphicsAbsorber を初期化する。
1. 対象ページを選択する。
1. 対象矩形を定義する。
1. グラフィック要素の抽出。
1. 削除用コレクションの作成。
1. 四角形内の要素を特定。
1. パフォーマンス向上のため更新を一時停止。
1. グラフィック要素の削除。
1. 更新の再開と変更の適用。
1. 更新されたドキュメントの保存。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first page of the document
            page = document.pages[1]
            # Define the rectangle where graphics will be removed
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Create a collection for the removed elements
            removed_elements_collection = ap.vector.GraphicElementCollection()
            # Add elements within the rectangle to the collection
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position,False):
                    removed_elements_collection.add(item)
            # Temporarily suppress updates for better performance
            page.contents.suppress_update()
            # Delete the selected graphic elements
            page.delete_graphics(removed_elements_collection)
            # Resume updates and apply changes
            page.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

## 別ページへのグラフィック追加

あるページから吸収したグラフィックは、同じドキュメント内の別のページに追加できます。
これを実現するための2つの方法があります：

### 方法1：個別にグラフィックを追加

次の例は、PDFドキュメントの1ページ目からベクトルグラフィック要素をコピーし、2ページ目に貼り付けるものです。この操作は、PDFドキュメント内のベクトルグラフィックの抽出と操作を可能にするGraphicsAbsorberクラスによって支援されます。

1. PDFドキュメントを開く。
1. GraphicsAbsorberを初期化する。
1. 対象ページを選択する。
1. 1ページ目からグラフィック要素を抽出する。
1. パフォーマンス向上のため2ページ目の更新を一時停止する。
1. 抽出したグラフィック要素を2ページ目に追加する。
1. 更新の再開と変更の適用。
1. 更新されたドキュメントの保存。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first and second pages
            page_1 = document.pages[1]
            page_2 = document.pages[2]
            # Extract graphic elements from the first page
            graphics_absorber.visit(page_1)
            # Temporarily suppress updates for better performance
            page_2.contents.suppress_update()
            # Add each graphic element from the first page to the second page
            for element in graphics_absorber.elements:
                element.add_on_page(page_2) # Add each graphic element to the second page.
            # Resume updates and apply changes
            page_2.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

### 方法2：コレクションとしてグラフィックを追加

次の例は、PDFドキュメントの1ページ目からベクトルグラフィック要素を複製し、2ページ目に配置するものです。これは、PDFドキュメント内のベクトルグラフィックの抽出と操作を支援するGraphicsAbsorberクラスを使用して実現します。

1. PDFドキュメントを開く。
1. GraphicsAbsorberを初期化する。
1. 対象ページを選択する。
1. 1ページ目からグラフィック要素を抽出する。
1. パフォーマンス向上のため2ページ目の更新を一時停止する。
1. 抽出したグラフィック要素を2ページ目に追加する。
1. 更新の再開と変更の適用。
1. 更新されたドキュメントの保存。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first and second pages
            page_1 = document.pages[1]
            page_2 = document.pages[2]
            # Extract graphic elements from the first page
            graphics_absorber.visit(page_1)
            # Temporarily suppress updates for better performance
            page_2.contents.suppress_update()
            # Add all graphics at once from the first page to the second page
            page_2.add_graphics(graphics_absorber.elements, None)
            # Resume updates and apply changes
            page_2.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```
