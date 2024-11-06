---
title: 자바를 통한 PHP의 Hello World 예제
linktitle: Hello World 예제
type: docs
weight: 40
url: ko/php-java/hello-world-example/
description: 이 페이지는 Aspose.PDF for PHP via Java를 사용하여 'Hello World' 텍스트가 포함된 PDF 문서를 생성하는 간단한 프로그래밍 방법을 보여줍니다.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Hello World 예제

“Hello World” 예제는 일반적으로 프로그래밍 언어나 소프트웨어의 기본 기능을 간단한 사용 사례로 보여주는 데 사용됩니다.

Aspose.PDF for PHP via Java API를 사용하면 개발자가 자바 응용 프로그램 내에서 PDF 파일을 생성, 읽기, 편집 및 조작할 수 있습니다. 다양한 파일 형식을 PDF 형식으로 읽고 변환하는 것을 지원합니다. 이 Hello World 글에서는 Aspose.PDF for PHP via Java API를 사용하여 PDF 파일을 생성하는 방법을 보여줍니다. 환경에 [Aspose.PDF for PHP via Java 설치](/pdf/php-java/installation/)를 완료한 후, 아래 코드 샘플을 실행하여 Aspose.PDF API가 어떻게 작동하는지 확인할 수 있습니다.

아래 코드 스니펫은 다음 단계를 따릅니다:


1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document) 객체를 인스턴스화합니다.
1. Document 객체에 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page)를 추가합니다.
1. [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) 객체를 생성합니다.
1. 페이지의 [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) 컬렉션에 TextFragment를 추가합니다.
1. 결과 PDF 문서를 저장합니다.

다음 코드 스니펫은 Java API를 통해 PHP용 Aspose.PDF의 작동을 보여주는 Hello World 프로그램입니다.

```php
    $document = new Document();    
    $page = $document->getPages()->add();
    $textFragment = new TextFragment("Hello World!");    
    $page->getParagraphs()->add($textFragment);
    $document->save($outputFile);
```