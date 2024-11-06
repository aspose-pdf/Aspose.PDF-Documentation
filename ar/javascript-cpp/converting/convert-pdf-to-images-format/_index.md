---
title: تحويل PDF إلى تنسيقات الصور في JavaScript
linktitle: تحويل PDF إلى صور
type: docs
weight: 70
url: ar/javascript-cpp/convert-pdf-to-images-format/
lastmod: "2023-11-01"
description: يوضح هذا الموضوع كيفية استخدام Aspose.PDF لتحويل PDF إلى تنسيقات صور مختلفة مثل TIFF وBMP وJPEG وPNG وSVG ببضع سطور من الشيفرة.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## تحويل PDF إلى صورة باستخدام JavaScript

في هذه المقالة، سنعرض لك الخيارات المتاحة لتحويل PDF إلى تنسيقات الصور.

غالبًا ما يتم حفظ المستندات الممسوحة ضوئيًا سابقًا بتنسيق ملف PDF. ولكن، هل تحتاج إلى تحريره في محرر رسومي أو إرساله بصيغة صورة؟ لدينا أداة عالمية لك لتحويل PDF إلى صور باستخدام 
المهمة الأكثر شيوعًا هي عندما تحتاج إلى حفظ مستند PDF كامل أو بعض الصفحات المحددة من المستند كمجموعة من الصور. **Aspose for JavaScript عبر C++** يسمح لك بتحويل PDF إلى تنسيقات JPG وPNG لتبسيط الخطوات المطلوبة للحصول على صورك من ملف PDF معين.

