---
title: PDF 문서 생성
linktitle: 생성
type: docs
weight: 10
url: /java/create-document/
description: Aspose.PDF for Java에서 PDF 파일을 생성하는 방법을 배우세요.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Java** API는 Java 애플리케이션 개발자가 애플리케이션에 PDF 문서 처리 기능을 포함할 수 있도록 합니다. 이는 기본 시스템에 다른 소프트웨어가 설치되어 있지 않아도 PDF 파일을 생성하고 읽는 데 사용할 수 있습니다. Aspose.PDF for Java는 데스크탑, JSP, JSF 애플리케이션과 같은 다양한 Java 애플리케이션 유형에서 사용할 수 있습니다.

## Java를 사용하여 PDF 파일을 생성하는 방법

Java를 사용하여 PDF 파일을 생성하려면 다음 단계를 사용할 수 있습니다.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체 인스턴스화
1. 문서 객체에 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 추가
1. [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment) 객체 생성

1. [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment)를 페이지의 [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) 컬렉션에 추가합니다.
1. 결과 PDF 문서를 저장합니다.

```java
// 문서 객체 초기화
Document document = new Document();
 
// 페이지 추가
Page page = document.getPages().add();
 
// 새 페이지에 텍스트 추가
page.getParagraphs().add(new TextFragment("Hello World!"));
 
// 업데이트된 PDF 저장
document.save("HelloWorld_out.pdf");
```