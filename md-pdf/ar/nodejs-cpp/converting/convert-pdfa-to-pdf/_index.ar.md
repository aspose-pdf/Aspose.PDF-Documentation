---
title: تحويل PDF/A إلى تنسيق PDF في Node.js
linktitle: تحويل PDF/A إلى تنسيق PDF
type: docs
weight: 110
url: /nodejs-cpp/convert-pdfa-to-pdf/
lastmod: "2023-11-16"
description: يوضح هذا الموضوع كيف يسمح لك Aspose.PDF بتحويل ملف PDF/A إلى مستند PDF في بيئة Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## تحويل PDF/A إلى تنسيق PDF

في حال كنت ترغب في تحويل مستند PDF، يمكنك استخدام وظيفة [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
يرجى التحقق من مقتطف الشيفرة التالي من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
2. تحديد اسم ملف PDF الذي سيتم تحويله.
3. استدعاء `AsposePdf` كـ Promise وإجراء العملية لتحويل الملف. استلام الكائن إذا كانت العملية ناجحة.

1. استدعاء الدالة [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. تحويل ملف PDF. وبذلك، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultConvertToPDF.pdf". إذا كانت قيمة parameter json.errorCode ليست 0 وبالتالي يظهر خطأ في ملفك، سيتم تضمين معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*تحويل ملف PDF/A إلى PDF وحفظ "ResultConvertToPDF.pdf"*/
      const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
      console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF/A الذي سيتم تحويله.

1. تهيئة وحدة AsposePdf. استلم الكائن إذا كانت العملية ناجحة.
1. استدعاء الدالة [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. تحويل ملف PDF. لذلك، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultConvertToPDF.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وظهر خطأ في ملفك، ستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  /*تحويل ملف PDF/A إلى PDF وحفظه في "ResultConvertToPDF.pdf"*/
  const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
  console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```