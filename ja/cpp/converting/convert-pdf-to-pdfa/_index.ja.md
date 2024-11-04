```
---
title: PDFをPDF/A形式に変換
linktitle: PDFをPDF/A形式に変換
type: docs
weight: 100
url: /cpp/convert-pdf-to-pdfa/
lastmod: "2021-11-01"
description: このトピックでは、Aspose.PDFを使用してPDFファイルをPDF/A準拠のPDFファイルに変換する方法を紹介します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for C++** を使用すると、PDFファイルを<abbr title="Portable Document Format / A">PDF/A</abbr>準拠のPDFファイルに変換できます。その前に、ファイルを検証する必要があります。このトピックではその方法を説明します。

{{% alert color="primary" %}}

PDF/Aの準拠性を検証するためにAdobe Preflightを使用しています。市場に出回っているすべてのツールは、それぞれのPDF/A準拠の「表現」を持っています。PDF/A検証ツールに関するこの記事を参考にしてください。Aspose.PDFがPDFファイルをどのように生成するかの検証にAdobe製品を選んだのは、AdobeがPDFに関連するすべての中心に位置しているためです。

{{% /alert %}}

DocumentクラスのConvertメソッドを使用してファイルを変換します。
``` PDFをPDF/A準拠ファイルに変換する前に、Validateメソッドを使用してPDFを検証します。検証結果はXMLファイルに保存され、この結果はConvertメソッドにも渡されます。また、ConvertErrorAction列挙を使用して変換できない要素に対するアクションを指定することもできます。
## PDFファイルをPDF/A-1bに変換する

以下のコードスニペットは、PDFファイルをPDF/A-1b準拠のPDFに変換する方法を示しています。

```cpp
void ConverttoPDFA_1b()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名の文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // 入力ファイル名の文字列
    String infilename("sample.pdf");
    // ログファイル名の文字列
    String logfilename("log.xml");
    // 入力ファイル名の文字列
    String outfilename("PDFToPDFA_out.pdf");

    // ドキュメントを開く
    auto document = new Document(_dataDir + infilename);

    // PDF/A準拠のドキュメントに変換する
    // 変換プロセス中に、検証も実行されます
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_1B, ConvertErrorAction::Delete);

    // 出力ドキュメントを保存する
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
ドキュメントの検証のみを実行するには、次のコード行を使用します。

```cpp
void ConverttoPDFA_1b_Validation()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名のための文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // 入力ファイル名のための文字列
    String infilename("sample.pdf");
    // ログファイル名のための文字列
    String logfilename("log.xml");

    // ドキュメントを開く
    auto document = new Document(_dataDir + infilename);

    // PDF/Aに準拠したドキュメントに変換
    // 変換プロセス中に検証も実行されます
    document->Validate(_dataDir + logfilename, PdfFormat::PDF_A_1B);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDFファイルをPDF/A-3bに変換

Aspose.PDF for C++は、PDFファイルをPDF/A-3b形式に変換する機能もサポートしています。

```cpp
void ConverttoPDFA_3b()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名のための文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // 入力ファイル名のための文字列
    String infilename("sample.pdf");
    // ログファイル名のための文字列
    String logfilename("log.xml");
    // 出力ファイル名のための文字列
    String outfilename("PDFToPDFA3b_out.pdf");

    // ドキュメントを開く
    auto document = new Document(_dataDir + infilename);

    // PDF/Aに準拠したドキュメントに変換
    // 変換プロセス中に検証も実行されます
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_3B, ConvertErrorAction::Delete);

    // 出力ドキュメントを保存
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDFファイルをPDF/A-2uに変換

Aspose.PDF for C++は、PDFファイルをPDF/A-2u形式に変換する機能もサポートしています。

```cpp
void ConverttoPDFA_2u()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名のための文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // 入力ファイル名のための文字列
    String infilename("sample.pdf");
    // ログファイル名のための文字列
    String logfilename("log.xml");
    // 入力ファイル名のための文字列
    String outfilename("PDFToPDFA3b_out.pdf");

    // ドキュメントを開く
    auto document = new Document(_dataDir + infilename);

    // PDF/A準拠のドキュメントに変換
    // 変換プロセス中に、検証も実行されます
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_2U, ConvertErrorAction::Delete);

    // 出力ドキュメントを保存
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDFファイルをPDF/A-3uに変換

Aspose.PDF for C++は、PDFファイルをPDF/A-3u形式に変換する機能もサポートしています。

```cpp
void ConverttoPDFA_3u()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名のための文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // 入力ファイル名のための文字列
    String infilename("sample.pdf");
    // ログファイル名のための文字列
    String logfilename("log.xml");
    // 出力ファイル名のための文字列
    String outfilename("PDFToPDFA3b_out.pdf");

    // ドキュメントを開く
    auto document = new Document(_dataDir + infilename);

    // PDF/A準拠のドキュメントに変換
    // 変換プロセス中に検証も行われます
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_2U, ConvertErrorAction::Delete);

    // 出力ドキュメントを保存
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PDF/Aファイルに添付ファイルを追加

PDF/A準拠形式にファイルを添付する必要がある場合は、Aspose.PDF.PdfFormat列挙体のPDF_A_3A値を使用することをお勧めします。

PDF/A_3aは、PDF/A準拠ファイルに任意のファイル形式を添付ファイルとして添付する機能を提供する形式です。

```cpp
void ConverttoPDFA_AddAttachment()
{
    std::clog << __func__ << ": 開始" << std::endl;
    // パス名のための文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // 入力ファイル名のための文字列
    String infilename("sample.pdf");
    // ログファイル名のための文字列
    String logfilename("log.xml");
    // 入力ファイル名のための文字列
    String outfilename("PDFToPDFA3b_out.pdf");

    // ドキュメントを開く
    auto document = new Document(_dataDir + infilename);

    // 添付ファイルとして追加する新しいファイルを設定
    auto fileSpecification = MakeObject<FileSpecification>(_dataDir + String("aspose-logo.jpg"), String("大型画像ファイル"));
    // ドキュメントの添付ファイルコレクションに添付を追加
    document->get_EmbeddedFiles()->Add(fileSpecification);

    // PDF/A準拠のドキュメントに変換
    // 変換プロセス中に検証も実行される
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_3A, ConvertErrorAction::Delete);

    // 出力ドキュメントを保存
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": 終了" << std::endl;
}
```

## 欠落フォントを代替フォントに置き換える

PDFA 標準によれば、フォントは PDFA ドキュメントに埋め込まれている必要があります。しかし、フォントがソースドキュメントに埋め込まれていない場合や、マシン上に存在しない場合、PDFA は検証に失敗します。この場合、マシン上のいくつかの代替フォントで欠落フォントを代用する必要があります。PDF から PDFA への変換中に、SimpleFontSubsituation メソッドを使用して欠落フォントを代用できます。

{{% alert color="primary" %}}
**PDFをPDF/Aにオンラインで変換してみてください**

Aspose.PDF for C++は、無料のオンラインアプリケーション["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF Convertion PDF to PDF/A with Free App](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}