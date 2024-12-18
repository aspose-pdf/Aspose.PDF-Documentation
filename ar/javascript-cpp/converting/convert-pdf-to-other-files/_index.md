---
title: تحويل PDF إلى EPUB، TeX، نص، XPS في JavaScript
linktitle: تحويل PDF إلى صيغ أخرى
type: docs
weight: 90
url: /ar/javascript-cpp/convert-pdf-to-other-files/
lastmod: "2023-11-01"
description: يوضح هذا الموضوع كيفية تحويل ملف PDF إلى صيغ ملفات أخرى مثل EPUB، LaTeX، نص، XPS وغيرها باستخدام JavaScript أو JavaScript.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

تعتمد عملية التحويل على عدد الصفحات في المستند ويمكن أن تكون مستهلكة للوقت بشكل كبير. لذلك، نوصي بشدة باستخدام عمال الويب.

يوضح هذا الكود طريقة لنقل مهام تحويل ملفات PDF المستهلكة للموارد إلى عامل ويب لمنع حظر سلسلة واجهة المستخدم الرئيسية. كما يوفر طريقة سهلة للمستخدم لتنزيل الملف المحول.

{{% alert color="success" %}}
**حاول تحويل PDF إلى EPUB عبر الإنترنت**

يقدم لك Aspose.PDF for JavaScript تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF Convertion PDF to EPUB with Free App](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## تحويل PDF إلى EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** هو معيار كتب إلكترونية مجاني ومفتوح من المنتدى الدولي للنشر الرقمي (IDPF). الملفات تتمتع بامتداد .epub. تم تصميم EPUB للمحتوى القابل لإعادة التدفق، مما يعني أن قارئ EPUB يمكنه تحسين النص لعرضه على جهاز معين. كما يدعم EPUB المحتوى ذو التخطيط الثابت. يهدف التنسيق ليكون تنسيقًا واحدًا يمكن للناشرين ومنازل التحويل استخدامه داخليًا، بالإضافة إلى التوزيع والبيع. إنه يحل محل معيار الكتاب الإلكتروني المفتوح.

```js

    /*إنشاء عامل ويب*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من عامل الويب: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'تم التحميل!' :
        (evt.data.json.errorCode == 0) ? `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/epub+zip", evt.data.params[0])}` : `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffileToEPUB = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*تحويل ملف PDF إلى ePub وحفظ "ResultPDFtoEPUB.epub" - طلب من عامل الويب*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToEPUB', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoEPUB.epub"] }, [event.target.result]);
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


يظهر مقتطف الشفرة JavaScript التالي مثالاً بسيطًا لتحويل صفحات PDF إلى ملفات EPUB:

1. اختر ملف PDF للتحويل.
2. أنشئ 'FileReader'.
3. يتم تنفيذ وظيفة [AsposePdfToEPUB](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftoepub/).
4. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPDFtoEPUB.epub".
5. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فإن ملف النتيجة الخاص بك يُعطى الاسم الذي حددته سابقًا. إذا لم يكن معامل 'json.errorCode' مساويًا لـ 0، وبالتالي، سيكون هناك خطأ في الملف الخاص بك، فسيتم احتواء معلومات حول هذا الخطأ في ملف 'json.errorText'.
6. كنتيجة لذلك، تولد وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) رابطًا وتسمح لك بتنزيل الملف الناتج إلى نظام التشغيل الخاص بالمستخدم.

