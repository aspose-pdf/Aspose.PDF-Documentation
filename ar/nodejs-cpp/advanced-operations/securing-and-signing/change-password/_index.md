---
title: تغيير كلمة مرور ملف PDF في Node.js
linktitle: تغيير كلمة المرور
type: docs
weight: 50
url: /ar/nodejs-cpp/change-password-pdf/
description: تغيير كلمة مرور ملف PDF باستخدام Aspose.PDF for Node.js via C++.
lastmod: "2026-07-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## تغيير كلمة مرور ملف PDF

في حالة رغبتك في تغيير كلمة مرور PDF، يمكنك استخدام [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/) دالة. تقوم بتغيير كلمة مرور المستخدم وكلمة مرور المالك باستخدام كلمة مرور المالك، مع الحفاظ على إعدادات الأمان الأصلية.
إذا أردت تغيير كلمة مرور ملف PDF من "owner" إلى "newowner" أو "newuser" جرّب مقتطف الشيفرة التالي:

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` الوحدة كـ `AsposePdf` متغيّر.
1. حدّد اسم ملف PDF الذي سيغيّر كلمة المرور.
1. اتصال `AsposePdf` كـ Promise و تنفيذ العملية لتغيير كلمة المرور. استقبل الكائن إذا تم بنجاح.
1. استدع الدالة [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. تغيير كلمة المرور. تم تعيين كلمة مرور المالك الحالية إلى "owner," وتم تغييرها إلى "newowner" مع كلمة مرور المستخدم الجديدة "newuser".
1. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfChangePassword.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي ظهر خطأ في ملفك، ستحتوي معلومات الخطأ على 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Change passwords of the PDF-file from "owner" to "newowner" and save the "ResultPdfChangePassword.pdf"*/
      const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
      console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

يرجى ملاحظة أنه إذا كانت كلمة المرور سلسلة فارغة:

1. إذا كانت كلمة مرور المستخدم فارغة - يفتح PDF دون طلب كلمة مرور (ولكن لا يزال مشفرًا).
1. إذا كانت كلمة مرور المالك فارغة، يفتح ملف PDF بطلب لكلمة مرور المستخدم.
1. إذا كان كلاهما فارغًا  - يفتح ملف PDF دون طلب كلمة مرور (لكن لا يزال مشفرًا).


**ECMAScript/ES6:**

1. استيراد ال `asposepdfnodejs` وحدة.
1. حدّد اسم ملف PDF الذي سيغيّر كلمة المرور.
1. قم بتهيئة وحدة AsposePdf. استقبل الكائن إذا نجحت.
1. استدع الدالة [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. تغيير كلمة المرور. تم تعيين كلمة مرور المالك الحالية إلى "owner," وتم تغييرها إلى "newowner" مع كلمة مرور المستخدم الجديدة "newuser".
1. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfChangePassword.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي ظهر خطأ في ملفك، ستحتوي معلومات الخطأ على 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Change passwords of the PDF-file from "owner" to "newowner" and save the "ResultPdfChangePassword.pdf"*/
  const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
  console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```