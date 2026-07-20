---
title: استخراج الصور من PDF في Node.js
linktitle: استخراج الصور من PDF
type: docs
weight: 20
url: /ar/nodejs-cpp/extract-images-from-the-pdf-file/
description: يوضح هذا الموضوع كيفية استخراج الصور من PDF باستخدام Aspose.PDF لـ Node.js عبر C++.
lastmod: "2026-07-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج الصور من ملفات PDF في بيئة Node.js

إذا كنت ترغب في استخراج الصور من مستند PDF، يمكنك استخدام الدالة [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
يجب أن نمرّر ثلاثة وسائط إلى هذه الدالة:  اسم ملف الإدخال والإخراج والدقة.
الرجاء التحقق من مقتطف الشيفرة التالي لاستخراج الصور من ملف PDF باستخدام Node.js.

**CommonJS:**

1. استدعِ `require` واستورد الوحدة `asposepdfnodejs` في المتغير `AsposePdf`.
1. حدد اسم ملف PDF الذي سيتم استخراج الصورة منه.
1. استدعِ `AsposePdf` كـ Promise ونفّذ عملية استخراج الصورة. استلم الكائن إذا نجحت العملية.
1. استدعِ الدالة [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. استخرج الصور من ملف PDF. إذا كانت القيمة `json.errorCode` تساوي `0`، فسيتم حفظ النتيجة في `"ResultPdfExtractImage{0:D2}.jpg"`، حيث يمثّل `{0:D2}` رقم الصفحة بصيغة من رقمين. تُحفظ الصور بدقة 150 DPI. وإذا لم تكن القيمة كذلك، فستجد معلومات الخطأ في `json.errorText`.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extract image from a PDF-file with template "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
      console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استورد الوحدة `asposepdfnodejs`.
1. حدد اسم ملف PDF الذي سيتم استخراج الصورة منه.
1. هيّئ الوحدة `AsposePdf`. استلم الكائن إذا نجحت العملية.
1. استدعِ الدالة [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. استخرج الصور من ملف PDF. إذا كانت القيمة `json.errorCode` تساوي `0`، فسيتم حفظ النتيجة في `"ResultPdfExtractImage{0:D2}.jpg"`، حيث يمثّل `{0:D2}` رقم الصفحة بصيغة من رقمين. تُحفظ الصور بدقة 150 DPI. وإذا لم تكن القيمة كذلك، فستجد معلومات الخطأ في `json.errorText`.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Extract image from a PDF-file with template "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
    const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
    console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```
