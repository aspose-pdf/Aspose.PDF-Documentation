---
title: PDFを画像形式に変換する
linktitle: PDFを画像に変換する
type: docs
weight: 70
url: /ja/cpp/convert-pdf-to-images-format/
lastmod: "2021-11-19"
description: このトピックでは、Aspose.PDFがPDFをさまざまな画像形式に変換する方法を紹介します。数行のコードでPDFページをPNG、JPEG、BMP画像に変換します。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for C++** は、PDFを画像に変換するためのいくつかのアプローチを使用します。一般的に、デバイスアプローチを使用した変換とSaveOptionを使用した変換の2つのアプローチを使用します。このセクションでは、これらのアプローチのいずれかを使用して、PDFドキュメントをBMP、JPEG、PNG、TIFF、SVG形式の画像に変換する方法を示します。

ライブラリには、仮想デバイスを使用して画像を変換することを可能にするいくつかのクラスがあります。DocumentDeviceはドキュメント全体の変換を目的としていますが、ImageDeviceは特定のページ用です。

## DocumentDeviceクラスを使用してPDFを変換する

**Aspose.PDF for C++** は、PDFページをTIFF画像に変換することが可能です。

The [TiffDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device/)（DocumentDeviceに基づく）クラスは、PDFページをTIFF画像に変換することを可能にします。このクラスは、PDFファイル内のすべてのページを単一のTIFF画像に変換することを可能にする[Process](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device#a0790daa96125c5638a645647e9678f0c)という名前のメソッドを提供します。

{{% alert color="success" %}}
**PDFをTIFFにオンラインで変換してみてください**

Aspose.PDF for C++はオンラインの無料アプリケーション["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)を提供しており、そこで機能と品質を調査することができます。

[![Aspose.PDF conversion PDF to TIFF with Free App](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### PDFページを1つのTIFF画像に変換

Aspose.PDF for С++ は、PDFファイル内のすべてのページを単一のTIFF画像に変換する方法を説明します:

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/)をMakeObjectで開きます。
1. Resolutionオブジェクトを作成します。
1. [TIffSettings](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_settings/)オブジェクトを作成します。
1. 指定された属性で[Tiff device](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device/)を作成します。
1. 特定のページを変換し、画像をストリームに保存します。

次のコードスニペットは、すべてのPDFページを単一のTIFF画像に変換する方法を示しています。

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTIFF()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名のための文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // ファイル名のための文字列
    String infilename("PageToTiff.pdf");
    String outfilename("PagesToTIFF_out.tif");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto imageStream = System::IO::File::OpenWrite(_dataDir + outfilename);

    // Resolutionオブジェクトを作成する
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // TiffSettingsオブジェクトを作成する
    auto tiffSettings = MakeObject<Aspose::Pdf::Devices::TiffSettings>();
    tiffSettings->set_Compression(Aspose::Pdf::Devices::CompressionType::None);
    tiffSettings->set_Depth(Aspose::Pdf::Devices::ColorDepth::Default);
    tiffSettings->set_Shape(Aspose::Pdf::Devices::ShapeType::Landscape);
    tiffSettings->set_SkipBlankPages(false);

    // TIFFデバイスを作成する
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution, tiffSettings);

    // ページを変換し、画像をストリームに保存する
    tiffDevice->Process(document, 1, 2, imageStream);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
### 特定のページをTIFF画像に変換する

Aspose.PDF for C++を使用すると、PDFファイルの特定のページをTIFF画像に変換できます。変換のためにページ番号を引数として受け取るProcess(..)メソッドのオーバーロードバージョンを使用します。次のコードスニペットは、PDFの最初のページをTIFF形式に変換する方法を示しています。

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTiffSinglePage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名の文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // ファイル名の文字列
    String infilename("PageToTiff.pdf");
    String outfilename("PageToTiff_out.tif");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto imageStream = System::IO::File::OpenWrite(_dataDir + outfilename);

    // Resolutionオブジェクトを作成
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // TIFFデバイスを作成
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution);

    // 特定のページを変換し、画像をストリームに保存
    tiffDevice->Process(document, 1, 1, imageStream);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### 変換時にBradleyアルゴリズムを使用する

Aspose.PDF for C++は、LZW圧縮を使用してPDFをTIFに変換する機能をサポートしており、その後AForgeを使用して二値化を適用できます。しかし、ある顧客から、特定の画像に対して大津のしきい値を取得する必要があるため、Bradleyも使用したいという要望がありました。

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTiffBradleyBinarization()
{
    // パス名用の文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // ドキュメントを開く
    auto pdfDocument = MakeObject<Document>(_dataDir + u"PageToTIFF.pdf");

    String outputImageFile = _dataDir + u"resultant_out.tif";
    String outputBinImageFile = _dataDir + u"37116-bin_out.tif";

    // 解像度オブジェクトを作成
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // TiffSettingsオブジェクトを作成
    auto tiffSettings = MakeObject<Aspose::Pdf::Devices::TiffSettings>();
    tiffSettings->set_Compression(Aspose::Pdf::Devices::CompressionType::LZW);
    tiffSettings->set_Depth(Aspose::Pdf::Devices::ColorDepth::Format1bpp);

    // TIFFデバイスを作成
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution, tiffSettings);
    auto imageStream = System::IO::File::OpenWrite(_dataDir + outputImageFile);

    // 特定のページを変換し、画像をストリームに保存
    tiffDevice->Process(pdfDocument, 1, 2, imageStream);

    imageStream->Close();

    auto inStream = System::IO::File::OpenRead(outputImageFile);
    auto outStream = System::IO::File::OpenWrite(outputBinImageFile);

    tiffDevice->BinarizeBradley(inStream, outStream, 0.1);
}
```

## Convert PDF using ImageDevice class

`ImageDevice` は、`BmpDevice`、`JpegDevice`、`GifDevice`、`PngDevice`、`EmfDevice` の祖先です。

- [BmpDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device/) クラスを使用すると、PDF ページを <abbr title="Bitmap Image File">BMP</abbr> 画像に変換できます。
- [EmfDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.emf_device/) クラスを使用すると、PDF ページを <abbr title="Enhanced Meta File">EMF</abbr> 画像に変換できます。
- [JpegDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.jpeg_device/) クラスを使用すると、PDF ページを JPEG 画像に変換できます。
- [PngDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.png_device/) クラスを使用すると、PDF ページを <abbr title="Portable Network Graphics">PNG</abbr> 画像に変換できます。

- [GifDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.gif_device/) クラスを使用すると、PDF ページを <abbr title="Graphics Interchange Format">GIF</abbr> 画像に変換できます。

以下を見て、PDFページを画像に変換する方法を確認しましょう。

[BmpDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device) クラスは、PDFファイルの特定のページをBMP画像形式に変換することを可能にする[Process](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device#a22cefdb47b7c762320fa7973aa4f1f93)というメソッドを提供します。他のクラスも同じメソッドを持っています。したがって、PDFページを画像に変換する必要がある場合は、必要なクラスをインスタンス化するだけです。

次のコードスニペットは、この可能性を示しています:

```cpp
void Convert_PDF_To_Images::ConvertPDFusingImageDevice()
{
    std::clog << __func__ << ": Start" << std::endl;

    // パス名の文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // Resolutionオブジェクトの作成            
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300); //300 dpi

    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    bmpDevice = MakeObject<Aspose::Pdf::Devices::BmpDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    jpegDevice = MakeObject<Aspose::Pdf::Devices::JpegDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    gifDevice = MakeObject<Aspose::Pdf::Devices::GifDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    pngDevice = MakeObject<Aspose::Pdf::Devices::PngDevice>(resolution);
    System::SmartPtr<Aspose::Pdf::Devices::ImageDevice>
    emfDevice = MakeObject<Aspose::Pdf::Devices::EmfDevice>(resolution);

    auto document = MakeObject<Document>(_dataDir + u"ConvertAllPagesToBmp.pdf");

    ConvertPDFtoImage(bmpDevice, u"bmp", document);
    ConvertPDFtoImage(jpegDevice, u"jpeg", document);
    ConvertPDFtoImage(gifDevice, u"gif", document);
    ConvertPDFtoImage(pngDevice, u"png", document);
    ConvertPDFtoImage(emfDevice, u"emf", document);

    std::clog << __func__ << ": Finish" << std::endl;

}

