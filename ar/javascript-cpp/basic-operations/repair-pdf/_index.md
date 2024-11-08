---
title: إصلاح PDF باستخدام JavaScript عبر C++
linktitle: إصلاح PDF
type: docs
weight: 10
url: /ar/javascript-cpp/repair-pdf/
description: يصف هذا الموضوع كيفية إصلاح PDF عبر JavaScript عبر C++
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

يسمح Aspose.PDF لـ JavaScript بإصلاح PDF بجودة عالية. قد لا يفتح ملف PDF لأي سبب، بغض النظر عن البرنامج أو المتصفح. في بعض الحالات يمكن استعادة المستند، جرب الكود التالي وشاهد بنفسك.

1. قم بإنشاء 'FileReader'.
1. يتم تنفيذ وظيفة [AsposePdfRepair](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfrepair/).
1. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPdfRepair.pdf".
1. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، يمكنك الحصول على روابط لملفات النتيجة. إذا لم يكن معامل 'json.errorCode' يساوي 0 وبالتالي، سيكون هناك خطأ في ملفك، فإن معلومات حول هذا الخطأ ستكون موجودة في ملف 'json.errorText'.

1. نتيجة لذلك، تقوم وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتسمح لك بتنزيل الملف الناتج إلى نظام تشغيل المستخدم.

```js

    var ffilePdfRepair = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*إصلاح ملف PDF وحفظ "ResultPdfRepair.pdf"*/
        const json = AsposePdfRepair(event.target.result, e.target.files[0].name, "ResultPdfRepair.pdf");
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
      (evt.data == 'ready') ? 'محمل!' :
        (evt.data.json.errorCode == 0) ? `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffilePdfRepair = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*إصلاح ملف PDF وحفظ "ResultPdfRepair.pdf" - طلب من عامل الويب*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfRepair', "params": [event.target.result, e.target.files[0].name, "ResultPdfRepair.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [مقتطف الشيفرة]

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