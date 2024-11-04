---
title: Добавление цифровой подписи или цифровая подпись PDF в JavaScript через C++
linktitle: Цифровая подпись PDF
type: docs
weight: 70
url: /javascript-cpp/sign-pdf/
description: Цифровая подпись PDF документов с использованием JavaScript через C++.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Цифровая подпись в PDF-документе — это способ проверки подлинности и целостности документа. Это процесс электронной подписи PDF-документа с использованием закрытого ключа и цифрового сертификата. Эта подпись гарантирует держателю, что документ не был изменен или изменен после подписания и что подписант является тем, кем он утверждает себя. Чтобы подписать PDF с помощью JavaScript, используйте инструмент Aspose.PDF.

Aspose.PDF для JavaScript через C++ поддерживает возможность цифровой подписи PDF-файлов с использованием [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfsignpkcs7/).

## Подписание PDF с цифровыми подписями

```js

    /*Установить имя файла ключа по умолчанию PKCS7*/
    var fileSign = "/test.pfx";

    var ffileSign = function (e) {
      const file_reader = new FileReader();
      /*Установить имя файла ключа PKCS7*/
      fileImage = e.target.files[0].name;
      file_reader.onload = (event) => {
        /*Сохранить BLOB в памяти FS для обработки*/
        AsposePdfPrepare(event.target.result, fileSign);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Установить имя файла изображения по умолчанию (Appearance подписи)*/
    var signatureAppearance = "/Aspose.jpg";

    var ffileImage = function (e) {
      const file_reader = new FileReader();
      /*Установить имя файла изображения*/
      signatureAppearance = e.target.files[0].name;
      file_reader.onload = (event) => {
        /*Сохранить BLOB в памяти FS для обработки*/
        AsposePdfPrepare(event.target.result, signatureAppearance);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    var ffileSignPKCS7 = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        let pswSign = document.getElementById("passwordSign").value;
        /*Подписать PDF-файл с цифровыми подписями и сохранить как "ResultSignPKCS7.pdf"*/
        const json = AsposePdfSignPKCS7(event.target.result, e.target.files[0].name, 1, fileSign, pswSign, 200, 200, 200, 100, "TEST", "test@test.com", "EU", 1, signatureAppearance,"ResultSignPKCS7.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Создать ссылку для загрузки результирующего файла*/
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
      (evt.data == 'ready') ? 'загружено!' :
        (evt.data.json.errorCode == 0) ?
          `Результат:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            'файл подготовлен!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Ошибка: ${evt.data.json.errorText}`;

    /*Установить имя файла ключа PKCS7 по умолчанию*/
    var fileSign = "test.pfx";
    /*Установить имя файла изображения (вид подписи) по умолчанию: 'Aspose.jpg' уже загружено, см. настройки в 'settings.json'*/
    var signatureAppearance = "Aspose.jpg";

    /*Обработчик события*/
    const ffileSignPKCS7 = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const pageNum = 1;
        const pswSign = document.getElementById("passwordSign").value;
        const setXIndent = 100;
        const setYIndent = 100;
        const setHeight = 200;
        const setWidth = 100;
        const reason = 'Причина';
        const contact = 'contact@test.com';
        const location = 'Местоположение';
        const isVisible = 1;
        /*Подписать PDF-файл цифровыми подписями и сохранить как "ResultSignPKCS7.pdf" - Запросить Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSignPKCS7',
            "params": [event.target.result, e.target.files[0].name, pageNum, fileSign, pswSign, setXIndent, setYIndent,
                      setHeight, setWidth, reason, contact, location, isVisible, signatureAppearance, "ResultSignPKCS7.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileSign = e => {
      const file_reader = new FileReader();
      /*Установить имя файла ключа PKCS7*/
      fileSign = e.target.files[0].name;
      file_reader.onload = event => {
        /*Сохранить BLOB в памяти FS для обработки*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, fileSign] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*Установить имя файла изображения*/
      signatureAppearance = e.target.files[0].name;
      file_reader.onload = event => {
        /*Сохранить BLOB в памяти FS для обработки*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, signatureAppearance] },
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