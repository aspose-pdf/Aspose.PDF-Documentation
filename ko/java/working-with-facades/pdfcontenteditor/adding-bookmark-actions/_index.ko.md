---
title: 기존 PDF 파일에 북마크 작업 추가
type: docs
weight: 20
url: /java/adding-bookmark-actions/
description: 이 섹션은 Aspose.PDF Facades로 기존 PDF 파일에 북마크 작업을 추가하는 방법을 설명합니다.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 클래스는 com.aspose.pdf.facades 패키지에 있으며 PDF 파일에 북마크 작업을 추가할 수 있는 유연성을 제공합니다. PDF 뷰어에서 메뉴 항목을 실행하는 일련의 작업과 연결된 링크를 만들 수 있습니다. 이 클래스는 문서 이벤트에 대한 추가 작업을 생성하는 기능도 제공합니다.

다음 코드 예제는 PDF 문서에 북마크 작업을 추가하는 방법을 보여줍니다.
 탭을 클릭하면 원하는 동작이 수행됩니다. 북마크를 사용하여 클릭하면 원하는 동작을 수행합니다. 그런 다음 [CreateBookmarkAction](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createBookmarksAction-java.lang.String-java.awt.Color-boolean-boolean-java.lang.String-java.lang.String-java.lang.String-)을 생성하고, 텍스트의 매개변수, 색상, 북마크 이름을 설정하고 페이지 번호를 지정합니다. 마지막 동작은 "GoTo"로 수행되며, 이를 통해 어디서든 필요한 페이지로 이동할 수 있습니다.

```java
public static void AddBookmarksAction()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            editor.createBookmarksAction("Bookmark 1", java.awt.Color.GREEN, true, false, "", "GoTo", "2");

            // 결과 PDF를 파일에 저장합니다
            editor.save(_dataDir + "PdfContentEditorDemo_Bookmark.pdf");
        }
```