---
title: Конвертировать PDF в форматы изображений в Node.js
linktitle: Конвертировать PDF в изображения
type: docs
weight: 70
url: /ru/nodejs-cpp/convert-pdf-to-images-format/
lastmod: "2026-07-18"
description: Эта тема показывает, как использовать Aspose.PDF для преобразования PDF в различные форматы изображений, например TIFF, BMP, JPEG, PNG, SVG, с помощью нескольких строк кода в среде Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Node.js Преобразовать PDF в изображение

В этой статье мы покажем вам варианты преобразования PDF в форматы изображений.

Ранее отсканированные документы часто сохраняются в формате PDF. Однако вам нужно отредактировать их в графическом редакторе или отправить дальше в формате изображения? У нас есть универсальный инструмент для конвертации PDF в изображения с помощью 
Самая распространённая задача — когда необходимо сохранить весь PDF‑документ или отдельные страницы документа в виде набора изображений. **Aspose for Node.js via C++** позволяет конвертировать PDF в форматы JPG и PNG, упрощая шаги, необходимые для получения изображений из конкретного PDF‑файла.

**Aspose.PDF for Node.js via C++** поддерживает преобразование PDF в различные форматы изображений. Пожалуйста, проверьте раздел. [Aspose.PDF Поддерживаемые форматы файлов](https://docs.aspose.com/pdf/nodejs-cpp/supported-file-formats/).

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в JPEG онлайн**

Aspose.PDF for Node.js представляет вам онлайн бесплатное приложение ["PDF в JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), где вы можете попробовать исследовать функциональность и качество его работы.

[![Преобразование PDF в JPEG с помощью бесплатного приложения Aspose.PDF](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## Конвертируйте PDF в JPEG

Если вы хотите конвертировать PDF-документ, вы можете использовать [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы выполнить конвертацию в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF‑файла, который будет конвертирован.
1. Вызовите `AsposePdf` как Promise и выполните операцию конвертации файла. Получите объект при успешном выполнении.
1. Вызовите функцию [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).
1. Конвертируйте PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPdfToJpg{0:D2}.jpg". Где {0:D2} обозначает номер страницы в двухсимвольном формате. Изображения сохраняются с разрешением 150 DPI. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

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

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF‑файла, который будет преобразован
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).
1. Конвертируйте PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPdfToJpg{0:D2}.jpg". Где {0:D2} обозначает номер страницы в двухсимвольном формате. Изображения сохраняются с разрешением 150 DPI. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to JPG with template "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
  console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в TIFF онлайн**

Aspose.PDF for Node.js представляет вам онлайн бесплатное приложение ["PDF в TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF конвертация PDF в TIFF с бесплатным приложением](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Конвертируйте PDF в TIFF

Если вы хотите конвертировать PDF-документ, вы можете использовать [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы выполнить конвертацию в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF‑файла, который будет конвертирован.
1. Вызовите `AsposePdf` как Promise и выполните операцию конвертации файла. Получите объект при успешном выполнении.
1. Вызовите функцию [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/).
1. Преобразуйте PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPdfToTiff{0:D2}.tiff". Где {0:D2} представляет номер страницы в двузначном формате. Изображения сохраняются с разрешением 150 DPI. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле возникает ошибка, информация об ошибке будет содержаться в 'json.errorText'.

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

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF‑файла, который будет преобразован
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/).
1. Преобразуйте PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPdfToTiff{0:D2}.tiff". Где {0:D2} представляет номер страницы в двузначном формате. Изображения сохраняются с разрешением 150 DPI. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле возникает ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to TIFF with template "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
  console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в PNG онлайн**

В качестве примера того, как работают наши бесплатные приложения, пожалуйста, проверьте следующую функцию.

Aspose.PDF for Node.js представляет вам онлайн бесплатное приложение ["PDF в PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), где вы можете попробовать исследовать функциональность и качество его работы.

[![Как конвертировать PDF в PNG с помощью бесплатного приложения](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Преобразуйте PDF в PNG

Если вы хотите конвертировать PDF-документ, вы можете использовать [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы выполнить конвертацию в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF‑файла, который будет конвертирован.
1. Вызовите `AsposePdf` как Promise и выполните операцию конвертации файла. Получите объект при успешном выполнении.
1. Вызовите функцию [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
1. Конвертируйте PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPdfToPng{0:D2}.png". Где {0:D2} представляет номер страницы в двухцифровом формате. Изображения сохраняются с разрешением 150 DPI. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

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

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF‑файла, который будет преобразован
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
1. Конвертируйте PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPdfToPng{0:D2}.png". Где {0:D2} представляет номер страницы в двухцифровом формате. Изображения сохраняются с разрешением 150 DPI. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to PNG with template "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
  console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в SVG онлайн**

Aspose.PDF for Node.js представляет вам онлайн бесплатное приложение ["PDF в SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в SVG с бесплатным приложением](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** — это семейство спецификаций XML‑основного файлового формата для двумерной векторной графики, как статической, так и динамической (интерактивной или анимированной). Спецификация SVG является открытым стандартом, разрабатываемым консорциумом World Wide Web Consortium (W3C) с 1999 года.

## Преобразуйте PDF в SVG

### Конвертируйте PDF в классический SVG

Если вы хотите конвертировать PDF-документ, вы можете использовать [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы выполнить конвертацию в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF‑файла, который будет конвертирован.
1. Вызовите `AsposePdf` как Promise и выполните операцию конвертации файла. Получите объект при успешном выполнении.
1. Вызовите функцию [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
1. Конвертируйте PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPdfToSvg.svg". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

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

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF‑файла, который будет преобразован
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
1. Конвертируйте PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPdfToSvg.svg". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to SVG and save the "ResultPdfToSvg.svg"*/
  const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
  console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

### Преобразуйте PDF в zip-архив SVG

Если вы хотите конвертировать PDF-документ, вы можете использовать [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы выполнить конвертацию в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF‑файла, который будет конвертирован.
1. Вызовите `AsposePdf` как Promise и выполните операцию конвертации файла. Получите объект при успешном выполнении.
1. Вызовите функцию [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
1. Конвертируйте PDF‑файл. Таким образом, если ‘json.errorCode’ равно 0, результат операции сохраняется в «ResultPdfToSvgZip.zip». Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в ‘json.errorText’.

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

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF‑файла, который будет преобразован
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
1. Конвертируйте PDF‑файл. Таким образом, если ‘json.errorCode’ равно 0, результат операции сохраняется в «ResultPdfToSvgZip.zip». Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*convert a PDF-file to SVG zip and save the "ResultPdfToSvgZip.zip"*/
  const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
  console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText)
```

## Конвертируйте PDF в DICOM

Если вы хотите конвертировать PDF-документ, вы можете использовать [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы выполнить конвертацию в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF‑файла, который будет конвертирован.
1. Вызовите `AsposePdf` как Promise и выполните операцию конвертации файла. Получите объект при успешном выполнении.
1. Вызовите функцию [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
1. Преобразуйте PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfToDICOM{0:D2}.dcm". Где {0:D2} представляет номер страницы в двухзначном формате. Изображения сохраняются с разрешением 150 DPI. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

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

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF‑файла, который будет преобразован
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
1. Преобразуйте PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfToDICOM{0:D2}.dcm". Где {0:D2} представляет номер страницы в двухзначном формате. Изображения сохраняются с разрешением 150 DPI. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to DICOM with template "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
  console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

## Конвертируйте PDF в BMP

Если вы хотите конвертировать PDF-документ, вы можете использовать [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы выполнить конвертацию в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF‑файла, который будет конвертирован.
1. Вызовите `AsposePdf` как Promise и выполните операцию конвертации файла. Получите объект при успешном выполнении.
1. Вызовите функцию [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/).
1. Конвертируйте PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в \"ResultPdfToBmp{0:D2}.bmp\". Где {0:D2} представляет номер страницы в двухзначном формате. Изображения сохраняются с разрешением 150 DPI. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

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

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF‑файла, который будет преобразован
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/).
1. Конвертируйте PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в \"ResultPdfToBmp{0:D2}.bmp\". Где {0:D2} представляет номер страницы в двухзначном формате. Изображения сохраняются с разрешением 150 DPI. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to BMP with template "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
  console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```





