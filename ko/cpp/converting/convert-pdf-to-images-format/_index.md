---
title: PDF를 이미지 형식으로 변환
linktitle: PDF를 이미지로 변환
type: docs
weight: 70
url: /ko/cpp/convert-pdf-to-images-format/
lastmod: "2021-11-19"
description: 이 주제는 Aspose.PDF가 PDF를 다양한 이미지 형식으로 변환하는 방법을 보여줍니다. 몇 줄의 코드로 PDF 페이지를 PNG, JPEG, BMP 이미지로 변환하십시오.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for C++**는 PDF를 이미지로 변환하기 위해 몇 가지 접근 방식을 사용합니다. 일반적으로 우리는 Device 접근 방식과 SaveOption을 사용하는 변환의 두 가지 접근 방식을 사용합니다. 이 섹션에서는 이러한 접근 방식 중 하나를 사용하여 PDF 문서를 BMP, JPEG, PNG, TIFF 및 SVG 형식과 같은 이미지 형식으로 변환하는 방법을 보여줍니다.

라이브러리에는 이미지를 변환하기 위해 가상 장치를 사용할 수 있는 여러 클래스가 있습니다. DocumentDevice는 전체 문서 변환을 지향하지만, ImageDevice는 특정 페이지를 위한 것입니다.

## DocumentDevice 클래스를 사용하여 PDF 변환

**Aspose.PDF for C++**는 PDF 페이지를 TIFF 이미지로 변환할 수 있습니다.

The [TiffDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device/) (기반 DocumentDevice) 클래스는 PDF 페이지를 TIFF 이미지로 변환할 수 있게 해줍니다. 이 클래스는 PDF 파일의 모든 페이지를 단일 TIFF 이미지로 변환할 수 있는 [Process](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device#a0790daa96125c5638a645647e9678f0c)라는 메서드를 제공합니다.

{{% alert color="success" %}}
**PDF를 TIFF로 온라인 변환 시도**

Aspose.PDF for C++는 ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)라는 온라인 무료 응용 프로그램을 제공하여 기능과 품질을 조사해 볼 수 있습니다.

[![무료 앱으로 Aspose.PDF 변환 PDF to TIFF](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### PDF 페이지를 하나의 TIFF 이미지로 변환

Aspose.PDF for C++는 PDF 파일의 모든 페이지를 단일 TIFF 이미지로 변환하는 방법을 설명합니다:

1. Open [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) with MakeObject.  
1. Resolution 객체를 만듭니다.  
1. [TIffSettings](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_settings/) 객체를 만듭니다.  
1. 지정된 속성으로 [Tiff device](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.tiff_device/)를 만듭니다.  
1. 특정 페이지를 변환하고 이미지를 스트림에 저장합니다.

다음 코드 스니펫은 모든 PDF 페이지를 단일 TIFF 이미지로 변환하는 방법을 보여줍니다.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTIFF()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 파일 이름을 위한 문자열
    String infilename("PageToTiff.pdf");
    String outfilename("PagesToTIFF_out.tif");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto imageStream = System::IO::File::OpenWrite(_dataDir + outfilename);

    // Resolution 객체 만들기
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // TiffSettings 객체 만들기
    auto tiffSettings = MakeObject<Aspose::Pdf::Devices::TiffSettings>();
    tiffSettings->set_Compression(Aspose::Pdf::Devices::CompressionType::None);
    tiffSettings->set_Depth(Aspose::Pdf::Devices::ColorDepth::Default);
    tiffSettings->set_Shape(Aspose::Pdf::Devices::ShapeType::Landscape);
    tiffSettings->set_SkipBlankPages(false);

    // TIFF 장치 만들기
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution, tiffSettings);

    // 페이지를 변환하고 이미지를 스트림에 저장
    tiffDevice->Process(document, 1, 2, imageStream);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
### 한 페이지를 TIFF 이미지로 변환

Aspose.PDF for C++를 사용하면 PDF 파일의 특정 페이지를 TIFF 이미지로 변환할 수 있습니다. 페이지 번호를 인수로 사용하여 변환하는 오버로드된 버전의 Process(..) 메서드를 사용하세요. 다음 코드 스니펫은 PDF의 첫 페이지를 TIFF 형식으로 변환하는 방법을 보여줍니다.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTiffSinglePage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 파일 이름을 위한 문자열
    String infilename("PageToTiff.pdf");
    String outfilename("PageToTiff_out.tif");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto imageStream = System::IO::File::OpenWrite(_dataDir + outfilename);

    // 해상도 객체 생성
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // TIFF 장치 생성
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution);

    // 특정 페이지를 변환하고 이미지를 스트림에 저장
    tiffDevice->Process(document, 1, 1, imageStream);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### 변환 중 Bradley 알고리즘 사용

