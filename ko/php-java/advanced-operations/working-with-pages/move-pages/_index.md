---
title: PDF 페이지 이동
linktitle: PDF 페이지 이동
type: docs
weight: 20
url: /ko/php-java/move-pages/
description: Aspose.PDF for PHP via Java를 사용하여 원하는 위치나 PDF 파일의 끝으로 페이지를 이동해 보세요.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 한 PDF 문서에서 다른 문서로 페이지 이동

이 주제는 한 PDF 문서에서 다른 문서의 끝으로 페이지를 이동하는 방법을 설명합니다. 페이지를 이동하려면 다음을 수행해야 합니다:

1. 원본 PDF 파일로 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스 객체 생성
1. 대상 PDF 파일로 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스 객체 생성
1. 출력 문서에 페이지 추가. 출력 파일 저장
1. 입력 문서에서 페이지 삭제. 수정된 입력 문서 저장
1. 문서 닫기
1. 출력 문서를 저장하고 닫기

다음 코드 스니펫은 한 페이지를 이동하는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile1);
    $dstDocument = new Document($outputFile);
    
    $page = $document->getPages()->get_Item(2);
    $dstDocument->getPages()->add($page);

    // 출력 파일 저장
    $dstDocument->save($srcFileName);
    $document->getPages()->delete(2);
    $document->save($dstFileName);
    $document->close();
    $dstDocument->close();
  
    // 출력 문서 저장
    $document->save($outputFile);
    $document->close();
```


## 하나의 PDF 문서에서 다른 PDF 문서로 여러 페이지 이동

1. 소스 PDF 파일로 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스 객체를 생성합니다.
1. 대상 PDF 파일로 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스 객체를 생성합니다.
1. 입력 문서에서 출력 문서로 복사할 페이지를 정의합니다.
1. 배열을 통해 반복 실행합니다:
    1. 입력 문서에서 지정된 인덱스의 페이지를 가져옵니다.
    1. 페이지를 대상 문서에 추가합니다.
1. Save 메서드를 사용하여 출력 PDF를 저장합니다.
1. 배열을 사용하여 소스 문서에서 페이지를 삭제합니다.
1. Save 메서드를 사용하여 소스 PDF를 저장합니다.

다음 코드 스니펫은 PDF 파일의 끝에 빈 페이지를 삽입하는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile1);
    $dstDocument = new Document($outputFile);
    
    $pages = [1, 3 ];
    foreach ($pages as $pageIndex) {
      $page = $document->getPages()->get_Item($pageIndex);
      $dstDocument->getPages()->add(page);
    }
    // 출력 파일 저장
    $dstDocument->save($srcFileName);
    $document->getPages()->delete($pages);

    $document->save(dstFileName);

    $document->close();
    $dstDocument->close();  
```


## 현재 PDF 문서에서 새 위치로 페이지 이동

1. 소스 PDF 파일로 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스 객체를 생성합니다.
1. [pageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) 컬렉션에서 페이지를 가져옵니다.
1. 페이지를 새 위치에 추가합니다.
1. 인덱스 2에 있는 페이지를 삭제합니다.
1. 저장 메서드를 사용하여 출력 PDF를 저장합니다.

```php

    // 문서 열기
    $document = new Document($inputFile);
        
    $pageCollection = $document->getPages();
    
    $page = $pageCollection->get_Item(2);
    $pageCollection->add(page);
    $pageCollection->delete(2);

    // 출력 파일 저장
    $document->save($outputFile);
    $document->close();      
```