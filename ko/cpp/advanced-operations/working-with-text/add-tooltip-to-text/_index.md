---
title: PDF 툴팁을 C++를 사용하여 추가하기
linktitle: PDF 툴팁
type: docs
weight: 20
url: ko/cpp/pdf-tooltip/
description: C++ 및 Aspose.PDF를 사용하여 PDF의 텍스트 조각에 툴팁을 추가하는 방법을 배워보세요.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 보이지 않는 버튼을 추가하여 검색된 텍스트에 툴팁 추가하기

이 문서에서는 C++에서 기존 PDF 문서의 텍스트에 툴팁을 추가하는 방법을 설명합니다. Aspose.PDF는 PDF 파일에서 검색된 텍스트 위에 보이지 않는 버튼을 추가하여 툴팁을 생성할 수 있습니다.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;


void AddTooltipToSearchedText() {

    String _dataDir("C:\\Samples\\");

    // 출력 파일 이름을 위한 문자열
    String outputFileName("Tooltip_out.pdf");

    // 텍스트가 포함된 샘플 문서 만들기
    auto document = MakeObject<Document>();
    document->get_Pages()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("여기에 마우스 커서를 이동하여 툴팁을 표시합니다"));

    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(MakeObject<TextFragment>("여기에 마우스 커서를 이동하여 매우 긴 툴팁을 표시합니다"));

    document->Save(outputFileName);

    // 텍스트가 포함된 문서 열기
    auto document = MakeObject<Document>(outputFileName);
    // 정규 표현식과 일치하는 모든 구문을 찾기 위한 TextAbsorber 객체 생성
    auto absorber = MakeObject<TextFragmentAbsorber>("여기에 마우스 커서를 이동하여 툴팁을 표시합니다");
    // 문서 페이지에 대해 absorber를 수락
    document->get_Pages()->Accept(absorber);

    // 추출된 텍스트 조각 가져오기
    auto textFragments = absorber->get_TextFragments();

    // 조각을 반복
    for(auto fragment : textFragments)
    {
        // 텍스트 조각 위치에 보이지 않는 버튼 생성
        auto field = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
        // AlternateName 값은 뷰어 애플리케이션에 의해 툴팁으로 표시됩니다
        field->set_AlternateName (u"텍스트에 대한 툴팁.");
        // 문서에 버튼 필드 추가
        document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(field));
    }

    // 다음은 매우 긴 툴팁의 샘플입니다
    absorber = MakeObject<TextFragmentAbsorber>("여기에 마우스 커서를 이동하여 매우 긴 툴팁을 표시합니다");
    document->get_Pages()->Accept(absorber);
    textFragments = absorber->get_TextFragments();

    for(auto fragment : textFragments)
    {
        auto field = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
        // 매우 긴 텍스트 설정
        field->set_AlternateName(String("Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
            sed do eiusmod tempor incididunt ut labore et dolore magna\
            aliqua. Ut enim ad minim veniam, quis nostrud exercitation\
            ullamco laboris nisi ut aliquip ex ea commodo consequat.\
            Duis aute irure dolor in reprehenderit in voluptate velit\
            esse cillum dolore eu fugiat nulla pariatur. Excepteur sint\
            occaecat cupidatat non proident, sunt in culpa qui officia\
            deserunt mollit anim id est laborum."));
        document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(field));
    }

    // 문서 저장
    document->Save(outputFileName);

}
```

## 마우스 오버 시 숨겨진 텍스트 블록 생성 및 표시

Aspose.PDF for C++는 숨기기 동작 기능을 구현하여, 마우스가 보이지 않는 버튼 위로 들어가거나 나올 때 텍스트 필드(또는 다른 유형의 주석)를 표시/숨길 수 있습니다. 이를 위해 Aspose.Pdf.Annotations.HideAction 클래스를 사용하여 텍스트 블록에 숨기기/보이기 동작을 할당하십시오. 다음 코드 스니펫을 사용하여 마우스 입력/출력 시 텍스트 블록을 표시/숨길 수 있습니다.

또한 문서의 PDF 동작은 해당 리더(예: Adobe Reader)에서 잘 작동하지만 다른 PDF 리더(예: 웹 브라우저 플러그인)에 대한 보장은 제공하지 않는다는 점을 유의하십시오. 우리는 간단한 조사를 통해 다음을 발견했습니다:

- PDF 문서에서의 숨기기 동작의 모든 구현은 Internet Explorer v.11.0에서 잘 작동합니다.
- 숨기기 동작의 모든 구현은 Opera v.12.14에서도 작동하지만, 문서를 처음 열 때 일부 응답 지연이 발견됩니다.

- 필드 이름을 수용하는 HideAction 생성자를 사용하는 구현만 Google Chrome v.61.0에서 문서를 열람할 때 작동합니다; Google Chrome에서 열람이 중요한 경우 해당 생성자를 사용하십시오:

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```cpp
void CreateHiddenTextBlock() {

    String _dataDir("C:\\Samples\\");

    // 출력 파일 이름에 대한 문자열
    String outputFileName("TextBlock_HideShow_MouseOverOut_out.pdf");

    // 텍스트가 있는 샘플 문서 생성
    auto document = MakeObject<Document>();

    document->get_Pages()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("마우스 커서를 이곳으로 이동하면 떠 있는 텍스트가 표시됩니다"));
    document->Save(outputFileName);

    // 텍스트가 있는 문서 열기
    auto document = MakeObject<Document>(outputFileName);

    // 정규 표현식과 일치하는 모든 구를 찾기 위한 TextAbsorber 객체 생성
    auto absorber = MakeObject<TextFragmentAbsorber>("마우스 커서를 이곳으로 이동하면 떠 있는 텍스트가 표시됩니다");
    // 문서 페이지에 흡수기를 수락
    document->get_Pages()->Accept(absorber);
    // 첫 번째로 추출된 텍스트 조각 가져오기
    auto textFragments = absorber->get_TextFragments();
    auto fragment = textFragments->idx_get(1);

    // 페이지의 지정된 사각형에 떠 있는 텍스트를 위한 숨겨진 텍스트 필드 생성
    auto floatingField = MakeObject<Aspose::Pdf::Forms::TextBoxField>(fragment->get_Page(), MakeObject<Rectangle>(100, 700, 220, 740));
    // 필드 값으로 표시할 텍스트 설정
    floatingField->set_Value(u"이것은 \"떠 있는 텍스트 필드\"입니다.");
    // 이 시나리오에서는 필드를 '읽기 전용'으로 만드는 것이 좋습니다
    floatingField->set_ReadOnly(true);
    // 문서 열기 시 필드를 보이지 않게 하기 위해 '숨김' 플래그 설정
    floatingField->set_Flags(floatingField->get_Flags() | Aspose::Pdf::Annotations::AnnotationFlags::Hidden);

    // 필드 이름을 고유하게 설정하는 것은 필수가 아니지만 허용됩니다
    floatingField->set_PartialName (u"FloatingField_1");

    // 필드 외관의 특성을 설정하는 것은 필수가 아니지만 더 좋습니다
    floatingField->set_DefaultAppearance(MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>("Helv", 10, Color::get_Blue()));
    floatingField->get_Characteristics()->set_Background (System::Drawing::Color::get_LightBlue());
    floatingField->get_Characteristics()->set_Border (System::Drawing::Color::get_DarkBlue());
    floatingField->set_Border(MakeObject<Aspose::Pdf::Annotations::Border>(floatingField));
    floatingField->get_Border()->set_Width (1);
    floatingField->set_Multiline (true);

    // 문서에 텍스트 필드 추가
    document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(floatingField));

    // 텍스트 조각 위치에 보이지 않는 버튼 생성
    auto buttonField = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
    // 지정된 필드(주석)와 불가시성 플래그에 대한 새 숨김 작업 생성
    // (위에서 지정한 경우 이름으로 떠 있는 필드를 참조할 수도 있습니다.)
    // 보이지 않는 버튼 필드에 마우스 들어가기/나가기 작업 추가
    buttonField->get_Actions()->set_OnEnter(MakeObject<Aspose::Pdf::Annotations::HideAction>(floatingField, false));
    buttonField->get_Actions()->set_OnExit(MakeObject<Aspose::Pdf::Annotations::HideAction>(floatingField));

    // 문서에 버튼 필드 추가
    document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(buttonField));

    // 문서 저장
    document->Save(outputFileName);
}
```