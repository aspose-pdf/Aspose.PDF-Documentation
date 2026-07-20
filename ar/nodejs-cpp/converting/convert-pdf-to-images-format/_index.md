---
title: تحويل PDF إلى صيغ الصور في Node.js
linktitle: تحويل PDF إلى صور
type: docs
weight: 70
url: /ar/nodejs-cpp/convert-pdf-to-images-format/
lastmod: "2026-07-16"
description: يعرض هذا الموضوع لك كيفية استخدام Aspose.PDF لتحويل PDF إلى صيغ صور مختلفة مثل TIFF و BMP و JPEG و PNG و SVG باستخدام بضع أسطر من الشيفرة في بيئة Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## تحويل PDF إلى صورة في Node.js

في هذه المقالة، سنعرض الخيارات المتاحة لتحويل PDF إلى صيغ الصور.

غالبًا ما يتم حفظ المستندات الممسوحة ضوئيًا بصيغة PDF. ولكن قد تحتاج أحيانًا إلى تعديلها في محرر رسومي أو إرسالها لاحقًا بصيغة صورة.
من أكثر السيناريوهات شيوعًا حفظ مستند PDF كامل أو صفحات محددة منه كمجموعة من الصور. يتيح لك **Aspose.PDF لـ Node.js عبر C++** تحويل PDF إلى صيغ مثل JPG وPNG لتبسيط الخطوات المطلوبة لاستخراج الصور من ملف PDF معين.

