---
title: 책갈피 만들기
type: docs
weight: 10
url: /ko/net/create-bookmarks/
description: 이 섹션에서는 PdfBookmarEditor 클래스를 사용하여 Aspose.PDF Facades로 PDF 파일에 책갈피를 만드는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## 모든 페이지의 책갈피 만들기

모든 페이지의 책갈피를 만들려면 매개 변수를 사용하지 않고 [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) 메서드를 사용해야 합니다. [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스는 PDF 파일의 모든 페이지에 책갈피를 만들 수 있도록 합니다. 먼저, [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 입력 PDF를 바인딩해야 합니다. 그런 다음, [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) 메서드를 호출하고 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 출력 PDF 파일을 저장해야 합니다. 다음 코드 조각은 북마크를 생성하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarksAll-CreateBookmarksAll.cs" >}}

## 모든 페이지에 속성이 있는 북마크 생성

[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스는 PDF 파일의 모든 페이지에 대한 북마크를 생성하고 속성(색상, 굵게, 기울임꼴)을 지정할 수 있도록 합니다. 다음은 [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) 메소드를 사용하여 할 수 있습니다. 먼저, [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메소드를 사용하여 입력 PDF를 바인딩해야 합니다. 그런 다음, [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) 메소드를 호출하고 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메소드를 사용하여 출력 PDF 파일을 저장해야 합니다. 다음 코드 스니펫은 모든 페이지의 북마크를 속성과 함께 생성하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarksPagesProperties-CreateBookmarksPagesProperties.cs" >}}

## 특정 페이지의 북마크 생성

[CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) 메소드를 사용하여 기존 PDF 파일의 특정 페이지에 대한 북마크를 생성할 수 있습니다. 이 메서드는 두 개의 인수를 받습니다: 책갈피 제목과 페이지 번호입니다. 먼저, [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그런 다음, [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) 메서드를 호출하고 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 출력 PDF 파일을 저장해야 합니다. 다음 코드 스니펫은 특정 페이지의 책갈피를 생성하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarkPage-CreateBookmarkPage.cs" >}}

## 여러 페이지의 범위에 대한 책갈피 생성

[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스는 여러 페이지의 범위에 대한 책갈피를 생성할 수 있도록 합니다. 문서의 텍스트는 다음과 같습니다:
[CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) 메소드는 두 개의 매개변수를 사용합니다: 북마크 목록 (북마크 제목의 목록) 및 페이지 목록 (북마크를 설정할 페이지 목록). 먼저, [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메소드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그런 다음, [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) 메소드를 호출하고 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메소드를 사용하여 출력 PDF를 저장해야 합니다. 다음 코드 스니펫은 여러 페이지 범위의 북마크를 생성하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarkPageRange-CreateBookmarkPageRange.cs" >}}
## 기존 PDF 파일에 북마크 추가

[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스를 사용하여 기존 PDF 파일에 북마크를 추가할 수 있습니다. 북마크를 생성하기 위해서는 [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) 객체를 생성하고 북마크의 필요한 속성을 설정해야 합니다. 그 후, [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스의 [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) 메서드에 [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) 객체를 전달해야 합니다. 마지막으로, [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 업데이트된 PDF 파일을 저장해야 합니다. 다음 코드 스니펫은 기존 PDF 파일에 북마크를 추가하는 방법을 보여줍니다.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-AddBookmark-AddBookmark.cs" >}}

## 기존 PDF 파일에 하위 북마크 추가

[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스를 사용하여 기존 PDF 파일에 하위 북마크를 추가할 수 있습니다. In order to add child bookmarks, you need to create [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) objects.

자식 북마크를 추가하려면 [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) 객체를 생성해야 합니다. ```
You can add individual [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) objects into [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks) object.
개별 [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) 객체를 [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks) 객체에 추가할 수 있습니다.
``` 당신은 또한 [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) 객체를 생성하고 [ChildItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem) 속성을 [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks) 객체로 설정해야 합니다. 그런 다음 이 [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) 객체를 [ChildItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem)과 함께 [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) 메서드에 전달해야 합니다. 마지막으로, [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 업데이트된 PDF를 저장해야 합니다. 다음 코드 스니펫은 기존 PDF 파일에 하위 북마크를 추가하는 방법을 보여줍니다.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-AddChildBookmark-AddChildBookmark.cs" >}}
## See also

비교하고 자신에게 맞는 북마크 작업 방법을 찾아보세요. [PDF에서 북마크 작업하기](/pdf/ko/net/bookmarks/) 섹션을 학습해 봅시다.