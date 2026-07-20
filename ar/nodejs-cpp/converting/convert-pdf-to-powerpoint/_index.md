---
title: تحويل PDF إلى PPTX في Node.js
linktitle: تحويل PDF إلى PowerPoint
type: docs
weight: 30
url: /ar/nodejs-cpp/convert-pdf-to-powerpoint/
lastmod: "2026-07-16"
description: يتيح لك Aspose.PDF تحويل PDF إلى تنسيق PPTX باستخدام Node.js مباشرةً في بيئة Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

{{% alert color="success" %}}
**جرب تحويل PDF إلى PowerPoint عبر الإنترنت**

يقدم لك Aspose.PDF for Node.js تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), حيث يمكنك محاولة استكشاف الوظيفة والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى PPTX باستخدام تطبيق مجاني](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## تحويل PDF إلى PPTX

في حال رغبتك في تحويل مستند PDF، يمكنك استخدام [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/) دالة. 
يرجى التحقق من مقتطف الشيفرة التالي من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` الوحدة كـ `AsposePdf` متغير.
1. حدد اسم ملف PDF الذي سيتم تحويله.
1. اتصال `AsposePdf` كـ Promise وقم بأداء العملية لتحويل الملف. استلم الكائن إذا نجحت.
1. استدعِ الدالة [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/).
1. حوّل ملف PDF. وبالتالي، إذا كان ‘json.errorCode’ يساوي 0، يتم حفظ نتيجة العملية في “ResultPDFtoPptX.pptx”. إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to PptX and save the "ResultPDFtoPptX.pptx"*/
      const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
      console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` وحدة.
1. حدد اسم ملف PDF الذي سيتم تحويله
1. قم بتهيئة وحدة AsposePdf. استلم الكائن إذا نجحت العملية.
1. استدعِ الدالة [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/).
1. حوّل ملف PDF. وبالتالي، إذا كان ‘json.errorCode’ يساوي 0، يتم حفظ نتيجة العملية في “ResultPDFtoPptX.pptx”. إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to PptX and save the "ResultPDFtoPptX.pptx"*/
  const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
  console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```