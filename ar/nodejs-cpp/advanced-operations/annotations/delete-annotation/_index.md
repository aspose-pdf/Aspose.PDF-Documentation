---
title: حذف التعليق التوضيحي في Node.js
linktitle: حذف التعليق التوضيحي
type: docs
weight: 10
url: /ar/nodejs-cpp/delete-annotation/
description: باستخدام Aspose.PDF for Node.js يمكنك حذف التعليق التوضيحي من ملف PDF الخاص بك.
lastmod: "2026-07-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

يمكنك حذف التعليقات التوضيحية من ملف PDF باستخدام Aspose.PDF for Node.js عبر C++. في حال رغبتك في حذف التعليقات التوضيحية من PDF، يمكنك استخدام [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/) دالة. 
يرجى مراجعة مقتطف الشيفرة التالي لحذف التعليقات التوضيحية من ملف PDF في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` وحدة كـ `AsposePdf` متغير.
1. حدد اسم ملف PDF الذي ستتم إزالة التعليقات التوضيحية منه.
1. اتصال `AsposePdf` كـ Promise وتنفيذ العملية لإزالة التعليقات التوضيحية. استقبل الكائن إذا نجحت.
1. استدعِ الدالة [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/).
1. احذف التعليقات التوضيحية. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfDeleteAnnotations.pdf". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، سيتم تضمين معلومات الخطأ في 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete annotations from a PDF-file and save the "ResultPdfDeleteAnnotations.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAnnotations(pdf_file, "ResultPdfDeleteAnnotations.pdf");
        console.log("AsposePdfDeleteAnnotations => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. استيراد `asposepdfnodejs` وحدة.
1. حدد اسم ملف PDF الذي ستتم إزالة التعليقات التوضيحية منه.
1. ابدأ وحدة AsposePdf. استلم الكائن إذا كان ناجحًا.
1. استدعِ الدالة [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/).
1. احذف التعليقات التوضيحية. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfDeleteAnnotations.pdf". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، سيتم تضمين معلومات الخطأ في 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete annotations from a PDF-file and save the "ResultPdfDeleteAnnotations.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAnnotations(pdf_file, "ResultPdfDeleteAnnotations.pdf");
    console.log("AsposePdfDeleteAnnotations => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```
