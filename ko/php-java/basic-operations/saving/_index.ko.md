---
title: PDF 문서 저장
linktitle: 저장
type: docs
weight: 30
url: /php-java/save-pdf-document/
description: Aspose.PDF for PHP via Java 라이브러리를 사용하여 PDF 파일을 저장하는 방법을 학습합니다.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 파일 시스템에 PDF 문서 저장

[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스의 save 메서드를 사용하여 생성되거나 조작된 PDF 문서를 파일 시스템에 저장할 수 있습니다.

```php

    $document = new Document($inputFile);        
    $document->save($outputFile);
```