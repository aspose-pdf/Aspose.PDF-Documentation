---
title: PythonでPDFをHTMLに変換
linktitle: PDFをHTML形式に変換
type: docs
weight: 50
url: /ja/python-net/convert-pdf-to-html/
lastmod: "2021-11-01"
description: このトピックでは、Aspose.PDF for Python .NETライブラリを使用してPDFファイルをHTML形式に変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 概要

この記事では、Pythonを使用して**PDFをHTMLに変換する方法**を説明します。次のトピックをカバーします。

_形式_: **HTML**
- [Python PDFをHTMLに](#python-pdf-to-html)
- [Python PDFをHTMLに変換](#python-pdf-to-html)
- [Python PDFファイルをHTMLに変換する方法](#python-pdf-to-html)


## PDFをHTMLに変換

**Aspose.PDF for Python via .NET**は、さまざまなファイル形式をPDFドキュメントに変換し、PDFファイルをさまざまな出力形式に変換するための多くの機能を提供します。
 この記事では、PDFファイルを<abbr title="HyperText Markup Language">HTML</abbr>に変換する方法について説明します。PDFをHTMLに変換するために、Pythonのコードを数行だけ使用することができます。ウェブサイトを作成したり、オンラインフォーラムにコンテンツを追加したりする場合に、PDFをHTMLに変換する必要があるかもしれません。PDFをHTMLに変換する一つの方法は、Pythonをプログラム的に使用することです。

{{% alert color="success" %}}
**オンラインでPDFをHTMLに変換してみる**

Aspose.PDF for Pythonは、無料のオンラインアプリケーション["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF Convertion PDF to HTML with Free App](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

<a name="csharp-pdf-to-html"><strong>手順: PythonでPDFをHTMLに変換する</strong></a>

1. ソースPDFドキュメントを使用して[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)オブジェクトのインスタンスを作成します。
2. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを呼び出して [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/) に保存します。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_html.html"
    # PDFドキュメントを開く
    document = ap.Document(input_pdf)

    # ドキュメントをHTML形式で保存
    save_options = ap.HtmlSaveOptions()
    document.save(output_pdf, save_options)
```

## 関連情報

この記事は以下のトピックもカバーしています。コードは上記と同じです。

_フォーマット_: **HTML**
- [Python PDF to HTML コード](#python-pdf-to-html)
- [Python PDF to HTML API](#python-pdf-to-html)
- [Python PDF to HTML プログラムによる実装](#python-pdf-to-html)
- [Python PDF to HTML ライブラリ](#python-pdf-to-html)
- [Python PDF を HTML として保存](#python-pdf-to-html)
- [Python PDF から HTML を生成](#python-pdf-to-html)
- [Python PDF から HTML を作成](#python-pdf-to-html)

- [Python PDF to HTML コンバーター](#python-pdf-to-html)