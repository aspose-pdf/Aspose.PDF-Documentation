---
title: C++を使用してPDFドキュメントを保存する
linktitle: 保存
type: docs
weight: 30
url: /cpp/save-pdf-document/
description: Aspose.PDF for C++ライブラリを使用してPDFファイルを保存する方法を学びます。
lastmod: "2021-11-01"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## PDFドキュメントをファイルシステムに保存する

[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) クラスのSaveメソッドを使用して、作成または操作したPDFドキュメントをファイルシステムに保存できます。

```cpp
void SaveDocument()
{
    // パス名のための文字列
    String _dataDir("C:\\Samples\\");

    String originalFileName("SimpleResume.pdf");
    String modifiedFileName("SimpleResumeModified.pdf");

    auto document = MakeObject<Document>(_dataDir + originalFileName);
    // 一部の操作を行う、例: 新しい空のページを追加
    document->get_Pages()->Add();
    document->Save(_dataDir + modifiedFileName);
}
```

## PDFドキュメントをストリームに保存する

Saveメソッドのオーバーロードを使用して、作成または操作したPDFドキュメントをストリームに保存することもできます。

```cpp
void SaveDocumentStream()
{
    // パス名のための文字列
    String _dataDir("C:\\Samples\\");

    String originalFileName("SimpleResume.pdf");
    String modifiedFileName("SimpleResumeModified.pdf");

    auto document = MakeObject<Document>(_dataDir + originalFileName);

    // 一部の操作を行う、例: 新しい空のページを追加
    document->get_Pages()->Add();

    auto fileStream = System::IO::File::OpenWrite(_dataDir + modifiedFileName);
    document->Save(fileStream);
}
```

## PDF/A または PDF/X 形式で保存する

PDF/A は、電子文書のアーカイブと長期保存に使用するための、ポータブルドキュメントフォーマット（PDF）の ISO 標準化バージョンです。  
PDF/A は、フォントのリンク（フォントの埋め込みとは対照的）や暗号化など、長期のアーカイブに適さない機能を禁止している点で、PDF と異なります。PDF/A ビューアの ISO 要件には、カラーマネジメントのガイドライン、埋め込みフォントのサポート、および埋め込まれた注釈を読み取るためのユーザーインターフェースが含まれます。

PDF/X は、PDF ISO 標準のサブセットです。PDF/X の目的は、グラフィックス交換を容易にすることです。したがって、標準の PDF ファイルには適用されない印刷関連の一連の要件があります。

いずれの場合も、ドキュメントを保存するために Save メソッドが使用されますが、ドキュメントは [PdfFormatConversionOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pdf_format_conversion_options) を使用して準備する必要があります。

```cpp
void SaveDocumentAsPDFx()
{
    // パス名のための文字列
    String _dataDir("C:\\Samples\\");

    // ファイル名のための文字列
    String infilename("SimpleResume.pdf");
    String outfilename("SimpleResume_A3U.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);
    auto options = new PdfFormatConversionOptions(Aspose::Pdf::PdfFormat::PDF_A_3U);
    try
    {
        document->Convert(options);
    }
    catch (const std::exception& e)
    {
        std::cerr << e.what();
    }

    document->Save(_dataDir + outfilename);
}
```