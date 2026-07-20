---
title: إزالة المرفقات من PDF في Node.js
linktitle: إزالة مرفق من ملف PDF موجود
type: docs
weight: 10
url: /ar/nodejs-cpp/removing-attachment-from-an-existing-pdf/
description: يمكن لـ Aspose.PDF إزالة المرفقات من مستندات PDF الخاصة بك. استخدم بيئة Node.js لإزالة المرفقات في ملفات PDF بواسطة Aspose.PDF.
lastmod: "2026-07-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

يمكنك حذف المرفقات من ملف PDF باستخدام Aspose.PDF for Node.js عبر C++. في حال رغبتك في حذف المرفقات من PDF، يمكنك الاستخدام [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/) دالة. 
يرجى فحص مقتطف الشيفرة التالي بهدف حذف المرفقات من ملف PDF في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` وحدة كـ `AsposePdf` متغير.
1. حدّد اسم ملف PDF الذي ستُزال منه المرفقات.
1. اتصال `AsposePdf` كـ Promise ونفّذ العملية لإزالة المرفقات. استلم الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. احذف المرفقات. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfDeleteAttachments.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete attachments from a PDF-file and save the "ResultPdfDeleteAttachments.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
        console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. استيراد `asposepdfnodejs` الوحدة.
1. حدّد اسم ملف PDF الذي ستُزال منه المرفقات.
1. تهيئة وحدة AsposePdf. استلم الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. احذف المرفقات. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfDeleteAttachments.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete attachments from a PDF-file and save the "ResultPdfDeleteAttachments.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
    console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```