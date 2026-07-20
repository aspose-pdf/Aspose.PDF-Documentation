---
title: حذف الصور من ملف PDF في Node.js
linktitle: حذف الصور
type: docs
weight: 20
url: /ar/nodejs-cpp/delete-images-from-pdf-file/
description: تشرح هذه الفقرة كيفية حذف الصور من ملف PDF باستخدام Aspose.PDF for Node.js عبر C++.
lastmod: "2026-07-16"
---


يمكنك حذف الصور من ملف PDF باستخدام Aspose.PDF for Node.js عبر C++.

في حال رغبتك في حذف الصور من PDF، يمكنك استخدام [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/) دالة. 
يرجى التحقق من مقتطف الشيفرة التالي من أجل حذف الصور في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` الوحدة ك `AsposePdf` متغير.
1. حدّد اسم ملف الـ PDF الذي سيتم إزالة الصورة منه.
1. اتصال `AsposePdf` كـ Promise وتنفيذ العملية لإزالة الصور. استقبل الكائن إذا نجح.
1. استدع الدالة [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
1. حذف الصور من ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfDeleteImages.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete images from a PDF-file and save the "ResultPdfDeleteImages.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
        console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. استيراد `asposepdfnodejs` وحدة.
1. حدّد اسم ملف الـ PDF الذي سيتم إزالة الصورة منه.
1. تهيئة وحدة AsposePdf. استقبل الكائن إذا نجحت العملية.
1. استدع الدالة [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
1. حذف الصور من ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfDeleteImages.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete images from a PDF-file and save the "ResultPdfDeleteImages.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
    console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```