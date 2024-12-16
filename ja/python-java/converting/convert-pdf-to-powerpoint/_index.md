---
title: PDFをPowerPointに変換するPython
linktitle: PDFをPowerPointに変換する
type: docs
weight: 30
url: /ja/python-java/convert-pdf-to-powerpoint/
description: Aspose.PDFを使用して、PythonでPDFをPPT（PowerPoint）形式に変換できます。一つの方法として、スライドを画像としてPDFをPPTXに変換する可能性があります。
lastmod: "2023-04-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 概要

PDFファイルをPowerPointに変換することは可能ですか？はい、可能です！そして、それは簡単です！
この記事では、Pythonを使用して**PDFをPowerPointに変換する方法**を説明します。これらのトピックをカバーしています。

_形式_: **PPTX**
- [Python PDFをPPTXに](#python-pdf-to-pptx)
- [Python PDFをPPTXに変換する](#python-pdf-to-pptx)
- [Python PDFファイルをPPTXに変換する方法](#python-pdf-to-pptx)

_形式_: **PowerPoint**
- [Python PDFをPowerPointに](#python-pdf-to-powerpoint)
- [Python PDFをPowerPointに変換する](#python-pdf-to-powerpoint)
- [Python PDFファイルをPowerPointに変換する方法](#python-pdf-to-powerpoint)


## Python PDFをPowerPointおよびPPTXに変換する

**Aspose.PDF for Python via Java**は、PDFからPPTXへの変換の進行状況を追跡することができます。

Aspose.Slidesという名前のAPIがあり、PPT/PPTXプレゼンテーションを作成および操作する機能を提供します。このAPIはまた、PPT/PPTXファイルをPDF形式に変換する機能も提供しています。この変換中に、PDFファイルの個々のページはPPTXファイルの個別のスライドに変換されます。

PDFから<abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>への変換では、テキストは選択/更新可能なテキストとしてレンダリングされます。PDFファイルをPPTX形式に変換するには、Aspose.PDFが[`PptxSaveOptions`](https://reference.aspose.com/pdf/java/aspose.pdf/pptxsaveoptions)という名前のクラスを提供していることに注意してください。PptxSaveOptionsクラスのオブジェクトは、[`Document.Save(..) メソッド`](https://reference.aspose.com/pdf/java/aspose.pdf/document/methods/save)の第二引数として渡されます。以下のコードスニペットは、PDFファイルをPPTX形式に変換するプロセスを示しています。

## PythonとAspose.PDF for Pythonを使用した単純なPDFからPowerPointへの変換

PDFをPPTXに変換するために、Aspose.PDF for Pythonは以下のコードステップを使用することを推奨します。

<a name="csharp-pdf-to-powerpoint"><strong>ステップ: PythonでPDFをPowerPointに変換</strong></a> | <a name="csharp-pdf-to-pptx"><strong>ステップ: PythonでPDFをPPTXに変換</strong></a>

1. [Document](https://reference.aspose.com/pdf/java/aspose.pdf/document) クラスのインスタンスを作成します
2. [PptxSaveOptions](https://reference.aspose.com/pdf/java/aspose.pdf/pptxsaveoptions) クラスのインスタンスを作成します
3. **Document** オブジェクトの **Save** メソッドを使用して、PDFをPPTXとして保存します

```python

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx_with_options.pptx"
# PDFドキュメントを開く
document = Api.Document(input_pdf)

save_options = Api.PptxSaveOptions()
save_options._ImageResolution = 300
save_options._SeparateImages = True
save_options._OptimizeTextBoxes = True

# ファイルをMS Wordのドキュメント形式で保存する
document.save(output_pdf, save_options)
```


## PDFをスライドとして画像に変換してPPTXにする

{{% alert color="success" %}}
**PDFをPowerPointにオンラインで変換してみてください**

Aspose.PDF for Pythonは、オンラインで無料アプリケーション["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)を提供しており、その機能と品質を試すことができます。

[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

選択可能なテキストの代わりに画像として検索可能なPDFをPPTXに変換する必要がある場合、Aspose.PDFは[Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/)クラスを通じてそのような機能を提供します。これを達成するには、次のコードサンプルに示すように、[PptxSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/)クラスのプロパティ[SlidesAsImages](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/#properties)を'true'に設定します。

```python

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx_with_options.pptx"
# PDFドキュメントを開く
document = Api.Document(input_pdf)

save_options = Api.PptxSaveOptions()
save_options._ImageResolution = 300
save_options._SlidesAsImages = True

# ファイルをMS Wordドキュメント形式で保存
document.save(output_pdf, save_options)
```


## 関連項目

この記事では、これらのトピックも取り上げています。コードは上記と同じです。

_フォーマット_: **PowerPoint**
- [Python PDF to PowerPoint Code](#python-pdf-to-powerpoint)
- [Python PDF to PowerPoint API](#python-pdf-to-powerpoint)
- [Python PDF to PowerPoint Programmatically](#python-pdf-to-powerpoint)
- [Python PDF to PowerPoint Library](#python-pdf-to-powerpoint)
- [Python Save PDF as PowerPoint](#python-pdf-to-powerpoint)
- [Python Generate PowerPoint from PDF](#python-pdf-to-powerpoint)
- [Python Create PowerPoint from PDF](#python-pdf-to-powerpoint)
- [Python PDF to PowerPoint Converter](#python-pdf-to-powerpoint)

_フォーマット_: **PPTX**
- [Python PDF to PPTX Code](#python-pdf-to-pptx)
- [Python PDF to PPTX API](#python-pdf-to-pptx)
- [Python PDF to PPTX Programmatically](#python-pdf-to-pptx)
- [Python PDF to PPTX Library](#python-pdf-to-pptx)
- [Python Save PDF as PPTX](#python-pdf-to-pptx)
- [Python Generate PPTX from PDF](#python-pdf-to-pptx)
- [Python Create PPTX from PDF](#python-pdf-to-pptx)
- [Python PDF to PPTX Converter](#python-pdf-to-pptx)