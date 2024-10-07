---
title: 업데이트, 삭제 및 북마크 가져오기
type: docs
weight: 30
url: /net/update-delete-and-get-bookmarks/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 북마크를 업데이트, 삭제 및 가져오는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## PDF 파일에서 기존 북마크 업데이트

PDF 파일에서 기존 북마크를 업데이트하려면 [ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks) 메서드를 사용해야 합니다. 이 메서드는 두 개의 인수를 받습니다: 소스 제목 (수정할 북마크의 제목), 대상 제목 (교체할 제목). [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그 후, [ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks) 메서드를 호출하고, [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 업데이트된 PDF를 저장해야 합니다. 다음 코드 스니펫은 PDF 파일에서 기존 북마크를 수정하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-UpdateBookmark-UpdateBookmark.cs" >}}

## PDF 파일에서 모든 북마크 삭제

매개 변수를 사용하지 않고 [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) 메서드를 사용하여 PDF 파일에서 모든 북마크를 삭제할 수 있습니다. 먼저, [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그 후, [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) 메서드를 호출하고 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 업데이트된 PDF 파일을 저장해야 합니다. 다음 코드 스니펫은 PDF 파일에서 모든 북마크를 삭제하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-DeleteAllBookmarks-DeleteAllBookmarks.cs" >}}

## PDF 파일에서 특정 북마크 삭제

특정 북마크를 삭제하려면, 문자열(제목) 매개변수와 함께 [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) 메서드를 호출해야 합니다. The *title* here represents the bookmark to be deleted from the PDF. Create an object of [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) class and bind input PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method. After that, call [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) method and then save the updated PDF file using [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method. The following code snippet shows you how to delete a particular bookmark from a PDF file.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-DeleteABookmark-DeleteABookmark.cs" >}}

## PDF 문서 외관에서 북마크 가져오기

[PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 클래스는 기존 PDF 파일에서 북마크를 조작하는 기능을 제공합니다. 정보 책갈피에 관한 정보를 가져오거나 설정하는 다양한 속성을 제공합니다. 다음 코드 스니펫은 PDF 파일의 각 책갈피와 관련된 정보를 가져오는 방법을 보여줍니다.

## 기존 PDF 파일에서 책갈피 추출

[ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) 메소드는 PDF 파일에서 책갈피를 추출할 수 있도록 합니다. In order to extract the bookmarks, you need to create [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) object and bind the PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) method.

북마크를 추출하려면 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메소드를 사용하여 PDF 파일을 바인딩해야 합니다. 그 후, [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) 메서드를 호출해야 합니다. [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) 메서드는 [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks/methods/index) 객체를 반환합니다. 그런 다음 이러한 책갈피를 반복하여 개별 [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) 객체를 얻을 수 있습니다. 마지막으로 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다. 다음 코드 스니펫은 책갈피를 XML 파일로 내보내는 방법을 보여줍니다.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ExtractBookmarks-ExtractBookmarks.cs" >}}