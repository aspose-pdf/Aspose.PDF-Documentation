---
title: تحويل PDF إلى صيغ PDF/A في Node.js
linktitle: تحويل PDF إلى صيغ PDF/A
type: docs
weight: 100
url: /ar/nodejs-cpp/convert-pdf-to-pdfa/
lastmod: "2026-07-16"
description: توضح لك هذه المقالة كيفية تمكين Aspose.PDF من تحويل ملف PDF إلى ملف PDF متوافق مع PDF/A في بيئة Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Node.js** يتيح لك تحويل ملف PDF إلى <abbr title="Portable Document Format for Archiving of electronic documents">PDF/A</abbr> ملف PDF متوافق. 

{{% alert color="success" %}}
**جرب تحويل PDF إلى PDF/A عبر الإنترنت**

تقدم لك Aspose.PDF for Node.js تطبيقًا مجانيًا على الإنترنت ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), حيث يمكنك تجربة استكشاف الوظيفة والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى PDF/A باستخدام تطبيق مجاني](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## تحويل PDF إلى تنسيق PDF/A

في حال رغبتك في تحويل مستند PDF، يمكنك استخدام [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/) دالة. 
يرجى مراجعة مقتطف الكود التالي من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` وحدة كـ `AsposePdf` متغير.
1. حدد اسم ملف PDF الذي سيُحوَّل.
1. اتصال `AsposePdf` كـ Promise وقم بتنفيذ العملية لتحويل الملف. استقبل الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. إصلاح ملف PDF. وبالتالي، إذا كان ‘json.errorCode’ يساوي 0، يتم حفظ نتيجة العملية في "ResultConvertToPDFA.pdf". خلال عملية التحويل، يتم إجراء التحقق، وتُحفظ نتائج التحقق في "ResultConvertToPDFALog.xml". إذا كانت قيمة معلمة json.errorCode ليست 0 وبالتالي ظهر خطأ في الملف الخاص بك، ستكون معلومات الخطأ موجودة في ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to PDF/A(1A) and save the "ResultConvertToPDFA.pdf"*/
      /*During conversion process, the validation is also performed, "ResultConvertToPDFA.xml"*/
      const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
      console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` وحدة.
1. حدد اسم ملف PDF الذي سيُحوَّل.
1. .تهيئة وحدة AsposePdf. استلم الكائن إذا نجح
1. استدعِ الدالة [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. إصلاح ملف PDF. وبالتالي، إذا كان ‘json.errorCode’ يساوي 0، يتم حفظ نتيجة العملية في "ResultConvertToPDFA.pdf". خلال عملية التحويل، يتم إجراء التحقق، وتُحفظ نتائج التحقق في "ResultConvertToPDFALog.xml". إذا كانت قيمة معلمة json.errorCode ليست 0 وبالتالي ظهر خطأ في الملف الخاص بك، ستكون معلومات الخطأ موجودة في ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to PDF/A(1A) and save the "ResultConvertToPDFA.pdf"*/
  /*During conversion process, the validation is also performed, "ResultConvertToPDFA.xml"*/
  const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
  console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
```





