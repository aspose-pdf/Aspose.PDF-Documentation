---
title: 기존 PDF 파일에 주석 추가
type: docs
weight: 80
url: /net/adding-annotations-to-existing-pdf-file/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 기존 PDF 파일에 주석을 추가하는 방법을 설명합니다.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 기존 PDF 파일에 자유 텍스트 주석 추가 (facades)

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)는 기존 PDF 파일에 다양한 유형의 주석을 추가할 수 있게 합니다. 특정 주석을 추가하기 위해 각각의 메서드를 사용할 수 있습니다. 예를 들어, 다음 코드 스니펫에서는 [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) 메서드를 사용하여 [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) 유형의 주석을 추가했습니다.

어떠한 유형의 주석도 같은 방식으로 PDF 파일에 추가할 수 있습니다. 먼저, [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 유형의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 두 번째로, 주석의 영역을 지정하기 위해 Rectangle 객체를 생성해야 합니다.

그 후, [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) 메서드를 호출하여 [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) 주석을 추가할 수 있으며, [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 업데이트된 PDF 파일을 저장할 수 있습니다.

다음 코드 스니펫은 PDF 파일에 자유 텍스트 주석을 추가하는 방법을 보여줍니다.

```csharp
  public static void AddFreeTextAnnotation()
        {
            var document = new Document(_dataDir + "sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
            tfa.Visit(document.Pages[1]);

            var rect = new System.Drawing.Rectangle
            {
                X = (int)tfa.TextFragments[1].Rectangle.LLX,
                Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
                Height = 18,
                Width = 100
            };

            editor.CreateFreeText(rect, "Free Text Demo", 1); // 마지막 매개변수는 페이지 번호입니다
            editor.Save(_dataDir + "PdfContentEditorDemo_FreeTextAnnotation.pdf");
        }
```
## 기존 PDF 파일에 텍스트 주석 추가하기 (facades)

이 예제에서도 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 유형의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 두 번째로, 주석의 영역을 지정하기 위해 Rectangle 객체를 생성해야 합니다. 그 후, [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) 메서드를 호출하여 FreeText 주석을 추가하고, 주석의 제목과 주석이 위치한 페이지 번호를 생성할 수 있습니다.

```csharp
 public static void AddTextAnnotation()
        {
            var document = new Document(_dataDir + "sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
            tfa.Visit(document.Pages[1]);

            var rect = new System.Drawing.Rectangle
            {
                X = (int)tfa.TextFragments[1].Rectangle.LLX,
                Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
                Height = 18,
                Width = 100
            };

            editor.CreateText(rect, "Aspose User", "PDF is a better format for modern documents", false, "Key", 1);
            editor.Save(_dataDir + "PdfContentEditorDemo_TextAnnotation.pdf");
        }
```

## 기존 PDF 파일에 선 주석 추가 (facades)

우리는 또한 선의 시작과 끝 좌표, 페이지 번호, 주석 프레임의 두께, 스타일 및 색상, 선 대시 유형, 선의 시작 및 끝 유형을 지정합니다.

```csharp
  public static void AddLineAnnotation()
        {
            var document = new Document(_dataDir + "Appartments.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            // Create Line Annotation
            editor.CreateLine(
                new System.Drawing.Rectangle(550, 93, 562, 439),
                "Test",
                556, 99, 556, 443, 1, 2,
                System.Drawing.Color.Red,
                "dash",
                new int[] { 1, 0, 3 },
                new[] { "Open", "Open" });
            editor.Save(_dataDir + "PdfContentEditorDemo_LineAnnotation.pdf");
        }
```