---
title: PythonでPDFをMicrosoft Word文書に変換
linktitle: PDFをWord 2003/2019に変換
type: docs
weight: 10
url: /ja/python-net/convert-pdf-to-word/
lastmod: "2022-12-23"
description: Aspose.PDF for Python via .NETを使用して、PDFをMicrosoft Word形式に変換するPythonコードの書き方を学びます。また、PDFからDOC(DOCX)への変換を調整します。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 概要

この記事では、Pythonを使用して**PDFをMicrosoft Word文書に変換する方法**を説明します。以下のトピックをカバーします。

_フォーマット_: **DOC**
- [Python PDFからDOCへ](#python-pdf-to-doc)
- [Python PDFをDOCに変換](#python-pdf-to-doc)
- [Python PDFファイルをDOCに変換する方法](#python-pdf-to-doc)

_フォーマット_: **DOCX**
- [Python PDFからDOCXへ](#python-pdf-to-docx)
- [Python PDFをDOCXに変換](#python-pdf-to-docx)
- [Python PDFファイルをDOCXに変換する方法](#python-pdf-to-docx)

_フォーマット_: **Word**
- [Python PDFからWordへ](#python-pdf-to-docx)
- [Python PDFをWordに変換](#python-pdf-to-doc)

- [Python PDFファイルをWordに変換する方法](#python-pdf-to-docx)

## Python PDF to DOCおよびDOCX変換

最も人気のある機能の一つに、PDFからMicrosoft Word DOCへの変換があります。これにより、コンテンツ管理が容易になります。**Aspose.PDF for Python**を使用すると、PDFファイルをDOCだけでなく、DOCX形式にも簡単かつ効率的に変換できます。

## PDFをDOC (Word 97-2003)ファイルに変換

PDFファイルをDOC形式に簡単かつ完全にコントロールして変換します。Aspose.PDF for Pythonは柔軟で、多様な変換をサポートしています。たとえば、PDFドキュメントのページを画像に変換することは非常に人気のある機能です。

多くのお客様からのリクエストがある変換は、PDFからDOCへの変換です。PDFファイルをMicrosoft Wordドキュメントに変換します。お客様は、PDFファイルは簡単に編集できないのに対し、Wordドキュメントは編集可能であるため、これを望んでいます。一部の企業は、ユーザーがPDFから始まったファイル内のテキスト、テーブル、画像を操作できるようにしたいと考えています。

物事をシンプルで理解しやすくする伝統を守り、Aspose.PDF for Pythonは、ソースのPDFファイルをDOCファイルに2行のコードで変換することを可能にします。
 この機能を実現するために、SaveFormatという列挙型を導入しました。その値.Docを使用すると、ソースファイルをMicrosoft Word形式で保存できます。

以下のPythonコードスニペットは、PDFファイルをDOC形式に変換するプロセスを示しています。

<a name="csharp-pdf-to-doc"><strong>手順: PythonでPDFをDOCに変換する</strong></a>

1. ソースPDFドキュメントで[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)オブジェクトのインスタンスを作成します。
2. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)メソッドを呼び出して[SaveFormat](https://reference.aspose.com/pdf/python-net/aspose.pdf/saveformat/)形式で保存します。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_doc.doc"
    # PDFドキュメントを開く
    document = ap.Document(input_pdf)
    # ファイルをMS Wordドキュメント形式で保存する
    document.save(output_pdf, ap.SaveFormat.DOC)
```

### DocSaveOptionsクラスを使用する

[DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/)クラスは、PDFファイルをDOC形式に変換するプロセスを改善する多くのプロパティを提供します。 このプロパティの中で、ModeはPDFコンテンツの認識モードを指定することを可能にします。このプロパティには、RecognitionMode列挙から任意の値を指定することができます。これらの各値には、特定の利点と制限があります。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.doc"
    # PDFドキュメントを開く
    document = ap.Document(input_pdf)

    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC
    # 認識モードをFlowに設定
    save_options.mode = ap.DocSaveOptions.RecognitionMode.FLOW
    # 水平方向の近接を2.5に設定
    save_options.relative_horizontal_proximity = 2.5
    # 変換プロセス中に箇条書きを認識するように値を有効にする
    save_options.recognize_bullets = True

    # ファイルをMS Wordドキュメント形式で保存
    document.save(output_pdf, save_options)
```

{{% alert color="success" %}}
**PDFをDOCにオンラインで変換してみてください**

Aspose.PDF for Pythonは、オンライン無料アプリケーション["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)を提供しており、機能性や品質を試すことができます。
[![PDFをDOCに変換](/pdf/ja/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## PDFをDOCXに変換

Aspose.PDF for Python APIを使用すると、.NETを介してPythonでPDF文書を読み取り、DOCXに変換できます。DOCXはMicrosoft Word文書のよく知られた形式であり、その構造はプレーンバイナリからXMLとバイナリファイルの組み合わせに変更されました。DocxファイルはWord 2007およびそれ以降のバージョンで開くことができますが、DOCファイル拡張をサポートするMS Wordの以前のバージョンでは開くことができません。

次のPythonコードスニペットは、PDFファイルをDOCX形式に変換するプロセスを示しています。

<a name="csharp-pdf-to-docx"><strong>手順: PythonでPDFをDOCXに変換</strong></a>

1. ソースPDF文書を使用して[Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)オブジェクトのインスタンスを作成します。

2. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) メソッドを呼び出して、[SaveFormat](https://reference.aspose.com/pdf/python-net/aspose.pdf/saveformat/) 形式で保存します。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_docx_options.docx"
    # PDF ドキュメントを開く
    document = ap.Document(input_pdf)

    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    # 認識モードをフローとして設定
    save_options.mode = ap.DocSaveOptions.RecognitionMode.FLOW
    # 水平近接度を 2.5 に設定
    save_options.relative_horizontal_proximity = 2.5
    # 変換プロセス中に箇条書きを認識するように値を有効にする
    save_options.recognize_bullets = True

    # ファイルを MS Word ドキュメント形式で保存する
    document.save(output_pdf, save_options)
```

[DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) クラスには、結果のドキュメントの形式を指定する機能を提供する Format というプロパティがあります。つまり、DOC または DOCX です。
 PDFファイルをDOCX形式に変換するには、DocSaveOptions.DocFormat列挙型からDocx値を渡してください。

{{% alert color="warning" %}}
**PDFをDOCXにオンラインで変換を試みる**

Aspose.PDF for Pythonは、オンライン無料アプリケーション["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)を提供しており、機能や品質を試すことができます。

[![Aspose.PDF Convertion PDF to Word Free App](/pdf/ja/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## 関連項目

この記事では、以下のトピックについても説明しています。コードは上記と同じです。

_フォーマット_: **Word**
- [Python PDF to Word Code](#python-pdf-to-docx)
- [Python PDF to Word API](#python-pdf-to-docx)
- [Python PDF to Word Programmatically](#python-pdf-to-docx)
- [Python PDF to Word Library](#python-pdf-to-docx)
- [Python Save PDF as Word](#python-pdf-to-docx)
- [Python Generate Word from PDF](#python-pdf-to-docx)
- [Python Create Word from PDF](#python-pdf-to-docx)

- [Python PDF to Word Converter](#python-pdf-to-docx)
_Format_: **DOC**
- [Python PDFからDOCへのコード](#python-pdf-to-doc)
- [Python PDFからDOCへのAPI](#python-pdf-to-doc)
- [Python PDFからDOCへのプログラム](#python-pdf-to-doc)
- [Python PDFからDOCへのライブラリ](#python-pdf-to-doc)
- [Python PDFをDOCとして保存](#python-pdf-to-doc)
- [Python PDFからDOCを生成](#python-pdf-to-doc)
- [Python PDFからDOCを作成](#python-pdf-to-doc)
- [Python PDFからDOCへのコンバーター](#python-pdf-to-doc)

_Format_: **DOCX**
- [Python PDFからDOCXへのコード](#python-pdf-to-docx)
- [Python PDFからDOCXへのAPI](#python-pdf-to-docx)
- [Python PDFからDOCXへのプログラム](#python-pdf-to-docx)
- [Python PDFからDOCXへのライブラリ](#python-pdf-to-docx)
- [Python PDFをDOCXとして保存](#python-pdf-to-docx)
- [Python PDFからDOCXを生成](#python-pdf-to-docx)
- [Python PDFからDOCXを作成](#python-pdf-to-docx)
- [Python PDFからDOCXへのコンバーター](#python-pdf-to-docx)