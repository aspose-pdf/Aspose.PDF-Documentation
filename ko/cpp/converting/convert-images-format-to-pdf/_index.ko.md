---
title: 다양한 이미지 형식을 PDF로 변환 
linktitle: 이미지를 PDF로 변환
type: docs
weight: 60
url: /cpp/convert-images-format-to-pdf/
lastmod: "2021-11-19"
description: 이 주제는 Aspose.PDF for C++ 라이브러리가 다양한 이미지 형식을 PDF로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for C++**를 사용하면 다양한 형식의 이미지를 PDF 파일로 변환할 수 있습니다. 우리 라이브러리는 BMP, DICOM, EMF, JPG, PNG, SVG 및 TIFF 형식과 같은 가장 인기 있는 이미지 형식을 변환하기 위한 코드 스니펫을 제공합니다.

## BMP를 PDF로 변환

**Aspose.PDF for C++** 라이브러리를 사용하여 BMP 파일을 PDF 문서로 변환합니다.

<abbr title="Bitmap Image File">BMP</abbr> 이미지는 확장자를 가진 파일입니다. BMP는 비트맵 디지털 이미지를 저장하는 데 사용되는 비트맵 이미지 파일을 나타냅니다. 이러한 이미지는 그래픽 어댑터와 독립적이며 장치 독립 비트맵 (DIB) 파일 형식이라고도 합니다. Aspose.PDF for C++ API를 사용하여 BMP를 PDF 파일로 변환할 수 있습니다. 따라서 BMP 이미지를 변환하려면 다음 단계를 따를 수 있습니다:

1. 경로 이름과 파일 이름을 위한 [String 클래스](https://reference.aspose.com/pdf/cpp/class/system.string)를 생성합니다.
1. 새로운 Document 객체의 인스턴스를 생성합니다.
1. 이 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)에 새로운 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)를 추가합니다.
1. 새로운 Aspose.Pdf BMP를 생성합니다.
1. 입력 파일을 사용하여 Aspose.PDF BMP 객체를 초기화합니다.
1. Aspose.PDF BMP를 페이지에 단락으로 추가합니다.
1. 마지막으로 출력 PDF 파일을 저장합니다.

따라서 다음 코드 스니펫은 이러한 단계를 따르며 C++를 사용하여 BMP를 PDF로 변환하는 방법을 보여줍니다:

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
**BMP를 PDF로 온라인 변환 시도**

