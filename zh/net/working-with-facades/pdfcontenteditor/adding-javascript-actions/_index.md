---
title: 添加 Javascript 动作 PDF 
type: docs
weight: 10
url: zh/net/adding-javascript-actions/
description: 本节解释了如何使用 Aspose.PDF Facades 向现有 PDF 文件添加 Javascript 动作。
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor) 类位于 Aspose.Pdf.Facades 包中，提供了向 PDF 文件添加 Javascript 动作的灵活性。您可以创建一个链接，具有执行 PDF 查看器中菜单项的串行动作。此类还提供为文档事件创建附加动作的功能。

首先，在 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 中绘制一个对象，在我们的示例中是一个 [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle)。 将操作[createJavaScriptLink](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createjavascriptlink)设置为Rectangle。之后，您可以保存您的文档。

```csharp
  public static void AddingJavascriptActions()
        {
            PdfContentEditor editor = new PdfContentEditor();
            editor.BindPdf(_dataDir + "sample.pdf");
            // 创建Javascript链接
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(50, 750, 50, 50);
            String code = "app.alert('Welcome to Aspose!');";
            editor.CreateJavaScriptLink(code, rect, 1, System.Drawing.Color.Green);
            // 保存输出文件
            editor.Save(_dataDir + "JavaScriptAdded_output.pdf");
        }
```