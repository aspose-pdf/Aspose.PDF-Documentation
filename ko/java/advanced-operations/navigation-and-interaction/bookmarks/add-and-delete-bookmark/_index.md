---
title: 책갈피 추가 및 삭제
linktitle: 책갈피 추가 및 삭제
type: docs
weight: 10
url: ko/java/add-and-delete-bookmark/
description: Java로 PDF 문서에 책갈피를 추가할 수 있습니다. PDF 문서에서 모든 또는 특정 책갈피를 삭제할 수 있습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서에 책갈피 추가

책갈피는 [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) 컬렉션 내의 [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) 컬렉션에 포함되어 있습니다.

PDF에 책갈피를 추가하려면:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체를 사용하여 PDF 문서를 엽니다.
2. 책갈피를 생성하고 그 속성을 정의합니다.
3. [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) 컬렉션을 Outlines 컬렉션에 추가합니다.

다음 코드 스니펫은 PDF 문서에 책갈피를 추가하는 방법을 보여줍니다.

```java
package com.aspose.pdf.examples;

import java.io.IOException;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.Bookmark;
import com.aspose.pdf.facades.Bookmarks;
import com.aspose.pdf.facades.PdfBookmarkEditor;

public class ExampleBookmarks {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Bookmarks/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Bookmarks\\";
        return _dataDir;
    }

    public static void AddBookmarks() throws IOException {

        Document pdfDocument = new Document(GetDataDir() + "AddBookmark.pdf");

        // 북마크 객체 생성
        OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfOutline.setTitle("Test Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        // 목적지 페이지 번호 설정
        pdfOutline.setAction(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // 문서의 개요 컬렉션에 북마크 추가
        pdfDocument.getOutlines().add(pdfOutline);

        // 업데이트된 문서 저장
        pdfDocument.save(_dataDir + "AddBookmark_out.pdf");
    }
```


## PDF 문서에 하위 북마크 추가하기

북마크는 중첩될 수 있으며, 이는 부모와 자식 북마크 간의 계층적 관계를 나타냅니다. 이 문서는 PDF에 2단계 북마크인 하위 북마크를 추가하는 방법을 설명합니다.

PDF 파일에 하위 북마크를 추가하려면, 먼저 부모 북마크를 추가합니다:

1. 문서를 엽니다.
1. [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection)에 북마크를 추가하고 그 속성을 정의합니다.
1. OutlineItemCollection을 Document 객체의 [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) 컬렉션에 추가합니다.

하위 북마크는 위에서 설명한 부모 북마크와 같이 생성되지만, 부모 북마크의 Outlines 컬렉션에 추가됩니다.

다음 코드 스니펫은 PDF 문서에 하위 북마크를 추가하는 방법을 보여줍니다.

```java
    public static void AddChildBookmark() {
        // 문서 열기
        Document pdfDocument = new Document(GetDataDir() + "AddChildBookmark.pdf");

        // 부모 북마크 객체 생성
        OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfOutline.setTitle("Parent Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        // 자식 북마크 객체 생성
        OutlineItemCollection pdfChildOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfChildOutline.setTitle("Child Outline");
        pdfChildOutline.setItalic(true);
        pdfChildOutline.setBold(true);

        // 부모 북마크의 컬렉션에 자식 북마크 추가
        pdfOutline.add(pdfChildOutline);
        // 문서의 아웃라인 컬렉션에 부모 북마크 추가.
        pdfDocument.getOutlines().add(pdfOutline);

        // 출력 저장
        pdfDocument.save(_dataDir + "AddChildBookmark_out.pdf");
    }
```


## PDF 문서에서 모든 북마크 삭제하기

PDF의 모든 북마크는 [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) 컬렉션에 저장됩니다. 이 문서에서는 PDF 파일에서 모든 북마크를 삭제하는 방법을 설명합니다.

PDF 파일에서 모든 북마크를 삭제하려면:

1. [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) 컬렉션의 Delete 메서드를 호출합니다.
1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 Save 메서드를 사용하여 수정된 파일을 저장합니다.

다음 코드 스니펫은 PDF 문서에서 모든 북마크를 삭제하는 방법을 보여줍니다.

```java
    public static void DeleteAllBookmarksFromPDFDocument() {
        // 문서 열기
        Document pdfDocument = new Document(GetDataDir() + "DeleteAllBookmarks.pdf");

        // 모든 북마크 삭제
        pdfDocument.getOutlines().delete();

        // 업데이트된 파일 저장
        pdfDocument.save(_dataDir + "DeleteAllBookmarks_out.pdf");
    }
```

## PDF 문서에서 특정 북마크 삭제하기

[PDF 문서에서 모든 첨부 파일 삭제하기](https://docs.aspose.com/pdf/java/working-with-attachments/)는 PDF 파일에서 모든 첨부 파일을 삭제하는 방법을 보여줍니다. 특정 첨부 파일만 삭제하는 것도 가능합니다.

PDF 파일에서 특정 북마크를 삭제하려면:

1. 북마크의 제목을 매개변수로 [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) 컬렉션의 [Delete](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection#delete--) 메서드에 전달합니다.
1. 그런 다음 Document 객체의 Save 메서드를 사용하여 업데이트된 파일을 저장합니다.

[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 클래스는 [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) 컬렉션을 제공합니다. [Delete](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection#delete--) 메서드는 메서드에 전달된 제목을 가진 모든 북마크를 제거합니다.

다음 코드 스니펫은 PDF 문서에서 특정 북마크를 삭제하는 방법을 보여줍니다.

```java
    public static void DeleteParticularBookmarkPDFDocument() {
        // 문서 열기
        Document pdfDocument = new Document(GetDataDir() + "DeleteParticularBookmark.pdf");

        // 제목에 따라 특정 북마크 삭제
        pdfDocument.getOutlines().delete("Child Outline");

        // 업데이트된 파일 저장
        pdfDocument.save(_dataDir + "DeleteParticularBookmark_out.pdf");
    }
```