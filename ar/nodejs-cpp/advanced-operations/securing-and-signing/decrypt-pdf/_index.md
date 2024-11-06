---
title: Decrypt PDF in Node.js
linktitle: Decrypt PDF File
type: docs
weight: 40
url: ar/nodejs-cpp/decrypt-pdf/
description: فك تشفير ملف PDF باستخدام Aspose.PDF لـ Node.js عبر C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## فك تشفير ملف PDF باستخدام كلمة مرور المالك

مؤخراً، يقوم المزيد والمزيد من المستخدمين بتبادل المستندات المشفرة من أجل عدم الوقوع ضحايا للاحتيال عبر الإنترنت وحماية مستنداتهم. في هذا الصدد، يصبح من الضروري الوصول إلى ملف PDF المشفر، حيث يمكن الحصول على هذا الوصول فقط من قبل مستخدم معتمد. أيضاً، يبحث الناس عن حلول مختلفة لفك تشفير ملفات PDF.

في حال كنت ترغب في فك تشفير ملف PDF، يمكنك استخدام وظيفة [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/). إذا كنت ترغب في فك تشفير ملف PDF جرب الكود التالي:

**CommonJS:**

1. قم باستدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
1. حدد اسم ملف PDF الذي سيتم تغيير فك تشفيره.

1. استدعاء `AsposePdf` كوعد وتنفيذ العملية لفك تشفير الملف. استقبال الكائن إذا كانت العملية ناجحة.
1. استدعاء وظيفة [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/).
1. فك تشفير ملف PDF بكلمة المرور "owner".
1. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultDecrypt.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وبناءً على ذلك، يظهر خطأ في ملفك، فسيتم تضمين معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*فك تشفير ملف PDF بكلمة المرور "owner" وحفظ "ResultDecrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
      console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي سيتم تغيير فك تشفيره.
1. تهيئة وحدة AsposePdf. استلم الكائن إذا نجحت العملية.
1. استدعاء وظيفة [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/).
1. فك تشفير ملف PDF بكلمة المرور "owner".
1. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultDecrypt.pdf". إذا لم يكن معلم json.errorCode يساوي 0 وظهرت خطأ في ملفك، سيتم تضمين معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*فك تشفير ملف PDF بكلمة المرور "owner" وحفظ "ResultDecrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
  console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```