---
title: PDF에서 주석 추출
type: docs
weight: 30
url: /ko/net/extract-annotation/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 PDF 파일에서 XFDF로 주석을 추출하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[ExtractAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) 메서드는 PDF 파일에서 주석을 추출할 수 있도록 해줍니다. 주석을 추출하려면 [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 PDF 파일을 바인딩해야 합니다. 그 후, PDF 파일에서 추출하고자 하는 주석 유형의 열거형을 만들어야 합니다.

그런 다음 [ExtractAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) 메서드를 사용하여 주석을 ArrayList로 추출할 수 있습니다. 그 후, 이 목록을 반복하여 개별 주석을 얻을 수 있습니다. 마지막으로, [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) 객체의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 업데이트된 PDF 파일을 저장하십시오. 다음 코드 스니펫은 PDF 파일에서 주석을 추출하는 방법을 보여줍니다.

```csharp
 public static void ExtractAnnotation()
        {
            var document = new Document(_dataDir + "sample_cats_dogs.pdf");
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(document);

            // 주석 추출
            var annotationTypes = new[] { AnnotationType.FreeText, AnnotationType.Text };
            var annotations = annotationEditor.ExtractAnnotations(1, 2, annotationTypes);
            foreach (var annotation in annotations)
            {
                Console.WriteLine(annotation.Contents);
            }
        }
```