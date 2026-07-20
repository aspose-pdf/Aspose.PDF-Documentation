---
title: تحويل PDF إلى Excel في Node.js
linktitle: تحويل PDF إلى Excel
type: docs
weight: 20
url: /ar/nodejs-cpp/convert-pdf-to-xlsx/
lastmod: "2026-07-16"
description: تتيح لك Aspose.PDF for Node.js تحويل PDF إلى تنسيق XLSX.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إنشاء جداول بيانات من PDF باستخدام Node.js 

**Aspose.PDF for Node.js via C++** تدعم ميزة تحويل ملفات PDF إلى ملف Excel.

{{% alert color="success" %}}
**حاول تحويل PDF إلى Excel عبر الإنترنت**

Aspose.PDF for Node.js يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), حيث يمكنك تجربة استكشاف الوظيفة والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى Excel مع تطبيق مجاني](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## تحويل PDF إلى XLSX

في حال رغبتك في تحويل مستند PDF، يمكنك استخدام [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/) دالة. 
يرجى مراجعة المقتطف البرمجي التالي من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` وحدة ك `AsposePdf` متغير.
1. حدد اسم ملف الـ PDF الذي سيتم تحويله.
1. اتصال `AsposePdf` كـ Promise وتنفيذ العملية لتحويل الملف. استلام الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. حوّل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPDFtoXlsX.xlsx". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to XlsX and save the "ResultPDFtoXlsX.xlsx"*/
      const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
      console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` الوحدة.
1. حدد اسم ملف الـ PDF الذي سيتم تحويله.
1. قم بتهيئة وحدة AsposePdf. استلم الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. حوّل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPDFtoXlsX.xlsx". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to XlsX and save the "ResultPDFtoXlsX.xlsx"*/
  const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
  console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

