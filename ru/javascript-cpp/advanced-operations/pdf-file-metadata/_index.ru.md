---
title: Работа с метаданными PDF файла с использованием JavaScript через C++
linktitle: Метаданные PDF файла
type: docs
weight: 130
url: /javascript-cpp/pdf-file-metadata/
description: Этот раздел объясняет, как получить информацию о PDF файле, как получить метаданные из PDF файла, установить информацию о PDF файле.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Получение информации о PDF файле

1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfGetInfo](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetinfo/).
1. Метаданные PDF, которые можно получить:
- title - название
- creator - создатель
- author - автор
- subject - тема
- keywords - ключевые слова
- creation - дата создания
- mod - дата изменения
1. Далее, если 'json.errorCode' равен 0, то вы можете получить список информации о PDF файле. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.

```js

  var ffilePdfGetInfo = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Получение информации (метаданных) из PDF файла.*/
      const json = AsposePdfGetInfo(event.target.result, e.target.files[0].name);
      /* JSON
      title - название
      creator - создатель
      author - автор
      subject - тема
      keywords - ключевые слова
      format - формат PDF
      version - версия PDF
      ispdfa - PDF является PDF/A
      ispdfua - PDF является PDF/UA
      islinearized - PDF линеаризован
      isencrypted - PDF зашифрован
      permission - разрешение PDF
      size - размер страницы PDF
      pagecount - количество страниц
      сreation Date: json.creation
      modify Date:   json.mod
      annotationcount - количество аннотаций
      bookmarkcount - количество закладок
      attachmentcount - количество вложений
      metadatacount - количество метаданных
      javascriptcount - количество JavaScript
      imagecount - количество изображений
      */
      if (json.errorCode == 0) document.getElementById('output').textContent = "JSON:\n" + JSON.stringify(json, null, 4);
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


### Использование Web Workers

```js

    /*Создать Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ?
          `информация:\n${JSON.stringify(evt.data.json, null, 4)}` :
          `Ошибка: ${evt.data.json.errorText}`; 

    /*Обработчик событий*/
    const ffilePdfGetInfo = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Получить информацию (метаданные) из PDF-файла - запросить Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfGetInfo', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## Получить все шрифты

Получение шрифтов из PDF-файла может быть полезным способом повторного использования шрифтов в других документах или приложениях.
 
В случае, если вы хотите получить все шрифты из PDF документа, вы можете использовать [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetallfonts/). Пожалуйста, ознакомьтесь со следующим фрагментом кода, чтобы получить все шрифты из существующего PDF документа, используя JavaScript через C++.

1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetallfonts/).
1. Далее, если 'json.errorCode' равен 0, тогда вы можете получить список шрифтов из PDF файла. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.

```js

  var ffilePdfGetAllFonts = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*получить список шрифтов из PDF файла.*/
      const json = AsposePdfGetAllFonts(event.target.result, e.target.files[0].name);
      if (json.errorCode == 0) document.getElementById('output').textContent = "JSON:\n" + JSON.stringify(json, null, 4);
      else document.getElementById('output').textContent = json.errorText;
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
          `шрифты:\n${JSON.stringify(evt.data.json.fonts, null, 4)}` :
          `Ошибка: ${evt.data.json.errorText}`; 

    /*Обработчик события*/
    const ffilePdfGetAllFonts = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Получить список шрифтов PDF-файла - Запросить Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfGetAllFonts', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```
## Установка информации о PDF файле

Aspose.PDF для JavaScript через C++ позволяет задавать специфичную для файла информацию для PDF, такую как автор, дата создания, тема и заголовок.
 Чтобы установить эту информацию:

1. Создайте 'FileReader'.
1. Если не нужно устанавливать значение, используйте undefined или "" (пустую строку).
1. Выполняется функция [AsposePdfSetInfo](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfsetinfo/).
1. Устанавливается имя результирующего файла, в этом примере "ResultSetInfo.pdf".
1. Далее, если 'json.errorCode' равен 0, то вашему DownloadFile присваивается имя, указанное вами ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет вам скачать результирующий файл на операционную систему пользователя.

```js

    var ffilePdfSetInfo = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Установите информацию PDF: заголовок, создатель, автор, тема, ключевые слова, создание (дата), модификация (дата изменения)*/
        /*Если не нужно устанавливать значение, используйте undefined или "" (пустую строку)*/
        /*Установите информацию (метаданные) в PDF-файл и сохраните "ResultSetInfo.pdf"*/
        const json = AsposePdfSetInfo(event.target.result, e.target.files[0].name, "Установка информации о PDF-документе", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "16/02/2023 11:55 PM", "ResultSetInfo.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Создайте ссылку для скачивания результирующего файла*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

### Использование Web Workers

```js

    /*Создание Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ?
          `Результат:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик событий*/
    const ffilePdfSetInfo = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Информация о PDF: заголовок, создатель, автор, тема, ключевые слова, создание (дата), модификация (дата изменения)*/
        const title = 'Установка информации документа PDF';
        const creator = ''; /*если не нужно задавать значение, используйте: undefined или ""/'' (пустая строка)*/
        const author = 'Aspose';
        const subject = undefined;
        const keywords = 'Aspose.Pdf, DOM, API';
        const creation = undefined; /*дата создания*/
        const mod = '16/02/2023 11:55 PM'; /*дата изменения*/
        /*Установить информацию (метаданные) в PDF-файл и сохранить "ResultSetInfo.pdf" - запросить Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSetInfo',
            "params": [event.target.result, e.target.files[0].name, title, creator, author, subject, keywords, creation, mod, "ResultSetInfo.pdf"] },
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


## Удаление информации из PDF файла

Aspose.PDF для JavaScript через C++ позволяет удалять метаданные из PDF файла:

1. Создайте 'FileReader'.
1. Выполняется функция [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/javascript-cpp/metadata/asposepdfremovemetadata/).
1. Устанавливается имя результирующего файла, в этом примере "ResultPdfRemoveMetadata.pdf".
1. Далее, если 'json.errorCode' равен 0, тогда ваш DownloadFile получает имя, которое вы указали ранее. Если параметр 'json.errorCode' не равен 0 и, соответственно, в вашем файле будет ошибка, то информация о такой ошибке будет содержаться в файле 'json.errorText'.
1. В результате функция [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) генерирует ссылку и позволяет вам скачать результирующий файл на операционную систему пользователя.

```js

    var ffilePdfRemoveMetadata = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Удалить метаданные PDF-файла и сохранить "ResultPdfRemoveMetadata.pdf"*/
        const json = AsposePdfRemoveMetadata(event.target.result, e.target.files[0].name, "ResultPdfRemoveMetadata.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Создать ссылку для скачивания результирующего файла*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


### Использование Web Workers

```js

    /*Создать Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Ошибка от Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'загружен!' :
        (evt.data.json.errorCode == 0) ? `Результат:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Ошибка: ${evt.data.json.errorText}`;

    /*Обработчик событий*/
    const ffilePdfRemoveMetadata = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Удалить метаданные из PDF-файла и сохранить как "ResultPdfRemoveMetadata.pdf" - Запрос к Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfRemoveMetadata', "params": [event.target.result, e.target.files[0].name, "ResultPdfRemoveMetadata.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Фрагмент кода]

    /*Создать ссылку для загрузки файла с результатом*/
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