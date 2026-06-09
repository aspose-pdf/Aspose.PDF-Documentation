---
title: Python で PDF テキストを回転させる
linktitle: PDF 内のテキストを回転
type: docs
weight: 50
url: /ja/python-net/rotate-text-inside-pdf/
description: Python で PDF ドキュメント内のテキストフラグメントと段落を回転させる方法を学びます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用して PDF ドキュメント内のテキストフラグメントと段落を回転させる
Abstract: この記事では、.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメント内のテキストを回転する方法について説明します。さまざまなレイアウトシナリオで、`TextFragment` に `rotation` プロパティを設定する方法、`TextBuilder` と `TextParagraph` を使用して回転したコンテンツを作成する方法、回転したテキストをページの段落に直接追加する方法を示します。
---

.NET 経由で Aspose.PDF for Python を使用して PDF ドキュメント内のテキストフラグメントをローテーションします。このページでは、を使用してテキストの位置と回転を制御する方法を説明します。 `TextFragment`, `TextState`、および `TextBuilder`。回転角度を調整することで、斜めヘッダー、垂直ラベル、回転した注釈などのレイアウトを作成できます。

## PDF のテキストビルダーを使用してテキストフラグメントを回転させる

という名前の PDF ファイルを作成します `rotated_fragments.pdf` 水平方向に整列された 3 つのテキストフラグメントを含む:

- 最初のテキストは回転されていません
- 2つ目は45°回転します
- 3つ目は90°回転します

