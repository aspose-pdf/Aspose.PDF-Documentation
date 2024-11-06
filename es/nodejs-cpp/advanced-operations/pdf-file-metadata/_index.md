---
title: Trabajando con Metadatos de Archivos PDF en Node.js 
linktitle: Metadatos de Archivos PDF
type: docs
weight: 130
url: es/nodejs-cpp/pdf-file-metadata/
description: Esta sección explica cómo obtener información de archivos PDF, cómo obtener metadatos de un archivo PDF, establecer información de archivos PDF en Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtener Información de Archivos PDF

En caso de que desees obtener información de archivos PDF, puedes usar la función [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/). 
Por favor, revisa el siguiente fragmento de código para obtener información de archivos PDF en el entorno Node.js.

**CommonJS:**

1. Llama a `require` e importa el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifica el nombre del archivo PDF del cual se extraerá la información.
1. Llama a `AsposePdf` como Promesa y realiza la operación para extraer la información. Recibe el objeto si es exitoso.

1. Llama a la función [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. Los metadatos extraídos se almacenan en el objeto JSON. Así, si 'json.errorCode' es 0, los metadatos extraídos se muestran usando console.log. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Obtener información (metadatos) de un archivo PDF*/
      const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
      /* JSON
        Título             : json.title
        Creador            : json.creator
        Autor              : json.author
        Asunto             : json.subject
        Palabras clave     : json.keywords
        Fecha de creación  : json.creation
        Fecha de modificación: json.mod
        Formato PDF        : json.format
        Versión PDF        : json.version
        PDF es PDF/A       : json.ispdfa
        PDF es PDF/UA      : json.ispdfua
        PDF está linealizado: json.islinearized
        PDF está cifrado   : json.isencrypted
        Permiso PDF        : json.permission
        Tamaño de página PDF: json.size
        Conteo de páginas  : json.pagecount
        Conteo de anotaciones: json.annotationcount
        Conteo de marcadores: json.bookmarkcount
        Conteo de archivos adjuntos: json.attachmentcount
        Conteo de metadatos: json.metadatacount
        Conteo de JavaScript: json.javascriptcount
        Conteo de imágenes : json.imagecount
      */
      console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF del cual se extraerá la información.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llama a la función [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. Los metadatos extraídos se almacenan en el objeto JSON. Por lo tanto, si 'json.errorCode' es 0, los metadatos extraídos se muestran usando console.log. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error se encontrará en 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Obtener información (metadatos) de un archivo PDF*/
    const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
    /* JSON
      Título            : json.title
      Creador           : json.creator
      Autor             : json.author
      Asunto            : json.subject
      Palabras clave    : json.keywords
      Fecha de creación : json.creation
      Fecha de modificación : json.mod
      Formato PDF       : json.format
      Versión PDF       : json.version
      PDF es PDF/A      : json.ispdfa
      PDF es PDF/UA     : json.ispdfua
      PDF está linealizado : json.islinearized
      PDF está encriptado  : json.isencrypted
      Permiso PDF       : json.permission
      Tamaño de página PDF : json.size
      Conteo de páginas : json.pagecount
      Conteo de anotaciones : json.annotationcount
      Conteo de marcadores : json.bookmarkcount
      Conteo de adjuntos : json.attachmentcount
      Conteo de metadatos : json.metadatacount
      Conteo de JavaScript : json.javascriptcount
      Conteo de imágenes : json.imagecount
    */
    console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Título: ' + json.title : json.errorText);
```


## Obtener Todas las Fuentes

Obtener fuentes de un archivo PDF puede ser una forma útil de reutilizar fuentes en otros documentos o aplicaciones.

En caso de que desees obtener fuentes de un archivo PDF, puedes usar la función [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).
Por favor, revisa el siguiente fragmento de código para obtener fuentes de un archivo PDF en un entorno Node.js.

**CommonJS:**

1. Llama a `require` e importa el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifica el nombre del archivo PDF del cual se extraerán las fuentes.
1. Llama a `AsposePdf` como Promise y realiza la operación para extraer fuentes. Recibe el objeto si tiene éxito.
1. Llama a la función [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).

1. Las fuentes extraídas se almacenan en el objeto JSON. Por lo tanto, si 'json.errorCode' es 0, muestra un array de detalles de fuentes, incluyendo el nombre de la fuente, si está incrustada y su estado de accesibilidad utilizando console.log. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Obtener lista de fuentes de un archivo PDF*/
      const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
      /*json.fonts - array de fuentes: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
      console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF del cual se extraerán las fuentes.

1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llama a la función [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).
1. Las fuentes extraídas se almacenan en el objeto JSON. Por lo tanto, si 'json.errorCode' es 0, muestra un arreglo con los detalles de las fuentes, incluyendo el nombre de la fuente, si está incrustada y su estado de accesibilidad utilizando console.log. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Obtener lista de fuentes de un archivo PDF*/
  const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
  /*json.fonts - arreglo de fuentes: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
  console.log("AsposePdfGetAllFonts => fuentes: %O", json.errorCode == 0 ? json.fonts : json.errorText);
```

## Establecer Información del Archivo PDF


Aspose.PDF para Node.js vía C++ le permite establecer información específica del archivo para un PDF, información como autor, fecha de creación, asunto y título. Para establecer esta información:

En caso de que desee establecer información específica del archivo, puede usar la función [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/). 
Por favor, revise el siguiente fragmento de código para establecer la información del archivo en el entorno de Node.js.

Posible de establecer:
- título
- creador
- autor
- asunto
- listar palabras clave
- fecha de creación
- fecha de modificación
- nombre del archivo resultante

**CommonJS:**

1. Llame a `require` e importe el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifique el nombre del archivo PDF donde se establecerá la información.
1. Llame a `AsposePdf` como Promise y realice la operación. Reciba el objeto si tiene éxito.
1. Llame a la función [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).

1. Establecer la información del archivo PDF. La información como título, creador, autor, asunto, palabras clave, fecha de creación y fecha de modificación se proporcionan como parámetros. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultSetInfo.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js
  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Establecer información del PDF: título, creador, autor, asunto, palabras clave, creación (fecha), mod (fecha de modificación)*/
      /*Si no necesita establecer un valor, use undefined o "" (cadena vacía)*/
      /*Establecer información (metadatos) en un archivo PDF y guardar en "ResultSetInfo.pdf"*/
      const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Configuración de la Información del Documento PDF", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
      console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF donde se establecerá la información.
1. Inicializa el módulo AsposePdf. Recibe el objeto si es exitoso.
1. Llama a la función [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).
1. Establece la información del archivo PDF. Información como título, creador, autor, asunto, palabras clave, fecha de creación y fecha de modificación se proporcionan como parámetros. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultSetInfo.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error se contendrá en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Establecer información del PDF: título, creador, autor, asunto, palabras clave, creación (fecha), mod (fecha de modificación)*/
  /*Si no necesita establecer el valor, use undefined o "" (cadena vacía)*/
  /*Establecer información (metadata) en un archivo PDF y guardar el "ResultSetInfo.pdf"*/
  const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Configuración de Información del Documento PDF", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
  console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```


## Eliminar Información del Archivo PDF

Aspose.PDF para Node.js vía C++ te permite eliminar los metadatos de archivos PDF:

En caso de que desees eliminar los metadatos de un PDF, puedes utilizar la función [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/). 
Por favor, revisa el siguiente fragmento de código para eliminar los metadatos de un PDF en un entorno Node.js.

**CommonJS:**

1. Requiere el módulo AsposePDFforNode.js.
1. Especifica el nombre del archivo PDF del cual se eliminará la información.
1. Inicializa el módulo AsposePdf. Recibe el objeto si es exitoso.
1. Llama a la función [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. Elimina la información del archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfRemoveMetadata.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error se contendrá en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Eliminar metadatos de un archivo PDF y guardar en "ResultPdfRemoveMetadata.pdf"*/
      const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
      console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF del cual se eliminará la información.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llama a la función [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. Elimina la información del archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfRemoveMetadata.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Eliminar metadatos de un archivo PDF y guardar en "ResultPdfRemoveMetadata.pdf"*/
  const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
  console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```