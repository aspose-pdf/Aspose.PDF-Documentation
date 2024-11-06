---
title: Конвертировать PDF в PPTX на JavaScript
linktitle: Конвертировать PDF в PowerPoint
type: docs
weight: 30
url: ru/javascript-cpp/convert-pdf-to-powerpoint/
lastmod: "2023-11-01"
description: Aspose.PDF позволяет конвертировать PDF в формат PPTX с использованием JavaScript напрямую в вебе.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Операция конвертации зависит от количества страниц в документе и может быть очень долгой. Поэтому мы настоятельно рекомендуем использовать веб-воркеры.

Этот код демонстрирует способ разгрузки ресурсоемких задач по конвертации PDF-файлов на веб-воркер, чтобы предотвратить блокировку основного потока пользовательского интерфейса. Он также предлагает удобный способ загрузки конвертированного файла.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в PowerPoint онлайн**

Aspose.PDF для JavaScript представляет вам бесплатное онлайн-приложение ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в PPTX с бесплатным приложением](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## Конвертировать PDF в PPTX

```js

  /*Создать Web Worker*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? 'загружено!' :
      (evt.data.json.errorCode == 0) ? `Результат:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.presentationml.presentation", evt.data.params[0])}` : `Ошибка: ${evt.data.json.errorText}`;

  /*Обработчик событий*/
  const ffileToPptX = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*Конвертировать PDF-файл в PptX и сохранить как "ResultPDFtoPptX.pptx" - Запросить Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToPptX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoPptX.pptx"] }, [event.target.result]);
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


Следующий фрагмент кода JavaScript показывает простой пример преобразования PDF в файлы PPTX:

1. Выберите PDF файл для конвертации.
1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfToPptX](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftopptx/).
1. Устанавливается имя результирующего файла, в этом примере "ResultPDFtoPptX.pptx".
1. Далее, если 'json.errorCode' равен 0, то вашему результирующему файлу присваивается указанное ранее имя. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет загрузить результирующий файл в операционную систему пользователя.

```js

  var ffileToPptX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Преобразовать PDF-файл в PptX и сохранить как "ResultPDFtoPptX.pptx"*/
      const json = AsposePdfToPptX(event.target.result, e.target.files[0].name, "ResultPDFtoPptX.pptx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*Создать ссылку для загрузки результирующего файла*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.presentationml.presentation");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```