---
title: XFA 양식을 AcroForm으로 변환
linktitle: XFA 양식 변환
type: docs
weight: 10
url: /php-java/convert-form/
description: 이 섹션에서는 Aspose.PDF for PHP via Java를 사용하여 XFA 양식을 AcroForm으로 변환하는 방법을 설명합니다.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 동적 XFA 양식을 표준 AcroForm으로 변환

동적 양식은 XFA, 즉 "XML Forms Architecture"로 알려진 XML 사양을 기반으로 합니다. 또한 동적 XFA 양식을 표준 Acroform으로 변환할 수 있습니다. 양식에 대한 정보는 (PDF와 관련하여) 매우 모호합니다. 필드가 속성과 JavaScript 이벤트와 함께 존재한다고 명시되어 있지만, 렌더링에 대해 명시하지 않습니다. XFA 양식의 객체는 문서를 로드할 때 그려집니다.

현재 PDF는 데이터와 PDF 양식을 통합하기 위한 두 가지 다른 방법을 지원합니다:

- AcroForms (Acrobat 양식이라고도 함)은 PDF 1.2 형식 사양에 도입되어 포함되었습니다.

- Adobe XML Forms Architecture (XFA) 폼은 선택적 기능으로 PDF 1.5 형식 사양에 도입되었습니다. (XFA 사양은 PDF 사양에 포함되어 있지 않으며, 단지 참조만 됩니다.)

XFA Forms의 페이지를 추출하거나 조작하는 것은 불가능합니다. 왜냐하면 폼 콘텐츠는 XFA 폼 보기 동안 실행 시에 이를 표시하거나 렌더링하려는 애플리케이션 내에서 생성되기 때문입니다. Aspose.PDF는 개발자가 XFA 폼을 표준 AcroForms로 변환할 수 있는 기능을 제공합니다.

```php

        // XFA 폼 로드
        $document = new Document($inputFile);
        
        // 폼 필드 유형을 표준 AcroForm으로 설정
        $formType = new FormType();
        $document->getForm()->setType($formType->getStandard());
            
        // 업데이트된 문서 저장
        $document->save($outputFile);
        
        // 수정된 PDF 저장    
        $document->close();
```