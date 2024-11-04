---
title: Convert PDF to Image Formats in Node.js
linktitle: Convert PDF to Images
type: docs
weight: 70
url: /nodejs-cpp/convert-pdf-to-images-format/
lastmod: "2023-11-16"
description: This topic show you how to use Aspose.PDF to convert PDF to various images formats e.g. TIFF, BMP, JPEG, PNG, SVG with a few lines of code in the Node.js environment.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Node.js Convert PDF to Image

В этой статье мы покажем вам варианты преобразования PDF в форматы изображений.

Ранее отсканированные документы часто сохраняются в формате PDF. Однако, нужно ли вам отредактировать его в графическом редакторе или отправить его дальше в формате изображения? У нас есть универсальный инструмент для преобразования PDF в изображения, используя 
Наиболее распространенная задача — это когда вам нужно сохранить весь PDF-документ или некоторые конкретные страницы документа как набор изображений.
 **Aspose for Node.js через C++** позволяет конвертировать PDF в форматы JPG и PNG, упрощая шаги, необходимые для получения изображений из конкретного PDF-файла.

**Aspose.PDF для Node.js через C++** поддерживает различные преобразования форматов изображений из PDF. Пожалуйста, ознакомьтесь с разделом [Поддерживаемые форматы файлов Aspose.PDF](https://docs.aspose.com/pdf/nodejs-cpp/supported-file-formats/).

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в JPEG онлайн**

Aspose.PDF для Node.js предлагает вам бесплатное онлайн-приложение ["PDF to JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), где вы можете исследовать функциональность и качество работы.

[![Преобразование Aspose.PDF из PDF в JPEG с бесплатным приложением](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## Конвертация PDF в JPEG

Если вы хотите конвертировать PDF-документ, вы можете использовать функцию [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/). 

Пожалуйста, ознакомьтесь со следующим фрагментом кода для конвертации в среде Node.js.
**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF файла, который будет конвертирован.
1. Вызовите `AsposePdf` как Promise и выполните операцию по конвертации файла. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).
1. Конвертируйте PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfToJpg{0:D2}.jpg". Где {0:D2} представляет номер страницы в формате с двумя цифрами. Изображения сохраняются с разрешением 150 DPI. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Конвертировать PDF-файл в JPG с шаблоном "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), разрешение 150 DPI и сохранить*/
      const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
      console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите название PDF файла, который будет конвертирован.
1. Инициализируйте модуль AsposePdf. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).
1. Конвертируйте PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfToJpg{0:D2}.jpg". Где {0:D2} представляет номер страницы в двухзначном формате. Изображения сохраняются с разрешением 150 DPI. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле возникает ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Конвертировать PDF-файл в JPG с шаблоном "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), разрешение 150 DPI и сохранить*/
  const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
  console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


{{% alert color="success" %}}
**Попробуйте конвертировать PDF в TIFF онлайн**

Aspose.PDF для Node.js предлагает вам бесплатное онлайн-приложение ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), где вы можете попробовать изучить функциональность и качество работы.

[![Конвертация Aspose.PDF PDF в TIFF с бесплатным приложением](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Конвертация PDF в TIFF

Если вы хотите конвертировать PDF документ, вы можете использовать функцию [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/). 
Пожалуйста, ознакомьтесь с приведенным ниже фрагментом кода, чтобы конвертировать в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF файла, который будет конвертирован.
1. Вызовите `AsposePdf` как Promise и выполните операцию для конвертации файла. Получите объект в случае успешного выполнения.

1. Вызовите функцию [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/).
1. Конвертируйте PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfToTiff{0:D2}.tiff". Где {0:D2} представляет номер страницы в двухзначном формате. Изображения сохраняются с разрешением 150 DPI. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Преобразовать PDF-файл в TIFF с шаблоном "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), разрешение 150 DPI и сохранить*/
      const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
      console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF файла, который будет конвертирован.
1. Инициализируйте модуль AsposePdf. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/).
1. Конвертируйте PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfToTiff{0:D2}.tiff". Где {0:D2} представляет номер страницы в двухзначном формате. Изображения сохраняются с разрешением 150 DPI. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Преобразование PDF файла в TIFF с шаблоном "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), разрешение 150 DPI и сохранение*/
  const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
  console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


{{% alert color="success" %}}
**Попробуйте конвертировать PDF в PNG онлайн**

В качестве примера того, как работают наши бесплатные приложения, пожалуйста, ознакомьтесь со следующей функцией.

