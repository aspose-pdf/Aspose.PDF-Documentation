---
title: العمل مع بيانات تعريف ملف PDF في Node.js
linktitle: بيانات تعريف ملف PDF
type: docs
weight: 130
url: /ar/nodejs-cpp/pdf-file-metadata/
description: يوضح هذا القسم كيفية الحصول على معلومات ملف PDF، وكيفية الحصول على البيانات الوصفية من ملف PDF، وتعيين معلومات ملف PDF في Node.js.
lastmod: "2026-07-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## احصل على معلومات ملف PDF

في حال كنت تريد الحصول على معلومات ملف PDF، يمكنك استخدام [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/) دالة. 
يرجى التحقق من مقتطف الشيفرة التالي للحصول على معلومات ملف PDF في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` وحدة ك `AsposePdf` متغير.
1. حدد اسم ملف PDF الذي سيتم استخراج المعلومات منه.
1. اتصال `AsposePdf` كـ Promise وتنفيذ العملية لاستخراج المعلومات. استقبل الكائن إذا نجح.
1. استدع الدالة [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. يتم تخزين البيانات الوصفية المستخرجة في كائن JSON. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم عرض البيانات الوصفية المستخرجة باستخدام console.log. إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، فستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Get info (metadata) from a PDF-file*/
      const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
      /* JSON
        Title             : json.title
        Creator           : json.creator
        Author            : json.author
        Subject           : json.subject
        Keywords          : json.keywords
        Creation Date     : json.creation
        Modify Date       : json.mod
        PDF format        : json.format
        PDF version       : json.version
        PDF is PDF/A      : json.ispdfa
        PDF is PDF/UA     : json.ispdfua
        PDF is linearized : json.islinearized
        PDF is encrypted  : json.isencrypted
        PDF permission    : json.permission
        PDF page size     : json.size
        Page count        : json.pagecount
        Annotation count  : json.annotationcount
        Bookmark count    : json.bookmarkcount
        Attachment count  : json.attachmentcount
        Metadata count    : json.metadatacount
        JavaScript count  : json.javascriptcount
        Image count       : json.imagecount
      */
      console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` وحدة.
