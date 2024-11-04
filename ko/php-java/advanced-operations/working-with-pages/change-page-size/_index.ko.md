---
title: PDF 페이지 크기 프로그래밍 방식으로 변경
linktitle: PDF 페이지 크기 변경
type: docs
weight: 50
url: /php-java/change-page-size/
description: PHP를 사용하여 PDF 파일의 페이지 크기를 변경합니다.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 페이지 크기 변경

Aspose.PDF for PHP via Java를 사용하면 Java 애플리케이션에서 간단한 코드로 PDF 페이지 크기를 변경할 수 있습니다. 이 주제에서는 기존 PDF 파일의 페이지 치수(크기)를 업데이트/변경하는 방법을 설명합니다.

[Page](https://reference.aspose.com/pdf//java/com.aspose.pdf/page) 클래스에는 페이지 크기를 설정할 수 있는 SetPageSize(...) 메서드가 포함되어 있습니다. 아래의 코드 스니펫은 몇 가지 간단한 단계로 페이지 치수를 업데이트합니다:

1. 소스 PDF 파일을 로드합니다.
1. 페이지를 [pageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) 객체에 가져옵니다.
1. 특정 페이지를 가져옵니다.
1. setPageSize(..) 메서드를 호출하여 치수를 업데이트합니다.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스의 save(..) 메서드를 호출하여 업데이트된 페이지 크기로 PDF 파일을 생성합니다.

다음 코드 스니펫은 PDF 페이지 크기를 A4 크기로 변경하는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);
      
    // 페이지 컬렉션 가져오기
    $pageCollection = $document->getPages();

    // 특정 페이지 가져오기
    $page = $pageCollection->get_Item(1);

    // 페이지 크기를 A4 (11.7 x 8.3 인치)로 설정하고, Aspose.Pdf에서는 1 인치 = 72 포인트입니다.
    // 따라서 A4 크기는 포인트로 (842.4, 597.6)입니다.
    $page.setPageSize(597.6, 842.4);

    // 출력 문서 저장
    $document->save($outputFile);
    $document->close();
```

## PDF 페이지 크기 가져오기

Java를 통해 PHP용 Aspose.PDF를 사용하여 기존 PDF 파일의 페이지 크기를 읽을 수 있습니다. 다음 코드 샘플은 PHP를 사용하여 PDF 페이지 크기를 읽는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);
      
    // PDF 문서에 빈 페이지 추가
    $page = $document->getPages()->size() > 0 
        ? $document->getPages()->get_Item(1) 
        : $document->getPages()->add();
    
    // 페이지 높이 및 너비 정보 가져오기
    $responseData = $page->getPageRect(true)->getWidth() . ":" . $page->getPageRect(true)->getHeight();
    
    // 페이지를 90도 각도로 회전
    $rotation = new Rotation();
    $page->setRotate($rotation->getOn90());

    // 페이지 높이 및 너비 정보 가져오기
    $responseData = $responseData . $page->getPageRect(true)->getWidth() . ":" . $page->getPageRect(true)->getHeight();
    
    // 출력 문서 저장
    $document->save($outputFile);
    $document->close();
```