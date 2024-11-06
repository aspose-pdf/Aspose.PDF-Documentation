---
linktitle: 다른 파일 형식을 PDF로 변환
type: docs
weight: 80
url: ko/cpp/convert-other-files-to-pdf/
lastmod: "2021-11-19"
description: 이 주제는 Aspose.PDF가 다른 파일 형식을 PDF 문서로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## EPUB을 PDF로 변환

**Aspose.PDF for C++**는 EPUB 파일을 PDF 형식으로 간단히 변환할 수 있게 합니다.

<abbr title="electronic publication">EPUB</abbr> (전자 출판의 약자)은 International Digital Publishing Forum (IDPF)에서 제공하는 무료 오픈 전자책 표준입니다. 파일 확장자는 .epub입니다. EPUB은 리플로우 가능한 콘텐츠를 위해 설계되었으며, 이는 EPUB 리더가 특정 디스플레이 장치에 맞춰 텍스트를 최적화할 수 있음을 의미합니다.

EPUB은 고정 레이아웃 콘텐츠도 지원합니다. 형식은 발행자와 변환 회사가 내부적으로 사용할 수 있을 뿐만 아니라 배포 및 판매를 위해 사용할 수 있는 단일 형식으로 의도되었습니다. 이는 Open eBook 표준을 대체합니다. EPUB 3 버전은 또한 콘텐츠 패키징을 위한 표준화된 모범 사례, 연구, 정보 및 행사에 대한 주요 도서 무역 협회인 Book Industry Study Group (BISG)의 승인을 받았습니다.

변환 단계:

1. 경로 이름 및 파일 이름을 위한 [String Class](https://reference.aspose.com/pdf/cpp/class/system.string)를 생성합니다.
1. [EpubLoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options) 클래스의 인스턴스를 생성합니다.
1. 소스 파일 이름과 옵션을 언급한 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스의 인스턴스를 생성합니다.
1. 입력 파일을 로드하고 [저장](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa)합니다.

다음 코드 스니펫은 C++로 EPUB 파일을 PDF 형식으로 변환하는 방법을 보여줍니다.

```cpp
void ConvertEPUBtoPDF()
{
    std::clog << "EPUB to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("aliceDynamic.epub");
    String outfilename("epub_test.pdf");
    auto options = MakeObject<EpubLoadOptions>();
    try {
    auto document = MakeObject<Document>(_dataDir + infilename, options);
    document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << "EPUB to PDF convert: End" << std::endl;
}
```
{{% alert color="success" %}}
**EPUB을 PDF로 온라인 변환 시도**

Aspose.PDF for C++는 온라인 무료 애플리케이션 ["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf)를 제공하여 기능과 품질을 조사할 수 있습니다.

[![Aspose.PDF Convertion EPUB to PDF with Free App](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## 텍스트를 PDF로 변환

**Aspose.PDF for C++**는 일반 텍스트 및 사전 형식화된 텍스트 파일을 PDF 형식으로 변환하는 기능을 지원합니다.

텍스트를 PDF로 변환하는 것은 PDF 페이지에 텍스트 조각을 추가하는 것을 의미합니다. 텍스트 파일의 경우, 우리는 사전 형식화된 텍스트(예: 80자의 25줄)와 비형식화된 텍스트(일반 텍스트) 두 가지 유형의 텍스트를 다룹니다. 우리의 필요에 따라, 우리는 이 추가를 스스로 제어할 수 있거나 라이브러리의 알고리즘에 맡길 수 있습니다.

### 일반 텍스트 파일을 PDF로 변환

일반 텍스트 파일의 경우, 다음 기술을 사용할 수 있습니다:

1. 문자열 클래스](https://reference.aspose.com/pdf/cpp/class/system.string)를 경로 이름 및 파일 이름으로 만듭니다.
1. [TextReader](https://reference.aspose.com/pdf/cpp/class/system.i_o.text_reader/.)를 사용하여 소스 텍스트 파일을 읽습니다.
1. [문서](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 개체를 인스턴스화합니다.
1. 문서의 페이지 컬렉션에 [페이지](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)를 추가합니다.
1. TextFragment의 새 개체를 생성하고 TextReader 개체를 생성자에 전달합니다.
1. 단락 컬렉션에 새 텍스트 단락을 추가하고 TextFragment 개체를 전달합니다.
1. 입력 파일을 로드하고 [저장](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa)합니다.

```cpp
void ConvertTextToPDF()
{
    std::clog << "텍스트를 PDF로 변환: 시작" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.txt");
    String outfilename("TextToPDF.pdf");

    // 소스 텍스트 파일 읽기
    String content = System::IO::File::ReadAllText(_dataDir + infilename);

    // 빈 생성자를 호출하여 문서 개체를 인스턴스화합니다.
    auto document = MakeObject<Document>();

    // 문서의 페이지 컬렉션에 새 페이지를 추가합니다.
    auto page = document->get_Pages()->Add();

    // TextFragmet 인스턴스를 생성하고 리더 개체에서 텍스트를 가져와 생성자의 인수로 전달합니다.
    auto text = MakeObject<TextFragment>(content);

    // 단락 컬렉션에 새 텍스트 단락을 추가하고 TextFragment 개체를 전달합니다.
    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // 결과 PDF 파일 저장
    document->Save(_dataDir + outfilename);
    std::clog << "텍스트를 PDF로 변환: 종료" << std::endl;
}
```
### 사전 포맷된 텍스트 파일을 PDF로 변환

사전 포맷된 텍스트로 변환하는 것은 일반 텍스트와 비슷하지만 여백 설정, 글꼴 유형 및 크기 설정과 같은 추가 작업이 필요합니다. 당연히 글꼴은 모노스페이스여야 합니다(예: Courier New).

C++로 사전 포맷된 텍스트를 PDF로 변환하려면 다음 단계를 따르세요:

1. 빈 생성자를 호출하여 Document 객체를 인스턴스화합니다.
1. 더 나은 표현을 위해 좌우 여백을 설정합니다.
1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체를 인스턴스화하고 Pages 컬렉션에 새 페이지를 추가합니다.
1. 입력 이미지 파일을 로드하고 [저장](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa)합니다.

```CPP
void ConvertPreFormattedTextToPdf()
{
    std::clog << "Performatted Text to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("rfc822.txt");
    String outfilename("TextToPDF.pdf");
    // 텍스트 파일을 문자열 배열로 읽습니다
    auto lines = System::IO::File::ReadAllLines(_dataDir + infilename);

    // 빈 생성자를 호출하여 Document 객체를 인스턴스화합니다
    auto document = MakeObject<Document>();

    // Document의 Pages 컬렉션에 새 페이지를 추가합니다
    auto page = document->get_Pages()->Add();

    // 더 나은 표현을 위해 좌우 여백을 설정합니다
    page->get_PageInfo()->get_Margin()->set_Left(20);
    page->get_PageInfo()->get_Margin()->set_Right(10);
    page->get_PageInfo()->get_DefaultTextState()->set_Font(FontRepository::FindFont(u"Courier New"));
    page->get_PageInfo()->get_DefaultTextState()->set_FontSize(12);

    for (int index = 0; index < lines->get_Length(); index++)
    {
        // 줄에 "form feed" 문자가 포함되어 있는지 확인합니다
        // https://en.wikipedia.org/wiki/Page_break 참조
        auto line = lines->idx_get(index);
        if (line.StartsWith(u"\x0c"))
        {
        if (document->get_Pages()->get_Count() > 3) break;
        page = document->get_Pages()->Add();
        // 더 나은 표현을 위해 좌우 여백을 설정합니다
        page->get_PageInfo()->get_Margin()->set_Left(20);
        page->get_PageInfo()->get_Margin()->set_Right(10);
        page->get_PageInfo()->get_DefaultTextState()->set_Font(FontRepository::FindFont(u"Courier New"));
        page->get_PageInfo()->get_DefaultTextState()->set_FontSize(12);
        }
        else
        {
        // TextFragment의 인스턴스를 생성하고
        // 줄을 인수로 전달하여 생성자에 전달합니다
        auto text = MakeObject<TextFragment>(line);

        // 단락 컬렉션에 새 텍스트 단락을 추가하고 TextFragment 객체를 전달합니다
        page->get_Paragraphs()->Add(text);
        }
    }

    // 결과 PDF 파일을 저장합니다
    document->Save(_dataDir + outfilename);
    std::clog << "Performatted Text to PDF convert: End" << std::endl;
}
```

{{% alert color="success" %}}
**TEXT를 PDF로 온라인으로 변환해보세요**

Aspose.PDF for C++는 ["Text to PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf)라는 무료 온라인 애플리케이션을 제공합니다. 여기서 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF Convertion TEXT to PDF with Free App](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

## XPS를 PDF로 변환하기

**Aspose.PDF for C++**는 <abbr title="XML Paper Specification">XPS</abbr> 파일을 PDF 형식으로 변환하는 기능을 지원합니다. 이 기사를 통해 작업을 해결하세요.

XPS 파일 형식은 주로 Microsoft Corporation의 XML Paper Specification과 관련이 있습니다. XML Paper Specification (XPS)은 이전에 Metro라는 코드명으로 불렸으며 차세대 인쇄 경로(NGPP) 마케팅 개념을 포함하여 문서 생성 및 보기를 Windows 운영 체제에 통합하려는 Microsoft의 이니셔티브입니다.

{{% alert color="primary" %}}

파일 형식은 기본적으로 배포 및 저장에 주로 사용되는 압축 XML 파일입니다. 편집하기 매우 어렵고 주로 Microsoft에 의해 구현됩니다.

{{% /alert %}}

Aspose.PDF for C++로 XPS를 PDF로 변환하기 위해, [XpsLoadOption](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options)이라는 클래스를 도입하였습니다. 이 클래스는 [LoadOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options) 객체를 초기화하는 데 사용됩니다. 이후 이 객체는 Document 객체 초기화 시 인수로 전달되며, PDF 렌더링 엔진이 원본 문서의 입력 형식을 결정하는 데 도움을 줍니다.

다음 코드 스니펫은 C++로 XPS 파일을 PDF 형식으로 변환하는 과정을 보여줍니다.

```cpp
void ConvertXPStoPDF()
{
    std::clog << "XPS to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.oxps");
    String outfilename("XPStoPDF.pdf");
    auto options = MakeObject<XpsLoadOptions>();
    try {
        auto document = MakeObject<Document>(_dataDir + infilename, options);
        document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
        std::cerr << ex->get_Message() << std::endl;
    };
    std::clog << "XPS to PDF convert: Finish" << std::endl;
}
```
{{% alert color="success" %}}
**XPS 형식을 PDF로 온라인 변환 시도하기**

Aspose.PDF for C++는 온라인 무료 애플리케이션 ["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/)를 제공하여 기능과 품질을 조사할 수 있습니다.

[![Aspose.PDF 변환 XPS to PDF 무료 앱](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## XML을 PDF로 변환

XML 형식은 구조화된 데이터를 저장하는 데 사용됩니다. Aspose.PDF에서 <abbr title="Extensible Markup Language">XML</abbr>을 PDF로 변환하는 몇 가지 방법이 있습니다.

## XSL-FO를 PDF로 변환

1. 경로 이름과 파일 이름에 대한 [String Class](https://reference.aspose.com/pdf/cpp/class/system.string)를 생성합니다.
1. [XslFoLoadOption 객체](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.load_options)를 인스턴스화합니다.
1. 오류 처리 전략을 설정합니다.
1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체를 인스턴스화합니다.
1. [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) 입력 이미지 파일을 저장합니다.

```cpp
void Convert_XSLFO_to_PDF()
{
    std::clog << "XSL-FO to PDF 변환: 시작" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilenameXSL("c:\\samples\\employees.xslt");
    String infilenameXML("c:\\samples\\employees.xml");

     String outfilename("XMLFOtoPDF.pdf");
    // XslFoLoadOption 객체 인스턴스화
    auto options = new XslFoLoadOptions(infilenameXSL);
    // 오류 처리 전략 설정
    options->ParsingErrorsHandlingType = XslFoLoadOptions::ParsingErrorsHandlingTypes::ThrowExceptionImmediately;
    // Document 객체 생성
    auto document = MakeObject<Document>(infilenameXML, options);
    document->Save(_dataDir + outfilename);
}
```

{{% alert color="success" %}}
**온라인에서 XML을 PDF로 변환해보세요**

Aspose.PDF for C++는 ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf)라는 무료 온라인 애플리케이션을 제공하며, 여기서 기능과 품질을 조사해볼 수 있습니다.
[![Aspose.PDF 변환 XML에서 PDF로 무료 앱](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}