Aspose는 당신이 기능과 품질을 조사해 볼 수 있는 온라인 무료 애플리케이션 ["BMP to PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)을 제공합니다.

[![Aspose.PDF Convertion BMP to PDF using Free App](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## DICOM을 PDF로 변환

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> 형식은 디지털 의료 이미지와 검토된 환자의 문서의 생성, 저장, 전송 및 시각화를 위한 의료 산업 표준입니다.

**Aspose.PDF for C++**는 DICOM 및 SVG 이미지를 변환할 수 있지만, 기술적인 이유로 이미지를 추가하기 위해 PDF에 추가할 파일의 유형을 지정해야 합니다:

1. 경로 이름과 파일 이름을 위한 [String Class](https://reference.aspose.com/pdf/cpp/class/system.string)를 생성합니다.
1. Instantiate [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체.
1. 문서의 페이지 컬렉션에 [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)를 추가합니다.
1. Aspose.PDF TDicom이 페이지에 단락으로 추가됩니다.
1. 입력 이미지 파일을 로드하고 [저장](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa)합니다.

다음 코드 스니펫은 Aspose.PDF를 사용하여 DICOM 파일을 PDF 형식으로 변환하는 방법을 보여줍니다. DICOM 이미지를 로드하고, PDF 파일의 페이지에 이미지를 배치하고, 출력을 PDF로 저장해야 합니다.

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
**DICOM을 PDF로 온라인 변환 시도**

Aspose는 당신이 기능과 품질을 조사해볼 수 있는 온라인 무료 애플리케이션 ["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)을 제공합니다.

[![Aspose.PDF Convertion DICOM to PDF using Free App](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## EMF를 PDF로 변환

<abbr title="Enhanced metafile format">EMF</abbr>EMF는 독립적으로 그래픽 이미지를 저장합니다. EMF의 메타파일은 순서대로 변동 길이의 기록들을 포함하며, 어떤 출력 장치에서도 파싱 후 저장된 이미지를 렌더링할 수 있습니다. 또한 아래의 단계를 사용하여 EMF를 PDF 이미지로 변환할 수 있습니다:

1. 경로 이름과 파일 이름에 대한 [String Class](https://reference.aspose.com/pdf/cpp/class/system.string)를 생성합니다.
1. 새로운 Document 객체의 인스턴스를 생성합니다.
1. 이 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)에 새 페이지를 추가합니다.
1. A new Aspose.Pdf TIFF is created.  
1. Aspose.PDF TIFF 객체는 입력 파일을 사용하여 초기화됩니다.  
1. Aspose.PDF TIFF가 문단으로 페이지에 추가됩니다.  
1. 입력 이미지 파일을 로드하고 [저장](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa)합니다.

Moreover, the following code snippet shows how to convert an EMF to PDF with C++ in your code snippet:

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
**EMF를 PDF로 온라인으로 변환해보세요**

Aspose는 온라인 무료 애플리케이션 ["EMF to PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/)을 제공합니다. 여기서 기능과 품질을 조사해보세요.

[![Aspose.PDF 변환 EMF를 PDF로 무료 앱 사용](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## JPG를 PDF로 변환

JPG를 PDF로 변환하는 방법을 궁금해할 필요가 없습니다, 왜냐하면 **Aspose.PDF for C++** 라이브러리가 최고의 해결책을 제공합니다.

다음 단계를 따르면 Aspose.PDF for C++로 JPG 이미지를 매우 쉽게 PDF로 변환할 수 있습니다:

1. 경로 이름과 파일 이름을 위한 [String Class](https://reference.aspose.com/pdf/cpp/class/system.string)를 만듭니다.
1. 새로운 Document 객체의 인스턴스가 생성됩니다.
1. 이 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)에 새로운 페이지를 추가합니다.
1. 새로운 Aspose::Pdf::Image가 생성됩니다.
1. Aspose.PDF 이미지 객체가 입력 파일을 사용하여 초기화됩니다.
1. Aspose.PDF 이미지가 페이지에 단락으로 추가됩니다.  
1. 입력 이미지 파일을 로드하고 저장합니다.

아래 코드 스니펫은 C++를 사용하여 JPG 이미지를 PDF로 변환하는 방법을 보여줍니다:

```cpp
void ConvertJPEGtoPDF() 
{
    std::clog << "JPEG to PDF convert: Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Conversion\\");

    // 입력 파일 이름을 위한 문자열
    String infilename("sample.jpg");

    // 출력 파일 이름을 위한 문자열
    String outfilename("ImageToPDF-JPEG.pdf");

    // 문서 열기
    auto document = MakeObject<Document>();

    // 빈 문서에 빈 페이지 추가
    auto page = document->get_Pages()->Add();
    auto image = MakeObject<Aspose::Pdf::Image>();
    image->set_File(_dataDir + infilename);

    // 페이지에 이미지 추가
    page->get_Paragraphs()->Add(image);

    // 출력 문서 저장
    document->Save(_dataDir + outfilename);
    std::clog << "JPEG to PDF convert: Finish" << std::endl;
}
```

그 다음, **페이지의 동일한 높이와 너비**로 이미지를 PDF로 변환하는 방법을 볼 수 있습니다. We will be getting the image dimensions and accordingly set the page dimensions of PDF document with the below steps:

이미지의 크기를 가져오고 다음 단계에 따라 PDF 문서의 페이지 크기를 설정합니다:

1. Load input image file
1. 입력 이미지 파일을 로드합니다
1. Get the height and width of the image
1. 이미지의 높이와 너비를 가져옵니다
1. Set height, width, and margins of a page
1. 페이지의 높이, 너비 및 여백을 설정합니다
1. Save the output PDF file
1. 출력 PDF 파일을 저장합니다

Following code snippet shows how to convert an Image to PDF with same page height and width using C++:

다음 코드 스니펫은 C++를 사용하여 동일한 페이지 높이와 너비로 이미지를 PDF로 변환하는 방법을 보여줍니다:

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
**JPG를 PDF로 온라인 변환 시도**

Aspose는 ["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)라는 무료 온라인 애플리케이션을 제공하여 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF Convertion JPG to PDF using Free App](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## PNG를 PDF로 변환

**Aspose.PDF for C++**는 PNG 이미지를 PDF 형식으로 변환하는 기능을 지원합니다. 작업을 실현하기 위한 다음 코드 스니펫을 확인하세요.

<abbr title="Portable Network Graphics">PNG</abbr>는 손실 없는 압축을 사용하는 래스터 이미지 파일 형식을 의미하며, 이는 사용자들 사이에서 인기가 많습니다.

아래 단계에 따라 PNG를 PDF 이미지로 변환할 수 있습니다:

1. 경로 이름 및 파일 이름을 위한 [String Class](https://reference.aspose.com/pdf/cpp/class/system.string)를 생성합니다.
1. 새 Document 객체의 인스턴스가 생성됩니다.
1. 새 페이지를 이 [문서](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)에 추가합니다.
1. 새로운 Aspose.Pdf PNG가 생성됩니다.
1. Aspose.PDF PNG 객체는 입력 파일을 사용하여 초기화됩니다.
1. Aspose.PDF PNG가 페이지에 문단으로 추가됩니다.
1. 입력 이미지 파일을 로드하고 저장합니다.

또한, 아래 코드 스니펫은 C++ 애플리케이션에서 PNG를 PDF로 변환하는 방법을 보여줍니다:

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
**PNG를 PDF로 온라인으로 변환해보세요**

Aspose는 온라인 무료 애플리케이션 ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/)을 제공합니다. 여기서 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF Convertion PNG to PDF using Free App](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## SVG를 PDF로 변환

**Aspose.PDF for C++**는 SVG 이미지를 PDF 형식으로 변환하는 방법과 원본 <abbr title="Scalable Vector Graphics">SVG</abbr> 파일의 치수를 얻는 방법을 설명합니다.

Scalable Vector Graphics (SVG)는 2차원 벡터 그래픽에 대한 XML 기반 파일 형식의 사양 가족으로, 정적 및 동적(대화형 또는 애니메이션) 그래픽을 포함합니다. SVG 사양은 1999년부터 월드 와이드 웹 컨소시엄(W3C)에 의해 개발된 오픈 표준입니다.

SVG 이미지와 그 동작은 XML 텍스트 파일로 정의됩니다. 이는 검색, 인덱싱, 스크립팅이 가능하며 필요시 압축할 수도 있습니다. XML 파일로서, SVG 이미지는 모든 텍스트 편집기로 생성 및 편집할 수 있지만, Inkscape와 같은 드로잉 프로그램으로 생성하는 것이 더 편리할 수 있습니다.

1. 경로 이름 및 파일 이름에 대한 [String 클래스](https://reference.aspose.com/pdf/cpp/class/system.string)를 생성합니다.
1. [`SvgLoadOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.svg_load_options) 클래스의 인스턴스를 생성합니다.
1. 소스 파일 이름과 옵션을 지정하여 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스의 인스턴스를 생성합니다.
1. 원하는 파일 이름으로 문서를 저장합니다.

다음 코드 스니펫은 Aspose.PDF for C++를 사용하여 SVG 파일을 PDF 형식으로 변환하는 과정을 보여줍니다.

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
고급 기능을 갖춘 예제를 고려하십시오:

```cpp
void ConvertSVGtoPDF_Advanced()
{
    std::clog << "SVG to PDF 변환: 시작" << std::endl;

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

    std::clog << "SVG to PDF 변환: 완료" << std::endl;
}
```

{{% alert color="success" %}}
**SVG 형식을 PDF로 온라인 변환 시도**


Aspose.PDF for C++는 ["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf)라는 무료 온라인 애플리케이션을 제공하여 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF Convertion SVG to PDF with Free App](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

## TIFF를 PDF로 변환

**Aspose.PDF** 파일 형식이 지원되며, 단일 프레임 또는 다중 프레임 <abbr title="Tag Image File Format">TIFF</abbr> 이미지 모두 가능합니다. 이는 C++ 애플리케이션에서 TIFF 이미지를 PDF로 변환할 수 있음을 의미합니다.

TIFF 또는 TIF, Tagged Image File Format은 이 파일 형식 표준을 준수하는 다양한 장치에서 사용하기 위한 래스터 이미지를 나타냅니다. TIFF 이미지는 서로 다른 이미지의 여러 프레임을 포함할 수 있습니다. Aspose.PDF 파일 형식도 지원되며, 단일 프레임 또는 다중 프레임 TIFF 이미지 모두 가능합니다. 따라서 C++ 애플리케이션에서 TIFF 이미지를 PDF로 변환할 수 있습니다. 따라서 다중 페이지 TIFF 이미지를 다중 페이지 PDF 문서로 변환하는 예제를 아래 단계로 살펴보겠습니다:

1. 경로 이름과 파일 이름에 대한 [String Class](https://reference.aspose.com/pdf/cpp/class/system.string)를 만듭니다.
1. 새로운 Document 객체의 인스턴스가 생성됩니다.
1. 이 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)에 새 페이지를 추가합니다.
1. 새로운 Aspose.Pdf TIFF가 생성됩니다.
1. 입력 파일을 사용하여 Aspose.PDF TIFF 객체가 초기화됩니다.
1. Aspose.PDF TIFF가 페이지에 단락으로 추가됩니다.
1. 입력 이미지 파일을 로드하고 저장합니다.

또한, 다음 코드 스니펫은 멀티 페이지 또는 멀티 프레임 TIFF 이미지를 C++로 PDF로 변환하는 방법을 보여줍니다:

```cpp
void ConvertTIFFtoPDF() 
{
    std::clog << "TIFF to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.tiff");
    String outfilename("ImageToPDF-TIFF.pdf");

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

    std::clog << "TIFF to PDF convert: Finish" << std::endl;
}
```