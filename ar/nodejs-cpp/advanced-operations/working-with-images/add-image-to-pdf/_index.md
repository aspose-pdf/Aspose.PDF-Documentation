---
title: إضافة صورة إلى PDF في Node.js
linktitle: إضافة صورة
type: docs
weight: 10
url: /ar/nodejs-cpp/add-image-to-pdf/
description: يصف هذا القسم كيفية إضافة صورة إلى ملف PDF موجود باستخدام Aspose.PDF for Node.js via C++.
lastmod: "2026-07-16"
---

## إضافة صورة إلى ملف PDF موجود

يُعتقد عادةً أن إضافة الصور إلى ملفات PDF تتطلب أداة معقدة خاصة. ومع ذلك، باستخدام Aspose.PDF for Node.js يمكنك بسرعة وسهولة إضافة الصور التي تحتاجها إلى PDF في بيئة Node.js.

يمكننا إضافة الصور إلى نهاية الملف فقط، لذلك المثال الصحيح هو أن لدينا بعض صفحات المستند الممسوح ضوئيا ونقوم بتحويلها إلى PDF واحد.

في حال رغبتك في إضافة صور، يمكنك استخدام [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/) دالة. 
يرجى مراجعة المقتطف البرمجي التالي لإضافة صور في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` الوحدة كـ `AsposePdf` متغيّر.
1. حدد اسم ملف PDF الذي ستُضاف إليه الصورة.
1. اتصال `AsposePdf` كـ Promise وأداء العملية لإضافة صورة. استلم الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. أضف الصورة إلى نهاية ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultAddImage.pdf". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، ستحتوي معلومات الخطأ على 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add an image to end a PDF-file and save the "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
      console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` وحدة.
1. حدد اسم ملف PDF الذي ستُضاف إليه الصورة.
1. تهيئة وحدة AsposePdf. استلم الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. أضف الصورة إلى نهاية ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultAddImage.pdf". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، ستحتوي معلومات الخطأ على 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  /*Add an image to end a PDF-file and save the "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
  console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```