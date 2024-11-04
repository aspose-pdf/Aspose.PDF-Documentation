---
title: PDF 파일 메타데이터 작업하기
linktitle: PDF 파일 메타데이터
type: docs
weight: 140
url: /php-java/pdf-file-metadata/
description: 이 섹션은 PDF 파일 정보를 얻는 방법, PDF 파일에서 XMP 메타데이터를 얻는 방법, PDF 파일 정보를 설정하는 방법을 설명합니다.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 파일 정보 얻기

PDF 파일에 대한 파일별 정보를 얻으려면 먼저 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스의 [getInfo()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getInfo--)를 사용하여 'docInfo' 객체를 가져옵니다. 'docInfo' 객체를 가져오면 개별 속성의 값을 얻을 수 있습니다.

다음 코드 스니펫은 PDF 파일 정보를 설정하는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);
    
    // 문서 정보 가져오기
    $docInfo = $document->getInfo();

    // 문서 정보 표시
    $responseData1 = "Author: " . $docInfo->getAuthor() . ", ";
    $responseData2 = "Creation Date: " . $docInfo->getCreationDate() . ", ";
    $responseData3 = "Keywords: " . $docInfo->getKeywords() . ", ";
    $responseData4 = "Modify Date: " . $docInfo->getModDate() . ", ";
    $responseData5 = "Subject: " . $docInfo->getSubject() . ", ";
    $responseData6 = "Title: " . $docInfo->getTitle() . "";

    $document->close();
```