---
title: PDF 문서 생성
linktitle: 생성
type: docs
weight: 10
url: ko/php-java/create-document/
description: Aspose.PDF for PHP via Java에서 PDF 파일을 생성하는 방법을 배웁니다.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for PHP via Java** API는 응용 프로그램 개발자가 응용 프로그램에 PDF 문서 처리 기능을 포함시킬 수 있게 해줍니다. 이는 기본 시스템에 다른 소프트웨어를 설치할 필요 없이 PDF 파일을 생성하고 읽는 데 사용될 수 있습니다. Aspose.PDF for PHP via Java는 데스크톱, JSP 및 JSF 응용 프로그램과 같은 다양한 응용 프로그램 유형에서 사용할 수 있습니다.

## PHP를 통해 Java로 PDF 파일 생성하는 방법

PHP를 통해 Java로 PDF 파일을 생성하려면 다음 단계를 사용할 수 있습니다.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체를 인스턴스화합니다.
1. 문서 객체에 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)를 추가합니다.

1. [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment) 객체를 생성합니다.
1. [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment)를 페이지의 [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) 컬렉션에 추가합니다.
1. 결과 PDF 문서를 저장합니다.

```php

    $document = new Document();    
    $page = $document->getPages()->add();
    $textFragment = new TextFragment("Hello World!");    
    $page->getParagraphs()->add($textFragment);
    $document->save($outputFile);
```