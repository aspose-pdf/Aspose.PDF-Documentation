---
title: إضافة إجراءات جافا سكريبت إلى ملف PDF موجود
type: docs
weight: 10
url: /java/adding-javascript-actions/
description: يوضح هذا القسم كيفية إضافة إجراءات جافا سكريبت إلى ملف PDF موجود باستخدام Aspose.PDF Facades.
lastmod: "2021-06-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

توفر فئة [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) الموجودة ضمن حزمة com.aspose.pdf.facades المرونة لإضافة إجراءات جافا سكريبت إلى ملف PDF. يمكنك إنشاء رابط مع الإجراءات التسلسلية المقابلة لتنفيذ عنصر قائمة في عارض PDF. توفر هذه الفئة أيضًا ميزة إنشاء إجراءات إضافية لأحداث المستند.

أولاً وقبل كل شيء، يتم رسم كائن في [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)، في مثالنا [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle).
 وضع الإجراء [createJavaScriptLink](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#createJavaScriptLink-java.lang.String-java.awt.Rectangle-int-java.awt.Color-) على المستطيل. بعد ذلك يمكنك حفظ المستند الخاص بك.

```java
 public static void AddingJavascriptActions() {
        PdfContentEditor editor = new PdfContentEditor();
        editor.bindPdf(_dataDir+"sample.pdf");
        // إنشاء رابط جافا سكريبت
        java.awt.Rectangle rect = new java.awt.Rectangle(50, 750, 50, 50);
        String code = "app.alert('Welcome to Aspose!');";
        editor.createJavaScriptLink(code, rect, 1, java.awt.Color.GREEN);
        // حفظ ملف الإخراج
        editor.save(_dataDir+"JavaScriptAdded_output.pdf");
    }
```