Aspose.PDF for C++는 LZW 압축을 사용하여 PDF를 TIF로 변환하는 기능을 지원하고 있으며, AForge를 사용하여 이진화(Binarization)를 적용할 수 있습니다. 그러나 일부 고객은 특정 이미지에 대해 Otsu를 사용하여 임계값을 얻어야 하기 때문에 Bradley도 사용하고 싶어합니다. 

```cpp
void Convert_PDF_To_Images::ConvertPDFtoTiffBradleyBinarization()
{
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 문서 열기
    auto pdfDocument = MakeObject<Document>(_dataDir + u"PageToTIFF.pdf");

    String outputImageFile = _dataDir + u"resultant_out.tif";
    String outputBinImageFile = _dataDir + u"37116-bin_out.tif";

    // 해상도 객체 생성
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // TiffSettings 객체 생성
    auto tiffSettings = MakeObject<Aspose::Pdf::Devices::TiffSettings>();
    tiffSettings->set_Compression(Aspose::Pdf::Devices::CompressionType::LZW);
    tiffSettings->set_Depth(Aspose::Pdf::Devices::ColorDepth::Format1bpp);

    // TIFF 장치 생성
    auto tiffDevice = MakeObject<Aspose::Pdf::Devices::TiffDevice>(resolution, tiffSettings);
    auto imageStream = System::IO::File::OpenWrite(_dataDir + outputImageFile);

    // 특정 페이지를 변환하고 이미지를 스트림에 저장
    tiffDevice->Process(pdfDocument, 1, 2, imageStream);

    imageStream->Close();

    auto inStream = System::IO::File::OpenRead(outputImageFile);
    auto outStream = System::IO::File::OpenWrite(outputBinImageFile);

    tiffDevice->BinarizeBradley(inStream, outStream, 0.1);
}
```

## ImageDevice 클래스를 사용하여 PDF 변환

`ImageDevice`는 `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` 및 `EmfDevice`의 조상입니다.

- [BmpDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device/) 클래스는 PDF 페이지를 <abbr title="Bitmap Image File">BMP</abbr> 이미지로 변환할 수 있게 해줍니다.
- [EmfDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.emf_device/) 클래스는 PDF 페이지를 <abbr title="Enhanced Meta File">EMF</abbr> 이미지로 변환할 수 있게 해줍니다.
- [JpegDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.jpeg_device/) 클래스는 PDF 페이지를 JPEG 이미지로 변환할 수 있게 해줍니다.
- [PngDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.png_device/) 클래스는 PDF 페이지를 <abbr title="Portable Network Graphics">PNG</abbr> 이미지로 변환할 수 있게 해줍니다.

- [GifDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.gif_device/) 클래스는 PDF 페이지를 <abbr title="Graphics Interchange Format">GIF</abbr> 이미지로 변환할 수 있게 해줍니다.

PDF 페이지를 이미지로 변환하는 방법을 살펴보겠습니다.

[BmpDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device) 클래스는 PDF 파일의 특정 페이지를 BMP 이미지 형식으로 변환할 수 있는 [Process](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.bmp_device#a22cefdb47b7c762320fa7973aa4f1f93)라는 메소드를 제공합니다. 다른 클래스도 같은 메소드를 가지고 있습니다. 따라서 PDF 페이지를 이미지로 변환해야 한다면, 필요한 클래스를 인스턴스화하면 됩니다.

다음 코드 스니펫은 이 가능성을 보여줍니다:

```cpp
void Convert_PDF_To_Images::ConvertPDFusingImageDevice()
{
    std::clog << __func__ << ": Start" << std::endl;

    // 경로명에 대한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 해상도 객체 생성
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
    // 경로명에 대한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    for (int pageCount = 1; pageCount <= document->get_Pages()->get_Count(); pageCount++)
    {
    String outfilename = String::Format(u"{0}PageToBmp{1}_out.{2}",
    _dataDir, pageCount, ext);

    auto imageStream = System::IO::File::OpenWrite(outfilename);

    // 해상도 객체 생성
    auto resolution = MakeObject<Aspose::Pdf::Devices::Resolution>(300);

    // 특정 페이지를 변환하고 이미지를 스트림에 저장
    imageDevice->Process(document->get_Pages()->idx_get(pageCount), imageStream);

    // 스트림 닫기
    imageStream->Close();
    }
}
```

{{% alert color="success" %}}
**PDF를 PNG로 온라인 변환 시도**

무료 애플리케이션이 작동하는 방식을 보여주는 예로 다음 기능을 확인하세요.

Aspose.PDF for C++는 온라인 무료 애플리케이션 ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)을 제공하며, 여기서 기능과 품질을 조사해 볼 수 있습니다.

[![무료 앱을 사용하여 PDF를 PNG로 변환하는 방법](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## SaveOptions 클래스를 사용하여 PDF 변환

이 기사 부분에서는 C++ 및 SaveOptions 클래스를 사용하여 PDF를 <abbr title="Scalable Vector Graphics">SVG</abbr>로 변환하는 방법을 보여줍니다.

{{% alert color="success" %}}
**PDF를 SVG로 온라인 변환 시도**

Aspose.PDF for C++는 온라인 무료 애플리케이션 ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)을 제공하며, 여기서 기능과 품질을 조사해 볼 수 있습니다.

[![무료 앱을 사용하여 PDF를 SVG로 변환하는 방법](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

PDF를 SVG로 변환하기 위해 Aspose.PDF for CPP는 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스의 [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) 메서드를 제공합니다. PDF를 SVG로 변환하려면 출력 경로와 enum SaveFormat:: svg를 Save 메서드에 전달해야 합니다. 다음 코드 스니펫은 PDF를 SVG로 변환하는 방법을 보여줍니다:

이 문서는 C++를 사용하여 PDF를 <abbr title="Scalable Vector Graphics">SVG</abbr>로 변환하는 방법을 가르칩니다.

**스케일러블 벡터 그래픽스(SVG)**는 2차원 벡터 그래픽, 정적 및 동적(대화형 또는 애니메이션)의 XML 기반 파일 형식의 사양 집합입니다. SVG 사양은 1999년부터 월드 와이드 웹 컨소시엄(W3C)에 의해 개발된 오픈 표준입니다.

SVG 이미지와 그 동작은 XML 텍스트 파일로 정의됩니다. 이것은 검색, 인덱싱, 스크립팅이 가능하며 필요 시 압축할 수 있음을 의미합니다. XML 파일로서 SVG 이미지는 모든 텍스트 편집기로 생성 및 편집할 수 있지만, Inkscape와 같은 드로잉 프로그램을 사용하는 것이 더 편리한 경우가 많습니다.

Aspose.PDF for C++는 SVG 이미지를 PDF 형식으로 변환하는 기능을 지원하며, PDF 파일을 SVG 형식으로 변환하는 기능도 제공합니다. 이 요구 사항을 충족하기 위해 `SvgSaveOptions` 클래스가 Aspose.PDF 네임스페이스에 도입되었습니다. SvgSaveOptions의 객체를 인스턴스화하고 이를 [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) 메서드의 두 번째 인수로 전달하십시오.

다음 코드 조각은 C++로 PDF 파일을 SVG 형식으로 변환하는 단계를 보여줍니다.

```cpp
void Convert_PDF_To_Images::ConvertPDFtoSvgSinglePage()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름에 대한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 파일 이름에 대한 문자열
    String infilename("PageToSvg.pdf");
    String outfilename("PageToSvg_out.svg");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // SvgSaveOptions의 객체 인스턴스화
    auto saveOptions = MakeObject<SvgSaveOptions>();
    // SVG 이미지를 Zip 아카이브로 압축하지 않음
    saveOptions->CompressOutputToZipArchive = false;

    try {
    // SVG 파일로 출력 저장
    document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```