---
title: تحويل PDF إلى DOC
linktitle: تحويل PDF إلى DOC
type: docs
weight: 70
url: /ar/androidjava/convert-pdf-to-doc/
lastmod: "2026-06-30"
description: قم بتحويل ملف PDF إلى تنسيق DOC بسهولة وتحكم كامل باستخدام Aspose.PDF for Android via Java. تعرف على المزيد حول كيفية تحسين تحويل ملف Microsoft Word Doc إلى PDF.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

إحدى أكثر الميزات شيوعًا هي تحويل PDF إلى Microsoft Word DOC، مما يجعل المحتوى سهل التعديل. يتيح لك Aspose.PDF for Android via Java تحويل ملفات PDF إلى DOC.

**Aspose.PDF for Android via Java** يمكنه إنشاء مستندات PDF من الصفر وهو مجموعة أدوات رائعة لتحديث وتحرير وتعديل مستندات PDF الموجودة. ميزة مهمة هي القدرة على تحويل الصفحات ومستندات PDF بالكامل إلى صور. ميزة شائعة أخرى هي تحويل PDF إلى Microsoft Word DOC، مما يجعل المحتوى سهل التعديل. (معظم المستخدمين لا يستطيعون تحرير مستندات PDF لكن يمكنهم بسهولة العمل مع الجداول والنصوص والصور في Microsoft Word.)

لتبسيط الأمور وجعلها مفهومة، يوفر Aspose.PDF for Android via Java كودًا من سطرين لتحويل ملف PDF المصدر إلى ملف DOC.

{{% alert color="primary" %}}

جرّب عبر الإنترنت. يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت عبر هذا الرابط [products.aspose.app/pdf/conversion/pdf-to-doc](https://products.aspose.app/pdf/conversion/pdf-to-doc)

{{% /alert %}}

المقتطف البرمجي التالي يوضح عملية تحويل ملف PDF إلى تنسيق DOC.

```java
 public void convertPDFtoDOC() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File docFileName = new File(fileStorage, "PDF-to-Word.doc");

        try {
            // Save the file into MS document format
            document.save(docFileName.toString(), SaveFormat.Doc);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


