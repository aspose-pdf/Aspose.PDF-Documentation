---
title: PDF에서 주석 수정하기
type: docs
weight: 50
url: ko/net/modify-annotations/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 PDF 파일에서 XFDF로 주석을 수정하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[ModifyAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotations) 메서드를 사용하면 주석의 기본 속성, 즉 주제, 수정 날짜, 작성자, 주석 색상 및 열린 플래그를 변경할 수 있습니다. ModifyAnnotations 메서드를 사용하여 작성자를 직접 설정할 수도 있습니다. 이 클래스는 주석을 삭제하는 두 가지 오버로드된 메서드도 제공합니다. DeleteAnnotations라는 첫 번째 메서드는 PDF 파일에서 모든 주석을 삭제합니다.

예를 들어, 다음 코드에서는 [ModifyAnnotationsAuthor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotationsauthor)를 사용하여 주석의 작성자를 변경하는 것을 고려합니다.

```csharp
   public static void ModifyAnnotationsAuthor()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            annotationEditor.ModifyAnnotationsAuthor(1, 2, "Aspose User", "Aspose.PDF user");
            annotationEditor.Save(_dataDir + "ModifyAnnotationsAuthor.pdf");
        }
```

두 번째 방법은 지정된 유형의 모든 주석을 삭제할 수 있습니다.

```csharp
   public static void ModifyAnnotations()
        {
            var document = new Document(_dataDir + "sample_cats_dogs.pdf");
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(document);

            // 주석 속성을 수정하기 위해 주석 유형의 새 객체 생성
            var defaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance();
            Aspose.Pdf.Annotations.FreeTextAnnotation annotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(
                document.Pages[1],
                new Aspose.Pdf.Rectangle(1, 1, 1, 1),
                defaultAppearance)
            {

                // 새 주석 속성 설정
                Title = "Aspose.PDF 데모 사용자",
                Subject = "기술 기사"
            };
            // PDF 파일의 주석 수정
            annotationEditor.ModifyAnnotations(1, 1, annotation);
            annotationEditor.Save(_dataDir + "ModifyAnnotations.pdf");
        }
```

## See also

자신에게 맞는 주석 작업 방식을 비교하고 찾아보세요. [PDF 주석](/pdf/net/annotations/) 섹션을 배워봅시다.