---  
title: Добавление изображений штампов в PDF на Node.js  
linktitle: Изображения штампов в PDF файле  
type: docs  
weight: 60  
url: ru/nodejs-cpp/stamping/  
description: Добавьте штамп изображения в ваш PDF документ с помощью AsposePdfAddStamp с использованием инструмента Node.js.  
lastmod: "2023-11-16"  
sitemap:  
    changefreq: "weekly"  
    priority: 0.7  
---  

## Добавление изображения штампа в PDF файл  

Штампование PDF документа похоже на штампование бумажного документа. Штамп в PDF файле предоставляет дополнительную информацию к PDF файлу, такую как защита PDF файла для использования другими и подтверждение безопасности содержимого PDF файла.  
Вы можете использовать функцию [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/) для добавления штампа изображения в PDF файл с помощью Node.js.  

Пожалуйста, ознакомьтесь со следующим фрагментом кода, чтобы добавить штамп изображения в PDF файл в среде Node.js.  

**CommonJS:**  

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.

1. Укажите имя PDF-файла, в который будет добавлена штамп-изображение.
1. Вызовите `AsposePdf` как Promise и выполните операцию добавления штампа-изображения. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. Добавьте штамп в PDF-файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultImage.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Добавить штамп в PDF-файл и сохранить как "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
      console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF файла, в который будет добавлена штамп-изображение.
1. Инициализируйте модуль AsposePdf. Получите объект при успешной инициализации.
1. Вызовите функцию [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. Добавьте штамп в PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultImage.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  /*Добавить штамп в PDF файл и сохранить "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
  console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```