يدعم **Aspose.PDF لـ Node.js عبر C++** تحويل PDF إلى صيغ صور متعددة. راجع قسم [تنسيقات الملفات المدعومة لـ Aspose.PDF](https://docs.aspose.com/pdf/nodejs-cpp/supported-file-formats/).

{{% alert color="success" %}}
**حاول تحويل PDF إلى JPEG عبر الإنترنت**

يقدم لك Aspose.PDF for Node.js تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), حيث يمكنك محاولة التحقيق في الوظيفة والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى JPEG مع تطبيق مجاني](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## تحويل PDF إلى JPEG

في حال رغبتك في تحويل مستند PDF، يمكنك استخدام [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/) دالة. 
يرجى التحقق من مقطع التعليمات البرمجية التالي من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` وحدة كـ `AsposePdf` متغير.
1. حدد اسم ملف الـ PDF الذي سيتم تحويله.
1. اتصال `AsposePdf` كـ Promise وتنفيذ العملية لتحويل الملف. استلم الكائن إذا نجحت.
1. استدع الدالة [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfToJpg{0:D2}.jpg". حيث يمثل {0:D2} رقم الصفحة بتنسيق من رقمين. تُحفظ الصور بدقة 150 DPI. إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to JPG with template "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
      console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` وحدة.
1. حدد اسم ملف PDF الذي سيتم تحويله
1. قم بتهيئة وحدة AsposePdf. استقبل الكائن إذا نجح.
1. استدع الدالة [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfToJpg{0:D2}.jpg". حيث يمثل {0:D2} رقم الصفحة بتنسيق من رقمين. تُحفظ الصور بدقة 150 DPI. إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to JPG with template "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
  console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى TIFF عبر الإنترنت**

يقدم لك Aspose.PDF for Node.js تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), حيث يمكنك محاولة التحقيق في الوظيفة والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى TIFF باستخدام تطبيق مجاني](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## تحويل PDF إلى TIFF

في حال رغبتك في تحويل مستند PDF، يمكنك استخدام [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/) دالة. 
يرجى التحقق من مقطع التعليمات البرمجية التالي من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` وحدة كـ `AsposePdf` متغير.
1. حدد اسم ملف الـ PDF الذي سيتم تحويله.
1. اتصال `AsposePdf` كـ Promise وتنفيذ العملية لتحويل الملف. استلم الكائن إذا نجحت.
1. استدع الدالة [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfToTiff{0:D2}.tiff". حيث يمثل {0:D2} رقم الصفحة بتنسيق رقمين. يتم حفظ الصور بدقة 150 DPI. إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to TIFF with template "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
      console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` وحدة.
1. حدد اسم ملف PDF الذي سيتم تحويله
1. قم بتهيئة وحدة AsposePdf. استقبل الكائن إذا نجح.
1. استدع الدالة [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfToTiff{0:D2}.tiff". حيث يمثل {0:D2} رقم الصفحة بتنسيق رقمين. يتم حفظ الصور بدقة 150 DPI. إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to TIFF with template "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
  console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى PNG عبر الإنترنت**

كمثال على كيفية عمل تطبيقاتنا المجانية، يرجى التحقق من الميزة التالية.

يقدم لك Aspose.PDF for Node.js تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), حيث يمكنك محاولة التحقيق في الوظيفة والجودة التي يعمل بها.

[![كيفية تحويل PDF إلى PNG باستخدام تطبيق مجاني](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## تحويل PDF إلى PNG

في حال رغبتك في تحويل مستند PDF، يمكنك استخدام [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/) دالة. 
يرجى التحقق من مقطع التعليمات البرمجية التالي من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` وحدة كـ `AsposePdf` متغير.
1. حدد اسم ملف الـ PDF الذي سيتم تحويله.
1. اتصال `AsposePdf` كـ Promise وتنفيذ العملية لتحويل الملف. استلم الكائن إذا نجحت.
1. استدع الدالة [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfToPng{0:D2}.png". حيث يمثل {0:D2} رقم الصفحة بصيغة رقمين. تُحفظ الصور بدقة 150 DPI. إذا لم يكن معلم json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to PNG with template "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
      console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` وحدة.
1. حدد اسم ملف PDF الذي سيتم تحويله
1. قم بتهيئة وحدة AsposePdf. استقبل الكائن إذا نجح.
1. استدع الدالة [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfToPng{0:D2}.png". حيث يمثل {0:D2} رقم الصفحة بصيغة رقمين. تُحفظ الصور بدقة 150 DPI. إذا لم يكن معلم json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، ستتضمن معلومات الخطأ في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to PNG with template "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
  console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى SVG عبر الإنترنت**

يقدم لك Aspose.PDF for Node.js تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), حيث يمكنك محاولة التحقيق في الوظيفة والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى SVG مع تطبيق مجاني](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**رسوميات المتجهات القابلة للتوسع (SVG)** هي عائلة من المواصفات لتنسيق ملف مبني على XML للرسومات المتجهية ثنائية الأبعاد، سواء الثابتة أو الديناميكية (تفاعلية أو متحركة). مواصفة SVG هي معيار مفتوح قيد التطوير من قبل اتحاد شبكة الويب العالمية (W3C) منذ عام 1999.

## تحويل PDF إلى SVG

### تحويل PDF إلى SVG كلاسيكي

في حال رغبتك في تحويل مستند PDF، يمكنك استخدام [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/) دالة. 
يرجى التحقق من مقطع التعليمات البرمجية التالي من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` وحدة كـ `AsposePdf` متغير.
1. حدد اسم ملف الـ PDF الذي سيتم تحويله.
1. اتصال `AsposePdf` كـ Promise وتنفيذ العملية لتحويل الملف. استلم الكائن إذا نجحت.
1. استدع الدالة [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfToSvg.svg". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، ستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to SVG and save the "ResultPdfToSvg.svg"*/
      const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
      console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` وحدة.
1. حدد اسم ملف PDF الذي سيتم تحويله
1. قم بتهيئة وحدة AsposePdf. استقبل الكائن إذا نجح.
1. استدع الدالة [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfToSvg.svg". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، ستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to SVG and save the "ResultPdfToSvg.svg"*/
  const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
  console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

### تحويل PDF إلى SVG مضغوط

في حال رغبتك في تحويل مستند PDF، يمكنك استخدام [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/) دالة. 
يرجى التحقق من مقطع التعليمات البرمجية التالي من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` وحدة كـ `AsposePdf` متغير.
1. حدد اسم ملف الـ PDF الذي سيتم تحويله.
1. اتصال `AsposePdf` كـ Promise وتنفيذ العملية لتحويل الملف. استلم الكائن إذا نجحت.
1. استدع الدالة [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfToSvgZip.zip". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، فإن معلومات الخطأ ستكون موجودة في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to SVG(zip) and save the "ResultPdfToSvgZip.zip"*/
      const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
      console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` وحدة.
1. حدد اسم ملف PDF الذي سيتم تحويله
1. قم بتهيئة وحدة AsposePdf. استقبل الكائن إذا نجح.
1. استدع الدالة [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfToSvgZip.zip". إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، فإن معلومات الخطأ ستكون موجودة في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*convert a PDF-file to SVG zip and save the "ResultPdfToSvgZip.zip"*/
  const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
  console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText)
```

## تحويل PDF إلى DICOM

في حال رغبتك في تحويل مستند PDF، يمكنك استخدام [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/) دالة. 
يرجى التحقق من مقطع التعليمات البرمجية التالي من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` وحدة كـ `AsposePdf` متغير.
1. حدد اسم ملف الـ PDF الذي سيتم تحويله.
1. اتصال `AsposePdf` كـ Promise وتنفيذ العملية لتحويل الملف. استلم الكائن إذا نجحت.
1. استدع الدالة [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfToDICOM{0:D2}.dcm". حيث أن {0:D2} تمثل رقم الصفحة بتنسيق من رقمين. يتم حفظ الصور بدقة 150 DPI. إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، فستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to DICOM with template "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
      console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` وحدة.
1. حدد اسم ملف PDF الذي سيتم تحويله
1. قم بتهيئة وحدة AsposePdf. استقبل الكائن إذا نجح.
1. استدع الدالة [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، يتم حفظ نتيجة العملية في "ResultPdfToDICOM{0:D2}.dcm". حيث أن {0:D2} تمثل رقم الصفحة بتنسيق من رقمين. يتم حفظ الصور بدقة 150 DPI. إذا لم يكن معامل json.errorCode يساوي 0 وبالتالي ظهر خطأ في ملفك، فستكون معلومات الخطأ موجودة في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to DICOM with template "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
  console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

## تحويل PDF إلى BMP

في حال رغبتك في تحويل مستند PDF، يمكنك استخدام [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/) دالة. 
يرجى التحقق من مقطع التعليمات البرمجية التالي من أجل التحويل في بيئة Node.js.

**CommonJS:**

1. اتصال `require` و استيراد `asposepdfnodejs` وحدة كـ `AsposePdf` متغير.
1. حدد اسم ملف الـ PDF الذي سيتم تحويله.
1. اتصال `AsposePdf` كـ Promise وتنفيذ العملية لتحويل الملف. استلم الكائن إذا نجحت.
1. استدع الدالة [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، فإن نتيجة العملية تُحفظ في "ResultPdfToBmp{0:D2}.bmp". حيث يمثل {0:D2} رقم الصفحة بتنسيق عدد مكوّن من رقمين. تُحفظ الصور بدقة 150 DPI. إذا كان معامل json.errorCode ليس 0، ووفقًا لذلك يظهر خطأ في ملفك، فإن معلومات الخطأ ستكون موجودة في 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to BMP with template "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
      console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. استيراد الـ `asposepdfnodejs` وحدة.
1. حدد اسم ملف PDF الذي سيتم تحويله
1. قم بتهيئة وحدة AsposePdf. استقبل الكائن إذا نجح.
1. استدع الدالة [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/).
1. تحويل ملف PDF. وبالتالي، إذا كان 'json.errorCode' يساوي 0، فإن نتيجة العملية تُحفظ في "ResultPdfToBmp{0:D2}.bmp". حيث يمثل {0:D2} رقم الصفحة بتنسيق عدد مكوّن من رقمين. تُحفظ الصور بدقة 150 DPI. إذا كان معامل json.errorCode ليس 0، ووفقًا لذلك يظهر خطأ في ملفك، فإن معلومات الخطأ ستكون موجودة في 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to BMP with template "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
  console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```





