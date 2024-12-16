---
title: 모든 PDF 페이지에서 텍스트 추출하기 C++ 사용
linktitle: PDF에서 텍스트 추출하기
type: docs
weight: 10
url: /ko/cpp/extract-text-from-all-pdf/
description: 이 문서는 Aspose.PDF를 사용하여 C++에서 PDF 문서에서 텍스트를 추출하는 다양한 방법을 설명합니다. 전체 페이지, 특정 부분, 열 기반 등.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서의 모든 페이지에서 텍스트 추출하기

PDF 문서에서 텍스트를 추출하는 것은 일반적인 요구 사항입니다. 이 예제에서는 Aspose.PDF for C++가 PDF 문서의 모든 페이지에서 텍스트를 추출하는 방법을 보여줍니다. [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) 클래스의 객체를 생성해야 합니다. 그런 다음 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스를 사용하여 PDF를 열고 [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 컬렉션의 'Accept' 메서드를 호출합니다. [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) 클래스는 문서에서 텍스트를 흡수하고 'Text' 속성에 반환합니다. 다음 코드 스니펫은 PDF 문서의 모든 페이지에서 텍스트를 추출하는 방법을 보여줍니다.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ExtractTextFromAllThePages() {

    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Parsing\\");

    // String for file name
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Create TextAbsorber object to extract text
    auto textAbsorber = MakeObject<TextAbsorber>();
    // Accept the absorber for all the pages
    document->get_Pages()->Accept(textAbsorber);
    // Get the extracted text
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
문서 객체의 특정 페이지에서 **Accept** 메서드를 호출합니다. Index는 텍스트를 추출해야 하는 특정 페이지 번호입니다.

```cpp
void ExtractTextFromParticularPage() {

    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Parsing\\");

    // 파일 이름을 위한 문자열
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 텍스트 추출을 위한 TextAbsorber 객체 생성
    auto textAbsorber = MakeObject<TextAbsorber>();
    // 모든 페이지에 대해 흡수기를 허용
    document->get_Pages()->idx_get(1)->Accept(textAbsorber);
    // 추출된 텍스트 가져오기
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## 텍스트 디바이스를 사용하여 페이지에서 텍스트 추출

PDF 파일에서 텍스트를 추출하기 위해 [TextDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.text_device/) 클래스를 사용할 수 있습니다. TextDevice는 구현에서 TextAbsorber를 사용하므로 사실상 동일한 작업을 수행하지만 TextDevice는 페이지에서 이미지, 페이지 등을 추출하기 위한 "Device" 접근 방식을 통합하기 위해 구현되었습니다. TextAbsorber는 페이지, 전체 PDF 또는 XForm에서 텍스트를 추출할 수 있으며, 이 TextAbsorber는 더 범용적입니다.

### 모든 페이지에서 텍스트 추출

다음 단계 및 코드 스니펫은 텍스트 장치를 사용하여 PDF에서 텍스트를 추출하는 방법을 보여줍니다.

1. 입력 PDF 파일을 지정하여 Document 클래스의 객체 생성
1. TextDevice 클래스의 객체 생성
1. TextExtractOptions 클래스의 객체를 사용하여 추출 옵션 지정
1. TextDevice 클래스의 Process 메서드를 사용하여 콘텐츠를 텍스트로 변환
1. 텍스트를 출력 파일에 저장
## 특정 페이지 영역에서 텍스트 추출

[TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) 클래스는 PDF 문서의 특정 페이지 또는 모든 페이지에서 텍스트를 추출할 수 있는 기능을 제공합니다. 이 클래스는 추출된 텍스트를 'Text' 속성으로 반환합니다. 그러나 특정 페이지 영역에서 텍스트를 추출해야 하는 경우, [TextSearchOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_search_options/)의 **Rectangle** 속성을 사용할 수 있습니다. Rectangle 속성은 Rectangle 객체를 값으로 받아 이 속성을 사용하여 텍스트를 추출해야 하는 페이지의 영역을 지정할 수 있습니다.

텍스트를 추출하기 위해 페이지의 **Accept** 메서드를 호출합니다. 객체를 생성하십시오 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) 및 [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) 클래스. 'Accept' 메서드를 [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) 객체의 개별 페이지, 즉 **Page** Index에서 호출합니다. **Index**는 텍스트를 추출해야 하는 특정 페이지 번호입니다. [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) 클래스의 'Text' 속성에서 텍스트를 얻을 수 있습니다. 다음 코드 스니펫은 개별 페이지에서 텍스트를 추출하는 방법을 보여줍니다.

```cpp
void ExtractTextFromParticularPageRegion() {

    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름에 대한 문자열
    String _dataDir("C:\\Samples\\Parsing\\");

    // 파일 이름에 대한 문자열
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 텍스트 추출을 위한 TextAbsorber 객체 생성
    auto textAbsorber = MakeObject<TextAbsorber>();
    textAbsorber->get_TextSearchOptions()->set_LimitToPageBounds(true);
    textAbsorber->get_TextSearchOptions()->set_Rectangle(MakeObject<Rectangle>(100, 200, 250, 350));

    // 모든 페이지에 대해 흡수기 허용
    document->get_Pages()->idx_get(1)->Accept(textAbsorber);
    // 추출된 텍스트 가져오기
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;

}
```
## 열을 기준으로 텍스트 추출

PDF는 매우 인기 있는 형식이며 그럴만한 이유가 있습니다. PDF를 사용하면 문서가 다른 컴퓨터에서도 동일한 방식으로 표시되고 인쇄될 것이라고 거의 확신할 수 있습니다.

그러나 PDF 문서는 일반적으로 단락, 표, 그림, 헤더/푸터 정보 등에 어떤 콘텐츠가 있는지에 대한 정보가 부족하다는 단점이 있습니다.

Aspose.PDF for C++ - 열을 기준으로 텍스트를 추출할 수 있는 사용하기 쉬운 유틸리티입니다.

```cpp
void ExtractTextBasedOnColumns() {

    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Parsing\\");

    // 파일 이름을 위한 문자열
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 텍스트 추출을 위한 TextAbsorber 객체 생성
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>();


    // 모든 페이지에 대해 흡수기 수락
    document->get_Pages()->Accept(textFragmentAbsorber);

    auto tfc = textFragmentAbsorber->get_TextFragments();
    for (auto tf : tfc)
    {
        // 폰트 크기를 최소 70% 줄여야 합니다.
        auto size = tf->get_TextState()->get_FontSize() * 0.7f;
        tf->get_TextState()->set_FontSize(size);
    }
    auto stream = MakeObject<System::IO::MemoryStream>();
    document->Save(stream);
    document = MakeObject<Document>(stream);
    auto textAbsorber = MakeObject<TextAbsorber>();
    document->get_Pages()->Accept(textAbsorber);
    String extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### 두 번째 접근 방식 - ScaleFactor 사용

이 새로운 릴리스에서는 TextAbsorber와 내부 텍스트 형식화 메커니즘의 여러 개선 사항도 도입했습니다. 따라서 'Pure' 모드를 사용한 텍스트 추출 중에 [ScaleFactor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_extraction_options#a4f9a173765d483b493c31e416f8b035a) 옵션을 지정할 수 있으며, 이는 위에서 언급한 접근 방식 외에 다중 열 PDF 문서에서 텍스트를 추출하는 또 다른 방법이 될 수 있습니다. 이 스케일 팩터는 텍스트 추출 중 내부 텍스트 형식화 메커니즘에 사용되는 그리드를 조정하기 위해 설정할 수 있습니다. 1에서 0.1(0.1 포함) 사이의 ScaleFactor 값을 지정하면 글꼴 축소와 동일한 효과를 줍니다.

0.1에서 -0.1 사이의 ScaleFactor 값을 지정하면 0 값으로 처리되지만, 텍스트 추출 중에 필요한 스케일 팩터를 자동으로 계산하도록 알고리즘을 만듭니다. 계산은 페이지에서 가장 인기 있는 글꼴의 평균 글리프 너비를 기반으로 하지만, 추출된 텍스트에서 열의 시작 부분에 다음 열이 도달하지 않는다는 것을 보장할 수 없습니다. ScaleFactor 값이 지정되지 않으면 기본 값 1.0이 사용됩니다. 이는 스케일링이 수행되지 않음을 의미합니다. 지정된 ScaleFactor 값이 10보다 크거나 -0.1보다 작으면 기본 값 1.0이 사용됩니다.

대량의 PDF 파일에서 텍스트 내용을 추출할 때 자동 스케일링(ScaleFactor = 0)의 사용을 제안합니다. 또는 그리드 너비의 여유 감소를 수동으로 설정합니다(약 ScaleFactor = 0.5). 그러나 특정 문서에 대해 스케일링이 필요한지 여부를 결정해서는 안 됩니다. 문서에 대해 그리드 너비의 여유 감소를 설정하면(필요하지 않은 경우) 추출된 텍스트 내용은 완전히 적절하게 유지됩니다. 다음 코드 스니펫을 살펴보세요.

```cpp
void ExtractTextUsingScaleFactor() {

    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Parsing\\");

    // 파일 이름을 위한 문자열
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto textAbsorber = MakeObject<TextAbsorber>();
    textAbsorber->set_ExtractionOptions(MakeObject<TextExtractionOptions>(TextExtractionOptions::TextFormattingMode::Pure));
    // 대부분의 문서에서 열을 분할하기 위해 0.5의 스케일 팩터 설정이 충분합니다.
    // 0으로 설정하면 알고리즘이 스케일 팩터를 자동으로 선택할 수 있습니다.
    textAbsorber->get_ExtractionOptions()->set_ScaleFactor(0.5); /* 0; */
    document->get_Pages()->Accept(textAbsorber);
    String extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## PDF 문서에서 강조 표시된 텍스트 추출

PDF 문서에서 텍스트를 추출하는 다양한 시나리오에서 PDF 문서에서 강조 표시된 텍스트만 추출해야 하는 요구 사항이 있을 수 있습니다. 이 기능을 구현하기 위해 API에 TextMarkupAnnotation.GetMarkedText() 및 TextMarkupAnnotation.GetMarkedTextFragments() 메서드를 추가했습니다. TextMarkupAnnotation을 필터링하고 언급된 메서드를 사용하여 PDF 문서에서 강조 표시된 텍스트를 추출할 수 있습니다. 다음 코드 스니펫은 PDF 문서에서 강조 표시된 텍스트를 추출하는 방법을 보여줍니다.

```cpp
void ExtractHighlightedText() {

    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름에 대한 문자열
    String _dataDir("C:\\Samples\\Parsing\\");

    // 파일 이름에 대한 문자열
    String infilename("sample-highlight.pdf");
    String outfilename("extracted-text.txt");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + infilename);

    // 모든 주석을 반복
    for (auto annotation : document->get_Pages()->idx_get(1)->get_Annotations())
    {
        // TextMarkupAnnotation 필터링
        if (annotation->get_AnnotationType() == Aspose::Pdf::Annotations::AnnotationType::Highlight)
        {
        auto highlightedAnnotation = System::DynamicCast<Aspose::Pdf::Annotations::HighlightAnnotation>(annotation);

        // 강조 표시된 텍스트 조각 검색
        auto collection = highlightedAnnotation->GetMarkedTextFragments();
        for (auto tf : collection)
        {
            // 강조 표시된 텍스트 표시
            String s = tf->get_Text();
            std::cout << s << std::endl;
        }
        }
    }
}
```

## XML에서 텍스트 조각 및 세그먼트 요소에 접근하기

때때로 우리는 XML에서 생성된 PDF 문서를 처리할 때 TextFragement 또는 TextSegment 항목에 접근할 필요가 있습니다. Aspose.PDF for C++는 이름으로 이러한 항목에 접근할 수 있는 기능을 제공합니다. 아래 코드 스니펫은 이 기능을 사용하는 방법을 보여줍니다.

```cpp
void AccessTextFragmentandSegmentElementsXML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // 경로 이름을 위한 문자열
    String _dataDir("C:\\Samples\\Parsing\\");

    // 파일 이름을 위한 문자열
    String infilename("sample-doc.xml");
    String outfilename("sample-doc.pdf");

    auto document = MakeObject<Document>();
    document->BindXml(_dataDir + infilename);

    System::SharedPtr<Page> page = System::DynamicCast<Aspose::Pdf::Page>(document->GetObjectById(u"mainSection"));
    // 페이지와 몇 가지 작업 수행
    // ...

    System::SharedPtr<TextSegment> segment = System::DynamicCast<Aspose::Pdf::Text::TextSegment>(document->GetObjectById(u"product_description"));
    // 세그먼트와 몇 가지 작업 수행
    // ...
    document->Save(_dataDir + outfilename);

    std::clog << __func__ << ": Finish" << std::endl;
}
```