---
title: PDF 파일에 링크 생성
linktitle: 링크 생성
type: docs
weight: 10
url: /java/create-links/
description: 이 섹션에서는 Java로 PDF 문서에 링크를 생성하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 링크 생성

Aspose.PDF for Java를 사용하면 외부 PDF 파일에 링크를 추가하여 여러 문서를 함께 연결할 수 있습니다. 문서에 애플리케이션 링크를 추가하면 문서에서 애플리케이션으로 연결할 수 있습니다. 이는 예를 들어 튜토리얼의 특정 지점에서 독자가 특정 작업을 수행하도록 하고 싶거나, 기능이 풍부한 문서를 만들고 싶을 때 유용합니다. 애플리케이션 링크를 만들려면:

1. [문서](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체를 생성합니다.
2. 링크를 추가할 [페이지](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)를 가져옵니다.

1. [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 및 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) 객체를 사용하여 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) 객체를 생성합니다.
1. [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) 객체를 사용하여 링크 속성을 설정합니다.
1. 또한 [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaunchAction) 객체로 설정하고 setAction(..) 메서드를 호출합니다.
1. [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaunchAction) 객체를 생성할 때 실행하고자 하는 애플리케이션을 지정합니다.
1. 링크를 Page 객체의 [Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationCollection) 컬렉션에 추가합니다.
1. 마지막으로 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 Save 메서드를 사용하여 업데이트된 PDF를 저장합니다.

다음 코드 스니펫은 PDF 파일에서 애플리케이션에 대한 링크를 만드는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;


public class ExampleLinks {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Links-Actions";
        return _dataDir;
    }

    public static void CreateLink() {

        // 문서 열기
        Document document = new Document(GetDataDir() + "CreateApplicationLink.pdf");

        // 링크 생성
        Page page = document.getPages().get_Item(1);
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 200, 300, 300));
        link.setColor(Color.getGreen());
        link.setAction(new LaunchAction(document, _dataDir + "sample.pdf"));
        page.getAnnotations().add(link);

        // 업데이트된 문서 저장
        document.save(_dataDir + "CreateApplicationLink_out.pdf");
    }
```

### PDF 파일에 PDF 문서 링크 생성

Aspose.PDF for Java를 사용하면 외부 PDF 파일에 링크를 추가하여 여러 문서를 함께 연결할 수 있습니다.
 PDF 문서 링크를 생성하려면:

1. 먼저, [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체를 생성합니다.
1. 그런 다음, 링크를 추가하고자 하는 특정 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)를 가져옵니다.
1. [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 및 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) 객체를 사용하여 [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) 객체를 생성합니다.
1. [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) 객체를 사용하여 링크 속성을 설정합니다.
1. setAction(..) 메서드를 호출하고 [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToRemoteAction) 객체를 전달합니다.
1. [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToRemoteAction) 객체를 생성할 때, 실행할 PDF 파일과 열어야 할 페이지 번호를 지정합니다.
1. 링크를 Page 객체의 [Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationCollection) 컬렉션에 추가합니다.
1. 마지막으로, [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 Save 메서드를 사용하여 업데이트된 PDF를 저장합니다.

다음 코드 스니펫은 PDF 파일에서 PDF 문서 링크를 생성하는 방법을 보여줍니다.

```java
    public static void CreatePDFDocumentLink() {

        // 문서 열기
        Document document = new Document(_dataDir + "CreateDocumentLink.pdf");

        // 링크 생성
        Page page = document.getPages().get_Item(1);
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 200, 300, 300));
        link.setColor(Color.getGreen());
        link.setAction(new GoToRemoteAction(_dataDir + "sample.pdf", 1));
        page.getAnnotations().add(link);

        // 업데이트된 문서 저장
        document.save(_dataDir + "CreateDocumentLink_out.pdf");
    }
```