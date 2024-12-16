---
title: Añadir fondo a PDF en Node.js
linktitle: Añadir fondo
type: docs
weight: 10
url: /es/nodejs-cpp/add-background/
description: Añadir una imagen de fondo a su archivo PDF en Node.js
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Los siguientes fragmentos de código muestran cómo añadir una imagen de fondo a las páginas PDF usando la función [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/) en Node.js.

Por favor, revise el siguiente fragmento de código para añadir una imagen de fondo en el entorno de Node.js.

**CommonJS:**

1. Llama a `require` e importa el módulo `asposepdfnodejs` como la variable `AsposePdf`.
1. Especifica el nombre del archivo PDF al cual se le añadirá la imagen de fondo.
1. Llama a `AsposePdf` como Promesa y realiza la operación para añadir la imagen de fondo. Recibe el objeto si es exitoso.
1. Llama a la función [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/).

1. Agregar imagen de fondo a un archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultAddBackgroundImage.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Agregar imagen de fondo a un archivo PDF y guardar el "ResultBackgroundImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
      console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el módulo `asposepdfnodejs`.
1. Especificar el nombre del archivo PDF en el que se agregará la imagen de fondo.
1. Inicializar el módulo AsposePdf. Recibir el objeto si es exitoso.

1. Llama a la función [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/).
1. Agrega una imagen de fondo a un archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultAddBackgroundImage.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se contendrá en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  /*Agregar imagen de fondo a un archivo PDF y guardar en "ResultBackgroundImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
  console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```