---
title: Replace Text - Facades
type: docs
weight: 40
url: /net/replace-text-facades/
description: This section explains how to work with Text - Facades using PdfContentEditor Class.
lastmod: "2021-06-24"
draft: false
---

## Replace Text in an Existing PDF File

In order to replace text in an existing PDF file, you need to create an object of [PdfContentEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class and bind an input PDF file using [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. After that, you need to call [ReplaceText](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replacetext/index) method. You need to save the updated PDF file using [Save](https://apireference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method of [PdfContentEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class. The following code snippet shows you how to replace text in an existing PDF file.

```csharp
public static void ReplaceText01()
{
    PdfContentEditor editor = new PdfContentEditor();
    ditor.BindPdf(_dataDir + "sample.pdf");
    editor.ReplaceText("Value", "Label");

    // save the output file
    editor.Save(_dataDir + "PdfContentEditorDemo01.pdf");
    }
```

Check how it's looks in the original document:

![Replace Text](replace_text1.png)

And check the result after replacing the text:

![Result of replacing Text](replace_text2.png)

In the second example, you will see how, in addition to replacing the text, you can also increase or decrease the font size:

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

For more advanced possibilities for working with our text, we will use the [TextState](https://apireference.aspose.com/pdf/net/aspose.pdf.text/textstate) method. With this method, we can make text bold, italic, colored, and so on.

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

In case you need to replace all the specified text in the document, use the following code snippet. That is, the replacement of the text will take place wherever the text specified for replacement will be encountered, and it will also count the number of such replacements.

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

![Replace all Text](replace_text3.png)

The following code snippet shows how to make all the text replacements but on a specific page of your document.

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

In the next code snippet, we will show how to replace, for example, a given number with the letters we need.

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
        // save the output file
        editor.Save(_dataDir + "PdfContentEditorDemo06.pdf");
    }
```
