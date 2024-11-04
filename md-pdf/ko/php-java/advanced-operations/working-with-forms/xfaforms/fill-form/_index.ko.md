---
title: Fill AcroForms
linktitle: Fill AcroForms
type: docs
weight: 20
url: /php-java/fill-form/
description: 이 섹션에서는 Aspose.PDF for PHP via Java를 사용하여 PDF 문서에서 양식 필드를 채우는 방법을 설명합니다.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 문서는 양식을 만드는 데 정말로 선호되는 파일 유형이며 훌륭합니다.

Aspose.PDF for PHP via Java를 사용하면 문서 객체의 폼 컬렉션에서 필드를 가져와 양식 필드를 채울 수 있습니다.

다음 예제를 통해 이 작업을 해결하는 방법을 살펴보겠습니다:

```php

    // XFA 양식 불러오기
    $document = new Document($inputFile);
    
    // XFA 양식 필드 이름 가져오기
    $names = $document->getForm()->getXFA()->getFieldNames();
        
    // 필드 값 설정        
    $document->getForm()->getXFA()->set_Item($names[0],"Field 0");
    $document->getForm()->getXFA()->set_Item($names[1],"Field 1");
        
    // 업데이트된 문서 저장
    $document->save($outputFile);
    
    // 수정된 PDF 저장    
    $document->close();
```