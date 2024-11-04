---
title: Добавить изображение в PDF с использованием JavaScript через C++
linktitle: Добавить изображение
type: docs
weight: 10
url: /javascript-cpp/add-image-to-pdf/
description: Этот раздел описывает, как добавить изображение в существующий PDF файл с помощью Aspose.PDF для JavaScript через C++.
lastmod: "2023-12-15"
---

## Добавить изображение в существующий PDF файл

Вам нужно прикрепить изображение к PDF? Хотите улучшить читаемость вашего PDF? Добавьте изображения в ваш PDF, и ваша презентация или резюме будет выглядеть более презентабельно.

Считается, что добавление изображений в PDF файлы требует сложного специального инструмента. Однако с помощью Aspose.PDF для JavaScript вы можете быстро и легко добавить необходимые изображения в PDF, используя JavaScript прямо в вашем браузере.

Чтобы добавить изображение в существующий PDF файл:

1. Установите имя файла изображения по умолчанию.
1. Создайте 'FileReader'.
1. Установите имя файла изображения.
1. Подготовьте файл изображения из BLOB.
1. Выполняется функция [AsposePdfAddImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddimage/).

1. Добавьте файл изображения в конец PDF-файла и сохраните "ResultImage.pdf".
1. Далее, если 'json.errorCode' равен 0, то ваш DownloadFile получает имя, указанное ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет загрузить полученный файл на операционную систему пользователя.

Следующий фрагмент кода показывает, как добавить изображение в PDF-документ.

```js

  /*установить имя файла изображения по умолчанию*/
  var fileImage = "/Aspose.jpg";

  var ffileImage = function (e) {
    const file_reader = new FileReader();
    /*установить имя файла изображения*/
    fileImage = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*подготовить(сохранить) файл изображения из BLOB*/
      AsposePdfPrepare(event.target.result, fileImage);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

В следующем примере мы выбираем изображение для обработки:

```js

  var ffileAddImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*добавить файл изображения в конец PDF-файла и сохранить как "ResultImage.pdf"*/
      const json = AsposePdfAddImage(event.target.result, e.target.files[0].name, fileImage, "ResultImage.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*создать ссылку для загрузки результирующего файла*/
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

    /*Установить имя файла изображения по умолчанию: 'Aspose.jpg' уже загружено, см. настройки в 'settings.json'*/
    var fileImage = "Aspose.jpg";

    /*Обработчик события*/
    const ffileAddImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Добавить изображение в конец PDF-файла и сохранить как "ResultImage.pdf" - Запрос к Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddImage',
            "params": [event.target.result, e.target.files[0].name, fileImage, "ResultImage.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*Установить имя файла изображения*/
      fileImage = e.target.files[0].name;
      file_reader.onload = event => {
        /*Сохранить BLOB в памяти для обработки*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
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