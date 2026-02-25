---
title: PDF ドキュメントを比較する
linktitle: PDF を比較
type: docs
weight: 130
url: /ja/python-net/compare-pdf-documents/
description: PDF ドキュメントの内容を注釈マークと並べて出力で比較することが可能です。
lastmod: "2025-05-12"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 
Abstract: 
---

## PDF ドキュメントの比較方法

PDF ドキュメントを扱う際、2 つのドキュメントの内容を比較して違いを特定する必要があることがあります。Aspose.PDF for Python via .NET ライブラリは、この目的のための強力なツールセットを提供します。本記事では、簡単なコードスニペットをいくつか使って PDF ドキュメントを比較する方法を探ります。

Aspose.PDF の比較機能を使用すると、2 つの PDF ドキュメントをページ単位で比較できます。特定のページだけを比較することも、ドキュメント全体を比較することも可能です。結果として得られる比較ドキュメントは違いをハイライトし、2 つのファイル間の変更点を容易に識別できるようにします。

以下は、Aspose.PDF for Python via .NET ライブラリを使用して PDF ドキュメントを比較する可能な方法の一覧です：

1. **特定のページを比較** - 2 つの PDF ドキュメントの最初のページを比較します。
1. **ドキュメント全体を比較** - 2 つの PDF ドキュメントの全内容を比較します。
1. **PDF ドキュメントをグラフィカルに比較**：

- 'comparer.get_difference' メソッドを使用して PDF を比較 - 変更がマークされた個別画像。
- 'comparer.compare_documents_to_pdf' メソッドを使用して PDF を比較 - 変更がマークされた画像を含む PDF ドキュメント。

## 特定のページを比較

最初のコードスニペットは、SideBySidePdfComparer クラスを使用して 2 つの PDF ドキュメントの最初のページを比較する方法を示しています。

1. ドキュメントの初期化。
1. 比較を実行する関数を作成します。
1. 比較プロセス：

- document1.pages[1] と document2.pages[1]：- それぞれのドキュメントの最初のページを指定します。Aspose.PDF ではページインデックスは 1 から始まることに注意してください。
- SideBySideComparisonOptions - このクラスは比較動作のカスタマイズを可能にします。
- additional_change_marks = True - 変更マークを追加表示できるようにし、現在比較しているページにないページでも差分がハイライトされます。
- comparison_mode = ComparisonMode.IgnoreSpaces - テキストのスペースを無視する比較モードを設定し、単語内の変更のみを対象とします。

1. 比較結果は、指定された data_dir に ComparingSpecificPages_out.pdf という名前の新しい PDF ファイルとして保存されます。

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import SideBySidePdfComparer, SideBySideComparisonOptions, ComparisonMode

    def comparing_specific_pages():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparingSpecificPages1.pdf")
        document2 = ap.Document(data_dir + "ComparingSpecificPages2.pdf")

        # Compare
        options = SideBySideComparisonOptions()
        options.additional_change_marks = True
        options.comparison_mode = ComparisonMode.IgnoreSpaces

        # Perform comparison and save the result
        SideBySidePdfComparer.compare(document1.pages[1], document2.pages[1], data_dir + "ComparingSpecificPages_out.pdf", options)
```

## ドキュメント全体を比較

2 番目のコードスニペットは、2 つの PDF ドキュメントの全体内容を比較するよう範囲を拡大します。

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import SideBySidePdfComparer, SideBySideComparisonOptions, ComparisonMode

    def comparing_entire_documents():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparingEntireDocuments1.pdf")
        document2 = ap.Document(data_dir + "ComparingEntireDocuments2.pdf")

        # Compare
        options = SideBySideComparisonOptions()
        options.additional_change_marks = True
        options.comparison_mode = ComparisonMode.IgnoreSpaces

        # Perform comparison and save the result
        SideBySidePdfComparer.compare(document1, document2, data_dir + "ComparingEntireDocuments_out.pdf", options)
```

提供されたコードは、Aspose.PDF for Python via .NET を使用して 2 つの PDF ドキュメントを比較する方法を示しています。SideBySidePdfComparer クラスを利用してページごとの比較を実行し、差分を並べて表示する新しい PDF を生成します。比較は SideBySideComparisonOptions で構成され、additional_change_marks が True に設定されているため、現在のページだけでなく他のページの変更もハイライトされ、comparison_mode が IgnoreSpaces に設定されているため、空白の違いを無視して実質的な内容の違いに焦点を当てます。

## GraphicalPdfComparer を使用した比較

