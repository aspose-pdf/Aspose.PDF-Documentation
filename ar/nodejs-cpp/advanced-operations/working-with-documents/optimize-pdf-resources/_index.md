---
title: تحسين موارد ملفات PDF في Node.js
linktitle: تحسين موارد PDF
type: docs
weight: 15
url: /ar/nodejs-cpp/optimize-pdf-resources/
description: تحسين موارد ملفات PDF لعرض الويب السريع باستخدام أداة Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## تحسين موارد PDF

تحسين الموارد في المستند:

1. تتم إزالة الموارد غير المستخدمة في صفحات المستند
1. يتم دمج الموارد المتساوية في كائن واحد
1. يتم حذف الكائنات غير المستخدمة

في حالة رغبتك في تحسين موارد PDF، يمكنك استخدام وظيفة [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/). 
يرجى التحقق من مقتطف الشيفرة التالي من أجل تحسين موارد PDF في بيئة Node.js.

**CommonJS:**

1. قم باستدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
1. حدد اسم ملف PDF الذي سيتم تحسين موارده.

1. استدعاء `AsposePdf` كـ Promise وتنفيذ العملية لتحسين الملف. استلام الكائن إذا نجحت العملية.
1. استدعاء الدالة [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. تحسين موارد PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfOptimizeResource.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وبناءً عليه، يظهر خطأ في ملفك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /* تحسين موارد ملف PDF وحفظ "ResultPdfOptimizeResource.pdf" */
      const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
      console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي سيتم تحسين موارده.
1. تهيئة وحدة AsposePdf. استلم الكائن إذا نجحت العملية.
1. استدعاء الدالة [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. تحسين موارد PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfOptimizeResource.pdf". إذا لم يكن معامل json.errorCode يساوي 0 وظهرت خطأ في ملفك، ستحتوي معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*تحسين موارد ملف PDF وحفظ "ResultPdfOptimizeResource.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
  console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```
```