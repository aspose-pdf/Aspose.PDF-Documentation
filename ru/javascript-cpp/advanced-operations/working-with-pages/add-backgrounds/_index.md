---
title: Добавить фон в PDF с помощью JavaScript через C++
linktitle: Добавить фоны
type: docs
weight: 10
url: ru/javascript-cpp/add-backgrounds/
description: Добавьте фоновое изображение в ваш PDF файл с помощью JavaScript через C++.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Следующие фрагменты кода показывают, как добавить фоновое изображение на страницы PDF, используя функцию [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddbackgroundimage/) с JavaScript.

В следующем фрагменте кода мы загружаем изображение для дальнейшей работы во внутреннюю файловую систему:

1. Создайте 'FileReader'.
1. Установите имя файла изображения.
1. Подготовьте файл изображения из BLOB.

```js

  var ffileImage = function (e) {
    const file_reader = new FileReader();
    /*установите имя файла изображения*/
    fileBackgroundImage = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*подготовьте(сохраните) файл изображения из BLOB*/
      AsposePdfPrepare(event.target.result, fileBackgroundImage);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


In the next example, we select the PDF file to handle.  
1. Создайте 'FileReader'.  
1. Выполняется функция [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddbackgroundimage/).  
1. Добавьте файл изображения в PDF и сохраните как "ResultBackgroundImage.pdf".  
1. Далее, если 'json.errorCode' равен 0, вашему DownloadFile присваивается имя, указанное вами ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле возникнет ошибка, то информация об этой ошибке будет содержаться в файле 'json.errorText'.  
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет скачать полученный файл на операционную систему пользователя.  

```js

  var ffileAddBackgroundImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*добавить файл фонового изображения в PDF и сохранить как "ResultBackgroundImage.pdf"*/
      const json = AsposePdfAddBackgroundImage(event.target.result, e.target.files[0].name, fileBackgroundImage, "ResultBackgroundImage.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*создать ссылку для скачивания результирующего файла*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


## Использование Web Workers

```js

    /*Создать Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ? 
          `Результат:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            'изображение подготовлено!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Ошибка: ${evt.data.json.errorText}`;

    /*Установить имя файла по умолчанию: 'Aspose.jpg' уже загружено, см. настройки в 'settings.json'*/
    var fileBackgroundImage = "Aspose.jpg";

    /*Обработчик события*/
    const ffileAddBackgroundImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Добавить фоновое изображение в PDF-файл и сохранить как "ResultBackgroundImage.pdf" - запросить Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddBackgroundImage',
            "params": [event.target.result, e.target.files[0].name, fileBackgroundImage, "ResultBackgroundImage.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*Установить имя файла изображения*/
      fileBackgroundImage = e.target.files[0].name;
      file_reader.onload = event => {
        /*Сохранить BLOB в память FS для обработки*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
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