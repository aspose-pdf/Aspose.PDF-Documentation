---
title: استخراج النص من PDF في Node.js
linktitle: استخراج النص من PDF
type: docs
weight: 10
url: /ar/nodejs-cpp/extract-text/
description: يوضح هذا القسم كيفية استخراج النص من مستند PDF باستخدام Aspose.PDF لـ Node.js عبر C++.
lastmod: "2026-07-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج النص من جميع صفحات مستند PDF

استخراج النص من PDF ليس أمرًا سهلًا. فعدد قليل فقط من قارئات PDF يمكنه استخراج النص من صور PDF أو من ملفات PDF الممسوحة ضوئيًا. لكن **Aspose.PDF لـ Node.js عبر C++** يتيح لك استخراج النص بسهولة من ملفات PDF في بيئة Node.js.

يوضح هذا المثال كيفية استخدام وحدة `asposepdfnodejs` لاستخراج النص من ملف PDF محدد وتسجيل النص المستخرج أو الأخطاء التي قد تظهر.

تحقق من مقتطفات الشيفرة واتبع الخطوات لاستخراج النص من ملف PDF الخاص بك:

**CommonJS:**

1. استدعِ `require` واستورد الوحدة `asposepdfnodejs` في المتغير `AsposePdf`.
1. حدّد اسم ملف PDF الذي سيتم استخراج النص منه.
1. استدعِ `AsposePdf` كـ Promise ونفّذ عملية استخراج النص. استلم الكائن إذا نجحت العملية.
1. استدعِ الدالة [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. يتم تخزين النص المستخرج في كائن JSON. إذا كانت القيمة `json.errorCode` تساوي `0`، فسيتم عرض النص المستخرج باستخدام `console.log`. وإذا لم تكن كذلك، فستحتوي `json.errorText` على معلومات الخطأ.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extract text from a PDF-file*/
      const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
      console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استورد الوحدة `asposepdfnodejs`.
1. حدّد اسم ملف PDF الذي سيتم استخراج النص منه.
1. هيّئ الوحدة `AsposePdf`. استلم الكائن إذا نجحت العملية.
1. استدعِ الدالة [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. يتم تخزين النص المستخرج في كائن JSON. إذا كانت القيمة `json.errorCode` تساوي `0`، فسيتم عرض النص المستخرج باستخدام `console.log`. وإذا لم تكن كذلك، فستحتوي `json.errorText` على معلومات الخطأ.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Extract text from a PDF-file*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```
