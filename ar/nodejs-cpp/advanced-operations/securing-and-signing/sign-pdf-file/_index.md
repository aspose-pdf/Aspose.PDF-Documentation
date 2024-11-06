---
title: إضافة توقيع رقمي في PDF باستخدام Node.js
linktitle: التوقيع الرقمي لملف PDF
type: docs
weight: 70
url: ar/nodejs-cpp/sign-pdf/
description: توقيع مستندات PDF رقميًا في بيئة Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

التوقيع الرقمي في مستند PDF هو وسيلة للتحقق من صحة المستند وسلامته. هذه هي عملية التوقيع الإلكتروني لمستند PDF باستخدام مفتاح خاص وشهادة رقمية. يضمن هذا التوقيع لحامله أن المستند لم يتم تغييره أو تعديله منذ التوقيع وأن الموقع هو من يوافق عليه. لتوقيع PDF باستخدام Node.js، استخدم أداة Aspose.PDF.

في حال كنت ترغب في توقيع ملف PDF، يمكنك استخدام دالة [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/).

يمكن استخدام **البارامترات** المتعلقة بالتوقيع:

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
- الموقع
- isVisible
- signatureAppearance
- fileNameResult

يستخدم مقتطف الشيفرة هذا وحدة AsposePDFforNode.js في بيئة Node.js لتوقيع ملف PDF رقميًا باستخدام توقيع PKCS7.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
1. حدد اسم ملف PDF المراد توقيعه، وملف مفتاح PKCS7، وملف صورة شكل التوقيع. يمكن وضع الشهادة والصورة في أي مكان على نظام الملفات الخاص بك حيث تقوم بتحميلها لتوقيع PDF.
1. استدعاء `AsposePdf` كـ Promise وتنفيذ العملية لتوقيع الملف. استلم الكائن إذا كانت العملية ناجحة.
1. استدعاء وظيفة [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/).
1. قم بتوقيع ملف PDF بتوقيعات رقمية. المعلمات المتعلقة بالتوقيع (مثل ملف المفتاح، كلمة المرور، الإحداثيات، السبب، الاتصال، الموقع، إلخ).

1. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultSignPKCS7.pdf". إذا لم يكن معامل json.errorCode يساوي 0 وظهرت بالتالي خطأ في ملفك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*ملف PKCS7*/
      const test_pfx_file = 'test.pfx';
      /*مظهر التوقيع*/
      const sign_img_file = 'Aspose.jpg';
      /*توقيع ملف PDF بالتوقيعات الرقمية وحفظه في "ResultSignPKCS7.pdf"*/
      const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
      console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.

1. حدد اسم ملف PDF المراد توقيعه، وملف المفتاح PKCS7، وملف صورة مظهر التوقيع.
1. قم بتهيئة وحدة AsposePdf. احصل على الكائن إذا نجحت العملية.
1. استدع دالة [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/).
1. قم بتوقيع ملف PDF بتوقيعات رقمية. المعلمات المتعلقة بالتوقيع (مثل ملف المفتاح، كلمة المرور، الإحداثيات، السبب، جهة الاتصال، الموقع، إلخ).
1. بالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultSignPKCS7.pdf". إذا كانت قيمة json.errorCode لا تساوي 0، وظهر خطأ في ملفك، فإن معلومات الخطأ ستكون موجودة في 'json.errorText'.

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