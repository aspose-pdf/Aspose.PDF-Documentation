---
title: 주석 삭제 (파사드)
type: docs
weight: 10
url: ko/net/delete-annotations/
description: 이 섹션은 PdfAnnotationEditor 클래스를 사용하여 Aspose.PDF Facades로 주석을 삭제하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 기존 PDF 파일에서 모든 주석 삭제

[PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor)를 사용하면 기존 PDF 파일에서 모든 주석을 삭제할 수 있습니다. 첫째, [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 입력 PDF 파일을 바인딩합니다. 그런 다음, [DeleteAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations) 메서드를 호출하여 파일에서 모든 주석을 삭제하고, [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일에서 모든 주석을 삭제하는 방법을 보여줍니다.

```csharp
   public static void DeleteAllAnnotations()
        {
            // 문서 열기
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            // 모든 주석 삭제
            annotationEditor.DeleteAnnotations();
            // 업데이트된 PDF 저장
        }   
    
```
## Delete All Annotations by Specified Type

지정된 주석 유형으로 모든 주석 삭제

[PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) 클래스를 사용하여 기존 PDF 파일에서 지정된 주석 유형에 따라 모든 주석을 삭제할 수 있습니다. 이를 수행하려면 [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 메서드를 사용하여 입력 PDF 파일을 바인딩해야 합니다. 그런 다음 문자열 매개변수를 사용하여 [DeleteAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations) 메서드를 호출하여 파일의 모든 주석을 삭제합니다. 문자열 매개변수는 삭제할 주석 유형을 나타냅니다. 마지막으로 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다. 다음 코드 조각은 지정된 주석 유형에 따라 모든 주석을 삭제하는 방법을 보여줍니다.

```csharp
    public static void DeleteAnnotation()
        {
            // 문서 열기
            var document = new Document(_dataDir + "sample_cats_dogs.pdf");
            int index;
            for (index = 1; index <= document.Pages[1].Annotations.Count; index++)
            {
                System.Console.WriteLine($"{index}. {document.Pages[1].Annotations[index].Name} {document.Pages[1].Annotations[index].AnnotationType}");
            }
            System.Console.Write("숫자를 입력하세요:");
            index = int.Parse(System.Console.ReadLine());

            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(document);
            annotationEditor.DeleteAnnotation(document.Pages[1].Annotations[index].Name);

            // 업데이트된 PDF 저장
            annotationEditor.Save(_dataDir + "DeleteAnnotation.pdf");
        }
```