Aspose.PDF для Node.js предлагает вам бесплатное онлайн-приложение ["PDF в PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), где вы можете попробовать исследовать функциональность и качество работы.

[![Как конвертировать PDF в PNG с помощью бесплатного приложения](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Конвертировать PDF в PNG

Если вы хотите конвертировать PDF документ, вы можете использовать функцию [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/). 
Пожалуйста, ознакомьтесь со следующим фрагментом кода для конвертации в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF файла, который будет конвертирован.
1. Вызовите `AsposePdf` как Promise и выполните операцию конвертации файла. Получите объект в случае успеха.

1. Вызовите функцию [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
1. Конвертируйте PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfToPng{0:D2}.png". Где {0:D2} представляет собой номер страницы в двузначном формате. Изображения сохраняются с разрешением 150 DPI. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Преобразование PDF-файла в PNG с шаблоном "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), разрешение 150 DPI и сохранение*/
      const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
      console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF файла, который будет конвертирован.
1. Инициализируйте модуль AsposePdf. Получите объект в случае успешного выполнения.
1. Вызовите функцию [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
1. Конвертируйте PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfToPng{0:D2}.png". Где {0:D2} представляет номер страницы в двухзначном формате. Изображения сохраняются с разрешением 150 DPI. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Конвертируйте PDF-файл в PNG с шаблоном "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), разрешение 150 DPI и сохраните*/
  const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
  console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


{{% alert color="success" %}}
**Попробуйте онлайн-конвертацию PDF в SVG**

Aspose.PDF для Node.js предлагает вам бесплатное онлайн-приложение ["PDF в SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в SVG с бесплатным приложением](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** - это семейство спецификаций формата файлов на основе XML для двумерной векторной графики, как статической, так и динамической (интерактивной или анимированной). Спецификация SVG является открытым стандартом, который разрабатывается Консорциумом Всемирной паутины (W3C) с 1999 года.

## Конвертировать PDF в SVG

### Конвертировать PDF в классический SVG

Если вы хотите конвертировать PDF-документ, вы можете использовать функцию [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/). Пожалуйста, ознакомьтесь со следующим фрагментом кода, чтобы выполнить конвертацию в среде Node.js.


**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF файла, который будет конвертирован.
1. Вызовите `AsposePdf` как Promise и выполните операцию по конвертации файла. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
1. Конвертируйте PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfToSvg.svg". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Преобразовать PDF-файл в SVG и сохранить как "ResultPdfToSvg.svg"*/
      const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
      console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите название PDF-файла, который будет конвертирован.
1. Инициализируйте модуль AsposePdf. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
1. Преобразуйте PDF-файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPdfToSvg.svg". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Преобразование PDF-файла в SVG и сохранение в "ResultPdfToSvg.svg"*/
  const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
  console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

### Конвертация PDF в архивированный SVG

В случае, если вы хотите конвертировать PDF-документ, вы можете использовать функцию [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
 
Пожалуйста, проверьте следующий фрагмент кода для преобразования в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
2. Укажите имя PDF-файла, который будет преобразован.
3. Вызовите `AsposePdf` как Promise и выполните операцию по преобразованию файла. Получите объект в случае успеха.
4. Вызовите функцию [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
5. Преобразуйте PDF-файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfToSvgZip.zip". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Преобразуйте PDF-файл в SVG(zip) и сохраните в "ResultPdfToSvgZip.zip"*/
      const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
      console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF файла, который будет преобразован.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
1. Преобразуйте PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfToSvgZip.zip". Если параметр json.errorCode не равен 0 и, соответственно, в файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*преобразование PDF-файла в SVG zip и сохранение в "ResultPdfToSvgZip.zip"*/
  const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
  console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText)
```

## Преобразование PDF в DICOM

Если вы хотите преобразовать PDF документ, вы можете использовать функцию [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
 
Пожалуйста, ознакомьтесь со следующим фрагментом кода, чтобы выполнить преобразование в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF-файла, который будет преобразован.
1. Вызовите `AsposePdf` как Promise и выполните операцию по преобразованию файла. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
1. Преобразуйте PDF-файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfToDICOM{0:D2}.dcm". Где {0:D2} представляет номер страницы в двухзначном формате. Изображения сохраняются с разрешением 150 DPI. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Преобразуйте PDF-файл в DICOM с шаблоном "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), разрешение 150 DPI и сохраните*/
      const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
      console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF файла, который будет конвертирован.
1. Инициализируйте модуль AsposePdf. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
1. Конвертируйте PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfToDICOM{0:D2}.dcm". Где {0:D2} представляет номер страницы в двухзначном формате. Изображения сохраняются с разрешением 150 DPI. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Преобразуйте PDF-файл в DICOM с шаблоном "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), разрешение 150 DPI и сохраните*/
  const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
  console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


## Конвертировать PDF в BMP

Если вы хотите конвертировать PDF документ, вы можете использовать функцию [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/). Пожалуйста, изучите следующий фрагмент кода для выполнения преобразования в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
2. Укажите имя PDF файла, который будет конвертирован.
3. Вызовите `AsposePdf` как Promise и выполните операцию для конвертации файла. Получите объект в случае успеха.
4. Вызовите функцию [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/).

1. Конвертировать PDF файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPdfToBmp{0:D2}.bmp". Где {0:D2} представляет номер страницы в двухзначном формате. Изображения сохраняются с разрешением 150 DPI. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Преобразовать PDF-файл в BMP с шаблоном "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), разрешение 150 DPI и сохранить*/
      const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
      console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF файла, который будет преобразован.

1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/).
1. Конвертируйте PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfToBmp{0:D2}.bmp". Где {0:D2} представляет номер страницы в двухзначном формате. Изображения сохраняются с разрешением 150 DPI. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Конвертируйте PDF-файл в BMP с шаблоном "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), разрешение 150 DPI и сохраните*/
  const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
  console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```