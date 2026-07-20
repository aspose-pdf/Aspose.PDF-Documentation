---
title: تحسين موارد PDF في Node.js
linktitle: تحسين موارد PDF
type: docs
weight: 15
url: /ar/nodejs-cpp/optimize-pdf-resources/
description: تحسين موارد ملفات PDF لعرض ويب سريع باستخدام أداة Node.js.
lastmod: "2026-07-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## تحسين موارد PDF

تحسين الموارد في المستند:

1. يتم إزالة الموارد التي لا تُستخدم في صفحات المستند
1. يتم دمج الموارد المتساوية في كائن واحد
1. يتم حذف الكائنات غير المستخدمة
 

في حال رغبتك في تحسين موارد PDF، يمكنك استخدام [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/) function. 
الرجاء مراجعة مقتطف الشيفرة التالي من أجل تحسين موارد PDF في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` وحدة كـ `AsposePdf` متغيّر.
1. حدّد اسم ملف PDF الذي سيتم تحسين موارده.
1. اتصال `AsposePdf` كـ Promise وقم بتنفيذ العملية لتحسين الملف. استلم الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. قم بتحسين موارد PDF. وبالتالي، إذا كان ‘json.errorCode’ يساوي 0، يُحفظ نتيجة العملية في “ResultPdfOptimizeResource.pdf”. إذا كانت قيمة json.errorCode ليست 0 وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Optimize resources of PDF-file and save the "ResultPdfOptimizeResource.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
      console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` الوحدة.
1. حدّد اسم ملف PDF الذي سيتم تحسين موارده.
1. قم بتهيئة وحدة AsposePdf. استلم الكائن إذا نجحت العملية.
1. استدعِ الدالة [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. قم بتحسين موارد PDF. وبالتالي، إذا كان ‘json.errorCode’ يساوي 0، يُحفظ نتيجة العملية في “ResultPdfOptimizeResource.pdf”. إذا كانت قيمة json.errorCode ليست 0 وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Optimize resources of PDF-file and save the "ResultPdfOptimizeResource.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
  console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```