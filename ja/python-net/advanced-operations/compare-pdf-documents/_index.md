---
title: Python での PDF ドキュメントの比較
linktitle: PDF ファイルを比較
type: docs
weight: 130
url: /ja/python-net/compare-pdf-documents/
description: .NET 経由で Aspose.PDF for Python を使用して、並べて表示したりグラフィカルな差分出力を行ったりして Python の PDF ドキュメントを比較する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python での視覚的な違いによる出力で PDF ページとドキュメント全体を比較
Abstract: この記事では、.NET 経由で Aspose.PDF for Python の PDF ドキュメントを比較する方法について説明します。特定のページまたは PDF ファイル全体を並べて出力する方法と、グラフィカルな比較方法を使用して画像ベースまたは PDF ベースの差分レポートを生成する方法を学びます。
---

## PDF ドキュメントを比較する方法

PDF 文書を扱う場合、2 つの文書の内容を比較して違いを見分ける必要がある場合があります。.NET ライブラリ経由の Python 用 Aspose.PDF は、この目的のための強力なツールセットを提供します。この記事では、2 つの簡単なコードスニペットを使用して PDF 文書を比較する方法を探ります。

ページ間でテキストやレイアウトの変更が強調表示される PDF 出力が必要な場合は、横に並べて比較します。視覚的なレビューワークフロー、回帰チェック、または PDF 比較レポート用に画像ベースの差異検出が必要な場合は、グラフィカル比較を使用してください。

Aspose.PDF の比較機能を使用すると、2 つの PDF ドキュメントを 1 ページずつ比較できます。特定のページを比較するか、文書全体を比較するかを選択できます。結果の比較文書では相違点が強調表示されるため、2 つのファイル間の変更を簡単に識別できます。

.NET ライブラリ経由で Aspose.PDF for Python を使用して PDF ドキュメントを比較する方法は次のとおりです。

1. **特定のページの比較**-2 つの PDF 文書の最初のページを比較します。
1. **文書全体の比較**-2 つの PDF 文書の内容全体を比較します。
1. ** PDF ドキュメントをグラフィカルに比較**:

- 「comparer.get_difference」メソッド（変更がマークされている個々の画像）を使用して PDF を比較します。
- 「comparer.compare_documents_to_pdf」メソッドで PDF を比較します。つまり、変更がマークされた画像を含む PDF ドキュメント。

## 特定のページの比較

最初のコードスニペットは、SidebySidePDFComparer クラスを使用して 2 つの PDF ドキュメントの最初のページを比較する方法を示しています。

1. ドキュメント初期化。
1. 比較を実行する関数を作成します。
1. 比較プロセス:

- document1.pages [1] と document2.pages [1]:-これらは比較する各ドキュメントの最初のページを指定します。Aspose.PDF では、ページのインデックスは 1 から始まることに注意してください。
- サイドバイサイド比較オプション-このクラスでは比較動作をカスタマイズできます。
- additional_change_marks = True-比較中の現在のページにない場合でも、他のページに存在する可能性のある相違点を強調表示して、追加の変更マーカーを表示できるようにします。
- comparison_mode = comparisonMode.IgnoreSpaces-テキスト内のスペースを無視し、単語内の変更のみに焦点を当てるように比較モードを設定します。

1. 比較の結果は、指定された data_dir に ComparingSpecificPages_out.pdf という名前の新しい PDF ファイルとして保存されます。

```python
import aspose.pdf as ap
import sys
from os import path

def comparing_specific_pages(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Compare
    options = ap.comparison.SideBySideComparisonOptions()
    options.additional_change_marks = True
    options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES

    # Perform comparison and save the result
    ap.comparison.SideBySidePdfComparer.compare(
        document_1.pages[1], document_2.pages[1], outfile, options
    )
```

## 文書全体の比較

2 番目のコードスニペットでは、2 つの PDF ドキュメントの内容全体を比較できるように範囲を広げています。

```python
import aspose.pdf as ap
import sys
from os import path

def comparing_entire_documents(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Compare
    options = ap.comparison.SideBySideComparisonOptions()
    options.additional_change_marks = True
    options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES

    # Perform comparison and save the result
    ap.comparison.SideBySidePdfComparer.compare(
        document_1, document_2, outfile, options
    )
```

提供されているコードは、.NET 経由で Aspose.PDF for Python を使用して 2 つの PDF ドキュメントを比較する方法を示しています。このコードでは、SidebySidePDFComparer クラスを利用してページごとの比較を行い、相違点を並べて表示する新しい PDF を生成します。比較は SideBySideComparisonOptions で設定されます。additional_change_marks を True に設定すると、現在のページだけでなく他のページの変更も強調表示され、comparison_mode は IgnoreSpaces に設定されているため、空白のバリエーションを無視して意味のある内容の違いに焦点を当てることができます。

