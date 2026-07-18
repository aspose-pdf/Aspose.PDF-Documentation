---
title: تحويل PDF إلى مستندات Word في Node.js
linktitle: تحويل PDF إلى Word
type: docs
weight: 10
url: /ar/nodejs-cpp/convert-pdf-to-doc/
lastmod: "2026-07-16"
description: تعلم كيفية تحويل PDF إلى DOC(DOCX) في بيئة Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

لتحرير محتوى ملف PDF في Microsoft Word أو معالجات النصوص الأخرى التي تدعم صيغ DOC و DOCX. ملفات PDF قابلة للتحرير، لكن ملفات DOC و DOCX أكثر مرونة وقابلة للتخصيص.

{{% alert color="success" %}}
**حاول تحويل PDF إلى DOC عبر الإنترنت**

Aspose.PDF for Node.js يقدم لك تطبيقًا مجانيًا على الإنترنت [“PDF to DOC”](https://products.aspose.app/pdf/conversion/pdf-to-doc), حيث يمكنك محاولة استكشاف الوظيفة والجودة التي يعمل بها.

[![تحويل PDF إلى DOC](/pdf/ar/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## تحويل PDF إلى DOC

في حالة رغبتك في تحويل مستند PDF، يمكنك استخدام [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/) دالة. 
يرجى التحقق من مقتطف الكود التالي لإجراء التحويل في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` الوحدة كـ `AsposePdf` متغيّر.
1. حدّد اسم ملف PDF الذي سيُحول.
1. اتصال `AsposePdf` كـ Promise ونفّذ العملية لتحويل الملف. استقبل الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في \"ResultPDFtoDoc.doc\". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، ستحتوي معلومات الخطأ على 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to Doc and save the "ResultPDFtoDoc.doc"*/
      const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
      console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد `asposepdfnodejs` وحدة.
1. حدد اسم ملف PDF الذي سيتم تحويله
1. ابدأ وحدة AsposePdf. استلم الكائن إذا نجحت العملية.
1. استدعِ الدالة [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في \"ResultPDFtoDoc.doc\". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، ستحتوي معلومات الخطأ على 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to Doc and save the "ResultPDFtoDoc.doc"*/
  const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
  console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="warning" %}}
**حاول تحويل PDF إلى DOCX عبر الإنترنت**

Aspose.PDF for Node.js يقدم لك تطبيقًا مجانيًا على الإنترنت ["PDF إلى Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), حيث يمكنك محاولة استكشاف الوظيفة والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى Word تطبيق مجاني](/pdf/ar/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## تحويل PDF إلى DOCX

تتيح مجموعة أدوات Aspose.PDF for Node.js عبر C++ لك قراءة وتحويل مستندات PDF إلى DOCX. DOCX هو تنسيق معروف لمستندات Microsoft Word تم تغيير هيكله من ثنائي بسيط إلى مزيج من ملفات XML والملفات الثنائية. يمكن فتح ملفات DOCX باستخدام Word 2007 والإصدارات اللاحقة ولكن ليس مع الإصدارات الأقدم من MS Word التي تدعم امتدادات ملفات DOC.

في حالة رغبتك في تحويل مستند PDF، يمكنك استخدام [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/) دالة. 
يرجى التحقق من مقتطف الكود التالي لإجراء التحويل في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` الوحدة كـ `AsposePdf` متغيّر.
1. حدّد اسم ملف PDF الذي سيُحول.
1. اتصال `AsposePdf` كـ Promise ونفّذ العملية لتحويل الملف. استقبل الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPDFtoDocX.docx". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to DocX and save the "ResultPDFtoDocX.docx"*/
      const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
      console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد `asposepdfnodejs` وحدة.
1. حدد اسم ملف PDF الذي سيتم تحويله
1. ابدأ وحدة AsposePdf. استلم الكائن إذا نجحت العملية.
1. استدعِ الدالة [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPDFtoDocX.docx". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to DocX and save the "ResultPDFtoDocX.docx"*/
  const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
  console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```


