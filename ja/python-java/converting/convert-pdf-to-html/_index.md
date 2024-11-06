---
title: PDFをHTMLに変換するPython 
linktitle: PDFをHTML形式に変換
type: docs
weight: 50
url: ja/python-java/convert-pdf-to-html/
lastmod: "2021-11-01"
description: このトピックでは、Aspose.PDF for Python Javaライブラリを使用してPDFファイルをHTML形式に変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 概要

この記事では、Pythonを使用して**PDFをHTMLに変換する**方法を説明します。これらのトピックをカバーします。

_形式_: **HTML**
- [Python PDFからHTMLへ](#python-pdf-to-html)
- [Python PDFをHTMLに変換](#python-pdf-to-html)
- [Python PDFファイルをHTMLに変換する方法](#python-pdf-to-html)


## PDFをHTMLに変換

**.NET経由のAspose.PDF for Python**は、さまざまなファイル形式をPDFドキュメントに変換し、PDFファイルをさまざまな出力形式に変換するための多くの機能を提供します。
 この記事では、PDFファイルを<abbr title="HyperText Markup Language">HTML</abbr>に変換する方法について説明します。PDFをHTMLに変換するために、Pythonのほんの数行のコードを使用することができます。ウェブサイトを作成したり、オンラインフォーラムにコンテンツを追加したりする場合、PDFをHTMLに変換する必要があるかもしれません。PDFをHTMLに変換する一つの方法は、Pythonを使用してプログラム的に行うことです。

{{% alert color="success" %}}
**オンラインでPDFをHTMLに変換してみてください**

Aspose.PDF for Pythonは、オンラインで無料のアプリケーション["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)を提供しており、その機能と品質を試してみることができます。

[![Aspose.PDF Convertion PDF to HTML with Free App](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

<a name="csharp-pdf-to-html"><strong>ステップ: PythonでPDFをHTMLに変換する</strong></a>

1. ソースPDFドキュメントを使用して[Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/)オブジェクトのインスタンスを作成します。
2. [Document.save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) メソッドを呼び出して、[HtmlSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/htmlsaveoptions/) に保存します。

```python
from asposepdf import Api

documentName = "../../testdata/source.pdf"
documentOutName = "../../testout/result.html"
# PDFドキュメントを開く
document = Api.Document(documentName)

# ドキュメントをHTML形式で保存
save_options = Api.HtmlSaveOptions()
document.save(documentOutName, save_options)
```

## 関連項目

この記事は次のトピックもカバーしています。コードは上記と同じです。

_フォーマット_: **HTML**
- [Python PDFをHTMLに変換するコード](#python-pdf-to-html)
- [Python PDFをHTMLに変換するAPI](#python-pdf-to-html)
- [Python PDFをHTMLにプログラムで変換](#python-pdf-to-html)
- [Python PDFをHTMLに変換するライブラリ](#python-pdf-to-html)
- [Python PDFをHTMLとして保存](#python-pdf-to-html)
- [Python PDFからHTMLを生成](#python-pdf-to-html)
- [Python PDFからHTMLを作成](#python-pdf-to-html)

- [Python PDFをHTMLに変換するコンバーター](#python-pdf-to-html)