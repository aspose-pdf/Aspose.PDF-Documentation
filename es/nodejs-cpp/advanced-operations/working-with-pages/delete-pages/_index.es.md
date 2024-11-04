---
title: Eliminar Página en PDF en Node.js
linktitle: Eliminar Páginas PDF
type: docs
weight: 30
url: /nodejs-cpp/delete-pages/
description: Puede eliminar páginas de su archivo PDF usando Aspose.PDF para Node.js a través de C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

En caso de que desee eliminar páginas de PDF, puede utilizar la función [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/).

Una característica de esta función es que puede aceptar varios tipos como parámetro numPages:

- string: en este caso, podemos mencionar un conjunto de páginas utilizando páginas particulares o intervalos. Por ejemplo, la cadena "7, 20, 30-32, 34" significa que queremos eliminar las páginas 7, 20, desde 30 hasta 32 y 34.
- array: en este caso, solo podemos mencionar páginas. El array [3,7] significa que queremos eliminar las páginas 3 y 7.
- int: un solo número de página.

Por favor, revise el siguiente fragmento de código para eliminar páginas de PDF en el entorno de Node.js.

**CommonJS:**

1. Llamar a `require` e importar el módulo `asposepdfnodejs` como la variable `AsposePdf`.
1. Especificar el nombre del archivo PDF del cual se eliminarán las páginas.
1. Llamar a `AsposePdf` como Promise y realizar la operación para eliminar páginas. Recibir el objeto si es exitoso.
1. Llamar a la función [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/).
1. Elimina las páginas específicas del archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultDeletePages.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se contendrá en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*cadena, incluye números de página con intervalo: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      /*const numPages = "1-3";*/
      /*arreglo, arreglo de números de página*/
      /*const numPages = [1,3];*/
      /*número, número de página*/
      const numPages = 1;
      /*Eliminar páginas de un archivo PDF y guardar en "ResultDeletePages.pdf"*/
      const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
      console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF del cual se eliminarán las páginas.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llama a la función [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). Esta función ayuda a eliminar las páginas especificadas del archivo PDF. La operación está determinada por la variable numPages, que puede ser una cadena con intervalos de páginas (por ejemplo, "7, 20, 22, 30-32, 33, 36-40, 46"), un arreglo de números de página, o un solo número de página.
1. Elimina las páginas particulares del archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultDeletePages.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*cadena, incluye números de páginas con intervalo: "7, 20, 22, 30-32, 33, 36-40, 46"*/
  /*const numPages = "1-3";*/
  /*arreglo, arreglo de números de páginas*/
  /*const numPages = [1,3];*/
  /*número, número de página*/
  const numPages = 1;
  /*Eliminar páginas de un archivo PDF y guardar el "ResultDeletePages.pdf"*/
  const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
  console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```