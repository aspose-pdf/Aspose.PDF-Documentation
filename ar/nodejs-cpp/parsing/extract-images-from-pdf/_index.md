---
title: استخراج الصور من PDF في Node.js
linktitle: استخراج الصور من PDF
type: docs
weight: 20
url: /ar/nodejs-cpp/extract-images-from-the-pdf-file/
description: كيفية استخراج جزء من الصورة من PDF باستخدام Aspose.PDF لأداة Node.js عبر C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج الصور من ملفات PDF في بيئة Node.js

في حال كنت ترغب في استخراج الصور من مستند PDF، يمكنك استخدام دالة [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/). 
يجب علينا تمرير ثلاثة معطيات إلى هذه الدالة: اسم الملف المدخل والمخرج والدقة.
يرجى مراجعة مقتطف الشيفرة التالي لاستخراج الصور من ملف PDF باستخدام Node.js.

**CommonJS:**

1. استدع `require` واستورد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
1. حدد اسم ملف PDF الذي ستستخرج منه الصورة.

1. استدعاء `AsposePdf` كـ Promise وتنفيذ العملية لاستخراج الصورة. استلم الكائن إذا نجحت العملية.
1. استدعاء الدالة [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. استخراج الصور من ملف PDF. لذلك، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfExtractImage{0:D2}.jpg". حيث يمثل {0:D2} رقم الصفحة بتنسيق مكون من رقمين. يتم حفظ الصور بدقة 150 DPI. إذا كان معامل json.errorCode لا يساوي 0 وظهرت خطأ في ملفك، سيتم تضمين معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /* استخراج الصورة من ملف PDF باستخدام القالب "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... تنسيق رقم الصفحة)، دقة 150 DPI وحفظ*/
      const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
      console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي سيتم استخراج الصورة منه.
1. تهيئة وحدة AsposePdf. استلم الكائن إذا تم بنجاح.
1. استدعاء الدالة [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. استخراج الصور من ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfExtractImage{0:D2}.jpg". حيث يمثل {0:D2} رقم الصفحة بتنسيق مكون من رقمين. يتم حفظ الصور بدقة 150 DPI. إذا لم يكن معامل json.errorCode يساوي 0 وظهر خطأ في ملفك، فإن معلومات الخطأ ستكون موجودة في 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*استخراج الصورة من ملف PDF باستخدام القالب "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... صيغة رقم الصفحة)، دقة 150 DPI وحفظها*/
    const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
    console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```