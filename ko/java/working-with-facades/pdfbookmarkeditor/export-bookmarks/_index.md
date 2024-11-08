---
title: 기존 PDF 파일에서 XML로 북마크 내보내기 (facades)
type: docs
weight: 20
url: /ko/java/export-bookmark/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 PdfBookmarkEditor 클래스로 북마크를 내보내는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

{{% alert %}}

exportBookmarksToXml 메서드는 PDF 파일에서 XML 파일로 북마크를 내보낼 수 있게 합니다.

{{% /alert %}}

북마크를 내보내려면:

1. PdfBookmarkEditor 객체를 생성하고 bindPdf 메서드를 사용하여 PDF 파일을 바인딩합니다.
1. exportBookmarksToXml 메서드를 호출합니다.

다음 코드 스니펫은 북마크를 XML 파일로 내보내는 방법을 보여줍니다.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ExportBookmarksToXMLFromAnExistingPDFFile-ToExportBookmarks.java" >}}

From Aspose.PDF for Java 9.0.0, the PdfBookmarkEditor class implements the exportBookmarksToXML and importBookmarksWithXML methods with Stream arguments. As a result, extracted bookmarks can be saved to a stream object.

Aspose.PDF for Java 9.0.0부터 PdfBookmarkEditor 클래스는 Stream 인수를 사용하여 exportBookmarksToXML 및 importBookmarksWithXML 메서드를 구현합니다. 결과적으로 추출된 북마크는 스트림 객체에 저장될 수 있습니다.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ExportBookmarksToXMLFromAnExistingPDFFile-ExportBookmarksToXML.java" >}}