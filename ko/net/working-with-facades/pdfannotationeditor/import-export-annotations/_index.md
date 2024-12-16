---
title: Import and Export Annotations to XFDF 
type: docs
weight: 20
url: /ko/net/import-export-annotations/
description: 이 섹션에서는 Aspose.PDF Facades를 사용하여 PDF 파일에서 XFDF로 주석을 가져오고 내보내는 방법을 설명합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

XFDF는 XML Forms Data Format의 약자입니다. 이것은 XML 기반 파일 형식입니다. 이 파일 형식은 PDF 양식에 포함된 양식 데이터 또는 주석을 나타내는 데 사용됩니다. XFDF는 다양한 목적으로 사용할 수 있지만, 우리 경우에는 양식 데이터 또는 주석을 다른 컴퓨터나 서버 등에 보내거나 받거나, 양식 데이터나 주석을 보관하는 데 사용할 수 있습니다. 이 기사에서는 Aspose.Pdf.Facades가 이 개념을 어떻게 고려했는지, 그리고 주석 데이터를 XFDF 파일로 가져오고 내보낼 수 있는 방법을 살펴보겠습니다.

## XFDF로 주석 가져오기 및 내보내기

[Aspose.PDF for .NET](/pdf/ko/net/)은 PDF 문서를 편집할 때 기능이 풍부한 구성 요소입니다. As we know XFDF is an important aspect of PDF forms manipulation, [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) in [Aspose.PDF for .NET](/pdf/ko/net/) has considered this very well, and have provided methods to import and export annotations data to XFDF files.

우리가 알다시피 XFDF는 PDF 양식 조작의 중요한 측면이며, [Aspose.PDF for .NET](/pdf/ko/net/)의 [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades)에서는 이를 잘 고려하여 주석 데이터를 XFDF 파일로 가져오고 내보내는 메서드를 제공했습니다.

[PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) class contains two methods to work with import and export of annotations to XFDF file.

[PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) 클래스는 XFDF 파일로 주석을 가져오고 내보내는 작업을 위한 두 가지 메서드를 포함하고 있습니다. [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/exportannotationsxfdf/index) 메서드는 PDF 문서에서 주석을 XFDF 파일로 내보내는 기능을 제공하며, [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/importannotationfromxfdf/index) 메서드는 기존 XFDF 파일에서 주석을 가져올 수 있게 해줍니다. 주석을 가져오거나 내보내기 위해서는 주석 유형을 지정해야 합니다. 우리는 이러한 유형들을 열거형 형태로 지정하고, 이 열거형을 이러한 메서드 중 하나에 인수로 전달할 수 있습니다. 이렇게 하면, 지정된 유형의 주석만 XFDF 파일로 가져오거나 내보내게 됩니다.

다음 코드 스니펫은 XFDF 파일로 주석을 가져오는 방법을 보여줍니다:

```csharp
public static void ImportAnnotation()
        {
            var sources = new string[] { _dataDir + "sample_cats_dogs.pdf" };
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample.pdf");
            annotationEditor.ImportAnnotations(sources);
            annotationEditor.Save(_dataDir + "sample_demo.pdf");
        }
```
다음 코드 스니펫은 XFDF 파일로 주석을 가져오고 내보내는 방법을 설명합니다:

```csharp
public static void ImportExportXFDF01()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            System.IO.FileStream xmlOutputStream = System.IO.File.OpenWrite(_dataDir + "sample.xfdf");
            annotationEditor.ExportAnnotationsToXfdf(xmlOutputStream);
            xmlOutputStream.Close();
            var document = new Document();
            document.Pages.Add();
            annotationEditor.BindPdf(document);
            annotationEditor.ImportAnnotationsFromXfdf(System.IO.File.OpenRead(_dataDir + "sample.xfdf"));
            annotationEditor.Save(_dataDir + "ImportedAnnotation.pdf");
        }
```

이 방법으로, 지정된 유형의 주석만 XFDF 파일로 가져오거나 내보낼 수 있습니다.

```csharp
   public static void ImportExportXFDF02()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            System.IO.FileStream xmlOutputStream = System.IO.File.OpenWrite(_dataDir + "sample.xfdf");
            var annotationTypes = new[] { AnnotationType.FreeText, AnnotationType.Text };
            annotationEditor.ExportAnnotationsXfdf(xmlOutputStream, 2, 2, annotationTypes);
            xmlOutputStream.Close();

            var document = new Document(_dataDir + "sample.pdf");
            document.Pages.Add();
            annotationEditor.BindPdf(document);
            annotationEditor.ImportAnnotationsFromXfdf(System.IO.File.OpenRead(_dataDir + "sample.xfdf"));
            annotationEditor.Save(_dataDir + "ImportedAnnotation.pdf");
        }
```