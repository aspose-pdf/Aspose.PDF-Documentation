---
title: العمل مع بيانات ملف PDF الوصفية في Node.js
linktitle: بيانات ملف PDF الوصفية
type: docs
weight: 130
url: /nodejs-cpp/pdf-file-metadata/
description: يشرح هذا القسم كيفية الحصول على معلومات ملف PDF، وكيفية الحصول على البيانات الوصفية من ملف PDF، وضبط معلومات ملف PDF في Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## الحصول على معلومات ملف PDF

في حال كنت ترغب في الحصول على معلومات ملف PDF، يمكنك استخدام دالة [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
يرجى التحقق من مقطع الكود التالي للحصول على معلومات ملف PDF في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
2. تحديد اسم ملف PDF الذي سيتم استخراج المعلومات منه.
3. استدعاء `AsposePdf` كـ Promise وتنفيذ العملية لاستخراج المعلومات. استلام الكائن إذا نجحت العملية.

1. استدعاء الدالة [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. يتم تخزين البيانات الوصفية المستخرجة في كائن JSON. لذلك، إذا كان 'json.errorCode' يساوي 0، يتم عرض البيانات الوصفية المستخرجة باستخدام console.log. إذا كان معامل json.errorCode ليس 0 وظهرت بالتالي خطأ في ملفك، ستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*احصل على المعلومات (البيانات الوصفية) من ملف PDF*/
      const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
      /* JSON
        العنوان            : json.title
        المنشئ             : json.creator
        المؤلف             : json.author
        الموضوع            : json.subject
        الكلمات المفتاحية   : json.keywords
        تاريخ الإنشاء      : json.creation
        تاريخ التعديل      : json.mod
        تنسيق PDF         : json.format
        إصدار PDF         : json.version
        PDF هو PDF/A      : json.ispdfa
        PDF هو PDF/UA     : json.ispdfua
        PDF مفهرس         : json.islinearized
        PDF مشفر          : json.isencrypted
        إذن PDF           : json.permission
        حجم صفحة PDF      : json.size
        عدد الصفحات       : json.pagecount
        عدد التعليقات     : json.annotationcount
        عدد الإشارات المرجعية: json.bookmarkcount
        عدد المرفقات      : json.attachmentcount
        عدد البيانات الوصفية: json.metadatacount
        عدد JavaScript    : json.javascriptcount
        عدد الصور         : json.imagecount
      */
      console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
  });
```


**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي سيتم استخراج المعلومات منه.
1. تهيئة وحدة AsposePdf. استلام الكائن إذا تم بنجاح.
1. استدعاء الدالة [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. يتم تخزين البيانات الوصفية المستخرجة في كائن JSON. لذلك، إذا كان 'json.errorCode' يساوي 0، يتم عرض البيانات الوصفية المستخرجة باستخدام console.log. إذا كانت قيمة json.errorCode ليست 0 وظهرت بالتالي خطأ في ملفك، فسيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /* احصل على المعلومات (البيانات الوصفية) من ملف PDF */
    const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
    /* JSON
      العنوان             : json.title
      المُنشئ             : json.creator
      المؤلف             : json.author
      الموضوع            : json.subject
      الكلمات المفتاحية  : json.keywords
      تاريخ الإنشاء      : json.creation
      تاريخ التعديل      : json.mod
      تنسيق PDF         : json.format
      إصدار PDF         : json.version
      PDF هو PDF/A      : json.ispdfa
      PDF هو PDF/UA     : json.ispdfua
      PDF هو مُخطط      : json.islinearized
      PDF مُشفر         : json.isencrypted
      إذن PDF           : json.permission
      حجم صفحة PDF      : json.size
      عدد الصفحات       : json.pagecount
      عدد التعليقات     : json.annotationcount
      عدد العلامات      : json.bookmarkcount
      عدد المرفقات      : json.attachmentcount
      عدد البيانات الوصفية : json.metadatacount
      عدد جافا سكريبت   : json.javascriptcount
      عدد الصور         : json.imagecount
    */
    console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
```


## الحصول على جميع الخطوط

يمكن أن يكون الحصول على الخطوط من ملف PDF وسيلة مفيدة لإعادة استخدام الخطوط في مستندات أو تطبيقات أخرى.

في حال كنت ترغب في الحصول على الخطوط من ملف PDF، يمكنك استخدام دالة [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/). يرجى الاطلاع على مقتطف الكود التالي للحصول على الخطوط من ملف PDF في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
2. حدد اسم ملف الـ PDF الذي سيتم استخراج الخطوط منه.
3. استدعاء `AsposePdf` كوعد (Promise) وتنفيذ العملية لاستخراج الخطوط. استلام الكائن إذا نجحت العملية.
4. استدعاء الدالة [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).

