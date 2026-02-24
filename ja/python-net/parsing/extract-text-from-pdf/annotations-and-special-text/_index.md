---
title: Python を使用したアノテーションと特殊テキスト
linktitle: アノテーションと特殊テキスト
type: docs
weight: 40
url: /ja/python-net/annotation-and-special-text/
description: このセクションには、Python で Aspose.PDF を使用して PDF ドキュメントからアノテーションと特殊テキストを抽出する記事が含まれています。
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## スタンプアノテーションからテキストを抽出する

Aspose.PDF for Python ライブラリを使用すると、PDF ページ上のスタンプアノテーション（具体的には StampAnnotation）からテキストを抽出できます。

1. ドキュメントを開く。
1. ページのアノテーションコレクションからスタンプアノテーションにアクセスする。
1. スタンプの外観ストリーム（XForm）を取得する。
1. 'TextAbsorber' を使用して、その外観から埋め込まれたテキストを抽出する。

```python

import os
import aspose.pdf as ap

def extract_text_from_stamp(infile, page_number, annotation_index, outfile):
    """
    Extracts text from a stamp annotation on a given page in a PDF document.
    Args:
        infile (str): Path to the input PDF file.
        page_number (int): 1-based index of the page containing the stamp.
        annotation_index (int): 1-based index of the annotation in that page.
        outfile (str): Path to the output text file where extracted text will be saved.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[page_number]
        annot = page.annotations[annotation_index]
        # Ensure it's a StampAnnotation
        if isinstance(annot, ap.annotations.StampAnnotation):
            # Get normal appearance XForm of the stamp
            xform = annot.appearance["N"]
            absorber = ap.text.TextAbsorber()
            absorber.visit(xform)
            extracted = absorber.text
            with open(outfile, "w", encoding="utf-8") as f:
                f.write(extracted)
    finally:
        document.close()
```

## 強調表示テキストを抽出する

PDF 標準では、ドキュメント内のテキストの一部をハイライトする機能が提供されています。そのハイライトされた内容を抽出するには、次の手順に従います：

1. `aspose.pdf as ap` と使用するヘルパー（`is_assignable`、`cast` など）をインポートする。
2. `ap.Document(infile)` を呼び出して PDF を開く。
3. `document.pages` を使用して目的のページを選択する（ページコレクションは 1 から始まります）。
4. `page.annotations` をループして、そのページ上の各アノテーションを調べる。
5. ハイライトアノテーションのみが処理されるようにアノテーションをフィルタリングする。
6. アノテーションを `HighlightAnnotation` にキャストし、`get_marked_text()` を呼び出してハイライトされたテキストを取得する。
7. 取得したテキストを出力するか、他の方法で処理する。

```python
def extract_highlight_text(infile):
    """
    Extract text from highlight annotations.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_highlight_text("sample.pdf")

    Note:
        Prints marked text from each highlight annotation on first page.
    """
    document = ap.Document(infile)
    page = document.pages[1]

    for annotation in page.annotations:
        if is_assignable(annotation, ap.annotations.HighlightAnnotation):
            highlight_annotation = cast(ap.annotations.HighlightAnnotation, annotation)
            print(highlight_annotation.get_marked_text())
```

## 上付き文字と下付き文字のテキストを抽出する

**下付き文字と上付き文字**は、数式、数学的表現、化学化合物の記述などで最も頻繁に使用されます。同じテキストの中に多数存在すると、編集が困難です。
最新リリースの一つで、**Aspose.PDF for Python via .NET** ライブラリは PDF から上付き文字と下付き文字のテキストを抽出する機能を追加しました。'TextFragmentAbsorber' を使用して、PDF ドキュメントの特定ページからすべてのテキスト（上付き文字と下付き文字を含む）を抽出します。

1. PDF ドキュメントをロードする。
1. バージョン機能に応じて上付き文字/下付き文字テキストの検出をサポートする 'TextFragmentAbsorber()' をインスタンス化する。
1. 'document.pages[page_number].accept(absorber)' を呼び出して、指定されたページのみをスキャンする。
1. 'absorber.text' を介して抽出されたテキストを取得する。
1. 標準のファイル I/O を使用して、テキストを出力ファイルに書き込む。
1. リソースを解放するためにドキュメントを閉じる。

```python

import os
import aspose.pdf as ap

def extract_super_sub_text(infile, outfile, page_number=1):
    """
    Extract text (including superscript/subscript) from a specified page of a PDF and write to a text file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1‑based index of the page to extract.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextFragmentAbsorber()
        # Accept only the specific page for extraction
        document.pages[page_number].accept(absorber)
        extracted_text = absorber.text
        with open(outfile, "w", encoding="utf‑8") as f:
            f.write(extracted_text)
    finally:
        document.close()
```

## TextFragment を反復処理して上付き文字/下付き文字を検出する

ページ内の各テキストフラグメントをループし、それが上付き文字か下付き文字かを確認し、適切に処理する。

1. PDF ドキュメントをロードする。
1. 'TextFragmentAbsorber()' を作成し、選択したページで受け入れる。
1. 'absorber.text_fragments' にアクセスし、そのページで見つかったフラグメントのコレクションを取得する。
1. 各フラグメントについて：
- 'fragment.text' を取得する。
- 'fragment.text_state.superscript' と 'fragment.text_state.subscript' を確認する。
- フラグメントテキストとフラグを含む行を書き込む。
1. ファイルとドキュメントを閉じる。

```python

import os
import aspose.pdf as ap

def extract_super_sub_details(infile, outfile, page_number=1):
    """
    Extract details of each text fragment on a page, identifying superscript and subscript items.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1‑based page index.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages[page_number].accept(absorber)

        with open(outfile, "w", encoding="utf‑8") as f:
            for fragment in absorber.text_fragments:
                text = fragment.text
                is_sup = fragment.text_state.superscript  # True if superscript
                is_sub = fragment.text_state.subscript    # True if subscript
                f.write(f"Text: '{text}' | Superscript: {is_sup} | Subscript: {is_sub}\n")
    finally:
        document.close()
```
