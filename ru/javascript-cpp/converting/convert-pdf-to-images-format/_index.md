---
title: Convert PDF to Image Formats in JavaScript
linktitle: Convert PDF to Images
type: docs
weight: 70
url: ru/javascript-cpp/convert-pdf-to-images-format/
lastmod: "2023-11-01"
description: Эта тема покажет вам, как использовать Aspose.PDF для конвертации PDF в различные форматы изображений, такие как TIFF, BMP, JPEG, PNG, SVG, с помощью нескольких строк кода.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## JavaScript Конвертация PDF в Изображение

В этой статье мы покажем вам варианты конвертации PDF в форматы изображений.

Ранее отсканированные документы часто сохраняются в формате файла PDF. Однако, нужно ли вам редактировать его в графическом редакторе или отправить дальше в формате изображения? У нас есть универсальный инструмент для вас, чтобы конвертировать PDF в изображения с использованием 
Наиболее распространенная задача, когда вам нужно сохранить весь PDF-документ или некоторые конкретные страницы документа в виде набора изображений. **Aspose для JavaScript через C++** позволяет вам конвертировать PDF в форматы JPG и PNG, чтобы упростить шаги, необходимые для получения ваших изображений из конкретного PDF-файла.

**Aspose.PDF для JavaScript через C++** поддерживает конвертацию PDF в различные форматы изображений.
 Пожалуйста, проверьте раздел [Aspose.PDF Поддерживаемые Форматы Файлов](https://docs.aspose.com/pdf/javascript-cpp/supported-file-formats/).

Операция преобразования зависит от количества страниц в документе и может быть очень времязатратной. Поэтому мы настоятельно рекомендуем использовать Web Workers.

Этот код демонстрирует способ разгрузить ресурсоемкие задачи по преобразованию PDF файлов в web worker, чтобы предотвратить блокировку основного потока пользовательского интерфейса. Он также предлагает удобный способ загрузки преобразованного файла.

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в JPEG онлайн**

Aspose.PDF для JavaScript предлагает вам онлайн бесплатное приложение ["PDF to JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF конвертация PDF в JPEG с бесплатным приложением](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## Преобразование PDF в JPEG

```js

  /*Создать Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ? 
          `Количество файлов(страниц): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/jpeg", element) ) ?? ""}` : 
          `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик событий*/
    const ffileToJpg = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'owner';
        /*преобразовать PDF файл в jpg-файлы с шаблоном "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), разрешение 150 DPI и сохранить - Запросить Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToJpg', "params": [event.target.result, e.target.files[0].name, "ResultPdfToJpg{0:D2}.jpg", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Code snippet]

    /*создать ссылку для загрузки результирующего файла*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Нажмите здесь, чтобы загрузить файл " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```

The following JavaScript code snippet shows simple example of coverting PDF pages into Jpeg files:

1. Выберите PDF файл для конвертации.
1. Создайте 'FileReader'.
1. Функция [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfpagestojpg/) выполняется.
1. Устанавливается имя результирующего файла, в этом примере "ResultPdfToJpg{0:D2}.jpg".
1. Далее, если 'json.errorCode' равен 0, то ваш результирующий файл получает имя, которое вы указали ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация об этой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет скачать результирующий файл на операционную систему пользователя.

```js

  var ffileToJpg = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*конвертировать PDF файл в jpg-файлы с шаблоном "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), разрешение 150 DPI и сохранить*/
      const json = AsposePdfPagesToJpg(event.target.result, e.target.files[0].name, "ResultPdfToJpg{0:D2}.jpg", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "Количество файлов(страниц): " + json.filesCount.toString();
        /*создать ссылки на результирующие файлы*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/jpeg");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```


{{% alert color="success" %}}
**Попробуйте конвертировать PDF в TIFF онлайн**

Aspose.PDF для JavaScript предлагает вам бесплатное онлайн-приложение ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF конвертация PDF в TIFF с бесплатным приложением](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Конвертировать PDF в TIFF

```js

  /*Создать Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ? 
          `Количество файлов(страниц): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/tiff", element) ) ?? ""}` : 
          `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик событий*/
    const ffileToTiff = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Конвертировать PDF-файл в TIFF с шаблоном "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), разрешение 150 DPI и сохранить - Запросить у Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToTiff', "params": [event.target.result, e.target.files[0].name, "ResultPdfToTiff{0:D2}.tiff", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Создать ссылку для загрузки итогового файла*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Нажмите здесь, чтобы скачать файл " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


The following JavaScript code snippet shows simple example of coverting PDF pages into Tiff files:

1. Выберите PDF файл для конвертации.
1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestotiff/).
1. Устанавливается имя результирующего файла, в этом примере "ResultPdfToTiff{0:D2}.tiff".
1. Далее, если 'json.errorCode' равно 0, то вашему DownloadFile будет присвоено имя, которое вы указали ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет скачать результирующий файл в операционную систему пользователя.

```js

    var ffileToTiff = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Преобразование PDF-файла в TIFF с шаблоном "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), разрешение 150 DPI и сохранение*/
        const json = AsposePdfPagesToTiff(event.target.result, e.target.files[0].name, "ResultPdfToTiff{0:D2}.tiff", 150);
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "Количество файлов(страниц): " + json.filesCount.toString();
          /*Создание ссылок на результирующие файлы*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/tiff");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


{{% alert color="success" %}}
**Попробуйте конвертировать PDF в PNG онлайн**

В качестве примера того, как работают наши бесплатные приложения, пожалуйста, ознакомьтесь со следующей функцией.

Aspose.PDF для JavaScript предлагает вам бесплатное онлайн-приложение ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), где вы можете попробовать исследовать функциональность и качество его работы.

[![Как конвертировать PDF в PNG, используя бесплатное приложение](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Конвертировать PDF в PNG

```js

  /*Создать Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ? 
          `Количество файлов (страниц): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/png", element) ) ?? ""}` : 
          `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик события*/
    const ffileToPng = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'owner';
        /*конвертировать PDF файл в png-файлы с шаблоном "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), разрешение 150 DPI и сохранить - Запросить Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToPng', "params": [event.target.result, e.target.files[0].name, "ResultPdfToPng{0:D2}.png", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Фрагмент кода]

    /*создать ссылку для загрузки результирующего файла*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Щелкните здесь, чтобы загрузить файл " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


The following JavaScript code snippet shows simple example of coverting PDF pages into PNG files:

1. Выберите PDF файл для конвертации.
1. Создайте 'FileReader'.
1. Функция [AsposePdfPagesToPng](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfpagestopng/) выполняется.
1. Устанавливается имя результирующего файла, в этом примере "ResultPdfToPng{0:D2}.png".
1. Далее, если 'json.errorCode' равен 0, то вашему DownloadFile присваивается имя, указанное вами ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.
1. В результате, функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет скачать полученный файл в операционную систему пользователя.

```js

  var ffileToPng = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*конвертировать PDF файл в png-файлы с шаблоном "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), разрешение 150 DPI и сохранить*/
      const json = AsposePdfPagesToPng(event.target.result, e.target.files[0].name, "ResultPdfToPng{0:D2}.png", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "Количество файлов(страниц): " + json.filesCount.toString();
        /*создать ссылки на файлы результата*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/png");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```


{{% alert color="success" %}}
**Попробуйте преобразовать PDF в SVG онлайн**

Aspose.PDF для JavaScript предлагает вам бесплатное онлайн-приложение ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), где вы можете попробовать исследовать функциональность и качество работы.

[![Aspose.PDF Конвертация PDF в SVG с бесплатным приложением](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** — это семейство спецификаций формата файлов на основе XML для двумерной векторной графики, как статической, так и динамической (интерактивной или анимированной). Спецификация SVG является открытым стандартом, который разрабатывается Консорциумом Всемирной паутины (W3C) с 1999 года.

## Преобразование PDF в SVG

```js

  /*Создать Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ? 
          `Количество файлов(страниц): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/svg", element) ) ?? ""}` : 
          `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик событий*/
    const ffileToSvg = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Преобразовать PDF-файл в SVG - запрос к Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToSvg', "params": [event.target.result, e.target.files[0].name, "ResultPdfToSvg.svg"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Создать ссылку для загрузки результирующего файла*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Нажмите здесь, чтобы скачать файл " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


The following JavaScript code snippet shows simple example of coverting PDF pages into SVG files:

1. Выберите PDF файл для преобразования.
1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestosvg/).
1. Устанавливается имя результирующего файла, в этом примере "ResultPdfToSvg.svg".
1. Далее, если 'json.errorCode' равно 0, то вашему DownloadFile присваивается ранее указанное имя. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.
1. В результате, функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет скачать результирующий файл на операционную систему пользователя.

```js

    var ffileToSvg = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Преобразование PDF-файла в SVG*/
        const json = AsposePdfPagesToSvg(event.target.result, e.target.files[0].name, "ResultPdfToSvg.svg");
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "Количество файлов(страниц): " + json.filesCount.toString();
          /*Создание ссылок на результативные файлы*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/svg");
        }
        else document.getElementById('output').textContent = json.errorText;
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


### Конвертировать PDF в архивированный SVG

```js

  /*Создать Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ? `Результат:\n${DownloadFile(evt.data.json.fileNameResult, "application/zip", evt.data.params[0])}` : `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик событий*/
    const ffileToSvgZip = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Конвертировать PDF-файл в SVG(архив) и сохранить как "ResultPdfToSvgZip.zip" - Запрос к Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToSvgZip', "params": [event.target.result, e.target.files[0].name, "ResultPdfToSvgZip.zip"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Создать ссылку для загрузки файла результата*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Нажмите здесь, чтобы скачать файл " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


Следующий фрагмент кода JavaScript демонстрирует простой пример преобразования страниц PDF в файлы SVG(zip):

1. Выберите PDF файл для конвертации.
1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestosvgzip/).
1. Устанавливается имя полученного файла, в данном примере "ResultPdfToSvgZip.zip".
1. Далее, если 'json.errorCode' равен 0, то вашему DownloadFile присваивается имя, которое вы указали ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет загрузить полученный файл в операционную систему пользователя.

```js

    var ffileToSvgZip = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Преобразование PDF-файла в SVG(zip) и сохранение "ResultPdfToSvgZip.zip"*/
        const json = AsposePdfPagesToSvgZip(event.target.result, e.target.files[0].name, "ResultPdfToSvgZip.zip");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Создать ссылку для загрузки результирующего файла*/
        DownloadFile(json.fileNameResult, "application/zip");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


## Преобразование PDF в DICOM

```js

  /*Создать Web Worker*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? 'загружено!' :
      (evt.data.json.errorCode == 0) ?
        `Количество файлов(страниц): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
          (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "application/dicom", element) ) ?? ""}` :
        `Ошибка: ${evt.data.json.errorText}`;

  /*Обработчик событий*/
  const ffileToDICOM = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*Преобразовать PDF-файл в DICOM с шаблоном "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), разрешение 150 DPI и сохранить - запрос к Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToDICOM', "params": [event.target.result, e.target.files[0].name, "ResultPdfToDICOM{0:D2}.dcm", 150] }, [event.target.result]);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

  /*Создать ссылку для скачивания результирующего файла*/
  const DownloadFile = (filename, mime, content) => {
      mime = mime || "application/octet-stream";
      var link = document.createElement("a"); 
      link.href = URL.createObjectURL(new Blob([content], {type: mime}));
      link.download = filename;
      link.innerHTML = "Нажмите здесь, чтобы скачать файл " + filename;
      document.body.appendChild(link); 
      document.body.appendChild(document.createElement("br"));
      return filename;
    }
```


The following JavaScript code snippet shows simple example of coverting PDF pages into DICOM files:

1. Выберите PDF файл для конвертации.
1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestodicom/).
1. Устанавливается имя результирующего файла, в этом примере "ResultPdfToDICOM{0:D2}.dcm".
1. Далее, если 'json.errorCode' равен 0, то вашему результирующему файлу присваивается имя, которое вы указали ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.
1. В результате, функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет загрузить результирующий файл в операционную систему пользователя.

```js

  var ffileToDICOM = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Конвертировать PDF-файл в DICOM с шаблоном "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), разрешение 150 DPI и сохранить*/
      const json = AsposePdfPagesToDICOM(event.target.result, e.target.files[0].name, "ResultPdfToDICOM{0:D2}.dcm", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "Количество файлов(страниц): " + json.filesCount.toString();
        /*Создать ссылки на результирующие файлы*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "application/dicom");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


## Преобразование PDF в BMP

```js

    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ? 
          `Количество файлов (страниц): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/bmp", element) ) ?? ""}` : 
          `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик событий*/
    const ffileToBmp = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Преобразовать PDF-файл в BMP с шаблоном "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), разрешение 150 DPI и сохранить - запрос к Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToBmp', "params": [event.target.result, e.target.files[0].name, "ResultPdfToBmp{0:D2}.bmp", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Создать ссылку для загрузки результирующего файла*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Нажмите здесь, чтобы скачать файл " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


Следующий фрагмент кода JavaScript показывает простой пример преобразования страниц PDF в файлы BMP:

1. Выберите PDF файл для конвертации.
1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestobmp/).
1. Устанавливается имя результирующего файла, в этом примере "ResultPdfToBmp{0:D2}.bmp".
1. Далее, если 'json.errorCode' равен 0, то ваш DownloadFile получает имя, которое вы указали ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация об этой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет скачать результирующий файл на операционную систему пользователя.

```js

    var ffileToBmp = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Преобразовать PDF-файл в BMP с шаблоном "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), разрешение 150 DPI и сохранить*/
        const json = AsposePdfPagesToBmp(event.target.result, e.target.files[0].name, "ResultPdfToBmp{0:D2}.bmp", 150);
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "Количество файлов(страниц): " + json.filesCount.toString();
          /*Создать ссылки на результативные файлы*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/bmp");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```