1. يتم تخزين الخطوط المستخرجة في كائن JSON. وبالتالي، إذا كان 'json.errorCode' يساوي 0، فإنه يعرض مجموعة من تفاصيل الخطوط، بما في ذلك اسم الخط، وما إذا كان مضمناً، وحالة الوصول باستخدام console.log. إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي تظهر خطأ في ملفك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*الحصول على قائمة الخطوط من ملف PDF*/
      const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
      /*json.fonts - مصفوفة الخطوط: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
      console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي سيتم استخراج الخطوط منه.

1. قم بتهيئة وحدة AsposePdf. استلم الكائن إذا نجح.
1. استدعِ الدالة [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).
1. الخطوط المستخرجة مخزنة في كائن JSON. لذلك، إذا كانت 'json.errorCode' تساوي 0، فإنها تعرض مصفوفة من تفاصيل الخطوط، بما في ذلك اسم الخط، وما إذا كان مضمنًا، وحالة إمكانية الوصول الخاصة به باستخدام console.log. إذا كانت قيمة معلمة json.errorCode ليست 0، وبناءً على ذلك، يظهر خطأ في ملفك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*الحصول على قائمة الخطوط من ملف PDF*/
  const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
  /*json.fonts - مصفوفة من الخطوط: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
  console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
```

## تعيين معلومات ملف PDF


Aspose.PDF لـ Node.js عبر C++ يتيح لك تعيين معلومات خاصة بالملف لملف PDF، مثل المؤلف، وتاريخ الإنشاء، والموضوع، والعنوان. لتعيين هذه المعلومات:

في حال أردت تعيين معلومات خاصة بالملف، يمكنك استخدام دالة [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/). 
يرجى التحقق من مقطع الكود التالي لتعيين معلومات الملف في بيئة Node.js.

يمكن تعيين:
- العنوان
- المنشئ
- المؤلف
- الموضوع
- قائمة الكلمات المفتاحية
- تاريخ الإنشاء
- تاريخ التعديل
- اسم ملف النتيجة

**CommonJS:**

1. نداء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
1. تحديد اسم ملف PDF الذي سيتم تعيين المعلومات فيه.
1. استدعاء `AsposePdf` كـ Promise وإجراء العملية. استلام الكائن إذا تم بنجاح.
1. استدعاء الدالة [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).

1. قم بتعيين معلومات ملف PDF. يتم توفير معلومات مثل العنوان، المنشئ، المؤلف، الموضوع، الكلمات المفتاحية، تاريخ الإنشاء، وتاريخ التعديل كمعاملات. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultSetInfo.pdf". إذا لم يكن معامل json.errorCode يساوي 0 وظهرت، بالتالي، خطأ في ملفك، فستحتوي معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*تعيين معلومات PDF: العنوان، المنشئ، المؤلف، الموضوع، الكلمات المفتاحية، الإنشاء (التاريخ)، التعديل (تاريخ التعديل)*/
      /*إذا لم يكن هناك حاجة لتعيين قيمة، استخدم undefined أو "" (سلسلة فارغة)*/
      /*تعيين المعلومات (البيانات الوصفية) في ملف PDF وحفظ "ResultSetInfo.pdf"*/
      const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
      console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. استيراد الوحدة `asposepdfnodejs`.
2. تحديد اسم ملف PDF حيث سيتم تعيين المعلومات.
3. تهيئة وحدة AsposePdf. استلام الكائن إذا تم بنجاح.
4. استدعاء الدالة [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).
5. تعيين معلومات ملف PDF. يتم توفير معلومات مثل العنوان، المنشئ، المؤلف، الموضوع، الكلمات المفتاحية، تاريخ الإنشاء، وتاريخ التعديل كمعلمات. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultSetInfo.pdf". إذا كانت قيمة المعلمة json.errorCode ليست 0 وبالتالي، يظهر خطأ في ملفك، فإن معلومات الخطأ ستحتوي في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*تعيين معلومات PDF: العنوان، المنشئ، المؤلف، الموضوع، الكلمات المفتاحية، الإنشاء (التاريخ)، التعديل (تعديل التاريخ)*/
  /*إذا لم يكن هناك حاجة لتعيين قيمة، استخدم undefined أو "" (سلسلة فارغة)*/
  /*تعيين المعلومات (الميتاداتا) في ملف PDF وحفظ "ResultSetInfo.pdf"*/
  const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
  console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```


## إزالة معلومات ملف PDF

تتيح لك Aspose.PDF لـ Node.js عبر C++ إزالة بيانات التعريف لملف PDF:

في حالة رغبتك في إزالة بيانات التعريف من PDF، يمكنك استخدام دالة [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/). 
يرجى التحقق من مقتطف الشيفرة التالي من أجل إزالة بيانات التعريف من PDF في بيئة Node.js.

**CommonJS:**

1. استدعاء وحدة AsposePDFforNode.js.
2. تحديد اسم ملف PDF الذي سيتم إزالة المعلومات منه.
3. تهيئة وحدة AsposePdf. استقبل الكائن إذا نجحت العملية.
4. استدعاء الدالة [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
5. حذف معلومات ملف PDF. وبالتالي، إذا كان 'json.errorCode' هو 0، فسيتم حفظ نتيجة العملية في "ResultPdfRemoveMetadata.pdf". إذا لم يكن معامل json.errorCode هو 0 وظهرت خطأ في ملفك، فسيتم احتواء معلومات الخطأ في 'json.errorText'.

```js
  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*إزالة بيانات التعريف من ملف PDF وحفظ "ResultPdfRemoveMetadata.pdf"*/
      const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
      console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي سيتم إزالة المعلومات منه.
1. تهيئة وحدة AsposePdf. استلم الكائن إذا كان ناجحًا.
1. استدعاء الدالة [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. حذف معلومات ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfRemoveMetadata.pdf". إذا لم يكن معامل json.errorCode يساوي 0، ونتيجة لذلك تظهر خطأ في ملفك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*إزالة البيانات الوصفية من ملف PDF وحفظ "ResultPdfRemoveMetadata.pdf"*/
  const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
  console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```