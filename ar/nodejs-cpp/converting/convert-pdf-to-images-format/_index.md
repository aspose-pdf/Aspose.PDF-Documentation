---
title: Convert PDF to Image Formats in Node.js
linktitle: Convert PDF to Images
type: docs
weight: 70
url: /ar/nodejs-cpp/convert-pdf-to-images-format/
lastmod: "2023-11-16"
description: يوضح لك هذا الموضوع كيفية استخدام Aspose.PDF لتحويل PDF إلى تنسيقات صور مختلفة مثل TIFF وBMP وJPEG وPNG وSVG ببضع سطور من التعليمات البرمجية في بيئة Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Node.js تحويل PDF إلى صورة

في هذه المقالة، سنوضح لك الخيارات لتحويل PDF إلى تنسيقات الصور.

غالبًا ما يتم حفظ المستندات الممسوحة ضوئيًا مسبقًا بتنسيق ملف PDF. ومع ذلك، هل تحتاج إلى تحريره في محرر رسومات أو إرساله بتنسيق صورة؟ لدينا أداة شاملة لك لتحويل PDF إلى صور باستخدام
المهمة الأكثر شيوعًا هي عندما تحتاج إلى حفظ مستند PDF بالكامل أو بعض الصفحات المحددة من المستند كمجموعة من الصور.
 **Aspose ل Node.js عبر C++** يتيح لك تحويل PDF إلى تنسيقات JPG وPNG لتبسيط الخطوات المطلوبة للحصول على صورك من ملف PDF معين.

**Aspose.PDF ل Node.js عبر C++** يدعم تحويل تنسيقات متعددة من PDF إلى صور. يرجى مراجعة القسم [تنسيقات الملفات المدعومة من Aspose.PDF](https://docs.aspose.com/pdf/nodejs-cpp/supported-file-formats/).

{{% alert color="success" %}}
**حاول تحويل PDF إلى JPEG عبر الإنترنت**

يقدم لك Aspose.PDF ل Node.js تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى JPEG باستخدام التطبيق المجاني](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## تحويل PDF إلى JPEG

في حالة رغبتك في تحويل مستند PDF، يمكنك استخدام دالة [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).

يرجى التحقق من مقتطف الكود التالي لتحويل في بيئة Node.js.
**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
2. حدد اسم ملف PDF الذي سيتم تحويله.
3. استدعاء `AsposePdf` كـ Promise وتنفيذ العملية لتحويل الملف. استلم الكائن إذا نجحت العملية.
4. استدعاء الدالة [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).
5. تحويل ملف PDF. لذا، إذا كانت 'json.errorCode' تساوي 0، يتم حفظ نتيجة العملية في "ResultPdfToJpg{0:D2}.jpg". حيث يمثل {0:D2} رقم الصفحة بتنسيق مكون من رقمين. يتم حفظ الصور بدقة 150 DPI. إذا كانت قيمة المعامل json.errorCode لا تساوي 0 وظهرت، بالتالي، خطأ في ملفك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /* تحويل ملف PDF إلى JPG باستخدام النموذج "ResultPdfToJpg{0:D2}.jpg" (رقم الصفحة بتنسيق {0}, {0:D2}, {0:D3}, ...)، الدقة 150 DPI وحفظ */
      const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
      console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
2. تحديد اسم ملف PDF الذي سيتم تحويله.
3. تهيئة وحدة AsposePdf. استلم الكائن إذا تم بنجاح.
4. استدعاء الدالة [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).
5. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfToJpg{0:D2}.jpg". حيث يمثل {0:D2} رقم الصفحة بتنسيق مكون من رقمين. يتم حفظ الصور بدقة 150 DPI. إذا لم يكن معامل json.errorCode يساوي 0 وظهرت خطأ في ملفك، فسيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*تحويل ملف PDF إلى JPG باستخدام النموذج "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... تنسيق رقم الصفحة)، دقة 150 DPI وحفظ*/
  const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
  console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


{{% alert color="success" %}}
**حاول تحويل PDF إلى TIFF عبر الإنترنت**

يقدم لك Aspose.PDF لـ Node.js تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF التحويل من PDF إلى TIFF باستخدام التطبيق المجاني](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## تحويل PDF إلى TIFF

في حالة رغبتك في تحويل مستند PDF، يمكنك استخدام وظيفة [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/). 
يرجى التحقق من مقتطف الشيفرة التالي لتحويل في بيئة Node.js.

**CommonJS:**

1. قم باستدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
2. حدد اسم ملف PDF الذي سيتم تحويله.
3. استدع `AsposePdf` كـ Promise وقم بتنفيذ العملية لتحويل الملف. تلقي الكائن إذا نجحت العملية.

1. استدعاء الدالة [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfToTiff{0:D2}.tiff". حيث يمثل {0:D2} رقم الصفحة بصيغة من رقمين. يتم حفظ الصور بدقة 150 DPI. إذا لم يكن معامل json.errorCode يساوي 0 وظهرت بالتالي خطأ في ملفك، ستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*تحويل ملف PDF إلى TIFF باستخدام القالب "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}، ... صيغة رقم الصفحة)، دقة 150 DPI والحفظ*/
      const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
      console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي سيتم تحويله
