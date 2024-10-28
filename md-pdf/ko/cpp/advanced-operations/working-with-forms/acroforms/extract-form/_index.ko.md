---
title: C++를 사용하여 AcroForm 데이터 추출
linktitle: AcroForm 데이터 추출
type: docs
weight: 30
url: /cpp/extract-form/
description: 이 섹션에서는 Aspose.PDF for C++를 사용하여 PDF 문서에서 양식을 추출하는 방법을 설명합니다.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서의 모든 필드에서 값 가져오기

PDF 문서의 모든 필드에서 값을 가져오려면 모든 양식 필드를 탐색한 후 Value 속성을 사용하여 값을 가져와야 합니다. Form 컬렉션에서 각 필드를 가져와 Field라는 기본 필드 유형에서 Value 속성에 접근합니다.

다음 코드 스니펫은 PDF 문서의 모든 필드에서 값을 가져오는 방법을 보여줍니다.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void ExtractDataFromForm()
{
    String _dataDir("C:\\Samples\\");
    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");

    // 모든 필드에서 값 가져오기
    for(auto wa : document->get_Form())
    {
        auto formField = System::DynamicCast<Aspose::Pdf::Forms::Field>(wa);

        Console::WriteLine(u"필드 이름 : {0} ", formField->get_PartialName());
        Console::WriteLine(u"값 : {0} ", formField->get_Value());
    }
}
```

## PDF 문서의 개별 필드에서 값 가져오기

양식 필드의 Value 속성을 사용하면 특정 필드의 값을 가져올 수 있습니다. 값을 가져오려면 Document 객체의 Form 컬렉션에서 양식 필드를 가져옵니다. 이 예제는 [TextBoxField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.text_box_field)를 선택하고 Value 속성을 사용하여 해당 값을 검색합니다.

다음 코드 스니펫은 PDF 문서에서 개별 필드의 값을 가져오는 방법을 보여줍니다.

```cpp
void GetValueFromIndividualField(){

    String _dataDir("C:\\Samples\\");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + u"GetValueFromField.pdf");

    // 필드 가져오기
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // 필드 값 가져오기
    Console::WriteLine(u"PartialName : {0} ", textBoxField->get_PartialName());
    Console::WriteLine(u"Value : {0} ", textBoxField->get_Value());
}
```

제출 버튼의 URL을 가져오려면 다음 코드 줄을 사용하세요.

```cpp
void GetSubmitButtonURL()
{
    String _dataDir("C:\\Samples\\");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + u"GetValueFromField.pdf");
    auto act = System::DynamicCast<Aspose::Pdf::Annotations::SubmitFormAction>(document->get_Form()->idx_get(1)->get_OnActivated());

    if (act != nullptr)
        Console::WriteLine(act->get_Url()->get_Name());
}
```

## PDF 파일의 특정 영역에서 양식 필드 가져오기

때때로, 문서에서 양식 필드가 어디에 있는지 알지만 그 이름을 모를 수도 있습니다. 예를 들어, 인쇄된 양식의 도식만 가지고 있는 경우입니다. Aspose.PDF for C++를 사용하면 이는 문제가 되지 않습니다. PDF 파일의 특정 영역에 어떤 필드가 있는지 확인할 수 있습니다. PDF 파일의 특정 영역에서 양식 필드를 가져오려면:

1. Document 객체를 사용하여 PDF 파일을 엽니다.
1. 해당 영역의 필드를 얻기 위해 사각형 객체를 생성합니다.
1. 문서의 Forms 컬렉션에서 양식을 가져옵니다.
1. 필드 이름과 값을 표시합니다.

다음 코드 스니펫은 PDF 파일의 특정 직사각형 영역에서 양식 필드를 가져오는 방법을 보여줍니다.
```

```cpp
void GetFormFieldsFromSpecificRegion()
{
    String _dataDir("C:\\Samples\\");

    // pdf 파일 열기
    auto document = MakeObject<Aspose::Pdf::Document>(_dataDir + u"GetFieldsFromRegion.pdf");

    // 해당 영역의 필드를 가져오기 위해 사각형 객체 생성
    auto rectangle = MakeObject<Aspose::Pdf::Rectangle>(35, 30, 500, 500);

    // 사각형 영역 내의 필드 가져오기
    auto fields = document->get_Form()->GetFieldsInRect(rectangle);

    // 필드 이름과 값 표시
    for(auto field : fields)
    {
        // 모든 배치에 대한 이미지 배치 속성 표시
        Console::WriteLine(u"Field Name: {0} - Field Value: {1}", field->get_FullName(), field->get_Value());
    }
}
```