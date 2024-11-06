---
title: PDFをEPUB、LaTeX、Text、XPSに変換するPython
linktitle: PDFを他の形式に変換
type: docs
weight: 90
url: ja/python-net/convert-pdf-to-other-files/
lastmod: "2022-12-23"
keywords: convert, PDF, EPUB, LaText, Text, XPS, Python
description: このトピックでは、Pythonを使用してPDFファイルをEPUB、LaTeX、Text、XPSなどの他のファイル形式に変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## PDFをEPUBに変換

{{% alert color="success" %}}
**PDFをEPUBにオンラインで変換してみる**

Aspose.PDF for Pythonは、オンラインで無料のアプリケーション["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF Convertion PDF to EPUB with Free App](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Electronic Publication">EPUB</abbr>**は、国際デジタル出版フォーラム（IDPF）による無料でオープンな電子書籍標準です。
 ファイルには拡張子.epubがあります。  
EPUBはリフロー可能なコンテンツ向けに設計されており、EPUBリーダーは特定の表示デバイスに最適化されたテキストを表示することができます。また、EPUBは固定レイアウトのコンテンツもサポートしています。このフォーマットは、出版社や変換ハウスが社内で使用したり、配布や販売のために使用できる単一のフォーマットとして意図されています。Open eBook標準に代わるものです。

Aspose.PDF for Pythonは、PDFドキュメントをEPUB形式に変換する機能もサポートしています。Aspose.PDF for Pythonには「EpubSaveOptions」というクラスがあり、[save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)メソッドの第2引数として使用して、EPUBファイルを生成することができます。Pythonを使用してこの要件を達成するには、次のコードスニペットを試してください。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_epub.epub"
    # PDFドキュメントを開く
    document = ap.Document(input_pdf)

    # Epub Saveオプションをインスタンス化
    save_options = ap.EpubSaveOptions()

    # コンテンツのレイアウトを指定
    save_options.content_recognition_mode = ap.EpubSaveOptions.RecognitionMode.FLOW

    # ePUBドキュメントを保存
    document.save(output_pdf, save_options)
```

## PDFをLaTeX/TeXに変換する

**Aspose.PDF for Python via .NET**は、PDFをLaTeX/TeXに変換することをサポートしています。LaTeXファイル形式は、特殊なマークアップを持つテキストファイル形式であり、高品質な組版のためのTeXベースのドキュメント準備システムで使用されます。

{{% alert color="success" %}}
**PDFをLaTeX/TeXにオンラインで変換してみる**

Aspose.PDF for Pythonは、オンラインで無料アプリケーション["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)を提供しており、機能と品質を調べることができます。

[![Aspose.PDF Convertion PDF to LaTeX/TeX with Free App](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

PDFファイルをTeXに変換するには、Aspose.PDFには[LaTeXSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/)というクラスがあり、変換プロセス中に一時的な画像を保存するためのOutDirectoryPathプロパティを提供しています。

次のコードスニペットは、PythonでPDFファイルをTEX形式に変換するプロセスを示しています。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_tex.tex"
    # PDFドキュメントを開く
    document = ap.Document(input_pdf)
    # LaTeXSaveOptionsのオブジェクトをインスタンス化
    saveOptions = ap.LaTeXSaveOptions()
    document.save(output_pdf, saveOptions)
```

## PDFをテキストに変換

**Aspose.PDF for Python**は、PDFドキュメント全体と単一ページをテキストファイルに変換することをサポートしています。

### PDFドキュメントをテキストファイルに変換

'TextDevice'クラスを使用してPDFドキュメントをTXTファイルに変換することができます。

次のコードスニペットは、すべてのページからテキストを抽出する方法を説明します。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_txt.txt"
    # PDFドキュメントを開く
    document = ap.Document(input_pdf)

    # テキストデバイスを作成
    textDevice = ap.devices.TextDevice()

    # 特定のページを変換して保存
    textDevice.process(document.pages[1], output_pdf)
```
**PDFをテキストにオンラインで変換してみる**
{{% alert color="success" %}}

Aspose.PDF for Pythonは、オンラインで無料のアプリケーション["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)を提供しています。これを使って、その機能性と品質を調査してみてください。

[![Aspose.PDF Convertion PDF to Text with Free App](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## PDFをXPSに変換する

**Aspose.PDF for Python**は、PDFファイルを<abbr title="XML Paper Specification">XPS</abbr>形式に変換する可能性を提供します。PythonでPDFファイルをXPS形式に変換するために提示されたコードスニペットを使ってみましょう。

{{% alert color="success" %}}
**PDFをXPSにオンラインで変換してみる**

Aspose.PDF for Pythonは、オンラインで無料のアプリケーション["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)を提供しています。これを使って、その機能性と品質を調査してみてください。

[![Aspose.PDF Convertion PDF to XPS with Free App](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

XPSファイルタイプは、主にMicrosoft CorporationによるXML Paper Specificationに関連付けられています。XML Paper Specification（XPS）は、以前はMetroというコードネームで呼ばれ、Next Generation Print Path（NGPP）というマーケティングコンセプトを包含しており、Windowsオペレーティングシステムに文書の作成と閲覧を統合するためのMicrosoftの取り組みです。

PDFファイルをXPSに変換するには、Aspose.PDFには[XpsSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/)クラスがあり、これはXPSファイルを生成するために[save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)メソッドの第2引数として使用されます。

次のコードスニペットは、PDFファイルをXPS形式に変換するプロセスを示しています。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xps.xps"
    # PDFドキュメントを開く
    document = ap.Document(input_pdf)

    # XPS保存オプションをインスタンス化
    save_options = ap.XpsSaveOptions()

    # XPSドキュメントを保存
    document.save(output_pdf, save_options)
```

## PDFをXMLに変換

{{% alert color="success" %}}
**PDFをXMLにオンラインで変換してみてください**

Aspose.PDF for Pythonは、オンラインで無料アプリケーション「[PDF to XML](https://products.aspose.app/pdf/conversion/pdf-to-xml)」を提供しており、その機能と品質をお試しいただけます。

[![Aspose.PDF Convertion PDF to XML with Free App](pdf_to_xml.png)](https://products.aspose.app/pdf/conversion/pdf-to-xml)
{{% /alert %}}

<abbr title="拡張可能なマークアップ言語">XML</abbr>は、任意のデータを保存、送信、再構築するためのマークアップ言語およびファイル形式です。

Aspose.PDF for Pythonは、PDFドキュメントをXML形式に変換する機能もサポートしています。Aspose.PDF for Pythonには「XmlSaveOptions」というクラスがあり、[save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)メソッドの第2引数として使用して、XMLファイルを生成することができます。この要件をPythonで達成するために、次のコードスニペットを試してください。

```python

    import aspose.pdf as ap

    def convert_pdf_to_xml(self, infile, outfile):
        path_infile = self.dataDir + infile
        path_outfile = self.dataDir + outfile

        # PDFドキュメントを開く

        document = ap.Document(path_infile)

        # XML保存オプションをインスタンス化
        save_options = ap.XmlSaveOptions()

        # XMLドキュメントを保存
        document.save(path_outfile, save_options)
        print(infile + " が " + outfile + " に変換されました")
```