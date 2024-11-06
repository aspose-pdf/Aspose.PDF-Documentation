---
title: 提取注释（facades）
type: docs
weight: 30
url: zh/java/extract-annotation/
description: 本节解释如何使用 Aspose.PDF Facades 从 PDF 文件中提取注释到 XFDF。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[extractAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#extractAnnotations-int-int-int:A-0) 方法允许您从 PDF 文件中提取注释。为了提取注释，您需要创建 [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) 对象，并使用 [BindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Facade#bindPdf-com.aspose.pdf.IDocument-) 方法绑定 PDF 文件。之后，您需要创建一个枚举以指定您想从 PDF 文件中提取的注释类型。最后，使用 PdfAnnotationEditor 对象的 Save 方法保存更新后的 PDF 文件。以下代码片段展示了如何从 PDF 文件中提取注释。

```java
  public static void ExtractAnnotation() {
        var document = new Document(_dataDir + "sample_cats_dogs.pdf");
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);

        // 提取注释
        var annotationTypes = new int[] { AnnotationType.FreeText, AnnotationType.Text };
        var annotations = annotationEditor.extractAnnotations(1, 2, annotationTypes);
        for (var annotation : annotations) {
            System.out.println(annotation.getContents());
        }
```