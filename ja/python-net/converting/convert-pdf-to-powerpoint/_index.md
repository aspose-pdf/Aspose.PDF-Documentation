---
title: PythonでPDFをPowerPointに変換
linktitle: PDFをPowerPointに変換
type: docs
weight: 30
url: ja/python-net/convert-pdf-to-powerpoint/
description: Aspose.PDFを使用すると、Pythonを使ってPDFをPPT（PowerPoint）形式に変換できます。PDFをスライドとして画像でPPTXに変換する可能性があります。
lastmod: "2022-12-23"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 概要

PDFファイルをPowerPointに変換することは可能ですか？はい、可能です！そして簡単です！
この記事では、Pythonを使用して**PDFをPowerPointに変換する方法**を説明します。以下のトピックをカバーしています。

_フォーマット_: **PPTX**
- [Python PDFからPPTXへ](#python-pdf-to-pptx)
- [Python PDFをPPTXに変換](#python-pdf-to-pptx)
- [Python PDFファイルをPPTXに変換する方法](#python-pdf-to-pptx)

_フォーマット_: **PowerPoint**
- [Python PDFからPowerPointへ](#python-pdf-to-powerpoint)
- [Python PDFをPowerPointに変換](#python-pdf-to-powerpoint)
- [Python PDFファイルをPowerPointに変換する方法](#python-pdf-to-powerpoint)


## PythonでPDFをPowerPointおよびPPTXに変換する方法

**Aspose.PDF for Python via .NET**を使用すると、PDFからPPTXへの変換の進行状況を追跡できます。

Aspose.SlidesというAPIがあり、PPT/PPTXプレゼンテーションの作成および操作機能を提供しています。このAPIは、PPT/PPTXファイルをPDF形式に変換する機能も提供します。この変換中に、PDFファイルの個々のページはPPTXファイルの別々のスライドに変換されます。

PDFから<abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>への変換中に、テキストは選択または更新できるテキストとしてレンダリングされます。PDFファイルをPPTX形式に変換するために、Aspose.PDFは[PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/)というクラスを提供しています。PptxSaveOptionsクラスのオブジェクトは、[save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)の2番目の引数として渡されます。以下のコードスニペットは、PDFファイルをPPTX形式に変換するプロセスを示しています。

## PythonとAspose.PDF for Pythonを使用したPDFからPowerPointへの簡単な変換

PDFをPPTXに変換するために、Aspose.PDF for Pythonは次のコードステップを使用することを推奨します。

<a name="csharp-pdf-to-powerpoint"><strong>手順: PythonでPDFをPowerPointに変換する</strong></a> | <a name="csharp-pdf-to-pptx"><strong>手順: PythonでPDFをPPTXに変換する</strong></a>

1. [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) クラスのインスタンスを作成する
2. [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) クラスのインスタンスを作成する
3. **Document** オブジェクトの **Save** メソッドを使用してPDFをPPTXとして保存する

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx.pptx"
    # PDFドキュメントを開く
    document = ap.Document(input_pdf)
    # PptxSaveOptionsインスタンスを作成
    save_option = ap.PptxSaveOptions()
    # ファイルをMS PowerPoint形式で保存
    document.save(output_pdf, save_option)
```

## スライドを画像としてPDFをPPTXに変換する


{{% alert color="success" %}}
**オンラインでPDFをPowerPointに変換してみてください**

Aspose.PDF for Pythonでは、オンラインの無料アプリケーション["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)を提供しており、機能性と品質を試すことができます。

[![Aspose.PDF コンバージョン PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

検索可能なPDFを選択可能なテキストではなく画像としてPPTXに変換する必要がある場合、Aspose.PDFは[PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/)クラスを通じてその機能を提供します。これを達成するには、以下のコードサンプルに示すように、[PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/)クラスのプロパティ[slides_as_images](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties)を'true'に設定します。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_pptx_with_slides_as_images.pptx"
    # PDFドキュメントを開く
    document = ap.Document(input_pdf)
    # PptxSaveOptionsインスタンスを作成
    save_option = ap.PptxSaveOptions()
    save_option.slides_as_images = True
    # ファイルをMS PowerPoint形式で保存
    document.save(output_pdf, save_option)
```


## 参照

この記事はこれらのトピックもカバーしています。コードは上記と同じです。

_フォーマット_: **PowerPoint**
- [Python PDF to PowerPoint コード](#python-pdf-to-powerpoint)
- [Python PDF to PowerPoint API](#python-pdf-to-powerpoint)
- [Python PDF to PowerPoint プログラム](#python-pdf-to-powerpoint)
- [Python PDF to PowerPoint ライブラリ](#python-pdf-to-powerpoint)
- [Python PDFをPowerPointとして保存](#python-pdf-to-powerpoint)
- [Python PDFからPowerPointを生成](#python-pdf-to-powerpoint)
- [Python PDFからPowerPointを作成](#python-pdf-to-powerpoint)
- [Python PDF to PowerPoint コンバーター](#python-pdf-to-powerpoint)

_フォーマット_: **PPTX**
- [Python PDF to PPTX コード](#python-pdf-to-pptx)
- [Python PDF to PPTX API](#python-pdf-to-pptx)
- [Python PDF to PPTX プログラム](#python-pdf-to-pptx)
- [Python PDF to PPTX ライブラリ](#python-pdf-to-pptx)
- [Python PDFをPPTXとして保存](#python-pdf-to-pptx)
- [Python PDFからPPTXを生成](#python-pdf-to-pptx)
- [Python PDFからPPTXを作成](#python-pdf-to-pptx)
- [Python PDF to PPTX コンバーター](#python-pdf-to-pptx)