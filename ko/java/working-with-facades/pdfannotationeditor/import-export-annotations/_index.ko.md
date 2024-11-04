---
title: com.aspose.pdf.facades를 사용하여 주석을 XFDF 형식으로 가져오기 및 내보내기
type: docs
weight: 20
url: /java/import-export-annotations/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 PDF 파일에서 XFDF로 주석을 내보내고 가져오는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

XFDF는 XML Forms Data Format의 약자입니다. 이것은 XML 기반 파일 형식입니다. 이 파일 형식은 PDF 폼에 포함된 폼 데이터나 주석을 나타내는 데 사용됩니다. XFDF는 여러 가지 목적으로 사용할 수 있지만, 우리의 경우에는 폼 데이터나 주석을 다른 컴퓨터나 서버 등으로 보내거나 받을 때 사용할 수 있으며, 폼 데이터나 주석을 보관하는 데 사용할 수 있습니다. 이 문서에서는 Aspose.Pdf.Facades가 이 개념을 어떻게 고려했는지, 주석 데이터를 XFDF 파일로 가져오고 내보내는 방법을 알아보겠습니다.

[PDFAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) 클래스에는 XFDF 파일로 주석을 가져오고 내보내는 작업을 수행하는 두 가지 메서드가 포함되어 있습니다.
 [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#exportAnnotationsToXfdf-java.io.OutputStream-) 메서드는 PDF 문서에서 XFDF 파일로 주석을 내보내는 기능을 제공하며, [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#importAnnotationFromXfdf-java.io.InputStream-) 메서드는 기존 XFDF 파일에서 주석을 가져올 수 있도록 합니다. 주석을 가져오거나 내보내기 위해서는 주석 유형을 지정해야 합니다. 이러한 유형을 열거형 형태로 지정한 다음, 이 열거형을 이러한 메서드의 인수로 전달할 수 있습니다.

다음 코드 스니펫은 XFDF 파일로 주석을 가져오는 방법을 보여줍니다:

```java
public static void ImportAnnotation() {
        String[] sources = new String[] { _dataDir + "sample_cats_dogs.pdf" };
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample.pdf");
        annotationEditor.importAnnotations(sources);
        annotationEditor.save(_dataDir + "sample_demo.pdf");
    }
```

다음 코드 스니펫은 XFDF 파일로 주석을 가져오고 내보내는 방법을 설명합니다:

```java
    public static void ImportExportXFDF01() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        OutputStream xmlOutputStream;
        try {
            xmlOutputStream = new FileOutputStream(_dataDir + "sample.xfdf");
            annotationEditor.exportAnnotationsToXfdf(xmlOutputStream);
            xmlOutputStream.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        Document document = new Document();
        document.getPages().add();
        annotationEditor.bindPdf(document);
        annotationEditor.importAnnotationsFromXfdf(_dataDir + "sample.xfdf");
        annotationEditor.save(_dataDir + "ImportedAnnotation.pdf");
    }
```

이 방법으로, 지정된 유형의 주석만 XFDF 파일로 가져오거나 내보낼 수 있습니다.

```java
    public static void ImportExportXFDF02() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        OutputStream xmlOutputStream;

        try {
            xmlOutputStream = new FileOutputStream(_dataDir + "sample.xfdf");
            int[] annotationTypes = new int[] { AnnotationType.FreeText, AnnotationType.Text };
            annotationEditor.exportAnnotationsXfdf(xmlOutputStream, 2, 2, annotationTypes);
            xmlOutputStream.close();
        } catch (IOException e) {            
            e.printStackTrace();
        }

        Document document = new Document(_dataDir + "sample.pdf");
        document.getPages().add();
        annotationEditor.bindPdf(document);
        annotationEditor.importAnnotationsFromXfdf(_dataDir + "sample.xfdf");
        annotationEditor.save(_dataDir + "ImportedAnnotation.pdf");
    }
```