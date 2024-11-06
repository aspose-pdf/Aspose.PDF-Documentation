---
title: 기존 PDF 파일의 뷰어 환경 설정 가져오기
type: docs
weight: 70
url: ko/net/get-viewer-preference-of-an-existing-pdf-file/
description: 이 섹션에서는 PdfContentEditor 클래스를 사용하여 기존 PDF 파일의 뷰어 환경 설정을 가져오는 방법을 보여줍니다.
lastmod: "2021-06-05"
draft: false
---

## 기존 PDF 파일의 뷰어 환경 설정 가져오기

[ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) 클래스는 PDF 파일의 디스플레이 모드를 나타냅니다. 예를 들어, 문서 창을 화면 중앙에 위치시키기, 뷰어 응용 프로그램의 메뉴 바 숨기기 등을 설정할 수 있습니다.

설정을 읽기 위해 [GetViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/getviewerpreference) 클래스를 사용합니다. 이 메서드는 모든 설정이 저장되는 변수를 반환합니다.

```csharp
      public static void GetViewerPreference()
        {
            var document = new Document(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Change Viewer Preferences
            var preferences = editor.GetViewerPreference();
            if ((preferences & ViewerPreference.CenterWindow) != 0)
                Console.WriteLine("CenterWindow");
            if ((preferences & ViewerPreference.HideMenubar) != 0)
                Console.WriteLine("Menu bar hided");
            if ((preferences & ViewerPreference.PageModeFullScreen) != 0)
                Console.WriteLine("Page Mode Full Screen");
        }
```