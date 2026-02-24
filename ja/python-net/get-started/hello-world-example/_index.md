---
title: Pythonを使用したHello Worldの例
linktitle: Hello Worldの例
type: docs
weight: 20
url: /ja/python-net/hello-world-example/
description: このサンプルは、Aspose.PDF for Python via .NET を使用して、テキスト「Hello World」のシンプルな PDF ドキュメントを作成する方法を示しています。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Python を使用した Hello World の例
Abstract: この記事では、Aspose.PDF for Python via .NET ライブラリを使用して PDF ドキュメントを作成する Hello World の例を提供します。この例は、テキスト "Hello World!" を含む PDF を生成することで Aspose.PDF API の基本的な手順を示しています。手順は、`Document` オブジェクトのインスタンス化、`Page` の追加、`TextFragment` オブジェクトの作成、フォントサイズや色などのテキストプロパティの設定、そして `TextBuilder` を使用してページにテキストを追加することです。生成された PDF は "HelloWorld_out.pdf" として保存されます。この記事には、これらの手順を示す完全な Python コードスニペットが含まれており、ライブラリの使い方への入門ガイドとなっています。
---

A "Hello World" の例は、任意のプログラミング言語における最もシンプルな構文とプログラムを示します。開発者は、デバイス画面に "Hello World" を出力する方法を学ぶことで、基本的なプログラミング言語構文に慣れ親しみます。したがって、私たちは通常、ライブラリとの最初の出会いをこの例から始めます。

この記事では、テキスト "Hello World!" を含む PDF ドキュメントを作成します。環境に **Aspose.PDF for Python via .NET** をインストールした後、以下のコードサンプルを実行して Aspose.PDF API の動作を確認できます。

以下のコードスニペットは、これらの手順に従っています：

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトをインスタンス化する
1. ドキュメントオブジェクトに [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) を追加する
1. [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) オブジェクトを作成する
1. テキストの色を設定する
1. Text Builder を作成する
1. ページに [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) を追加する
1. [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) で結果の PDF ドキュメントを保存する

以下のコードスニペットは、Aspose.PDF for Python via .NET API の機能を示す "Hello World" プログラムです。

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
    textFragment.text_state.font = ap.text.FontRepository.find_font(
        "TimesNewRoman"
    )
    textFragment.text_state.background_color = ap.Color.blue
    textFragment.text_state.foreground_color = ap.Color.yellow

    # Create TextBuilder object
    textBuilder = ap.text.TextBuilder(page)

    # Append the text fragment to the PDF page
    textBuilder.append_text(textFragment)

    document.save(self.data_dir + "HelloWorld_out.pdf")
```
