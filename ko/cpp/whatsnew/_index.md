---
title: C++의 새로운 기능
linktitle: 새로운 기능
type: docs
weight: 10
url: /ko/cpp/whatsnew/
description: 이 페이지는 최근 릴리스에서 소개된 Aspose.PDF for C++의 가장 인기 있는 새로운 기능을 소개합니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-12-22"
---

## Aspose.PDF 24.8의 새로운 기능

페이지에 SVG 이미지를 추가할 수 있는 기능.

## Aspose.PDF 24.4의 새로운 기능

SVG 이미지 로딩 문제 수정.

## Aspose.PDF 24.3의 새로운 기능

PDF 문서를 다른 형식으로 변환할 때 메모리 누수를 수정했습니다.

## Aspose.PDF 24.2의 새로운 기능

24.2부터 구현되었습니다:

- JPXDecoder 성능이 향상되었습니다.

- 구조가 손상된 문서를 읽는 문제를 수정했습니다.

## Aspose.PDF 23.7의 새로운 기능

- PDF 문서를 EPUB 형식으로 저장하는 기능이 도입되었습니다:

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

- PCL 형식 파일을 로드하는 기능이 구현되었습니다:

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
            Console::WriteLine(u"오류: {0}", error->get_Message());
            return 1;
        }
        catch (const std::exception& error)
        {
            std::cerr << "오류: " << error.what() << std::endl;
            return 1;
        }

        return 0;
    }
```

## Aspose.PDF 23.1의 새로운 기능

23.1부터 Dicom 형식 이미지 지원이 추가되었습니다:

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

## Aspose.PDF 22.11의 새로운 기능

22.11부터 **Aspose.PDF for C++ macOS**의 첫 공개 릴리스를 발표했습니다.

Aspose.PDF for C++ macOS의 첫 공개 릴리스를 발표하게 되어 기쁩니다. Aspose.PDF for C++ macOS는 개발자가 Adobe Acrobat을 사용하지 않고 PDF 문서를 생성하고 조작할 수 있도록 하는 독점 C++ 라이브러리입니다. Aspose.PDF for C++ macOS는 개발자가 양식을 생성하고, 텍스트를 추가/편집하고, PDF 페이지를 조작하고, 주석을 추가하고, 사용자 지정 폰트를 처리하는 등의 작업을 할 수 있도록 합니다.

## Aspose.PDF 22.5의 새로운 기능

PDF 문서에서 XFA 양식의 지원이 구현되었습니다.

## Aspose.PDF 22.4의 새로운 기능

C++용 Aspose.PDF의 새 버전은 Aspose.PDF for .Net 22.4 및 Aspose.Imaging 22.4의 코드베이스를 가지고 있습니다.

- System::Drawing::GetThumbnailImage() 메서드가 구현되었습니다;
- RegionDataNodeRect 생성자가 최적화되었습니다;
- 1비트당 픽셀 흑백 이미지 로딩이 수정되었습니다.

## Aspose.PDF 22.3의 새로운 기능

여러 클래스에 메서드 오버로드가 추가되었습니다. 이러한 지원은 이전에 ArrayPtr만 지원되었던 곳에서 ArrayView-타입의 매개변수를 지원합니다.

## Aspose.PDF 22.1의 새로운 기능

C++용 Aspose.PDF의 새 버전은 Aspose.PDF for .Net 22.1의 코드베이스를 가지고 있습니다:

- System::Xml에 대한 새로운 구현이 제공되었습니다. 이전에는 libxml2 및 libxslt 라이브러리를 기반으로 한 사용자 정의 구현이 있었습니다. 새 버전은 포팅된 CoreFX 코드를 기반으로 합니다.

- double-conversion 라이브러리가 3.1.7 버전으로 업그레이드되었습니다.

- Dll 파일은 Aspose 인증서로 서명되었습니다.

## Aspose.PDF 21.10의 새로운 기능

### C++용 Aspose.PDF는 SVG를 PDF 형식으로 변환하는 기능을 지원합니다

다음 코드 스니펫은 C++용 Aspose.PDF를 사용하여 SVG 파일을 PDF 형식으로 변환하는 과정을 보여줍니다.

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
문서의 고급 기능 예시를 고려해보세요:

```cpp

    void ConvertSVGtoPDF_Advanced()
    {
        std::clog << "SVG to PDF 변환: 시작" << std::endl;

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

        std::clog << "SVG to PDF 변환: 종료" << std::endl;
    }
```

## Aspose.PDF 21.4의 새로운 기능

### PDF 문서를 HTML 형식으로 저장하는 기능이 구현되었습니다

Aspose.PDF for C++는 PDF 파일을 HTML로 변환하는 기능을 지원합니다.

```cpp

    int main()
    {
        auto doc = MakeObject<Document>(u"e:\\sample.pdf");
        doc->Save(u"e:\\sample.html", SaveFormat::Html);
    }
```