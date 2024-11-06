---
title: PDF의 보기 환경 설정 설정하기
type: docs
weight: 60
url: ko/net/set-viewer-preference-of-an-existing-pdf-file/
description: 이 섹션에서는 PdfContentEditor 클래스를 사용하여 기존 PDF 파일의 보기 환경 설정을 설정하는 방법을 보여줍니다.
lastmod: "2021-06-05"
draft: false
---

## 기존 PDF 파일의 보기 환경 설정 설정하기

[ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) 클래스는 PDF 파일의 표시 모드를 나타냅니다. 예를 들어, 문서 창을 화면 중앙에 배치하거나 뷰어 애플리케이션의 메뉴 바를 숨기는 등의 기능이 있습니다.

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 클래스의 [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) 메서드를 사용하면 보기 환경 설정을 변경할 수 있습니다. 문서를 번역하려면 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/bindpdf/index) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다.

그 후, [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) 메서드를 호출하여 환경 설정을 설정할 수 있습니다. 마지막으로, [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) 메서드를 사용하여 업데이트된 PDF 파일을 저장해야 합니다. 다음 코드 스니펫은 기존 PDF 파일에서 뷰어 환경 설정을 변경하는 방법을 보여줍니다.

예를 들어, 우리는 [CenterWindow](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/centerwindow) 매개변수를 지정하여 창을 가운데에 배치하고, [HideMenubar](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/hidemenubar)로 상단 도구 모음을 제거하며, [PageModeUseNone](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/pagemodeusenone)으로 전체 화면 모드를 엽니다.
```csharp
 public static void SetViewerPreference()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // 뷰어 기본 설정 변경
            editor.ChangeViewerPreference(ViewerPreference.CenterWindow);
            editor.ChangeViewerPreference(ViewerPreference.HideMenubar);
            editor.ChangeViewerPreference(ViewerPreference.PageModeFullScreen);
            // 결과 PDF 파일로 저장
            editor.Save(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            GetViewerPreference();
        }
```