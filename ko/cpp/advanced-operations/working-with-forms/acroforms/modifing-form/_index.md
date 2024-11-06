---
title: AcroForm 수정
linktitle: AcroForm 수정
type: docs
weight: 40
url: ko/cpp/modifing-form/
description: Aspose.PDF for C++ 라이브러리를 사용하여 PDF 파일의 양식을 수정합니다. 기존 양식에 필드를 추가하거나 제거하고, 필드 제한을 설정 및 가져오는 등의 작업을 수행할 수 있습니다.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 필드 제한 설정 또는 가져오기

FormEditor 클래스의 SetFieldLimit(field, limit) 메서드를 사용하면 필드에 입력할 수 있는 최대 문자 수인 필드 제한을 설정할 수 있습니다.

```cpp
void SetFieldLimitDom() {
    String _dataDir("C:\\Samples\\");
    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));
    textBoxField->set_MaxLen(15);
    document->Save(_dataDir + u"GetValuesFromAllFields.pdf");
}
```

마찬가지로, Aspose.PDF에는 DOM 접근 방식을 사용하여 필드 제한을 가져오는 메서드가 있습니다. 다음 코드 스니펫은 단계를 보여줍니다.

```cpp
void GetFieldLimitDom() {
    String _dataDir("C:\\Samples\\");
    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));
    Console::WriteLine(u"Limit: {0}", textBoxField->get_MaxLen());        
}
```

다음 코드 스니펫을 사용하여 *Aspose.PDF.Facades* 네임스페이스를 사용하여 동일한 값을 설정하고 가져올 수도 있습니다.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void SetFieldLimitFacade(){
    String _dataDir("C:\\Samples\\");
    // 제한과 함께 필드 추가
    auto form = MakeObject<Aspose::Pdf::Facades::FormEditor>(_dataDir + u"input.pdf", _dataDir + u"SetFieldLimit_out.pdf");
    form->SetFieldLimit(u"textbox1", 15);
    form->Save();
}
```

```cpp
void GetFieldLimitFacade(){
    String _dataDir("C:\\Samples\\");
    // 제한과 함께 필드 추가
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + u"input.pdf");
    Console::WriteLine(u"Limit: {0}", form->GetFieldLimit(u"textbox1"));
}
```
## 양식 필드에 사용자 지정 글꼴 설정

Adobe PDF 파일의 양식 필드는 특정 기본 글꼴을 사용하도록 구성할 수 있습니다. Aspose.PDF의 초기 버전에서는 14개의 기본 글꼴만 지원되었습니다. 이후 릴리스에서는 개발자가 임의의 글꼴을 적용할 수 있게 되었습니다. 양식 필드에 사용되는 기본 글꼴을 설정하고 업데이트하려면 DefaultAppearance(Font font, double size, Color color) 클래스를 사용하세요. 이 클래스는 Aspose.PDF.InteractiveFeatures 네임스페이스 아래에 있습니다. 이 객체를 사용하려면 Field 클래스의 DefaultAppearance 속성을 사용하세요.

다음 코드 스니펫은 PDF 양식 필드에 기본 글꼴을 설정하는 방법을 보여줍니다.

```cpp
void SetCustomFontForField() {

    String _dataDir("C:\\Samples\\");

    // 문서 열기
    auto document = new Document(_dataDir + u"FormFieldFont14.pdf");

    // 문서에서 특정 양식 필드 가져오기
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // 글꼴 객체 생성
    auto font = Aspose::Pdf::Text::FontRepository::FindFont(u"ComicSansMS");

    // 양식 필드에 대한 글꼴 정보 설정

    textBoxField->set_DefaultAppearance(MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>(font, 10, System::Drawing::Color::get_Black()));

    // 업데이트된 문서 저장
    document->Save(_dataDir + u"FormFieldFont14.pdf");
}
```

## 기존 양식에서 필드 삭제

모든 양식 필드는 Document 객체의 Form 컬렉션에 포함되어 있습니다. 이 컬렉션은 Delete 메서드를 포함하여 양식 필드를 관리하는 다양한 메서드를 제공합니다. 특정 필드를 삭제하려면 필드 이름을 Delete 메서드의 매개변수로 전달한 다음 업데이트된 PDF 문서를 저장하십시오. 다음 코드 스니펫은 PDF 문서에서 특정 필드를 삭제하는 방법을 보여줍니다.

```cpp
void DeleteFormField() {    
    String _dataDir("C:\\Samples\\");

    // 문서 열기
    auto document = new Document(_dataDir + u"DeleteFormField.pdf");

    // 이름으로 특정 필드 삭제
    document->get_Form()->Delete(u"textbox1");
    
    // 수정된 문서 저장
    document->Save(_dataDir + u"DeleteFormField_out.pdf");
}
```