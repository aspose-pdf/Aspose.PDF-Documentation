---
title: إضافة ترقيم الصفحات إلى PDF في Node.js
linktitle: إضافة رقم الصفحة
type: docs
weight: 100
url: /nodejs-cpp/add-page-number/
description: Aspose.PDF لـ Node.js عبر C++ يتيح لك إضافة ختم رقم الصفحة إلى ملف PDF باستخدام AsposePdfAddPageNum.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

رقم الصفحة يسهل على القارئ تحديد أجزاء مختلفة من المستند. يوضح مقطع الشيفرة التالي كيفية إضافة أرقام الصفحات إلى صفحات PDF باستخدام وظيفة [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/) في Node.js.

يرجى التحقق من مقطع الشيفرة التالي لإضافة أرقام الصفحات إلى PDF في بيئة Node.js.

**CommonJS:**

1. قم باستدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
1. حدد اسم ملف PDF الذي ستتم إضافة أرقام الصفحات إليه.
1. قم باستدعاء `AsposePdf` كـ Promise وأجرِ العملية لإضافة أرقام الصفحات. استلم الكائن إذا كانت العملية ناجحة.

1. استدعاء الدالة [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. إضافة رقم الصفحة إلى ملف PDF. لذلك، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultAddPageNum.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وظهرت بالتالي خطأ في ملفك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*إضافة رقم الصفحة إلى ملف PDF وحفظ "ResultAddPageNum.pdf"*/
      const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
      console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي سيتم إضافة أرقام الصفحات إليه.
1. تهيئة وحدة AsposePdf. استلم الكائن إذا كان ناجحًا.

1. استدعاء الدالة [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. إضافة رقم الصفحة إلى ملف PDF. لذلك، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultAddPageNum.pdf". إذا كانت قيمة باراميتر json.errorCode لا تساوي 0 وبالتالي يظهر خطأ في ملفك، سيتم تضمين معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*إضافة رقم الصفحة إلى ملف PDF وحفظ "ResultAddPageNum.pdf"*/
  const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
  console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```