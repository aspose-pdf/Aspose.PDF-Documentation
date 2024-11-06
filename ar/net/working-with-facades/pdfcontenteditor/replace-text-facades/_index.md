---
title: استبدال النص - الواجهات
type: docs
weight: 40
url: ar/net/replace-text-facades/
description: يشرح هذا القسم كيفية العمل مع النص - الواجهات باستخدام فئة PdfContentEditor.
lastmod: "2021-06-24"
draft: false
---

## استبدال النص في ملف PDF موجود

من أجل استبدال النص في ملف PDF موجود، تحتاج إلى إنشاء كائن من فئة [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) وربط ملف PDF المدخل باستخدام طريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). بعد ذلك، تحتاج إلى استدعاء [ReplaceText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replacetext/index) الطريقة. تحتاج إلى حفظ ملف PDF المحدث باستخدام [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) الطريقة لفئة [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). يوضح لك المثال البرمجي التالي كيفية استبدال النص في ملف PDF موجود.

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

تحقق من كيف يبدو في المستند الأصلي:

![استبدال النص](replace_text1.png)

وتحقق من النتيجة بعد استبدال النص:

![نتيجة استبدال النص](replace_text2.png)

في المثال الثاني، سترى كيف يمكنك، بالإضافة إلى استبدال النص، زيادة أو تقليل حجم الخط:
```csharp
public static void ReplaceText02()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.BindPdf(_dataDir + "sample.pdf");
        editor.ReplaceText("Value", "Label", 12);

        // حفظ الملف الناتج
        editor.Save(_dataDir + "PdfContentEditorDemo02.pdf");
    }
```

للحصول على إمكانيات أكثر تقدمًا للعمل مع نصوصنا، سنستخدم طريقة [TextState](https://reference.aspose.com/pdf/net/aspose.pdf.text/textstate). باستخدام هذه الطريقة، يمكننا جعل النص غامقًا، مائلًا، ملونًا، وما إلى ذلك.

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

        // حفظ الملف الناتج
        editor.Save(_dataDir + "PdfContentEditorDemo03.pdf");
    }
```

في حال كنت بحاجة إلى استبدال كل النص المحدد في المستند، استخدم مقطع الكود التالي. ذلك هو، سيتم استبدال النص أينما تم العثور على النص المحدد للاستبدال، وسيتم أيضًا عد عدد هذه الاستبدالات.

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

![استبدل كل النص](replace_text3.png)

يظهر مقطع الشفرة التالي كيفية إجراء جميع استبدالات النص ولكن في صفحة محددة من مستندك.

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
في مقتطف الشيفرة التالي، سوف نوضح كيفية استبدال، على سبيل المثال، رقم معين بالحروف التي نحتاجها.

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
        // حفظ ملف الإخراج
        editor.Save(_dataDir + "PdfContentEditorDemo06.pdf");
    }
```