---
title: PDFドキュメントを作成する
linktitle: PDFを作成
type: docs
weight: 10
url: /ja/cpp/create-pdf-document/
description: この記事では、Aspose.PDF for C++を使用してPDFドキュメントを作成およびフォーマットする方法について説明します。
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

私たちは常に、C++プロジェクトでPDFドキュメントを生成し、それらをより正確かつ効果的に操作する方法を探しています。ライブラリの使いやすい機能を利用することで、仕事の多くを追跡し、C++でPDFを生成しようとする時間のかかる詳細にあまり注意を払わずに済むようになります。

## C++を使用してPDFを生成する

Aspose.PDF for C++ APIを使用すると、C++を使用してPDFファイルを作成および読み取ることができます。このAPIは、WinFormsなどを含むさまざまなC++アプリケーションで使用できます。この記事では、Aspose.PDF for C++ APIを使用して、C++アプリケーションでPDFファイルを簡単に生成および読み取る方法を紹介します。

### シンプルなPDFファイルを作成する方法

C++を使用してPDFファイルを作成するには、以下の手順を使用できます。

1. オブジェクトを作成する[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)クラス
1. [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)オブジェクトをDocumentオブジェクトの'Pages'コレクションに追加する
1. [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/)をページの[Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs)コレクションに追加する
1. 結果として得られるPDFドキュメントを保存する

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void CreateDocument() {
    // パス名のための文字列。
    String _dataDir("C:\\Samples\\");

    // ファイル名のための文字列。
    String outputFileName("HelloWorld_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // 新しいページにテキストを追加
    auto text = MakeObject<TextFragment>(u"Hello world!");

    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // 更新されたPDFを保存
    document->Save(_dataDir + outputFileName);
}
```
## 検索可能なPDFドキュメントを作成する

Aspose.PDF for C++を使用すると、ゼロからPDFを作成したり、既存のPDFを操作したりできます。PDFにテキスト要素を追加すると、生成されたPDFは検索可能になります。ただし、テキストを含む画像をPDFファイルに変換すると、PDF内のコンテンツは検索可能ではありません。しかし、回避策として、生成されたファイルにOCRを使用して検索可能にすることができます。したがって、最初にシステムにTesseract-OCRをインストールする必要があり、tesseractコンソールアプリケーションを持つことになります。

以下は、この要件を達成するための完全なコードです：

```cpp
void CreateSearchableDocument() {
    // パス名のための文字列。
    String _dataDir("C:\\Samples\\");
    // ファイル名のための文字列。
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);
    bool convertResult = false;
    try
    {
        convertResult = document->Convert(CallBackGetHocr);
    }
    catch (Exception ex)
    {
        std::cerr << ex->get_Message() << std::endl;
    }
    document->Dispose();
}

static String CallBackGetHocr(System::SharedPtr<System::Drawing::Image> img)
{
    String tmpFile = System::IO::Path::GetTempFileNameSafe();

    auto bmp = MakeObject<System::Drawing::Bitmap>(img);

    bmp->Save(tmpFile, System::Drawing::Imaging::ImageFormat::get_Bmp());
    String inputFile = String::Format(u"\"{0}\"", tmpFile);
    String outputFile = String::Format(u"\"{0}\"", tmpFile);
    String arguments = inputFile + u" " + outputFile + u" -l eng hocr";
    String tesseractProcessName = u"C:\\Program Files\\Tesseract-OCR\\Tesseract.exe";

    auto psi = MakeObject<System::Diagnostics::ProcessStartInfo>(tesseractProcessName, arguments);
    psi->set_UseShellExecute(true);
    psi->set_CreateNoWindow(true);
    psi->set_WindowStyle(System::Diagnostics::ProcessWindowStyle::Hidden);
    psi->set_WorkingDirectory(System::IO::Path::GetDirectoryName(tesseractProcessName));

    auto p = MakeObject<System::Diagnostics::Process>(psi);
    p->Start();
    p->WaitForExit();

    auto streamReader = MakeObject<System::IO::StreamReader>(tmpFile + u".hocr");
    String text = streamReader->ReadToEnd();
    streamReader->Close();

    if (System::IO::File::Exists(tmpFile))
        System::IO::File::Delete(tmpFile);
    if (System::IO::File::Exists(tmpFile + u".hocr"))
        System::IO::File::Delete(tmpFile + u".hocr");

    return text;
}
```