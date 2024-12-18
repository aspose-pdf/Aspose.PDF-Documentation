---
title: PDFをMicrosoft Word文書に変換するC++
linktitle: PDFをWordに変換
type: docs
weight: 10
url: /ja/cpp/convert-pdf-to-word/
lastmod: "2021-11-19"
description: Aspose.PDF for C++ライブラリを使用すると、C++でPDFをWord形式に簡単にかつ完全に制御して変換できます。これらの形式にはDOCとDOCXが含まれます。PDFをMicrosoft Word文書に変換する方法を詳しく学びましょう。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 概要

この記事では、C++を使用してPDFをMicrosoft Word文書に変換する方法を説明します。これらのトピックをカバーしています。

_フォーマット_: **DOC**
- [C++ PDFをDOCに](#cpp-pdf-to-doc)
- [C++ PDFをDOCに変換](#cpp-pdf-to-doc)
- [C++ PDFファイルをDOCに変換する方法](#cpp-pdf-to-doc)

_フォーマット_: **DOCX**
- [C++ PDFをDOCXに](#cpp-pdf-to-docx)
- [C++ PDFをDOCXに変換](#cpp-pdf-to-docx)
- [C++ PDFファイルをDOCXに変換する方法](#cpp-pdf-to-docx)

_フォーマット_: **Microsoft Word DOC形式**
- [C++ PDFをWordに](#cpp-pdf-to-word-doc)
- [C++ PDFをWordに変換](#cpp-pdf-to-word-doc)

- [C++ PDFファイルをWordに変換する方法](#cpp-pdf-to-word-doc)

_Format_: **Microsoft Word DOCX 形式**
- [C++ PDF から Word へ](#cpp-pdf-to-word-docx)
- [C++ PDF を Word に変換](#cpp-pdf-to-word-docx)
- [C++ PDF ファイルを Word に変換する方法](#cpp-pdf-to-word-docx)

この記事で取り上げるその他のトピック
- [参照](#see-also)

## C++ PDF から Word への変換

最も人気のある機能の1つは、PDF を Microsoft Word DOC に変換することで、コンテンツを簡単に操作できるようになります。Aspose.PDF for C++ は、PDF ファイルを DOC に変換することができます。

## PDF を DOC (Word 97-2003) ファイルに変換

PDF ファイルを簡単かつ完全に制御して DOC 形式に変換します。Aspose.PDF for C++ は柔軟で、さまざまな変換をサポートしています。例えば、PDF ドキュメントのページを画像に変換することは非常に人気のある機能です。

多くのお客様からリクエストされている変換は、PDF から DOC への変換です。PDF ファイルを Microsoft Word ドキュメントに変換します。 顧客はPDFファイルが簡単に編集できないのに対し、Word文書は編集可能であるため、これを望んでいます。一部の企業は、ユーザーがPDFとして開始されたファイル内のテキスト、表、画像を操作できるようにしたいと考えています。

物事を簡単で理解しやすくする伝統を守り、Aspose.PDF for C++では、2行のコードでソースPDFファイルをDOCファイルに変換することができます。この機能を実現するために、SaveFormatという列挙型を導入しており、その値.Docを用いることで、ソースファイルをMicrosoft Word形式に保存できます。

以下のC++コードスニペットは、PDFファイルをDOC形式に変換するプロセスを示しています。

<a name="cpp-pdf-to-doc" id="cpp-pdf-to-doc"><strong>ステップ: C++でPDFをDOCに変換</strong></a> | <a name="cpp-pdf-to-word-doc" id="cpp-pdf-to-word-doc"><strong>ステップ: C++でPDFをMicrosoft Word DOC形式に変換</strong></a>

1. ソースPDFドキュメントを使用して[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)オブジェクトのインスタンスを作成します。
2. ドキュメントを **Document->Save()** メソッドを呼び出して **SaveFormat::Doc** 形式で保存します。

```cpp
void ConvertPDFtoWord()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名のための文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // ファイル名のための文字列
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.doc");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
        // ファイルをMSドキュメント形式で保存
        document->Save(_dataDir + outfilename, SaveFormat::Doc);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```

次のコードスニペットは、PDFファイルをDOCアドバンストバージョンに変換するプロセスを示しています:

```cpp
void ConvertPDFtoWordDocAdvanced()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名のための文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // ファイル名のための文字列
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.doc");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto saveOptions = MakeObject<DocSaveOptions>();
    saveOptions->set_Format(DocSaveOptions::DocFormat::Doc);
    // 認識モードをFlowに設定
    saveOptions->set_Mode(DocSaveOptions::RecognitionMode::Flow);
    // 水平近接を2.5に設定
    saveOptions->set_RelativeHorizontalProximity(2.5f);
    // 変換プロセス中に箇条書きを認識するように値を有効にする
    saveOptions->set_RecognizeBullets(true);

    try {
        // ファイルをMSドキュメント形式で保存
        document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```
{{% alert color="success" %}}
**PDFをDOCにオンラインで変換してみてください**

Aspose.PDF for C++はオンラインの無料アプリケーション["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)を提供しており、そこで機能と品質を調査することができます。

[![PDFをDOCに変換](pdf_to_doc.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## PDFをDOCXに変換

Aspose.PDF for C++ APIを使用すると、C++言語を使用してPDFドキュメントをDOCXに読み取り変換できます。DOCXはMicrosoft Wordドキュメントのよく知られた形式で、その構造はプレーンバイナリからXMLとバイナリファイルの組み合わせに変更されました。DocxファイルはWord 2007およびそれ以降のバージョンで開くことができますが、DOCファイル拡張子をサポートするMS Wordの以前のバージョンでは開くことができません。

以下のC++コードスニペットは、PDFファイルをDOCX形式に変換するプロセスを示しています。

<a name="cpp-pdf-to-docx" id="cpp-pdf-to-docx"><strong>ステップ: C++でPDFをDOCXに変換</strong></a> | <a name="cpp-pdf-to-word-docx" id="cpp-pdf-to-word-docx"><strong>ステップ: C++でPDFをMicrosoft Word DOCX形式に変換</strong></a>

1. ソースPDFドキュメントで[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)オブジェクトのインスタンスを作成します。
2. **Document->Save()**メソッドを呼び出して、**SaveFormat::DocX**形式で保存します。

```cpp
void ConvertPDFtoWord_DOCX_Format()
{
    std::clog << __func__ << ": 開始" << std::endl;
    // パス名のための文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // ファイル名のための文字列
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.docx");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
        // ファイルをMSドキュメント形式で保存する
        document->Save(_dataDir + outfilename, SaveFormat::DocX);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": 終了" << std::endl;
}
```

[`DocSaveOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options)クラスには、結果のドキュメントの形式、つまりDOCまたはDOCXを指定する機能を提供するFormatというプロパティがあります。 In order to convert a PDF file to DOCX format, please pass the Docx value from the DocSaveOptions.DocFormat enumeration.

PDFファイルをDOCX形式に変換するには、DocSaveOptions.DocFormat列挙からDocx値を渡してください。

Please take a look over the following code snippet which provides the capability to convert PDF file to DOCX format with C++.

以下のコードスニペットをご覧ください。これは、C++でPDFファイルをDOCX形式に変換する機能を提供します。

```cpp
void ConvertPDFtoWord_Advanced_DOCX_Format()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for file name
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.docx");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto saveOptions = MakeObject<DocSaveOptions>();
    saveOptions->set_Format(DocSaveOptions::DocFormat::DocX);

    // Set other DocSaveOptions params
    // ...

    // Save the file into MS document format

    try {
        // Save the file into MS document format
        document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```
{{% alert color="warning" %}}
**PDFをDOCXにオンラインで変換してみてください**

Aspose.PDF for C++は、オンラインで無料のアプリケーション["PDF to DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx)を提供しており、その機能と品質を試すことができます。

[![Aspose.PDF Convertion PDF to Word Free App](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## 関連情報

この記事では、これらのトピックもカバーしています。コードは上記と同じです。

_フォーマット_: **Microsoft Word DOC形式**
- [C++ PDF to Word Code](#cpp-pdf-to-word-doc)
- [C++ PDF to Word API](#cpp-pdf-to-word-doc)
- [C++ PDF to Word Programmatically](#cpp-pdf-to-word-doc)
- [C++ PDF to Word Library](#cpp-pdf-to-word-doc)
- [C++ Save PDF as Word](#cpp-pdf-to-word-doc)
- [C++ Generate Word from PDF](#cpp-pdf-to-word-doc)
- [C++ Create Word from PDF](#cpp-pdf-to-word-doc)
- [C++ PDF to Word Converter](#cpp-pdf-to-word-doc)

_フォーマット_: **Microsoft Word DOCX形式**

- [C++ PDF to Word Code](#cpp-pdf-to-word-docx)
- [C++ PDF to Word API](#cpp-pdf-to-word-docx)  
- [C++ PDF to Word Programmatically](#cpp-pdf-to-word-docx)  
- [C++ PDF to Word Library](#cpp-pdf-to-word-docx)  
- [C++ Save PDF as Word](#cpp-pdf-to-word-docx)  
- [C++ Generate Word from PDF](#cpp-pdf-to-word-docx)  
- [C++ Create Word from PDF](#cpp-pdf-to-word-docx)  
- [C++ PDF to Word Converter](#cpp-pdf-to-word-docx)  

_フォーマット_: **DOC**  
- [C++ PDF to DOC Code](#cpp-pdf-to-doc)  
- [C++ PDF to DOC API](#cpp-pdf-to-doc)  
- [C++ PDF to DOC Programmatically](#cpp-pdf-to-doc)  
- [C++ PDF to DOC Library](#cpp-pdf-to-doc)  
- [C++ Save PDF as DOC](#cpp-pdf-to-doc)  
- [C++ Generate DOC from PDF](#cpp-pdf-to-doc)  
- [C++ Create DOC from PDF](#cpp-pdf-to-doc)  
- [C++ PDF to DOC Converter](#cpp-pdf-to-doc)  

_フォーマット_: **DOC**  
- [C++ PDF to DOCX Code](#cpp-pdf-to-docx)  
- [C++ PDF to DOCX API](#cpp-pdf-to-docx)  
- [C++ PDF to DOCX Programmatically](#cpp-pdf-to-docx)  
- [C++ PDF to DOCX Library](#cpp-pdf-to-docx)  
- [C++ Save PDF as DOCX](#cpp-pdf-to-docx)  

- [C++ Generate DOCX from PDF](#cpp-pdf-to-docx)  
```
- [C++ から DOCX を PDF から作成](#cpp-pdf-to-docx)
- [C++ PDF から DOCX へのコンバーター](#cpp-pdf-to-docx)
```