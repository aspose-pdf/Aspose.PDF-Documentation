---
title: 기존 PDF 파일에 이미지 추가
linktitle: 이미지 추가
type: docs
weight: 10
url: ko/php-java/add-image-to-existing-pdf-file/
description: 이 섹션에서는 PHP를 사용하여 기존 PDF 파일에 이미지를 추가하는 방법을 설명합니다.
lastmod: "2024-06-05"
---

모든 PDF 페이지는 리소스와 콘텐츠 속성을 포함합니다. 예를 들어, 리소스는 이미지와 양식일 수 있으며, 콘텐츠는 PDF 연산자 세트로 표현됩니다. 각 연산자는 이름과 인수를 가집니다. 이 예제는 연산자를 사용하여 PDF 파일에 이미지를 추가합니다.

기존 PDF 파일에 이미지를 추가하려면:

- [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체를 생성하고 입력 PDF 문서를 엽니다.
- 이미지를 추가할 페이지를 가져옵니다.
- 문서에 새 페이지를 추가합니다.
- 페이지의 크기를 1190.7 x 841.995로 설정합니다.
- 지정된 이미지 파일과 페이지의 크롭 박스를 사용하여 페이지에 이미지를 추가합니다.
- 파일을 저장합니다.

다음 코드 스니펫은 PDF 문서에 이미지를 추가하는 방법을 보여줍니다.

```php

    // 지정된 입력 파일을 사용하여 문서를 엽니다.
    $document = new Document($inputFile);
    
    // 문서에 새 페이지를 추가합니다.
    $page = $document->getPages()->add();
    
    // 페이지의 크기를 1190.7 x 841.995로 설정합니다.
    $page->setPageSize(1190.7, 841.995);
    
    // 지정된 이미지 파일과 페이지의 크롭 박스를 사용하여 페이지에 이미지를 추가합니다.
    $page->addImage($imageFileName, $page->getCropBox());
    
    // 수정된 문서를 지정된 출력 파일에 저장합니다.
    $document->save($outputFile);
    
    // 문서를 닫습니다.
    $document->close();
```