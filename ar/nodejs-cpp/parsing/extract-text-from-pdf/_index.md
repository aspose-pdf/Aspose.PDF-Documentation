---
title: تحليل النص من PDF في Node.js
linktitle: تحليل النص من PDF
type: docs
weight: 30
url: /ar/nodejs-cpp/extract-text-from-pdf/
description: تستعرض هذه المقالة طرقًا متعددة لاستخراج النص من ملفات PDF باستخدام Aspose.PDF لـ Node.js عبر C++.
lastmod: "2026-07-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## تحليل النص من مستند PDF

يُعدّ تحليل النص من مستند PDF مهمة شائعة ومفيدة جدًا. 
يخدم استخراج النص من ملفات PDF مجموعة متنوعة من الأغراض، من تحسين البحث وإمكانية الوصول إلى تمكين التحليل وأتمتة البيانات في مجالات مختلفة مثل الأعمال والبحث وإدارة المعلومات.

إذا كنت ترغب في استخراج النص من مستند PDF، يمكنك استخدام الدالة [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
يرجى مراجعة مقتطف الشيفرة التالي لاستخراج النص من ملف PDF باستخدام Node.js عبر C++.

تحقق من مقتطفات الشيفرة واتبع الخطوات لاستخراج النص من ملف PDF الخاص بك:

**CommonJS:**

1. استدعِ `require` واستورد الوحدة `asposepdfnodejs` في المتغير `AsposePdf`.
1. حدّد اسم ملف الـ PDF الذي سيُستخرج منه النص.
1. استدعِ `AsposePdf` كـ Promise ونفّذ عملية استخراج النص. استلم الكائن إذا نجحت العملية.
1. استدعِ الدالة [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. يُخزن النص المستخرج في كائن JSON. إذا كانت القيمة `json.errorCode` تساوي `0`، فسيتم عرض النص المستخرج باستخدام `console.log`. وإذا لم تكن كذلك، فستكون معلومات الخطأ موجودة في `json.errorText`.

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
1. حدّد اسم ملف الـ PDF الذي سيُستخرج منه النص.
1. هيّئ الوحدة `AsposePdf`. استلم الكائن إذا نجحت العملية.
1. استدعِ الدالة [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. يُخزن النص المستخرج في كائن JSON. إذا كانت القيمة `json.errorCode` تساوي `0`، فسيتم عرض النص المستخرج باستخدام `console.log`. وإذا لم تكن كذلك، فستكون معلومات الخطأ موجودة في `json.errorText`.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Extract text from a PDF-file*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```
