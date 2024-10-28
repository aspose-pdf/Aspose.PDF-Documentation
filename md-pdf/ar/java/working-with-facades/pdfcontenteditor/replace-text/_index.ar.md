---
title: استبدال النص في ملف PDF
type: docs
weight: 40
url: /java/replace-text/
description: يوضح هذا القسم كيفية استبدال النص باستخدام Aspose.PDF Facades - مجموعة أدوات للعمليات الشائعة مع PDF.
lastmod: "2021-06-24"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## استبدال النص في ملف PDF موجود (الواجهات)

من أجل استبدال النص في ملف PDF موجود، تحتاج إلى إنشاء كائن من فئة [pdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor)، وربط ملف PDF مدخل باستخدام طريقة bindPdf. بعد ذلك، تحتاج إلى استدعاء طريقة [replaceText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#replaceText-java.lang.String-int-java.lang.String-). تحتاج إلى حفظ ملف PDF المحدث باستخدام طريقة save من فئة [pdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor). يوضح لك مقتطف الشفرة التالي كيفية استبدال النص في ملف PDF موجود.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.TextState;
import com.aspose.pdf.facades.PdfContentEditor;
import com.aspose.pdf.facades.ReplaceTextStrategy;

public class PdfContentEditorText {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void ReplaceText01(){
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");        
        editor.replaceText("Value", "Label");

        // حفظ ملف الإخراج
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    
```


تحقق من كيف تبدو في المستند الأصلي:

![استبدال النص](replace_text1.png)

وتحقق من النتيجة بعد استبدال النص:

![نتيجة استبدال النص](replace_text2.png)

في المثال الثاني، سترى كيف يمكنك، بالإضافة إلى استبدال النص، زيادة أو تقليل حجم الخط:

```java
public static void ReplaceText02(){
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");        
        editor.replaceText("Value", "Label", 12);

        // حفظ ملف الإخراج
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    
```

لإمكانيات أكثر تقدمًا للعمل مع نصوصنا، سنستخدم طريقة [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState). باستخدام هذه الطريقة، يمكننا جعل النص عريض، مائل، ملون، وهكذا.

```java
public static void ReplaceText03(){
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");        
        TextState textState = new TextState();
        textState.setFontSize(12);
        editor.replaceText("Value", "Label", textState);

        // حفظ ملف الإخراج
        editor.save(_dataDir+"replaced_text_demo.pdf");
    }    

```


في حالة الحاجة لاستبدال كل النص المحدد في المستند، استخدم جزء الشيفرة البرمجية التالي. أي أن الاستبدال للنص سيتم أينما واجه النص المحدد للاستبدال، وسيتم أيضًا حساب عدد مثل هذه الاستبدالات.

```java
    public static void ReplaceText04()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.replaceText("Value", "Label")) count++;

        System.out.println(count+" occurrences have been replaced.");

        // احفظ ملف الإخراج
        editor.save(_dataDir + "PdfContentEditorDemo04.pdf");
    }
```

![استبدال كل النص](replace_text3.png)

يظهر جزء الشيفرة البرمجية التالي كيفية إجراء كل استبدالات النص ولكن في صفحة محددة من المستند.

```java
    public static void ReplaceText05()
    {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir + "sample.pdf");
        int count = 0;
        while (editor.replaceText("9999", 2, "ABCDE")) count++;
        System.out.println(count+" occurrences have been replaced.");

        // احفظ ملف الإخراج
        editor.save(_dataDir + "PdfContentEditorDemo05.pdf");
    }
```


في مقتطف الشيفرة التالي، سنوضح كيفية استبدال، على سبيل المثال، رقم معين بالحروف التي نحتاجها.

```java
    public static void ReplaceText06()
    {
        PdfContentEditor editor = new PdfContentEditor();
        ReplaceTextStrategy replaceTextStrategy = new ReplaceTextStrategy();
        replaceTextStrategy.setRegularExpressionUsed(true);
        replaceTextStrategy.setReplaceScope(ReplaceTextStrategy.Scope.ReplaceAll);
        editor.setReplaceTextStrategy(replaceTextStrategy);
        
        editor.bindPdf(_dataDir + "sample.pdf");
        editor.replaceText("\\d{4}", "ABCDE");

        // حفظ ملف الإخراج
        editor.save(_dataDir + "PdfContentEditorDemo06.pdf");
    }

}
```