1. حدد اسم ملف PDF الذي سيتم استخراج المعلومات منه.
1. قم بتهيئة وحدة AsposePdf. استقبل الكائن إذا نجحت.
1. استدع الدالة [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. يتم تخزين البيانات الوصفية المستخرجة في كائن JSON. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم عرض البيانات الوصفية المستخرجة باستخدام console.log. إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، فستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Get info (metadata) from a PDF-file*/
    const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
    /* JSON
      Title             : json.title
      Creator           : json.creator
      Author            : json.author
      Subject           : json.subject
      Keywords          : json.keywords
      Creation Date     : json.creation
      Modify Date       : json.mod
      PDF format        : json.format
      PDF version       : json.version
      PDF is PDF/A      : json.ispdfa
      PDF is PDF/UA     : json.ispdfua
      PDF is linearized : json.islinearized
      PDF is encrypted  : json.isencrypted
      PDF permission    : json.permission
      PDF page size     : json.size
      Page count        : json.pagecount
      Annotation count  : json.annotationcount
      Bookmark count    : json.bookmarkcount
      Attachment count  : json.attachmentcount
      Metadata count    : json.metadatacount
      JavaScript count  : json.javascriptcount
      Image count       : json.imagecount
    */
    console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
```

## الحصول على جميع الخطوط

استخراج الخطوط من ملف PDF يمكن أن يكون طريقة مفيدة لإعادة استخدام الخطوط في مستندات أو تطبيقات أخرى. 

في حال رغبتك في الحصول على الخطوط من ملف PDF، يمكنك استخدام [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/) دالة. 
يرجى التحقق من مقتطف الشيفرة التالي للحصول على الخطوط من ملف PDF في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` وحدة ك `AsposePdf` متغير.
1. حدد اسم ملف PDF الذي سيتم استخراج الخطوط منه.
1. اتصال `AsposePdf` كـ Promise وتنفيذ العملية لاستخراج الخطوط. استلم الكائن إذا نجح.
1. استدع الدالة [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).
1. يتم تخزين الخطوط المستخرجة في كائن JSON. وبالتالي، إذا كان 'json.errorCode' يساوي 0، فإنه يعرض مصفوفة من تفاصيل الخطوط، بما في ذلك اسم الخط، وما إذا كان مضمنًا، وحالة إمكانية الوصول باستخدام console.log. إذا لم يكن معامل json.errorCode يساوي 0 ووفقًا لذلك ظهر خطأ في ملفك، فستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Get list fonts from a PDF-file*/
      const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
      /*json.fonts - array of fonts: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
      console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` وحدة.
1. حدد اسم ملف PDF الذي سيتم استخراج الخطوط منه.
1. قم بتهيئة وحدة AsposePdf. استقبل الكائن إذا نجحت.
1. استدع الدالة [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).
1. يتم تخزين الخطوط المستخرجة في كائن JSON. وبالتالي، إذا كان 'json.errorCode' يساوي 0، فإنه يعرض مصفوفة من تفاصيل الخطوط، بما في ذلك اسم الخط، وما إذا كان مضمنًا، وحالة إمكانية الوصول باستخدام console.log. إذا لم يكن معامل json.errorCode يساوي 0 ووفقًا لذلك ظهر خطأ في ملفك، فستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Get list fonts from a PDF-file*/
  const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
  /*json.fonts - array of fonts: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
  console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
```

## تعيين معلومات ملف PDF

Aspose.PDF for Node.js via C++ يسمح لك بتعيين معلومات محددة للملف في PDF، معلومات مثل المؤلف، تاريخ الإنشاء، الموضوع، والعنوان. لتعيين هذه المعلومات:

في حالة رغبتك في تعيين معلومات خاصة بالملف، يمكنك استخدام [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/) دالة. 
يرجى التحقق من المقتطف البرمجي التالي من أجل تعيين معلومات الملف في بيئة Node.js.

ممكن التعيين: 
- العنوان
- المُنشئ
- المؤلف
- الموضوع
- قائمة الكلمات المفتاحية
- تاريخ الإنشاء
- تعديل التاريخ
- اسم ملف النتيجة

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` وحدة ك `AsposePdf` متغير.
1. حدد اسم ملف PDF الذي ستُحدد فيه المعلومات.
1. اتصال `AsposePdf` كـ Promise وتنفيذ العملية. استلم الكائن إذا نجح.
1. استدع الدالة [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).
1. تعيين معلومات ملف PDF. يتم توفير معلومات مثل العنوان، المنشئ، المؤلف، الموضوع، الكلمات المفتاحية، تاريخ الإنشاء، وتاريخ التعديل كمعاملات. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultSetInfo.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي يظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set PDF info: title, creator, author, subject, keywords, creation (date), mod (date modify)*/
      /*If not need to set value, use undefined or "" (empty string)*/
      /*Set info (metadata) in a PDF-file and save the "ResultSetInfo.pdf"*/
      const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
      console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` وحدة.
1. حدد اسم ملف PDF الذي ستُحدد فيه المعلومات.
1. قم بتهيئة وحدة AsposePdf. استقبل الكائن إذا نجحت.
1. استدع الدالة [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).
1. تعيين معلومات ملف PDF. يتم توفير معلومات مثل العنوان، المنشئ، المؤلف، الموضوع، الكلمات المفتاحية، تاريخ الإنشاء، وتاريخ التعديل كمعاملات. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultSetInfo.pdf". إذا لم يكن معامل json.errorCode يساوي 0، وبالتالي يظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set PDF info: title, creator, author, subject, keywords, creation (date), mod (date modify)*/
  /*If not need to set value, use undefined or "" (empty string)*/
  /*Set info (metadata) in a PDF-file and save the "ResultSetInfo.pdf"*/
  const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
  console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

## إزالة معلومات ملف PDF

Aspose.PDF for Node.js via C++ يتيح لك إزالة بيانات التعريف لملف PDF:

في حال رغبتك في إزالة البيانات الوصفية من PDF، يمكنك استخدام [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/) دالة. 
يرجى التحقق من مقتطف الشيفرة التالي من أجل إزالة البيانات الوصفية من PDF في بيئة Node.js.

**CommonJS:**

1. يتطلب وحدة AsposePDFforNode.js.
1. حدد اسم ملف PDF الذي سيتم إزالة المعلومات منه.
1. قم بتهيئة وحدة AsposePdf. استقبل الكائن إذا نجحت.
1. استدع الدالة [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. حذف معلومات ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfRemoveMetadata.pdf". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Remove metadata from a PDF-file and save the "ResultPdfRemoveMetadata.pdf"*/
      const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
      console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` وحدة.
1. حدد اسم ملف PDF الذي سيتم إزالة المعلومات منه.
1. قم بتهيئة وحدة AsposePdf. استقبل الكائن إذا نجحت.
1. استدع الدالة [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. حذف معلومات ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfRemoveMetadata.pdf". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Remove metadata from a PDF-file and save the "ResultPdfRemoveMetadata.pdf"*/
  const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
  console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```