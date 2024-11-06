---
title: C++の新機能
linktitle: 新機能
type: docs
weight: 10
url: ja/cpp/whatsnew/
description: このページでは、最近のリリースで導入されたAspose.PDF for C++の最も人気のある新機能を紹介します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-12-22"
---

## Aspose.PDF 24.8の新機能

ページにSVG画像を追加する機能。

## Aspose.PDF 24.4の新機能

SVG画像の読み込みに関する問題を修正。

## Aspose.PDF 24.3の新機能

PDFドキュメントを他の形式に変換する際のメモリリークを修正。

## Aspose.PDF 24.2の新機能

24.2以降に実装された内容:

- JPXDecoderのパフォーマンスが向上しました。

- 構造が壊れたドキュメントの読み込みを修正。

## Aspose.PDF 23.7の新機能

- PDFドキュメントをEPUB形式に保存する機能が導入されました:

```cpp

    void ConvertPDFtoEPUB()
    {
        std::clog << __func__ << ": Start" << std::endl;
        // String for path name
        String _dataDir("C:\\Samples\\Conversion\\");

        // String for input file name
        String infilename("sample.pdf");
        // String for output file name
        String outfilename("PDFToEPUB_out.epub");

        // Open document
        auto document = MakeObject<Document>(_dataDir + infilename);

        // Save PDF file into EPUB format
        document->Save(_dataDir + outfilename, SaveFormat::Epub);
        std::clog << __func__ << ": Finish" << std::endl;
    }
```

- PCL形式ファイルの読み込みが実装されました：

```cpp

    int main(int argc, char** argv)
    {
        try
        {
            auto options = System::MakeObject<PclLoadOptions>();
            options->ConversionEngine = Aspose::Pdf::PclLoadOptions::ConversionEngines::NewEngine;
            options->SupressErrors = false;

            auto doc = System::MakeObject<Document>(u"c:/aspose.pcl", options);
            doc->Save(u"e:/37432.pdf");
        }
        catch (const System::Exception& error)
        {
            Console::WriteLine(u"エラー: {0}", error->get_Message());
            return 1;
        }
        catch (const std::exception& error)
        {
            std::cerr << "エラー: " << error.what() << std::endl;
            return 1;
        }

        return 0;
    }
```

## Aspose.PDF 23.1の新機能

23.1以降、Dicom形式の画像のサポートが追加されました：

```cpp

    int main()
    {
        auto document = MakeObject<Document>();
        auto page = document->get_Pages()->Add();
        auto image = MakeObject<Image>();
        image->set_FileType(ImageFileType::Dicom);
        image->set_ImageStream(MakeObject<FileStream>(u"c:/aspose.pdf/Aspose.dcm", FileMode::Open, FileAccess::Read));
        page->get_Paragraphs()->Add(image);
        document->Save(u"e:/document.pdf");
    }
```

## Aspose.PDF 22.11の新機能

22.11から**Aspose.PDF for C++ macOS**の最初のパブリックリリースが発表されました。

Aspose.PDF for C++ macOSの最初のパブリックリリースを発表できることを嬉しく思います。Aspose.PDF for C++ macOSは、開発者がAdobe Acrobatを使用せずにPDF文書を作成および操作できるプロプライエタリなC++ライブラリです。
Aspose.PDF for C++ macOSを使用すると、開発者はフォームの作成、テキストの追加/編集、PDFページの操作、注釈の追加、カスタムフォントの処理などが可能になります。

## Aspose.PDF 22.5の新機能

PDF文書でのXFAフォームのサポートが実装されました。

## Aspose.PDF 22.4の新機能

新しいバージョンのAspose.PDF for C++は、Aspose.PDF for .Net 22.4およびAspose.Imaging 22.4のコードベースを持っています。

- System::Drawing::GetThumbnailImage()メソッドが実装されました;
- RegionDataNodeRectコンストラクタが最適化されました;
- 1ビットパーセルの白黒画像の読み込みが修正されました。

## Aspose.PDF 22.3の新機能

多くのクラスにメソッドのオーバーロードが追加されました。 これらは、以前はArrayPtrのみがサポートされていた場所でArrayView型のパラメーターをサポートします。

## Aspose.PDF 22.1の新機能

C++用Aspose.PDFの新バージョンは、.NetのAspose.PDF 22.1のコードベースを持っています。

- System::Xmlの新しい実装が提供されました。以前は、libxml2およびlibxsltライブラリに基づいたカスタム実装を持っていました。新しいバージョンは、移植されたCoreFXコードに基づいています。

- double-conversionライブラリが3.1.7バージョンにアップグレードされました。

- DllファイルはAspose証明書で署名されています。

## Aspose.PDF 21.10の新機能

### C++用Aspose.PDFはSVGをPDF形式に変換する機能をサポート

次のコードスニペットは、C++用Aspose.PDFを使用してSVGファイルをPDF形式に変換するプロセスを示しています。

```cpp

    void ConvertSVGtoPDF()
    {
        std::clog << "SVG to PDF convert: Start" << std::endl;

        String _dataDir("C:\\Samples\\Conversion\\");
        String infilename("sample.svg");
        String outfilename("ImageToPDF-SVG.pdf");

        auto options = MakeObject<SvgLoadOptions>();
        try {
        auto document = MakeObject<Document>(_dataDir + infilename, options);
        document->Save(_dataDir + outfilename);
        }
        catch (System::Exception ex) {
        std::cerr << ex->get_Message() << std::endl;
        }
        std::clog << "SVG to PDF convert: Finish" << std::endl;
    }
```
例を高度な機能で考えてみましょう：

```cpp

    void ConvertSVGtoPDF_Advanced()
    {
        std::clog << "SVGからPDFへの変換：開始" << std::endl;

        String _dataDir("C:\\Samples\\Conversion\\");
        String infilename("Aspose.svg");
        String outfilename("ImageToPDF-SVG.pdf");

        auto options = MakeObject<SvgLoadOptions>();
        options->set_AdjustPageSize(true);
        options->ConversionEngine = SvgLoadOptions::ConversionEngines::NewEngine;

        try {
        auto document = MakeObject<Document>(_dataDir + infilename, options);
        document->Save(_dataDir + outfilename);
        }
        catch (System::Exception ex) {
        std::cerr << ex->get_Message() << std::endl;
        }

        std::clog << "SVGからPDFへの変換：終了" << std::endl;
    }
```

## Aspose.PDF 21.4の新機能

### PDFドキュメントをHTML形式に保存する機能が実装されました

Aspose.PDF for C++は、PDFファイルをHTMLに変換する機能をサポートしています。

```cpp

    int main()
    {
        auto doc = MakeObject<Document>(u"e:\\sample.pdf");
        doc->Save(u"e:\\sample.html", SaveFormat::Html);
    }
```