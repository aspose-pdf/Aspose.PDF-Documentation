---
title: Python を使ったハローワールドの例
linktitle: ハローワールドの例
type: docs
weight: 20
url: /ja/python-net/hello-world-example/
description: このサンプルでは、.NET 経由で Aspose.PDF for Python を使用して、Hello World というテキストを含む簡単な PDF ドキュメントを作成する方法を示します。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python によるハローワールドの例
Abstract: この記事では、.NET ライブラリ経由の Aspose.PDF for Python を使用して PDF ドキュメントを作成するハローワールドの例を紹介します。この例は、Aspose.PDF API を使用して「Hello World!」というテキストを含む PDF を生成する基本的な手順を示しています。このプロセスには、「Document」オブジェクトをインスタンス化し、「Page」を追加し、「TextFragment」オブジェクトを作成し、フォントサイズや色などのテキストプロパティを設定し、「TextBuilder」を使用してテキストをページに追加します。その後、生成された PDF は「HelloWorld_out.pdf」として保存されます。この記事には、ライブラリの使用法の入門ガイドとして役立つ、これらの手順を説明する完全な Python コードスニペットが含まれています。
---

「Hello World」の例は、どのプログラミング言語でも最も単純な構文と最も単純なプログラムを示しています。開発者は、デバイス画面に「Hello World」を印刷する方法を学ぶことで、基本的なプログラミング言語構文を理解できます。したがって、私たちは伝統的にライブラリをそこから使い始めることになります。

この記事では、「Hello World!」というテキストを含む PDF ドキュメントを作成しています。**.NET 経由で Python 用 Aspose.pdf をインストールしたら、以下のコードサンプルを実行して Aspose.PDF API がどのように機能するかを確認することができます。

以下のコードスニペットは以下の手順に従います。

1. をインスタンス化する [文書](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 対象
1. を追加 [ページ](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 文書オブジェクトへ
1. を作成 [テキストフラグメント](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) 対象
1. テキストの色を設定
1. テキストビルダーの作成
1. 追加 [テキストフラグメント](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) ページへ
1. [ドキュメント.save ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 結果の PDF ドキュメント

次のコードスニペットは、.NET API 経由で Aspose.PDF for Python の機能を示す「ハローワールド」プログラムです。

```python
from datetime import timedelta
import aspose.pdf as ap


def run_simple(self):
    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Add text to new page
    textFragment = ap.text.TextFragment("Hello, world!")
    textFragment.position = ap.text.Position(100, 600)

    textFragment.text_state.font_size = 12
    textFragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    textFragment.text_state.background_color = ap.Color.blue
    textFragment.text_state.foreground_color = ap.Color.yellow

    # Create TextBuilder object
    textBuilder = ap.text.TextBuilder(page)

    # Append the text fragment to the PDF page
    textBuilder.append_text(textFragment)

    document.save(self.data_dir + "HelloWorld_out.pdf")
```
