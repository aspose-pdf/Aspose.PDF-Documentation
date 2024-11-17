---
title: تحويل PDF إلى Excel في Node.js
linktitle: تحويل PDF إلى Excel
type: docs
weight: 20
url: /ar/nodejs-cpp/convert-pdf-to-xlsx/
lastmod: "2023-11-16"
description: Aspose.PDF لـ Node.js يسمح لك بتحويل PDF إلى تحويل PDF إلى تنسيق XLSX.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إنشاء جداول بيانات من PDF باستخدام Node.js

يدعم **Aspose.PDF لـ Node.js عبر C++** ميزة تحويل ملفات PDF إلى ملفات Excel.

{{% alert color="success" %}}
**حاول تحويل PDF إلى Excel عبر الإنترنت**

يقدم لك Aspose.PDF لـ Node.js تطبيقًا مجانيًا عبر الإنترنت ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى Excel باستخدام تطبيق مجاني](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## تحويل PDF إلى XLSX

في حال كنت ترغب في تحويل مستند PDF، يمكنك استخدام وظيفة [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
 
يرجى التحقق من الكود المقتطف التالي من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
2. تحديد اسم ملف PDF الذي سيتم تحويله.
3. استدعاء `AsposePdf` كـ Promise وأداء العملية لتحويل الملف. استلام الكائن في حال النجاح.
4. استدعاء الدالة [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
5. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPDFtoXlsX.xlsx". إذا لم يكن معامل json.errorCode يساوي 0، وظهرت خطأ في ملفك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*تحويل ملف PDF إلى XlsX وحفظ "ResultPDFtoXlsX.xlsx"*/
      const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
      console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي سيتم تحويله.
1. تهيئة وحدة AsposePdf. استلم الكائن إذا نجحت العملية.
1. استدعاء الدالة [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPDFtoXlsX.xlsx". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهرت خطأ في ملفك، ستحتوي معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*تحويل ملف PDF إلى XlsX وحفظ "ResultPDFtoXlsX.xlsx"*/
  const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
  console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```