---
title: PythonでHTMLをPDFに変換
linktitle: HTMLをPDFファイルに変換
type: docs
weight: 40
url: /ja/python-net/convert-html-to-pdf/
lastmod: "2025-09-27"
description: Aspose.PDF for Python via .NET を使用して、HTML コンテンツを PDF ドキュメントに変換する方法を学びます
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Aspose.PDF for Python を使用して HTML を PDF に変換する方法
Abstract: Aspose.PDF for Python via .NET は、アプリケーション内でウェブページや生の HTML コードから PDF ファイルを作成するための強力なソリューションを提供します。本記事では、Python を使用して HTML を PDF に変換する手順を紹介し、HTML 文書を PDF 形式にシームレスに変換できる PDF 操作 API である Aspose.PDF for Python の使用方法を概説します。変換プロセスは必要に応じてカスタマイズ可能です。この記事には、HtmlLoadOptions クラスのインスタンス作成、Document オブジェクトの初期化、Document.Save() メソッドによる出力 PDF の保存を含む、変換プロセスを示す Python コードサンプルが含まれています。また、Aspose はオンラインツールも提供しており、HTML を PDF に変換できるので、機能と品質を確認できます。
---

## PythonでHTMLをPDFに変換

**Aspose.PDF for Python** は、任意の既存 HTML ドキュメントをシームレスに PDF に変換できる PDF 操作 API です。HTML を PDF に変換するプロセスは柔軟にカスタマイズ可能です。

## HTMLをPDFに変換

以下の Python コードサンプルは、HTML ドキュメントを PDF に変換する方法を示しています。

1. [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) クラスのインスタンスを作成します。
1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) オブジェクトを初期化します。
1. **document.save()** メソッドを呼び出して、出力 PDF ドキュメントを保存します。

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.page_layout_option = ap.HtmlPageLayoutOption.SCALE_TO_PAGE_WIDTH
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**HTMLをオンラインでPDFに変換してみる**

Aspose は、オンライン無料アプリケーション ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf) を提供しており、機能と品質を試すことができます。

[![Aspose.PDF 無料アプリを使用した HTML から PDF への変換](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## メディアタイプを使用してHTMLをPDFに変換

この例では、特定のレンダリングオプションを使用して、Aspose.PDF for Python via .NET で HTML ファイルを PDF に変換する方法を示します。

1. [HtmlLoadOptions()](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) クラスのインスタンスを作成します。'html_media_type' は画面表示用の CSS ルールを適用します。'html_media_type' プロパティは複数の値を持つことができ、HtmlMediaType.SCREEN または HtmlMediaType.PRINT に設定できます。
1. ロードオプションを使用して、HTML を ap.Document にロードします。
1. ドキュメントを PDF として保存します。

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.html_media_type = ap.HtmlMediaType.SCREEN
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## 優先CSSページルールでHTMLをPDFに変換

一部のドキュメントには、[the Page rule](https://developer.mozilla.org/en-US/docs/Web/CSS/@page) を利用したレイアウト設定が含まれており、レイアウト生成時に曖昧さが生じることがあります。'is_priority_css_page_rule' プロパティを使用して優先度を制御できます。このプロパティが 'True' に設定されている場合、CSS ルールが最初に適用されます。

1. [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) クラスのインスタンスを作成します。
1. '@page' CSS ルールの優先順位を無効にし、他のスタイルが優先されるようにするには、'is_priority_css_page_rule = False' を設定します。
1. 設定したオプションで HTML を ap.Document にロードします。
1. ドキュメントを PDF として保存します。

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    # load_options.is_priority_css_page_rule = False
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## 埋め込みフォント付きでHTMLをPDFに変換

この例では、フォントを埋め込みながら HTML ファイルを PDF に変換する方法を示します。埋め込みフォント付きの PDF が必要な場合は、'is_embed_fonts' を True に設定してください。

1. HTML から PDF への変換を構成するために 'HtmlLoadOptions()' を作成します。
1. 'is_embed_fonts = True' を設定して、HTML で使用されるすべてのフォントが PDF に直接埋め込まれ、視覚的な忠実度が保たれるようにします。
1. これらのオプションで HTML を ap.Document にロードします。
1. ドキュメントを PDF として保存します。

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.HtmlLoadOptions()
    load_options.is_embed_fonts = True
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## HTMLをPDFに変換する際に単一ページにコンテンツをレンダリング

この例では、Aspose.PDF for Python を使用して HTML ファイルを単一ページの PDF に変換する方法を示します。
'is_render_to_single_page' プロパティを使用すると、すべてのコンテンツを1ページに表示できます。

1. 変換プロセスを構成するために 'HtmlLoadOptions()' のインスタンスを作成します。
1. 'is_render_to_single_page' を有効にして、HTML の全コンテンツを単一の連続した PDF ページにレンダリングします。
1. 設定したオプションでドキュメントを 'ap.Document' にロードします。
1. 結果を PDF ファイルとして保存します。

```python
    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    options = ap.HtmlLoadOptions()
    options.is_render_to_single_page = True

    doc = ap.Document(path_infile, options)
    doc.save(path_outfile)
```

## MHTMLをPDFに変換

この例では、Aspose.PDF for Python を使用して、特定のページサイズで MHT（MHTML）ファイルを PDF ドキュメントに変換する方法を示します。

1. MHT ファイルの処理を構成するために ap.MhtLoadOptions() のインスタンスを作成します。
1. ページサイズなど、さまざまなパラメータを設定します。
1. 入力ファイルと構成したロードオプションを使用してドキュメントを初期化します。
1. 結果のドキュメントを PDF として保存します。

```python

    from os import path
    import aspose.pdf as ap
    import requests
    import io

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    load_options = ap.MhtLoadOptions()
    load_options.page_info.width = 842
    load_options.page_info.height= 1191
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```
