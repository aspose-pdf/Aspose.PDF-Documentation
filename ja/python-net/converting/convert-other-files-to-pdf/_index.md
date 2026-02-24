---
title: Pythonで他のファイル形式をPDFに変換する
linktitle: 他のファイル形式をPDFに変換する
type: docs
weight: 80
url: /ja/python-net/convert-other-files-to-pdf/
lastmod: "2025-09-01"
description: このトピックでは、Aspose.PDF が EPUB、MD、PCL、XPS、PS、XML、LaTeX などの他のファイル形式を PDF ドキュメントに変換できる方法を示します。
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Pythonで他のファイル形式をPDFに変換する方法
Abstract: この記事は、Python と Aspose.PDF for Python via .NET の機能を活用して、さまざまなファイル形式を PDF に変換する包括的なガイドを提供します。ドキュメントでは、EPUB、Markdown、PCL、テキスト、XPS、PostScript、XML、XSL-FO、LaTeX/TeX など複数の形式の変換プロセスを概説しています。各セクションでは、具体的なコードスニペットと変換実装手順が示されています。この記事は、各ファイルタイプに合わせたロードオプションなど、Aspose.PDF の機能の有用性を強調し、正確かつ効率的な変換を保証します。さらに、ユーザーが機能を直接体験できる無料のオンライン変換アプリケーションの提供も紹介しています。このガイドは、Python アプリケーションに PDF 変換機能を統合したい開発者にとって実用的なリソースとなります。
---

この記事では、**Python を使用してさまざまな他のファイル形式を PDF に変換する方法**について説明します。以下のトピックをカバーしています。

## OFDをPDFに変換する

OFD は Open Fixed-layout Document（オープン固定レイアウトドキュメント、別名 Open Fixed Document フォーマット）の略です。これは、中国の国家標準（GB/T 33190-2016）であり、PDF の代替として導入された電子文書です。

PythonでOFDをPDFに変換する手順:

1. OfdLoadOptions() を使用して OFD のロードオプションを設定します。
1. OFD ドキュメントを読み込みます。
1. PDF として保存します。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.OfdLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## LaTeX/TeX を PDF に変換する

LaTeX ファイル形式は、TeX 系列言語の派生である LaTeX のマークアップを備えたテキストファイル形式で、TeX システムから派生した形式です。LaTeX（ˈleɪtɛk/lay-tek または lah-tek）は、文書作成システムおよび文書マークアップ言語であり、数学、物理学、コンピュータサイエンスなど多数の分野で科学文書のコミュニケーションや出版に広く使用されています。また、韓国語、日本語、中国語、アラビア語など複雑な多言語素材を含む書籍や記事の作成・出版においても重要な役割を果たしています。

LaTeX は出力の書式設定に TeX 組版プログラムを使用し、TeX マクロ言語で記述されています。

{{% alert color="success" %}}
**オンラインで LaTeX/TeX を PDF に変換してみる**

Aspose.PDF for Python via .NET は、オンラインで無料のアプリケーション ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf) を提供しており、機能と品質を実際に試すことができます。

