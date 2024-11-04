---
title: Cómo Unir PDF en Node.js
linktitle: Unir archivos PDF
type: docs
weight: 20
url: /nodejs-cpp/merge-pdf/
description: Esta página explica cómo unir documentos PDF en un solo archivo PDF con Aspose.PDF para Node.js a través de C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Unir o combinar dos PDF en un solo PDF en Node.js

Combinar y unir archivos es una tarea muy popular al trabajar con una gran cantidad de documentos. A veces, al trabajar con documentos e imágenes, cuando se escanean, procesan y organizan, se crean varios archivos.
Pero, ¿qué pasa si necesitas almacenar todo en un solo archivo? ¿O no quieres imprimir varios documentos? Concatenar dos archivos PDF con Aspose.PDF para Node.js a través de C++.

En caso de que quieras unir dos PDFs, puedes usar la función [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
Por favor, revisa el siguiente fragmento de código para unir dos archivos PDFs en el entorno de Node.js.

**CommonJS:**

1. Llame a `require` e importe el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifique el nombre de los archivos PDF que se fusionarán.
1. Llame a `AsposePdf` como Promesa y realice la operación para fusionar. Reciba el objeto si es exitoso.
1. Llame a la función [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. Fusione dos archivos PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultMerge.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se contendrá en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Fusionar dos archivos PDF y guardar el "ResultMerge.pdf"*/
      const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
      console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre de los archivos PDF que se fusionarán.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llama a la función [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. Fusiona dos archivos PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultMerge.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Fusiona dos archivos PDF y guarda el "ResultMerge.pdf"*/
  const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
  console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```