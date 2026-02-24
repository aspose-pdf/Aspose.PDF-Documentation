---
title: Python で PDF を EPUB、LaTeX、テキスト、XPS に変換
linktitle: PDF を他の形式に変換
type: docs
weight: 90
url: /ja/python-net/convert-pdf-to-other-files/
lastmod: "2025-09-27"
description: このトピックでは、Python を使用して PDF ファイルを EPUB、LaTeX、テキスト、XPS などの他のファイル形式に変換する方法を示します。
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Python で PDF を他の形式に変換する方法
Abstract: この記事では、Aspose.PDF for Python を使用して PDF ファイルをさまざまな形式に変換する包括的なガイドを提供します。PDF を EPUB、LaTeX/TeX、テキスト、XPS、XML 形式に変換する方法をカバーしています。各セクションは、Aspose が提供するオンラインの無料アプリケーションで PDF を各形式に変換してみることを案内し、使いやすさとツールの品質を強調しています。
---

## PDF を EPUB に変換

{{% alert color="success" %}}
**PDF をオンラインで EPUB に変換してみる**

Aspose.PDF for Python は、オンラインの無料アプリケーション ["PDF を EPUB に変換"](https://products.aspose.app/pdf/conversion/pdf-to-epub) を提供しており、機能と品質を試すことができます。

[![Aspose.PDF 無料アプリで PDF から EPUB への変換](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> は、International Digital Publishing Forum (IDPF) が策定した無料かつオープンな電子書籍標準です。ファイルの拡張子は .epub です。
EPUB は再フロー可能なコンテンツ向けに設計されており、EPUB リーダーは特定の表示デバイスに合わせてテキストを最適化できます。また、固定レイアウトのコンテンツもサポートしています。このフォーマットは、出版社や変換ハウスが社内で使用できる単一フォーマットとして、配布や販売にも利用されます。Open eBook 標準に取って代わるものです。

Aspose.PDF for Python は、PDF ドキュメントを EPUB 形式に変換する機能もサポートしています。Aspose.PDF for Python には 'EpubSaveOptions' というクラスがあり、[document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドの第2引数として使用して、EPUB ファイルを生成できます。
以下のコードスニペットを使用して、Python でこの要件を実現してみてください。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.EpubSaveOptions()
    save_options.content_recognition_mode = (
        ap.EpubSaveOptions.RecognitionMode.FLOW
    )
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## PDF を LaTeX/TeX に変換

**Aspose.PDF for Python via .NET** は、PDF を LaTeX/TeX に変換することをサポートしています。
LaTeX ファイル形式は、特別なマークアップを持つテキストファイル形式で、TeX ベースの文書作成システムで高品質な組版に使用されます。

{{% alert color="success" %}}
**PDF をオンラインで LaTeX/TeX に変換してみる**

Aspose.PDF for Python は、オンラインの無料アプリケーション ["PDF を LaTeX に変換"](https://products.aspose.app/pdf/conversion/pdf-to-tex) を提供しており、機能と品質を試すことができます。

[![Aspose.PDF 無料アプリで PDF から LaTeX/TeX への変換](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

PDF ファイルを TeX に変換するには、Aspose.PDF のクラス [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) を使用します。このクラスは変換プロセス中に一時画像を保存するための OutDirectoryPath プロパティを提供します。

以下のコードスニペットは、Python で PDF ファイルを TEX 形式に変換する手順を示しています。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.LaTeXSaveOptions()

    document.save(path_outfile, save_options)
    print(infile + " converted into " + outfile)
```

## PDF をテキストに変換

**Aspose.PDF for Python** は、PDF 全体や単一ページをテキストファイルに変換することをサポートしています。'TextDevice' クラスを使用して PDF ドキュメントを TXT ファイルに変換できます。以下のコードスニペットは、すべてのページからテキストを抽出する方法を説明しています。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    device = ap.devices.TextDevice()
    device.process(document.pages[1], path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**PDF をオンラインでテキストに変換してみる**

Aspose.PDF for Python は、オンラインの無料アプリケーション ["PDF をテキストに変換"](https://products.aspose.app/pdf/conversion/pdf-to-txt) を提供しており、機能と品質を試すことができます。

[![Aspose.PDF 無料アプリで PDF をテキストに変換](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## PDF を XPS に変換

**Aspose.PDF for Python** は、PDF ファイルを XPS 形式に変換する機能を提供します。以下のコードスニペットを使用して、Python で PDF ファイルを XPS 形式に変換してみてください。

{{% alert color="success" %}}
**PDF をオンラインで XPS に変換してみる**

Aspose.PDF for Python は、オンラインの無料アプリケーション ["PDF を XPS に変換"](https://products.aspose.app/pdf/conversion/pdf-to-xps) を提供しており、機能と品質を試すことができます。

[![Aspose.PDF 無料アプリで PDF を XPS に変換](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

XPS ファイル形式は主に Microsoft Corporation の XML Paper Specification（XPS）に関連付けられています。XML Paper Specification（XPS）は、かつて Metro というコードネームで、Next Generation Print Path（NGPP）というマーケティングコンセプトを包含しており、Microsoft が Windows オペレーティングシステムに文書作成と閲覧を統合する取り組みです。

PDF ファイルを XPS に変換するには、Aspose.PDF のクラス [XpsSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/) を使用します。このクラスは [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドの第2引数として使用され、XPS ファイルを生成します。

以下のコードスニペットは、PDF ファイルを XPS 形式に変換する手順を示しています。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.XpsSaveOptions()
    save_options.use_new_imaging_engine = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## PDFをMDに変換

Aspose.PDF には 'MarkdownSaveOptions()' クラスがあり、PDF ドキュメントを画像やリソースを保持したまま Markdown (MD) 形式に変換します。

1. 'ap.Document' を使用してソース PDF を読み込みます。
1. 'MarkdownSaveOptions' のインスタンスを作成します。
1. 'resources_directory_name' を 'images' に設定します。抽出された画像はこのフォルダーに保存されます。
1. 設定したオプションを使用して変換された Markdown ドキュメントを保存します。
1. 変換後に確認メッセージを出力します。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.MarkdownSaveOptions()
    # save_options.extract_vector_graphics = True
    save_options.resources_directory_name = "images"
    save_options.use_image_html_tag = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

指定された images フォルダーに保存されたテキストとリンクされた画像を含む Markdown ファイルです。

## PDFをMobiXMLに変換

このメソッドは PDF ドキュメントを MOBI (MobiXML) 形式に変換します。MOBI は Kindle デバイスで一般的に使用される電子書籍フォーマットです。

1. 'ap.Document' を使用してソース PDF ドキュメントを読み込みます。
1. ドキュメントを形式 'ap.SaveFormat.MOBI_XML' で保存します。
1. 変換が完了したら確認メッセージを出力します。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.save(path_outfile, ap.SaveFormat.MOBI_XML)

    print(infile + " converted into " + outfile)
```
