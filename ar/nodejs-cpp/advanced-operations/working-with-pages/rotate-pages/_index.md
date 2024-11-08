---
title: تدوير صفحات PDF في Node.js
linktitle: تدوير صفحات PDF
type: docs
weight: 50
url: /ar/nodejs-cpp/rotate-pages/
description: يصف هذا الموضوع كيفية تدوير اتجاه الصفحة في ملف PDF موجود برمجيًا في بيئة Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

يصف هذا القسم كيفية تدوير الصفحات في ملف PDF موجود باستخدام Aspose.PDF لـ Node.js عبر C++.

في حال كنت ترغب في تدوير صفحات PDF، يمكنك استخدام وظيفة [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). تستخدم هذه الوظيفة معلمة خاصة 'AsposePdfModule.Rotation' لقيمة التدوير، والتي يمكنك من خلالها تحديد عدد الدرجات التي تحتاج إلى تدوير PDF. هناك خيارات: لا شيء، 90، 180، أو 270 درجة.

يرجى التحقق من المقتطف الشفري التالي لتدوير صفحات PDF في بيئة Node.js.

**CommonJS:**

1. قم باستدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.

1. حدد اسم ملف PDF لتدويره.
1. استدعاء `AsposePdf` كوعود وتنفيذ عملية تدوير الصفحات. استلم الكائن إذا نجح.
1. استدعاء الدالة [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/).
1. قم بتدوير جميع ملفات PDF. يتم ضبط الدوران إلى 270 درجة (on270). وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultRotation.pdf". إذا كان معامل json.errorCode ليس 0 وبالنتيجة ظهرت خطأ في ملفك، ستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*تدوير صفحات PDF وحفظ "ResultRotation.pdf"*/
      const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
      console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF لتدويره.
1. تهيئة وحدة AsposePdf. استقبال الكائن إذا تم بنجاح.
1. استدعاء الدالة [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/).
1. تدوير جميع ملفات PDF. يتم ضبط التدوير على 270 درجة (on270). وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultRotation.pdf". إذا لم يكن معامل json.errorCode يساوي 0 ونتيجة لذلك، تظهر خطأ في الملف الخاص بك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /* تدوير صفحات PDF وحفظ "ResultRotation.pdf" */
  const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
  console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```