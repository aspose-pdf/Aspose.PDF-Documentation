---
title: 删除注释（facades）
type: docs
weight: 10
url: zh/java/delete-annotations/
description: 本节介绍如何使用 Aspose.PDF Facades 和 PdfAnnotationEditor 类删除注释。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

您可以使用 [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) 类，从现有的 PDF 文件中按指定的注释类型删除注释。
 为了做到这一点，您需要创建一个[PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor)对象，并使用bindPdf方法绑定输入PDF文件。之后，调用[deleteAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#deleteAnnotation-java.lang.String-)方法，使用字符串参数，从文件中删除所有的注释；字符串参数表示要删除的注释类型。最后，使用save方法保存更新后的PDF文件。

以下代码片段向您展示了如何按指定注释类型删除注释。

```java
public static void DeleteAnnotation() {
        // 打开文档
        Scanner consoleScanner = new Scanner(System.in);
        Document document = new Document(_dataDir + "sample_cats_dogs.pdf");
        int index;
        for (index = 1; index <= document.getPages().get_Item(1).getAnnotations().size(); index++) {
            System.out.println(index + ". " + document.getPages().get_Item(1).getAnnotations().get_Item(index).getName()
                    + " " + document.getPages().get_Item(1).getAnnotations().get_Item(index).toString());
        }
        System.out.print("请输入编号:");
        index = consoleScanner.nextInt();

        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);
        annotationEditor.deleteAnnotation(document.getPages().get_Item(1).getAnnotations().get_Item(1).getName());

        // 保存更新后的PDF
        annotationEditor.save(_dataDir + "DeleteAnnotation.pdf");
        consoleScanner.close();
    }
```
[PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) 允许您删除现有 PDF 文件中的所有注释。

首先，创建一个 [PdfAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) 并使用 BindPdf 方法绑定输入的 PDF 文件。

之后，调用 [deleteAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#deleteAnnotation-java.lang.String-) 方法删除文件中的所有注释，然后使用 Save 方法保存更新后的 PDF 文件。以下代码片段展示了如何从 PDF 文件中删除所有注释。

```java
public static void DeleteAllAnnotations() {
    // 打开文档
    PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
    annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
    // 删除所有注释
    annotationEditor.deleteAnnotations();
    // 保存更新后的 PDF
    annotationEditor.save(_dataDir + "DeleteAllAnnotations_out.pdf");
}
```