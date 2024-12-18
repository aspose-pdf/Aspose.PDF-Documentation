---
title: Javascript 작업 추가 PDF
type: docs
weight: 10
url: /ko/net/adding-javascript-actions/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 기존 PDF 파일에 Javascript 작업을 추가하는 방법을 설명합니다.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor) 클래스는 Aspose.Pdf.Facades 패키지 하에 있으며, PDF 파일에 Javascript 작업을 추가할 수 있는 유연성을 제공합니다. PDF 뷰어에서 메뉴 항목을 실행하는 일련의 작업과 연결된 링크를 만들 수 있습니다. 이 클래스는 문서 이벤트에 대한 추가 작업을 생성하는 기능도 제공합니다.

우선, [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)에 객체가 그려집니다. 우리의 예에서는 [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle)입니다. 문서에 액션 [createJavaScriptLink](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createjavascriptlink)를 사각형에 설정합니다. 그런 다음 문서를 저장할 수 있습니다.

```csharp
  public static void AddingJavascriptActions()
        {
            PdfContentEditor editor = new PdfContentEditor();
            editor.BindPdf(_dataDir + "sample.pdf");
            // 자바스크립트 링크 생성
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(50, 750, 50, 50);
            String code = "app.alert('Aspose에 오신 것을 환영합니다!');";
            editor.CreateJavaScriptLink(code, rect, 1, System.Drawing.Color.Green);
            // 출력 파일 저장
            editor.Save(_dataDir + "JavaScriptAdded_output.pdf");
        }
```