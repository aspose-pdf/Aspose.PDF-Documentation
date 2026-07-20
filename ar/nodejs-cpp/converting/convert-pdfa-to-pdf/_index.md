---
title: تحويل PDF/A إلى تنسيق PDF في Node.js
linktitle: تحويل PDF/A إلى تنسيق PDF
type: docs
weight: 110
url: /ar/nodejs-cpp/convert-pdfa-to-pdf/
lastmod: "2026-07-16"
description: هذا الموضوع يوضح لك كيف يسمح Aspose.PDF بتحويل ملف PDF/A إلى مستند PDF في بيئة Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## تحويل PDF/A إلى تنسيق PDF

في حال رغبتك في تحويل مستند PDF، يمكنك استخدام [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/) دالة. 
يرجى فحص مقطع الكود التالي لتحويله في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` الوحدة ك `AsposePdf` متغير.
1. حدد اسم ملف PDF الذي سيتم تحويله.
1. اتصال `AsposePdf` كـ Promise وتنفيذ العملية لتحويل الملف. استقبل الكائن إذا نجح.
1. استدعي الدالة [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultConvertToPDF.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي ظهر خطأ في ملفك، فإن معلومات الخطأ ستكون موجودة في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF/A-file to PDF and save the "ResultConvertToPDF.pdf"*/
      const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
      console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد `asposepdfnodejs` وحدة.
1. حدّد اسم ملف PDF/A الذي سيتم تحويله
1. تهيئة وحدة AsposePdf. استلم الكائن إذا نجح.
1. استدعي الدالة [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultConvertToPDF.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي ظهر خطأ في ملفك، فإن معلومات الخطأ ستكون موجودة في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  /*Convert a PDF/A-file to PDF and save the "ResultConvertToPDF.pdf"*/
  const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
  console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```