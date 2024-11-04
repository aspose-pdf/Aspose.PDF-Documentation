---
title: 모든 페이지의 북마크 만들기 (facades)
type: docs
weight: 10
url: /java/create-bookmark/
description: 이 섹션에서는 PdfBookmarEditor 클래스를 사용하여 Aspose.PDF Facades로 북마크를 만드는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 모든 페이지의 북마크 만들기 (facades)

모든 페이지의 북마크를 만들려면 매개변수 없이 createBookmarks 메서드를 사용해야 합니다. PdfBookmarEditor 클래스는 PDF 파일의 모든 페이지에 대한 북마크를 만들 수 있게 해줍니다. 먼저, PdfBookmarkEditor 클래스의 객체를 생성하고 bindPdf 메서드를 사용하여 입력 PDF를 바인딩해야 합니다. 그런 다음, createBookmarks 메서드를 호출하고 save 메서드를 사용하여 출력 PDF 파일을 저장해야 합니다.

다음 코드 스니펫을 참조하세요:

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-CreateBookmarksOfAllPages-.java" >}}

## 속성이 있는 모든 페이지의 북마크 만들기 (facades)

PdfBookmarEditor 클래스는 PDF 파일의 모든 페이지에 대한 북마크를 만들고 속성(색상, 굵게, 기울임꼴)을 지정할 수 있게 해줍니다.
 당신은 createBookmarks 메소드를 사용하여 이를 수행할 수 있습니다. 먼저, PdfBookmarkEditor 클래스의 객체를 생성하고 bindPdf 메소드를 사용하여 입력 PDF를 바인딩해야 합니다. 그런 다음, createBookmarks 메소드를 호출하고 save 메소드를 사용하여 출력 PDF 파일을 저장해야 합니다.

다음 코드 스니펫은 모든 페이지의 북마크를 속성과 함께 생성하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Bookmarks-CreateBookmarksOfAllPagesWithProperties-.java" >}}