[![Aspose.PDF 無料アプリで LaTeX/TeX を PDF に変換](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

PythonでTEXをPDFに変換する手順:

1. LatexLoadOptions() を使用して LaTeX のロードオプションを設定します。
1. LaTeX ドキュメントを読み込みます。
1. PDF として保存します。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.LatexLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```
## OFDをPDFに変換する

OFD は Open Fixed-layout Document（オープン固定レイアウトドキュメント、別名 Open Fixed Document フォーマット）の略です。これは、中国の国家標準（GB/T 33190-2016）であり、PDF の代替として導入された電子文書です。

PythonでOFDをPDFに変換する手順:

1. OfdLoadOptions() を使用して OFD のロードオプションを設定します。
1. OFD ドキュメントを読み込みます。
1. PDF として保存します。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.OfdLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## LaTeX/TeX を PDF に変換する

LaTeX ファイル形式は、TeX 系列言語の派生である LaTeX のマークアップを備えたテキストファイル形式で、TeX システムから派生した形式です。LaTeX（ˈleɪtɛk/lay-tek または lah-tek）は、文書作成システムおよび文書マークアップ言語であり、数学、物理学、コンピュータサイエンスなど多数の分野で科学文書のコミュニケーションや出版に広く使用されています。また、サンスクリット語やアラビア語など複雑な多言語素材を含む書籍や記事の作成・出版においても重要な役割を果たしています。LaTeX は出力の書式設定に TeX 組版プログラムを使用し、TeX マクロ言語で記述されています。

{{% alert color="success" %}}
**オンラインで LaTeX/TeX を PDF に変換してみる**

Aspose.PDF for Python via .NET は、オンラインで無料のアプリケーション ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf) を提供しており、機能と品質を実際に試すことができます。

[![Aspose.PDF 無料アプリで LaTeX/TeX を PDF に変換](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

PythonでTEXをPDFに変換する手順:

1. LatexLoadOptions() を使用して LaTeX のロードオプションを設定します。
1. LaTeX ドキュメントを読み込みます。
1. PDF として保存します。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.LatexLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## EPUBをPDFに変換する

**Aspose.PDF for Python via .NET** は、簡単に EPUB ファイルを PDF 形式に変換できます。

EPUB（electronic publication の略）は、International Digital Publishing Forum（IDPF）による無料でオープンな電子書籍標準です。ファイルの拡張子は .epub です。EPUB はリフロー可能なコンテンツ向けに設計されており、EPUB リーダーは特定の表示デバイスに最適化してテキストを表示できます。

<abbr title="electronic publication">EPUB</abbr> は固定レイアウトコンテンツもサポートします。このフォーマットは、出版社や変換ハウスが社内で使用できる単一のフォーマットとして、また配布や販売にも利用できるよう意図されています。Open eBook 標準に取って代わります。EPUB 3 バージョンは、標準化されたベストプラクティス、調査、情報、イベント、コンテンツのパッケージングを提供する主要な書籍業界協会である Book Industry Study Group（BISG）にも支持されています。

{{% alert color="success" %}}
**オンラインで EPUB を PDF に変換してみる**

Aspose.PDF for Python via .NET は、オンラインの無料アプリケーション ["EPUB を PDF に変換"](https://products.aspose.app/pdf/conversion/epub-to-pdf) を提供します。ここで、機能と品質をご確認いただけます。

[![Aspose.PDF 変換 EPUB から PDF への無料アプリ](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

Python で EPUB を PDF に変換する手順：

1. EpubLoadOptions() を使用して EPUB ドキュメントを読み込みます。
1. EPUB を PDF に変換します。
1. 確認を出力します。

次のコードスニペットは、Python で EPUB ファイルを PDF 形式に変換する方法を示します。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.EpubLoadOptions()
    document = ap.Document(path_infile, load_options)

    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Markdown を PDF に変換

**この機能はバージョン 19.6 以降でサポートされています。**

{{% alert color="success" %}}
**オンラインで Markdown を PDF に変換してみる**

Aspose.PDF for Python via .NET は、オンラインの無料アプリケーション ["Markdown を PDF に変換"](https://products.aspose.app/pdf/conversion/md-to-pdf) を提供します。ここで、機能と品質をご確認いただけます。

[![Aspose.PDF 変換 Markdown から PDF への無料アプリ](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Aspose.PDF for Python via .NET によるこのコードスニペットは、Markdown ファイルを PDF に変換し、文書の共有、書式の保持、印刷互換性を向上させます。

以下のコードスニペットは、Aspose.PDF ライブラリでこの機能を使用する方法を示しています。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.MdLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## PCL を PDF に変換

<abbr title="Printer Command Language">PCL</abbr>（Printer Command Language）は、Hewlett-Packard が開発したプリンタ言語で、標準的なプリンタ機能にアクセスするために使用されます。PCL レベル 1 から 5e/5c は、受信順に処理・解釈される制御シーケンスを使用するコマンドベースの言語です。コンシューマーレベルでは、PCL データストリームは印刷ドライバによって生成されます。PCL の出力はカスタムアプリケーションでも簡単に生成できます。

{{% alert color="success" %}}
**オンラインで PCL を PDF に変換してみる**

Aspose.PDF for for .NET は、オンラインの無料アプリケーション ["PCL を PDF に変換"](https://products.aspose.app/pdf/conversion/pcl-to-pdf) を提供します。ここで、機能と品質をご確認いただけます。

[![Aspose.PDF 変換 PCL から PDF への無料アプリ](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

PCL から PDF への変換を可能にするため、Aspose.PDF は [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions) クラスを提供しています。このクラスは LoadOptions オブジェクトの初期化に使用されます。その後、Document オブジェクトの初期化時にこのオブジェクトが引数として渡され、PDF レンダリングエンジンがソースドキュメントの入力形式を判断できるようにします。

以下のコードスニペットは、PCL ファイルを PDF 形式に変換するプロセスを示しています。

Python で PCL を PDF に変換する手順：

1. PclLoadOptions() を使用して PCL のロードオプションを設定します。
1. ドキュメントを読み込みます。
1. PDF として保存します。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.PclLoadOptions()
    load_options.supress_errors = True

    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## 整形済みテキストを PDF に変換

**Aspose.PDF for Python via .NET** は、プレーンテキストおよび整形済みテキストファイルを PDF 形式に変換する機能をサポートします。

テキストを PDF に変換するということは、PDF ページにテキストフラグメントを追加することを意味します。テキストファイルに関しては、整形済みテキスト（例：1 行 80 文字、25 行など）と非整形テキスト（プレーンテキスト）の 2 種類を扱います。必要に応じて、追加を自分で制御することも、ライブラリのアルゴリズムに任せることもできます。

{{% alert color="success" %}}
**オンラインで TEXT を PDF に変換してみる**

Aspose.PDF for Python via .NET は、オンラインの無料アプリケーション ["テキストを PDF に変換"](https://products.aspose.app/pdf/conversion/txt-to-pdf) を提供します。ここで、機能と品質をご確認いただけます。

[![Aspose.PDF 変換 TEXT から PDF への無料アプリ](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

Python で TEXT を PDF に変換する手順：

1. 入力テキストファイルを行ごとに読み取ります。
1. 等幅フォント（Courier New）を設定し、テキストの整列を一定にします。
1. 新しい PDF ドキュメントを作成し、カスタム余白とフォント設定で最初のページを追加します。
1. テキストファイルの行を反復処理します。タイプライターをシミュレートするため、'monospace_font' フォントとサイズ 12 を使用します。
1. ページ作成を最大 4 ページに制限します。
1. 最終的な PDF を指定されたパスに保存します。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    with open(path_infile, "r") as file:
        lines = file.readlines()

    monospace_font = ap.text.FontRepository.find_font("Courier New")

    document = ap.Document()
    page = document.pages.add()

    page.page_info.margin.left = 20
    page.page_info.margin.right = 10
    page.page_info.default_text_state.font = monospace_font
    page.page_info.default_text_state.font_size = 12
    count = 1
    for line in lines:
        if line != "" and line[0] == "\x0c":
            page = document.pages.add()
            page.page_info.margin.left = 20
            page.page_info.margin.right = 10
            page.page_info.default_text_state.font = monospace_font
            page.page_info.default_text_state.font_size = 12
            count = count + 1
        else:
            text = ap.text.TextFragment(line)
            page.paragraphs.add(text)

        if count == 4:
            break

    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## PostScript を PDF に変換

この例では、Aspose.PDF for Python via .NET を使用して PostScript ファイルを PDF ドキュメントに変換する方法を示します。

1. PS ファイルを正しく解釈するために 'PsLoadOptions' のインスタンスを作成します。
1. ロードオプションを使用して 'PostScript' ファイルを Document オブジェクトにロードします。
1. ドキュメントを PDF 形式で希望の出力パスに保存します。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.PsLoadOptions()

    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## XPS を PDF に変換

**Aspose.PDF for Python via .NET** は <abbr title="XML Paper Specification">XPS</abbr> ファイルを PDF 形式に変換する機能をサポートしています。この記事を確認してタスクを解決してください。

XPS ファイルタイプは主に Microsoft Corporation の XML Paper Specification（XML ペーパー仕様）に関連付けられています。XML Paper Specification (XPS) は、かつて Metro とコード名が付けられ、Next Generation Print Path（NGPP）というマーケティングコンセプトを包含していた、Microsoft の Windows オペレーティングシステムにドキュメント作成と閲覧を統合する取り組みです。

以下のコードスニペットは、Python を使用して XPS ファイルを PDF 形式に変換するプロセスを示しています。

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.XpsLoadOptions()
    document = ap.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**XPS 形式をオンラインで PDF に変換してみましょう**

Aspose.PDF for Python via .NET は、オンラインで無料のアプリケーション ["XPS を PDF に変換"](https://products.aspose.app/pdf/conversion/xps-to-pdf/) を提供し、機能と品質を試すことができます。

[![Aspose.PDF 無料アプリで XPS から PDF へ変換](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## XSL-FO を PDF に変換

以下のコードスニペットは、Aspose.PDF for Python via .NET を使用して XSL-FO を PDF 形式に変換するために使用できます。

```python

    from os import path
    import aspose.pdf as ap

    path_xsltfile = path.join(self.data_dir, xsltfile)
    path_xmlfile = path.join(self.data_dir, xmlfile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = ap.XslFoLoadOptions(path_xsltfile)
    load_options.parsing_errors_handling_type = (
        ap.XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately
    )
    document = ap.Document(path_xmlfile, load_options)
    document.save(path_outfile)

    print(xmlfile + " converted into " + outfile)
```

## XSLT を使用した XML を PDF に変換

この例では、XSLT テンプレートを使用して XML ファイルを HTML に変換し、その後 HTML を Aspose.PDF にロードして PDF に変換する方法を示します。

1. HTML から PDF への変換を設定するために 'HtmlLoadOptions' のインスタンスを作成します。
1. 変換された HTML ファイルを Aspose.PDF Document オブジェクトにロードします。
1. 指定された出力パスに PDF としてドキュメントを保存します。
1. 変換が成功したら、一時的な HTML ファイルを削除します。

```python

    from os import path
    import aspose.pdf as ap

    def transform_xml_to_html(xml_file, xslt_file, html_file):
        from lxml import etree
        """
        Transform XML to HTML using XSLT and return as a stream
        """
        # Parse XML document
        xml_doc = etree.parse(xml_file)

        # Parse XSLT stylesheet
        xslt_doc = etree.parse(xslt_file)
        transform = etree.XSLT(xslt_doc)

        # Apply transformation
        result = transform(xml_doc)

        # Save result to HTML file
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(str(result))


    def convert_XML_to_PDF(template, infile, outfile):
        path_infile = path.join(data_dir, infile)
        path_outfile = path.join(data_dir, "python", outfile)
        path_template = path.join(data_dir, template)
        path_temp_file = path.join(data_dir, "temp.html")

        load_options = ap.HtmlLoadOptions()
        transform_xml_to_html(path_infile, path_template, path_temp_file)

        document = ap.Document(path_temp_file, load_options)
        document.save(path_outfile)

        if path.exists(path_temp_file):
            os.remove(path_temp_file)

        print(infile + " converted into " + outfile)
```

