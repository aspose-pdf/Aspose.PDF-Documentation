---
title: PythonでPDFをMicrosoft Word文書に変換する
linktitle: PDFをWord 2003/2019に変換
type: docs
weight: 10
url: /ja/python-java/convert-pdf-to-word/
lastmod: "2023-04-06"
description: Aspose.PDF for Python via .NETを使用して、PDFからMicrosoft Word形式への変換用Pythonコードの書き方を学びます。また、PDFからDOC(DOCX)への変換を調整します。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 概要

この記事では、Pythonを使用して**PDFをMicrosoft Word文書に変換する方法**について説明します。以下のトピックをカバーします。

_フォーマット_: **DOC**
- [Python PDFをDOCに](#python-pdf-to-doc)
- [Python PDFをDOCに変換](#python-pdf-to-doc)
- [Python PDFファイルをDOCに変換する方法](#python-pdf-to-doc)

_フォーマット_: **DOCX**
- [Python PDFをDOCXに](#python-pdf-to-docx)
- [Python PDFをDOCXに変換](#python-pdf-to-docx)
- [Python PDFファイルをDOCXに変換する方法](#python-pdf-to-docx)

_フォーマット_: **Word**
- [Python PDFをWordに](#python-pdf-to-docx)
- [Python PDFをWordに変換](#python-pdf-to-doc)

- [Python PDFファイルをWordに変換する方法](#python-pdf-to-docx)

## Python PDF to DOCおよびDOCX変換

最も人気のある機能の1つは、PDFからMicrosoft Word DOCへの変換であり、コンテンツ管理を容易にします。**Aspose.PDF for Python**は、PDFファイルをDOCだけでなくDOCX形式にも簡単かつ効率的に変換することができます。

## PDFをDOC（Word 97-2003）ファイルに変換

PDFファイルを簡単にDOC形式に変換し、完全に制御することができます。Aspose.PDF for Pythonは柔軟で、さまざまな変換をサポートしています。例えば、PDFドキュメントのページを画像に変換することは非常に人気のある機能です。

多くのお客様からリクエストされた変換は、PDFからDOCへの変換です。これは、PDFファイルをMicrosoft Wordドキュメントに変換することです。お客様は、PDFファイルは簡単に編集できないのに対し、Wordドキュメントは編集できるため、これを望んでいます。いくつかの企業は、ユーザーがPDFとして始まったファイルのテキスト、表、画像を操作できるようにしたいと考えています。

物事を簡単で理解しやすくするという伝統を守り続け、Aspose.PDF for Pythonでは、ソースPDFファイルを2行のコードでDOCファイルに変換できます。
 この機能を実現するために、SaveFormatという列挙を導入しました。その値.DOCは、ソースファイルをMicrosoft Word形式で保存することができます。

以下のPythonコードスニペットは、PDFファイルをDOC形式に変換するプロセスを示しています。

<a name="csharp-pdf-to-doc"><strong>ステップ: PythonでPDFをDOCに変換する</strong></a>

1. ソースPDFドキュメントを持つ[Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/)オブジェクトのインスタンスを作成します。
2. [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods)メソッドを呼び出して、[SaveFormat.Doc](https://reference.aspose.com/pdf/python-java/aspose.pdf/saveformat/)形式で保存します。

```python

from asposepdf import Api

documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/out.doc"
doc.save(documentOutName, Api.SaveFormat.Doc)
```

### DocSaveOptionsクラスの使用

[DocSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/docsaveoptions/)クラスは、PDFファイルをDOC形式に変換するプロセスを改善する多数のプロパティを提供します。 これらのプロパティの中で、ModeはPDFコンテンツの認識モードを指定することを可能にします。このプロパティには、RecognitionMode列挙から任意の値を指定することができます。これらの各値には特定の利点と制限があります。

```python

from asposepdf import Api

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.doc"
# PDFドキュメントを開く
document = Api.Document(input_pdf)

save_options = Api.DocSaveOptions()
save_options.format = Api.DocSaveOptions.DocFormat.Doc
# 認識モードをFlowとして設定
save_options.mode = Api.DocSaveOptions.RecognitionMode.Flow
# 水平近似を2.5に設定
save_options.relative_horizontal_proximity = 2.5
# 変換プロセス中に箇条書きを認識するように値を有効にする
save_options.recognize_bullets = True

# ファイルをMS Wordドキュメント形式で保存
document.save(output_pdf, save_options)

```

{{% alert color="success" %}}
**PDFをDOCにオンラインで変換してみてください**

Aspose.PDF for Pythonは、オンライン無料アプリケーション["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)を提供しており、その機能と品質を試すことができます。
[![Convert PDF to DOC](/pdf/ja/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) {{% /alert %}}

## PDFをDOCXに変換

Aspose.PDF for Python APIを使用すると、Python via .NETを使ってPDFドキュメントをDOCXに読み取り、変換することができます。DOCXは、Microsoft Wordドキュメントのためのよく知られたフォーマットであり、その構造はプレーンなバイナリからXMLとバイナリファイルの組み合わせに変更されました。DocxファイルはWord 2007およびそれ以降のバージョンで開くことができますが、DOCファイル拡張子をサポートする以前のMS Wordバージョンでは開くことができません。

以下のPythonコードスニペットは、PDFファイルをDOCX形式に変換するプロセスを示しています。

<a name="csharp-pdf-to-docx"><strong>ステップ: PythonでPDFをDOCXに変換</strong></a>

1. ソースPDFドキュメントを使用して[Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/)オブジェクトのインスタンスを作成します。

2. [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) メソッドを呼び出して、[SaveFormat.DocX](https://reference.aspose.com/pdf/python-java/aspose.pdf/saveformat/) 形式で保存します。

```python


from asposepdf import Api

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.docx"
# PDFドキュメントを開く
document = Api.Document(input_pdf)

save_options = Api.DocSaveOptions()
save_options.format = Api.DocSaveOptions.DocFormat.Docx
# 認識モードをFlowとして設定
save_options.mode = Api.DocSaveOptions.RecognitionMode.Flow
# 水平方向の近接度を2.5として設定
save_options.relative_horizontal_proximity = 2.5
# 変換プロセス中に箇条書きを認識するための値を有効にする
save_options.recognize_bullets = True

# ファイルをMS Wordドキュメント形式で保存
document.save(output_pdf, save_options)
```

[DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) クラスには、結果のドキュメントの形式を指定する機能を提供するFormatというプロパティがあり、DOCまたはDOCXです。
 PDFファイルをDOCX形式に変換するには、DocSaveOptions.DocFormat列挙からDocx値を渡してください。

{{% alert color="warning" %}}
**PDFをDOCXにオンラインで変換してみてください**

Aspose.PDF for Pythonは、オンラインで無料のアプリケーション["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)を提供しており、その機能と品質を試すことができます。

[![Aspose.PDF Convertion PDF to Word Free App](/pdf/ja/java/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## 関連情報

この記事はこれらのトピックもカバーしています。コードは上記と同じです。

_フォーマット_: **Word**
- [Python PDFからWordへのコード](#python-pdf-to-docx)
- [Python PDFからWordへのAPI](#python-pdf-to-docx)
- [PythonでPDFをWordにプログラム的に変換](#python-pdf-to-docx)
- [Python PDFからWordライブラリ](#python-pdf-to-docx)
- [PythonでPDFをWordとして保存](#python-pdf-to-docx)
- [PythonでPDFからWordを生成](#python-pdf-to-docx)
- [PythonでPDFからWordを作成](#python-pdf-to-docx)

- [Python PDFからWordへのコンバータ](#python-pdf-to-docx)
_Format_: **DOC**
- [Python PDF to DOC Code](#python-pdf-to-doc)
- [Python PDF to DOC API](#python-pdf-to-doc)
- [Python PDF to DOC Programmatically](#python-pdf-to-doc)
- [Python PDF to DOC Library](#python-pdf-to-doc)
- [Python Save PDF as DOC](#python-pdf-to-doc)
- [Python Generate DOC from PDF](#python-pdf-to-doc)
- [Python Create DOC from PDF](#python-pdf-to-doc)
- [Python PDF to DOC Converter](#python-pdf-to-doc)

_Format_: **DOCX**
- [Python PDF to DOCX Code](#python-pdf-to-docx)
- [Python PDF to DOCX API](#python-pdf-to-docx)
- [Python PDF to DOCX Programmatically](#python-pdf-to-docx)
- [Python PDF to DOCX Library](#python-pdf-to-docx)
- [Python Save PDF as DOCX](#python-pdf-to-docx)
- [Python Generate DOCX from PDF](#python-pdf-to-docx)
- [Python Create DOCX from PDF](#python-pdf-to-docx)
- [Python PDF to DOCX Converter](#python-pdf-to-docx)