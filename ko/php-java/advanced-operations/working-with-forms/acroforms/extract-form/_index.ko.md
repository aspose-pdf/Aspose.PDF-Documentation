---
title: 데이터 추출 AcroForms
linktitle: 데이터 추출 AcroForms
type: docs
weight: 30
url: /php-java/extract-form/
description: 이 섹션에서는 Aspose.PDF for PHP via Java를 사용하여 PDF 문서에서 양식을 추출하는 방법을 설명합니다.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서의 개별 필드에서 값 가져오기

양식 필드의 [getValue() 메서드](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--)를 사용하여 특정 필드의 값을 가져올 수 있습니다.

값을 얻으려면 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 Form 컬렉션에서 양식 필드를 가져옵니다.

이 예제는 [textBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField)를 선택하고 [getValue() 메서드](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--)를 사용하여 해당 값을 검색합니다.

```php

    // 문서 열기
    $document = new Document($inputFile);

    // 필드 가져오기
    $textBoxField = $document->getForm()->get("textbox1");

    // 필드 이름 가져오기
    $responseData = "PartialName: " . $textBoxField->getPartialName();

    // 필드 값 가져오기
    $responseData = $responseData . " Value: " . $textBoxField->getValue();
    $document->close();
```