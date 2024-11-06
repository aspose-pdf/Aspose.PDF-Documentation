---
title: 将Javascript操作添加到现有PDF文件
type: docs
weight: 10
url: zh/java/adding-javascript-actions/
description: 本节介绍如何使用Aspose.PDF Facades将Javascript操作添加到现有PDF文件。
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) 类位于 com.aspose.pdf.facades 包下，提供了向PDF文件添加Javascript操作的灵活性。您可以创建一个链接，其中包含在PDF查看器中执行菜单项的串行操作。该类还提供了为文档事件创建附加操作的功能。

首先，在[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)中绘制一个对象，在我们的示例中是一个[Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle)。
 将动作[createJavaScriptLink](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createJavaScriptLink-java.lang.String-java.awt.Rectangle-int-java.awt.Color-)设置为Rectangle。之后，您可以保存文档。

```java
 public static void AddingJavascriptActions() {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");
        // 创建Javascript链接
        java.awt.Rectangle rect = new java.awt.Rectangle(50, 750, 50, 50);
        String code = "app.alert('欢迎使用Aspose!');";
        editor.createJavaScriptLink(code, rect, 1, java.awt.Color.GREEN);
        // 保存输出文件
        editor.save(_dataDir+"JavaScriptAdded_output.pdf");
    }
```