---
title: Python での PDF テキストの検索と抽出
linktitle: テキストを検索して取得
type: docs
weight: 60
url: /ja/python-net/search-and-get-text-from-pdf/
description: Python で PDF ドキュメントを検索、検査、テキストを抽出する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python で PDF テキストを検索し、抽出されたフラグメントを検査する
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメントからテキストを検索および抽出する方法について説明します。地域ベースの抽出、ページ固有の検索、フレーズの照合、テキストの位置とフォントのプロパティの検査など、「TextAbSorber」と「TextFragmentAbSorber」について説明します。
---

## PDF からテキストを検索

を使用して、PDF ドキュメント内の定義済みの四角形領域からテキストを検索および抽出します。 `TextAbsorber` クラス。ピュア・テキスト・フォーマット・モードを使用するため、ヘッダー、フッター、表領域などの構造化された領域からコンテンツを抽出する場合に便利です。組み合わせることによって `TextExtractionOptions` そして `TextSearchOptions` 矩形コンストレイントを使用すると、テキストを抽出する場所と方法を制御できます。

このページは、PDF テキストコンテンツの監査、分析用のテキストの抽出、または一致したテキストフラグメントの位置やフォーマットの検査を行う必要がある場合に使用します。

1. 「AP.ドキュメント」を使用してPDFファイルをロードします。
1. テキスト抽出オプションを設定します。
1. 四角形の制約を使用して検索領域を定義します。
1. テキストアブソーバーを作成して設定します。
1. 文書内のすべてのページを処理します。
1. 抽出されたテキストを取得して表示します。

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_absorber_search(input_file_path):
    # Open PDF document
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Process all pages
    document.pages.accept(absorber)

    print(f"Text fragments found: {absorber.text}")
```

## 特定の PDF ページからテキストを検索する

Aspose.PDF の TextAbsorber を使用して、PDF 内の特定のページや領域からテキストを検索して抽出します。文書の 2 ページ目を対象とし、定義した長方形の領域内にあるテキストのみを抽出します。
TextExtractionOptions (フォーマット制御用) と TextSearchOptions (領域制限用) を組み合わせることにより、ページ固有の正確なテキスト抽出を効率的に実行できます。

1. PDF ドキュメントをロードします。
1. テキスト抽出オプションを設定します。
1. テキスト抽出をページ上の特定の四角形領域に制限します。
1. テキストアブソーバーを作成して設定します。
1. 特定のページを処理します。
1. 抽出されたテキストを取得して表示します。

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_absorber_search_page(input_file_path):
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Only page 2
    document.pages[2].accept(absorber)

    print(f"Text fragments found: {absorber.text}")
```

## PDF からの詳細なテキストフラグメントプロパティの分析と抽出

生のテキストを抽出する TextAbsorber とは異なり、TextFragmentAbsorber は、位置、フォント属性、色、埋め込みの詳細など、各テキストフラグメントに関する詳細な低レベルの情報を提供します。

1. PDF ドキュメントをロードします。
1. テキストフラグメントアブソーバーを初期化します。
1. 文書内のすべてのページを処理します。
1. 抽出されたテキストフラグメントを繰り返し処理します。
1. 基本的なテキスト情報を印刷します。
1. フォントと書式の詳細を印刷します。

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    document.pages.accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
        print("XIndent:", fragment.position.x_indent)
        print("YIndent:", fragment.position.y_indent)
        print("Font - Name:", fragment.text_state.font.font_name)
        print("Font - IsAccessible:", fragment.text_state.font.is_accessible)
        print("Font - IsEmbedded:", fragment.text_state.font.is_embedded)
        print("Font - IsSubset:", fragment.text_state.font.is_subset)
        print("Font Size:", fragment.text_state.font_size)
        print("Foreground Color:", fragment.text_state.foreground_color)
