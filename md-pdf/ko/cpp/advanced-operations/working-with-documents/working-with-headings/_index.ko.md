---
title: Working with Headings in PDF
type: docs
weight: 90
url: /cpp/working-with-headings/
lastmod: "2021-11-11"
description: C++로 PDF 문서의 머리글에 번호 매기기를 만듭니다. Aspose.PDF for C++는 다양한 번호 매기기 스타일을 보여줍니다.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 머리글에 번호 매기기 스타일 적용

문서의 모든 텍스트는 머리글로 시작됩니다. 머리글은 스타일과 테마에 상관없이 콘텐츠의 필수적인 부분입니다.
머리글은 텍스트에 주의를 끌고 사용자가 문서에서 필요한 정보를 찾는 데 도움을 주어 가독성과 시각적 인식을 향상시킵니다. 머리글 스타일을 사용하면 목차를 빠르게 생성하고 문서의 구조를 변경할 수도 있습니다.
따라서 Aspose.PDF for C++ 라이브러리를 사용하여 머리글을 어떻게 작업하는지 확인해 보겠습니다.

[Aspose.PDF for C++](/pdf/cpp/)는 많은 사전 정의된 번호 매기기 스타일을 제공합니다. 이러한 사전 정의된 번호 매기기 스타일은 열거형 NumberingStyle에 저장되어 있습니다. NumberingStyle 열거형의 사전 정의된 값과 그 설명은 아래와 같습니다:

|**헤딩 유형**|**설명**|
| :- | :- |
|NumeralsArabic|아랍 유형, 예: 1,1.1,...|
|NumeralsRomanUppercase|로마 대문자 유형, 예: I,I.II, ...|
|NumeralsRomanLowercase|로마 소문자 유형, 예: i,i.ii, ...|
|LettersUppercase|영어 대문자 유형, 예: A,A.B, ...|
|LettersLowercase|영어 소문자 유형, 예: a,a.b, ...|
**Aspose.PDF.Heading** 클래스의 **Style** 속성은 헤딩의 번호 매기기 스타일을 설정하는 데 사용됩니다.

|**그림: 사전 정의된 번호 매기기 스타일**|
| :- |
위 그림에 표시된 출력을 얻기 위한 소스 코드는 아래 예제에 나와 있습니다.

```cpp
void WorkingWithHeadingsInPDF() {
    // 경로 이름에 대한 문자열
    String _dataDir("C:\\Samples\\");

    // 입력 파일 이름에 대한 문자열
    String outputFileName("ApplyNumberStyle_out.pdf");

    // 문서 열기
    auto document = MakeObject<Document>();

    document->get_PageInfo()->set_Width(612.0);
    document->get_PageInfo()->set_Height(792.0);
    document->get_PageInfo()->set_Margin (MakeObject<MarginInfo>());
    document->get_PageInfo()->get_Margin()->set_Left(72);
    document->get_PageInfo()->get_Margin()->set_Right(72);
    document->get_PageInfo()->get_Margin()->set_Top (72);
    document->get_PageInfo()->get_Margin()->set_Bottom (72);
            
    auto pdfPage = document->get_Pages()->Add();
    pdfPage->get_PageInfo()->set_Width (612.0);
    pdfPage->get_PageInfo()->set_Height (792.0);
    pdfPage->get_PageInfo()->set_Margin(MakeObject<MarginInfo>());
    pdfPage->get_PageInfo()->get_Margin()->set_Left(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Right(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Top(72);
    pdfPage->get_PageInfo()->get_Margin()->set_Bottom(72);

    auto floatBox = MakeObject<FloatingBox>();
    floatBox->set_Margin(pdfPage->get_PageInfo()->get_Margin());

    pdfPage->get_Paragraphs()->Add(floatBox);

    auto textFragment = MakeObject<TextFragment>();
    auto segment = MakeObject<TextSegment>();

    auto heading = MakeObject<Heading>(1);
    heading->set_IsInList(true);
    heading->set_StartNumber(1);
    heading->set_Text (u"목록 1");
    heading->set_Style(NumberingStyle::NumeralsRomanLowercase);
    heading->set_IsAutoSequence(true);

    floatBox->get_Paragraphs()->Add(heading);

    auto heading2 = MakeObject<Heading>(1);
    heading2->set_IsInList (true);
    heading2->set_StartNumber(13);
    heading2->set_Text (u"목록 2");
    heading2->set_Style(NumberingStyle::NumeralsRomanLowercase);
    heading2->set_IsAutoSequence(true);;

    floatBox->get_Paragraphs()->Add(heading2);

    auto heading3 = MakeObject<Heading>(2);
    heading3->set_IsInList (true);
    heading3->set_StartNumber(1);
    heading3->set_Text (u"계획의 유효 날짜 기준으로 계획에 따라 분배될 재산의 가치");
    heading3->set_Style(NumberingStyle::LettersLowercase);
    heading3->set_IsAutoSequence(true);

    floatBox->get_Paragraphs()->Add(heading3); 

    // 연결된 출력 파일 저장
    document->Save(_dataDir + outputFileName);
}
```