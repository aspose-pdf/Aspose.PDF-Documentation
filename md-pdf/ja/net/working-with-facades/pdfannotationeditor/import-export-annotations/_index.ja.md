---
title: インポートとエクスポートの注釈をXFDFに
type: docs
weight: 20
url: /net/import-export-annotations/
description: このセクションでは、Aspose.PDF Facadesを使用してPDFファイルからXFDFへの注釈のインポートとエクスポート方法について説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

XFDFはXML Forms Data Formatの略です。これはXMLベースのファイル形式です。このファイル形式は、PDFフォームに含まれるフォームデータや注釈を表すために使用されます。XFDFは多くの異なる目的で使用できますが、私たちの場合、フォームデータや注釈を他のコンピュータやサーバーなどに送信または受信するために使用することができます。また、フォームデータや注釈をアーカイブするために使用することもできます。この記事では、Aspose.Pdf.Facadesがこの概念をどのように考慮しているか、そしてどのようにして注釈データをXFDFファイルにインポートおよびエクスポートできるかを見ていきます。

## XFDFへの注釈のインポートとエクスポート

[Aspose.PDF for .NET](/pdf/net/)は、PDFドキュメントを編集する際に豊富な機能を備えたコンポーネントです。 ```
As we know XFDF is an important aspect of PDF forms manipulation, [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) in [Aspose.PDF for .NET](/pdf/net/) has considered this very well, and have provided methods to import and export annotations data to XFDF files.

[PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) class contains two methods to work with import and export of annotations to XFDF file.
```

```
XFDFはPDFフォーム操作の重要な側面であることは周知の通りです。[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) は [Aspose.PDF for .NET](/pdf/net/) でこれを非常によく考慮しており、注釈データをXFDFファイルにインポートおよびエクスポートするためのメソッドを提供しています。

[PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) クラスには、XFDFファイルへの注釈のインポートとエクスポートを処理するための2つのメソッドが含まれています。
``` [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/exportannotationsxfdf/index) メソッドは、PDF ドキュメントから XFDF ファイルに注釈をエクスポートする機能を提供します。一方、[ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/importannotationfromxfdf/index) メソッドは、既存の XFDF ファイルから注釈をインポートすることを可能にします。注釈をインポートまたはエクスポートするためには、注釈の種類を指定する必要があります。これらの種類を列挙型の形で指定し、これらのメソッドのいずれかに引数として渡すことができます。この方法で、指定された種類の注釈のみが XFDF ファイルにインポートまたはエクスポートされます。

次のコードスニペットは、XFDF ファイルに注釈をインポートする方法を示しています:

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
次のコードスニペットは、XFDFファイルへの注釈のインポート/エクスポート方法を示しています:

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

このようにして、指定されたタイプの注釈のみがXFDFファイルにインポートまたはエクスポートされます。

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