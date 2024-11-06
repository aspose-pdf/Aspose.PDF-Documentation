---
title: حذف الصور من ملف PDF في Node.js
linktitle: حذف الصور
type: docs
weight: 20
url: ar/nodejs-cpp/delete-images-from-pdf-file/
description: يشرح هذا القسم كيفية حذف الصور من ملف PDF باستخدام Aspose.PDF لـ Node.js عبر C++.
lastmod: "2023-11-16"
---

يمكنك حذف الصور من ملف PDF باستخدام Aspose.PDF لـ Node.js عبر C++.

في حالة رغبتك في حذف الصور من PDF، يمكنك استخدام وظيفة [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/). 
يرجى التحقق من جزء الكود التالي من أجل حذف الصور في بيئة Node.js.

**CommonJS:**

1. قم باستدعاء `require` واستيراد الوحدة `asposepdfnodejs` كمتغير `AsposePdf`.
2. حدد اسم ملف PDF الذي سيتم إزالة الصور منه.
3. قم باستدعاء `AsposePdf` كـ Promise وقم بتنفيذ العملية لإزالة الصور. استلم الكائن إذا نجحت العملية.
4. قم باستدعاء الوظيفة [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).

1. حذف الصور من ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfDeleteImages.pdf". إذا كان معامل json.errorCode ليس 0، وظهرت بالتالي خطأ في ملفك، سيتم تضمين معلومات الخطأ في 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*حذف الصور من ملف PDF وحفظ "ResultPdfDeleteImages.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
        console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي سيتم إزالة الصورة منه.
1. تهيئة وحدة AsposePdf. استلم الكائن إذا كان ناجحاً.

1. استدع وظيفة [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
1. حذف الصور من ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfDeleteImages.pdf". إذا لم يكن معامل json.errorCode يساوي 0 وظهر خطأ في ملفك، فإن معلومات الخطأ ستكون موجودة في 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*حذف الصور من ملف PDF وحفظ "ResultPdfDeleteImages.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
    console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```