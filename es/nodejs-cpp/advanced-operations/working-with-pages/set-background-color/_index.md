---
title: Establecer el color de fondo para PDF en Node.js
linktitle: Establecer color de fondo
type: docs
weight: 80
url: /es/nodejs-cpp/set-background-color/
description: Establecer el color de fondo para su archivo PDF con Node.js vía C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

En caso de que desee establecer el color de fondo del PDF, puede usar [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/) función. 

Por favor, revise el siguiente fragmento de código para establecer el color de fondo del PDF en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifique el nombre del archivo PDF cuyo color de fondo desea establecer.
1. Llamar `AsposePdf` como Promise y realiza la operación para establecer el color de fondo. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/). 
1. Establezca el color de fondo para el archivo PDF. Necesita pasar 3 argumentos a esta función: un nombre de archivo de entrada, un color deseado en forma hexadecimal y un nombre de archivo de salida. Así, si ‘json.errorCode’ es 0, el resultado de la operación se guarda en “ResultRotation.pdf”. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set the background color for the PDF-file and save the "ResultPdfSetBackgroundColor.pdf"*/
      const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
      console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF cuyo color de fondo desea establecer.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/). 
1. Establezca el color de fondo para el archivo PDF. El color de fondo se establece en "#426bf4," que es un código de color hexadecimal que representa un tono de azul. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultRotation.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set the background color for the PDF-file and save the "ResultPdfSetBackgroundColor.pdf"*/
  const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
  console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```