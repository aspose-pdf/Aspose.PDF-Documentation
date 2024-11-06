---
title: تحويل PDF إلى DOC 
linktitle: تحويل PDF إلى DOC
type: docs
weight: 70
url: ar/androidjava/convert-pdf-to-doc/
lastmod: "2021-06-05"
description: تحويل ملف PDF إلى تنسيق DOC بسهولة وتحكم كامل باستخدام Aspose.PDF لـ Android عبر Java. تعرف على المزيد حول كيفية ضبط تحويل ملف Microsoft Word Doc إلى PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

إحدى أكثر الميزات شيوعًا هي تحويل PDF إلى مستند Microsoft Word DOC، مما يجعل المحتوى سهل التلاعب. يتيح لك Aspose.PDF لـ Android عبر Java تحويل ملفات PDF إلى DOC.

**Aspose.PDF لـ Android عبر Java** يمكنه إنشاء مستندات PDF من الصفر وهو مجموعة أدوات رائعة لتحديث وتحرير والتلاعب بمستندات PDF الحالية.
 ميزة مهمة هي القدرة على تحويل الصفحات والمستندات الكاملة بصيغة PDF إلى صور. ميزة شائعة أخرى هي تحويل PDF إلى مستند Microsoft Word DOC، مما يجعل من السهل التعامل مع المحتوى. (معظم المستخدمين لا يمكنهم تحرير مستندات PDF ولكن يمكنهم بسهولة العمل مع الجداول والنصوص والصور في Microsoft Word.)

لتبسيط الأمور وجعلها مفهومة، يوفر Aspose.PDF لـ Android عبر Java كود مكون من سطرين لتحويل ملف PDF المصدر إلى ملف DOC.

{{% alert color="primary" %}}

جرب عبر الإنترنت. يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت في هذا الرابط [products.aspose.app/pdf/conversion/pdf-to-doc](https://products.aspose.app/pdf/conversion/pdf-to-doc)

{{% /alert %}}

يوضح مقتطف الشيفرة التالي عملية تحويل ملف PDF إلى تنسيق DOC.

```java
 public void convertPDFtoDOC() {
        // فتح مستند PDF المصدر
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File docFileName = new File(fileStorage, "PDF-to-Word.doc");

        try {
            // حفظ الملف بتنسيق مستند MS
            document.save(docFileName.toString(), SaveFormat.Doc);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```