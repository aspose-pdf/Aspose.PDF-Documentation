---
title: الإشارات المرجعية في PDF في Node.js
linktitle: الإشارات المرجعية في PDF
type: docs
weight: 10
url: /ar/nodejs-cpp/bookmark/
description: يمكنك إضافة أو حذف إشارة مرجعية في مستند PDF في بيئة Node.js.
lastmod: "2026-07-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## حذف إشارة مرجعية معينة من مستند PDF

يمكنك حذف الإشارات المرجعية من ملف PDF باستخدام Aspose.PDF for Node.js via C++. إذا رغبت في حذف الإشارات المرجعية من PDF، يمكنك استخدام [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/) دالة. 
يرجى مراجعة مقتطف الشيفرة التالي لحذف العلامات المرجعية من ملف PDF في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` وحدة كـ `AsposePdf` متغيّر.
1. حدد اسم ملف PDF الذي سيُزال منه العلامات المرجعية.
1. اتصال `AsposePdf` كـ Promise وتنفيذ العملية لإزالة العلامة المرجعية. استلم الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. احذف إشارات المرجعية. وبالتالي، إذا كان 'json.errorCode' يساوي 0، سيتم حفظ نتيجة العملية في "ResultPdfDeleteBookmarks.pdf". إذا كان معامل json.errorCode ليس 0 وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete bookmarks from a PDF-file and save the "ResultPdfDeleteBookmarks.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
        console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. استيراد `asposepdfnodejs` وحدة.
1. حدد اسم ملف PDF الذي سيُزال منه العلامات المرجعية.
1. تهيئة وحدة AsposePdf. استلام الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. احذف إشارات المرجعية. وبالتالي، إذا كان 'json.errorCode' يساوي 0، سيتم حفظ نتيجة العملية في "ResultPdfDeleteBookmarks.pdf". إذا كان معامل json.errorCode ليس 0 وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete bookmarks from a PDF-file and save the "ResultPdfDeleteBookmarks.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
    console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```