```

## 単一の PDF ページで特定のテキストフレーズを検索する

TextFragmentAbsorber を使用して、PDF ドキュメントのページ内の特定のテキストフレーズを検索します。文書全体を検索する場合とは異なり、この方法では検索が 1 ページのみに制限されるため、ヘッダー、フッター、特定のコンテンツセクションなどの対象領域にあるテキストの存在と位置をより効率的に確認できます。

1. PDF ドキュメントをロードします。
1. テキストフラグメントアブソーバーを検索フレーズで初期化します。
1. 特定のページにアブソーバーを適用します。
1. 見つかったフラグメントを繰り返し処理します。

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_page(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale")
    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## 累積結果を含むページ単位の連続テキスト検索

Aspose.PDF の TextFragmentAbsorber を使用して、PDF ドキュメントの複数のページにわたってテキストを段階的に検索します。
単一ページ検索や文書全体検索とは異なり、この方法では、ページを順番に処理し、結果を段階的に収集し、ページ固有のコンテキストでテキストフラグメントを分析できます。この方法は、サイズの大きい文書や段階的な処理ワークフローに最適です。

1. PDF ドキュメントをロードします。
1. テキストフラグメントアブソーバーを初期化し、検索フレーズを設定します。
1. 最初のページを処理します。1 ページ目のみを検索します。テキスト、ページ番号、位置を印刷します。わかりやすくするために、ページ固有の結果を分離して提供してください。
1. 次のページを順番に処理します。2 ページ目に移動し、必要に応じてドキュメントの残りの部分に進みます。'absorber.visit () 'を使うと、訪問したすべてのページからの結果が確実に蓄積されます。テキストと場所の両方を表示して、累積検索結果を出力します。

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_sequential_search(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.phrase = "whale"

    # First page
    document.pages[1].accept(absorber)
    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)

    print("--")

    # Continue to next page
    document.pages[2].accept(absorber)
    absorber.visit(document)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)
```

## 長方形の領域内でのターゲットフレーズ検索

PDF 内の特定の語句を検索し、1 ページの特定の四角形領域に検索を制限します。
フレーズ検索と空間的制約を組み合わせることで、ページや文書全体をスキャンしなくても、指定された領域のコンテンツを正確に見つけることができます。これは、コンテンツが予測可能な場所に表示されるフォーム、ヘッダー、フッター、または構造化レポートに特に役立ちます。

