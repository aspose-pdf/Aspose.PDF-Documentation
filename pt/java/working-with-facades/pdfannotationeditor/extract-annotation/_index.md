---
title: Extrair Anotação (fachadas)
type: docs
weight: 30
url: pt/java/extract-annotation/
description: Esta seção explica como extrair anotações de um arquivo PDF para XFDF com Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[extractAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#extractAnnotations-int-int-int:A-0) método permite que você extraia anotações de um arquivo PDF. Para extrair anotações, você precisa criar um objeto [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) e vincular o arquivo PDF usando o método [BindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Facade#bindPdf-com.aspose.pdf.IDocument-). Depois disso, você precisa criar uma enumeração dos tipos de anotação que deseja extrair do arquivo PDF. E, finalmente, salve o arquivo PDF atualizado usando o método Save do objeto PdfAnnotationEditor. O seguinte trecho de código mostra como extrair anotações de um arquivo PDF.

```java
  public static void ExtractAnnotation() {
        var document = new Document(_dataDir + "sample_cats_dogs.pdf");
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);

        // Extrair anotações
        var annotationTypes = new int[] { AnnotationType.FreeText, AnnotationType.Text };
        var annotations = annotationEditor.extractAnnotations(1, 2, annotationTypes);
        for (var annotation : annotations) {
            System.out.println(annotation.getContents());
        }
```