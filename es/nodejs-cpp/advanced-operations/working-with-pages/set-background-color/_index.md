---
title: Establecer el color de fondo para PDF en Node.js
linktitle: Establecer color de fondo
type: docs
weight: 80
url: es/nodejs-cpp/set-background-color/
description: Establecer el color de fondo para su archivo PDF con Node.js a través de C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

En caso de que desee establecer el color de fondo del PDF, puede utilizar la función [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/).

Por favor, revise el siguiente fragmento de código para establecer el color de fondo del PDF en el entorno Node.js.

**CommonJS:**

1. Llame a `require` e importe el módulo `asposepdfnodejs` como la variable `AsposePdf`.
1. Especifique el nombre del archivo PDF cuyo color de fondo desea establecer.
1. Llame a `AsposePdf` como una Promesa y realice la operación para establecer el color de fondo. Reciba el objeto si es exitoso.

1. Llame a la función [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/).
1. Establezca el color de fondo para el archivo PDF. Necesita pasar 3 argumentos a esta función: un nombre de archivo de entrada, un color deseado en forma hexadecimal y un nombre de archivo de salida. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultRotation.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Establezca el color de fondo para el archivo PDF y guarde el "ResultPdfSetBackgroundColor.pdf"*/
      const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
      console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF cuyo color de fondo deseas establecer.
1. Inicializa el módulo AsposePdf. Recibe el objeto si es exitoso.
1. Llama a la función [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/).
1. Establece el color de fondo para el archivo PDF. El color de fondo se establece en "#426bf4," que es un código de color hexadecimal que representa un tono de azul. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultRotation.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Establece el color de fondo para el archivo PDF y guarda el "ResultPdfSetBackgroundColor.pdf"*/
  const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
  console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```