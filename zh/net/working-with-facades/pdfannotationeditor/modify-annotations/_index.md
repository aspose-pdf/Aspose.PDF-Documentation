---
title: 修改PDF中的注释
type: docs
weight: 50
url: zh/net/modify-annotations/
description: 本节解释如何使用Aspose.PDF Facades将PDF文件中的注释修改为XFDF。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[ModifyAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotations) 方法允许您更改注释的基本属性，即主题、修改日期、作者、注释颜色和打开标志。您还可以通过使用 ModifyAnnotations 方法直接设置作者。此类还提供了两个重载方法来删除注释。第一个方法称为 DeleteAnnotations，将删除PDF文件中的所有注释。

例如，在以下代码中，考虑使用 [ModifyAnnotationsAuthor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotationsauthor) 更改我们注释中的作者。

```csharp
   public static void ModifyAnnotationsAuthor()
        {
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(_dataDir + "sample_cats_dogs.pdf");
            annotationEditor.ModifyAnnotationsAuthor(1, 2, "Aspose User", "Aspose.PDF user");
            annotationEditor.Save(_dataDir + "ModifyAnnotationsAuthor.pdf");
        }
```

第二种方法允许您删除指定类型的所有注释。

```csharp
   public static void ModifyAnnotations()
        {
            var document = new Document(_dataDir + "sample_cats_dogs.pdf");
            PdfAnnotationEditor annotationEditor = new PdfAnnotationEditor();
            annotationEditor.BindPdf(document);

            // 创建一个新的注释对象以修改注释属性
            var defaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance();
            Aspose.Pdf.Annotations.FreeTextAnnotation annotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(
                document.Pages[1],
                new Aspose.Pdf.Rectangle(1, 1, 1, 1),
                defaultAppearance)
            {

                // 设置新的注释属性
                Title = "Aspose.PDF 演示用户",
                Subject = "技术文章"
            };
            // 修改 PDF 文件中的注释
            annotationEditor.ModifyAnnotations(1, 1, annotation);
            annotationEditor.Save(_dataDir + "ModifyAnnotations.pdf");
        }
```

## 另请参阅

尝试比较并找到适合您的注释工作方式。让我们学习 [PDF 注释](/pdf/net/annotations/) 部分。