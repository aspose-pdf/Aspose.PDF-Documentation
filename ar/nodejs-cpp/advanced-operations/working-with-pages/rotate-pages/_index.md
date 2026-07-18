---
title: تدوير صفحات PDF في Node.js
linktitle: تدوير صفحات PDF
type: docs
weight: 50
url: /ar/nodejs-cpp/rotate-pages/
description: يوضح هذا الموضوع كيفية تدوير اتجاه الصفحة في ملف PDF موجود برمجياً في بيئة Node.js.
lastmod: "2026-07-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

يوضح هذا القسم كيفية تدوير الصفحات في ملف PDF موجود باستخدام Aspose.PDF for Node.js via C\u002B\u002B.

في حال رغبتك في تدوير صفحات PDF، يمكنك استخدام [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/) دالة. تستخدم هذه الدالة معاملًا خاصًا 'AsposePdfModule.Rotation' لقيمة الدوران. يمكنك من خلاله تحديد عدد الدرجات التي تحتاج إلى تدوير PDF بها. هناك خيارات: لا شيء، 90، 180، أو 270 درجة.

يرجى مراجعة مقتطف الشيفرة التالي لتدوير صفحات PDF في بيئة Node.js.

**CommonJS:**

1. مكالمة `require` و استيراد `asposepdfnodejs` الوحدة كـ `AsposePdf` متغير.
1. حدد اسم ملف PDF الذي تريد تدويره.
1. مكالمة `AsposePdf` كـ Promise وتنفيذ العملية لتدوير الصفحات. استلام الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). 
1. قم بتدوير جميع ملفات PDF. تم ضبط التدوير على 270 درجة (on270). وبالتالي، إذا كان 'json.errorCode' يساوي 0، تُحفظ نتيجة العملية في "ResultRotation.pdf". إذا لم يكن معلمة json.errorCode هي 0، وبالتالي ظهر خطأ في ملفك، ستحتوي معلومات الخطأ على 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Rotate PDF-pages and save the "ResultRotation.pdf"*/
      const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
      console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` وحدة.
1. حدد اسم ملف PDF الذي تريد تدويره.
1. قم بتهيئة وحدة AsposePdf. استقبل الكائن إذا نجحت العملية.
1. استدعِ الدالة [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). 
1. قم بتدوير جميع ملفات PDF. تم ضبط التدوير على 270 درجة (on270). وبالتالي، إذا كان 'json.errorCode' يساوي 0، تُحفظ نتيجة العملية في "ResultRotation.pdf". إذا لم يكن معلمة json.errorCode هي 0، وبالتالي ظهر خطأ في ملفك، ستحتوي معلومات الخطأ على 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Rotate PDF-pages and save the "ResultRotation.pdf"*/
  const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
  console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```