---
title: PDF에서 XFA 양식 작업하기
linktitle: XFA 양식
type: docs
weight: 20
url: /ko/java/xfa-forms/
description: Aspose.PDF for Java를 사용하여 처음부터 양식을 만들고, PDF 문서의 양식 필드를 채우고, 양식에서 데이터를 추출하고, 기존 양식에서 필드를 추가하거나 제거할 수 있습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

XFA는 XML 양식 아키텍처를 의미합니다. 1999년에 웹 양식과 함께 사용하기 위해 원래 개발된 독점 XML 사양 세트이며, 이후 PDF에서도 사용할 수 있게 되었습니다.

## 동적 XFA 양식을 표준 AcroForm으로 변환

동적 양식은 XFA, 즉 "XML 양식 아키텍처"로 알려진 XML 사양을 기반으로 합니다. 또한 동적 XFA 양식을 표준 AcroForm으로 변환할 수 있습니다. 양식에 대한 정보는 (PDF와 관련하여) 매우 모호하며, 필드가 존재하고 속성과 JavaScript 이벤트가 있다는 것만 명시하고, 렌더링에 대해서는 명시하지 않습니다. XFA 양식의 객체는 문서를 로드할 때 그려집니다.

현재 PDF는 데이터와 PDF 양식을 통합하기 위한 두 가지 다른 방법을 지원합니다:

- AcroForms (Acrobat 양식이라고도 함)은 PDF 1.2 형식 사양에 도입되고 포함되었습니다.

- Adobe XML Forms Architecture (XFA) 양식은 PDF 1.5 형식 사양에서 선택적 기능으로 도입되었습니다. (XFA 사양은 PDF 사양에 포함되어 있지 않고, 단지 참조로만 언급됩니다.)

XFA 양식의 페이지를 추출하거나 조작하는 것은 불가능합니다. 왜냐하면 양식 내용은 XFA 양식을 표시하거나 렌더링하려는 애플리케이션 내에서 XFA 양식 보기 중에 런타임에 생성되기 때문입니다. Aspose.PDF는 개발자가 XFA 양식을 표준 AcroForms로 변환할 수 있는 기능을 제공합니다.

```java
// 동적 XFA 양식 로드
Document document = new Document("XFAform.pdf");
// 양식 필드 유형을 표준 AcroForm으로 설정
document.getForm().setType(FormType.Standard);
// 결과 PDF 저장
document.save("Standard_AcroForm.pdf");
```