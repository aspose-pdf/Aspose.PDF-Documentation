---
title: PDF 페이지 회전을 프로그래밍 방식으로
linktitle: PDF 페이지 회전
type: docs
weight: 60
url: ko/php-java/rotate-pages/
description: Java를 사용하여 페이지 방향을 변경하고 페이지 내용을 새로운 페이지 방향에 맞추는 방법을 설명합니다.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 페이지 방향 변경

이 문서는 기존 PDF 파일의 페이지 방향을 업데이트하거나 변경하는 방법을 설명합니다.

Aspose.PDF for PHP via Java는 가로에서 세로로, 또는 그 반대로 페이지 방향을 변경할 수 있는 기능을 제공합니다.

1. 지정된 입력 파일을 사용하여 문서를 엽니다.
1. 문서의 모든 페이지를 가져옵니다.
1. 각 페이지를 반복하면서 회전을 90도로 설정합니다.
1. 수정된 문서를 지정된 출력 파일에 저장합니다.
1. 문서를 닫습니다.

```php

    // 문서 열기
    $document = new Document($inputFile);                
    $pages = $document->getPages();
    $pagesSize = java_values($pages->size());
       
    // 모든 페이지를 순회
    for ($pageCount = 1; $pageCount <= $pagesSize; $pageCount++) {
        $page = $pages->get_Item($pageCount);
       
        $page->setRotate((new Rotation())->On90);
    }

    // 출력 문서 저장
    $document->save($outputFile);
    $document->close();
```