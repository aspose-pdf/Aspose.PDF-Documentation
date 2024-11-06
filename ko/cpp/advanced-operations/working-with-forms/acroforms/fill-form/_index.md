---
title: Fill AcroForm
linktitle: Fill AcroForm
type: docs
weight: 20
url: ko/cpp/fill-form/
description: 이 섹션에서는 Aspose.PDF for C++로 PDF 문서의 양식 필드를 채우는 방법을 설명합니다.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 문서는 양식을 생성하기 위한 최고의, 그리고 정말로 선호되는 파일 유형입니다.

이 주제에서는 Aspose.PDF for C++를 사용하여 PDF 양식을 작성하는 방법을 설명합니다.

Aspose.PDF for C++를 사용하면 양식 필드를 작성하고, Document 객체의 Form 컬렉션에서 필드를 가져올 수 있습니다.

다음 예제를 통해 이 작업을 해결하는 방법을 살펴보겠습니다:

```cpp
using namespace System;
using namespace Aspose::Pdf;

void FillAcroform()
{
    String _dataDir("C:\\Samples\\");

    // 문서 열기
    auto document = MakeObject<Document>(_dataDir + u"FillFormField.pdf");

    // 필드 가져오기
    auto textBoxField = System::DynamicCast<Aspose::Pdf::Forms::TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // 필드 값 수정
    textBoxField->set_Value(u"필드에 채워질 값");

    // 업데이트된 문서 저장
    document->Save(_dataDir + u"FillFormField_out.pdf");

}
```