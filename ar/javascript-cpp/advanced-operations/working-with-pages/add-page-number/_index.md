---
title: إضافة رقم الصفحة إلى PDF باستخدام JavaScript عبر C++
linktitle: إضافة رقم الصفحة
type: docs
weight: 100
url: ar/javascript-cpp/add-page-number/
description: Aspose.PDF لــ JavaScript عبر C++ يسمح لك بإضافة ختم رقم الصفحة إلى ملف PDF الخاص بك باستخدام AsposePdfAddPageNum.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

يجب أن تحتوي جميع الوثائق على أرقام الصفحات فيها. يجعل رقم الصفحة من السهل على القارئ تحديد أجزاء مختلفة من الوثيقة.

**Aspose.PDF لــ JavaScript عبر C++** يسمح لك بإضافة أرقام الصفحات باستخدام [AsposePdfAddPageNum](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddpagenum/).

1. أنشئ 'FileReader'.
1. يتم تنفيذ وظيفة [AsposePdfAddPageNum](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddpagenum/).
1. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultAddPageNum.pdf".

1. بعد ذلك، إذا كانت قيمة 'json.errorCode' تساوي 0، فإن ملف DownloadFile سيُعطى الاسم الذي حددته سابقًا. إذا كانت قيمة 'json.errorCode' لا تساوي 0 وبالتالي سيكون هناك خطأ في ملفك، فإن معلومات حول هذا الخطأ ستكون موجودة في ملف 'json.errorText'.
1. نتيجة لذلك، فإن دالة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) تُنشئ رابطًا وتسمح لك بتنزيل الملف الناتج إلى نظام تشغيل المستخدم.

```js
  var ffileAddPageNum = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*إضافة رقم صفحة إلى ملف PDF وحفظه باسم "ResultAddPageNum.pdf"*/
      const json = AsposePdfAddPageNum(event.target.result, e.target.files[0].name, "ResultAddPageNum.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*إنشاء رابط لتنزيل ملف النتيجة*/
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
      (evt.data == 'ready') ? 'تم التحميل!' :
        (evt.data.json.errorCode == 0) ?
          `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffileAddPageNum = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*إضافة رقم صفحة إلى ملف PDF وحفظ "ResultAddPageNum.pdf" - طلب من عامل الويب*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddPageNum', "params": [event.target.result, e.target.files[0].name, "ResultAddPageNum.pdf"] },
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