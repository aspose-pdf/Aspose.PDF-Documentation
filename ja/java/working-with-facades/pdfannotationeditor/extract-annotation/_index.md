---
title: 注釈を抽出する (ファサード)
type: docs
weight: 30
url: /ja/java/extract-annotation/
description: このセクションでは、Aspose.PDF Facadesを使用してPDFファイルからXFDF形式に注釈を抽出する方法について説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[extractAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#extractAnnotations-int-int-int:A-0) メソッドは、PDFファイルから注釈を抽出することを可能にします。注釈を抽出するためには、[PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) オブジェクトを作成し、PDFファイルを [BindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Facade#bindPdf-com.aspose.pdf.IDocument-) メソッドを使用してバインドする必要があります。その後、PDFファイルから抽出したい注釈タイプの列挙を作成する必要があります。そして最後に、PdfAnnotationEditorオブジェクトのSaveメソッドを使用して更新されたPDFファイルを保存します。以下のコードスニペットは、PDFファイルから注釈を抽出する方法を示しています。

```java
  public static void ExtractAnnotation() {
        var document = new Document(_dataDir + "sample_cats_dogs.pdf");
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);

        // 注釈を抽出
        var annotationTypes = new int[] { AnnotationType.FreeText, AnnotationType.Text };
        var annotations = annotationEditor.extractAnnotations(1, 2, annotationTypes);
        for (var annotation : annotations) {
            System.out.println(annotation.getContents());
        }
```