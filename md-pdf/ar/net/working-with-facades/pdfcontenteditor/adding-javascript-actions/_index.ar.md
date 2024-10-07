---
title: إضافة إجراءات جافا سكريبت PDF 
type: docs
weight: 10
url: /net/adding-javascript-actions/
description: يوضح هذا القسم كيفية إضافة إجراءات جافا سكريبت إلى ملف PDF موجود باستخدام Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

توفر فئة [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/PdfContentEditor) الموجودة ضمن حزمة Aspose.Pdf.Facades المرونة لإضافة إجراءات جافا سكريبت إلى ملف PDF. يمكنك إنشاء رابط مع الإجراءات التسلسلية المقابلة لتنفيذ عنصر قائمة في عارض PDF. توفر هذه الفئة أيضًا ميزة إنشاء إجراءات إضافية لأحداث المستندات.

أولاً، يتم رسم كائن في [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)، في مثالنا [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle). وضع الإجراء [createJavaScriptLink](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createjavascriptlink) إلى المستطيل. بعد ذلك يمكنك حفظ المستند.

```csharp
  public static void AddingJavascriptActions()
        {
            PdfContentEditor editor = new PdfContentEditor();
            editor.BindPdf(_dataDir + "sample.pdf");
            // إنشاء رابط جافا سكريبت
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(50, 750, 50, 50);
            String code = "app.alert('Welcome to Aspose!');";
            editor.CreateJavaScriptLink(code, rect, 1, System.Drawing.Color.Green);
            // حفظ ملف الإخراج
            editor.Save(_dataDir + "JavaScriptAdded_output.pdf");
        }
```