---
title: 주석 삭제 (파사드)
type: docs
weight: 10
url: ko/java/delete-annotations/
description: 이 섹션은 PdfAnnotationEditor 클래스를 사용하여 Aspose.PDF 파사드로 주석을 삭제하는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) 클래스를 사용하여 기존 PDF 파일에서 지정된 주석 유형의 주석을 삭제할 수 있습니다.
 In order to do that you need to create a [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) object and bind input PDF file using bindPdf method. After that, call [deleteAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#deleteAnnotation-java.lang.String-) method, with the string parameter, to delete all the annotations from the file; the string parameter represents the annotation type to be deleted. Finally, use save method to save the updated PDF file.

The following code snippet shows you how to delete annotation by specified annotation type.

```java
public static void DeleteAnnotation() {
        // 문서 열기
        Scanner consoleScanner = new Scanner(System.in);
        Document document = new Document(_dataDir + "sample_cats_dogs.pdf");
        int index;
        for (index = 1; index <= document.getPages().get_Item(1).getAnnotations().size(); index++) {
            System.out.println(index + ". " + document.getPages().get_Item(1).getAnnotations().get_Item(index).getName()
                    + " " + document.getPages().get_Item(1).getAnnotations().get_Item(index).toString());
        }
        System.out.print("번호를 입력하세요:");
        index = consoleScanner.nextInt();

        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);
        annotationEditor.deleteAnnotation(document.getPages().get_Item(1).getAnnotations().get_Item(1).getName());

        // 업데이트된 PDF 저장
        annotationEditor.save(_dataDir + "DeleteAnnotation.pdf");
        consoleScanner.close();
    }
    ```
[PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor)를 사용하면 기존 PDF 파일에서 모든 주석을 삭제할 수 있습니다.

먼저, [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor)를 생성하고 BindPdf 메서드를 사용하여 입력 PDF 파일을 바인딩합니다.

그 후, [deleteAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#deleteAnnotation-java.lang.String-) 메서드를 호출하여 파일에서 모든 주석을 삭제한 다음, Save 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일에서 모든 주석을 삭제하는 방법을 보여줍니다.

```java
public static void DeleteAllAnnotations() {
    // 문서 열기
    PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
    annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
    // 모든 주석 삭제
    annotationEditor.deleteAnnotations();
    // 업데이트된 PDF 저장
    annotationEditor.save(_dataDir + "DeleteAllAnnotations_out.pdf");
}
```