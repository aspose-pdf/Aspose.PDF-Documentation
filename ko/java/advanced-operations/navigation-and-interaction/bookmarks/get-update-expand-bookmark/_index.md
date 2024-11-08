---
title: 북마크 가져오기, 업데이트 및 확장
linktitle: 북마크 가져오기, 업데이트 및 확장
type: docs
weight: 20
url: /ko/java/get-update-and-expand-bookmark/
description: 이 문서는 PDF 파일에서 북마크를 사용하는 방법을 설명합니다. Java 라이브러리를 사용하여 PDF 파일에서 북마크를 가져오고, 북마크의 페이지 번호를 얻고, PDF 문서에서 북마크를 업데이트하고, 문서를 볼 때 북마크를 확장할 수 있습니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 북마크 가져오기

[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 객체의 [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) 컬렉션에는 PDF 파일의 모든 북마크가 포함되어 있습니다. 이 문서는 PDF 파일에서 북마크를 가져오는 방법과 특정 북마크가 어느 페이지에 있는지를 얻는 방법을 설명합니다.

북마크를 가져오기 위해 [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) 컬렉션을 반복하고 OutlineItemCollection에서 각 북마크를 가져옵니다.
 The OutlineItemCollection은 모든 책갈피 속성에 대한 접근을 제공합니다. 다음 코드 스니펫은 PDF 파일에서 책갈피를 가져오는 방법을 보여줍니다.

```java
    public static void GettingBookmarks() {
        // 문서 열기
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // 모든 책갈피를 순회
        for (OutlineItemCollection outlineItem : (Iterable<OutlineItemCollection>) pdfDocument.getOutlines()) {
            System.out.println("제목 :- " + outlineItem.getTitle());
            System.out.println("기울임꼴 :- " + outlineItem.getItalic());
            System.out.println("굵게 :- " + outlineItem.getBold());
            System.out.println("색상 :- " + outlineItem.getColor());
        }
    }
```

## 책갈피의 페이지 번호 가져오기

책갈피를 추가한 후에는 Bookmark 객체와 연결된 목적지 PageNumber를 얻어 책갈피가 있는 페이지를 확인할 수 있습니다.

```java
    public static void GettingBookmarksPageNumber() {
        // PdfBookmarkEditor 생성
        PdfBookmarkEditor bookmarkEditor = new PdfBookmarkEditor();
        // PDF 파일 열기
        bookmarkEditor.bindPdf(GetDataDir() + "UpdateBookmarks.pdf");
        // 책갈피 추출
        Bookmarks bookmarks = bookmarkEditor.extractBookmarks();
        for (Bookmark bookmark : (Iterable<Bookmark>) bookmarks) {
            String strLevelSeprator = "";
            for (int i = 1; i < bookmark.getLevel(); i++) {
                strLevelSeprator += "---- ";
            }
            System.out.println("제목 :- " + strLevelSeprator + bookmark.getTitle());
            System.out.println("페이지 번호 :- " + strLevelSeprator + bookmark.getPageNumber());
            System.out.println("페이지 동작 :- " + strLevelSeprator + bookmark.getAction());
        }
    }
```

## PDF 문서의 북마크 업데이트

PDF 파일에서 북마크를 업데이트하려면 먼저 북마크의 인덱스를 지정하여 Document 객체의 OutlineCollection 컬렉션에서 특정 북마크를 가져옵니다. [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) 객체로 북마크를 가져온 후, 해당 속성을 업데이트하고 Save 메서드를 사용하여 업데이트된 PDF 파일을 저장할 수 있습니다. 다음 코드 스니펫은 PDF 문서에서 북마크를 업데이트하는 방법을 보여줍니다.

```java
    public static void UpdateBookmarksInPDFDocument() {
        // 문서 열기
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // 북마크 객체 가져오기
        OutlineItemCollection pdfOutline = pdfDocument.getOutlines().get_Item(1);

        // 북마크 객체 업데이트
        pdfOutline.setTitle("Updated Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);
        // 대상 페이지를 2로 설정
        pdfOutline.setDestination(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // 출력 저장
        pdfDocument.save(GetDataDir() + "Bookmarkupdated_output.pdf");
    }
```


## PDF 문서에서 자식 북마크 업데이트

자식 북마크를 업데이트하려면:

1. 먼저 적절한 인덱스 값을 사용하여 부모 북마크를 가져오고, 그 다음 자식 북마크를 가져와서 업데이트하려는 자식 북마크를 PDF 파일에서 검색합니다.
1. Save 메소드를 사용하여 업데이트된 PDF 파일을 저장합니다.

{{% alert color="primary" %}}

북마크의 인덱스를 지정하여 Document 객체의 OutlineCollection 컬렉션에서 북마크를 가져온 다음, 이 부모 북마크의 인덱스를 지정하여 자식 북마크를 가져옵니다.

{{% /alert %}}

다음 코드 스니펫은 PDF 문서에서 자식 북마크를 업데이트하는 방법을 보여줍니다.

```java
    public static void UpdateChildBookmarksInPDFDocument() {
        // 문서 열기
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // 북마크 객체 가져오기
        OutlineItemCollection pdfOutline = pdfDocument.getOutlines().get_Item(1);
        // 자식 북마크 객체 가져오기
        OutlineItemCollection childOutline = pdfOutline.get_Item(1);

        // 북마크 객체 업데이트
        childOutline.setTitle("Updated Outline");
        childOutline.setItalic(true);
        childOutline.setBold(true);
        // 대상 페이지를 2로 설정
        childOutline.setDestination(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // 출력 저장
        pdfDocument.save(GetDataDir() + "Bookmarkupdated_output.pdf");
    }
```


## 문서를 볼 때 확장된 책갈피

책갈피는 Document 객체의 [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) 컬렉션에 있으며, 이는 [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) 컬렉션에 포함되어 있습니다. 그러나 PDF 파일을 볼 때 모든 책갈피가 확장된 상태로 표시되기를 원하는 경우가 있을 수 있습니다.

이 요구 사항을 충족하려면 각 개요/책갈피 항목의 열림 상태를 Open으로 설정할 수 있습니다. 다음 코드 스니펫은 PDF 문서에서 각 책갈피의 열림 상태를 확장된 상태로 설정하는 방법을 보여줍니다.

```java
    public static void ExpandedBookmarks() {    
        Document doc = new Document(GetDataDir()+"UpdateBookmarks.pdf");
        // 페이지 보기 모드 설정, 즉 썸네일 표시, 전체 화면, 첨부 파일 패널 표시
        doc.setPageMode(PageMode.UseOutlines);
        // PDF 파일의 책갈피 총 개수 출력
        System.out.println(doc.getOutlines().size());
        // PDF 파일의 개요 컬렉션에서 각 개요 항목을 순회
        for (int counter = 1; counter <= doc.getOutlines().size(); counter++) {
            // 개요 항목의 열림 상태 설정
            doc.getOutlines().get_Item(counter).setOpen(true);
        }
        // PDF 파일 저장
        doc.save(_dataDir+"Bookmarks_Expanded.pdf");
    }
```