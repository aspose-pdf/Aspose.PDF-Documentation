---
linktitle: 他のファイル形式をPDFに変換する
type: docs
weight: 80
url: ja/cpp/convert-other-files-to-pdf/
lastmod: "2021-11-19"
description: このトピックは、Aspose.PDFが他のファイル形式をPDFドキュメントに変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## EPUBをPDFに変換する

**Aspose.PDF for C++** は、EPUBファイルをPDF形式に簡単に変換することができます。

<abbr title="電子出版">EPUB</abbr>（電子出版の略）は、国際デジタル出版フォーラム（IDPF）による無料でオープンな電子書籍標準です。ファイルは.epub拡張子を持ちます。EPUBはリフロー可能なコンテンツ用に設計されており、EPUBリーダーが特定の表示デバイスに合わせてテキストを最適化できます。

EPUBは固定レイアウトのコンテンツもサポートしています。 フォーマットは、出版社やコンバージョンハウスが社内で使用するだけでなく、配布や販売のためにも使用できる単一のフォーマットとして意図されています。これはOpen eBook標準に取って代わります。EPUB 3バージョンは、標準化されたベストプラクティス、研究、情報、イベントのための主要な書籍取引協会であるBook Industry Study Group（BISG）によっても承認されています。

変換手順：

1. パス名とファイル名のために[Stringクラス](https://reference.aspose.com/pdf/cpp/class/system.string)を作成します。
1. [EpubLoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options)クラスのインスタンスを作成します。
1. ソースファイル名とオプションを指定して[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)クラスのインスタンスを作成します。
1. 入力ファイルをロードして[保存](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa)します。

次のコードスニペットは、C++でEPUBファイルをPDF形式に変換する方法を示しています。

```cpp
void ConvertEPUBtoPDF()
{
    std::clog << "EPUB to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("aliceDynamic.epub");
    String outfilename("epub_test.pdf");
    auto options = MakeObject<EpubLoadOptions>();
    try {
    auto document = MakeObject<Document>(_dataDir + infilename, options);
    document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << "EPUB to PDF convert: End" << std::endl;
}
```
{{% alert color="success" %}}
**EPUB を PDF にオンラインで変換してみる**

Aspose.PDF for C++ は、オンラインで無料のアプリケーション ["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf) を提供しています。ここで、その機能と品質を試してみることができます。

[![Aspose.PDF Convertion EPUB to PDF with Free App](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## テキストを PDF に変換

**Aspose.PDF for C++** はプレーンテキストや事前にフォーマットされたテキストファイルを PDF フォーマットに変換する機能をサポートしています。

テキストを PDF に変換するということは、テキストフラグメントを PDF ページに追加することを意味します。テキストファイルに関しては、事前フォーマットされたテキスト（例えば、1行に80文字の25行）とフォーマットされていないテキスト（プレーンテキスト）の2種類のテキストを扱います。私たちのニーズに応じて、この追加を自分で制御するか、ライブラリのアルゴリズムに任せることができます。

### プレーンテキストファイルを PDF に変換

プレーンテキストファイルの場合、次の方法を使用できます：

1. Create a [String Class](https://reference.aspose.com/pdf/cpp/class/system.string) for path name and file name.
1. [TextReader](https://reference.aspose.com/pdf/cpp/class/system.i_o.text_reader/.) を使用してソーステキストファイルを読み込みます。
1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) オブジェクトをインスタンス化します。
1. ドキュメントのページコレクションに [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) を追加します。
1. TextFragment の新しいオブジェクトを作成し、TextReader オブジェクトをそのコンストラクタに渡します。
1. 段落コレクションに新しいテキスト段落を追加し、TextFragment オブジェクトを渡します。
1. 入力ファイルを読み込み、[Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) します。

```cpp
void ConvertTextToPDF()
{
    std::clog << "Text to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.txt");
    String outfilename("TextToPDF.pdf");

    // Read the source text file
    String content = System::IO::File::ReadAllText(_dataDir + infilename);

    // Instantiate a Document object by calling its empty constructor
    auto document = MakeObject<Document>();

    // Add a new page in Pages collection of Document
    auto page = document->get_Pages()->Add();

    // Create an instance of TextFragmet and pass the text from reader object to its constructor as argument
    auto text = MakeObject<TextFragment>(content);

    // Add a new text paragraph in paragraphs collection and pass the TextFragment object
    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // Save resultant PDF file
    document->Save(_dataDir + outfilename);
    std::clog << "Text to PDF convert: End" << std::endl;
}
```
### プレフォーマットされたテキストファイルをPDFに変換

プレフォーマットされたテキストの変換は、プレーンテキストに似ていますが、マージン、フォントの種類とサイズの設定など、いくつかの追加のアクションを実行する必要があります。明らかに、そのフォントは等幅フォント（例えばCourier New）であるべきです。

C++でプレフォーマットされたテキストをPDFに変換するために、次の手順に従います：

1. 空のコンストラクタを呼び出してDocumentオブジェクトをインスタンス化します。
1. より良いプレゼンテーションのために左と右のマージンを設定します。
1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)オブジェクトをインスタンス化し、Pagesコレクションに新しいページを追加します。
1. 入力画像ファイルを読み込み、[保存](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa)します。

{{% alert color="success" %}}
**オンラインでTEXTをPDFに変換してみてください**

Aspose.PDF for C++は、オンラインの無料アプリケーション["Text to PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf)を提供しており、その機能と品質を試すことができます。

[![Aspose.PDF Convertion TEXT to PDF with Free App](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

## XPSをPDFに変換

**Aspose.PDF for C++**は<abbr title="XML Paper Specification">XPS</abbr>ファイルをPDF形式に変換する機能をサポートしています。この記事をチェックして、タスクを解決してください。

XPSファイルタイプは、主にMicrosoft CorporationによるXML Paper Specificationに関連付けられています。XML Paper Specification (XPS)は、かつてMetroのコードネームを持ち、次世代プリントパス (NGPP) マーケティングコンセプトを包含していたもので、Microsoftがドキュメント作成と表示をWindowsオペレーティングシステムに統合するための取り組みです。

{{% alert color="primary" %}}

このファイル形式は基本的に圧縮されたXMLファイルで、主に配布と保管に使用されます。 編集するのが非常に難しく、主にMicrosoftによって実装されています。

{{% /alert %}}

Aspose.PDF for C++を使用してXPSをPDFに変換するために、[XpsLoadOption](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options)というクラスを導入しました。このクラスは[LoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options)オブジェクトを初期化するために使用されます。その後、このオブジェクトはDocumentオブジェクトの初期化時に引数として渡され、PDFレンダリングエンジンがソースドキュメントの入力形式を判断するのに役立ちます。

以下のコードスニペットは、C++でXPSファイルをPDF形式に変換するプロセスを示しています。

```cpp
void ConvertXPStoPDF()
{
    std::clog << "XPS to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.oxps");
    String outfilename("XPStoPDF.pdf");
    auto options = MakeObject<XpsLoadOptions>();
    try {
        auto document = MakeObject<Document>(_dataDir + infilename, options);
        document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
        std::cerr << ex->get_Message() << std::endl;
    };
    std::clog << "XPS to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**XPS形式をPDFにオンラインで変換してみてください**

Aspose.PDF for C++は、オンラインで無料アプリケーション["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/)を提供しており、その機能と動作の品質を調査することができます。

[![Aspose.PDF Convertion XPS to PDF with Free App](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## XMLをPDFに変換

XML形式は構造化データを保存するために使用されます。Aspose.PDFでは、<abbr title="Extensible Markup Language">XML</abbr>をPDFに変換するいくつかの方法があります。

## XSL-FOをPDFに変換

1. パス名とファイル名のための[String Class](https://reference.aspose.com/pdf/cpp/class/system.string)を作成します。
1. [XslFoLoadOption object](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options)をインスタンス化します。
1. エラーハンドリング戦略を設定します。
1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)オブジェクトをインスタンス化します。
1. [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) 入力画像ファイル。

```cpp
void Convert_XSLFO_to_PDF()
{
    std::clog << "XSL-FO to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilenameXSL("c:\\samples\\employees.xslt");
    String infilenameXML("c:\\samples\\employees.xml");

     String outfilename("XMLFOtoPDF.pdf");
    // XslFoLoadOptionオブジェクトをインスタンス化
    auto options = new XslFoLoadOptions(infilenameXSL);
    // エラーハンドリング戦略を設定
    options->ParsingErrorsHandlingType = XslFoLoadOptions::ParsingErrorsHandlingTypes::ThrowExceptionImmediately;
    // Documentオブジェクトを作成
    auto document = MakeObject<Document>(infilenameXML, options);
    document->Save(_dataDir + outfilename);
}
```

{{% alert color="success" %}}
**XMLをPDFにオンラインで変換してみる**

Aspose.PDF for C++は、オンラインの無料アプリケーション["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf)を提供しており、機能性と品質を調査することができます。
```
[![Aspose.PDF Convertion XML to PDF with Free App](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}
```