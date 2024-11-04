---
title: PDF 페이지를 프로그래밍 방식으로 삭제
linktitle: PDF 페이지 삭제
type: docs
weight: 40
url: /php-java/delete-pages/
description: PHP를 사용하여 PDF 파일에서 페이지를 삭제할 수 있습니다.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 파일에서 페이지 삭제

1. delete 메서드를 호출하고 페이지의 인덱스를 지정합니다.
1. save 메서드를 호출하여 업데이트된 PDF 파일을 저장합니다.
다음 코드 스니펫은 PHP를 사용하여 PDF 파일에서 특정 페이지를 삭제하는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);      

    $pages = $document->getPages();

    // 특정 페이지 삭제
    $pages->delete(2);

    // 출력 문서 저장
    $document->save($outputFile);
    $document->close();
```