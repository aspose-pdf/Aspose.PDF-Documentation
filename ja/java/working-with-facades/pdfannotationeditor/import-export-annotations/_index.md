---
title: com.aspose.pdf.facadesを使用してXFDF形式に注釈をインポートおよびエクスポートする
type: docs
weight: 20
url: ja/java/import-export-annotations/
description: このセクションでは、Aspose.PDF Facadesを使用してPDFファイルからXFDFに注釈をエクスポートおよびインポートする方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

XFDFはXML Forms Data Formatの略です。これはXMLベースのファイル形式です。このファイル形式は、PDFフォームに含まれるフォームデータや注釈を表現するために使用されます。XFDFは多くの異なる目的で使用できますが、私たちのケースでは、フォームデータや注釈を他のコンピュータやサーバーに送信または受信するために使用できます。また、フォームデータや注釈をアーカイブするためにも使用できます。この記事では、Aspose.Pdf.Facadesがこのコンセプトをどのように考慮しているか、そしてどのようにして注釈データをXFDFファイルにインポートおよびエクスポートできるかを見ていきます。

[PDFAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) クラスには、XFDFファイルへの注釈のインポートおよびエクスポートを操作するための2つのメソッドが含まれています。
 [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#exportAnnotationsToXfdf-java.io.OutputStream-) メソッドは、PDF ドキュメントから XFDF ファイルに注釈をエクスポートする機能を提供します。一方、[ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#importAnnotationFromXfdf-java.io.InputStream-) メソッドは、既存の XFDF ファイルから注釈をインポートすることを可能にします。注釈をインポートまたはエクスポートするには、注釈の種類を指定する必要があります。これらの種類を列挙型の形式で指定し、この列挙型をこれらのメソッドの引数として渡すことができます。

次のコードスニペットは、注釈を XFDF ファイルにインポートする方法を示しています:

```java
public static void ImportAnnotation() {
        String[] sources = new String[] { _dataDir + "sample_cats_dogs.pdf" };
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample.pdf");
        annotationEditor.importAnnotations(sources);
        annotationEditor.save(_dataDir + "sample_demo.pdf");
    }
```

次のコードスニペットは、注釈をXFDFファイルにインポート/エクスポートする方法を示しています:

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

この方法では、指定されたタイプの注釈のみがXFDFファイルにインポートまたはエクスポートされます。

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