```
title: 북마크 추가 및 삭제
linktitle: 북마크 추가 및 삭제
type: docs
weight: 10
url: /cpp/add-and-delete-bookmark/
description: 이 주제는 C++ 라이브러리를 사용하여 PDF 문서에 북마크를 추가하는 방법을 설명합니다. 또한 PDF 문서에서 모든 북마크 또는 특정 북마크를 삭제할 수 있습니다.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF 문서에 북마크 추가

북마크는 Document 객체의 [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection/) 컬렉션에 포함되어 있으며, 이는 [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) 컬렉션에 포함되어 있습니다.

PDF에 북마크를 추가하려면:

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) 객체를 사용하여 PDF 문서를 엽니다.
1. 북마크를 생성하고 그 속성을 정의합니다.
1.
``` [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) 컬렉션을 Outlines 컬렉션에 추가합니다.

다음 코드 스니펫은 PDF 문서에 책갈피를 추가하는 방법을 보여줍니다.

```cpp
void AddBookmarks() {


String _dataDir("C:\\Samples\\Bookmarks\\");

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddBookmark.pdf");


// Create a bookmark object

auto pdfOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfOutline->set_Title(u"Test Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);


// Set the destination page number

pdfOutline->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));


// Add a bookmark in the document's outline collection.

pdfDocument->get_Outlines()->Add(pdfOutline);


// Save the update document

pdfDocument->Save(_dataDir + u"AddBookmark_out.pdf");
}
```

## PDF 문서에 자식 책갈피 추가하기

책갈피는 중첩될 수 있으며, 이는 부모와 자식 책갈피 간의 계층적 관계를 나타냅니다. 이 문서에서는 PDF에 두 번째 수준의 책갈피인 하위 책갈피를 추가하는 방법을 설명합니다.

PDF 파일에 하위 책갈피를 추가하려면 먼저 상위 책갈피를 추가합니다:

1. 문서를 엽니다.
1. [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection/)에 책갈피를 추가하고, 속성을 정의합니다.
1. OutlineItemCollection을 Document 객체의 [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) 컬렉션에 추가합니다.

하위 책갈피는 앞서 설명한 상위 책갈피와 동일한 방식으로 생성되지만, 상위 책갈피의 Outlines 컬렉션에 추가됩니다.

다음 코드 스니펫은 PDF 문서에 하위 책갈피를 추가하는 방법을 보여줍니다.

```cpp
void AddChildBookmark() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// 문서 열기

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddChildBookmark.pdf");


// 상위 책갈피 객체 생성

auto pdfOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfOutline->set_Title(u"Parent Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);


// 하위 책갈피 객체 생성

auto pdfChildOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfChildOutline->set_Title(u"Child Outline");

pdfChildOutline->set_Italic(true);

pdfChildOutline->set_Bold(true);


// 상위 책갈피의 컬렉션에 하위 책갈피 추가

pdfOutline->Add(pdfChildOutline);

// 문서의 개요 컬렉션에 상위 책갈피 추가.

pdfDocument->get_Outlines()->Add(pdfOutline);


// 출력 저장

pdfDocument->Save(_dataDir + u"AddChildBookmark_out.pdf");
}
```
## PDF 문서에서 모든 북마크 삭제하기

모든 북마크는 [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) 컬렉션에 저장됩니다. 이 글에서는 PDF 파일에서 모든 북마크를 삭제하는 방법을 설명합니다.

PDF 파일에서 모든 북마크를 삭제하려면:

1. [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) 컬렉션의 Delete 메서드를 호출합니다.
1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) 객체의 Save 메서드를 사용하여 수정된 파일을 저장합니다.

다음 코드 스니펫은 PDF 문서에서 모든 북마크를 삭제하는 방법을 보여줍니다.

```cpp
void DeleteAllBookmarksFromPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// 문서 열기

auto pdfDocument = MakeObject<Document>(_dataDir + u"DeleteAllBookmarks.pdf");


// 모든 북마크 삭제

pdfDocument->get_Outlines()->Delete();


// 업데이트된 파일 저장

pdfDocument->Save(_dataDir + u"DeleteAllBookmarks_out.pdf");
}
```


## PDF 문서에서 특정 북마크 삭제하기

[PDF 문서에서 모든 첨부 파일 삭제](https://docs.aspose.com/pdf/cpp/working-with-attachments/)는 PDF 파일에서 모든 첨부 파일을 삭제하는 방법을 보여줍니다. 특정 첨부 파일만 제거하는 것도 가능합니다.

PDF 파일에서 특정 책갈피를 삭제하려면:

1. [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) 컬렉션의 Delete 메서드에 책갈피의 제목을 매개변수로 전달합니다.
1. 그런 다음 Document 객체의 Save 메서드를 사용하여 업데이트된 파일을 저장합니다.

[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) 클래스는 [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) 컬렉션을 제공합니다. [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection#a04f36a1f4f7c4fde3189399eb046a98b) 메서드는 메서드에 전달된 제목을 가진 모든 책갈피를 제거합니다.

다음 코드 스니펫은 PDF 문서에서 특정 책갈피를 삭제하는 방법을 보여줍니다.

```cpp
void DeleteParticularBookmarkPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// 문서 열기

auto pdfDocument = MakeObject<Document>(_dataDir + u"DeleteParticularBookmark.pdf");


// 제목으로 특정 개요 삭제

pdfDocument->get_Outlines()->Delete(u"Child Outline");


// 업데이트된 파일 저장

pdfDocument->Save(_dataDir + u"DeleteParticularBookmark_out.pdf");
}
```