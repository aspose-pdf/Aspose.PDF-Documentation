---
title: PDF 페이지 크기 프로그램으로 변경하기
linktitle: 페이지 크기 변경
type: docs
weight: 50
url: /java/change-page-size/
description: Java 라이브러리를 사용하여 PDF 파일의 페이지 크기를 변경합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 페이지 크기 변경

Aspose.PDF for Java를 사용하면 Java 애플리케이션에서 간단한 코드로 PDF 페이지 크기를 변경할 수 있습니다. 이 주제에서는 기존 PDF 파일의 페이지 크기(치수)를 업데이트/변경하는 방법을 설명합니다.

[Page](https://reference.aspose.com/pdf//java/com.aspose.pdf/page) 클래스에는 페이지 크기를 설정할 수 있는 SetPageSize(...) 메서드가 포함되어 있습니다. 아래의 코드 스니펫은 몇 가지 간단한 단계로 페이지 치수를 업데이트합니다:

1. 소스 PDF 파일을 로드합니다.
2. [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) 객체에 페이지를 가져옵니다.
3. 주어진 페이지를 가져옵니다.
4. SetPageSize(..) 메서드를 호출하여 치수를 업데이트합니다.

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스의 Save(..) 메서드를 호출하여 업데이트된 페이지 크기로 PDF 파일을 생성합니다.

{{% alert color="primary" %}}

높이와 너비 속성은 기본 단위로 포인트를 사용하며, 1 인치 = 72 포인트, 1 cm = 1/2.54 인치 = 0.3937 인치 = 28.3 포인트입니다.

{{% /alert %}}

다음 코드 스니펫은 PDF 페이지 크기를 A4 크기로 변경하는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleChangePDFPageSize {
    // 문서 디렉토리의 경로입니다.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ChangePDFPageSize() {
        
        // 첫 번째 문서 열기
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
                
        // 페이지 컬렉션 가져오기
        PageCollection pageCollection = pdfDocument.getPages();

        // 특정 페이지 가져오기
        Page pdfPage = pageCollection.get_Item(1);

        // 페이지 크기를 A4 (11.7 x 8.3 인치)로 설정하고 Aspose.Pdf에서 1 인치 = 72 포인트입니다.
        // 따라서 A4 크기는 포인트로 (842.4, 597.6)입니다.
        pdfPage.setPageSize(597.6, 842.4);

        _dataDir = _dataDir + "UpdateDimensions_out.pdf";
        
        // 업데이트된 문서 저장
        pdfDocument.save(_dataDir);
    }
```


## PDF 페이지 크기 가져오기

Aspose.PDF for Java를 사용하여 기존 PDF 파일의 PDF 페이지 크기를 읽을 수 있습니다. 다음 코드 샘플은 Java를 사용하여 PDF 페이지 크기를 읽는 방법을 보여줍니다.

```java
    public static void GetPDFPageSize() {
        
        // 첫 번째 문서 열기
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
                
        // 빈 페이지를 PDF 문서에 추가
        Page page = pdfDocument.getPages().size() > 0 ? pdfDocument.getPages().get_Item(1) : pdfDocument.getPages().add();
        
        // 페이지 높이 및 너비 정보 가져오기
        System.out.println(page.getPageRect(true).getWidth() + ":" + page.getPageRect(true).getHeight());
        
        // 페이지를 90도 각도로 회전
        page.setRotate (Rotation.on90);

        // 페이지 높이 및 너비 정보 가져오기
        System.out.println(page.getPageRect(true).getWidth() + ":" + page.getPageRect(true).getHeight());
        
        // 업데이트된 문서 저장
        _dataDir = _dataDir + "UpdateDimensions_out.pdf";
        pdfDocument.save(_dataDir);
    }

}
```