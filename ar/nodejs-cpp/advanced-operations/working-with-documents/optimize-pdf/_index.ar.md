---
title: تحسين PDF باستخدام Aspose.PDF لـ Node.js عبر C++ 
linktitle: تحسين ملف PDF
type: docs
weight: 10
url: /nodejs-cpp/optimize-pdf/
description: تحسين وضغط ملفات PDF لتصفح سريع عبر الويب باستخدام بيئة Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## تحسين مستند PDF

تتيح لك مجموعة أدوات Aspose.PDF لـ Node.js عبر C++ تحسين محتوى PDF لبيئة Node.js.

يشير التحسين، أو الخطية، إلى عملية جعل ملف PDF مناسبًا للتصفح عبر الإنترنت باستخدام متصفح الويب.

في حال كنت ترغب في تحسين PDF، يمكنك استخدام وظيفة [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/). يرجى مراجعة مقتطف الشفرة التالي لتحسين ملفات PDF في بيئة Node.js.

**CommonJS:**

1. استدع `require` واستورد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
1. حدد اسم ملف PDF الذي سيتم تحسينه.

1. استدعاء `AsposePdf` كـ Promise وتنفيذ العملية لتحسين الملف. استلم الكائن إذا نجحت العملية.
1. استدعاء الدالة [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. تحسين ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultOptimize.pdf". إذا كانت قيمة المعامل json.errorCode ليست 0، وبالتالي يظهر خطأ في ملفك، سيتم تضمين معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*تحسين ملف PDF وحفظ "ResultOptimize.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
      console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي سيتم تحسينه.

1. قم بتهيئة وحدة AsposePdf. استلم الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. قم بتحسين ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، فإن نتيجة العملية تُحفظ في "ResultOptimize.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي تظهر خطأ في ملفك، فسيتم احتواء معلومات الخطأ في 'json.errorText'.

```js
  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /* تحسين ملف PDF وحفظ "ResultOptimize.pdf" */
  const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
  console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```