void Convert_PDF_To_Images::ConvertPDFtoImage(
 System::SmartPtr<Aspose::Pdf::Devices::ImageDevice> imageDevice,
 String ext, System::SmartPtr<Document> document)
{
    // パス名の文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    for (int pageCount = 1; pageCount <= document->get_Pages()->get_Count(); pageCount++)
    {
    String outfilename = String::Format(u"{0}PageToBmp{1}_out.{2}",
    _dataDir, pageCount, ext);

    auto imageStream = System::IO::File::OpenWrite(outfilename);

    // Resolutionオブジェクトの作成
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // 特定のページを変換し、ストリームに画像を保存
    imageDevice->Process(document->get_Pages()->idx_get(pageCount), imageStream);

    // ストリームを閉じる
    imageStream->Close();
    }
}
```

{{% alert color="success" %}}
**PDFをPNGにオンラインで変換してみてください**

私たちの無料アプリケーションがどのように機能するかの例として、次の機能を確認してください。

Aspose.PDF for C++は、オンライン無料アプリケーション["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)を提供しており、その機能と品質を試すことができます。

[![無料アプリを使ってPDFをPNGに変換する方法](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## SaveOptionsクラスを使用してPDFを変換する

この記事のこの部分では、C++とSaveOptionsクラスを使用してPDFを<abbr title="Scalable Vector Graphics">SVG</abbr>に変換する方法を紹介します。

{{% alert color="success" %}}
**PDFをSVGにオンラインで変換してみてください**

Aspose.PDF for C++は、オンライン無料アプリケーション["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)を提供しており、その機能と品質を試すことができます。

[![Aspose.PDF 無料アプリでPDFをSVGに変換](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

PDFをSVGに変換するために、Aspose.PDF for CPPは[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)クラスの[Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa)メソッドを提供します。PDFをSVGに変換するためには、出力パスとenum SaveFormat:: svgをSaveメソッドに渡す必要があります。以下のコードスニペットは、PDFをSVGに変換する方法を示しています。

この記事では、C++を使用してPDFを<abbr title="Scalable Vector Graphics">SVG</abbr>に変換する方法を説明します。

**スケーラブルベクターグラフィックス (SVG)** は、静的および動的（インタラクティブまたはアニメーション）な2次元ベクターグラフィックスのためのXMLベースのファイル形式の仕様のファミリーです。SVG仕様は、1999年からワールドワイドウェブコンソーシアム（W3C）によって開発されているオープンスタンダードです。

SVG画像とその動作は、XMLテキストファイルで定義されています。 これは、検索、インデックス作成、スクリプト作成、必要に応じて圧縮できることを意味します。XMLファイルとして、SVG画像は任意のテキストエディタで作成および編集できますが、Inkscapeなどの描画プログラムを使用して作成する方が便利なことがよくあります。

Aspose.PDF for C++ は、SVG 画像を PDF 形式に変換する機能をサポートし、PDF ファイルを SVG 形式に変換する機能も提供します。この要件を達成するために、`SvgSaveOptions` クラスが Aspose.PDF 名前空間に導入されました。SvgSaveOptions のオブジェクトをインスタンス化し、それを [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) メソッドの第 2 引数として渡します。

次のコードスニペットは、PDF ファイルを C++ で SVG 形式に変換する手順を示しています。

```cpp
void Convert_PDF_To_Images::ConvertPDFtoSvgSinglePage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // パス名の文字列
    String _dataDir("C:\\Samples\\Conversion\\");

    // ファイル名の文字列
    String infilename("PageToSvg.pdf");
    String outfilename("PageToSvg_out.svg");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + infilename);

    // SvgSaveOptions のオブジェクトをインスタンス化
    auto saveOptions = MakeObject<SvgSaveOptions>();
    // SVG 画像を Zip アーカイブに圧縮しない
    saveOptions->CompressOutputToZipArchive = false;

    try {
    // 出力を SVG ファイルに保存
    document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```