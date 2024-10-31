---
title: تحويل PDF إلى مستندات Word في Node.js
linktitle: تحويل PDF إلى Word
type: docs
weight: 10
url: /nodejs-cpp/convert-pdf-to-doc/
lastmod: "2023-11-16"
description: تعلم كيفية تحويل PDF إلى DOC(DOCX) في بيئة Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

لتحرير محتوى ملف PDF في Microsoft Word أو معالجات النصوص الأخرى التي تدعم تنسيقات DOC وDOCX. ملفات PDF قابلة للتحرير، ولكن ملفات DOC وDOCX أكثر مرونة وقابلية للتخصيص.

{{% alert color="success" %}}
**حاول تحويل PDF إلى DOC عبر الإنترنت**

تقدم لك Aspose.PDF لبيئة Node.js تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل PDF إلى DOC](/pdf/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## تحويل PDF إلى DOC

في حال كنت ترغب في تحويل مستند PDF، يمكنك استخدام وظيفة [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
 
يرجى التحقق من مقتطف الشيفرة التالي من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
2. حدد اسم ملف PDF الذي سيتم تحويله.
3. استدعاء `AsposePdf` كـ Promise وتنفيذ العملية لتحويل الملف. استلم الكائن إذا نجحت العملية.
4. استدعاء الدالة [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
5. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPDFtoDoc.doc". إذا لم تكن قيمة المعلمة json.errorCode تساوي 0، وظهرت خطأ في ملفك، فستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*تحويل ملف PDF إلى Doc وحفظ "ResultPDFtoDoc.doc"*/
      const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
      console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
2. تحديد اسم ملف PDF الذي سيتم تحويله
3. تهيئة وحدة AsposePdf. استلام الكائن إذا نجح.
4. استدعاء الوظيفة [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
5. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPDFtoDoc.doc". إذا كان معامل json.errorCode ليس 0 وبالتالي تظهر رسالة خطأ في ملفك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*تحويل ملف PDF إلى Doc وحفظ "ResultPDFtoDoc.doc"*/
  const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
  console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="warning" %}}
**حاول تحويل PDF إلى DOCX عبر الإنترنت**

Aspose.PDF for Node.js تقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF Convertion PDF to Word Free App](/pdf/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## تحويل PDF إلى DOCX

تتيح لك مجموعة أدوات Aspose.PDF لـ Node.js عبر C++ قراءة وتحويل مستندات PDF إلى DOCX. يُعد DOCX تنسيقًا معروفًا لمستندات Microsoft Word حيث تم تغيير هيكله من ثنائي بسيط إلى مزيج من ملفات XML وملفات ثنائية. يمكن فتح ملفات Docx باستخدام Word 2007 والإصدارات اللاحقة ولكن ليس مع الإصدارات الأقدم من MS Word التي تدعم امتدادات ملفات DOC.

في حال كنت ترغب في تحويل مستند PDF، يمكنك استخدام وظيفة [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
يرجى التحقق من مقتطف الشفرة التالي من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
2. تحديد اسم ملف PDF الذي سيتم تحويله.

1. استدعاء `AsposePdf` كـ Promise وتنفيذ العملية لتحويل الملف. استلام الكائن إذا نجحت العملية.
1. استدعاء الدالة [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPDFtoDocX.docx". إذا كان معامل json.errorCode ليس 0 وبالتالي يظهر خطأ في الملف الخاص بك، ستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /* تحويل ملف PDF إلى DocX وحفظ "ResultPDFtoDocX.docx" */
      const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
      console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي سيتم تحويله

1. قم بتهيئة وحدة AsposePdf. احصل على الكائن إذا نجحت العملية.
1. استدعِ الدالة [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. قم بتحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPDFtoDocX.docx". إذا لم يكن معامل json.errorCode يساوي 0 وظهرت بالتالي خطأ في ملفك، ستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /* تحويل ملف PDF إلى DocX وحفظ "ResultPDFtoDocX.docx" */
  const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
  console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```