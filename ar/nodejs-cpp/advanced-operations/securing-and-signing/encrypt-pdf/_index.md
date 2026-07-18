---
title:  تشفير PDF في Node.js
linktitle: تشفير ملف PDF
type: docs
weight: 50
url: /ar/nodejs-cpp/encrypt-pdf/
description: تشفير ملف PDF باستخدام Aspose.PDF for Node.js عبر C++.
lastmod: "2026-07-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## تشفير ملف PDF باستخدام كلمة مرور المستخدم أو المالك

إذا كنت تُرسل بريدًا إلكترونيًا إلى شخص ما يحتوي على مرفق PDF يحمل معلومات سرية، قد ترغب في إضافة بعض الأمان إليه أولاً لمنع سقوطه في الأيدي الخاطئة. أفضل طريقة للحد من الوصول غير المصرح به إلى مستند PDF هي حمايته بكلمة مرور. لتشفير المستندات بسهولة وبأمان، يمكنك استخدام Aspose.PDF for Node.js عبر C++.

>يرجى تحديد كلمات مرور مختلفة للمستخدم والمالك أثناء تشفير ملف PDF.

- **كلمة مرور المستخدم**، إذا تم تعيينها، هي ما تحتاج إلى تقديمه لفتح ملف PDF. سيطلب Acrobat/Reader من المستخدم إدخال كلمة مرور المستخدم. إذا لم تكن صحيحة، لن يتم فتح المستند.
- **كلمة مرور المالك**، إذا تم تعيينها، تتحكم في الصلاحيات، مثل الطباعة، التحرير، الاستخراج، التعليق، إلخ. سيمنع Acrobat/Reader هذه الأمور بناءً على إعدادات الصلاحيات. سيطلب Acrobat هذه كلمة المرور إذا أردت تعيين/تغيير الصلاحيات.

في حال رغبتك في تشفير ملف PDF، يمكنك استخدام [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) دالة. 
إذا أردت تشفير ملف PDF، جرّب مقتطف الشيفرة التالي:

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` الوحدة كـ `AsposePdf` متغيّر.
1. حدِّد اسم ملف الـ PDF الذي سيتم تشفيره.
1. اتصال `AsposePdf` كـ Promise وتنفيذ العملية لتشفير الملف. استلم الكائن إذا كان ناجحًا.
1. استدعِ الـ [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) دالة. 
1. قم بتشفير ملف PDF باستخدام كلمتي المرور “user” و “owner”.
1. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultEncrypt.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي ظهر خطأ في ملفك، فإن معلومات الخطأ ستكون موجودة في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Encrypt a PDF-file with passwords "user" and "owner", and save the "ResultEncrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

هناك مختلفة [أذونات التشفير](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#acbb404dc8d3b328891faa5fba341ce0c):

- Module.Permissions.PrintDocument
- Module.Permissions.ModifyContent
- الوحدة.الأذونات.استخراج المحتوى
- الوحدة.الأذونات.تعديل تعليقات النص
- الوحدة.الأذونات.ملء النموذج
- الوحدة.الأذونات.استخراج المحتوى مع الإعاقات
- الوحدة.الأذونات.تجميع المستند
- الوحدة.الأذونات.جودة الطباعة

هناك عدة [خوارزميات التشفير](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ae15d4d8afe86aae14972a6e493d19f66):

- Module.CryptoAlgorithm.RC4x40
- Module.CryptoAlgorithm.RC4x128
- Module.CryptoAlgorithm.AESx128
- Module.CryptoAlgorithm.AESx256

**ECMAScript/ES6:**

1. استيراد `asposepdfnodejs` وحدة.
1. حدد اسم ملف PDF الذي سيغير التشفير.
1. ابدأ وحدة AsposePdf. استلم الكائن إذا نجح.
1. استدعِ الـ [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) دالة. 
1. فك تشفير ملف PDF باستخدام كلمتي المرور "user" و "owner".
1. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultEncrypt.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي ظهر خطأ في ملفك، فإن معلومات الخطأ ستكون موجودة في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Encrypt a PDF-file with passwords "user" and "owner", and save the "ResultEncrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
  console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```