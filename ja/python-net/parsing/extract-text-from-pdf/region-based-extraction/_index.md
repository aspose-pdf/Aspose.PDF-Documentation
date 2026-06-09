---
title: Python を使用したリージョンベースの抽出
linktitle: 地域ベースの抽出
type: docs
weight: 20
url: /ja/python-net/region-based-extraction/
description: Aspose.PDF for Python を使用して PDF 文書内の特定のページ領域または段落構造からテキストを抽出する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## ページの特定の領域からテキストを抽出する

使用 [テキストアブソーバー](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) と一緒に [四角形](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) 抽出をページの特定の領域に制限します。この方法は、ヘッダー、フッター、テーブルセル、フォームフィールド、請求書、またはテキストの位置が事前にわかっているその他の固定レイアウト領域からゾーンベースで抽出する場合に便利です。

1. ソース PDF をとして開きます [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. を作成 `TextAbsorber` インスタンス。
1. 環境設定 `text_search_options` 抽出を長方形に制限します。
1. ターゲットページのアブソーバーを受け入れます。
1. 抽出したテキストを出力ファイルに書き込みます。

```python
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

## 段落を繰り返し処理して抽出する

使用 [パラグラフアブソーバー](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/paragraphabsorber/) プレーンページテキストの代わりに段落対応抽出が必要な場合。とは違います [テキストアブソーバー](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) または [テキストフラグメントアブソーバー](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/)、この API は、出力をページ、セクション、および段落ごとに整理します。これは、テキスト分析、構造化されたエクスポート、およびレイアウトに依存する処理に役立ちます。

1. ソース PDF をとして開きます [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. を作成 `ParagraphAbsorber` インスタンス。
1. コール `absorber.visit(document)` すべてのページを分析します。
1. イテレートスルー `page_markups`次に、各セクションと段落を確認します。
1. 各段落のテキストフラグメントを読み取り、結果をファイルに書き込みます。

```python
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

        with open(outfile, "w", encoding="utf-8") as tw:
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
                        tw.write(
                            f"Page {page_markup.number}, Section {sec_idx}, Paragraph {para_idx}:\n"
                        )
                        tw.write(paragraph_text + "\n")
    finally:
        document.close()
```

## バウンディングポリゴンレンダリングによる段落の抽出

使用することもできます [パラグラフアブソーバー](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/paragraphabsorber/) 段落のジオメトリを検査します。この方法では、テキストを抽出するだけでなく、各セクションの四角形と段落の多角形も記録されるため、レイアウトマッピング、文書分析、アクセシビリティツール、または領域を意識した後処理に役立ちます。

1. ソース PDF をとして開きます [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. を作成 `ParagraphAbsorber` インスタンス。
1. ターゲットページにアクセスしてください。
1. ページマークアップを以下から読み込む `absorber.page_markups`.
1. セクションや段落を繰り返し読み込んで、ジオメトリとテキストをキャプチャします。
1. 長方形、多角形、およびテキストデータを出力ファイルに書き込みます。

```python
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
        with open(outfile, "w", encoding="utf-8") as tw:
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