1. PDF ドキュメントをロードします。
1. テキストフラグメントアブソーバーをフレーズ制約と四角形制約で初期化
1. 2ページ目にアブソーバーを塗布します。処理を 2 ページ目に制限し、不要な計算を減らします。検索がページ固有であることを保証します。
1. 見つかったフラグメントを繰り返し処理して印刷する

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_phrase(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        "elephant", ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## 正規表現を使用した PDF のテキストパターン検索

正規表現を使用して PDF 内のテキストパターンを検索します。TextFragmentAbsorber で正規表現モードを有効にすると、数字、日付、価格、座標、カスタムテキスト形式などの複雑なパターンを検索できます。この関数は検索を特定のページに制限するので、構造化データを的を絞って効率的に抽出できます。

1. PDF ドキュメントをロードします。
1. テキストフラグメントアブソーバーを正規表現パターンで初期化します。
1. 2ページ目にアブソーバーを塗布します。効率と精度を高めるため、検索を 2 ページ目に制限します。このページのテキストのみが分析されます。
1. 見つかったフラグメントを繰り返し処理します。一致するテキストフラグメントとその座標を出力します。抽出されたパターンの正確な位置情報を提供します。

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_regex(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        r"\d+\.\d+", ap.text.TextSearchOptions(is_regular_expression_used=True)
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## テキストフラグメントアブソーバーを使用して PDF 内のテキストマッチをハイパーリンクに変換

PDF 内の特定のテキストフレーズを検索し、クリック可能なハイパーリンクに変換します。TextFragmentAbsorber を正規表現パターンとともに使用することで、ターゲットとなる単語を検索し、インタラクティブなリンクとともに視覚的なスタイル (色と下線) を適用します。

1. PDF ドキュメントをロードします。
1. テキストフラグメントアブソーバーを正規表現パターンで初期化します。
1. 1ページ目にアブソーバーを塗布します。
1. スタイルを設定してマッチにハイパーリンクを追加します。
1. 変更した PDF を保存します。

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_and_add_hyperlink(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale|elephant")
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.underline = True
        fragment.hyperlink = ap.WebHyperlink(
            f"https://en.wikipedia.org/wiki/{fragment.text}"
        )

    output = input_file_path.replace("in.pdf", "out.pdf")
    document.save(output)
```

## TextFragmentAbsorber を使用して PDF 内のスタイル付きテキストを検索および識別する

PDF 内のテキストフラグメントを、コンテンツではなくフォーマットプロパティに基づいて検索します。TextFragmentAbsorber を使用すると、太字テキストなどの特定のスタイルのテキストを識別できます。

1. PDF ドキュメントをロードします。
1. テキストフラグメントアブソーバーを初期化します。
1. 1ページ目にアブソーバーを塗布します。
1. フォーマットに基づいてテキストフラグメントを検査します。フォントスタイルが太字になっているかどうかをチェックします。

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_styled_text(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.font_style == ap.text.FontStyles.BOLD:
            print(f"Bold: {fragment.text}")
        if fragment.text_state.invisible:
            print(f"Invisible: {fragment.text}")
```

## PDF ページでのビジュアルテキストハイライト

この機能は、テキスト認識とレンダリングを単一のワークフローに統合します。テキストを抽出するだけでなく、各ページの PNG 画像上の色分けされた長方形の断片、セグメント、文字をハイライトして視覚化します。

この例では、次の方法で PDF の高度なテキストビジュアライゼーションを実行します。

- 正規表現を使用して表示されているすべてのテキストフラグメントを検索する
- 各 PDF ページを高解像度 PNG 画像にレンダリングする
- テキストフラグメント、テキストセグメント、および個々の文字の周囲に色付きの長方形を描く

1. 出力画像の解像度を設定します。各 PDF ページは 150 DPI の PNG イメージに変換されます。
1. PDF を開き、テキストアブソーバーを初期化します。
1. 各ページを処理します。すべてのページにアブソーバーを塗布します。検出されたすべてのテキストフラグメントとその幾何学的位置を収集します。
1. ページを PNG ストリームに変換します。
1. 描画用のグラフィックスオブジェクトを準備します。
1. 座標変換を適用します。PDF 座標を画像ピクセルに変換します。
1. テキスト要素に長方形を描画します。
1. 結果を保存します。

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_and_highlight(infile):
    resolution = 150
    png_device = ap.devices.PngDevice(ap.devices.Resolution(resolution, resolution))

    # Open PDF document
    document = ap.Document(infile)
    absorber = ap.text.TextFragmentAbsorber(r"[\S]+")
    absorber.text_search_options.is_regular_expression_used = True

    for page in document.pages:
        page.accept(absorber)
        stream = io.BytesIO()
        png_device.process(page, stream)
        with drawing.Bitmap.from_stream(stream) as bmp:
            with drawing.Graphics.from_image(bmp) as gr:
                scale = resolution / 72
                gr.transform = drawing.drawing2d.Matrix(
                    float(scale),
                    float(0),
                    float(0),
                    float(-scale),
                    float(0),
                    float(bmp.height),
                )
                text_fragment_collection = absorber.text_fragments
                # Loop through the fragments
                for text_fragment in text_fragment_collection:
                    gr.draw_rectangle(
                        drawing.Pens.yellow,
                        float(text_fragment.position.x_indent),
                        float(text_fragment.position.y_indent),
                        float(text_fragment.rectangle.width),
                        float(text_fragment.rectangle.height),
                    )
                    for seg_num in range(1, len(text_fragment.segments) + 1):
                        segment = text_fragment.segments[seg_num]
                        for char_num in range(1, len(segment.characters) + 1):
                            character_info = segment.characters[char_num]
                            rect = page.get_page_rect(True)
                            print(
                                f"TextFragment = {text_fragment.text}"
                                + f" Page URY = {rect.ury}"
                                + f" TextFragment URY = {text_fragment.rectangle.ury}"
                            )
                            gr.draw_rectangle(
                                drawing.Pens.black,
                                float(character_info.rectangle.llx),
                                float(character_info.rectangle.lly),
                                float(character_info.rectangle.width),
                                float(character_info.rectangle.height),
                            )
                        gr.draw_rectangle(
                            drawing.Pens.green,
                            float(segment.rectangle.llx),
                            float(segment.rectangle.lly),
                            float(segment.rectangle.width),
                            float(segment.rectangle.height),
                        )

                # Save result
                bmp.save(
                    infile.replace("_in.pdf", str(page.number) + "_out.png"),
                    drawing.imaging.ImageFormat.png,
                )
```

## 関連テキストトピック

- [Python を使用して PDF 内のテキストを操作する](/pdf/ja/python-net/working-with-text/)
- [Python を使用して PDF 内のテキストを置き換える](/pdf/ja/python-net/replace-text-in-pdf/)
- [Python で PDF テキストにツールチップを追加する方法](/pdf/ja/python-net/pdf-tooltip/)
- [PDF へのテキストの追加](/pdf/ja/python-net/add-text-to-pdf-file/)