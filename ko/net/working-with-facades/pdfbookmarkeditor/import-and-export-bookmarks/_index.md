---
title: 북마크 가져오기 및 내보내기
type: docs
weight: 20
url: ko/net/import-and-export-bookmarks/
description: 이 섹션에서는 Aspose.PDF Facades로 북마크를 가져오고 내보내는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---

## 기존 PDF 파일로부터 XML에서 북마크 가져오기

[ImportBookmarksWithXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1) 메서드는 XML 파일에서 북마크를 PDF 파일로 가져올 수 있게 해줍니다. 북마크를 가져오려면 [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) 메서드를 사용하여 PDF 파일을 바인딩해야 합니다. 그런 다음, [ImportBookmarksWithXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1) 메서드를 호출해야 합니다. 마지막으로, [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다. 다음 코드 스니펫은 XML 파일에서 북마크를 가져오는 방법을 보여줍니다.

## 기존 PDF 파일에서 XML로 북마크 내보내기

ExportBookmarksToXml 메서드를 사용하면 PDF 파일에서 XML 파일로 북마크를 내보낼 수 있습니다.

북마크를 내보내려면:

1. Create a PdfBookmarkEditor object and bind the PDF file using the BindPdf method.  
1. ExportBookmarksToXml 메서드를 호출합니다.  
2. Save 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다.  

다음 코드 스니펫은 북마크를 XML 파일로 내보내는 방법을 보여줍니다.  

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ExportToXML-ExportToXML.cs" >}}