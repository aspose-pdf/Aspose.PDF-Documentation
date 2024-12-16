---
title: تحسين PDF باستخدام Aspose.PDF لـ JavaScript عبر C++
linktitle: تحسين ملف PDF
type: docs
weight: 10
url: /ar/javascript-cpp/optimize-pdf/
description: تحسين وضغط ملفات PDF لعرض سريع على الويب باستخدام أداة JavaScript.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## تحسين مستند PDF

تتيح لك الأداة من Aspose.PDF لـ JavaScript عبر C++ تحسين محتوى PDF للويب.

يشير التحسين، أو الخطية للويب، إلى عملية جعل ملف PDF مناسبًا للتصفح عبر الإنترنت باستخدام متصفح ويب. لتحسين ملف لعرض الويب:

1. اختر ملف PDF للتحسين.
2. أنشئ 'FileReader'.
3. يتم تنفيذ وظيفة [AsposePdfOptimize](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfoptimize/).
4. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultOptimize.pdf".

1. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فإن ملف DownloadFile يتم إعطاؤه الاسم الذي حددته سابقاً. إذا كانت قيمة 'json.errorCode' لا تساوي 0 وبالتالي يوجد خطأ في الملف، فإن المعلومات حول هذا الخطأ ستكون موجودة في ملف 'json.errorText'.
1. كنتيجة لذلك، فإن وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) تولد رابطاً وتسمح لك بتحميل الملف الناتج إلى نظام التشغيل الخاص بالمستخدم.

يوضح مقطع الشيفرة التالي كيفية تحسين مستند PDF.

```js

  var ffileOptimize = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*تحسين ملف PDF وحفظ "ResultOptimize.pdf"*/
      const json = AsposePdfOptimize(event.target.result, e.target.files[0].name, "ResultOptimize.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*إنشاء رابط لتحميل ملف النتيجة*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


## استخدام عمال الويب

```js

    /*إنشاء عامل ويب*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من عامل الويب: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'محمل!' :
        (evt.data.json.errorCode == 0) ?
          `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffileOptimize = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*تحسين ملف PDF وحفظ "ResultOptimize.pdf" - اسأل عامل الويب*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfOptimize', "params": [event.target.result, e.target.files[0].name, "ResultOptimize.pdf"] },
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