1. تهيئة وحدة AsposePdf. استلم الكائن إذا نجحت العملية.
1. استدعاء الدالة [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfToTiff{0:D2}.tiff". حيث يمثل {0:D2} رقم الصفحة بصيغة مكونة من رقمين. يتم حفظ الصور بدقة 150 DPI. إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، فسيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*تحويل ملف PDF إلى TIFF باستخدام القالب "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... صيغة رقم الصفحة)، دقة 150 DPI وحفظ*/
  const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
  console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


{{% alert color="success" %}}
**حاول تحويل PDF إلى PNG عبر الإنترنت**

كمثال على كيفية عمل تطبيقاتنا المجانية، يرجى التحقق من الميزة التالية.

Aspose.PDF لـ Node.js يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![كيفية تحويل PDF إلى PNG باستخدام التطبيق المجاني](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## تحويل PDF إلى PNG

في حال كنت ترغب في تحويل مستند PDF، يمكنك استخدام دالة [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
يرجى التحقق من مقتطف الشفرة التالي من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
1. تحديد اسم ملف PDF الذي سيتم تحويله.
1. استدعاء `AsposePdf` كـ Promise وتنفيذ العملية لتحويل الملف. استلم الكائن إذا نجحت العملية.

1. استدعاء الدالة [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfToPng{0:D2}.png". حيث يمثل {0:D2} رقم الصفحة بتنسيق من رقمين. يتم حفظ الصور بدقة 150 DPI. إذا كانت قيمة معلمة json.errorCode ليست 0 وبناءً عليه ظهر خطأ في ملفك، سيتم تضمين معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /* تحويل ملف PDF إلى PNG مع النموذج "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... تنسيق رقم الصفحة)، دقة 150 DPI وحفظ */
      const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
      console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي سيتم تحويله
1. تهيئة وحدة AsposePdf. استلم الكائن إذا كان ناجحًا.
1. استدعاء الدالة [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' هو 0، يتم حفظ نتيجة العملية في "ResultPdfToPng{0:D2}.png". حيث يمثل {0:D2} رقم الصفحة بصيغة مكونة من رقمين. يتم حفظ الصور بدقة 150 DPI. إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي يظهر خطأ في ملفك، سيتم تضمين معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*تحويل ملف PDF إلى PNG باستخدام القالب "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}، ... صيغة رقم الصفحة)، بدقة 150 DPI وحفظها*/
  const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
  console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


{{% alert color="success" %}}
**حاول تحويل PDF إلى SVG عبر الإنترنت**

Aspose.PDF ل Node.js يقدم لك تطبيقًا مجانيًا عبر الإنترنت ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى SVG باستخدام تطبيق مجاني](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**رسومات المتجهات القابلة للتحجيم (SVG)** هي عائلة من المواصفات لتنسيق ملف قائم على XML للرسومات المتجهة ثنائية الأبعاد، سواء كانت ثابتة أو ديناميكية (تفاعلية أو متحركة). مواصفات SVG هي معيار مفتوح تم تطويره من قبل رابطة الشبكة العالمية (W3C) منذ عام 1999.

## تحويل PDF إلى SVG

### تحويل PDF إلى SVG كلاسيكي

في حالة رغبتك في تحويل مستند PDF، يمكنك استخدام وظيفة [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
يرجى مراجعة مقتطف الكود التالي لتحويل في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
1. تحديد اسم ملف PDF الذي سيتم تحويله.
1. استدعاء `AsposePdf` كـ Promise وقم بتنفيذ العملية لتحويل الملف. استلم الكائن إذا كانت العملية ناجحة.
1. استدعاء الدالة [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' هو 0، يتم حفظ نتيجة العملية في "ResultPdfToSvg.svg". إذا لم يكن معامل json.errorCode يساوي 0 وظهرت بالتالي خطأ في الملف الخاص بك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*تحويل ملف PDF إلى SVG وحفظ "ResultPdfToSvg.svg"*/
      const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
      console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي سيتم تحويله
1. تهيئة وحدة AsposePdf. استلام الكائن إذا تم بنجاح.
1. استدعاء الدالة [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfToSvg.svg". إذا كانت قيمة json.errorCode لا تساوي 0، وظهرت بالتالي خطأ في ملفك، ستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*تحويل ملف PDF إلى SVG وحفظ "ResultPdfToSvg.svg"*/
  const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
  console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

### تحويل PDF إلى SVG مضغوط

في حال كنت ترغب في تحويل مستند PDF، يمكنك استخدام دالة [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
 
يرجى التحقق من مقطع الشيفرة التالي من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
1. تحديد اسم ملف PDF الذي سيتم تحويله.
1. استدعاء `AsposePdf` كـ Promise وتنفيذ العملية لتحويل الملف. استقبال الكائن إذا نجحت العملية.
1. استدعاء الدالة [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfToSvgZip.zip". إذا كان معامل json.errorCode ليس 0 وظهرت خطأ في ملفك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*تحويل ملف PDF إلى SVG(zip) وحفظ النتيجة في "ResultPdfToSvgZip.zip"*/
      const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
      console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. تحديد اسم ملف PDF الذي سيتم تحويله
1. تهيئة وحدة AsposePdf. الحصول على الكائن إذا كان ناجحًا.
1. استدعاء الدالة [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
1. تحويل ملف PDF. وهكذا، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfToSvgZip.zip". إذا كانت معلمة json.errorCode ليست 0 وظهرت خطأ في ملفك، فستحتوي معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*تحويل ملف PDF إلى SVG مضغوط وحفظ "ResultPdfToSvgZip.zip"*/
  const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
  console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText)
```

## تحويل PDF إلى DICOM

في حال كنت تريد تحويل مستند PDF، يمكنك استخدام دالة [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
 
يرجى التحقق من المقتطف البرمجي التالي لتحويله في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
1. تحديد اسم ملف PDF الذي سيتم تحويله.
1. استدعاء `AsposePdf` كـ Promise وإجراء العملية لتحويل الملف. استلام الكائن إذا نجحت العملية.
1. استدعاء الدالة [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' هو 0، يتم حفظ نتيجة العملية في "ResultPdfToDICOM{0:D2}.dcm". حيث يمثل {0:D2} رقم الصفحة بتنسيق ذو رقمين. يتم حفظ الصور بدقة 150 DPI. إذا كانت قيمة المعامل json.errorCode ليست 0 وبالتالي ظهرت خطأ في ملفك، فإن معلومات الخطأ ستكون موجودة في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*تحويل ملف PDF إلى DICOM باستخدام النموذج "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... تنسيق رقم الصفحة)، دقة 150 DPI وحفظ*/
      const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
      console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
1. حدد اسم ملف PDF الذي سيتم تحويله.
1. تهيئة وحدة AsposePdf. استلم الكائن إذا تم بنجاح.
1. استدعاء الدالة [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfToDICOM{0:D2}.dcm". حيث يمثل {0:D2} رقم الصفحة بصيغة ذات رقمين. يتم حفظ الصور بدقة 150 DPI. إذا كانت قيمة بارامتر json.errorCode ليست 0، وبناءً عليه، يظهر خطأ في ملفك، فإن معلومات الخطأ ستكون موجودة في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*تحويل ملف PDF إلى DICOM مع القالب "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... صيغة رقم الصفحة)، دقة 150 DPI وحفظ*/
  const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
  console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


## تحويل PDF إلى BMP

في حال كنت ترغب في تحويل مستند PDF، يمكنك استخدام وظيفة [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/). 
يرجى الاطلاع على الجزء التالي من الكود من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. استدعاء `require` واستيراد وحدة `asposepdfnodejs` كمتغير `AsposePdf`.
1. تحديد اسم ملف PDF الذي سيتم تحويله.
1. استدعاء `AsposePdf` كـ Promise وأداء العملية لتحويل الملف. استلام الكائن إذا كانت العملية ناجحة.
1. استدعاء الوظيفة [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/).

1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfToBmp{0:D2}.bmp". حيث يمثل {0:D2} رقم الصفحة بتنسيق مكون من رقمين. يتم حفظ الصور بدقة 150 DPI. إذا كان معامل json.errorCode ليس 0 وبالتالي يظهر خطأ في ملفك، سيتم تضمين معلومات الخطأ في 'json.errorText'.

```js
  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*تحويل ملف PDF إلى BMP باستخدام القالب "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... تنسيق رقم الصفحة)، دقة 150 DPI وحفظ*/
      const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
      console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد وحدة `asposepdfnodejs`.
2. تحديد اسم ملف PDF الذي سيتم تحويله

1. تهيئة وحدة AsposePdf. استلم الكائن إذا نجحت العملية.
1. استدعاء الدالة [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfToBmp{0:D2}.bmp". حيث يمثل {0:D2} رقم الصفحة بتنسيق مكون من رقمين. يتم حفظ الصور بدقة 150 DPI. إذا كانت قيمة المعامل json.errorCode ليست 0 وبالتالي، تظهر خطأ في ملفك، سيتم احتواء معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*تحويل ملف PDF إلى BMP باستخدام القالب "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... تنسيق رقم الصفحة)، دقة 150 DPI وحفظ*/
  const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
  console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```