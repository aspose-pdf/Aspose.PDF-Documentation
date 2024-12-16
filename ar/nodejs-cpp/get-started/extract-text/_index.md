---

title: استخراج النص من PDF في Node.js  
linktitle: استخراج النص من PDF  
type: docs  
weight: 10  
url: /ar/nodejs-cpp/extract-text/  
description: يصف هذا القسم كيفية استخراج النص من مستند PDF باستخدام Aspose.PDF لـ Node.js عبر مجموعة أدوات C++.  
lastmod: "2023-11-16"  
sitemap:  
changefreq: "weekly"  
priority: 0.7  
---
## استخراج النص من جميع صفحات مستند PDF

استخراج النص من PDF ليس سهلاً. فقط عدد قليل من قارئي PDF يمكنهم استخراج النص من صور PDF أو ملفات PDF الممسوحة ضوئيًا. لكن أداة **Aspose.PDF لـ Node.js عبر C++** تتيح لك بسهولة استخراج النص من كافة ملفات PDF في بيئة Node.js.

يوضح هذا الكود كيفية استخدام وحدة AsposePDFforNode.js لاستخراج النص من ملف PDF محدد وتسجيل النص المستخرج أو الأخطاء التي تم مواجهتها.

تحقق من الأجزاء البرمجية واتبع الخطوات لاستخراج النص من ملف PDF الخاص بك:

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.

1. حدد اسم ملف PDF الذي سيتم استخراج النص منه.
1. استدعاء `AsposePdf` كـ Promise وتنفيذ العملية لاستخراج النص. استلم الكائن إذا نجحت العملية.
1. استدعاء الدالة [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. يتم تخزين النص المستخرج في كائن JSON. لذلك، إذا كان 'json.errorCode' يساوي 0، يتم عرض النص المستخرج باستخدام console.log. إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي تظهر خطأ في الملف الخاص بك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*استخراج النص من ملف PDF*/
      const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
      console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الوحدة `asposepdfnodejs`.

1. حدد الاسم لملف PDF الذي سيتم استخراج النص منه.
1. قم بتفعيل وحدة AsposePdf. استلم الكائن إذا كانت العملية ناجحة.
1. استدعِ الوظيفة [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. يتم تخزين النص المستخرج في كائن JSON. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم عرض النص المستخرج باستخدام console.log. إذا كانت قيمة json.errorCode ليست 0 ونتيجة لذلك، يظهر خطأ في ملفك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*استخراج النص من ملف PDF*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```