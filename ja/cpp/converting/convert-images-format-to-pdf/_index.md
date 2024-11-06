---
title: さまざまな画像形式をPDFに変換する
linktitle: 画像をPDFに変換する
type: docs
weight: 60
url: ja/cpp/convert-images-format-to-pdf/
lastmod: "2021-11-19"
description: このトピックでは、Aspose.PDF for C++ライブラリを使用して、さまざまな画像形式をPDFに変換する方法を紹介します。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for C++** を使用すると、さまざまな形式の画像をPDFファイルに変換できます。当ライブラリは、BMP、DICOM、EMF、JPG、PNG、SVG、TIFFといった最も一般的な画像形式を変換するためのコードスニペットを示しています。

## BMPをPDFに変換

**Aspose.PDF for C++** ライブラリを使用してBMPファイルをPDFドキュメントに変換します。

<abbr title="Bitmap Image File">BMP</abbr> 画像は拡張子を持つファイルです。BMPはビットマップ画像ファイルを表し、ビットマップデジタル画像を保存するために使用されます。これらの画像はグラフィックアダプタに依存せず、デバイス独立ビットマップ (DIB) ファイル形式とも呼ばれます。Aspose.PDF for C++ APIを使用してBMPをPDFファイルに変換できます。 したがって、BMP画像を変換するために次の手順に従うことができます：

