---
title: テキストを置換 - ファサード
type: docs
weight: 40
url: ja/net/replace-text-facades/
description: このセクションでは、PdfContentEditor クラスを使用してテキスト - ファサードを操作する方法を説明します。
lastmod: "2021-06-24"
draft: false
---

## 既存のPDFファイルでテキストを置換

既存のPDFファイルでテキストを置換するには、[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) クラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) メソッドを使用して入力PDFファイルをバインドする必要があります。 その後、[ReplaceText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replacetext/index) メソッドを呼び出す必要があります。[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) クラスの [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) メソッドを使用して、更新されたPDFファイルを保存する必要があります。以下のコードスニペットは、既存のPDFファイル内のテキストを置き換える方法を示しています。

```csharp
public static void ReplaceText01()
{
    PdfContentEditor editor = new PdfContentEditor();
    editor.BindPdf(_dataDir + "sample.pdf");
    editor.ReplaceText("Value", "Label");

    // 出力ファイルを保存
    editor.Save(_dataDir + "PdfContentEditorDemo01.pdf");
    }
```

元のドキュメントでの見え方を確認してください：

![Replace Text](replace_text1.png)

テキストを置き換えた後の結果を確認してください：

![Result of replacing Text](replace_text2.png)

2つ目の例では、テキストを置き換えるだけでなく、フォントサイズを増減させる方法も示します。
```csharp
public static void ReplaceText02()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.BindPdf(_dataDir + "sample.pdf");
        editor.ReplaceText("Value", "Label", 12);

        // 出力ファイルを保存する
        editor.Save(_dataDir + "PdfContentEditorDemo02.pdf");
    }
```

より高度なテキスト操作の可能性については、[TextState](https://reference.aspose.com/pdf/net/aspose.pdf.text/textstate) メソッドを使用します。このメソッドを使用すると、テキストを太字、斜体、カラーなどにすることができます。

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

        // 出力ファイルを保存する
        editor.Save(_dataDir + "PdfContentEditorDemo03.pdf");
    }
```

ドキュメント内のすべての指定されたテキストを置き換える必要がある場合は、次のコードスニペットを使用してください。 そのため、置換用に指定されたテキストが見つかるたびにテキストの置換が行われ、そのような置換の数もカウントされます。

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

次のコードスニペットは、ドキュメントの特定のページでテキストの置換を行う方法を示しています。

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
次のコードスニペットでは、例えば、指定された番号を必要な文字で置き換える方法を示します。

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
        // 出力ファイルを保存
        editor.Save(_dataDir + "PdfContentEditorDemo06.pdf");
    }
```