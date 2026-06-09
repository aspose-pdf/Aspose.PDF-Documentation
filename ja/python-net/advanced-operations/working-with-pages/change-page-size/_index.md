---
title: Python で PDF ページサイズを変更する方法
linktitle: ページサイズの変更
type: docs
weight: 40
url: /ja/python-net/change-page-size/
description: Python で PDF ページのサイズを読み込んで変更する方法を学びましょう。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用してページサイズを変更する
Abstract: この記事では、Aspose.PDF を使用して PDF ページのサイズを読み取り、変更する方法を説明します。Get Page Size のサンプルでは、特定の PDF ページの幅と高さを取得して、ユーザーがページレイアウトを調べたり、フォーマットを検証したり、文書構造を分析したりできるようにします。「ページサイズを設定」の例は、最初のページを A4 サイズに変換するなど、ページのサイズを変更する方法を示していますが、変更前と変更後にボックスのプロパティ (クロップボックス、トリムボックス、アートボックス、ブリードボックス、メディアボックス) も表示する方法を示しています。
---

.NET 経由の Python 用 Aspose.PDF では、簡単なコード行で PDF ページサイズを変更できます。このトピックでは、を使用してページサイズを更新する方法を説明します。 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) そして [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) API。

Python で既存の PDF ページのサイズを変更したり、文書のサイズを正規化したり、ページボックスの設定を確認したりする必要がある場合は、このガイドを使用してください。

{{% alert color="primary" %}}

高さと幅のプロパティでは、基本単位としてポイントが使用されることに注意してください。1 インチ = 72 ポイント、1 cm = 1/2.54 インチ = 0.3937 インチ = 28.3 ポイントです。

{{% /alert %}}

## PDF ページのページサイズを A4 に設定

この例では、PDF 文書の最初のページのサイズを標準の A4 サイズに更新します。また、サイズ変更の前後にページのボックスサイズ (クロップボックス、トリムボックス、アートボックス、ブリードボックス、メディアボックス) も印刷されるので、変更を確認することができます。

次のコードスニペットは、PDF ページのサイズを A4 サイズに変更する方法を示しています。

1. 最初にアクセスする [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) の [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 変更前のページのボックスサイズ (クロップボックス、トリムボックス、アートボックス、ブリードボックス、メディアボックス) を表示します。
1. ページ API を使用して A4 ディメンション (597.6 × 842.4 ポイント) を適用します。
1. 更新されたページボックスのサイズを表示します。
1. 変更を保存する [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 指定された出力パスへ。

```python
import aspose.pdf as ap

def set_page_size(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]

    # Set the page size as A4 (8.3 x 11.7 in) and in Aspose.Pdf, 1 inch = 72 points
    # So A4 dimensions in points will be (597.6, 842.4) for portrait orientation
    print("Before set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    page.set_page_size(597.6, 842.4)
    print("After set")
    print(f"CropBox: {page.crop_box.width} x {page.crop_box.height}")
    print(f"TrimBox: {page.trim_box.width} x {page.trim_box.height}")
    print(f"ArtBox: {page.art_box.width} x {page.art_box.height}")
    print(f"BleedBox: {page.bleed_box.width} x {page.bleed_box.height}")
    print(f"MediaBox: {page.media_box.width} x {page.media_box.height}")

    # Save the updated document
    document.save(output_file_name)
```

## PDF ページサイズを取得

このスニペットは PDF を読み取り、最初のページのサイズ (幅と高さ) を取得します。次のものを使用します。 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) ページの境界を抽出する API [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) そのサイズをコンソールに出力します。これは、ページレイアウトの検査、フォーマットの検証、または今後の処理に向けた文書の準備に役立ちます。

1. PDF をとして読み込む [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 最初にアクセスする [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. を使用してページの境界矩形を取得します `get_page_rect()`.
1. 幅と高さの値を抽出します。
1. ページのサイズを印刷します。

```python
import aspose.pdf as ap

def get_page_size(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    # Get particular page
    page = document.pages[1]
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

### 回転前と回転後の PDF ページサイズの取得

90°回転を適用する前と適用した後のPDFページのサイズを取得します。これは、回転が幅と高さにどのように影響するか、またその使用方法を示しています。 `get_page_rect()` ローテーションの考慮の有無にかかわらず。

1. PDF をとして開く [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 最初にアクセスする [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. を使用して90°回転を適用します `page.rotate = ap.Rotation.ON90` (を参照してください [`Rotation`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rotation/) 列挙)。
1. を使用して回転せずにページの長方形を取得する `get_page_rect(False)` そしてその幅と高さを印刷します。
1. 回転を考慮してページの長方形を取得する `get_page_rect(True)` そしてその幅と高さを印刷します。
1. 回転によって寸法がどのように変化するかを比較してください。

```python
import aspose.pdf as ap

def get_page_size_rotation(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]
    page.rotate = ap.Rotation.ON90
    rectangle = page.get_page_rect(False)
    print(f"{rectangle.width} : {rectangle.height}")
    rectangle = page.get_page_rect(True)
    print(f"{rectangle.width} : {rectangle.height}")
```

## 関連ページトピック

- [Python で PDF ページを操作する](/pdf/ja/python-net/working-with-pages/)
- [Python で PDF ページをトリミングする方法](/pdf/ja/python-net/crop-pages/)
- [Python で PDF ページのプロパティを取得および設定する方法](/pdf/ja/python-net/get-and-set-page-properties/)
- [Python で PDF ページを回転させる](/pdf/ja/python-net/rotate-pages/)