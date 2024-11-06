---
title: تحسين موارد PDF باستخدام JavaScript عبر C++
linktitle: تحسين موارد PDF
type: docs
weight: 15
url: ar/javascript-cpp/optimize-pdf-resources/
description: تحسين موارد ملفات PDF لعرض الويب السريع باستخدام أداة JavaScript.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## تحسين موارد PDF

تحسين الموارد في الوثيقة:

  1. يتم إزالة الموارد التي لا تُستخدم في صفحات الوثيقة
  1. يتم دمج الموارد المتساوية في كائن واحد
  1. يتم حذف الكائنات غير المستخدمة
 
1. اختر ملف PDF لتحسينه.
1. أنشئ 'FileReader'.
1. يتم تنفيذ وظيفة [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfoptimizeresource/).
1. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPdfOptimizeResource.pdf".

1. بعد ذلك، إذا كان 'json.errorCode' هو 0، فإن ملف DownloadFile الخاص بك سيُعطى الاسم الذي قمت بتحديده مسبقًا. إذا كانت قيمة المعامل 'json.errorCode' لا تساوي 0، وبالتالي، سيكون هناك خطأ في ملفك، فإن المعلومات حول هذا الخطأ ستكون موجودة في ملف 'json.errorText'.
1. نتيجة لذلك، تقوم وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتسمح لك بتنزيل الملف الناتج إلى نظام التشغيل الخاص بالمستخدم.

يعرض مقطع الشيفرة التالي كيفية تحسين مستند PDF.

```js

    var ffilePdfOptimizeResource = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*تحسين موارد ملف PDF وحفظ "ResultPdfOptimizeResource.pdf"*/
        const json = AsposePdfOptimizeResource(event.target.result, e.target.files[0].name, "ResultPdfOptimizeResource.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*إنشاء رابط لتنزيل ملف النتيجة*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


## استخدام Web Workers

```js

    /*إنشاء Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'تم التحميل!' :
        (evt.data.json.errorCode == 0) ? `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffilePdfOptimizeResource = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*تحسين موارد ملف PDF وحفظ "ResultPdfOptimizeResource.pdf" - طلب من Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfOptimizeResource', "params": [event.target.result, e.target.files[0].name, "ResultPdfOptimizeResource.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [مقتطف الكود]

    /*إنشاء رابط لتحميل ملف النتيجة*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "انقر هنا لتحميل الملف " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```