**Aspose.PDF for JavaScript عبر C++** يدعم تحويل PDF إلى تنسيقات الصور المختلفة.
 يرجى التحقق من القسم [Aspose.PDF Supported File Formats](https://docs.aspose.com/pdf/javascript-cpp/supported-file-formats/).

تعتمد عملية التحويل على عدد الصفحات في المستند ويمكن أن تكون مستهلكة للوقت بشكل كبير. لذلك، نوصي بشدة باستخدام Web Workers.

يوضح هذا الكود طريقة لتفريغ مهام تحويل ملفات PDF المكثفة للموارد إلى عامل ويب لمنع حظر خيط واجهة المستخدم الرئيسي. كما أنه يوفر طريقة سهلة الاستخدام لتنزيل الملف المحول.

{{% alert color="success" %}}
**حاول تحويل PDF إلى JPEG عبر الإنترنت**

يقدم لك Aspose.PDF لـ JavaScript تطبيقًا مجانيًا عبر الإنترنت ["PDF to JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF conversion PDF to JPEG with Free App](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## تحويل PDF إلى JPEG

```js

  /*إنشاء عامل ويب*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من عامل الويب: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'تم التحميل!' :
        (evt.data.json.errorCode == 0) ? 
          `عدد الملفات (الصفحات): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/jpeg", element) ) ?? ""}` : 
          `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffileToJpg = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'owner';
        /*تحويل ملف PDF إلى ملفات jpg مع القالب "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... تنسيق رقم الصفحة)، دقة 150 DPI وحفظ - طلب عامل الويب*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToJpg', "params": [event.target.result, e.target.files[0].name, "ResultPdfToJpg{0:D2}.jpg", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Code snippet]

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

The following JavaScript code snippet shows simple example of coverting PDF pages into Jpeg files:

1. اختر ملف PDF للتحويل.
2. قم بإنشاء 'FileReader'.
3. يتم تنفيذ وظيفة [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfpagestojpg/).
4. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPdfToJpg{0:D2}.jpg".
5. بعد ذلك، إذا كانت 'json.errorCode' تساوي 0، سيتم إعطاء ملف النتيجة الاسم الذي حددته سابقًا. إذا كانت قيمة المعامل 'json.errorCode' لا تساوي 0 وبالتالي كان هناك خطأ في ملفك، فسيتم احتواء معلومات عن هذا الخطأ في ملف 'json.errorText'.
6. نتيجة لذلك، تولد وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) رابطًا وتسمح لك بتنزيل الملف الناتج إلى نظام التشغيل الخاص بالمستخدم.

```js

  var ffileToJpg = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*تحويل ملف PDF إلى ملفات jpg مع قالب "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... تنسيق رقم الصفحة), دقة 150 DPI وحفظ*/
      const json = AsposePdfPagesToJpg(event.target.result, e.target.files[0].name, "ResultPdfToJpg{0:D2}.jpg", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "عدد الملفات (الصفحات): " + json.filesCount.toString();
        /*إنشاء روابط للملفات الناتجة*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/jpeg");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```


{{% alert color="success" %}}
**حاول تحويل PDF إلى TIFF عبر الإنترنت**

يقدم لك Aspose.PDF لـ JavaScript تطبيقًا مجانيًا عبر الإنترنت ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)، حيث يمكنك تجربة استكشاف الوظيفة والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى TIFF باستخدام التطبيق المجاني](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## تحويل PDF إلى TIFF

```js

  /*إنشاء عامل ويب*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من عامل الويب: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'محمل!' :
        (evt.data.json.errorCode == 0) ? 
          `عدد الملفات (الصفحات): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/tiff", element) ) ?? ""}` : 
          `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffileToTiff = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*تحويل ملف PDF إلى TIFF مع القالب "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}، ... تنسيق رقم الصفحة)، دقة 150 DPI وحفظ - اطلب من عامل الويب*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToTiff', "params": [event.target.result, e.target.files[0].name, "ResultPdfToTiff{0:D2}.tiff", 150] }, [event.target.result]);
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


The following JavaScript code snippet shows simple example of coverting PDF pages into Tiff files:

1. Select a PDF file for converting.  
1. Create a 'FileReader'.  
1. The [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestotiff/) function is executed.  
1. The name of the resulting file is set, in this example "ResultPdfToTiff{0:D2}.tiff".  
1. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.  
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.  

```js

    var ffileToTiff = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Convert a PDF-file to TIFF with template "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
        const json = AsposePdfPagesToTiff(event.target.result, e.target.files[0].name, "ResultPdfToTiff{0:D2}.tiff", 150);
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "Files(pages) count: " + json.filesCount.toString();
          /*Make links to result files*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/tiff");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

الشفرة التالية بلغة JavaScript تعرض مثالًا بسيطًا لتحويل صفحات PDF إلى ملفات Tiff:

1. اختر ملف PDF للتحويل.
1. أنشئ 'FileReader'.
1. يتم تنفيذ دالة [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestotiff/).
1. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPdfToTiff{0:D2}.tiff".
1. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فإن ملف DownloadFile الخاص بك سيحمل الاسم الذي حددته سابقًا. إذا لم يكن معامل 'json.errorCode' يساوي 0 وبالتالي سيكون هناك خطأ في ملفك، فسيتم احتواء معلومات حول هذا الخطأ في ملف 'json.errorText'.
1. نتيجة لذلك، تقوم دالة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتسمح لك بتنزيل الملف الناتج إلى نظام التشغيل الخاص بالمستخدم.

```js

    var ffileToTiff = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*تحويل ملف PDF إلى TIFF بالقالب "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... رقم الصفحة بالتنسيق)، دقة 150 DPI والحفظ*/
        const json = AsposePdfPagesToTiff(event.target.result, e.target.files[0].name, "ResultPdfToTiff{0:D2}.tiff", 150);
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "عدد الملفات (الصفحات): " + json.filesCount.toString();
          /*إنشاء روابط للملفات الناتجة*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/tiff");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


{{% alert color="success" %}}
**حاول تحويل PDF إلى PNG عبر الإنترنت**

كمثال على كيفية عمل تطبيقاتنا المجانية، يرجى التحقق من الميزة التالية.

يقدم لك Aspose.PDF for JavaScript تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![كيفية تحويل PDF إلى PNG باستخدام التطبيق المجاني](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## تحويل PDF إلى PNG

```js

  /*إنشاء Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'محمل!' :
        (evt.data.json.errorCode == 0) ? 
          `عدد الملفات (الصفحات): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/png", element) ) ?? ""}` : 
          `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffileToPng = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'owner';
        /*تحويل ملف PDF إلى ملفات png باستخدام القالب "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... تنسيق رقم الصفحة)، دقة 150 DPI وحفظ - اطلب من Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToPng', "params": [event.target.result, e.target.files[0].name, "ResultPdfToPng{0:D2}.png", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [مقتطف الشيفرة]

    /*إنشاء رابط لتنزيل الملف الناتج*/
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


The following JavaScript code snippet shows simple example of coverting PDF pages into PNG files:

1. اختر ملف PDF للتحويل.
2. أنشئ 'FileReader'.
3. يتم تنفيذ وظيفة [AsposePdfPagesToPng](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfpagestopng/).
4. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPdfToPng{0:D2}.png".
5. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، يتم إعطاء 'DownloadFile' الاسم الذي حددته سابقًا. إذا كانت قيمة 'json.errorCode' لا تساوي 0، ونتيجة لذلك، سيكون هناك خطأ في ملفك، فسيتم تضمين معلومات حول هذا الخطأ في ملف 'json.errorText'.
6. كنتيجة لذلك، تقوم وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتتيح لك تنزيل الملف الناتج إلى نظام تشغيل المستخدم.

```js

  var ffileToPng = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*تحويل ملف PDF إلى ملفات png باستخدام القالب "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... تنسيق رقم الصفحة)، دقة 150 DPI وحفظ*/
      const json = AsposePdfPagesToPng(event.target.result, e.target.files[0].name, "ResultPdfToPng{0:D2}.png", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "عدد الملفات (الصفحات): " + json.filesCount.toString();
        /*إنشاء روابط للملفات الناتجة*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/png");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```


{{% alert color="success" %}}
**حاول تحويل PDF إلى SVG عبر الإنترنت**

Aspose.PDF ل JavaScript يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)، حيث يمكنك محاولة التحقيق في الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى SVG مع تطبيق مجاني](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**رسومات متجهة قابلة للتوسع (SVG)** هي عائلة من المواصفات لصيغة ملفات مبنية على XML للرسوميات المتجهة الثنائية الأبعاد، سواء كانت ثابتة أو ديناميكية (تفاعلية أو متحركة). تعد مواصفة SVG معيارًا مفتوحًا تم تطويره بواسطة اتحاد شبكة الويب العالمية (W3C) منذ عام 1999.

## تحويل PDF إلى SVG

```js

  /*إنشاء عامل ويب*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error from Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ? 
          `عدد الملفات (الصفحات): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/svg", element) ) ?? ""}` : 
          `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffileToSvg = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*تحويل ملف PDF إلى SVG - طلب من عامل الويب*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToSvg', "params": [event.target.result, e.target.files[0].name, "ResultPdfToSvg.svg"] }, [event.target.result]);
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


يُظهر مقتطف الشيفرة البرمجية التالي بلغة JavaScript مثالاً بسيطاً لتحويل صفحات PDF إلى ملفات SVG:

1. اختر ملف PDF للتحويل.
2. أنشئ 'FileReader'.
3. يتم تنفيذ الدالة [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestosvg/).
4. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPdfToSvg.svg".
5. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، يتم إعطاء ملف التنزيل الاسم الذي حددته سابقًا. إذا لم يكن معامل 'json.errorCode' يساوي 0 وبالتالي سيكون هناك خطأ في ملفك، فإن معلومات عن هذا الخطأ ستكون موجودة في ملف 'json.errorText'.
6. وكنتيجة لذلك، تقوم الدالة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتسمح لك بتنزيل الملف الناتج إلى نظام التشغيل الخاص بالمستخدم.

```js

    var ffileToSvg = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*تحويل ملف PDF إلى SVG*/
        const json = AsposePdfPagesToSvg(event.target.result, e.target.files[0].name, "ResultPdfToSvg.svg");
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "عدد الملفات (الصفحات): " + json.filesCount.toString();
          /*إنشاء روابط للملفات الناتجة*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/svg");
        }
        else document.getElementById('output').textContent = json.errorText;
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


### تحويل PDF إلى SVG مضغوط

```js

  /*إنشاء عامل ويب*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من عامل الويب: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'تم التحميل!' :
        (evt.data.json.errorCode == 0) ? `النتيجة:\n${DownloadFile(evt.data.json.fileNameResult, "application/zip", evt.data.params[0])}` : `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffileToSvgZip = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*تحويل ملف PDF إلى SVG (مضغوط) وحفظ "ResultPdfToSvgZip.zip" - اسأل عامل الويب*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToSvgZip', "params": [event.target.result, e.target.files[0].name, "ResultPdfToSvgZip.zip"] }, [event.target.result]);
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


The following JavaScript code snippet shows simple example of coverting PDF pages into SVG(zip) files:

1. Select a PDF file for converting.  
حدد ملف PDF للتحويل.
1. Create a 'FileReader'.  
قم بإنشاء 'FileReader'.
1. The [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestosvgzip/) function is executed.  
يتم تنفيذ دالة [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestosvgzip/).
1. The name of the resulting file is set, in this example "ResultPdfToSvgZip.zip".  
يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPdfToSvgZip.zip".
1. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.  
بعد ذلك، إذا كانت 'json.errorCode' تساوي 0، سيتم إعطاء ملفك القابل للتنزيل الاسم الذي حددته سابقًا. إذا لم يكن معامل 'json.errorCode' يساوي 0، وبناءً عليه ستكون هناك خطأ في ملفك، فإن المعلومات حول هذا الخطأ ستكون موجودة في ملف 'json.errorText'.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.  
كنتيجة لذلك، تقوم دالة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتسمح لك بتنزيل الملف الناتج إلى نظام تشغيل المستخدم.

```js

    var ffileToSvgZip = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Convert a PDF-file to SVG(zip) and save the "ResultPdfToSvgZip.zip"*/
        /* تحويل ملف PDF إلى SVG(zip) وحفظ "ResultPdfToSvgZip.zip" */
        const json = AsposePdfPagesToSvgZip(event.target.result, e.target.files[0].name, "ResultPdfToSvgZip.zip");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Make a link to download the result file*/
        /* إنشاء رابط لتنزيل الملف الناتج */
        DownloadFile(json.fileNameResult, "application/zip");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


## تحويل PDF إلى DICOM

```js

  /*إنشاء Web Worker*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`خطأ من Web Worker: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? 'تم التحميل!' :
      (evt.data.json.errorCode == 0) ?
        `عدد الملفات (الصفحات): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
          (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "application/dicom", element) ) ?? ""}` :
        `خطأ: ${evt.data.json.errorText}`;

  /*مُعالج الحدث*/
  const ffileToDICOM = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*تحويل ملف PDF إلى DICOM باستخدام القالب "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... تنسيق رقم الصفحة)، دقة 150 DPI وحفظ - اطلب من Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToDICOM', "params": [event.target.result, e.target.files[0].name, "ResultPdfToDICOM{0:D2}.dcm", 150] }, [event.target.result]);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

  /*إنشاء رابط لتنزيل ملف النتيجة*/
  const DownloadFile = (filename, mime, content) => {
      mime = mime || "application/octet-stream";
      var link = document.createElement("a"); 
      link.href = URL.createObjectURL(new Blob([content], {type: mime}));
      link.download = filename;
      link.innerHTML = "اضغط هنا لتنزيل الملف " + filename;
      document.body.appendChild(link); 
      document.body.appendChild(document.createElement("br"));
      return filename;
    }
```


The following JavaScript code snippet shows simple example of coverting PDF pages into DICOM files:

1. Select a PDF file for converting.
1. Create a 'FileReader'.
1. The [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestodicom/) function is executed.
1. The name of the resulting file is set, in this example "ResultPdfToDICOM{0:D2}.dcm".
1. Next, if the 'json.errorCode' is 0, then your result File is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

```js

  var ffileToDICOM = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Convert a PDF-file to DICOM with template "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfPagesToDICOM(event.target.result, e.target.files[0].name, "ResultPdfToDICOM{0:D2}.dcm", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "Files(pages) count: " + json.filesCount.toString();
        /*Make links to result files*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "application/dicom");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

يظهر مقتطف الكود JavaScript التالي مثالًا بسيطًا لتحويل صفحات PDF إلى ملفات DICOM:

1. حدد ملف PDF للتحويل.
2. أنشئ 'FileReader'.
3. يتم تنفيذ وظيفة [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestodicom/).
4. يتم تعيين اسم الملف الناتج، في هذا المثال "ResultPdfToDICOM{0:D2}.dcm".
5. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فإن ملف النتائج الخاص بك يتم إعطاؤه الاسم الذي حددته سابقًا. إذا لم يكن معامل 'json.errorCode' يساوي 0 وبالتالي سيكون هناك خطأ في ملفك، فإن المعلومات حول هذا الخطأ ستتواجد في ملف 'json.errorText'.
6. ونتيجة لذلك، تقوم وظيفة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتسمح لك بتنزيل الملف الناتج إلى نظام تشغيل المستخدم.

```js

  var ffileToDICOM = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*حول ملف PDF إلى DICOM باستخدام القالب "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... صيغة رقم الصفحة)، بدقة 150 DPI واحفظه*/
      const json = AsposePdfPagesToDICOM(event.target.result, e.target.files[0].name, "ResultPdfToDICOM{0:D2}.dcm", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "عدد الملفات (الصفحات): " + json.filesCount.toString();
        /*إنشاء روابط للملفات الناتجة*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "application/dicom");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


## تحويل PDF إلى BMP

```js

    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`خطأ من العامل على الويب: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'محمل!' :
        (evt.data.json.errorCode == 0) ? 
          `عدد الملفات (الصفحات): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/bmp", element) ) ?? ""}` : 
          `خطأ: ${evt.data.json.errorText}`;

    /*معالج الحدث*/
    const ffileToBmp = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*تحويل ملف PDF إلى BMP باستخدام القالب "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... تنسيق رقم الصفحة)، الدقة 150 DPI وحفظ - طلب من العامل على الويب*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToBmp', "params": [event.target.result, e.target.files[0].name, "ResultPdfToBmp{0:D2}.bmp", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*إنشاء رابط لتنزيل الملف الناتج*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "اضغط هنا لتنزيل الملف " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


The following JavaScript code snippet shows simple example of coverting PDF pages into BMP files:

1. اختر ملف PDF للتحويل.
1. أنشئ 'FileReader'.
1. يتم تنفيذ دالة [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestobmp/).
1. يتم تحديد اسم الملف الناتج، في هذا المثال "ResultPdfToBmp{0:D2}.bmp".
1. بعد ذلك، إذا كان 'json.errorCode' يساوي 0، فإن DownloadFile الخاص بك يتم إعطاؤه الاسم الذي حددته سابقًا. إذا كانت قيمة المعلمة 'json.errorCode' لا تساوي 0 وبالتالي سيكون هناك خطأ في ملفك، فسيتم احتواء معلومات حول مثل هذا الخطأ في ملف 'json.errorText'.
1. كنتيجة لذلك، تقوم دالة [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) بإنشاء رابط وتسمح لك بتنزيل الملف الناتج على نظام التشغيل الخاص بالمستخدم.

```js

    var ffileToBmp = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*تحويل ملف PDF إلى BMP باستخدام القالب "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... تنسيق رقم الصفحة)، الدقة 150 DPI وحفظ*/
        const json = AsposePdfPagesToBmp(event.target.result, e.target.files[0].name, "ResultPdfToBmp{0:D2}.bmp", 150);
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "عدد الملفات (الصفحات): " + json.filesCount.toString();
          /*إنشاء روابط لملفات النتيجة*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/bmp");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```