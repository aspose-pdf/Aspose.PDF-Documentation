---
title: تعيين لون الخلفية لملف PDF باستخدام JavaScript عبر C++
linktitle: تعيين لون الخلفية
type: docs
weight: 80
url: ar/javascript-cpp/set-background-color/
description: تعيين لون الخلفية لملف PDF الخاص بك باستخدام JavaScript عبر C++.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

توضح مقتطفات الشيفرة التالية كيفية تعيين لون خلفية صفحات PDF باستخدام وظيفة [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfsetbackgroundcolor/) مع JavaScript.

في المثال التالي، نقوم بتحديد ملف PDF للتعامل معه.

1. قم بإنشاء 'FileReader'.
2. يتم تنفيذ وظيفة [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfsetbackgroundcolor/) (بصيغة ست عشرية “#RRGGBB”، حيث RR-الأحمر، GG-الأخضر و BB-الأزرق أعداد ست عشرية).
3. قم بتعيين لون الخلفية لملف PDF واحفظه باسم "ResultPdfSetBackgroundColor.pdf"

1. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فإن ملف DownloadFile سيتم إعطاؤه الاسم الذي حددته سابقًا. إذا لم يكن معامل 'json.errorCode' يساوي 0 وبالتالي سيكون هناك خطأ في ملفك، فسيتم احتواء معلومات حول هذا الخطأ في ملف 'json.errorText'.
1. كنتيجة، تقوم الدالة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتسمح لك بتنزيل الملف الناتج إلى نظام تشغيل المستخدم.

```js

  var ffilePdfSetBackgroundColor = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*تعيين لون الخلفية لملف PDF وحفظ "ResultPdfSetBackgroundColor.pdf"*/
        const json = AsposePdfSetBackgroundColor(event.target.result, e.target.files[0].name, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
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
        (evt.data.json.errorCode == 0) ? `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffilePdfSetBackgroundColor = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const backgroundColor= "#426bf4";
        /*تعيين لون الخلفية لملف PDF وحفظ "ResultPdfSetBackgroundColor.pdf" - طلب من عامل الويب*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfSetBackgroundColor', "params": [event.target.result, e.target.files[0].name, backgroundColor, "ResultPdfSetBackgroundColor.pdf"] }, [event.target.result]);
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