---
title: حذف التعليق التوضيحي في Node.js
linktitle: حذف التعليق التوضيحي
type: docs
weight: 10
url: /ar/nodejs-cpp/delete-annotation/
description: باستخدام Aspose.PDF لـ Node.js يمكنك حذف التعليق التوضيحي من ملف PDF الخاص بك.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

يمكنك حذف التعليقات التوضيحية من ملف PDF باستخدام Aspose.PDF لـ Node.js عبر C++. في حال كنت تريد حذف التعليقات التوضيحية من ملف PDF، يمكنك استخدام وظيفة [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/). 
يرجى التحقق من الكود المختصر التالي لحذف التعليقات التوضيحية من ملف PDF في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
2. تحديد اسم ملف PDF الذي سيتم إزالة التعليق التوضيحي منه.
3. استدعاء `AsposePdf` كـ Promise وتنفيذ العملية لإزالة التعليقات التوضيحية. استلم الكائن إذا كان ناجحًا.

1. استدعِ الدالة [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/).
1. حذف التعليقات التوضيحية. وبالتالي، إذا كان 'json.errorCode' هو 0، يتم حفظ نتيجة العملية في "ResultPdfDeleteAnnotations.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وظهرت بالتالي خطأ في ملفك، فإن معلومات الخطأ ستحتوي في 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*حذف التعليقات التوضيحية من ملف PDF وحفظه في "ResultPdfDeleteAnnotations.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAnnotations(pdf_file, "ResultPdfDeleteAnnotations.pdf");
        console.log("AsposePdfDeleteAnnotations => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. حدد اسم ملف PDF الذي سيتم إزالة التعليق التوضيحي منه.

1. قم بتهيئة وحدة AsposePdf. استلم الكائن إذا تم بنجاح.
1. استدعِ الدالة [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/).
1. احذف التعليقات التوضيحية. لذلك، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfDeleteAnnotations.pdf". إذا لم يكن معامل json.errorCode يساوي 0 وظهرت خطأ في ملفك، ستحتوي معلومات الخطأ في 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*حذف التعليقات التوضيحية من ملف PDF وحفظ "ResultPdfDeleteAnnotations.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAnnotations(pdf_file, "ResultPdfDeleteAnnotations.pdf");
    console.log("AsposePdfDeleteAnnotations => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```