---
title: تغيير كلمة مرور ملف PDF في Node.js
linktitle: تغيير كلمة المرور
type: docs
weight: 50
url: /nodejs-cpp/change-password-pdf/
description: تغيير كلمة مرور ملف PDF باستخدام Aspose.PDF لـ Node.js عبر C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## تغيير كلمة مرور ملف PDF

في حال كنت ترغب في تغيير كلمة مرور ملف PDF، يمكنك استخدام دالة [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/). تقوم بتغيير كلمة مرور المستخدم وكلمة مرور المالك بكلمة مرور المالك، مع الاحتفاظ بإعدادات الأمان الأصلية. إذا كنت ترغب في تغيير كلمة مرور ملف PDF من "owner" إلى "newowner" أو "newuser"، جرب الكود التالي:

**CommonJS:**

1. استدع `require` واستورد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
2. حدد اسم ملف PDF الذي سيتم تغيير كلمته.
3. استدع `AsposePdf` كـ Promise وقم بتنفيذ العملية لتغيير كلمة المرور. استقبل الكائن إذا نجحت العملية.

1. استدعِ الدالة [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. تغيير كلمة المرور. كلمة مرور المالك الحالية هي "owner"، ويتم تغييرها إلى "newowner" مع كلمة مرور المستخدم الجديدة "newuser".
1. وبالتالي، إذا كانت 'json.errorCode' تساوي 0، يتم حفظ نتيجة العملية في "ResultPdfChangePassword.pdf". إذا كانت قيمة json.errorCode ليست 0 وظهرت بالتالي خطأ في ملفك، فستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*تغيير كلمات المرور لملف PDF من "owner" إلى "newowner" وحفظ "ResultPdfChangePassword.pdf"*/
      const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
      console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


يرجى ملاحظة أنه إذا كانت كلمة المرور سلسلة فارغة:

1. إذا كانت كلمة مرور المستخدم فارغة - يفتح ملف PDF دون طلب كلمة مرور (ولكنه لا يزال مشفرًا).
2. إذا كانت كلمة مرور المالك فارغة، يفتح ملف PDF مع طلب كلمة مرور المستخدم.
3. إذا كانت كلتاهما فارغتين - يفتح ملف PDF دون طلب كلمة مرور (ولكنه لا يزال مشفرًا).

**ECMAScript/ES6:**

1. استيراد الوحدة `asposepdfnodejs`.
2. تحديد اسم ملف PDF الذي سيغير كلمة المرور.
3. تهيئة وحدة AsposePdf. تلقي الكائن في حالة النجاح.
4. استدعاء الدالة [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
5. تغيير كلمة المرور. تم تعيين كلمة مرور المالك الحالية إلى "owner"، وتم تغييرها إلى "newowner" مع كلمة مرور المستخدم الجديدة "newuser".

1. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfChangePassword.pdf". إذا كانت قيمة parameter json.errorCode ليست 0 وظهرت بالتالي خطأ في ملفك، فستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /* تغيير كلمات المرور لملف PDF من "owner" إلى "newowner" وحفظه في "ResultPdfChangePassword.pdf" */
  const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
  console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```