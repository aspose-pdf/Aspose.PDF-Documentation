---
title: كيفية دمج PDF باستخدام JavaScript عبر C++ 
linktitle: دمج ملفات PDF
type: docs
weight: 20
url: ar/javascript-cpp/merge-pdf/
description: تشرح هذه الصفحة كيفية دمج مستندات PDF في ملف PDF واحد باستخدام Aspose.PDF لـ JavaScript عبر C++ 
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## دمج أو تجميع ملفين PDF في PDF واحد في JavaScript

يُعد دمج وتجميع الملفات مهمة شائعة جدًا أثناء العمل مع عدد كبير من المستندات. في بعض الأحيان، عند العمل مع المستندات والصور، عندما يتم مسحها ضوئيًا ومعالجتها وتنظيمها، يتم إنشاء عدة ملفات. ولكن ماذا لو كنت بحاجة إلى تخزين كل شيء في ملف واحد؟ أو لا ترغب في طباعة عدة مستندات؟ قم بدمج ملفين PDF باستخدام Aspose.PDF لـ JavaScript عبر C++.

تسمح لك هذه الأداة في JavaScript بدمج ملفين PDF في مستند PDF واحد باستخدام Aspose.PDF لـ JavaScript عبر C++. المثال مكتوب بلغة JavaScript.

1. حدد ملفات PDF للدمج.
1. أنشئ 'FileReader'.

1. يتم تنفيذ وظيفة [AsposePdfMerge2Files](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfmerge2files/).
1. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultMerge.pdf".
1. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فإنه يتم إعطاء ملفك الذي تم تنزيله الاسم الذي حددته سابقًا. إذا لم يكن معامل 'json.errorCode' يساوي 0 وبالتالي سيكون هناك خطأ في ملفك، فسيتم احتواء معلومات حول هذا الخطأ في ملف 'json.errorText'.
1. ونتيجة لذلك، تولد وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) رابطًا وتسمح لك بتنزيل الملف الناتج إلى نظام التشغيل الخاص بالمستخدم.

يوضح مقتطف الشيفرة التالي كيفية دمج ملفات PDF:

```js

  var ffileMerge = function (e) {
    const file_reader = new FileReader();
    function readFile(index) {
      /*فقط ملفين*/
      if (index >= e.target.files.length || index >= 2) {
        /*دمج ملفي PDF وحفظ "ResultMerge.pdf"*/
        const json = AsposePdfMerge2Files(undefined, undefined, e.target.files[0].name, e.target.files[1].name, "ResultMerge.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*إنشاء رابط لتنزيل الملف الناتج*/
        DownloadFile(json.fileNameResult, "application/pdf");
        return;
      }
      const file = e.target.files[index];
      file_reader.onload = function (event) {
        /*إعداد (حفظ) ملف من BLOB*/
        AsposePdfPrepare(event.target.result, file.name);
        readFile(index + 1)
      }
      file_reader.readAsArrayBuffer(file);
    }
    readFile(0);
  }
```


### استخدام Web Workers

```js

    /*إنشاء Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'تحميل!' :
        (evt.data.json.errorCode == 0) ? 
          `النتيجة:\n${(evt.data.operation == 'AsposePdfPrepare') ? 
                      fileProcess('AsposePdfMerge2Files', evt.data.json.optdata[0].file, {"fileName2": evt.data.json.fileNameResult}) ?? 'يرجى الانتظار...' : 
                      DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0]) /*AsposePdfMerge2Files*/
                    }` :
          `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث. يتم دمج ملفين فقط. إذا تم اختيار ملف واحد فقط، فاستخدمه. للملف الثاني، تحتاج إلى تنفيذ AsposePdfPrepare */
    const ffileMerge = evt => fileProcess('AsposePdfPrepare',  evt.target.files[(evt.target.files.length == 1) ? 0 : 1],
                                          [{"operation": 'AsposePdfMerge2Files', "file": evt.target.files[0]}])
    /* اسأل Web Worker */
    const fileProcess = (operation, ffile, optdata) => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        if (operation == 'AsposePdfPrepare')
          return AsposePDFWebWorker.postMessage(
                  { "operation": operation, "params": [event.target.result, ffile.name, optdata] },
                  [event.target.result]
                );
        else if (operation == 'AsposePdfMerge2Files')
          return AsposePDFWebWorker.postMessage(
                  { "operation": operation, 
                    "params": [event.target.result, undefined, ffile.name, (optdata === undefined) ? ffile.name : optdata.fileName2,
                                `Result${operation}.pdf`] },
                  [event.target.result]
                );
      }
      file_reader.readAsArrayBuffer(ffile);
    }

    /*إنشاء رابط لتحميل ملف النتيجة*/
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