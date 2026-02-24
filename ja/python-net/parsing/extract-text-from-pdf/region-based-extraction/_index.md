---
title: Python を使用した領域ベース抽出
linktitle: 領域ベース抽出
type: docs
weight: 20
url: /ja/python-net/region-based-extraction/
description: このセクションには、Python で Aspose.PDF を使用した PDF ドキュメントの領域ベース抽出に関する記事が含まれています。
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## 特定のページ領域からテキストを抽出

Aspose.PDF for Python を使用して、PDF の特定のページ上の定義された矩形領域からテキストを抽出します。座標を指定することで、テーブルセル、段落ブロック、またはフォームフィールド領域など、特定のエリアに抽出を集中させることができます。

ヘッダー、フッター、請求書、またはテキストが予測可能な位置に表示される固定レイアウトレポートなど、ゾーンベースのテキスト抽出に最適です。

1. PDF 文書を開く。
1. 'TextAbsorber' を作成する。
1. 'text_search_options' を設定して矩形領域に限定する。
1. 特定のページでアブソーバーを受け入れる。
1. 抽出されたテキストを書き込む。

```python

import os
import aspose.pdf as ap

def extract_text_from_region(infile, page_number, rect_coords, outfile):
    """
    Extract text from a specified rectangular region on a given page.
    Args:
        infile (str): Path to input PDF file.
        page_number (int): 1-based index of the page.
        rect_coords (tuple): (llx, lly, urx, ury) coordinates of the rectangle.
        outfile (str): Output text file path.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextAbsorber()
        # Set options to restrict search to the rectangle
        absorber.text_search_options.limit_to_page_bounds = True
        llx, lly, urx, ury = rect_coords
        absorber.text_search_options.rectangle = ap.Rectangle(llx, lly, urx, ury, True)
        # Accept on the specific page
        document.pages[page_number].accept(absorber)
        extracted_text = absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

## 段落を順に反復して抽出

PDF ドキュメントからテキストを取得する方法として、単一ページまたはドキュメント全体から特定のテキスト（「プレーンテキスト」や「正規表現」使用）を検索したり、単一ページ、ページ範囲、またはドキュメント全体の全文を取得したりできます。ただし、場合によっては PDF ドキュメントから段落単位でテキストを抽出したり、段落としてのテキストが必要になることがあります。我々は PDF ドキュメントページのテキスト内でセクションや段落を検索する機能を実装しました。TextFragmentAbsorber や TextAbsorber と同様の ParagraphAbsorber クラスを導入し、PDF ドキュメントから段落を抽出できるようにしました。

Aspose.PDF ライブラリを使用すると、PDF ファイルを読み取り、'ParagraphAbsorber' を使って各ページからすべての段落テキストを抽出できます。出力はページ、セクション、段落ごとに整理され、抽出されたコンテンツはプレーンテキストファイルに書き込まれます。これはテキスト分析、アーカイブ、または構造化された PDF コンテンツを読みやすい形式に変換する際に便利です。

1. PDF 文書を開く。
1. 'ParagraphAbsorber' のインスタンスを作成する。
1. 'absorber.visit(document)' を呼び出して、すべてのページの段落をスキャンする。
1. アブソーバーの 'page_markups' コレクションをループする。
1. 各 page‑markup に対して、その 'sections' をループし、次にセクション内の各 'paragraph' をループする。
1. 各段落内で 'lines' をループし、行内の各 'fragment' をループして、'fragment.text' を蓄積する。
1. 各段落（ページ/セクション/段落インデックス付き）を出力ファイルに書き込む。
1. 終了時にドキュメントを閉じる。

```python

import os
import aspose.pdf as ap

def extract_paragraphs_from_pdf(infile, outfile):
    """
    Extract all paragraphs from a PDF document, and write each paragraph’s text into an output file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.ParagraphAbsorber()
        absorber.visit(document)

        with open(outfile, "w", encoding="utf‑8") as tw:
            for page_markup in absorber.page_markups:
                for sec_idx, section in enumerate(page_markup.sections, start=1):
                    for para_idx, paragraph in enumerate(section.paragraphs, start=1):
                        # Concatenate all fragments/lines in the paragraph
                        parts = []
                        for line in paragraph.lines:
                            for fragment in line:
                                parts.append(fragment.text)
                            parts.append("\r\n")
                        paragraph_text = "".join(parts)
                        tw.write(f"Page {page_markup.number}, Section {sec_idx}, Paragraph {para_idx}:\n")
                        tw.write(paragraph_text + "\n")
    finally:
        document.close()
```

## バウンディングポリゴンレンダリングによる段落抽出

このコードスニペットは、PDF の特定ページから段落レベルのテキストとレイアウト情報を抽出します。各段落のバウンディング矩形とポリゴン座標、および実際のテキスト内容を取得し、結果をテキストファイルに書き込みます。これは、ドキュメント構造やレイアウトマッピングの分析、アクセシビリティやコンテンツ抽出タスク向けのデータ準備に役立ちます。

1. PDF を開き、ドキュメントをロードする。
1. 'ParagraphAbsorber' のインスタンスを作成する。
1. 抽出したい特定のページに対して 'absorber.visit(page)' を呼び出す。
1. 'absorber.page_markups' から最初の 'page_markup' を取得する。
1. そのマークアップ内の各セクションに対して：
- その 'rectangle' を取得する。
1. セクション内の各段落に対して：
- その 'points'（ポリゴン）を取得する。
- 'paragraph.lines' をループし、'fragment.text' を抽出する。
1. ジオメトリとテキスト情報を出力ファイルに書き込む。
1. ドキュメントを閉じる。

```python

import os
import aspose.pdf as ap

def extract_paragraphs_with_geometry(infile, outfile):
    """
    Extract paragraphs and record geometry info (rectangle / polygon) for each paragraph in a PDF.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.ParagraphAbsorber()
        absorber.visit(document.pages[1])  # Visit page 2 (pages are 1-indexed)

        page_markup = absorber.page_markups[0]
        with open(outfile, "w", encoding="utf‑8") as tw:
            for sec_idx, section in enumerate(page_markup.sections, start=1):
                tw.write(f"Section {sec_idx}: rectangle = {section.rectangle}\n")
                for para_idx, paragraph in enumerate(section.paragraphs, start=1):
                    tw.write(f"  Paragraph {para_idx}: polygon = {paragraph.points}\n")
                    # Concatenate paragraph text
                    parts = []
                    for line in paragraph.lines:
                        for fragment in line:
                            parts.append(fragment.text)
                        parts.append("\r\n")
                    tw.write("    Text: " + "".join(parts) + "\n\n")
    finally:
        document.close()
```

