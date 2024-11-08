---
title: PDF를 프로그래밍 방식으로 분할
linktitle: PDF 파일 분할
type: docs
weight: 60
url: /ko/php-java/split-document/
description: 이 주제는 PHP 애플리케이션에서 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Aspose.PDF를 사용하여 PDF 파일을 분할하고 이 링크에서 결과를 온라인으로 확인할 수 있습니다: [products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter)

{{% /alert %}}

이 주제는 PHP 애플리케이션에서 Aspose.PDF for PHP via Java를 사용하여 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다. PHP를 사용하여 PDF 페이지를 단일 페이지 PDF 파일로 분할하려면 다음 단계를 따를 수 있습니다:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) 컬렉션을 통해 PDF 문서의 페이지를 반복합니다.

1. 각 반복마다 새로운 Document 객체를 생성하고 개별 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 객체를 빈 문서에 추가합니다.
1. Save 메서드를 사용하여 새 PDF를 저장합니다.

다음 PHP 코드 스니펫은 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다.

```php

    // 문서 열기
    $document = new Document($inputFile);
    $pages = $document->getPages();
    $pagesSize = java_values($pages->size());
       
    // 모든 페이지를 반복
    for ($pageCount = 1; $pageCount <= $pagesSize; $pageCount++) {
        $page = $pages->get_Item($pageCount);
        $newDocument = new Document();
        $newDocument->getPages()->add($page);
        $newDocument->save($outputFile . "page_" . $pageCount . ".pdf");
        $newDocument->close();
    }
    $document->close();
```