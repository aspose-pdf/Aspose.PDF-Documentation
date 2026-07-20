---
title: إضافة توقيع رقمي في PDF في Node.js
linktitle: توقيع PDF رقمياً
type: docs
weight: 70
url: /ar/nodejs-cpp/sign-pdf/
description: توقيع مستندات PDF رقمياً في بيئة Node.js.
lastmod: "2026-07-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---


التوقيع الرقمي في مستند PDF هو وسيلة للتحقق من أصالة المستند وسلامته. هذه العملية هي توقيع إلكتروني لمستند PDF باستخدام مفتاح خاص وشهادة رقمية. يضمن هذا التوقيع للمالك أن المستند لم يتغير أو يُعدل منذ التوقيع وأن الموقع هو الشخص الذي يوافق عليه. لتوقيع PDF باستخدام Node.js، استخدم أداة Aspose.PDF.

في حال رغبتك في توقيع ملف PDF، يمكنك استخدام [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) دالة.

من الممكن استخدام **parameters** المتعلقة بالتوقيع:

- fileName
- pageNum
- fileSign
- pswSign
- setXIndent
- setYIndent
- setHeight
- setWidth
- reason
- contact
- location
- isVisible
- signatureAppearance
- fileNameResult 

يستخدم هذا المقتطف من الكود وحدة AsposePDFforNode.js في بيئة Node.js لتوقيع ملف PDF رقمياً باستخدام توقيع PKCS7.

**CommonJS:**

1. اتصل `require` و استيراد `asposepdfnodejs` وحدة كـ `AsposePdf` متغير.
1. حدّد اسم ملف PDF الذي سيُوقّع، ملف مفتاح PKCS7، وملف صورة مظهر التوقيع. يمكن وضع الشهادة والصورة في أي مكان على نظام الملفات الخاص بك حيث تقوم بتحميلها للتوقيع على PDF.
1. اتصل `AsposePdf` كـ Promise ونفّذ العملية لتوقيع الملف. استقبل الكائن إذا كان ناجحًا.
1. استدعِ الـ [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) دالة. 
1. وقّع ملف PDF باستخدام توقيعات رقمية. المعلمات المتعلقة بالتوقيع (مثل ملف المفتاح، كلمة المرور، الإحداثيات، السبب، جهة الاتصال، الموقع، إلخ). 
1. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultSignPKCS7.pdf". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، ستحتوي معلومات الخطأ على 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Key PKCS7*/
      const test_pfx_file = 'test.pfx';
      /*Signature appearance*/
      const sign_img_file = 'Aspose.jpg';
      /*Sign a PDF-file with digital signatures and save the "ResultSignPKCS7.pdf"*/
      const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
      console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد `asposepdfnodejs` وحدة.
1. حدد اسم ملف PDF الذي سيُوقع، وملف مفتاح PKCS7، وملف صورة مظهر التوقيع.
1. تهيئة وحدة AsposePdf. استلم الكائن إذا نجح.
1. استدعِ الـ [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) دالة. 
1. وقّع ملف PDF باستخدام توقيعات رقمية. المعلمات المتعلقة بالتوقيع (مثل ملف المفتاح، كلمة المرور، الإحداثيات، السبب، جهة الاتصال، الموقع، إلخ). 
1. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultSignPKCS7.pdf". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، ستحتوي معلومات الخطأ على 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Key PKCS7*/
  const test_pfx_file = 'test.pfx';
  /*Signature appearance*/
  const sign_img_file = 'Aspose.jpg';
  /*Sign a PDF-file with digital signatures and save the "ResultSignPKCS7.pdf"*/
  const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
  console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```