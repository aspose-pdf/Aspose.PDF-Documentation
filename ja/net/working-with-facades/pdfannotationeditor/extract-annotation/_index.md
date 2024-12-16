---
title: PDFから注釈を抽出する
type: docs
weight: 30
url: /ja/net/extract-annotation/
description: このセクションでは、Aspose.PDF Facadesを使用してPDFファイルからXFDFへの注釈の抽出方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[ExtractAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) メソッドを使用すると、PDFファイルから注釈を抽出できます。注釈を抽出するには、[PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) オブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) メソッドを使用してPDFファイルをバインドする必要があります。その後、PDFファイルから抽出したい注釈タイプの列挙を作成する必要があります。

その後、[ExtractAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) メソッドを使用して、注釈をArrayListに抽出できます。 その後、このリストをループして個々の注釈を取得できます。そして最後に、[PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor)オブジェクトの[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save)メソッドを使用して更新されたPDFファイルを保存します。次のコードスニペットは、PDFファイルから注釈を抽出する方法を示しています。

```csharp
 public static void ExtractAnnotation()
        {
            var document = new Document(_dataDir + "sample_cats_dogs.pdf");
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(document);

            // 注釈を抽出
            var annotationTypes = new[] { AnnotationType.FreeText, AnnotationType.Text };
            var annotations = annotationEditor.ExtractAnnotations(1, 2, annotationTypes);
            foreach (var annotation in annotations)
            {
                Console.WriteLine(annotation.Contents);
            }
        }
```