---
title: فك تشفير PDF في Node.js
linktitle: فك تشفير ملف PDF
type: docs
weight: 40
url: /ar/nodejs-cpp/decrypt-pdf/
description: فك تشفير ملف PDF باستخدام Aspose.PDF for Node.js عبر C++.
lastmod: "2026-07-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## فك تشفير ملف PDF باستخدام كلمة مرور المالك

مؤخرًا، يتبادل المزيد والمزيد من المستخدمين المستندات المشفرة لتجنب الوقوع كضحايا للاحتيال على الإنترنت وحماية مستنداتهم.
في هذا الصدد، يصبح من الضروري الوصول إلى ملف PDF المشفر، حيث لا يمكن الحصول على مثل هذا الوصول إلا من قبل مستخدم مخول. كما يبحث الناس عن حلول مختلفة لفك تشفير ملفات PDF. 

في حالة رغبتك في فك تشفير ملف PDF، يمكنك استخدام [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) دالة. 
إذا كنت تريد فك تشفير ملف PDF جرب مقتطف الشيفرة التالي:

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` الوحدة ك `AsposePdf` متغير.
1. حدد اسم ملف PDF الذي سيغير حالة فك التشفير.
1. اتصال `AsposePdf` كـ Promise وقم بتنفيذ العملية لفك تشفير الملف. استقبل الكائن إذا نجح.
1. استدعِ الـ [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) دالة.
1. فك تشفير ملف PDF باستخدام كلمة المرور "owner".
1. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultDecrypt.pdf". إذا لم يكن معلمة json.errorCode 0، وبالتالي ظهر خطأ في ملفك، فإن معلومات الخطأ ستتضمن في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Decrypt a PDF-file with password is "owner" and save the "ResultDecrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
      console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد `asposepdfnodejs` الوحدة.
1. حدد اسم ملف PDF الذي سيغير حالة فك التشفير.
1. قم بتهيئة وحدة AsposePdf. استلم الكائن إذا نجح.
1. استدعِ الـ [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) دالة.
1. فك تشفير ملف PDF باستخدام كلمة المرور "owner".
1. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultDecrypt.pdf". إذا لم يكن معلمة json.errorCode 0، وبالتالي ظهر خطأ في ملفك، فإن معلومات الخطأ ستتضمن في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Decrypt a PDF-file with password is "owner" and save the "ResultDecrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
  console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```