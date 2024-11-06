---
title: إضافة توقيع رقمي أو توقيع PDF رقميًا في JavaScript عبر C++
linktitle: توقيع PDF رقميًا
type: docs
weight: 70
url: ar/javascript-cpp/sign-pdf/
description: توقيع مستندات PDF رقميًا باستخدام JavaScript عبر C++.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

التوقيع الرقمي في مستند PDF هو وسيلة للتحقق من أصالة وسلامة المستند. هذه هي عملية التوقيع الإلكتروني لمستند PDF باستخدام مفتاح خاص وشهادة رقمية. يضمن هذا التوقيع لحامل المستند أنه لم يتم تغييره أو تعديله منذ توقيعه وأن الموقع هو الذي يقر به. لتوقيع PDF باستخدام JavaScript، استخدم أداة Aspose.PDF.

يدعم Aspose.PDF for JavaScript عبر C++ ميزة توقيع ملفات PDF رقميًا باستخدام [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfsignpkcs7/).

## توقيع PDF بالتوقيعات الرقمية

```js

    /*تعيين اسم ملف مفتاح PKCS7 الافتراضي*/
    var fileSign = "/test.pfx";

    var ffileSign = function (e) {
      const file_reader = new FileReader();
      /*تعيين اسم ملف مفتاح PKCS7*/
      fileImage = e.target.files[0].name;
      file_reader.onload = (event) => {
        /*حفظ BLOB في الذاكرة FS للمعالجة*/
        AsposePdfPrepare(event.target.result, fileSign);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*تعيين اسم ملف الصورة الافتراضي (مظهر التوقيع)*/
    var signatureAppearance = "/Aspose.jpg";

    var ffileImage = function (e) {
      const file_reader = new FileReader();
      /*تعيين اسم ملف الصورة*/
      signatureAppearance = e.target.files[0].name;
      file_reader.onload = (event) => {
        /*حفظ BLOB في الذاكرة FS للمعالجة*/
        AsposePdfPrepare(event.target.result, signatureAppearance);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    var ffileSignPKCS7 = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        let pswSign = document.getElementById("passwordSign").value;
        /*توقيع ملف PDF بتوقيعات رقمية وحفظ "ResultSignPKCS7.pdf"*/
        const json = AsposePdfSignPKCS7(event.target.result, e.target.files[0].name, 1, fileSign, pswSign, 200, 200, 200, 100, "TEST", "test@test.com", "EU", 1, signatureAppearance,"ResultSignPKCS7.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*إنشاء رابط لتحميل ملف النتيجة*/
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
      (evt.data == 'ready') ? 'تم التحميل!' :
        (evt.data.json.errorCode == 0) ?
          `النتيجة:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            'تم تجهيز الملف!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `خطأ: ${evt.data.json.errorText}`;

    /*تعيين اسم ملف مفتاح PKCS7 الافتراضي*/
    var fileSign = "test.pfx";
    /*تعيين اسم ملف الصورة الافتراضي (مظهر التوقيع): 'Aspose.jpg' تم تحميله بالفعل، انظر الإعدادات في 'settings.json'*/
    var signatureAppearance = "Aspose.jpg";

    /*معالج الحدث*/
    const ffileSignPKCS7 = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const pageNum = 1;
        const pswSign = document.getElementById("passwordSign").value;
        const setXIndent = 100;
        const setYIndent = 100;
        const setHeight = 200;
        const setWidth = 100;
        const reason = 'سبب';
        const contact = 'contact@test.com';
        const location = 'موقع';
        const isVisible = 1;
        /*توقيع ملف PDF بالتوقيعات الرقمية وحفظ "ResultSignPKCS7.pdf" - اسأل Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSignPKCS7',
            "params": [event.target.result, e.target.files[0].name, pageNum, fileSign, pswSign, setXIndent, setYIndent,
                      setHeight, setWidth, reason, contact, location, isVisible, signatureAppearance, "ResultSignPKCS7.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileSign = e => {
      const file_reader = new FileReader();
      /*تعيين اسم ملف مفتاح PKCS7*/
      fileSign = e.target.files[0].name;
      file_reader.onload = event => {
        /*حفظ BLOB في الذاكرة للمعالجة*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, fileSign] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*تعيين اسم ملف الصورة*/
      signatureAppearance = e.target.files[0].name;
      file_reader.onload = event => {
        /*حفظ BLOB في الذاكرة للمعالجة*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, signatureAppearance] },
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