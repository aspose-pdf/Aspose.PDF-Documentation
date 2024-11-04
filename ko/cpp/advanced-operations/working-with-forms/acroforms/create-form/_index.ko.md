---
title: C++를 사용하여 AcroForms 생성
linktitle: AcroForms 생성
type: docs
weight: 10
url: /cpp/create-form/
description: 이 섹션에서는 Aspose.PDF for C++를 사용하여 PDF 문서에서 AcroForms를 처음부터 생성하는 방법을 설명합니다.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서에 양식 필드 추가

[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 클래스는 PDF 문서에서 양식 필드를 관리하는 데 도움이 되는 Form이라는 컬렉션을 제공합니다.

양식 필드를 추가하려면:

1. 추가하려는 양식 필드를 생성합니다.
2. [Form](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.forms) 컬렉션의 add 메서드를 호출합니다.

이 예제는 [TextBoxField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.text_box_field)를 추가하는 방법을 보여줍니다. 동일한 접근 방식을 사용하여 모든 양식 필드를 추가할 수 있습니다:

1. 먼저 필드 객체를 생성하고 속성을 설정합니다.
2. 그런 다음 필드를 Form 컬렉션에 추가합니다.

### TextBoxField 추가

텍스트 필드는 수신자가 양식에 텍스트를 입력할 수 있는 양식 요소입니다. 사용자가 원하는 대로 입력할 자유를 허용하려는 경우 언제든지 사용할 수 있습니다.

다음 코드 스니펫은 PDF 문서에 TextBoxField를 추가하는 방법을 보여줍니다.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Annotations;
void AddingTextBoxField()
{
    String _dataDir("C:\\Samples\\");
    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + u"TextField.pdf");

    // 필드 생성
    auto textBoxField = MakeObject<TextBoxField>(document->get_Pages()->idx_get(1), MakeObject<Aspose::Pdf::Rectangle>(100, 200, 300, 300));
    textBoxField->set_PartialName (u"textbox1");
    textBoxField->set_Value (u"Text Box");

    // TextBoxField.Border = new Border(
    auto border = MakeObject<Aspose::Pdf::Annotations::Border>(textBoxField);
    border->set_Width(5);
    border->set_Dash (MakeObject<Aspose::Pdf::Annotations::Dash>(1, 1));
    textBoxField->set_Border(border);

    textBoxField->set_Color(Aspose::Pdf::Color::get_Green());

    // 문서에 필드 추가
    document->get_Form()->Add(textBoxField, 1);

    // 수정된 PDF 저장
    document->Save(_dataDir + u"TextBox_out.pdf");
}
```
## RadioButtonField 추가

라디오 버튼은 일반적으로 여러 선택 질문에서 사용되며, 한 가지 답변만 선택할 수 있는 상황에서 사용됩니다.

다음 코드 스니펫은 PDF 문서에 [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field)를 추가하는 방법을 보여줍니다.

```cpp
void AddingRadioButtonField()
{
    String _dataDir("C:\\Samples\\");
    // 문서 열기
    auto document = MakeObject<Document>();

    // PDF 파일에 페이지 추가
    document->get_Pages()->Add();

    // 페이지 번호를 인수로 하여 RadioButtonField 객체를 인스턴스화

    auto radio = MakeObject<RadioButtonField>(document->get_Pages()->idx_get(1));

    // 첫 번째 라디오 버튼 옵션을 추가하고 Rectangle 객체를 사용하여 원점을 지정
    radio->AddOption(u"Option 1", MakeObject<Rectangle>(0, 0, 20, 20));
    // 두 번째 라디오 버튼 옵션 추가
    radio->AddOption(u"Option 2", MakeObject<Rectangle>(20, 20, 40, 40));
    // Document 객체의 폼 객체에 라디오 버튼 추가
    document->get_Form()->Add(radio,1);

    // PDF 파일 저장
    document->Save(_dataDir + u"RadioButton_out.pdf");
}
```

다음 코드 조각은 세 가지 옵션이 있는 [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field)를 추가하고 이를 테이블 셀 내부에 배치하는 단계를 보여줍니다.

```cpp
void AddRadioButtonFieldInsideTableCells()
{
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto table = MakeObject<Aspose::Pdf::Table>();

    table->set_ColumnWidths(u"120 120 120");

    page->get_Paragraphs()->Add(table);

    auto r1 = table->get_Rows()->Add();
    auto c1 = r1->get_Cells()->Add();
    auto c2 = r1->get_Cells()->Add();
    auto c3 = r1->get_Cells()->Add();

    auto rf = MakeObject<RadioButtonField>(page);
    rf->set_PartialName(u"radio");
    document->get_Form()->Add(rf, 1);

    auto opt1 = MakeObject<RadioButtonOptionField>();
    auto opt2 = MakeObject<RadioButtonOptionField>();
    auto opt3 = MakeObject<RadioButtonOptionField>();

    opt1->set_OptionName(u"Item1");
    opt2->set_OptionName(u"Item2");
    opt3->set_OptionName(u"Item3");

    opt1->set_Width (15);
    opt1->set_Height(15);
    opt2->set_Width (15);
    opt2->set_Height(15);
    opt3->set_Width (15);
    opt3->set_Height(15);

    rf->Add(opt1);
    rf->Add(opt2);
    rf->Add(opt3);

    opt1->set_Border(MakeObject<Border>(opt1));
    opt1->get_Border()->set_Width(1);
    opt1->get_Border()->set_Style(BorderStyle::Solid);
    opt1->get_Characteristics()->set_Border(System::Drawing::Color::get_Black());
    opt1->get_DefaultAppearance()->set_TextColor(System::Drawing::Color::get_Red());
    opt1->set_Caption(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Item1"));
    opt2->set_Border(MakeObject<Border>(opt2));
    opt2->get_Border()->set_Width(1);
    opt2->get_Border()->set_Style(BorderStyle::Solid);
    opt2->get_Characteristics()->set_Border(System::Drawing::Color::get_Black());
    opt2->get_DefaultAppearance()->set_TextColor(System::Drawing::Color::get_Red());
    opt2->set_Caption(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Item2"));
    opt3->set_Border(MakeObject<Border>(opt3));
    opt3->get_Border()->set_Width(1);
    opt3->get_Border()->set_Style(BorderStyle::Solid);
    opt3->get_Characteristics()->set_Border(System::Drawing::Color::get_Black());
    opt3->get_DefaultAppearance()->set_TextColor(System::Drawing::Color::get_Red());
    opt3->set_Caption(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Item3"));
    c1->get_Paragraphs()->Add(opt1);
    c2->get_Paragraphs()->Add(opt2);
    c3->get_Paragraphs()->Add(opt3);

    // PDF 파일 저장
    document->Save(_dataDir + u"RadioButtonWithOptions_out.pdf");
}
```

## RadioButtonField에 캡션 추가하기

다음 코드 스니펫은 [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field)에 연결될 캡션을 추가하는 방법을 보여줍니다:

```cpp
void AddingCaptionToRadioButtonField()
{
    String _dataDir("C:\\Samples\\");
    auto document = MakeObject<Document>();

    // 소스 PDF 양식 로드
    auto form1 =
        MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + u"RadioButtonField.pdf");

    auto PDF_Template_PDF_HTML = MakeObject<Document>(_dataDir + u"RadioButtonField.pdf");

    for(auto item : form1->get_FieldNames())
    {
        System::Console::WriteLine(item);
        auto radioOptions = form1->GetButtonOptionValues(item);
        if (item.Contains(u"radio1"))
        {
            auto field0 = System::DynamicCast<RadioButtonField>(PDF_Template_PDF_HTML->get_Form()->idx_get(item));
            auto fieldoption = MakeObject<RadioButtonOptionField>();
            fieldoption->set_OptionName (u"Yes");
            fieldoption->set_PartialName (u"Yesname");

            auto updatedFragment = MakeObject<Aspose::Pdf::Text::TextFragment>(u"test123");
            updatedFragment->get_TextState()->set_Font (Aspose::Pdf::Text::FontRepository::FindFont(u"Arial"));
            updatedFragment->get_TextState()->set_FontSize(10);
            updatedFragment->get_TextState()->set_LineSpacing(6.32f);

            // TextParagraph 객체 생성
            auto par = MakeObject<Aspose::Pdf::Text::TextParagraph>();

            // 단락 위치 설정
            par->set_Position(MakeObject<Aspose::Pdf::Text::Position>(field0->get_Rect()->get_LLX(), field0->get_Rect()->get_LLY() + updatedFragment->get_TextState()->get_FontSize()));
            // 단어 줄바꿈 모드 지정
        par->get_FormattingOptions()->set_WrapMode(Aspose::Pdf::Text::TextFormattingOptions::WordWrapMode::ByWords);

            // 단락에 새로운 TextFragment 추가
            par->AppendLine(updatedFragment);

            // TextBuilder를 사용하여 TextParagraph 추가
            auto textBuilder = MakeObject<Aspose::Pdf::Text::TextBuilder>(PDF_Template_PDF_HTML->get_Pages()->idx_get(1));
            textBuilder->AppendParagraph(par);

            field0->DeleteOption(u"item1");
        }
    }
    PDF_Template_PDF_HTML->Save(_dataDir + u"RadioButtonField_out.pdf");
}
```

## ComboBox 필드 추가

콤보 박스는 문서에 드롭다운 메뉴를 추가하는 양식 필드입니다.

다음 코드 스니펫은 PDF 문서에 [ComboBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.combo_box_field) 필드를 추가하는 방법을 보여줍니다.

```cpp
void AddingComboBoxField()
{
    String _dataDir("C:\\Samples\\");
    // 문서 객체 생성
    auto document = MakeObject<Document>();
    // 문서 객체에 페이지 추가
    document->get_Pages()->Add();
    // 콤보 박스 필드 객체 인스턴스화
    auto combo = MakeObject<ComboBoxField>(document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(100, 600, 150, 616));

    // 콤보 박스에 옵션 추가
    combo->AddOption(u"Red");
    combo->AddOption(u"Yellow");
    combo->AddOption(u"Green");
    combo->AddOption(u"Blue");

    // 문서 객체의 양식 필드 컬렉션에 콤보 박스 객체 추가
    document->get_Form()->Add(combo);

    // PDF 문서 저장
    document->Save(_dataDir + u"ComboBox_out.pdf");
}
```


## 양식에 툴팁 추가

The Document 클래스는 PDF 문서의 폼 필드를 관리하는 Form이라는 컬렉션을 제공합니다. 폼 필드에 툴팁을 추가하려면 Field 클래스의 AlternateName을 사용하세요. Adobe Acrobat은 '대체 이름'을 필드 툴팁으로 사용합니다.

다음 코드 스니펫은 C++로 폼 필드에 툴팁을 추가하는 방법을 보여줍니다.

```cpp
void AddTooltipToFormField()
{
    String _dataDir("C:\\Samples\\");
    // 소스 PDF 폼 로드
    auto document = new Document(_dataDir + u"AddTooltipToField.pdf");

    // 텍스트 필드에 툴팁 설정
    //(doc.Form["textbox1"] as Field).AlternateName = "텍스트 박스 툴팁";

    // 업데이트된 문서 저장
    document->Save(_dataDir + u"AddTooltipToField_out.pdf");
}
```