---
title: PDFをMicrosoft PowerPointに変換する方法 C++
linktitle: PDFをPowerPointに変換する
type: docs
weight: 30
url: /cpp/convert-pdf-to-powerpoint/
description: Aspose.PDFを使用すると、C++でPDFをPowerPoint形式に変換できます。スライドを画像としてPDFをPPTXに変換することも可能です。
lastmod: "2021-11-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 概要

この記事では、C++を使用して**PDFをPowerPoint形式に変換する方法**を説明します。以下のトピックをカバーしています。

_形式_: **PPTX**
- [C++ PDFからPPTXへ](#cpp-pdf-to-pptx)
- [C++ PDFをPPTXに変換](#cpp-pdf-to-pptx)
- [C++ PDFファイルをPPTXに変換する方法](#cpp-pdf-to-pptx)

_形式_: **Microsoft PowerPoint PPTX形式**
- [C++ PDFからPowerPointへ](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDFをPowerPointに変換](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDFファイルをPowerPointに変換する方法](#cpp-pdf-to-powerpoint-pptx)

この記事でカバーされているその他のトピック。
- [関連項目](#see-also)

## C++ PDFからPowerPointへの変換

**Aspose.PDF for C++**を使用すると、PDFからPPTXへの変換の進行状況を追跡できます。

PDFを<abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>に変換する際、テキストは選択/更新可能なテキストとしてレンダリングされます。PDFファイルをPPTX形式に変換するために、Aspose.PDFは[`PptxSaveOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options)というクラスを提供しています。PptxSaveOptionsクラスのオブジェクトは、[`Document.Save(..) method`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa)メソッドの2番目の引数として渡されます。以下のコードスニペットは、PDFファイルをPPTX形式に変換するプロセスを示しています。

## Aspose.PDF for C++を使用したPDFからPPTXへの簡単な変換

PDFをPPTXに変換するために、Aspose.PDF for C++は以下のコード手順を使用することを推奨しています。

<a name="cpp-pdf-to-pptx" id="cpp-pdf-to-pptx"><strong>手順: C++でPDFをPPTXに変換する</strong></a> | <a name="cpp-pdf-to-powerpoint-pptx" id="cpp-pdf-to-powerpoint-pptx"><strong>手順: C++でPDFをPowerPoint PPTX形式に変換する</strong></a>

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) クラスのインスタンスを作成します。
2. [PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) クラスのインスタンスを作成します。
3. **Document** オブジェクトの **Save** メソッドを使用して _PDF を PPTX として保存_ します。

```cpp
void ConvertPDFtoPPTX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名のための文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // ファイル名のための文字列
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // PPTX形式で出力を保存
    document->Save(_dataDir + outfilename, SaveFormat::Pptx);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## スライドを画像として PDF を PPTX に変換

選択可能なテキストの代わりに画像として検索可能な PDF を PPTX に変換する必要がある場合、Aspose.PDF は [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) クラスを通じてそのような機能を提供します。 この目的を達成するには、[PptxSaveOptios](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) クラスの [SlidesAsImages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options#aeca0659ae24ea7cdeb171d941440dcb2) プロパティを 'true' に設定します。以下のコードサンプルを参照してください。

```cpp
void ConvertPDFtoPPTX_SlidesAsImages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名の文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // ファイル名の文字列
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto pptxOptions = MakeObject<PptxSaveOptions>();
    pptxOptions->set_SlidesAsImages(true);

    // 出力をPPTX形式で保存
    document->Save(_dataDir + outfilename, pptxOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## PPTX変換の進捗詳細

Aspose.PDF for C++ は、PDFからPPTXへの変換の進捗を追跡できます。 [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options) クラスは、変換の進捗を追跡するためのカスタムメソッドを指定できる [CustomProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pptx_save_options#ac9ad606c4b4d7249c5f299fd8d766474) プロパティを提供します。以下のコードサンプルに示されています。

```cpp
void ConvertPDFtoPPTX_ProgressDetailConversion()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名の文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // ファイル名の文字列
    String infilename("JSON Fundamenals.pdf");
    String outfilename("JSON Fundamenals.pptx");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto pptxOptions = MakeObject<PptxSaveOptions>();
    //pptxOptions->set_SlidesAsImages(true);
    //カスタム進捗ハンドラを指定
    pptxOptions->set_CustomProgressHandler(ShowProgressOnConsole);

    // 出力をPPTX形式で保存
    document->Save(_dataDir + outfilename, pptxOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
以下は、進捗の変換を表示するためのカスタムメソッドです。

```cpp
void ShowProgressOnConsole(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo> eventInfo)
{
    switch (eventInfo->EventType)
    {
    case ProgressEventType::TotalProgress:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - 変換の進捗 : " << eventInfo->Value << std::endl;
    break;
    case ProgressEventType::ResultPageCreated:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - 結果ページの " << eventInfo->Value << " / " << eventInfo->MaxValue << " レイアウトが作成されました。" << std::endl;
    break;
    case ProgressEventType::ResultPageSaved:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - 結果ページの " << eventInfo->Value << " / " << eventInfo->MaxValue << " がエクスポートされました。" << std::endl;
    break;
    case ProgressEventType::SourcePageAnalysed:
    std::clog << DateTime::get_Now().get_TimeOfDay() << " - ソースページ " << eventInfo->Value << " / " << eventInfo->MaxValue << " が分析されました。" << std::endl;
    break;
    default:
    break;
    }
}
```

{{% alert color="success" %}}
**PDFをオンラインでPowerPointに変換してみる**

Aspose.PDF for C++は、無料のオンラインアプリケーション["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)を提供しており、その機能と品質を調査することができます。

[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## 関連項目

この記事では、以下のトピックも扱っています。コードは上記と同じです。

_フォーマット_: **PowerPoint**
- [C++ PDFからPowerPointへのコード](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDFからPowerPointへのAPI](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDFからPowerPointへのプログラム](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDFからPowerPointへのライブラリ](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDFをPowerPointとして保存](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDFからPowerPointを生成](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDFからPowerPointを作成](#cpp-pdf-to-powerpoint-pptx)

- [C++ PDFからPowerPointへのコンバーター](#cpp-pdf-to-powerpoint-pptx)

_Format_: **Microsoft PowerPoint PPTX 形式**
- [C++ PDF から PowerPoint PPTX へのコード](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF から PowerPoint PPTX への API](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF から PowerPoint PPTX へのプログラム](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF から PowerPoint PPTX へのライブラリ](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF を PowerPoint PPTX として保存](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF から PowerPoint PPTX を生成](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF から PowerPoint PPTX を作成](#cpp-pdf-to-powerpoint-pptx)
- [C++ PDF から PowerPoint PPTX へのコンバータ](#cpp-pdf-to-powerpoint-pptx)

_Format_: **PPTX**
- [C++ PDF から PPTX へのコード](#cpp-pdf-to-pptx)
- [C++ PDF から PPTX への API](#cpp-pdf-to-pptx)
- [C++ PDF から PPTX へのプログラム](#cpp-pdf-to-pptx)
- [C++ PDF から PPTX へのライブラリ](#cpp-pdf-to-pptx)
- [C++ PDF を PPTX として保存](#cpp-pdf-to-pptx)
- [C++ PDF から PPTX を生成](#cpp-pdf-to-pptx)
- [C++ PDF から PPTX を作成](#cpp-pdf-to-pptx)
- [C++ PDF から PPTX へのコンバータ](#cpp-pdf-to-pptx)