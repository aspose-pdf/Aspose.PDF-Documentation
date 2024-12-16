---
title: PDF 문서 열기
linktitle: 열기
type: docs
weight: 20
url: /ko/php-java/open-pdf-document/
description: Aspose.PDF for PHP via Java를 사용하여 PDF 파일을 여는 방법을 배우십시오.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 기존 PDF 문서 열기

PDF 파일 또는 휴대용 문서 형식 파일은 문서 교환의 보편적인 표준이 되었습니다. 문서의 형식을 저장하는 데 널리 사용됩니다. 그러나 PHP를 통한 Java와 같은 프로그래밍 언어를 사용하여 PDF 파일을 다루는 것은 약간 어려울 수 있습니다. 이 문서에서는 PDF를 빠르고 쉽게 열 수 있도록 하는 Aspose.PDF for PHP via Java 라이브러리를 소개합니다.

```php

    $document = new Document($inputFile,"mypassword");
    $responseData = "문서가 성공적으로 열렸습니다. 파일 크기: " . filesize($inputFile);
```