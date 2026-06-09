---
title: Python を使った注釈と特殊テキスト
linktitle: 注釈と特殊テキスト
type: docs
weight: 40
url: /ja/python-net/annotation-and-special-text/
description: Aspose.PDF for Python を使用して、PDF ドキュメント内のスタンプ注釈、強調表示されたテキスト、上付き文字/下付き文字コンテンツからテキストを抽出する方法を学びます。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## スタンプ注釈からテキストを抽出

使用 [テキストアブソーバー](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) に埋め込まれたテキストを抽出するには [スタンプ注釈](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/stampannotation) アピアランスストリーム。これは、スタンプの内容がプレーンテキストとして保存されるのではなく、フォーム XObject としてレンダリングされる場合に便利です。

1. を開きます [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. ターゲットアノテーションには以下からアクセスしてください `page.annotations`.
1. それが次のものであることを確認してください `StampAnnotation`その後、通常の外観の XForm に戻します。
1. Xフォームをに渡す `TextAbsorber.visit()` 埋め込まれたテキストを抽出します。

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

## 強調表示されたテキストを抽出

ページの注釈を繰り返し処理して使用する [ハイライト・アノテーション。get_marked_text ()](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation) 各ハイライトでカバーされているテキストスパンを読むことができます。ページ・アノテーション・コレクションは 1 から始まります。

1. を開きます [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) 目的のページを選択します。
1. ループスルー `page.annotations`.
1. 使用 `is_assignable` フィルタリング対象 [注記をハイライト](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation) インスタンス。
1. 注釈をキャストして電話をかける `get_marked_text()` 強調表示されたコンテンツを取得します。

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

## 上付き文字と下付き文字を抽出

上付き文字と下付き文字は、式、数式、および化合物名によく登場します。.NET 経由の Python 用の Aspose.PDF は、次の方法でこのコンテンツを抽出することをサポートしています。 [テキストフラグメントアブソーバー](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber)は、文字レベルのポジショニングメタデータを検出します。

1. を開きます [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. を作成 `TextFragmentAbsorber` インスタンス。
1. コール `document.pages[page_number].accept(absorber)` ターゲットページをスキャンします。
1. から抽出したテキスト全体を取得する `absorber.text`.
1. 結果をファイルに書き込み、文書を閉じます。

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
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(extracted_text)
    finally:
        document.close()
```

## テキストフラグメントを繰り返し処理して上付き文字/下付き文字を検出

フラグメント単位の検査では、繰り返し処理してください `absorber.text_fragments` そして読んでください `text_state.superscript` そして `text_state.subscript` それぞれにブーリアンフラグ [テキストフラグメント](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment).

1. を開きます [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) そして作成する [テキストフラグメントアブソーバー](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber).
1. ターゲットページのアブソーバーを受け入れて入力してください `absorber.text_fragments`.
1. 各フラグメントについて、以下をお読みください。 `fragment.text`, `fragment.text_state.superscript`、および `fragment.text_state.subscript`.
1. 結果を出力ファイルに書き込み、文書を閉じます。

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

        with open(outfile, "w", encoding="utf-8") as f:
            for fragment in absorber.text_fragments:
                text = fragment.text
                is_sup = fragment.text_state.superscript  # True if superscript
                is_sub = fragment.text_state.subscript  # True if subscript
                f.write(
                    f"Text: '{text}' | Superscript: {is_sup} | Subscript: {is_sub}\n"
                )
    finally:
        document.close()
```
