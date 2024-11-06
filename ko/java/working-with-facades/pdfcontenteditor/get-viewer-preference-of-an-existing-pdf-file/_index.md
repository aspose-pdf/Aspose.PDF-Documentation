---
title: 기존 PDF 파일의 뷰어 환경 설정 가져오기
type: docs
weight: 70
url: ko/java/get-viewer-preference-of-an-existing-pdf-file/
description: 이 섹션에서는 PdfContentEditor 클래스를 사용하여 Aspose.PDF Facades와 작업하는 방법을 보여줍니다.
lastmod: "2021-06-05"
draft: false
---

## 기존 PDF 파일의 뷰어 환경 설정 가져오기

[ViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/viewerpreference) 클래스는 PDF 파일의 표시 모드를 나타냅니다. 예를 들어, 문서 창을 화면 중앙에 배치하거나 뷰어 애플리케이션의 메뉴 바를 숨기는 등의 기능이 있습니다.

설정을 읽기 위해 'getViewerPreference'를 사용합니다. 이 메서드는 모든 설정이 저장된 변수를 반환합니다.

```java
 public static void GetViewerPreference()
        {
            var document = new Document(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // 뷰어 환경 설정 변경
            var preferences = editor.getViewerPreference();
            if ((preferences & ViewerPreference.CENTER_WINDOW) != 0)
                System.out.println("CenterWindow");
            if ((preferences & ViewerPreference.HIDE_MENUBAR) != 0)
                System.out.println("메뉴 바 숨김");
        }
```