---
title: إضافة خلفية إلى PDF في Node.js
linktitle: إضافة خلفية
type: docs
weight: 10
url: /nodejs-cpp/add-background/
description: إضافة صورة خلفية إلى ملف PDF الخاص بك في Node.js 
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

يعرض مقتطفات الشيفرة التالية كيفية إضافة صورة خلفية إلى صفحات PDF باستخدام وظيفة [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/) في Node.js.

يرجى مراجعة مقتطف الشيفرة التالي من أجل إضافة صورة خلفية في بيئة Node.js.

**CommonJS:**

1. قم باستدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
2. حدد اسم ملف PDF الذي ستتم إضافة صورة الخلفية إليه.
3. استدعاء `AsposePdf` كـ Promise وتنفيذ العملية لإضافة صورة الخلفية. استلم الكائن إذا نجحت العملية.
4. استدعاء الوظيفة [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/).

1. إضافة صورة خلفية إلى ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultAddBackgroundImage.pdf". إذا لم يكن معامل json.errorCode يساوي 0 وظهرت بالتالي خطأ في ملفك، ستحتوي معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*إضافة صورة خلفية إلى ملف PDF وحفظ "ResultBackgroundImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
      console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي ستتم إضافة الصورة الخلفية إليه.
1. تهيئة وحدة AsposePdf. استلام الكائن إذا تم بنجاح.

1. استدعِ الدالة [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/).
2. أضف صورة خلفية إلى ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، فإن نتيجة العملية تُحفظ في "ResultAddBackgroundImage.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي ظهرت خطأ في ملفك، فإن معلومات الخطأ ستوجد في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  /*إضافة صورة خلفية إلى ملف PDF وحفظ "ResultBackgroundImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
  console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```