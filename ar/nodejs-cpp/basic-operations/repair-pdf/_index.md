---
title: إصلاح ملفات PDF في Node.js
linktitle: إصلاح PDF
type: docs
weight: 10
url: /ar/nodejs-cpp/repair-pdf/
description: يشرح هذا الموضوع كيفية إصلاح ملفات PDF في بيئة Node.js.
lastmod: "2026-07-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

يتيح Aspose.PDF لـ Node.js إصلاح ملفات PDF بجودة عالية. قد لا يفتح ملف PDF لأي سبب، بغض النظر عن البرنامج أو المتصفح. في بعض الحالات يمكن استعادة المستند. جرّب الشيفرة التالية وشاهد ذلك بنفسك.
إذا كنت تريد إصلاح مستند PDF، يمكنك استخدام الدالة [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
يرجى مراجعة مقطع الشيفرة التالي لإصلاح ملف PDF في بيئة Node.js.

**CommonJS:**

1. استدعِ `require` واستورد الوحدة `asposepdfnodejs` في المتغير `AsposePdf`.
1. حدد اسم ملف PDF الذي سيتم إصلاحه.
1. استدعِ `AsposePdf` كـ Promise ونفّذ عملية إصلاح الملف. استلم الكائن إذا نجحت العملية.
1. استدع الدالة [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. أصلِح ملف PDF. إذا كانت القيمة `json.errorCode` تساوي `0`، فسيتم حفظ النتيجة في `"ResultPdfRepair.pdf"`. وإذا لم تكن كذلك، فستجد معلومات الخطأ في `json.errorText`.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
    /*Repair a PDF-file and save the "ResultPdfRepair.pdf"*/
    const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
    console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استورد الوحدة `asposepdfnodejs`.
1. حدد اسم ملف PDF الذي سيتم إصلاحه.
1. هيّئ الوحدة `AsposePdf`. استلم الكائن إذا نجحت العملية.
1. استدع الدالة [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. أصلِح ملف PDF. إذا كانت القيمة `json.errorCode` تساوي `0`، فسيتم حفظ النتيجة في `"ResultPdfRepair.pdf"`. وإذا لم تكن كذلك، فستجد معلومات الخطأ في `json.errorText`.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Repair a PDF-file and save the "ResultPdfRepair.pdf"*/
  const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
  console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```
