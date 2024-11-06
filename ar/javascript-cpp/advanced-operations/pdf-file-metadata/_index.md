---
title: التعامل مع بيانات وصف ملف PDF باستخدام JavaScript عبر C++
linktitle: بيانات وصف ملف PDF
type: docs
weight: 130
url: ar/javascript-cpp/pdf-file-metadata/
description: يوضح هذا القسم كيفية الحصول على معلومات ملف PDF، وكيفية الحصول على البيانات الوصفية من ملف PDF، وتعيين معلومات ملف PDF.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## الحصول على معلومات ملف PDF

1. قم بإنشاء 'FileReader'.
1. يتم تنفيذ وظيفة [AsposePdfGetInfo](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetinfo/).
1. البيانات الوصفية لملف PDF التي يمكن الحصول عليها:
- title - العنوان
- creator - المبدع
- author - المؤلف
- subject - الموضوع
- keywords - الكلمات المفتاحية
- creation - تاريخ الإنشاء
- mod - تاريخ التعديل
1. بعد ذلك، إذا كانت القيمة 'json.errorCode' تساوي 0، يمكنك الحصول على قائمة بمعلومات ملف PDF. إذا لم تكن قيمة 'json.errorCode' تساوي 0، وبالتالي سيكون هناك خطأ في ملفك، فسيتم تضمين معلومات حول هذا الخطأ في ملف 'json.errorText'.

```js

  var ffilePdfGetInfo = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*احصل على المعلومات (البيانات الوصفية) من ملف PDF.*/
      const json = AsposePdfGetInfo(event.target.result, e.target.files[0].name);
      /* JSON
      title - العنوان
      creator - المبدع
      author - المؤلف
      subject - الموضوع
      keywords - الكلمات المفتاحية
      format - تنسيق PDF
      version - إصدار PDF
      ispdfa - PDF هو PDF/A
      ispdfua - PDF هو PDF/UA
      islinearized - PDF هو خطي
      isencrypted - PDF مشفر
      permission - صلاحيات PDF
      size - حجم الصفحة في PDF
      pagecount - عدد الصفحات
      сreation Date: json.creation
      modify Date:   json.mod
      annotationcount - عدد التعليقات التوضيحية
      bookmarkcount - عدد الإشارات المرجعية
      attachmentcount - عدد المرفقات
      metadatacount - عدد البيانات الوصفية
      javascriptcount - عدد JavaScript
      imagecount - عدد الصور
      */
      if (json.errorCode == 0) document.getElementById('output').textContent = "JSON:\n" + JSON.stringify(json, null, 4);
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


### استخدام عمال الويب

```js

    /*إنشاء عامل ويب*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من عامل الويب: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'تم التحميل!' :
        (evt.data.json.errorCode == 0) ?
          `المعلومات:\n${JSON.stringify(evt.data.json, null, 4)}` :
          `خطأ: ${evt.data.json.errorText}`; 

    /*معالج الحدث*/
    const ffilePdfGetInfo = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*الحصول على المعلومات (البيانات الوصفية) من ملف PDF - طلب من عامل الويب*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfGetInfo', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## الحصول على جميع الخطوط

يمكن أن يكون الحصول على الخطوط من ملف PDF وسيلة مفيدة لإعادة استخدام الخطوط في مستندات أو تطبيقات أخرى.
 
في حال كنت ترغب في الحصول على جميع الخطوط من مستند PDF، يمكنك استخدام [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetallfonts/). 
يرجى مراجعة مقتطف الشيفرة التالي للحصول على جميع الخطوط من مستند PDF موجود باستخدام JavaScript عبر C++.

1. إنشاء 'FileReader'.
1. يتم تنفيذ دالة [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetallfonts/).
1. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، يمكنك الحصول على قائمة الخطوط من ملف PDF. إذا كان معلمة 'json.errorCode' لا تساوي 0 وبالتالي ستكون هناك خطأ في ملفك، فسيتم احتواء معلومات حول مثل هذا الخطأ في ملف 'json.errorText'.

```js

  var ffilePdfGetAllFonts = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*الحصول على قائمة الخطوط من ملف PDF.*/
      const json = AsposePdfGetAllFonts(event.target.result, e.target.files[0].name);
      if (json.errorCode == 0) document.getElementById('output').textContent = "JSON:\n" + JSON.stringify(json, null, 4);
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

## استخدام Web Workers

```js

    /* إنشاء Web Worker */
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'تم التحميل!' :
        (evt.data.json.errorCode == 0) ?
          `الخطوط:\n${JSON.stringify(evt.data.json.fonts, null, 4)}` :
          `خطأ: ${evt.data.json.errorText}`; 

    /* معالج الحدث */
    const ffilePdfGetAllFonts = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /* الحصول على قائمة الخطوط لملف PDF - طلب من Web Worker */
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfGetAllFonts', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```
## ضبط معلومات ملف PDF

