---
title: 修改PDF文件中的注释（facades）
type: docs
weight: 50
url: /zh/java/modify-annotations/
description: 本节说明如何使用Aspose.PDF Facades将PDF文件中的注释修改为XFDF。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[modifyAnnotations](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#modifyAnnotations-int-int-com.aspose.pdf.Annotation-) 方法允许您更改注释的基本属性，例如主题、修改日期、作者、注释颜色和打开标志。您还可以通过使用 ModifyAnnotations 方法直接设置作者。此类还提供两个重载方法来删除注释。第一个方法称为 DeleteAnnotations，该方法删除PDF文件中的所有注释。

例如，在以下代码中，考虑使用 [modifyAnnotationsAuthor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor#modifyAnnotationsAuthor-int-int-java.lang.String-java.lang.String-) 更改我们注释中的作者。

```java
 public static void ModifyAnnotationsAuthor() {
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(_dataDir + "sample_cats_dogs.pdf");
        annotationEditor.modifyAnnotationsAuthor(1, 2, "Aspose User", "Aspose.PDF user");
        annotationEditor.save(_dataDir + "ModifyAnnotationsAuthor.pdf");
    }
```

第二种方法允许您删除指定类型的所有注释。

```java
    public static void ModifyAnnotations() {
        Document document = new Document(_dataDir + "sample_cats_dogs.pdf");
        PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
        annotationEditor.bindPdf(document);

        // 创建一个新的注释对象以修改注释属性
        DefaultAppearance defaultAppearance = new DefaultAppearance();
        FreeTextAnnotation annotation = new FreeTextAnnotation(document.getPages().get_Item(1),
                new Rectangle(1, 1, 1, 1), defaultAppearance);

        annotation.setTitle("Aspose.PDF 演示用户");
        annotation.setSubject("技术文章");

        // 修改PDF文件中的注释
        annotationEditor.modifyAnnotations(1, 1, annotation);
        annotationEditor.save(_dataDir + "ModifyAnnotations.pdf");
    }
```


## 另请参阅

尝试比较并找到适合您的注释工作方式。让我们学习 [PDF 注释](/pdf/zh/java/annotations/) 部分。