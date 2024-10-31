---
title: تحويل PDF إلى PPTX في Node.js
linktitle: تحويل PDF إلى PowerPoint
type: docs
weight: 30
url: /nodejs-cpp/convert-pdf-to-powerpoint/
lastmod: "2023-11-16"
description: يسمح لك Aspose.PDF بتحويل PDF إلى تنسيق PPTX باستخدام Node.js مباشرة في بيئة Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

{{% alert color="success" %}}
**حاول تحويل PDF إلى PowerPoint عبر الإنترنت**

يقدم لك Aspose.PDF for Node.js تطبيقًا مجانيًا عبر الإنترنت ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى PPTX باستخدام التطبيق المجاني](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## تحويل PDF إلى PPTX

في حال كنت ترغب في تحويل مستند PDF، يمكنك استخدام وظيفة [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/).

يرجى التحقق من مقتطف الشيفرة التالي من أجل التحويل في بيئة Node.js.


**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
1. تحديد اسم ملف PDF الذي سيتم تحويله.
1. استدعاء `AsposePdf` كوعد (Promise) وتنفيذ العملية لتحويل الملف. استلم الكائن إذا كان ناجحًا.
1. استدعاء الدالة [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPDFtoPptX.pptx". إذا كانت قيمة معامل json.errorCode ليست 0 وبالتالي تظهر خطأ في ملفك، فإن معلومات الخطأ ستكون موجودة في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*تحويل ملف PDF إلى PptX وحفظ "ResultPDFtoPptX.pptx"*/
      const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
      console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. حدد اسم ملف PDF الذي سيتم تحويله
1. تهيئة وحدة AsposePdf. استلم الكائن إذا تم بنجاح.
1. استدعاء الدالة [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPDFtoPptX.pptx". إذا كانت قيمة معامل json.errorCode ليست 0 وظهر خطأ في ملفك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*تحويل ملف PDF إلى PptX وحفظه كـ "ResultPDFtoPptX.pptx"*/
  const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
  console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```