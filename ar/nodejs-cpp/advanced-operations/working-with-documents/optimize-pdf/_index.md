---
title: تحسين PDF باستخدام Aspose.PDF for Node.js عبر C++
linktitle: تحسين ملف PDF
type: docs
weight: 10
url: /ar/nodejs-cpp/optimize-pdf/
description: تحسين وضغط ملفات PDF لعرض سريع على الويب باستخدام بيئة Node.js.
lastmod: "2026-07-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## تحسين مستند PDF

تتيح لك مجموعة الأدوات من Aspose.PDF for Node.js عبر C++ تحسين محتوى PDF لبيئة Node.js. 

يشير التحسين، أو التخطيط الخطي، إلى عملية جعل ملف PDF مناسبًا للتصفح عبر الإنترنت باستخدام متصفح ويب.

في حال رغبتك في تحسين PDF، يمكنك استخدام [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/) دالة. 
يرجى مراجعة مقتطف الشيفرة التالي من أجل تحسين ملفات PDF في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` وحدة ك `AsposePdf` متغيّر.
1. حدد اسم ملف PDF الذي سيتم تحسينه.
1. اتصال `AsposePdf` كـ Promise وتنفيذ العملية لتحسين الملف. استلم الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. حسّن ملف PDF. وبالتالي، إذا كان ‘json.errorCode’ يساوي 0، يتم حفظ نتيجة العملية في “ResultOptimize.pdf”. إذا كان معامل json.errorCode ليس 0 وبالتالي ظهر خطأ في ملفك، فإن معلومات الخطأ ستكون موجودة في ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Optimize a PDF-file and save the "ResultOptimize.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
      console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` وحدة.
1. حدد اسم ملف PDF الذي سيتم تحسينه.
1. تهيئة وحدة AsposePdf. استلام الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. حسّن ملف PDF. وبالتالي، إذا كان ‘json.errorCode’ يساوي 0، يتم حفظ نتيجة العملية في “ResultOptimize.pdf”. إذا كان معامل json.errorCode ليس 0 وبالتالي ظهر خطأ في ملفك، فإن معلومات الخطأ ستكون موجودة في ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Optimize a PDF-file and save the "ResultOptimize.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
  console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```