---
title: 북마크 가져오기, 업데이트 및 확장 
linktitle: 북마크 가져오기, 업데이트 및 확장
type: docs
weight: 20
url: ko/cpp/get-update-and-expand-bookmark/
description: Aspose.PDF for C++ 라이브러리를 사용하여 PDF 파일에서 업데이트할 수 있습니다.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 북마크 가져오기

[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) 객체의 [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection) 컬렉션에는 PDF 파일의 모든 북마크가 포함되어 있습니다. 이 문서에서는 PDF 파일에서 북마크를 가져오는 방법과 특정 북마크가 있는 페이지를 가져오는 방법을 설명합니다.

북마크를 가져오려면 [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection) 컬렉션을 반복하여 OutlineItemCollection에서 각 북마크를 가져옵니다. The OutlineItemCollection는 모든 북마크의 속성에 접근할 수 있게 해줍니다. 다음 코드 스니펫은 PDF 파일에서 북마크를 가져오는 방법을 보여줍니다.

```cpp
void GettingBookmarks() {

String _dataDir("C:\\Samples\\Bookmarks\\");

// 문서 열기

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// 모든 북마크 순회

for (auto outlineItem : pdfDocument->get_Outlines()) {


Console::WriteLine(u"제목 :- " + outlineItem->get_Title());


Console::WriteLine(u"기울임꼴 여부 :- " + outlineItem->get_Italic());


Console::WriteLine(u"볼드체 여부 :- " + outlineItem->get_Bold());


Console::WriteLine(u"색상 :- {0}", outlineItem->get_Color());

}
}
```

## 북마크의 페이지 번호 가져오기

북마크를 추가한 후에는 북마크 객체와 연관된 목적지 PageNumber를 얻어 그것이 어떤 페이지에 있는지 알 수 있습니다.

```cpp
void GettingBookmarksPageNumber() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// PdfBookmarkEditor 생성

auto bookmarkEditor = MakeObject<Aspose::Pdf::Facades::PdfBookmarkEditor>();

// PDF 파일 열기

bookmarkEditor->BindPdf(_dataDir + u"UpdateBookmarks.pdf");

// 북마크 추출

auto bookmarks = bookmarkEditor->ExtractBookmarks();

for (auto bookmark : bookmarks) {


String strLevelSeprator("");


for (int i = 1; i < bookmark->get_Level(); i++) {



strLevelSeprator += u"---- ";


}


Console::WriteLine(u"제목 :- " + strLevelSeprator + bookmark->get_Title());


Console::WriteLine(u"페이지 번호 :- " + strLevelSeprator + bookmark->get_PageNumber());


Console::WriteLine(u"페이지 액션 :- " + strLevelSeprator + bookmark->get_Action());

}
}
```
## PDF 문서에서 북마크 업데이트하기

PDF 파일에서 북마크를 업데이트하려면 먼저 북마크의 인덱스를 지정하여 Document 객체의 OutlineColletion 컬렉션에서 특정 북마크를 가져옵니다. [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection) 객체로 북마크를 가져온 후, 그 속성을 업데이트하고 Save 메서드를 사용하여 업데이트된 PDF 파일을 저장할 수 있습니다. 다음 코드 스니펫은 PDF 문서에서 북마크를 업데이트하는 방법을 보여줍니다.

```cpp
void UpdateBookmarksInPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// 문서 열기

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// 북마크 객체 가져오기

auto pdfOutline = pdfDocument->get_Outlines()->idx_get(1);


// 북마크 객체 업데이트

pdfOutline->set_Title(u"Updated Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);

// 대상 페이지를 2로 설정

pdfOutline->set_Destination(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));


// 출력 저장

pdfDocument->Save(_dataDir + u"Bookmarkupdated_output.pdf");
}
```

## PDF 문서에서 자식 북마크 업데이트하기

자식 북마크를 업데이트하려면:

1. 먼저 부모 북마크를 가져온 후 적절한 인덱스 값을 사용하여 PDF 파일에서 업데이트하려는 자식 북마크를 검색합니다.
1. Save 메소드를 사용하여 업데이트된 PDF 파일을 저장합니다.

{{% alert color="primary" %}}

Document 객체의 OutlineCollection 컬렉션에서 북마크의 인덱스를 지정하여 북마크를 가져온 다음, 이 부모 북마크의 인덱스를 지정하여 자식 북마크를 가져옵니다.

{{% /alert %}}

다음 코드 스니펫은 PDF 문서에서 자식 북마크를 업데이트하는 방법을 보여줍니다.

```cpp
void UpdateChildBookmarksInPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// 문서 열기

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// 북마크 객체 가져오기

auto pdfOutline = pdfDocument->get_Outlines()->idx_get(1);

// 자식 북마크 객체 가져오기

auto childOutline = pdfOutline->idx_get(1);


// 북마크 객체 업데이트

childOutline->set_Title(u"Updated Outline");

childOutline->set_Italic(true);

childOutline->set_Bold(true);

// 대상 페이지를 2로 설정

childOutline->set_Destination(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));


// 출력 저장

pdfDocument->Save(_dataDir + u"Bookmarkupdated_output.pdf");
}
```

## 문서 보기 시 확장된 북마크

북마크는 Document 객체의 [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection) 컬렉션에 보관되며, 이는 [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection) 컬렉션에 포함되어 있습니다. 그러나 PDF 파일을 볼 때 모든 북마크가 확장되도록 하는 요구 사항이 있을 수 있습니다.

이 요구 사항을 달성하기 위해 각 윤곽/북마크 항목의 열기 상태를 Open으로 설정할 수 있습니다. 다음 코드 스니펫은 PDF 문서에서 각 북마크의 열기 상태를 확장된 상태로 설정하는 방법을 보여줍니다.

```cpp
void ExpandedBookmarks() {


String _dataDir("C:\\Samples\\Bookmarks\\");


auto doc = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// 페이지 보기 모드 설정 예: 썸네일 보기, 전체 화면, 첨부 파일 패널 보기

doc->set_PageMode(PageMode::UseOutlines);

// PDF 파일의 북마크 총 개수 출력

Console::WriteLine(doc->get_Outlines()->get_Count());

// PDF 파일의 윤곽 컬렉션에서 각 윤곽 항목을 순회

for (int counter = 1; counter <= doc->get_Outlines()->get_Count(); counter++) {


// 윤곽 항목의 열기 상태 설정


doc->get_Outlines()->idx_get(counter)->set_Open(true);

}

// PDF 파일 저장

doc->Save(_dataDir + u"Bookmarks_Expanded.pdf");
}
```