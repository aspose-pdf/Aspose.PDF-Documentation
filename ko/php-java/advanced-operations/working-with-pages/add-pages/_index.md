---
title: PDF에 페이지 추가
linktitle: 페이지 추가
type: docs
weight: 10
url: /ko/php-java/add-pages/
description: 이 문서는 원하는 위치에 PDF 파일에 페이지를 삽입(추가)하는 방법을 가르칩니다. PHP를 사용하여 PDF 파일에서 페이지를 이동, 제거(삭제)하는 방법을 배우십시오.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 파일에 페이지 추가 또는 삽입

Aspose.PDF for PHP via Java를 사용하면 파일의 원하는 위치에 PDF 문서에 페이지를 삽입할 수 있으며 PDF 파일의 끝에 페이지를 추가할 수 있습니다. 빈 페이지를 삽입할 위치를 insert 메서드에 전달해야 합니다. 이 섹션에서는 Aspose.PDF for PHP via Java를 사용하여 PDF에 페이지를 추가하는 방법을 보여줍니다.

### 원하는 위치에 PDF 파일에 빈 페이지 삽입

다음 코드 스니펫은 PDF 파일에 빈 페이지를 삽입하는 방법을 보여줍니다:

1. 입력 PDF 파일로 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스 객체를 만듭니다.
1. 페이지를 추가하고 PDF에 삽입합니다.

1. Save 메서드를 사용하여 출력 PDF를 저장합니다.

다음 코드 스니펫은 PDF 파일에 페이지를 삽입하는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);

    // 페이지 추가
    $document->getPages()->add();

    // PDF에 빈 페이지 삽입
    $document->getPages()->insert(2);

    // 출력 문서 저장
    $document->save($outputFile);
    $document->close();
```

위의 예에서는 기본 매개변수로 빈 페이지를 추가했습니다. 문서의 다른 페이지와 같은 크기로 페이지 크기를 설정하려면 몇 줄의 코드를 추가해야 합니다.

```php

    // 문서 열기
    $document = new Document($inputFile);

    // 페이지 추가
    $page1 = $document->getPages()->add();

    // PDF에 빈 페이지 삽입
    $page2 = $document->getPages()->insert(2);

    // 페이지 1에서 페이지 매개변수 복사
    $page2->setCropBox($page1->getCropBox());
    $page2->setMediaBox($page1->getMediaBox());
    $page2->setTrimBox($page1->getTrimBox());
    $page2->setArtBox($page1->getArtBox());
    $page2->setBleedBox($page1->getBleedBox());
    
    // 출력 문서 저장
    $document->save($outputFile);
    $document->close();
```


### PDF 파일 끝에 빈 페이지 추가하기

때때로 문서가 빈 페이지로 끝나도록 하고 싶을 때가 있습니다. 이 주제에서는 PDF 문서의 끝에 빈 페이지를 삽입하는 방법을 설명합니다.

PDF 파일 끝에 빈 페이지를 삽입하려면:

1. 입력 PDF 파일로 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스 객체를 생성합니다.
1. 페이지를 추가하고, PDF에 삽입합니다.
1. 저장 메소드를 사용하여 출력 PDF를 저장합니다.

다음 코드 스니펫은 PDF 파일 끝에 빈 페이지를 삽입하는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);

    // 페이지 추가
    $document->getPages()->add();

    // PDF에 빈 페이지 삽입
    $document->getPages()->insert(2);

    // 출력 문서 저장
    $document->save($outputFile);
    $document->close();
```