يتيح لك Aspose.PDF لـ JavaScript عبر C++ تعيين معلومات خاصة بالملف لـ PDF، مثل المؤلف وتاريخ الإنشاء والموضوع والعنوان.
 لتعيين هذه المعلومات:

1. قم بإنشاء 'FileReader'.
1. إذا لم تكن بحاجة إلى تعيين قيمة، استخدم undefined أو "" (سلسلة فارغة).
1. يتم تنفيذ دالة [AsposePdfSetInfo](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfsetinfo/).
1. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultSetInfo.pdf".
1. بعد ذلك، إذا كانت 'json.errorCode' تساوي 0، فسيتم إعطاء DownloadFile الاسم الذي حددته سابقًا. إذا كان معامل 'json.errorCode' لا يساوي 0 وبالتالي سيكون هناك خطأ في ملفك، فسيتم تضمين معلومات حول هذا الخطأ في ملف 'json.errorText'.
1. كنتيجة، تقوم دالة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتسمح لك بتنزيل الملف الناتج إلى نظام تشغيل المستخدم.

```js

    var ffilePdfSetInfo = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*تعيين معلومات PDF: العنوان، المنشئ، المؤلف، الموضوع، الكلمات المفتاحية، الإنشاء (التاريخ)، التعديل (تاريخ التعديل)*/
        /*إذا لم تكن بحاجة إلى تعيين قيمة، استخدم undefined أو "" (سلسلة فارغة)*/
        /*تعيين المعلومات (البيانات الوصفية) في ملف PDF وحفظ "ResultSetInfo.pdf"*/
        const json = AsposePdfSetInfo(event.target.result, e.target.files[0].name, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "16/02/2023 11:55 PM", "ResultSetInfo.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*إنشاء رابط لتنزيل ملف النتيجة*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

### استخدام Web Workers

```js

    /*إنشاء Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'محمل!' :
        (evt.data.json.errorCode == 0) ?
          `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffilePdfSetInfo = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*معلومات PDF: العنوان، المنشئ، المؤلف، الموضوع، الكلمات المفتاحية، الإنشاء (التاريخ)، التعديل (تاريخ التعديل)*/
        const title = 'تعيين معلومات مستند PDF';
        const creator = ''; /*إذا لم تكن بحاجة لتعيين قيمة، استخدم: undefined أو ""/'' (سلسلة فارغة)*/
        const author = 'Aspose';
        const subject = undefined;
        const keywords = 'Aspose.Pdf, DOM, API';
        const creation = undefined; /*تاريخ الإنشاء*/
        const mod = '16/02/2023 11:55 PM'; /*تاريخ التعديل*/
        /*تعيين المعلومات (البيانات الوصفية) في ملف PDF وحفظ "ResultSetInfo.pdf" - اطلب من Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSetInfo',
            "params": [event.target.result, e.target.files[0].name, title, creator, author, subject, keywords, creation, mod, "ResultSetInfo.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*إنشاء رابط لتنزيل ملف النتيجة*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "انقر هنا لتنزيل الملف " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


## إزالة معلومات ملف PDF

تتيح لك Aspose.PDF لـ JavaScript عبر C++ إزالة بيانات تعريف ملف PDF:

1. قم بإنشاء 'FileReader'.
1. يتم تنفيذ وظيفة [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/javascript-cpp/metadata/asposepdfremovemetadata/).
1. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPdfRemoveMetadata.pdf".
1. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فسيتم إعطاء ملفك القابل للتنزيل الاسم الذي حددته سابقًا. إذا لم يكن معامل 'json.errorCode' مساويًا لـ 0 ونتيجة لذلك، سيكون هناك خطأ في ملفك، فسيتم احتواء معلومات حول هذا الخطأ في ملف 'json.errorText'.
1. وكنتيجة لذلك، تقوم وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتسمح لك بتنزيل الملف الناتج على نظام تشغيل المستخدم.

```js

    var ffilePdfRemoveMetadata = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*إزالة بيانات التعريف من ملف PDF وحفظ "ResultPdfRemoveMetadata.pdf"*/
        const json = AsposePdfRemoveMetadata(event.target.result, e.target.files[0].name, "ResultPdfRemoveMetadata.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*إنشاء رابط لتنزيل الملف الناتج*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


### استخدام عمال الويب

```js

    /*إنشاء عامل ويب*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من عامل الويب: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'تم التحميل!' :
        (evt.data.json.errorCode == 0) ? `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffilePdfRemoveMetadata = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*إزالة بيانات التعريف من ملف PDF وحفظ "ResultPdfRemoveMetadata.pdf" - اطلب من عامل الويب*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfRemoveMetadata', "params": [event.target.result, e.target.files[0].name, "ResultPdfRemoveMetadata.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [قطعة كود]

    /*إنشاء رابط لتنزيل ملف النتيجة*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "انقر هنا لتنزيل الملف " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```