1. 新しい PDF ドキュメントを作成します。
1. 回転したテキストをホストする新しいページを挿入します。
1. 最初のテキストフラグメントを作成します (回転なし)。
1. 2 番目のテキストフラグメントを作成します (45°回転)。
1. 3 番目のテキストフラグメントを作成します (90 度回転)。
1. を使用してテキストフラグメントを追加します `TextBuilder`.
1. 文書を保存します。

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_1(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        text_fragment_1.position = ap.text.Position(100, 600)
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create rotated text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        text_fragment_2.position = ap.text.Position(200, 600)
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        text_fragment_2.text_state.rotation = 45
        # Create rotated text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        text_fragment_3.position = ap.text.Position(300, 600)
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        text_fragment_3.text_state.rotation = 90
        # create TextBuilder object
        builder = ap.text.TextBuilder(page)
        # Append the text fragment to the PDF page
        builder.append_text(text_fragment_1)
        builder.append_text(text_fragment_2)
        builder.append_text(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## PDF の段落内の個々のテキストフラグメントを回転させる

段落内の個々のテキストフラグメントを回転します。それぞれが独自の回転角度を持つ複数のフラグメント（TextFragment）を含む複数行の段落（TextParagraph）を作成する方法を示します。この手法は、定型化されたヘッダー、図、注釈付きラベルなど、横向きのテキストと斜め向きのテキストを組み合わせた、見た目が豊かな文書を作成する場合に便利です。

という名前の PDF を作成します `rotated_paragraph_fragments.pdf` 3 行のテキストを含む段落で、各行の向きが異なります。

- 最初の線は 45°回転します
- 2 本目の線は水平 (0°) のままです
- 3 本目の線は -45 度回転します

1. 新しい PDF ドキュメントを作成します。
1. 回転したテキストが表示される空白ページを追加します。
1. を作成 `TextParagraph`.
1. 最初のテキストフラグメントを作成して設定します (+45°回転)。
1. 2 番目のテキストフラグメントを作成します (回転なし)。
1. 3 番目のテキストフラグメントを作成します (-45 度回転)。
1. 段落にテキストフラグメントを追加します。
1. を使用して段落をページに追加します `TextBuilder`.
1. 文書を保存します。

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_2(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        paragraph = ap.text.TextParagraph()
        paragraph.position = ap.text.Position(200, 600)
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_1.text_state.rotation = 45
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("another rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_3.text_state.rotation = -45
        # Append the text fragments to the paragraph
        paragraph.append_line(text_fragment_1)
        paragraph.append_line(text_fragment_2)
        paragraph.append_line(text_fragment_3)
        # Create TextBuilder object
        text_builder = ap.text.TextBuilder(page)
        # Append the text paragraph to the PDF page
        text_builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```

## PDF のページ段落を使用してテキストを回転する

このセクションでは、.NET 経由で Aspose.PDF for Python を使用して PDF 内のテキストを回転させる簡単な方法を紹介します。
との低レベルのアプローチとは異なり `TextBuilder` または `TextParagraph`、このメソッドは、回転したテキストフラグメントをページの段落コレクションに直接追加します (`page.paragraphs`)。基本的なテキストローテーションは必要だが、正確な配置や段落構造は必要ない場合に最適です。

という名前のファイルを生成します `simple_rotated_text.pdf` 含む:

- メインの水平テキストフラグメント (0°回転)
- 315°回転したフラグメント
- 270°回転したフラグメント

1. 新しい PDF ドキュメントを初期化します。
1. 回転したテキストが配置されるページを作成します。
1. 最初のテキストフラグメントを作成します (回転なし)。
1. 2 番目のテキストフラグメントを作成します (315° 回転)。
1. 3 番目のテキストフラグメントを作成します (270°回転)。
1. テキストフラグメントをページの段落に直接追加します。
1. PDF ドキュメントを保存します。

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_3(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_2.text_state.rotation = 315
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_3.text_state.rotation = 270
        page.paragraphs.add(text_fragment_1)
        page.paragraphs.add(text_fragment_2)
        page.paragraphs.add(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## PDF の段落全体を回転

この例は、PDF の高度な段落レベルのテキスト回転を示しています。フラグメントレベルの回転（各テキストが個別に回転する）とは異なり、この方法では段落全体が統一されたブロックとしてさまざまな角度で回転します。
各段落には複数のスタイル付きテキストフラグメントが含まれており、段落全体が特定の角度で回転するため、複雑で一貫したレイアウト変換が可能です。
これは、芸術的なレイアウト、ウォーターマーク、またはテキストセクション全体をさまざまな方向に向ける必要があるデザイン重視のPDFに最適です。

作成する `rotated_paragraphs.pdf`には、完全にスタイルが設定され、回転した4つの段落が含まれています。

- それぞれが独自の角度（45度、135度、225度、315度）で回転しています
- 各段落には、色付きの背景、下線が引かれ、一貫したスタイルが設定された3行のテキストがあります

1. 新しい PDF ドキュメントを作成します。
1. 回転した段落を格納する空白ページを追加します。
1. 繰り返し処理して複数の段落を作成します。
1. 段落を作成して配置します。
1. 書式を設定したテキストフラグメントを作成します。
1. テキストフォーマットを適用します。
1. 段落にテキストフラグメントを追加します。
1. を使用して段落をページに追加します `TextBuilder`.
1. 4 つの回転すべてについて繰り返します。
1. PDF ドキュメントを保存します。

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_4(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        for i in range(4):
            paragraph = ap.text.TextParagraph()
            paragraph.position = ap.text.Position(200, 600)
            # Specify rotation
            paragraph.rotation = i * 90 + 45
            # Create text fragment
            text_fragment_1 = ap.text.TextFragment("Paragraph Text")
            # Create text fragment
            text_fragment_1.text_state.font_size = 12
            text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_1.text_state.background_color = ap.Color.light_gray
            text_fragment_1.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_2 = ap.text.TextFragment("Second line of text")
            # Set text properties
            text_fragment_2.text_state.font_size = 12
            text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_2.text_state.background_color = ap.Color.light_gray
            text_fragment_2.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_3 = ap.text.TextFragment("And some more text...")
            # Set text properties
            text_fragment_3.text_state.font_size = 12
            text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_3.text_state.background_color = ap.Color.light_gray
            text_fragment_3.text_state.foreground_color = ap.Color.blue
            text_fragment_3.text_state.underline = True
            paragraph.append_line(text_fragment_1)
            paragraph.append_line(text_fragment_2)
            paragraph.append_line(text_fragment_3)
            # Create TextBuilder object
            builder = ap.text.TextBuilder(page)
            # Append the text fragment to the PDF page
            builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```

## 関連テキストトピック

- [Python を使用して PDF 内のテキストを操作する](/pdf/ja/python-net/working-with-text/)
- [PDF へのテキストの追加](/pdf/ja/python-net/add-text-to-pdf-file/)
- [Python で PDF テキストをフォーマットする](/pdf/ja/python-net/text-formatting-inside-pdf/)
- [PDF 内のテキストを Python に置き換える](/pdf/ja/python-net/replace-text-in-pdf/)