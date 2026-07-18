---
title: Rotar páginas PDF en Node.js
linktitle: Rotar páginas PDF
type: docs
weight: 50
url: /es/nodejs-cpp/rotate-pages/
description: Este tema describe cómo rotar la orientación de la página en un archivo PDF existente de forma programática en un entorno Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Esta sección describe cómo rotar páginas en un archivo PDF existente usando Aspose.PDF for Node.js via C\u002B\u002B.

En caso de que desee rotar páginas PDF, puede usar [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/) función. Esta función usa un parámetro especial 'AsposePdfModule.Rotation' para el valor de rotación. Con él puedes establecer cuántos grados necesitas rotar el PDF. Hay variantes: Ninguno, 90, 180 o 270 grados.

Por favor, revisa el siguiente fragmento de código para rotar páginas PDF en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifica el nombre del archivo PDF a rotar.
1. Llamar `AsposePdf` como Promise y realiza la operación para rotar páginas. Recibe el objeto si es exitoso.
1. Llame a la función [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). 
1. Rota todos los archivos PDF. La rotación está configurada en 270 grados (on270). Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultRotation.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Rotate PDF-pages and save the "ResultRotation.pdf"*/
      const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
      console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifica el nombre del archivo PDF a rotar.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). 
1. Rota todos los archivos PDF. La rotación está configurada en 270 grados (on270). Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultRotation.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Rotate PDF-pages and save the "ResultRotation.pdf"*/
  const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
  console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```