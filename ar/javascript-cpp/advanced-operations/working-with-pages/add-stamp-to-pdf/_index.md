---
title: إضافة أختام الصور في ملف PDF باستخدام JavaScript عبر C++
linktitle: أختام الصور في ملف PDF
type: docs
weight: 60
url: ar/javascript-cpp/stamping/
description: إضافة ختم الصورة إلى مستند PDF الخاص بك باستخدام وظيفة AsposePdfAddStamp مع مجموعة أدوات JavaScript.
lastmod: "2023-04-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## إضافة ختم صورة في ملف PDF

تُعتبر عملية ختم مستند PDF مشابهة لختم مستند ورقي. يوفر الختم في ملف PDF معلومات إضافية للملف، مثل حماية الملف PDF للاستخدام من قبل الآخرين وتأكيد أمان محتويات الملف PDF. يمكنك استخدام وظيفة [AsposePdfAddStamp](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddstamp/) لإضافة ختم صورة إلى ملف PDF باستخدام JavaScript.

لإضافة ختم صورة:

1. تعيين اسم الملف الافتراضي للصورة.
1. إنشاء 'FileReader'.
1. تعيين اسم ملف الصورة.
1. إعداد ملف الختم من BLOB.

يوضح مقطع الكود التالي كيفية إضافة ختم صورة في ملف PDF.

```js

  /*تعيين اسم ملف الختم الافتراضي*/
  var fileStamp = "/Aspose.jpg";

  var ffileStamp = function (e) {
    const file_reader = new FileReader();
    /*تعيين اسم ملف الختم*/
    fileStamp = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*إعداد (حفظ) ملف الختم من BLOB*/
      AsposePdfPrepare(event.target.result, fileStamp);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


1. قم بإنشاء 'FileReader'.
1. يتم تنفيذ دالة [AsposePdfAddStamp](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddstamp/).
1. أضف ملف الصورة إلى نهاية ملف PDF واحفظ "ResultImage.pdf".
1. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فسيتم إعطاء اسم DownloadFile الاسم الذي حددته سابقًا. إذا لم يكن معامل 'json.errorCode' يساوي 0، وبالتالي، سيكون هناك خطأ في الملف الخاص بك، فسيتم احتواء معلومات حول هذا الخطأ في ملف 'json.errorText'.
1. نتيجة لذلك، تقوم دالة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتسمح لك بتنزيل الملف الناتج على نظام تشغيل المستخدم.

```js
  var ffileAddStamp = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*إدراج ملف الختم في ملف PDF وحفظ "ResultImage.pdf"*/
      const json = AsposePdfAddStamp(event.target.result, e.target.files[0].name, fileStamp, 0, 5, 5, 40, 40, Module.Rotation.on270, 0.5, "ResultStamp.pdf");
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
        (evt.data.json.errorCode == 0) ?
          `النتيجة:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            'تم إعداد الصورة!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `خطأ: ${evt.data.json.errorText}`;

    /*تعيين اسم ملف الختم الافتراضي: 'Aspose.jpg' تم تحميله بالفعل، راجع الإعدادات في 'settings.json'*/
    var fileStamp = "Aspose.jpg";

    /*معالج الحدث*/
    const ffileAddStamp = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const setBackground = 0;
        const setXIndent_ = 5;
        const setYIndent_ = 5;
        const setHeight_ = 40;
        const setWidth_ = 40;
        const rotation_ = 'Module.Rotation.on270';
        const setOpacity = 0.5;
        /*إضافة ختم إلى ملف PDF وحفظه باسم "ResultStamp.pdf" - طلب من Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddStamp',
            "params": [event.target.result, e.target.files[0].name, fileStamp, setBackground, setXIndent_, setYIndent_,
                      setHeight_, setWidth_, rotation_, setOpacity, "ResultStamp.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileStamp = e => {
      const file_reader = new FileReader();
      /*تعيين اسم ملف الختم*/
      fileStamp = e.target.files[0].name;
      file_reader.onload = event => {
        /*حفظ BLOB في الذاكرة FS للمعالجة*/
        AsposePDFWebWorker.postMessage(
            { "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] },
            [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

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