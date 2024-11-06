---
title: تحويل PDF/A إلى تنسيق PDF 
linktitle: تحويل PDF/A إلى تنسيق PDF
type: docs
weight: 110
url: ar/javascript-cpp/convert-pdfa-to-pdf/
lastmod: "2023-11-01"
description: يوضح لك هذا الموضوع كيفية تحويل ملف PDF/A إلى مستند PDF باستخدام Aspose.PDF مع JavaScript.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## تحويل PDF/A إلى تنسيق PDF

```js

  /*إنشاء Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'تم التحميل!' :
        (evt.data.json.errorCode == 0) ? `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffilePdfAConvertToPDF = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*تحويل ملف PDF/A إلى PDF وحفظ "ResultConvertToPDF.pdf" - طلب من Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfAConvertToPDF', "params": [event.target.result, e.target.files[0].name, "ResultConvertToPDF.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [مقطع الكود]

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


التالي هو مثال بسيط لتحويل PDF/A إلى PDF باستخدام شفرة JavaScript:

1. اختيار ملف PDF للتحويل.
2. إنشاء 'FileReader'.
3. تنفيذ وظيفة [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaconverttopdf/).
4. تعيين اسم الملف الناتج، في هذا المثال "ResultConvertToPDFA.pdf".
5. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فإن DownloadFile الخاص بك سيحصل على الاسم الذي حددته سابقًا. إذا كانت قيمة 'json.errorCode' لا تساوي 0، وبناءً على ذلك، سيكون هناك خطأ في ملفك، فإن معلومات حول مثل هذا الخطأ ستكون موجودة في ملف 'json.errorText'.
6. كنتيجة لذلك، تقوم وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتسمح لك بتحميل الملف الناتج إلى نظام التشغيل الخاص بالمستخدم.

```js

    var ffilePdfAConvertToPDF = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*تحويل ملف PDF/A إلى PDF وحفظ "ResultConvertToPDF.pdf"*/
        const json = AsposePdfAConvertToPDF(event.target.result, e.target.files[0].name, "ResultConvertToPDF.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*إنشاء رابط لتحميل الملف الناتج*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

```