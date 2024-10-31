---
title: إصلاح ملف PDF في Node.js 
linktitle: إصلاح PDF
type: docs
weight: 10
url: /nodejs-cpp/repair-pdf/
description: يصف هذا الموضوع كيفية إصلاح ملف PDF في بيئة Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

يسمح Aspose.PDF لـ Node.js بإصلاح ملفات PDF بجودة عالية. قد لا يفتح ملف PDF لأي سبب، بغض النظر عن البرنامج أو المتصفح. في بعض الحالات يمكن استعادة الوثيقة، جرب الكود التالي لترى بنفسك.
في حال كنت ترغب في إصلاح مستند PDF، يمكنك استخدام وظيفة [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
يرجى التحقق من الكود التالي لإصلاح ملف PDF في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
1. تحديد اسم ملف PDF الذي سيتم إصلاحه.
1. استدعاء `AsposePdf` كـ Promise وتنفيذ العملية لإصلاح الملف. استلام الكائن إذا كان ناجحًا.

1. استدعاء الدالة [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. إصلاح ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfRepair.pdf". إذا كان معامل json.errorCode لا يساوي 0، وبالتالي، يظهر خطأ في ملفك، ستحتوي معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
    /*إصلاح ملف PDF وحفظ "ResultPdfRepair.pdf"*/
    const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
    console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي سيتم إصلاحه.
1. تهيئة وحدة AsposePdf. تلقي الكائن إذا نجحت العملية.

1. استدعاء الدالة [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. إصلاح ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfRepair.pdf". إذا كان معامل json.errorCode ليس 0 وبناءً عليه، تظهر خطأ في ملفك، ستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*إصلاح ملف PDF وحفظ "ResultPdfRepair.pdf"*/
  const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
  console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```