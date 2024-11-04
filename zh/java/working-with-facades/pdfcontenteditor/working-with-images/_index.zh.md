---
title: 使用图像
type: docs
weight: 30
url: /java/working-with-image/
description: 本节介绍如何使用Aspose.PDF Facades替换图像 - 这是一个用于PDF常见操作的工具集。
lastmod: "2021-06-25"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 从PDF的特定页面删除图像（Facades）

[PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 类允许您替换现有PDF文件中的图像。
 [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) 方法帮助您实现这一目标。您需要创建一个 [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 类的对象，并使用 bindPdf 方法绑定输入的 PDF 文件。之后，您需要调用 [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) 方法，并提供三个参数：页码、要替换的图像索引以及要替换的图像路径。

以下代码片段展示了如何在现有 PDF 文件中替换图像。

```java
public class PdfContentEditorImages {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/facades/PdfContentEditor/";

    public static void DeleteImage()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.deleteImage(2, new int [] { 1,3 });
        editor.save(_dataDir + "PdfContentEditorDemo10.pdf");
    }
```

## 从 PDF 文件中删除所有图像 (Facades)

可以使用 [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 的 [deleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) 方法从 PDF 文件中删除所有图像。调用 [deleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) 方法（不带任何参数的重载）删除所有图像，然后使用 Save 方法保存更新的 PDF 文件。

```java
   public static void DeleteImages()
    {
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
        editor.deleteImage();
        editor.save(_dataDir + "PdfContentEditorDemo11.pdf");
    }
```

## 替换 PDF 文件中的图像 (Facades)

您可以使用 [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 的 [replaceImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceImage-int-int-java.lang.String-) 方法替换 PDF 文件中的图像。

```java
   public static void ReplaceImage()
    {
        // 创建一个PdfContentEditor对象，并加载PDF文档
        PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample_cats_dogs.pdf"));
        // 替换页面上的图像
        editor.replaceImage(2, 4, _dataDir+"cat04.jpg");
        // 保存修改后的PDF文档
        editor.save(_dataDir + "PdfContentEditorDemo12.pdf");
    }
```