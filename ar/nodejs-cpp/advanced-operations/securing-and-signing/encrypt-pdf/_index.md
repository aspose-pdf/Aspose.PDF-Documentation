---
title: تشفير ملف PDF في Node.js
linktitle: تشفير ملف PDF
type: docs
weight: 50
url: /ar/nodejs-cpp/encrypt-pdf/
description: تشفير ملف PDF باستخدام Aspose.PDF لـ Node.js عبر C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## تشفير ملف PDF باستخدام كلمة مرور المستخدم أو المالك

إذا كنت ترسل بريدًا إلكترونيًا إلى شخص ما يحتوي على مرفق PDF يتضمن معلومات سرية، فقد ترغب في إضافة بعض الحماية إليه أولًا لمنعه من الوقوع في الأيدي الخطأ. أفضل طريقة لتقييد الوصول غير المصرح به إلى مستند PDF هي حمايته بكلمة مرور. لتشفير المستندات بسهولة وأمان، يمكنك استخدام Aspose.PDF لـ Node.js عبر C++.

>يرجى تحديد كلمات مرور مختلفة للمستخدم والمالك أثناء تشفير ملف PDF.

- **كلمة مرور المستخدم**، إذا تم تعيينها، هي ما تحتاج إلى تقديمه لفتح ملف PDF. سيطلب Acrobat/Reader من المستخدم إدخال كلمة مرور المستخدم. إذا لم تكن صحيحة، فلن يفتح المستند.
- **كلمة مرور المالك**، إذا تم تعيينها، تتحكم في الأذونات، مثل الطباعة، التحرير، الاستخراج، التعليق، إلخ.
 Acrobat/Reader سيمنع هذه الأشياء بناءً على إعدادات الأذونات. سوف يتطلب Acrobat هذا الرمز السري إذا كنت ترغب في تحديد/تغيير الأذونات.

في حالة رغبتك في تشفير ملف PDF، يمكنك استخدام دالة [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/). إذا كنت ترغب في تشفير ملف PDF جرب نموذج الشفرة التالي:

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
2. تحديد اسم ملف PDF الذي سيتم تشفيره.
3. استدعاء `AsposePdf` كـ Promise وتنفيذ العملية لتشفير الملف. استلم الكائن إذا نجحت العملية.
4. استدعاء دالة [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/).
5. تشفير ملف PDF بكلمات المرور "user" و"owner".
1. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultEncrypt.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وظهرت بالتالي خطأ في ملفك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*تشفير ملف PDF بكلمات مرور "user" و "owner"، وحفظ "ResultEncrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

هناك [أذونات تشفير](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#acbb404dc8d3b328891faa5fba341ce0c) مختلفة:

- Module.Permissions.PrintDocument
- Module.Permissions.ModifyContent
- Module.Permissions.ExtractContent

- Module.Permissions.ModifyTextAnnotations
- Module.Permissions.FillForm
- Module.Permissions.ExtractContentWithDisabilities
- Module.Permissions.AssembleDocument
- Module.Permissions.PrintingQuality

هناك [خوارزميات تشفير](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ae15d4d8afe86aae14972a6e493d19f66) مختلفة:

- Module.CryptoAlgorithm.RC4x40
- Module.CryptoAlgorithm.RC4x128
- Module.CryptoAlgorithm.AESx128
- Module.CryptoAlgorithm.AESx256

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. حدد اسم ملف PDF الذي سيغير المشفر.
1. قم بتهيئة وحدة AsposePdf. استلم الكائن إذا نجحت.
1. استدعاء دالة [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/).
1. فك تشفير ملف PDF باستخدام كلمات المرور "user" و "owner".

1. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultEncrypt.pdf". إذا كان معامل json.errorCode لا يساوي 0، وبالتالي، تظهر خطأ في ملفك، ستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /* تشفير ملف PDF بكلمات مرور "user" و"owner"، وحفظه في "ResultEncrypt.pdf" */
  const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
  console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```