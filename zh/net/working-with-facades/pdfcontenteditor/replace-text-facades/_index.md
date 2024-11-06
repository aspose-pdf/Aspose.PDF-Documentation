---
title: 替换文本 - Facades
type: docs
weight: 40
url: zh/net/replace-text-facades/
description: 本节解释如何使用PdfContentEditor类处理文本 - Facades。
lastmod: "2021-06-24"
draft: false
---

## 在现有PDF文件中替换文本

为了在现有PDF文件中替换文本，您需要创建一个[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)类的对象，并使用[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index)方法绑定输入的PDF文件。 之后，您需要调用[ReplaceText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replacetext/index)方法。您需要使用[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor)类的[Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save)方法保存更新后的PDF文件。以下代码片段向您展示了如何替换现有PDF文件中的文本。

```csharp
public static void ReplaceText01()
{
    PdfContentEditor editor = new PdfContentEditor();
    editor.BindPdf(_dataDir + "sample.pdf");
    editor.ReplaceText("Value", "Label");

    // save the output file
    editor.Save(_dataDir + "PdfContentEditorDemo01.pdf");
    }
```

查看原始文档中的显示情况：

![Replace Text](replace_text1.png)

并查看替换文本后的结果：

![Result of replacing Text](replace_text2.png)

在第二个示例中，您将看到除了替换文本之外，您还可以增加或减少字体大小：
```csharp
public static void ReplaceText02()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.BindPdf(_dataDir + "sample.pdf");
        editor.ReplaceText("Value", "Label", 12);

        // save the output file
        editor.Save(_dataDir + "PdfContentEditorDemo02.pdf");
    }
```

对于使用我们的文本处理的更多高级功能，我们将使用[TextState](https://reference.aspose.com/pdf/net/aspose.pdf.text/textstate)方法。通过这种方法，我们可以使文本变为粗体、斜体、着色等。

```csharp
    public static void ReplaceText03()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.BindPdf(_dataDir + "sample.pdf");
        TextState textState = new TextState
        {
            ForegroundColor = Color.Red,
            FontSize = 12,
        };
        editor.ReplaceText("Value", "Label", textState);

        // save the output file
        editor.Save(_dataDir + "PdfContentEditorDemo03.pdf");
    }
```

如果需要替换文档中所有指定的文本，请使用以下代码片段。 也就是说，文本的替换将发生在指定替换的文本出现的任何地方，并且它还将计算此类替换的次数。

```csharp
public static void ReplaceText04()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.BindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.ReplaceText("Value", "Label")) count++;

        Console.WriteLine($"{count} occurrences have been replaced.");

        // save the output file
        editor.Save(_dataDir + "PdfContentEditorDemo04.pdf");
    }
```

![替换所有文本](replace_text3.png)

以下代码片段展示了如何进行所有文本替换，但在文档的特定页面上。

```csharp
public static void ReplaceText05()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.BindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.ReplaceText("9999", 2, "ABCDE")) count++;
        Console.WriteLine($"{count} occurrences have been replaced.");

        // save the output file
        editor.Save(_dataDir + "PdfContentEditorDemo05.pdf");
    }
```
在下一个代码片段中，我们将展示如何用我们需要的字母替换给定的数字。

```csharp
   public static void ReplaceText06()
    {
        PdfContentEditor editor = new PdfContentEditor
        {
            ReplaceTextStrategy = new ReplaceTextStrategy
            {
                IsRegularExpressionUsed = true,
                ReplaceScope = ReplaceTextStrategy.Scope.ReplaceAll
            }
        };
        editor.BindPdf(_dataDir + "sample.pdf");
        editor.ReplaceText("\\d{4}", "ABCDE");
        // 保存输出文件
        editor.Save(_dataDir + "PdfContentEditorDemo06.pdf");
    }
```