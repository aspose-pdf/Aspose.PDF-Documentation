---
title: Posting AcroForm Data
linktitle: Posting AcroForm
type: docs
weight: 50
url: /cpp/posting-acroform-data/
description: Aspose.PDF for C++의 Aspose.Pdf.Facades 네임스페이스를 사용하여 양식 데이터를 XML 파일로 가져오고 내보낼 수 있습니다.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

AcroForm은 PDF 문서의 중요한 유형입니다. 문서의 텍스트는 다음과 같습니다:

Aspose.Pdf.Facades 네임스페이스를 사용하여 AcroForm을 생성하고 편집할 수 있을 뿐만 아니라 양식 데이터를 XML 파일로 가져오고 내보낼 수도 있습니다. C++용 Aspose.PDF의 Aspose.Pdf.Facades 네임스페이스를 사용하면 AcroForm의 또 다른 기능을 구현할 수 있으며, 이를 통해 AcroForm 데이터를 외부 웹 페이지에 게시할 수 있습니다. 이 웹 페이지는 게시된 변수를 읽고 이 데이터를 추가 처리에 사용합니다. 이 기능은 데이터를 PDF 파일에만 보관하지 않고 서버로 전송한 다음 데이터베이스 등에 저장하고자 할 때 유용합니다.

## 구현 세부사항

이 문서에서는 Aspose.Pdf.Facades 네임스페이스와 FormEditor 클래스를 사용하여 AcroForm을 생성하려고 시도했습니다. 또한 제출 버튼을 추가하고 대상 URL을 설정했습니다.

다음 코드 스니펫은 양식을 생성한 다음 웹 페이지에서 게시된 데이터를 수신하는 방법을 보여줍니다.
```cpp
using namespace System;
using namespace Aspose::Pdf;

void PostingExample() {

    // String _dataDir("C:\\Samples\\");
    // FormEditor 클래스의 인스턴스를 생성하고 입력 및 출력 pdf 파일을 바인딩합니다.
    auto editor = MakeObject<Aspose::Pdf::Facades::FormEditor>("input.pdf", "output.pdf");

    // AcroForm 필드를 생성합니다 - 간단함을 위해 두 개의 필드만 생성했습니다.
    editor->AddField(Aspose::Pdf::Facades::FieldType::Text, u"firstname", 1, 100, 600, 200, 625);
    editor->AddField(Aspose::Pdf::Facades::FieldType::Text, u"lastname", 1, 100, 550, 200, 575);

    // 제출 버튼을 추가하고 대상 URL을 설정합니다.
    editor->AddSubmitBtn(u"submitbutton", 1, u"Submit", u"http://localhost/csharptesting/show.aspx", 100, 450, 150, 475);

    // 출력 pdf 파일을 저장합니다.
    editor->Save();
}
```