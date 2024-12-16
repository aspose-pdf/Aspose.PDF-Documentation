---
title: XFA 양식 추출
linktitle: XFA 양식 추출
type: docs
weight: 30
url: /ko/php-java/extract-form/
description: 이 섹션에서는 Aspose.PDF for PHP via Java를 사용하여 PDF 문서에서 양식을 추출하는 방법을 설명합니다.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서의 양식 필드에서 값 가져오기

양식 필드의 [getValue() 메서드](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--)를 사용하면 특정 필드의 값을 가져올 수 있습니다.

값을 가져오려면 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 Form 컬렉션에서 양식 필드를 가져옵니다.

이 예제는 [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField)를 선택하고 [getValue() 메서드](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--)를 사용하여 해당 값을 검색합니다.

```php

    // XFA 양식 로드
    $document = new Document($inputFile);
    
    // XFA 양식 필드의 이름 가져오기
    $names = $document->getForm()->getXFA()->getFieldNames();
        
    // 필드 값 가져오기
    $document->getForm()->getXFA()->get_Item($names[0]);
    $document->getForm()->getXFA()->get_Item($names[1]);
    
    // 수정된 PDF 저장    
    $document->close();
```