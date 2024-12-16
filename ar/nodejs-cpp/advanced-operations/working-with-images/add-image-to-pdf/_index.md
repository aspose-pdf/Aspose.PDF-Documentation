---
title: إضافة صورة إلى ملف PDF في Node.js 
linktitle: إضافة صورة
type: docs
weight: 10
url: /ar/nodejs-cpp/add-image-to-pdf/
description: يصف هذا القسم كيفية إضافة صورة إلى ملف PDF موجود باستخدام Aspose.PDF لـ Node.js عبر C++.
lastmod: "2023-11-16"
---

## إضافة صورة إلى ملف PDF موجود

يُعتقد عمومًا أن إضافة الصور إلى ملفات PDF يتطلب أداة خاصة معقدة. ومع ذلك، باستخدام Aspose.PDF لـ Node.js يمكنك بسرعة وسهولة إضافة الصور التي تحتاجها إلى PDF في بيئة Node.js.

يمكننا إضافة الصور فقط في نهاية الملف، لذا المثال الصحيح هو أن لدينا بعض صفحات الوثائق الممسوحة ضوئيًا ونقوم بتحويلها إلى ملف PDF واحد.

في حال أردت إضافة الصور، يمكنك استخدام [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/) وظيفة.
يرجى مراجعة مقتطف الشيفرة التالي من أجل إضافة الصور في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.

1. حدد اسم ملف الـ PDF الذي ستضاف إليه الصورة.
1. استدعاء `AsposePdf` كـ Promise وأداء العملية لإضافة الصورة. استلم الكائن إذا كان ناجحًا.
1. استدعِ الدالة [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. إضافة صورة إلى نهاية ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultAddImage.pdf". إذا لم يكن معامل json.errorCode يساوي 0 وظهرت خطأ في ملفك، فسيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*إضافة صورة إلى نهاية ملف PDF وحفظ "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
      console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. حدد اسم ملف PDF الذي سيتم إضافة الصورة إليه.
1. تهيئة وحدة AsposePdf. استلم الكائن إذا تم بنجاح.
1. استدعاء الدالة [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. إضافة الصورة إلى نهاية ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultAddImage.pdf". إذا كانت قيمة json.errorCode ليست 0 وظهر خطأ في ملفك، فإن معلومات الخطأ ستكون موجودة في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  /*أضف صورة إلى نهاية ملف PDF واحفظ "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
  console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```