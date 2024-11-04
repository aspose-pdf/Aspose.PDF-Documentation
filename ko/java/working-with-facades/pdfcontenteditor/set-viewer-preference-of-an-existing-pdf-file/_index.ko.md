---
title: 기존 PDF 파일의 뷰어 환경 설정 설정
type: docs
weight: 60
url: /java/set-viewer-preference-of-an-existing-pdf-file/
description: 이 섹션에서는 PdfContentEditor 클래스를 사용하여 Aspose.PDF Facades를 다루는 방법을 보여줍니다.
lastmod: "2021-06-05"
draft: false
---

## 기존 PDF 파일의 뷰어 환경 설정 설정

[ViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/viewerpreference) 클래스는 PDF 파일의 디스플레이 모드를 나타냅니다; 예를 들어, 문서 창을 화면 중앙에 위치시키거나 뷰어 응용 프로그램의 메뉴 바를 숨기는 등의 기능입니다. 

[ChangeViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#changeViewerPreference-int-) 메서드는 [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 클래스에서 뷰어 환경 설정을 변경할 수 있도록 합니다.
 그렇게 하려면 [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 클래스의 객체를 생성하고 [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#bindPdf-java.lang.String-) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다.

그 후, [ChangeViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#changeViewerPreference-int-) 메서드를 호출하여 원하는 환경 설정을 설정할 수 있습니다. 마지막으로, 업데이트된 PDF 파일을 Save 메서드를 사용하여 저장해야 합니다. 다음 코드 스니펫은 기존 PDF 파일에서 뷰어 환경 설정을 변경하는 방법을 보여줍니다.

예를 들어, 파라미터 [CENTER WINDOW](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#CENTER_WINDOW)를 지정하여 창을 중앙에 배치하고, [HIDE MENUBAR](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#HIDE_MENUBAR)로 상단 툴바를 제거한 후 [PAGE MODE USE NONE](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#PAGE_MODE_USE_NONE)로 전체 화면 모드를 엽니다.
```java
public static void SetViewerPreference()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // 뷰어 기본 설정 변경
            editor.changeViewerPreference(ViewerPreference.CENTER_WINDOW);
            editor.changeViewerPreference(ViewerPreference.HIDE_MENUBAR);
            editor.changeViewerPreference(ViewerPreference.PAGE_MODE_USE_NONE);
            
            editor.save(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            GetViewerPreference();
        }
```