---
title: Eliminar página en PDF en Node.js
linktitle: Eliminar páginas de PDF
type: docs
weight: 30
url: /es/nodejs-cpp/delete-pages/
description: Puede eliminar páginas de su archivo PDF usando Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

En caso de que desee eliminar páginas PDF, puede usar [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/) función. 

Una característica de esta función es que puede aceptar varios tipos como parámetro numPages:

- string: en este caso, podemos mencionar un conjunto de páginas usando páginas particulares o intervalos. Por ejemplo, string "7, 20, 30-32, 34" significa que queremos eliminar las páginas 7, 20, de 30 a 32 y 34.
- array: en este caso, solo podemos mencionar páginas. Array [3,7] significa que queremos eliminar las páginas 3 y 7.
- int: un número de página único.

Por favor, revise el siguiente fragmento de código para eliminar páginas PDF en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifique el nombre del archivo PDF del que se eliminarán las páginas.
1. Llamar `AsposePdf` como Promise y realizar la operación para eliminar páginas. Reciba el objeto si tiene éxito.
1. Llame a la función [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). 
1. Elimina las páginas particulares del archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en \"ResultDeletePages.pdf\". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*string, include number pages with interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      /*const numPages = "1-3";*/
      /*array, array of number pages*/
      /*const numPages = [1,3];*/
      /*number, number page*/
      const numPages = 1;
      /*Delete pages from a PDF-file and save the "ResultDeletePages.pdf"*/
      const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
      console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF del que se eliminarán las páginas.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). Esta función ayuda a eliminar las páginas especificadas del archivo PDF. La operación está determinada por la variable numPages, que puede ser una cadena con intervalos de páginas (por ejemplo, "7, 20, 22, 30-32, 33, 36-40, 46"), una matriz de números de página o un número de página único.
1. Elimina las páginas particulares del archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en \"ResultDeletePages.pdf\". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*string, include number pages with interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
  /*const numPages = "1-3";*/
  /*array, array of number pages*/
  /*const numPages = [1,3];*/
  /*number, number page*/
  const numPages = 1;
  /*Delete pages from a PDF-file and save the "ResultDeletePages.pdf"*/
  const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
  console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```