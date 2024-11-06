---
title: 向现有PDF文件添加注释
type: docs
weight: 80
url: zh/net/adding-annotations-to-existing-pdf-file/
description: 本节解释如何使用Aspose.PDF Facades向现有PDF文件添加注释。
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 在现有PDF文件中添加自由文本注释（facades）

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 允许您在现有PDF文件中添加不同类型的注释。您可以使用相应的方法添加特定的注释。例如，在以下代码片段中，我们使用了 [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) 方法添加 [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) 类型的注释。

可以以相同的方式向PDF文件添加任何类型的注释。 首先，您需要创建一个类型为 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定输入的 PDF 文件。其次，您需要创建一个 Rectangle 对象来指定注释的区域。

之后，您可以调用 [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) 方法添加 [FreeText](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) 注释，然后使用 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存更新后的 PDF 文件。

以下代码片段向您展示了如何在 PDF 文件中添加自由文本注释。

```csharp
  public static void AddFreeTextAnnotation()
        {
            var document = new Document(_dataDir + "sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
            tfa.Visit(document.Pages[1]);

            var rect = new System.Drawing.Rectangle
            {
                X = (int)tfa.TextFragments[1].Rectangle.LLX,
                Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
                Height = 18,
                Width = 100
            };

            editor.CreateFreeText(rect, "Free Text Demo", 1); // last param is a page number
            editor.Save(_dataDir + "PdfContentEditorDemo_FreeTextAnnotation.pdf");
        }
```
## 在现有 PDF 文件中添加文本注释 (facades)

在这个例子中，您同样需要创建一个 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 类型的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定输入 PDF 文件。其次，您需要创建一个 Rectangle 对象来指定注释的区域。之后，您可以调用 [CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) 方法来添加自由文本注释，创建注释的标题以及注释所在的页码。

```csharp
 public static void AddTextAnnotation()
        {
            var document = new Document(_dataDir + "sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            TextFragmentAbsorber tfa = new TextFragmentAbsorber("PDF");
            tfa.Visit(document.Pages[1]);

            var rect = new System.Drawing.Rectangle
            {
                X = (int)tfa.TextFragments[1].Rectangle.LLX,
                Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
                Height = 18,
                Width = 100
            };

            editor.CreateText(rect, "Aspose User", "PDF is a better format for modern documents", false, "Key", 1);
            editor.Save(_dataDir + "PdfContentEditorDemo_TextAnnotation.pdf");
        }
```

## 在现有 PDF 文件中添加线注释（facades）

我们还指定了矩形、线的起始和结束坐标、页码、注释框的厚度、样式和颜色、线虚线类型、线的起始和结束类型。

```csharp
  public static void AddLineAnnotation()
        {
            var document = new Document(_dataDir + "Appartments.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);
            // 创建线注释
            editor.CreateLine(
                new System.Drawing.Rectangle(550, 93, 562, 439),
                "Test",
                556, 99, 556, 443, 1, 2,
                System.Drawing.Color.Red,
                "dash",
                new int[] { 1, 0, 3 },
                new[] { "Open", "Open" });
            editor.Save(_dataDir + "PdfContentEditorDemo_LineAnnotation.pdf");
        }
```