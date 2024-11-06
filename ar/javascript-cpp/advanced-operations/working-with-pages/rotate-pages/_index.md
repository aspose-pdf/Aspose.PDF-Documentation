---
title: تدوير صفحات PDF باستخدام JavaScript عبر C++
linktitle: تدوير صفحات PDF
type: docs
weight: 50
url: ar/javascript-cpp/rotate-pages/
description: يصف هذا الموضوع كيفية تدوير اتجاه الصفحة في ملف PDF موجود برمجيًا عبر JavaScript عبر C++
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

تصف هذه القسم كيفية تغيير اتجاه الصفحة من أفقي إلى عمودي والعكس في ملف PDF موجود باستخدام JavaScript عبر C++.

1. إنشاء 'FileReader'.
1. يتم تنفيذ وظيفة [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfrotateallpages/).
1. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultRotation.pdf".

1. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فإن ملفك الذي يتم تنزيله سيحمل الاسم الذي حددته سابقًا. إذا لم يكن معامل 'json.errorCode' يساوي 0، وبالتالي سيكون هناك خطأ في ملفك، فإن المعلومات حول هذا الخطأ ستكون موجودة في ملف 'json.errorText'.
1. كنتيجة لذلك، فإن وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) تولد رابطًا وتسمح لك بتنزيل الملف الناتج إلى نظام التشغيل الخاص بالمستخدم.

```js

  var ffileRotateAllPages = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /* تدوير جميع صفحات ملف PDF وحفظ "ResultRotation.pdf" */
      const json = AsposePdfRotateAllPages(event.target.result, e.target.files[0].name, Module.Rotation.on270, "ResultRotation.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /* إنشاء رابط لتنزيل ملف النتيجة */
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
        (evt.data.json.errorCode == 0) ?
          `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffileRotateAllPages = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const rotation = 'Module.Rotation.on270';
        /*تدوير صفحات الـPDF وحفظ "ResultRotation.pdf" - طلب من Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfRotateAllPages',
            "params": [event.target.result, e.target.files[0].name, rotation, "ResultRotation.pdf"] },
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