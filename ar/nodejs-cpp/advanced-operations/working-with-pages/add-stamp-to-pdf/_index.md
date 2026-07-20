---
title: إضافة طوابع صورة إلى PDF في Node.js
linktitle: طوابع صورة في ملف PDF
type: docs
weight: 60
url: /ar/nodejs-cpp/stamping/
description: أضف طابع الصورة في مستند PDF الخاص بك باستخدام AsposePdfAddStamp مع أداة Node.js.
lastmod: "2026-07-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إضافة طابع صورة إلى ملف PDF

تطبيق طابع على مستند PDF مشابه لتطبيق طابع على مستند ورقي. يضيف طابع في ملف PDF معلومات إضافية إلى ملف PDF، مثل حماية ملف PDF من استخدامها من قبل الآخرين وتأكيد أمان محتويات ملف PDF.
يمكنك استخدام [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/) دالة لإضافة ختم صورة إلى ملف PDF باستخدام Node.js.

يرجى مراجعة مقتطف الشيفرة التالي لإضافة ختم صورة إلى ملف PDF في بيئة Node.js.

**CommonJS:**

1. اتصل `require` و استيراد `asposepdfnodejs` وحدة كـ `AsposePdf` متغير.
1. حدّد اسم ملف PDF الذي سيُضاف إليه ختم الصورة.
1. اتصل `AsposePdf` كـ Promise وتنفيذ العملية لإضافة طابع صورة. استلم الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. أضف طابعًا إلى ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultImage.pdf". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، ستحتوي معلومات الخطأ على 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add stamp to a PDF-file and save the "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
      console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد `asposepdfnodejs` وحدة.
1. حدّد اسم ملف PDF الذي سيُضاف إليه ختم الصورة.
1. ابدأ وحدة AsposePdf. استلم الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. أضف طابعًا إلى ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultImage.pdf". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، ستحتوي معلومات الخطأ على 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  /*Add stamp to a PDF-file and save the "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
  console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```