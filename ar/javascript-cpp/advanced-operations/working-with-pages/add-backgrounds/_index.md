---
title: إضافة خلفية إلى PDF باستخدام JavaScript عبر C++
linktitle: إضافة الخلفيات
type: docs
weight: 10
url: /ar/javascript-cpp/add-backgrounds/
description: أضف صورة خلفية إلى ملف PDF الخاص بك باستخدام JavaScript عبر C++.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

توضح مقتطفات الكود التالية كيفية إضافة صورة خلفية إلى صفحات PDF باستخدام وظيفة [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddbackgroundimage/) مع JavaScript.

في مقتطف الكود التالي، نقوم بتحميل الصورة للعمل عليها في نظام الملفات الداخلي:

1. إنشاء 'FileReader'.
1. تعيين اسم ملف الصورة.
1. إعداد ملف الصورة من BLOB.

```js

  var ffileImage = function (e) {
    const file_reader = new FileReader();
    /*تعيين اسم ملف الصورة*/
    fileBackgroundImage = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*إعداد (حفظ) ملف الصورة من BLOB*/
      AsposePdfPrepare(event.target.result, fileBackgroundImage);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


في المثال التالي، نقوم باختيار ملف PDF للتعامل معه.  
1. قم بإنشاء 'FileReader'.  
1. يتم تنفيذ دالة [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddbackgroundimage/).  
1. أضف ملف الصورة إلى PDF واحفظه باسم "ResultBackgroundImage.pdf".  
1. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فإن ملف DownloadFile الخاص بك سيحمل الاسم الذي حددته مسبقًا. إذا لم يكن معامل 'json.errorCode' يساوي 0، وبناءً عليه، سيكون هناك خطأ في ملفك، فسيتم احتواء معلومات حول هذا الخطأ في ملف 'json.errorText'.  
1. كنتيجة لذلك، تقوم دالة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بتوليد رابط وتسمح لك بتنزيل الملف الناتج إلى نظام التشغيل الخاص بالمستخدم.

```js
  var ffileAddBackgroundImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*أضف ملف صورة خلفية إلى PDF واحفظه باسم "ResultBackgroundImage.pdf"*/
      const json = AsposePdfAddBackgroundImage(event.target.result, e.target.files[0].name, fileBackgroundImage, "ResultBackgroundImage.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*قم بإنشاء رابط لتنزيل ملف النتيجة*/
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
          `النتيجة:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            'تم تحضير الصورة!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `خطأ: ${evt.data.json.errorText}`;

    /*تعيين اسم ملف الصورة الافتراضي: 'Aspose.jpg' محمل بالفعل، انظر الإعدادات في 'settings.json'*/
    var fileBackgroundImage = "Aspose.jpg";

    /*معالج الحدث*/
    const ffileAddBackgroundImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*إضافة صورة خلفية إلى ملف PDF وحفظ "ResultBackgroundImage.pdf" - اسأل عامل الويب*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddBackgroundImage',
            "params": [event.target.result, e.target.files[0].name, fileBackgroundImage, "ResultBackgroundImage.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*تعيين اسم ملف الصورة*/
      fileBackgroundImage = e.target.files[0].name;
      file_reader.onload = event => {
        /*حفظ الـ BLOB في نظام الملفات في الذاكرة للمعالجة*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] },
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
        link.innerHTML = "انقر هنا لتحميل الملف " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```