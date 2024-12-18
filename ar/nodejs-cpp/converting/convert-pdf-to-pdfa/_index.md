---
title: تحويل PDF إلى تنسيقات PDF/A في Node.js
linktitle: تحويل PDF إلى تنسيقات PDF/A
type: docs
weight: 100
url: /ar/nodejs-cpp/convert-pdf-to-pdfa/
lastmod: "2023-11-16"
description: يوضح لك هذا الموضوع كيف يسمح Aspose.PDF بتحويل ملف PDF إلى ملف PDF متوافق مع PDF/A في بيئة Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Node.js** يسمح لك بتحويل ملف PDF إلى ملف PDF متوافق مع <abbr title="تنسيق المستندات المحمولة لأرشفة الوثائق الإلكترونية">PDF/A</abbr>.

{{% alert color="success" %}}
**حاول تحويل PDF إلى PDF/A عبر الإنترنت**

يقدم لك Aspose.PDF for Node.js تطبيقًا مجانيًا عبر الإنترنت ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى PDF/A مع تطبيق مجاني](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

## تحويل PDF إلى تنسيق PDF/A

في حالة رغبتك في تحويل مستند PDF، يمكنك استخدام وظيفة [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
 
يرجى التحقق من مقتطف الشيفرة التالي من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
2. تحديد اسم ملف PDF الذي سيتم تحويله.
3. استدعاء `AsposePdf` كـ Promise وتنفيذ العملية لتحويل الملف. استلم الكائن إذا كانت العملية ناجحة.
4. استدعاء الدالة [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
5. إصلاح ملف PDF. بالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultConvertToPDFA.pdf". أثناء عملية التحويل، يتم تنفيذ التحقق، ويتم حفظ نتائج التحقق كـ "ResultConvertToPDFALog.xml". إذا كانت قيمة json.errorCode ليست 0 وظهرت خطأ في ملفك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*تحويل ملف PDF إلى PDF/A(1A) وحفظ "ResultConvertToPDFA.pdf"*/
      /*أثناء عملية التحويل، يتم أيضاً تنفيذ التحقق، "ResultConvertToPDFA.xml"*/
      const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
      console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي سيتم تحويله.
1. تهيئة وحدة AsposePdf. استلم الكائن إذا كانت ناجحة.
1. استدعاء الدالة [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. إصلاح ملف PDF. وهكذا، إذا كان 'json.errorCode' هو 0، يتم حفظ نتيجة العملية في "ResultConvertToPDFA.pdf". أثناء عملية التحويل، يتم إجراء التحقق، ويتم حفظ نتائج التحقق كـ "ResultConvertToPDFALog.xml". إذا لم يكن معامل json.errorCode هو 0 وبناءً عليه، ظهرت خطأ في ملفك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*تحويل ملف PDF إلى PDF/A(1A) وحفظ "ResultConvertToPDFA.pdf"*/
  /*أثناء عملية التحويل، يتم أيضًا إجراء التحقق، "ResultConvertToPDFA.xml"*/
  const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
  console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
```