```js

    var ffileToEPUB = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /* تحويل ملف PDF إلى EPUB وحفظ "ResultPDFtoEPUB.epub" */
        const json = AsposePdfToEPUB(event.target.result, e.target.files[0].name, "ResultPDFtoEPUB.epub");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /* عمل رابط لتنزيل ملف النتيجة */
        DownloadFile(json.fileNameResult, "application/epub+zip");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


{{% alert color="success" %}}
**حاول تحويل PDF إلى LaTeX/TeX عبر الإنترنت**

تقدم Aspose.PDF لـ JavaScript تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى LaTeX/TeX مع تطبيق مجاني](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## تحويل PDF إلى TeX

يدعم **Aspose.PDF لـ JavaScript** تحويل PDF إلى TeX. تنسيق ملف LaTeX هو تنسيق ملف نصي مع العلامات الخاصة ويستخدم في نظام إعداد الوثائق المستند إلى TeX لتنسيق عالي الجودة.

```js

  /*إنشاء Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'تم التحميل!' :
        (evt.data.json.errorCode == 0) ? `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/x-tex", evt.data.params[0])}` : `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffileToTeX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*تحويل ملف PDF إلى TeX وحفظ "ResultPDFtoTeX.tex" - اطلب من Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToTeX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoTeX.tex"] }, [event.target.result]);
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


النص البرمجي التالي بلغة JavaScript يظهر مثالاً بسيطاً لتحويل صفحات PDF إلى ملفات TEX:

1. اختر ملف PDF للتحويل.
2. قم بإنشاء 'FileReader'.
3. يتم تنفيذ وظيفة [AsposePdfToTeX](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftotex/).
4. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPDFtoTeX.tex".
5. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فإن ملف النتيجة الخاص بك يُعطى الاسم الذي حددته سابقًا. إذا كانت قيمة معلمة 'json.errorCode' لا تساوي 0 وبالتالي سيكون هناك خطأ في ملفك، فسيتم احتواء معلومات حول هذا الخطأ في ملف 'json.errorText'.
6. كنتيجة لذلك، فإن وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) تقوم بإنشاء رابط وتسمح لك بتحميل الملف الناتج إلى نظام التشغيل الخاص بالمستخدم.

```js

    var ffileToTeX = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*تحويل ملف PDF إلى TeX وحفظ "ResultPDFtoTeX.tex"*/
        const json = AsposePdfToTeX(event.target.result, e.target.files[0].name, "ResultPDFtoTeX.tex");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*إنشاء رابط لتحميل ملف النتيجة*/
        DownloadFile(json.fileNameResult, "application/x-tex");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


{{% alert color="success" %}}
**حاول تحويل PDF إلى نص عبر الإنترنت**

يقدم لك Aspose.PDF لـ JavaScript تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى نص"](https://products.aspose.app/pdf/conversion/pdf-to-txt)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى نص باستخدام التطبيق المجاني](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## تحويل PDF إلى TXT

```js

    /*إنشاء عامل ويب*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من عامل الويب: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'تم التحميل!' :
        (evt.data.json.errorCode == 0) ? `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "text/plain", evt.data.params[0])}` : `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffileToTxt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*تحويل ملف PDF إلى نص وحفظ "ResultPDFtoTxt.txt" - اطلب من عامل الويب*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToTxt', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoTxt.txt"] }, [event.target.result]);
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


يوضح مقتطف الشيفرة البرمجية التالي بلغة JavaScript مثالاً بسيطاً لتحويل صفحات PDF إلى ملفات TXT:

1. اختر ملف PDF للتحويل.
2. أنشئ 'FileReader'.
3. يتم تنفيذ وظيفة [AsposePdfToTxt](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftotxt/).
4. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPDFtoTxt.txt".
5. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فإن ملف النتيجة سيتم إعطاؤه الاسم الذي حددته سابقاً. إذا لم يكن معامل 'json.errorCode' يساوي 0، وبناءً عليه، سيكون هناك خطأ في ملفك، فسيتم احتواء معلومات حول هذا الخطأ في ملف 'json.errorText'.
6. كنتيجة لذلك، تقوم وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتسمح لك بتنزيل الملف الناتج إلى نظام تشغيل المستخدم.

