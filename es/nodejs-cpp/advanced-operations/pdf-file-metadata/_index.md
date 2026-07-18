---
title: Trabajando con los metadatos de archivos PDF en Node.js
linktitle: Metadatos de archivos PDF
type: docs
weight: 130
url: /es/nodejs-cpp/pdf-file-metadata/
description: Esta sección explica cómo obtener información de archivos PDF, cómo obtener metadatos de un archivo PDF, establecer la información del archivo PDF en Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtener información del archivo PDF

En caso de que desees obtener información del archivo PDF, puedes usar [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/) función. 
Por favor, revise el siguiente fragmento de código para obtener información del archivo PDF en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifique el nombre del archivo PDF del cual se extraerá la información.
1. Llamar `AsposePdf` como Promise y realizar la operación para extraer información. Reciba el objeto si tiene éxito.
1. Llame a la función [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. Los metadatos extraídos se almacenan en el objeto JSON. Por lo tanto, si 'json.errorCode' es 0, los metadatos extraídos se muestran usando console.log. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Get info (metadata) from a PDF-file*/
      const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
      /* JSON
        Title             : json.title
        Creator           : json.creator
        Author            : json.author
        Subject           : json.subject
        Keywords          : json.keywords
        Creation Date     : json.creation
        Modify Date       : json.mod
        PDF format        : json.format
        PDF version       : json.version
        PDF is PDF/A      : json.ispdfa
        PDF is PDF/UA     : json.ispdfua
        PDF is linearized : json.islinearized
        PDF is encrypted  : json.isencrypted
        PDF permission    : json.permission
        PDF page size     : json.size
        Page count        : json.pagecount
        Annotation count  : json.annotationcount
        Bookmark count    : json.bookmarkcount
        Attachment count  : json.attachmentcount
        Metadata count    : json.metadatacount
        JavaScript count  : json.javascriptcount
        Image count       : json.imagecount
      */
      console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF del cual se extraerá la información.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. Los metadatos extraídos se almacenan en el objeto JSON. Por lo tanto, si 'json.errorCode' es 0, los metadatos extraídos se muestran usando console.log. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Get info (metadata) from a PDF-file*/
    const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
    /* JSON
      Title             : json.title
      Creator           : json.creator
      Author            : json.author
      Subject           : json.subject
      Keywords          : json.keywords
      Creation Date     : json.creation
      Modify Date       : json.mod
      PDF format        : json.format
      PDF version       : json.version
      PDF is PDF/A      : json.ispdfa
      PDF is PDF/UA     : json.ispdfua
      PDF is linearized : json.islinearized
      PDF is encrypted  : json.isencrypted
      PDF permission    : json.permission
      PDF page size     : json.size
      Page count        : json.pagecount
      Annotation count  : json.annotationcount
      Bookmark count    : json.bookmarkcount
      Attachment count  : json.attachmentcount
      Metadata count    : json.metadatacount
      JavaScript count  : json.javascriptcount
      Image count       : json.imagecount
    */
    console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
```

## Obtener todas las fuentes

Obtener fuentes de un archivo PDF puede ser una forma útil de reutilizar fuentes en otros documentos o aplicaciones. 

En caso de que desees obtener fuentes de un archivo PDF, puedes usar [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/) función. 
Por favor, revise el siguiente fragmento de código para obtener fuentes de un archivo PDF en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifique el nombre del archivo PDF del que se extraerán las fuentes.
1. Llamar `AsposePdf` como Promise y realiza la operación para extraer fuentes. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).
1. Las fuentes extraídas se almacenan en el objeto JSON. Así, si \u0027json.errorCode\u0027 es 0, muestra una matriz de detalles de fuentes, incluido el nombre de la fuente, si está incrustada y su estado de accesibilidad usando console.log. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en \u0027json.errorText\u0027.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Get list fonts from a PDF-file*/
      const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
      /*json.fonts - array of fonts: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
      console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF del que se extraerán las fuentes.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).
1. Las fuentes extraídas se almacenan en el objeto JSON. Así, si \u0027json.errorCode\u0027 es 0, muestra una matriz de detalles de fuentes, incluido el nombre de la fuente, si está incrustada y su estado de accesibilidad usando console.log. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en \u0027json.errorText\u0027.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Get list fonts from a PDF-file*/
  const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
  /*json.fonts - array of fonts: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
  console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
```

## Establecer información del archivo PDF

Aspose.PDF for Node.js via C++ le permite establecer información específica del archivo para un PDF, información como autor, fecha de creación, asunto y título. Para establecer esta información:

En caso de que desees establecer información específica del archivo, puedes usar [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/) función. 
Por favor, revise el siguiente fragmento de código para establecer la información del archivo en el entorno Node.js.

Posible establecer: 
- título
- creador
- autor
- asunto
- lista de palabras clave
- fecha de creación
- modificar fecha
- nombre del archivo de resultado

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifique el nombre del archivo PDF donde se establecerá la información.
1. Llamar `AsposePdf` como Promise y realizar la operación. Reciba el objeto si tiene éxito.
1. Llame a la función [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).
1. Establecer la información del archivo PDF. Información como el título, creador, autor, asunto, palabras clave, fecha de creación y fecha de modificación se proporcionan como parámetros. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultSetInfo.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set PDF info: title, creator, author, subject, keywords, creation (date), mod (date modify)*/
      /*If not need to set value, use undefined or "" (empty string)*/
      /*Set info (metadata) in a PDF-file and save the "ResultSetInfo.pdf"*/
      const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
      console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF donde se establecerá la información.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).
1. Establecer la información del archivo PDF. Información como el título, creador, autor, asunto, palabras clave, fecha de creación y fecha de modificación se proporcionan como parámetros. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultSetInfo.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set PDF info: title, creator, author, subject, keywords, creation (date), mod (date modify)*/
  /*If not need to set value, use undefined or "" (empty string)*/
  /*Set info (metadata) in a PDF-file and save the "ResultSetInfo.pdf"*/
  const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
  console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

## Eliminar información del archivo PDF

Aspose.PDF for Node.js via C++ permite eliminar los metadatos del archivo PDF:

En caso de que desees eliminar los metadatos del PDF, puedes usar [AsposePdfEliminarMetadatos](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/) función. 
Por favor, revise el siguiente fragmento de código para eliminar los metadatos del PDF en un entorno Node.js.

**CommonJS:**

1. Requiere el módulo AsposePDFforNode.js.
1. Especifique el nombre del archivo PDF del cual se eliminará la información.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfEliminarMetadatos](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. Eliminar la información del archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfRemoveMetadata.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Remove metadata from a PDF-file and save the "ResultPdfRemoveMetadata.pdf"*/
      const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
      console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF del cual se eliminará la información.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfEliminarMetadatos](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. Eliminar la información del archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfRemoveMetadata.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Remove metadata from a PDF-file and save the "ResultPdfRemoveMetadata.pdf"*/
  const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
  console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```