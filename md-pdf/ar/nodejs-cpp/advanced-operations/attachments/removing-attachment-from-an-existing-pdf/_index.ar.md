---
title: إزالة المرفقات من PDF في Node.js
linktitle: إزالة المرفقات من PDF موجود
type: docs
weight: 10
url: /nodejs-cpp/removing-attachment-from-an-existing-pdf/
description: يمكن لـ Aspose.PDF إزالة المرفقات من مستندات PDF الخاصة بك. استخدم بيئة Node.js لإزالة المرفقات في ملفات PDF بواسطة Aspose.PDF.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

يمكنك حذف المرفقات من ملف PDF باستخدام Aspose.PDF لـ Node.js عبر C++. في حالة رغبتك في حذف المرفقات من ملف PDF، يمكنك استخدام [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/) وظيفة. 
يرجى التحقق من الشفرة البرمجية التالية لحذف المرفقات من ملف PDF في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
1. حدد اسم ملف PDF الذي ستتم إزالة المرفقات منه.

1. استدعاء `AsposePdf` كـ Promise وتنفيذ العملية لإزالة المرفقات. استلم الكائن إذا تم بنجاح.
1. استدعاء الدالة [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. احذف المرفقات. وبالتالي، إذا كانت 'json.errorCode' تساوي 0، يتم حفظ نتيجة العملية في "ResultPdfDeleteAttachments.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وظهرت بالتالي خطأ في ملفك، ستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*حذف المرفقات من ملف PDF وحفظ "ResultPdfDeleteAttachments.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
        console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي سيتم إزالة المرفقات منه.
1. تهيئة وحدة AsposePdf. تلقي الكائن إذا تم بنجاح.
1. استدعاء الدالة [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. حذف المرفقات. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfDeleteAttachments.pdf". إذا كان معامل json.errorCode ليس 0 وظهرت بالتالي خطأ في ملفك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*حذف المرفقات من ملف PDF وحفظ "ResultPdfDeleteAttachments.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
    console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```