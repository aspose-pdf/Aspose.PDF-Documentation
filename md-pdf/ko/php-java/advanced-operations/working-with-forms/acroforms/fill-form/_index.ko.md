---
title: AcroForms 채우기
linktitle: AcroForms 채우기
type: docs
weight: 20
url: /php-java/fill-form/
description: 이 섹션에서는 Aspose.PDF for PHP via Java를 사용하여 PDF 문서에서 양식 필드를 채우는 방법을 설명합니다.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 문서는 양식을 생성하는 데 이상적이며 정말로 선호되는 파일 형식입니다.

Aspose.PDF for PHP via Java를 사용하면 문서 객체의 양식 컬렉션에서 필드를 가져와 양식 필드를 채울 수 있습니다.

다음 예제를 통해 이 작업을 해결하는 방법을 살펴보겠습니다:

```php

    // 문서 열기
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);
    
    // 필드 가져오기    
    $textBoxField = $document->getForm()->get("textbox1");

    // 필드 값 수정
    $textBoxField->setValue("필드에 채워질 값");
        
    // 업데이트된 문서 저장
    $document->save($outputFile);
    $document->close();
```