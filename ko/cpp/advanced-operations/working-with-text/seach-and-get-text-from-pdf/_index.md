---
title: PDF 문서의 페이지에서 텍스트 검색 및 가져오기
linktitle: 검색 및 텍스트 가져오기
type: docs
weight: 60
url: /ko/cpp/search-and-get-text-from-pdf/
description: 이 문서에서는 다양한 도구를 사용하여 PDF 문서에서 텍스트를 검색하고 가져오는 방법을 설명합니다. 특정 페이지나 전체 페이지에서 정규 표현식을 사용하여 검색할 수 있습니다.
lastmod: "2021-12-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF 문서의 모든 페이지에서 텍스트 검색 및 가져오기

[TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) 클래스는 PDF 문서의 모든 페이지에서 특정 구문과 일치하는 텍스트를 찾을 수 있게 해줍니다. 문서 전체에서 텍스트를 검색하려면 [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) 컬렉션의 Accept 메서드를 호출해야 합니다. 'Accept' 메서드는 TextFragmentAbsorber 객체를 매개변수로 받아, TextFragment 객체의 컬렉션을 반환합니다.

다음 코드 스니펫은 모든 페이지에서 텍스트를 검색하는 방법을 보여줍니다.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void SearchAndGetTextFromAllThePagesOfPDFDocument() {
    String _dataDir("C:\\Samples\\");

    auto document = new Document(_dataDir + u"sample.pdf");

    // 입력 검색 구문에 대한 모든 인스턴스를 찾기 위한 TextAbsorber 객체 생성
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("document");

    // 모든 페이지에 흡수기 수락
    document->get_Pages()->Accept(textFragmentAbsorber);

    // 수집된 텍스트 조각을 컬렉션으로 가져오기
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // 조각을 반복
    for (auto textFragment : textFragmentCollection) {
        Console::WriteLine(u"텍스트 :- {0}", textFragment->get_Text());
        Console::WriteLine(u"위치 :- {0}", textFragment->get_Position());
        Console::WriteLine(u"XIndent :- {0}", textFragment->get_Position()->get_XIndent());
        Console::WriteLine(u"YIndent :- {0}", textFragment->get_Position()->get_YIndent());
        Console::WriteLine(u"글꼴 - 이름 :- {0}", textFragment->get_TextState()->get_Font()->get_FontName());
        Console::WriteLine(u"글꼴 - 접근 가능 여부 :- {0}", textFragment->get_TextState()->get_Font()->get_IsAccessible());
        Console::WriteLine(u"글꼴 - 포함 여부 - {0}", textFragment->get_TextState()->get_Font()->get_IsEmbedded());
        Console::WriteLine(u"글꼴 - 부분 집합 여부 :- {0}", textFragment->get_TextState()->get_Font()->get_IsSubset());
        Console::WriteLine(u"글꼴 크기 :- {0}", textFragment->get_TextState()->get_FontSize());
        Console::WriteLine(u"전경색 :- {0}", textFragment->get_TextState()->get_ForegroundColor());
    }
}
```

## 정규 표현식을 사용하여 모든 페이지에서 텍스트 검색 및 가져오기

TextFragmentAbsorber는 정규 표현식을 기반으로 모든 페이지에서 텍스트를 검색하고 가져오는 데 도움을 줍니다. 먼저, 정규 표현식을 문구로 [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) 생성자에 전달해야 합니다. 그런 다음, TextFragmentAbsorber 객체의 [TextSearchOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_search_options/) 속성을 설정해야 합니다. 이 속성은 TextSearchOptions 객체를 필요로 하며 새 객체를 생성할 때 생성자에 매개변수로 true를 전달해야 합니다. 모든 페이지에서 일치하는 텍스트를 검색하려면 Pages 컬렉션의 Accept 메서드를 호출해야 합니다. [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/)는 정규 표현식으로 지정된 기준과 일치하는 모든 조각이 포함된 TextFragmentCollection을 반환합니다. 다음 코드 스니펫은 정규 표현식을 기반으로 모든 페이지에서 텍스트를 검색하고 가져오는 방법을 보여줍니다.

```cpp
void SearchAndGetTextFromPagesUsingRegularExpression()
{
    String _dataDir("C:\\Samples\\");

    auto document = new Document(_dataDir + u"sample.pdf");

    // 입력 검색 문구의 모든 인스턴스를 찾기 위한 TextAbsorber 객체 생성
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>(u"\\d{4}-\\d{4}"); // 예: 1999-2000

    // 정규 표현식 사용을 지정하기 위한 텍스트 검색 옵션 설정
    auto textSearchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // 문서의 첫 번째 페이지에 대해 흡수기 수락
    document->get_Pages()->Accept(textFragmentAbsorber);

    // 추출된 텍스트 조각을 컬렉션에 가져오기
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // 조각을 반복 처리
    for (auto textFragment : textFragmentCollection) {
        Console::WriteLine(u"Text :- {0}", textFragment->get_Text());
        Console::WriteLine(u"Position :- {0}", textFragment->get_Position());
        Console::WriteLine(u"XIndent :- {0}", textFragment->get_Position()->get_XIndent());
        Console::WriteLine(u"YIndent :- {0}", textFragment->get_Position()->get_YIndent());
        Console::WriteLine(u"Font - Name :- {0}", textFragment->get_TextState()->get_Font()->get_FontName());
        Console::WriteLine(u"Font - IsAccessible :- {0}", textFragment->get_TextState()->get_Font()->get_IsAccessible());
        Console::WriteLine(u"Font - IsEmbedded - {0}", textFragment->get_TextState()->get_Font()->get_IsEmbedded());
        Console::WriteLine(u"Font - IsSubset :- {0}", textFragment->get_TextState()->get_Font()->get_IsSubset());
        Console::WriteLine(u"Font Size :- {0}", textFragment->get_TextState()->get_FontSize());
        Console::WriteLine(u"Foreground Color :- {0}", textFragment->get_TextState()->get_ForegroundColor());
    }
}
```