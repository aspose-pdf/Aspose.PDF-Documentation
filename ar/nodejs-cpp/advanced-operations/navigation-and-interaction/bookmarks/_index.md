---
title: الإشارات المرجعية في PDF في Node.js
linktitle: الإشارات المرجعية في PDF
type: docs
weight: 10
url: /ar/nodejs-cpp/bookmark/
description: يمكنك إضافة أو حذف الإشارات المرجعية في مستند PDF في بيئة Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## حذف إشارة مرجعية معينة من مستند PDF

يمكنك حذف الإشارات المرجعية من ملف PDF باستخدام Aspose.PDF for Node.js عبر C++. في حالة رغبتك في حذف الإشارات المرجعية من PDF، يمكنك استخدام وظيفة [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
يرجى التحقق من مقتطف الشفرة التالي من أجل حذف الإشارات المرجعية من ملف PDF في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
1. تحديد اسم ملف PDF الذي سيتم إزالة الإشارات المرجعية منه.
1. استدعاء `AsposePdf` كـ Promise وتنفيذ العملية لإزالة الإشارة المرجعية. استلم الكائن إذا كانت العملية ناجحة.

1. استدعاء الدالة [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. حذف العلامات المرجعية. وبالتالي، إذا كان 'json.errorCode' يساوي 0، فإن نتيجة العملية تُحفظ في "ResultPdfDeleteBookmarks.pdf". إذا كانت قيمة json.errorCode لا تساوي 0 وظهرت بالتالي خطأ في ملفك، فسيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*حذف العلامات المرجعية من ملف PDF وحفظ "ResultPdfDeleteBookmarks.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
        console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي سيتم إزالة العلامات المرجعية منه.

1. تهيئة وحدة AsposePdf. استلم الكائن إذا نجحت العملية.
1. استدعاء الدالة [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. حذف العلامات المرجعية. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfDeleteBookmarks.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وظهرت بالتالي خطأ في ملفك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*حذف العلامات المرجعية من ملف PDF وحفظ "ResultPdfDeleteBookmarks.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
    console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```