---
title: إضافة خلفية إلى PDF في Node.js
linktitle: إضافة خلفية
type: docs
weight: 10
url: /ar/nodejs-cpp/add-background/
description: إضافة صورة خلفية إلى ملف PDF الخاص بك في Node.js
lastmod: "2026-07-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

تُظهر مقاطع الكود التالية كيفية إضافة صورة خلفية إلى صفحات PDF باستخدام [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/) دالة في Node.js.

يرجى التحقق من مقتطف الكود التالي لإضافة صورة خلفية في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` وحدة كـ `AsposePdf` متغير.
1. حدّد اسم ملف الـ PDF الذي ستتم إضافة صورة الخلفية إليه.
1. اتصال `AsposePdf` كـ Promise وقم بأداء العملية لإضافة صورة خلفية. استلم الكائن إذا نجحت العملية.
1. استدعِ الدالة [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/).
1. أضف صورة خلفية إلى ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultAddBackgroundImage.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add background image to a PDF-file and save the "ResultBackgroundImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
      console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد `asposepdfnodejs` وحدة.
1. حدّد اسم ملف الـ PDF الذي ستتم إضافة صورة الخلفية إليه.
1. تَهيئة وحدة AsposePdf. احصل على الكائن إذا نجح العملية.
1. استدعِ الدالة [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/).
1. أضف صورة خلفية إلى ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultAddBackgroundImage.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  /*Add background image to a PDF-file and save the "ResultBackgroundImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
  console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```