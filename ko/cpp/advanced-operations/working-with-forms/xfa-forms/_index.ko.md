---
title: C++를 사용하여 XFA 양식 작업하기
linktitle: XFA 양식
type: docs
weight: 20
url: /cpp/xfa-forms/
description: Aspose.PDF for C++ API는 PDF 문서에서 XFA 및 XFA Acroform 필드를 다룰 수 있게 합니다. Aspose.PDF.Facades.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

XFA 양식은 웹 양식의 처리를 개선하기 위해 JetForm이 제안하고 개발한 독점 XML 명세서의 집합인 XML 양식 아키텍처입니다. PDF 1.5 명세서부터 PDF 파일에서도 사용할 수 있습니다.

[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades)의 [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.form/) 클래스를 사용하여 XFA 필드를 채우십시오.

## XFA 필드 채우기

다음 코드 스니펫은 XFA 양식에서 필드를 채우는 방법을 보여줍니다.

```cpp
using namespace System;
using namespace System::Collections::Generic;

using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void FillXFA() {
    String _dataDir("C:\\Samples\\");

    // XFA 양식 로드
    auto document = MakeObject<Document>(_dataDir + u"FillXFAFields.pdf");

    // XFA 양식 필드의 이름 가져오기
    auto names = document->get_Form()->get_XFA()->get_FieldNames();

    // 필드 값 설정하기

    document->get_Form()->get_XFA()->idx_set(names->idx_get(0),u"Field 0");
    document->get_Form()->get_XFA()->idx_set(names->idx_get(1),u"Field 1");

    // 업데이트된 문서 저장하기
    document->Save(_dataDir + u"Filled_XFA_out.pdf");
}
```

## XFA를 AcroForm으로 변환

{{% alert color="primary" %}}

온라인으로 시도해보세요
Aspose.PDF 변환의 품질을 확인하고 결과를 이 링크에서 온라인으로 확인할 수 있습니다: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

동적 양식은 XFA, "XML Forms Architecture"로 알려진 XML 사양을 기반으로 합니다. PDF와 관련하여 양식에 대한 정보는 매우 모호합니다. 필드가 속성과 자바스크립트 이벤트로 존재한다는 것을 지정하지만, 렌더링을 지정하지 않습니다.

현재, PDF는 데이터와 PDF 양식을 통합하기 위한 두 가지 다른 방법을 지원합니다:

- AcroForms (Acrobat 양식으로도 알려짐), PDF 1.2 형식 사양에 도입되어 포함됨.
- Adobe XML Forms Architecture (XFA) 양식, PDF 1.5 형식 사양에 선택적 기능으로 도입됨 (XFA 사양은 PDF 사양에 포함되지 않고, 참조만 됩니다.)

우리는 XFA 양식의 페이지를 추출하거나 조작할 수 없습니다. 이는 양식 내용이 XFA 양식 보기 중에 애플리케이션 내에서 실행 시간에 생성되기 때문입니다. Aspose.PDF에는 개발자가 XFA 양식을 표준 AcroForms로 변환할 수 있는 기능이 있습니다.

```cpp
void ConvertXFAtoAcroForms() {

    String _dataDir("C:\\Samples\\");

    // XFA 양식 불러오기
    auto document = MakeObject<Document>(_dataDir + u"DynamicXFAToAcroForm.pdf");

    // 양식 필드 유형을 표준 AcroForm으로 설정
    document->get_Form()->set_Type(Aspose::Pdf::Forms::FormType::Standard);

    // 결과 PDF 저장
    document->Save(_dataDir + u"Standard_AcroForm_out.pdf");
}
```

## XFA 필드 속성 가져오기

필드 속성에 접근하려면 먼저 Document.Form.XFA.Teamplate를 사용하여 필드 템플릿에 접근하십시오. 다음 코드 스니펫은 XFA 양식 필드의 X 및 Y 좌표를 가져오는 단계를 보여줍니다.

```cpp
void GetXFAProprties() {

    String _dataDir("C:\\Samples\\");
    // XFA 양식 불러오기
    auto document = MakeObject<Document>(_dataDir + u"GetXFAProperties.pdf");

    auto names = document->get_Form()->get_XFA()->get_FieldNames();

    // 필드 값 설정
    document->get_Form()->get_XFA()->idx_set(names->idx_get(0), u"Field 0");
    document->get_Form()->get_XFA()->idx_set(names->idx_get(0), u"Field 1");

    // 필드 위치 가져오기
    Console::WriteLine(document->get_Form()->get_XFA()->GetFieldTemplate(names[0])->get_Attributes()->idx_get(u"x")->get_Value());

    // 필드 위치 가져오기
    Console::WriteLine(document->get_Form()->get_XFA()->GetFieldTemplate(names[0])->get_Attributes()->idx_get(u"y")->get_Value());

    // 업데이트된 문서 저장
    document->Save(_dataDir + u"Filled_XFA_out.pdf");
}
```