ドキュメントで共同作業を行う際、特にプロの環境では、同じファイルの複数バージョンが存在することがよくあります。
提供されたコードは、Aspose.PDF for Python via .NET を使用して 2 つの PDF ドキュメントの特定のページを視覚的に比較する方法を示しています。`GraphicalPdfComparer` クラスを使用することで、2 つの PDF の最初のページ間の違いをハイライトし、差分を表す画像を生成します。

以下のクラスプロパティを設定できます：

- Resolution - 出力画像および比較中に生成される画像の DPI 解像度。
- Color - 変更マークの色。
- Threshold - 変更閾値（パーセンテージ）。デフォルトは 0 です。0 以外の値を設定すると、重要でないグラフィックの変更を無視できます。

Aspose.PDF for Python via .NET を使用すると、ドキュメントやページを比較し、比較結果を PDF ドキュメントまたは画像ファイルとして出力することが可能です。

`GraphicalPdfComparer` クラスには、`get_difference(document1.pages[1], document2.pages[1])` のように、さらなる処理に適した形でページ画像の差分を取得できるメソッドがあります。

このメソッドは `images_difference` 型のオブジェクトを返し、比較対象の最初のページの画像と差分の配列を含みます。

`images_difference` オブジェクトを使用すると、元の画像に差分配列を適用して別の画像を生成し、比較対象の2ページ目の画像を取得できます。このためには `difference_to_image` および `get_destination_image` メソッドを使用します。

### Get Difference メソッドで PDF を比較

提供されたコードは、`get_difference` メソッドを定義し、2 つの PDF ドキュメントを比較して、双方の差分の視覚的表現を生成します。

このメソッドは、2 つの PDF ファイルの最初のページを比較し、2 つの PNG 画像を生成します：

- 1 つの画像は、ページ間の違いを赤色でハイライトします。
- 他の画像は目的地（2番目）のPDFページの視覚的表現です。

このプロセスは、ドキュメントの2つのバージョン間の変更や違いを視覚的に比較するのに役立ちます。

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import GraphicalPdfComparer

    def compare_pdf_with_get_difference_method():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparePDFWithGetDifferenceMethod1.pdf")
        document2 = ap.Document(data_dir + "ComparePDFWithGetDifferenceMethod2.pdf")

        # Create comparer
        comparer = GraphicalPdfComparer()

        # Compare specific pages
        images_difference = comparer.get_difference(document1.pages[1], document2.pages[1])

        # Get image showing differences in red over a white background
        diff_img = images_difference.difference_to_image(ap.Color.red, ap.Color.white)
        diff_img.save(data_dir + "ComparePDFWithGetDifferenceMethodDiffPngFilePath_out.png")

        # Get the second image representing the destination page
        dest_img = images_difference.get_destination_image()
        dest_img.save(data_dir + "ComparePDFWithGetDifferenceMethodDestPngFilePath_out.png")
```

### CompareDocumentsToPdf メソッドで PDF を比較

提供されたコードスニペットは `compare_documents_to_pdf` メソッドを使用し、2つのドキュメントを比較して比較結果のPDFレポートを生成します。

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import GraphicalPdfComparer
    from aspose.pdf.devices import Resolution

    def compare_pdf_with_compare_documents_to_pdf_method():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparePDFWithCompareDocumentsToPdfMethod1.pdf")
        document2 = ap.Document(data_dir + "ComparePDFWithCompareDocumentsToPdfMethod2.pdf")

        # Create comparer and set options
        comparer = GraphicalPdfComparer()
        comparer.threshold = 3.0
        comparer.color = ap.Color.blue
        comparer.resolution = Resolution(300)

        # Compare and output to a PDF file
        comparer.compare_documents_to_pdf(document1, document2, data_dir + "compareDocumentsToPdf_out.pdf")
```

この例では、Aspose.PDF for Python via .NET を使用して2つのPDF文書全体をグラフィカルに比較する方法を示しています。`GraphicalPdfComparer` クラスを活用することで、文書間の差異を視覚的に強調表示した新しいPDFファイルを生成します。

- threshold プロパティは 3.0 に設定されており、このパーセンテージ未満の小さな差異は比較時に無視され、より重要な変更に焦点を当てます。
- color プロパティを ap.Color.blue に設定することで、差異が青色でマークされ、視覚的に明確に区別できます。
- resolution プロパティを設定して、比較を 300 DPI の解像度で実行し、詳細で明確な出力を保証します。

`compare_documents_to_pdf` メソッドは両方のドキュメントのすべてのページを比較し、結果を新しいPDFファイル compareDocumentsToPdf_out.pdf に出力し、差異を視覚的にハイライトします。