1. パス名とファイル名のための[String Class](https://reference.aspose.com/pdf/cpp/class/system.string)を作成します。
1. 新しいDocumentオブジェクトのインスタンスを作成します。
1. この[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)に新しい[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)を追加します。
1. 新しいAspose.Pdf BMPを作成します。
1. 入力ファイルを使用してAspose.PDF BMPオブジェクトを初期化します。
1. Aspose.PDF BMPを段落としてページに追加します。
1. 最後に、出力PDFファイルを保存します。

したがって、次のコードスニペットはこれらの手順に従い、C++を使用してBMPをPDFに変換する方法を示しています：

```cpp
void ConvertBMPtoPDF() 
{
    std::clog << "BMP to PDF convert: Start" << std::endl;

    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for input file name
    String infilename("sample.bmp");

    // String for input file name
    String outfilename("ImageToPDF-BMP.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Add empty page in empty document
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Add image on a page
    page->get_Paragraphs()->Add(image);

    // Save output document
    document->Save(_dataDir + outfilename);

    std::clog << "BMP to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**BMPをPDFにオンラインで変換してみてください**

Asposeは、オンラインで無料のアプリケーション["BMP to PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)を提供しています。ここで機能性と品質を試すことができます。

[![Aspose.PDF Convertion BMP to PDF using Free App](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## DICOMをPDFに変換

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr>形式は、デジタル医療画像や診断された患者の文書の作成、保存、送信、視覚化のための医療業界の標準です。

**Aspsoe.PDF for C++**はDICOMおよびSVG画像を変換することができますが、技術的な理由で画像を追加するためには、PDFに追加するファイルの種類を指定する必要があります：

1. パス名とファイル名のために[String Class](https://reference.aspose.com/pdf/cpp/class/system.string)を作成します。
1. インスタンス化する [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) オブジェクト。
1. ドキュメントのページコレクションに [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) を追加します。
1. Aspose.PDF TDicom が段落としてページに追加されます。
1. 入力画像ファイルを読み込み、[保存](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) します。

次のコードスニペットは、Aspose.PDF を使用して DICOM ファイルを PDF 形式に変換する方法を示しています。DICOM 画像を読み込み、PDF ファイルのページに画像を配置し、出力を PDF として保存する必要があります。

```cpp
void ConvertDICOMtoPDF()
{
    std::clog << "DICOM to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("CR_Anno.dcm");
    String outfilename("PDFWithDicomImage_out.pdf");

    // Instantiate Document Object
    auto document = MakeObject<Document>();

    // Add a page to pages collection of document
    auto page = document->get_Pages()->Add();

    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);
    image->set_FileType(Aspose::Pdf::ImageFileType::Dicom);

    page->get_Paragraphs()->Add(image);

    // Save output as PDF format
    document->Save(_dataDir + outfilename);
    std::clog << "DICOM to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**DICOM を PDF にオンラインで変換してみてください**

Aspose は、オンライン無料アプリケーション ["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/) を提供しており、その機能や品質を試してみることができます。

[![Aspose.PDF コンバージョン DICOM から PDF への無料アプリ使用](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## EMF を PDF に変換

<abbr title="Enhanced metafile format">EMF</abbr>EMF は、グラフィカルな画像をデバイスに依存せずに保存します。EMF のメタファイルは、任意の出力デバイスで解析後に保存された画像をレンダリングできるように、時系列順の可変長レコードで構成されています。さらに、以下の手順を使用して EMF を PDF 画像に変換できます：

1. パス名とファイル名のための[String クラス](https://reference.aspose.com/pdf/cpp/class/system.string)を作成します。
1. 新しい Document オブジェクトのインスタンスを作成します。
1. この[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)に新しいページを追加します。
1.  新しい Aspose.Pdf TIFF が作成されます。
1. Aspose.PDF TIFF オブジェクトは入力ファイルを使用して初期化されます。
1. Aspose.PDF TIFF は段落としてページに追加されます。
1. 入力画像ファイルを読み込み、[保存](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa)します。

さらに、以下のコードスニペットは、C++ で EMF を PDF に変換する方法を示しています：

```cpp
void ConvertEMFtoPDF() 
{
    std::clog << "EMF to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.emf");
    String outfilename("ImageToPDF_emf.pdf");

    auto fileStream = System::IO::File::OpenRead(_dataDir + infilename);
    auto myimage = MakeObject<System::Drawing::Bitmap>(fileStream);

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto currentImage = MakeObject<System::IO::MemoryStream>();
    myimage->Save(currentImage, System::Drawing::Imaging::ImageFormat::get_Tiff());

    auto imageht = MakeObject<Aspose::Pdf::Image>();
    imageht->set_ImageStream(currentImage);
    page->get_Paragraphs()->Add(imageht);

    document->Save(_dataDir + outfilename);

    std::clog << "EMF to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**EMF を PDF にオンラインで変換してみる**

Aspose はオンラインの無料アプリケーション ["EMF to PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/) を提供しており、そこで機能性や品質を調査することができます。

[![Aspose.PDF Convertion EMF to PDF using Free App](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## JPG を PDF に変換

JPG を PDF に変換する方法に悩む必要はありません。なぜなら、**Aspose.PDF for C++** ライブラリが最適な解決策を提供するからです。

Aspose.PDF for C++ を使用して、次の手順で JPG 画像を PDF に非常に簡単に変換できます。

1. パス名とファイル名のために [String クラス](https://reference.aspose.com/pdf/cpp/class/system.string) を作成します。
1. 新しい Document オブジェクトのインスタンスが作成されます。
1. この [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) に新しいページを追加します。
1. 新しい Aspose::Pdf::Image が作成されます。
1. Aspose.PDF Image オブジェクトは、入力ファイルを使用して初期化されます。
1. Aspose.PDF Imageは、段落としてページに追加されます。  
1. 入力画像ファイルをロードして保存します。

以下のコードスニペットは、C++を使用してJPG画像をPDFに変換する方法を示しています：

```cpp
void ConvertJPEGtoPDF() 
{
    std::clog << "JPEG to PDF convert: Start" << std::endl;
    // パス名のための文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // 入力ファイル名のための文字列
    String infilename("sample.jpg");

    // 出力ファイル名のための文字列
    String outfilename("ImageToPDF-JPEG.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>();

    // 空のドキュメントに空のページを追加
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // ページに画像を追加
    page->get_Paragraphs()->Add(image);

    // 出力ドキュメントを保存
    document->Save(_dataDir + outfilename);
    std::clog << "JPEG to PDF convert: Finish" << std::endl;
}
```

次に、**ページの高さと幅が同じ**画像をPDFに変換する方法を確認できます。  画像の寸法を取得し、それに応じてPDFドキュメントのページ寸法を設定する手順は以下の通りです。

1. 入力画像ファイルを読み込む
1. 画像の高さと幅を取得する
1. ページの高さ、幅、および余白を設定する
1. 出力PDFファイルを保存する

以下のコードスニペットは、C++を使用して同じページの高さと幅で画像をPDFに変換する方法を示しています。

```cpp
void ConvertJPGtoPDF_fitsize() 
{
    std::clog << "JPEG to PDF convert: Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for input file name
    String infilename("sample.jpg");

    // String for input file name
    String outfilename("ImageToPDF-JPG.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Add empty page in empty document
    auto page = document->get_Pages()->Add();
    auto fileStream = System::IO::File::OpenRead(_dataDir + infilename);
    auto bitMap = MakeObject<System::Drawing::Bitmap>(fileStream);


    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Add image on a page
    page->get_Paragraphs()->Add(image);

    // Set page dimensions and margins
    page->get_PageInfo()->set_Height(bitMap->get_Height());
    page->get_PageInfo()->set_Width(bitMap->get_Width());
    page->get_PageInfo()->get_Margin()->set_Bottom(0);
    page->get_PageInfo()->get_Margin()->set_Top(0);
    page->get_PageInfo()->get_Margin()->set_Right(0);
    page->get_PageInfo()->get_Margin()->set_Left(0);
    page->get_Paragraphs()->Add(image);

    // Save output document
    document->Save(_dataDir + outfilename);
    std::clog << "JPEG to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**JPGをPDFにオンラインで変換してみてください**

Asposeは、オンライン無料アプリケーション["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)を提供しており、そこで機能性と品質を調査することができます。

[![Aspose.PDF Convertion JPG to PDF using Free App](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## PNGをPDFに変換する

**Aspose.PDF for C++**は、PNG画像をPDF形式に変換する機能をサポートしています。次のコードスニペットを確認してタスクを実現してください。

<abbr title="Portable Network Graphics">PNG</abbr>は、ロスレス圧縮を使用するラスター画像ファイル形式の一種であり、そのため利用者の間で人気があります。

以下の手順を使用してPNGをPDF画像に変換できます：

1. パス名とファイル名のための[String Class](https://reference.aspose.com/pdf/cpp/class/system.string)を作成します。
1. 新しいDocumentオブジェクトのインスタンスを作成します。
1. 新しいページをこの[ドキュメント](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)に追加します。
1. 新しいAspose.Pdf PNGが作成されます。
1. 入力ファイルを使用してAspose.PDF PNGオブジェクトが初期化されます。
1. Aspose.PDF PNGがページに段落として追加されます。
1. 入力画像ファイルをロードして保存します。

さらに、以下のコードスニペットは、C++アプリケーションでPNGをPDFに変換する方法を示しています。

```cpp
void ConvertPNGtoPDF() 
{
    std::clog << "PNG to PDF convert: Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for input file name
    String infilename("sample.png");

    // String for input file name
    String outfilename("ImageToPDF-PNG.pdf");

    // Open document
    auto document = MakeObject<Document>();

    // Add empty page in empty document
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // Add image on a page
    page->get_Paragraphs()->Add(image);

    // Save output document
    document->Save(_dataDir + outfilename);
    std::clog << "PNG to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**PNGをPDFにオンラインで変換してみてください**

Asposeは、オンライン無料アプリケーション["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/)を提供しており、そこで機能や品質を調査することができます。

[![Aspose.PDF Convertion PNG to PDF using Free App](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## SVGをPDFに変換

**Aspose.PDF for C++**は、SVG画像をPDF形式に変換する方法と、ソース<abbr title="Scalable Vector Graphics">SVG</abbr>ファイルの寸法を取得する方法を説明します。

スケーラブルベクターグラフィックス（SVG）は、2次元のベクターグラフィックス、静的および動的（インタラクティブまたはアニメーション）のためのXMLベースのファイル形式の仕様ファミリーです。SVG仕様は、1999年以降、ワールドワイドウェブコンソーシアム（W3C）によって開発されているオープンスタンダードです。

SVG画像とその動作は、XMLテキストファイルで定義されています。 これは、検索、インデックス化、スクリプト化され、必要に応じて圧縮されることを意味します。XMLファイルとして、SVG画像は任意のテキストエディタで作成および編集できますが、Inkscapeなどの描画プログラムで作成する方が便利です。

1. パス名とファイル名のための[String Class](https://reference.aspose.com/pdf/cpp/class/system.string)を作成します。
1. [`SvgLoadOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.svg_load_options)クラスのインスタンスを作成します。
1. ソースファイル名とオプションを指定して[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)クラスのインスタンスを作成します。
1. 希望のファイル名でドキュメントを保存します。

以下のコードスニペットは、Aspose.PDF for C++を使用してSVGファイルをPDF形式に変換するプロセスを示しています。

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
高機能を備えた例を考えてみましょう：

```cpp
void ConvertSVGtoPDF_Advanced()
{
    std::clog << "SVG to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("Sweden-Royal-flag-grand-coa.svg");
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

    std::clog << "SVG to PDF convert: Finish" << std::endl;
}
```

{{% alert color="success" %}}
**SVGフォーマットをPDFにオンラインで変換してみてください**


Aspose.PDF for C++は、オンラインで無料のアプリケーション["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf)を提供しており、その機能と品質を調査することができます。


[![Aspose.PDF Convertion SVG to PDF with Free App](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## TIFFをPDFに変換

**Aspose.PDF** ファイル形式は、単一フレームまたはマルチフレームの<abbr title="Tag Image File Format">TIFF</abbr>画像をサポートしています。つまり、C++アプリケーションでTIFF画像をPDFに変換することができます。

TIFFまたはTIF、タグ付き画像ファイル形式は、このファイル形式の標準に準拠するさまざまなデバイスでの使用を目的としたラスター画像を表します。TIFF画像には、異なる画像の複数のフレームを含めることができます。Aspose.PDFファイル形式もサポートされており、単一フレームまたはマルチフレームのTIFF画像を処理できます。そのため、C++アプリケーションでTIFF画像をPDFに変換することができます。したがって、以下のステップを使用して、マルチページのTIFF画像をマルチページのPDFドキュメントに変換する例を考えてみます：

1. パス名とファイル名のために[String Class](https://reference.aspose.com/pdf/cpp/class/system.string)を作成します。
1.
``` 新しいDocumentオブジェクトのインスタンスが作成されます。
1. この[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)に新しいページを追加します。
1. 新しいAspose.Pdf TIFFが作成されます。
1. Aspose.PDF TIFFオブジェクトは入力ファイルを使用して初期化されます。
1. Aspose.PDF TIFFは段落としてページに追加されます。
1. 入力画像ファイルを読み込み、保存します。

さらに、以下のコードスニペットは、複数ページまたは複数フレームのTIFF画像をC++でPDFに変換する方法を示しています。