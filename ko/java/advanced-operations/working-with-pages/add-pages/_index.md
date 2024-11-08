---
title: PDF에 페이지 추가 
linktitle: 페이지 추가
type: docs
weight: 10
url: /ko/java/add-pages/
description: 이 문서는 원하는 위치에 PDF 파일에 페이지를 삽입(추가)하는 방법을 가르칩니다. Java 라이브러리를 사용하여 PDF 파일에서 페이지를 이동하고 제거(삭제)하는 방법을 배웁니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 파일에 페이지 추가 또는 삽입

Aspose.PDF for Java를 사용하면 파일의 원하는 위치에 PDF 문서에 페이지를 삽입할 수 있으며 PDF 파일의 끝에 페이지를 추가할 수도 있습니다. 빈 페이지를 삽입하고자 하는 위치를 insert 메서드에 전달해야 합니다. 이 섹션에서는 Aspose.PDF for Java를 사용하여 PDF에 페이지를 추가하는 방법을 보여줍니다.

### 원하는 위치에 PDF 파일에 빈 페이지 삽입

다음 코드 스니펫은 PDF 파일에 빈 페이지를 삽입하는 방법을 보여줍니다:

1. 입력 PDF 파일로 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스 객체를 생성합니다.

1. [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) 컬렉션의 Insert 메소드를 지정된 인덱스로 호출하십시오.
1. Save 메소드를 사용하여 출력 PDF를 저장하십시오.

다음 코드 스니펫은 PDF 파일에 페이지를 삽입하는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddPages {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void InsertEmptyPageInPDFFileAtDesiredLocation() {
        Document document = new Document();

        // 페이지 추가
        document.getPages().add();

        // PDF에 빈 페이지 삽입
        document.getPages().insert(2);

        // 업데이트된 PDF 저장
        document.save(_dataDir + "InsertEmptyPage_out.pdf");
    }
```

위의 예제에서는 기본 매개변수로 빈 페이지를 추가했습니다. 문서의 다른 페이지와 동일한 크기로 페이지 크기를 설정하려면 몇 줄의 코드를 추가해야 합니다:

```java
    public static void InsertEmptyPageInPDFFileAtDesiredLocation01() {
        Document document = new Document();

        // 페이지 추가
        Page page1 = document.getPages().add();

        // PDF에 빈 페이지 삽입
        Page page2 = document.getPages().insert(2);

        // 페이지 1의 매개변수를 복사
        page2.setArtBox(page1.getArtBox());
        page2.setBleedBox(page1.getBleedBox());
        page2.setCropBox(page1.getCropBox());
        page2.setMediaBox(page1.getMediaBox());
        page2.setTrimBox(page1.getTrimBox());

        // 업데이트된 PDF 저장
        document.save(_dataDir + "InsertEmptyPage_out.pdf");
    }
```


### PDF 파일의 끝에 빈 페이지 추가

때때로 문서가 빈 페이지로 끝나도록 하고 싶을 때가 있습니다. 이 주제는 PDF 문서의 끝에 빈 페이지를 삽입하는 방법을 설명합니다.

PDF 파일의 끝에 빈 페이지를 삽입하려면:

1. 입력 PDF 파일로 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스 객체를 생성합니다.
1. 매개 변수 없이 [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection) 컬렉션의 Add 메서드를 호출합니다.
1. Save 메서드를 사용하여 출력 PDF를 저장합니다.

다음 코드 조각은 PDF 파일의 끝에 빈 페이지를 삽입하는 방법을 보여줍니다.

```java
public static void AddAnEmptyPageAtTheEndOfAPDFFile() {

        Document document = new Document();
        // 페이지 추가
        document.getPages().add();

        // PDF 파일의 끝에 빈 페이지 삽입
        document.getPages().add();

        // 업데이트된 PDF 저장
        document.save(_dataDir + "InsertEmptyPageAtEnd_out.pdf");
    }

}
```