---
title: إضافة رأس وتذييل إلى PDF عبر JavaScript عبر C++ 
linktitle: إضافة رأس وتذييل إلى PDF
type: docs
weight: 70
url: /javascript-cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for JavaScript via C++ يتيح لك إضافة رؤوس وتذييلات إلى ملف PDF الخاص بك باستخدام AsposePdfAddTextHeaderFooter.
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for JavaScript عبر C++** يتيح لك إضافة رأس وتذييل في ملف PDF الموجود لديك.

1. قم بإنشاء 'FileReader'.
1. يتم تنفيذ دالة [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddtextheaderfooter/).
1. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultAddHeader.pdf".

1. بعد ذلك، إذا كانت قيمة 'json.errorCode' تساوي 0، فإنه سيتم إعطاء ملف التنزيل الاسم الذي حددته سابقًا. إذا لم تكن قيمة 'json.errorCode' تساوي 0، وبالتالي سيكون هناك خطأ في ملفك، فإن معلومات حول هذا الخطأ ستكون موجودة في ملف 'json.errorText'.
1. نتيجة لذلك، فإن وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) تولد رابطًا وتسمح لك بتنزيل الملف الناتج إلى نظام تشغيل المستخدم.

يعرض لك مقتطف الشيفرة التالي كيفية إضافة نص في رأس ملف PDF باستخدام JavaScript.

```js

  var ffileAddTextHeaderFooter = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*إضافة رأس الصفحة إلى ملف PDF وحفظ "ResultAddHeader.pdf"*/
      const json = AsposePdfAddTextHeaderFooter(event.target.result, e.target.files[0].name, "Aspose.PDF for JavaScript via C++", "", "ResultAddHeader.pdf");
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
      (evt.data == 'ready') ? 'تم التحميل!' :
        (evt.data.json.errorCode == 0) ?
          `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffileAddTextHeaderFooter = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const header = 'Aspose.PDF for JavaScript via C++';
        const footer = 'ASPOSE';
        /*إضافة نص في رأس/تذييل ملف PDF وحفظه باسم "ResultAddHeaderFooter.pdf" - طلب من عامل الويب*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddTextHeaderFooter',
            "params": [event.target.result, e.target.files[0].name, header, footer, "ResultAddHeaderFooter.pdf"] },
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