```js

    var ffileToTxt = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*حول ملف PDF إلى Txt واحفظ "ResultPDFtoTxt.txt"*/
        const json = AsposePdfToTxt(event.target.result, e.target.files[0].name, "ResultPDFtoTxt.txt");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*قم بإنشاء رابط لتنزيل ملف النتيجة*/
        DownloadFile(json.fileNameResult, "text/plain");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


{{% alert color="success" %}}
**حاول تحويل PDF إلى XPS عبر الإنترنت**

تقدم Aspose.PDF for JavaScript تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي تعمل بها.

[![تحويل Aspose.PDF من PDF إلى XPS باستخدام التطبيق المجاني](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## تحويل PDF إلى XPS

يرتبط نوع ملف XPS بشكل أساسي بمواصفات الورق XML من قبل شركة Microsoft Corporation. مواصفات الورق XML (XPS)، التي كانت تُعرف سابقًا بالاسم الرمزي Metro وتحتوي على مفهوم التسويق Next Generation Print Path (NGPP)، هي مبادرة مايكروسوفت لدمج إنشاء المستندات وعرضها في نظام تشغيل Windows.

**Aspose.PDF for JavaScript** يمنح إمكانية تحويل ملفات PDF إلى تنسيق <abbr title="XML Paper Specification">XPS</abbr>. دعنا نحاول استخدام الكود المقدم لتحويل ملفات PDF إلى تنسيق XPS باستخدام JavaScript.

```js

    /*إنشاء عامل ويب*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من عامل الويب: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'تم التحميل!' :
        (evt.data.json.errorCode == 0) ? `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.ms-xpsdocument", evt.data.params[0])}` : `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffileToXps = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*تحويل ملف PDF إلى Xps وحفظ "ResultPDFtoXps.xps" - طلب من عامل الويب*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToXps', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoXps.xps"] }, [event.target.result]);
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


The following JavaScript code snippet shows simple example of coverting PDF pages into XPS files:

1. اختر ملف PDF للتحويل.
1. قم بإنشاء 'FileReader'.
1. يتم تنفيذ وظيفة [AsposePdfToXps](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftoxps/).
1. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPDFtoXps.xps".
1. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، يتم إعطاء ملف النتيجة الاسم الذي حددته سابقًا. إذا كانت قيمة 'json.errorCode' لا تساوي 0 وبناءً عليه، سيكون هناك خطأ في ملفك، فسيتم احتواء معلومات حول مثل هذا الخطأ في ملف 'json.errorText'.
1. كنتيجة لذلك، تولد وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) رابطًا وتسمح لك بتنزيل الملف الناتج على نظام تشغيل المستخدم.

```js

    var ffileToXps = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /* تحويل ملف PDF إلى Xps وحفظ "ResultPDFtoXps.xps" */
        const json = AsposePdfToXps(event.target.result, e.target.files[0].name, "ResultPDFtoXps.xps");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /* إنشاء رابط لتحميل ملف النتيجة */
        DownloadFile(json.fileNameResult, "application/vnd.ms-xpsdocument");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


## تحويل PDF إلى PDF بتدرج الرمادي

قم بتحويل PDF إلى أبيض وأسود باستخدام Aspose.PDF لـ JavaScript عبر مجموعة أدوات C++ للويب. لماذا يجب علي تحويل PDF إلى تدرج الرمادي؟ إذا كان ملف PDF يحتوي على العديد من الصور الملونة وكان حجم الملف مهمًا بدلاً من اللون، فإن التحويل يوفر المساحة. إذا قمت بطباعة ملف PDF بالأبيض والأسود، فإن تحويله سيسمح لك بالتحقق بصريًا مما يبدو عليه النتيجة النهائية.

```js

  /*إنشاء Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'تم التحميل!' :
        (evt.data.json.errorCode == 0) ? `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffileConvertToGrayscale = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*تحويل ملف PDF إلى تدرج الرمادي وحفظ "ResultConvertToGrayscale.pdf" - طلب من Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfConvertToGrayscale', "params": [event.target.result, e.target.files[0].name, "ResultConvertToGrayscale.pdf"] }, [event.target.result]);
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


The following JavaScript code snippet shows simple example of coverting PDF pages into Grayscale PDF:

1. حدد ملف PDF للتحويل.
1. قم بإنشاء 'FileReader'.
1. يتم تنفيذ دالة [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfconverttograyscale/).
1. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultConvertToGrayscale.pdf".
1. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، سيتم إعطاء DownloadFile الاسم الذي حددته سابقًا. إذا كان معامل 'json.errorCode' لا يساوي 0، وبالتالي سيكون هناك خطأ في ملفك، فإن معلومات حول هذا الخطأ ستكون موجودة في ملف 'json.errorText'.
1. كنتيجة، دالة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) تولد رابطًا وتسمح لك بتحميل الملف الناتج إلى نظام تشغيل المستخدم.

```js

  var ffileConvertToGrayscale = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*تحويل ملف PDF إلى تدرج الرمادي وحفظ "ResultConvertToGrayscale.pdf"*/
      const json = AsposePdfConvertToGrayscale(event.target.result, e.target.files[0].name, "ResultConvertToGrayscale.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*إنشاء رابط لتحميل الملف الناتج*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```