## グラフィカル PDF 比較ツールを使用して比較

特にプロフェッショナルな環境で文書を共同編集する場合、同じファイルの複数のバージョンが作成されることがよくあります。
提供されているコードは、.NET 経由の Aspose.PDF for Python を使用して 2 つの PDF ドキュメントの特定のページを視覚的に比較する方法を示しています。を使用して `GraphicalPdfComparer` クラスでは、2つのPDFの最初のページの違いを強調表示し、それらの違いを表す対応する画像を生成します。

次のクラスプロパティを設定できます。

- 解像度-出力画像と比較中に生成された画像のDPI単位の解像度。
- 色-変更マークの色。
- しきい値-しきい値をパーセント単位で変更します。デフォルト値は 0 です。0 以外の値を設定すると、自分にとって重要でないグラフィックの変更を無視できます。

.NET 経由の Python 用 Aspose.PDF を使用すると、ドキュメントとページを比較し、比較結果を PDF ドキュメントまたは画像ファイルに出力できます。

ザの `GraphicalPdfComparer` クラスには、ページ画像の違いを今後の処理に適した形式で取得できるメソッドがあります。 `get_difference(document1.pages[1], document2.pages[1])`.

このメソッドは、次のオブジェクトを返します。 `images_difference` type には、比較対象の最初のページの画像と相違点の配列が含まれます。

ザの `images_difference` object を使用すると、元の画像に差分の配列を適用することで、別の画像を生成し、比較対象の 2 ページ目の画像を取得できます。そのためには、 `difference_to_image` そして `get_destination_image` 方法。

### 差分取得メソッドによる PDF の比較

提供されたコードはメソッドを定義します `get_difference` 2 つの PDF ドキュメントを比較し、それらの違いを視覚的に表現します。

このメソッドは、2 つの PDF ファイルの最初のページを比較し、2 つの PNG 画像を生成します。

- 1つの画像は、ページ間の違いを赤で強調しています。
- もう 1 つの画像は、移動先 (2 番目の) PDF ページを視覚的に表現したものです。

このプロセスは、文書の 2 つのバージョン間の変更や相違点を視覚的に比較する場合に便利です。

```python
import aspose.pdf as ap
import sys
from os import path

def compare_pdf_with_get_difference_method(infile1, infile2, outfile1, outfile2):
    # Open PDF documents
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)

    # Create comparer
    comparer = ap.comparison.GraphicalPdfComparer()

    # Compare specific pages
    images_difference = comparer.get_difference(document1.pages[1], document2.pages[1])

    # Get image showing differences in red over a white background
    diff_img = images_difference.difference_to_image(ap.Color.red, ap.Color.white)
    diff_img.save(outfile1)

    # Get the second image representing the destination page
    dest_img = images_difference.get_destination_image()
    dest_img.save(outfile2)
```

### PDF と PDF の比較方法による文書の比較

提供されているコードスニペットは `compare_documents_to_pdf` メソッド。2 つのドキュメントを比較し、比較結果の PDF レポートを生成します。

```python
import aspose.pdf as ap
import sys
from os import path

def compare_pdf_with_compare_documents_to_pdf_method(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Create comparer and set options
    pdf_comparer = ap.comparison.GraphicalPdfComparer()
    pdf_comparer.threshold = 3.0
    pdf_comparer.color = ap.Color.blue
    pdf_comparer.resolution = ap.devices.Resolution(300)

    # Compare and output to a PDF file
    pdf_comparer.compare_documents_to_pdf(document_1, document_2, outfile)
```

この例は、.NET 経由で Aspose.PDF for Python を使用して 2 つの PDF ドキュメント全体をグラフィカルに比較する方法を示しています。を活用することで `GraphicalPdfComparer` クラス、ドキュメント間の違いを視覚的に強調する新しいPDFファイルを生成します。

- しきい値プロパティは 3.0 に設定されています。つまり、このパーセンテージを下回るわずかな違いは比較時に無視され、より重要な変更に注目します。
- color プロパティを ap.color.blue に設定すると、違いが青で示され、視覚的に区別しやすくなります。
- 解像度プロパティを設定することにより、300 DPIの解像度で比較が行われ、詳細で明確な出力が得られます。

ザの `compare_documents_to_pdf` メソッドは、両方の文書のすべてのページを比較し、その結果を新しい PDF ファイル compareDocumentsToPdf_out.pdf に出力します。差異は視覚的に強調表示されます。

## 関連トピック

- [Python での高度な PDF 操作](/pdf/ja/python-net/advanced-operations/)
- [Python で PDF ドキュメントを操作する](/pdf/ja/python-net/working-with-documents/)
- [Python で PDF ページを操作する](/pdf/ja/python-net/working-with-pages/)
- [Python で PDF テキストを操作する](/pdf/ja/python-net/working-with-text/)
