---
title: إضافة طوابع الصور إلى PDF في Node.js
linktitle: طوابع الصور في ملف PDF
type: docs
weight: 60
url: ar/nodejs-cpp/stamping/
description: أضف ختم الصورة إلى مستند PDF الخاص بك باستخدام AsposePdfAddStamp مع أداة Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إضافة ختم الصورة في ملف PDF

يشبه ختم مستند PDF ختم مستند ورقي. يوفر الختم في ملف PDF معلومات إضافية لملف PDF، مثل حماية ملف PDF لاستخدام الآخرين وتأكيد أمان محتويات ملف PDF.
يمكنك استخدام وظيفة [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/) لإضافة ختم صورة إلى ملف PDF باستخدام Node.js.

يرجى التحقق من نموذج الكود التالي لإضافة ختم صورة إلى ملف PDF في بيئة Node.js.

**CommonJS:**

1. استدعي `require` واستورد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.

1. حدد اسم ملف PDF الذي سيتم إضافة ختم الصورة إليه.
1. استدعِ `AsposePdf` كـ Promise وقم بإجراء العملية لإضافة ختم الصورة. استلم الكائن في حال النجاح.
1. استدعِ الدالة [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. أضف الختم إلى ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultImage.pdf". إذا كان معامل json.errorCode لا يساوي 0 وظهر خطأ في ملفك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*أضف الختم إلى ملف PDF واحفظ "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
      console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
2. تحديد اسم ملف PDF الذي سيتم إضافة ختم الصورة فيه.
3. تهيئة وحدة AsposePdf. استلام الكائن إذا تم بنجاح.
4. استدعاء الدالة [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
5. إضافة ختم إلى ملف PDF. وبالتالي، إذا كان 'json.errorCode' هو 0، يتم حفظ نتيجة العملية في "ResultImage.pdf". إذا لم يكن معامل json.errorCode هو 0، وبناءً على ذلك، يظهر خطأ في ملفك، فسيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  /*إضافة ختم إلى ملف PDF وحفظ "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
  console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```