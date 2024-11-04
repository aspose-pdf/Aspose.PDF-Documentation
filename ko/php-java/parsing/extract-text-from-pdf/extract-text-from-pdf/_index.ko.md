---
title: PDF 파일에서 원시 텍스트 추출
linktitle: PDF에서 텍스트 추출
type: docs
weight: 10
url: /php-java/extract-text-from-all-pdf/
description: 이 문서는 Aspose.PDF for PHP를 사용하여 PDF 문서에서 전체 페이지, 특정 부분, 열을 기준으로 텍스트를 추출하는 다양한 방법을 설명합니다.
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF 문서의 모든 페이지에서 텍스트 추출하기

PDF 문서에서 텍스트를 추출하는 것은 일반적인 요구 사항입니다. 이 예제에서는 Aspose.PDF for PHP가 PDF 문서의 모든 페이지에서 텍스트를 추출할 수 있도록 하는 방법을 보여줍니다.
모든 PDF 페이지에서 텍스트를 추출하려면:

1. [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) 클래스의 객체를 생성합니다.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스를 사용하여 PDF를 열고 [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 컬렉션의 [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) 메서드를 호출합니다.
1. [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) 클래스는 문서에서 텍스트를 흡수하고 [getText() 메서드](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/#getText--)로 반환합니다.

다음 코드 스니펫은 PDF 문서의 모든 페이지에서 텍스트를 추출하는 방법을 보여줍니다.

```php

    // 입력 PDF 파일에서 새 Document 객체를 생성합니다.
    $document = new Document($inputFile);

    // 문서에서 텍스트를 추출하기 위해 새 TextAbsorber 객체를 생성합니다.
    $textAbsorber = new TextAbsorber();

    // 문서에서 텍스트를 추출합니다.
    $textAbsorber->visit($document);

    // 추출된 텍스트 내용을 가져옵니다.
    $content = $textAbsorber->getText();

    // 추출된 텍스트를 출력 파일에 저장합니다.
    file_put_contents($outputFile, $content);
```