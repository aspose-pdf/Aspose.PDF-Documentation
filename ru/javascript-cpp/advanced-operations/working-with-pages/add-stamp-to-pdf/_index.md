---
title: Добавление изображений штампов в PDF с использованием JavaScript через C++
linktitle: Изображения штампов в PDF файле
type: docs
weight: 60
url: ru/javascript-cpp/stamping/
description: Добавьте изображение штампа в ваш PDF документ с помощью функции AsposePdfAddStamp и JavaScript.
lastmod: "2023-04-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Добавление изображения штампа в PDF файл

Штампование PDF документа похоже на штампование бумажного документа. Штамп в PDF файле предоставляет дополнительную информацию PDF файлу, такую как защита PDF файла для использования другими и подтверждение безопасности содержимого PDF файла. Вы можете использовать функцию [AsposePdfAddStamp](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddstamp/) для добавления изображения штампа в PDF файл с использованием JavaScript.

Чтобы добавить изображение штампа:

1. Установите имя файла изображения по умолчанию.
1. Создайте 'FileReader'.
1. Установите имя файла изображения.
1. Подготовьте файл штампа из BLOB.

Следующий фрагмент кода показывает, как добавить изображение штампа в PDF файл.

```js

  /*установить имя файла штампа по умолчанию*/
  var fileStamp = "/Aspose.jpg";

  var ffileStamp = function (e) {
    const file_reader = new FileReader();
    /*установить имя файла штампа*/
    fileStamp = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*подготовить(сохранить) файл штампа из BLOB*/
      AsposePdfPrepare(event.target.result, fileStamp);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


1. Создайте 'FileReader'.
1. Функция [AsposePdfAddStamp](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddstamp/) выполняется.
1. Добавьте изображение в конец PDF-файла и сохраните "ResultImage.pdf".
1. Далее, если 'json.errorCode' равен 0, то ваш DownloadFile получает имя, указанное вами ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле возникнет ошибка, то информация об этой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет скачать полученный файл в операционной системе пользователя.

```js
  var ffileAddStamp = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*вставить файл штампа в PDF-файл и сохранить "ResultImage.pdf"*/
      const json = AsposePdfAddStamp(event.target.result, e.target.files[0].name, fileStamp, 0, 5, 5, 40, 40, Module.Rotation.on270, 0.5, "ResultStamp.pdf");
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

    /*Установить имя файла штампа по умолчанию: 'Aspose.jpg' уже загружено, см. настройки в 'settings.json'*/
    var fileStamp = "Aspose.jpg";

    /*Обработчик событий*/
    const ffileAddStamp = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const setBackground = 0;
        const setXIndent_ = 5;
        const setYIndent_ = 5;
        const setHeight_ = 40;
        const setWidth_ = 40;
        const rotation_ = 'Module.Rotation.on270';
        const setOpacity = 0.5;
        /*Добавить штамп в PDF-файл и сохранить как "ResultStamp.pdf" - запросить Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddStamp',
            "params": [event.target.result, e.target.files[0].name, fileStamp, setBackground, setXIndent_, setYIndent_,
                      setHeight_, setWidth_, rotation_, setOpacity, "ResultStamp.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileStamp = e => {
      const file_reader = new FileReader();
      /*Установить имя файла штампа*/
      fileStamp = e.target.files[0].name;
      file_reader.onload = event => {
        /*Сохранить BLOB в памяти FS для обработки*/
        AsposePDFWebWorker.postMessage(
            { "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] },
            [event.target.result]
        );
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