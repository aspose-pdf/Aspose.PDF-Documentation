---
title: حذف صفحات PDF باستخدام JavaScript عبر C++
linktitle: حذف صفحات PDF
type: docs
weight: 30
url: ar/javascript-cpp/delete-pages/
description: يمكنك حذف الصفحات من ملف PDF الخاص بك باستخدام Aspose.PDF لـ JavaScript عبر C++.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

يمكنك حذف الصفحات من ملف PDF باستخدام Aspose.PDF لـ JavaScript عبر C++. يمكنك الحصول على النتيجة مباشرة في متصفحك.

1. قم بإنشاء 'FileReader'.
2. حدد أرقام الصفحات المراد حذفها.
3. يتم تنفيذ الدالة [AsposePdfDeletePages](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfdeletepages/).
4. يتم تحديد اسم الملف الناتج، في هذا المثال "ResultDeletePages.pdf".
5. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فإن DownloadFile الخاص بك يُعطى الاسم الذي حددته سابقًا. إذا لم يكن معامل 'json.errorCode' يساوي 0 وبالتالي سيكون هناك خطأ في ملفك، فسيتم احتواء معلومات حول هذا الخطأ في ملف 'json.errorText'.

1. نتيجة لذلك، تقوم وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتسمح لك بتنزيل الملف الناتج إلى نظام التشغيل الخاص بالمستخدم.

```js

  var ffileDeletePages = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*سلسلة نصية، تتضمن أرقام الصفحات بالفاصل: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      const numPages = "1-3";
      /*مصفوفة، مصفوفة أرقام الصفحات*/
      /*const numPages = [1,3];*/
      /*رقم، رقم الصفحة*/
      /*const numPages = 1;*/
      /*حذف الصفحات من 1 إلى 3 من ملف PDF وحفظ "ResultOptimize.pdf"*/
      const json = AsposePdfDeletePages(event.target.result, e.target.files[0].name, "ResultDeletePages.pdf", numPages);
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*إنشاء رابط لتنزيل الملف الناتج*/
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
    const ffileDeletePages = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*سلسلة نصية، تتضمن أرقام الصفحات مع الفاصل: "7, 20, 22, 30-32, 33, 36-40, 46"*/
        const numPages = "1-3";
        /*مصفوفة، مصفوفة من أرقام الصفحات*/
        /*const numPages = [1,3];*/
        /*رقم، رقم الصفحة*/
        /*const numPages = 1;*/
        /*حذف الصفحات من ملف PDF وحفظ "ResultDeletePages.pdf - اطلب من عامل الويب"*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfDeletePages',
            "params": [event.target.result, e.target.files[0].name, "ResultDeletePages.pdf", numPages] },
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