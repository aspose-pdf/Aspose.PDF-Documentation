---
title: Замена текста - Фасады
type: docs
weight: 40
url: /ru/net/replace-text-facades/
description: Этот раздел объясняет, как работать с текстом - фасадами, используя класс PdfContentEditor.
lastmod: "2021-06-24"
draft: false
---

## Замена текста в существующем PDF-файле

Для замены текста в существующем PDF-файле необходимо создать объект класса [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) и связать входной PDF-файл, используя метод [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). После этого необходимо вызвать метод [ReplaceText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replacetext/index). Вам нужно сохранить обновленный PDF файл, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) класса [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). Следующий фрагмент кода показывает, как заменить текст в существующем PDF файле.

```csharp
public static void ReplaceText01()
{
    PdfContentEditor editor = new PdfContentEditor();
    editor.BindPdf(_dataDir + "sample.pdf");
    editor.ReplaceText("Value", "Label");

    // сохранить выходной файл
    editor.Save(_dataDir + "PdfContentEditorDemo01.pdf");
    }
```

Посмотрите, как это выглядит в оригинальном документе:

![Заменить текст](replace_text1.png)

И проверьте результат после замены текста:

![Результат замены текста](replace_text2.png)

Во втором примере вы увидите, как, помимо замены текста, можно также увеличить или уменьшить размер шрифта:
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

Для более продвинутых возможностей работы с нашим текстом мы будем использовать метод [TextState](https://reference.aspose.com/pdf/net/aspose.pdf.text/textstate). С помощью этого метода мы можем сделать текст жирным, курсивным, цветным и так далее.

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

В случае, если вам нужно заменить весь указанный текст в документе, используйте следующий фрагмент кода. То есть, замена текста будет происходить везде, где будет встречаться указанный для замены текст, и также будет подсчитываться количество таких замен.

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

Следующий фрагмент кода показывает, как выполнять все замены текста, но на определенной странице вашего документа.

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
В следующем фрагменте кода мы покажем, как заменить, например, заданное число на нужные нам буквы.

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
        // сохранить выходной файл
        editor.Save(_dataDir + "PdfContentEditorDemo06.pdf");
    }
```