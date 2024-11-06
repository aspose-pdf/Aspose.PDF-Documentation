---
title: تقسيم PDF باستخدام JavaScript
linktitle: تقسيم ملفات PDF
type: docs
weight: 30
url: ar/javascript-cpp/split-pdf/
description: يوضح هذا الموضوع كيفية تقسيم صفحات PDF إلى ملفات PDF فردية باستخدام Aspose.PDF لـ JavaScript عبر C++.
lastmod: "2022-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## تقسيم PDF إلى ملفين باستخدام JavaScript

يوضح هذا الموضوع كيفية تقسيم صفحات PDF إلى ملفات PDF فردية باستخدام JavaScript. حاليًا، ندعم الانقسام إلى جزئين. يعني ذلك أن `pageToSplit` هو علامة للتقسيم. سيحتوي الملف الأول على جميع الصفحات من 1 إلى `pageToSplit` شاملة، وسيحتوي الملف الثاني على بقية الصفحات.

تعتمد عملية التقسيم على عدد الصفحات في المستند ويمكن أن تستغرق وقتًا طويلًا جدًا. لذلك، نوصي بشدة باستخدام Web Workers.

الشفرة البرمجية المقدمة هي مثال على استخدام Web Worker في JavaScript لتقسيم ملف PDF إلى ملفين PDF منفصلين وتقديم خيار للمستخدم لتحميل الملفات الناتجة.
 Here's a steps of the code:

1. إنشاء عامل ويب. يتم تهيئة عامل الويب باستخدام ملف البرنامج النصي "AsposePDFforJS.js". سيتولى هذا العامل مهام تقسيم ملفات PDF في الخلفية. في مثالنا، يتم التقاط أي أخطاء تحدث في العامل وتسجيلها في وحدة التحكم.
1. معالجة الرسائل. يتم إعداد عامل الويب للاستماع إلى الرسائل باستخدام معالج الحدث onmessage. عندما يتلقى رسالة من صفحة الويب، يقوم بمعالجة الطلب وإرسال استجابة إلى الخيط الرئيسي.
1. معالج حدث تقسيم الملف. يوجد معالج حدث ffileSplit يتم تشغيله عند اختيار المستخدم لملف PDF للتقسيم. يقرأ الملف PDF المختار باستخدام FileReader ويرسل محتوى الملف والمعايير ذات الصلة (مثل عدد الصفحات للتقسيم وأسماء الملفات الناتجة) إلى عامل الويب عبر استدعاء postMessage.
1. وظيفة تنزيل الملف. وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) مسؤولة عن إنشاء رابط يسمح للمستخدم بتنزيل ملف. تقبل اسم الملف، نوع MIME، ومحتوى الملف. تقوم الوظيفة بإنشاء رابط تنزيل، تربط محتوى الملف به، تعيّن اسم الملف، وتضيفه إلى المستند. هذا يسمح للمستخدم بتنزيل ملفات PDF الناتجة.

1. معالجة الرسائل في العامل الشبكي. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فسيحتوي json.fileNameResult على الاسم الذي حددته مسبقًا. إذا كانت قيمة 'json.errorCode' لا تساوي 0 وبالتالي سيكون هناك خطأ في ملفك، فسيتم تضمين معلومات حول هذا الخطأ في خاصية 'json.errorText'.

1. عرض النتيجة. تتضمن الصفحة الرئيسية عنصرًا بالمعرف 'output'. عندما يرسل عامل الويب رسالة بالنتيجة، يقوم بتحديث عنصر 'output'. إذا كانت العملية ناجحة، فإنه يعرض روابط تنزيل لملفي PDF المنقسمين. إذا كان هناك خطأ، فإنه يعرض رسالة خطأ.

يوضح هذا الكود طريقة لتحميل مهام تقسيم ملفات PDF كثيفة الموارد إلى عامل ويب لمنع حظر خيط واجهة المستخدم الرئيسية. كما يقدم طريقة سهلة الاستخدام لتنزيل ملفات PDF المنقسمة.

```js

    /*إنشاء عامل ويب*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من عامل الويب: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'تم التحميل!' :
        (evt.data.json.errorCode == 0) ?
          `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult1, "application/pdf", evt.data.params[0])}
                  \n${DownloadFile(evt.data.json.fileNameResult2, "application/pdf", evt.data.params[1])}` :
          `خطأ: ${evt.data.json.errorText}`;

    /*معالج الأحداث*/
    const ffileSplit = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*تعيين عدد الصفحات للتقسيم*/
        const pageToSplit = 1;
        /*تقسيم إلى ملفين PDF وحفظ "ResultSplit1.pdf"، "ResultSplit2.pdf" - طلب من عامل الويب*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSplit2Files',
            "params": [event.target.result, e.target.files[0].name, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf"] },
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

The following JavaScript code snippet shows simple example of splitting PDF pages into individual PDF files:

1. حدد ملف PDF للتقسيم.
1. قم بإنشاء كائن 'FileReader' في المعالج.
1. حدد رقم الصفحة للتقسيم.
1. استدعاء [AsposePdfSplit2Files](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfsplit2files/) في المعالج الأخير.
1. تحليل النتيجة. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultSplit2.pdf".
1. بعد ذلك، إذا كانت قيمة 'json.errorCode' تساوي 0، فإن json.fileNameResult سيحتوي على الاسم الذي حددته سابقًا. إذا كانت قيمة المعلمة 'json.errorCode' لا تساوي 0، وبناءً على ذلك، سيكون هناك خطأ في ملفك، فستحتوي الخاصية 'json.errorText' على معلومات حول هذا الخطأ.
1. يمكنك استخدام وظيفة المساعدة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/).

```js

  var ffileSplit = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*حدد رقم الصفحة للتقسيم*/
      const pageToSplit = 1;
      /*قسم إلى ملفي PDF واحفظ "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      const json = AsposePdfSplit2Files(event.target.result, e.target.files[0].name, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = e.target.files[0].name + " split: " + json.fileNameResult1 + ", " + json.fileNameResult2;
      else document.getElementById('output').textContent = json.errorText;
      /*إنشاء رابط لتنزيل ملف النتيجة الأول*/
      DownloadFile(json.fileNameResult1, "application/pdf");
      /*إنشاء رابط لتنزيل ملف النتيجة الثاني*/
      DownloadFile(json.fileNameResult2, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```