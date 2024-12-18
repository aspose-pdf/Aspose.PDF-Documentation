---
title: PDF 페이지 이동
linktitle: 페이지 이동
type: docs
weight: 20
url: /ko/java/move-pages/
description: Aspose.PDF for Java를 사용하여 원하는 위치 또는 PDF 파일의 끝으로 페이지를 이동해 보세요.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 한 PDF 문서에서 다른 PDF 문서로 페이지 이동

이 주제에서는 Java를 사용하여 한 PDF 문서의 페이지를 다른 문서의 끝으로 이동하는 방법을 설명합니다.
페이지를 이동하려면 다음을 수행해야 합니다:

1. 소스 PDF 파일로 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스 객체를 생성합니다.
1. 대상 PDF 파일로 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스 객체를 생성합니다.
1. [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) 컬렉션에서 페이지를 가져옵니다.
1. 페이지를 대상 문서에 추가합니다.
1. Save 메서드를 사용하여 출력 PDF를 저장합니다.
1. 소스 문서에서 페이지를 삭제합니다.
1. Save 메서드를 사용하여 소스 PDF를 저장합니다.

다음 코드 조각은 페이지 하나를 이동하는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleMovePDFPages {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void MovePage() {
    String srcFileName = _dataDir + "<파일 이름 입력>";
    String dstFileName = _dataDir + "<파일 이름 입력>";
    Document srcDocument = new Document();
    Document dstDocument = new Document();
    Page page = srcDocument.getPages().get_Item(2);
    dstDocument.getPages().add(page);
    // 출력 파일 저장
    dstDocument.save(srcFileName);
    srcDocument.getPages().delete(2);
    srcDocument.save(dstFileName);
  }
```

## 여러 페이지를 한 PDF 문서에서 다른 문서로 이동

1. 소스 PDF 파일로 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스 객체를 생성합니다.
1. 대상 PDF 파일로 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스 객체를 생성합니다.
1. 이동할 페이지 번호로 배열을 정의합니다.

1. 배열을 통해 루프 실행:
   1. [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) 컬렉션에서 페이지 가져오기.
   1. 페이지를 대상 문서에 추가합니다.
1. Save 메서드를 사용하여 출력 PDF를 저장합니다.
1. 배열을 사용하여 소스 문서에서 페이지 삭제.
1. Save 메서드를 사용하여 소스 PDF를 저장합니다.

다음 코드 스니펫은 PDF 파일 끝에 빈 페이지를 삽입하는 방법을 보여줍니다.

```java
  public static void MoveBunchPages() {
    String srcFileName = _dataDir + "<파일 이름 입력>";
    String dstFileName = _dataDir + "<파일 이름 입력>";
    Document srcDocument = new Document(srcFileName);
    Document dstDocument = new Document();

    Integer[] pages = { 1, 3 };
    for (int pageIndex : pages) {
      Page page = srcDocument.getPages().get_Item(pageIndex);
      dstDocument.getPages().add(page);
    }
    // 출력 파일 저장
    dstDocument.save(srcFileName);
    srcDocument.getPages().delete(pages);

    srcDocument.save(dstFileName);
  }
```

## 현재 PDF 문서의 새 위치로 페이지 이동

1. 소스 PDF 파일로 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스 객체를 생성합니다.
1. [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection) 컬렉션에서 페이지를 가져옵니다.
1. 페이지를 새로운 위치에 추가합니다 (예: 끝에).
1. 이전 위치에서 페이지를 삭제합니다.
1. Save 메서드를 사용하여 출력 PDF를 저장합니다.

```java
  public static void MovePagesInOnePDF() {
    String srcFileName = _dataDir + "<파일 이름 입력>";
    String dstFileName = _dataDir + "<파일 이름 입력>";

    Document srcDocument = new Document(srcFileName);
    Page page = srcDocument.getPages().get_Item(2);
    srcDocument.getPages().add(page);
    srcDocument.getPages().delete(2);

    // 출력 파일 저장
    srcDocument.save(dstFileName);
  }
}
```