---
title: تقسيم PDF في Node.js
linktitle: تقسيم ملفات PDF
type: docs
weight: 30
url: /ar/nodejs-cpp/split-pdf/
description: يوضح هذا الموضوع كيفية تقسيم صفحات PDF إلى ملفات PDF فردية باستخدام Aspose.PDF for Node.js via C++.
lastmod: "2026-07-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## تقسيم PDF إلى ملفين باستخدام Node.js

في حال رغبتك في تقسيم PDF واحد إلى أجزاء، يمكنك استخدام [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/) دالة. 
يرجى فحص مقتطف الشيفرة التالي لتقسيم ملفي PDF في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` وحدة كـ `AsposePdf` متغير.
1. حدّد اسم ملفات PDF التي سيتم تقسيمها.
1. اتصال `AsposePdf` كـ Promise وقم بتنفيذ العملية لتقسيم الملف. استقبل الكائن إذا نجحت.
1. استدع الدالة [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
1. قسّم ملفي PDF. يعيّن المتغيّر pageToSplit إلى 1، مما يدل على أن ملف PDF سيتم تقسيمه عند الصفحة 1. 
1. وبالتالي، إذا كان ‘json.errorCode’ يساوي 0، يتم حفظ نتيجة العملية في “ResultSplit1.pdf” و “ResultSplit2.pdf”. إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، ستحتوي معلومات الخطأ على ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set number a page to split*/
      const pageToSplit = 1;
      /*Split to two PDF-files and save the "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد `asposepdfnodejs` وحدة.
1. حدّد اسم ملفات PDF التي سيتم تقسيمها.
1. ابدأ وحدة AsposePdf. استقبل الكائن إذا نجح.
1. استدع الدالة [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
1. قسّم ملفي PDF. يعيّن المتغيّر pageToSplit إلى 1، مما يدل على أن ملف PDF سيتم تقسيمه عند الصفحة 1. 
1. وبالتالي، إذا كان ‘json.errorCode’ يساوي 0، يتم حفظ نتيجة العملية في “ResultSplit1.pdf” و “ResultSplit2.pdf”. إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، ستحتوي معلومات الخطأ على ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set number a page to split*/
  const pageToSplit = 1;
  /*Split to two PDF-files and save the "ResultSplit1.pdf", "ResultSplit2.pdf"*/
  const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
  console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
```