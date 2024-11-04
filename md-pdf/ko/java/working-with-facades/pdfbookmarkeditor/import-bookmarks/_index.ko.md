---
title: XML에서 기존 PDF 파일로 북마크 가져오기 (facades)
type: docs
weight: 30
url: /java/import-bookmark/
description: 이 섹션에서는 PdfBookmarEditor 클래스를 사용하여 Aspose.PDF Facades로 북마크를 가져오는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

importBookmarksWithXml 메서드는 XML 파일에서 PDF 파일로 북마크를 가져올 수 있게 해줍니다.

북마크를 가져오려면:

1. PdfBookmarkEditor 객체를 생성하고 bindPdf 메서드를 사용하여 PDF 파일을 바인딩합니다.
1. importBookmarksWithXml 메서드를 호출합니다.
1. save 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다.

다음 코드 스니펫은 XML 파일에서 북마크를 가져오는 방법을 보여줍니다.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ImportBookmarksFromXMLToAnExistingPDFFile-ToImportBookmarks.java" >}}

From Aspose.PDF for Java 9.0.0, the PdfBookmarkEditor class implements the exportBookmarksToXML and importBookmarksWithXML methods with Stream arguments. As a result, extracted bookmarks can be imported from a stream object.

Aspose.PDF for Java 9.0.0부터, PdfBookmarkEditor 클래스는 Stream 인수를 사용하여 exportBookmarksToXML 및 importBookmarksWithXML 메서드를 구현합니다. 결과적으로, 추출된 책갈피는 스트림 객체에서 가져올 수 있습니다.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-ImportBookmarksFromXMLToAnExistingPDFFile-ImportBookmarksWithXML.java" >}}