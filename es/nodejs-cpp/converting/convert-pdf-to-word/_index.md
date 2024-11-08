---
title: Convertir PDF a documentos Word en Node.js
linktitle: Convertir PDF a Word
type: docs
weight: 10
url: /es/nodejs-cpp/convert-pdf-to-doc/
lastmod: "2023-11-16"
description: Aprende cómo convertir PDF a DOC(DOCX) en el entorno de Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Para editar el contenido de un archivo PDF en Microsoft Word u otros procesadores de texto que soporten formatos DOC y DOCX. Los archivos PDF son editables, pero los archivos DOC y DOCX son más flexibles y personalizables.

{{% alert color="success" %}}
**Intenta convertir PDF a DOC en línea**

Aspose.PDF para Node.js te presenta una aplicación gratuita en línea ["PDF a DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Convertir PDF a DOC](/pdf/es/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convertir PDF a DOC

En caso de que quieras convertir un documento PDF, puedes usar la función [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
 
Por favor, revise el siguiente fragmento de código para convertir en el entorno de Node.js.

**CommonJS:**

1. Llama a `require` e importa el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifica el nombre del archivo PDF que será convertido.
1. Llama a `AsposePdf` como Promise y realiza la operación para convertir el archivo. Recibe el objeto si es exitoso.
1. Llama a la función [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
1. Convierte el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPDFtoDoc.doc". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convierte un archivo PDF a Doc y guarda el "ResultPDFtoDoc.doc"*/
      const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
      console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
2. Especifica el nombre del archivo PDF que se convertirá.
3. Inicializa el módulo AsposePdf. Recibe el objeto si es exitoso.
4. Llama a la función [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
5. Convierte el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPDFtoDoc.doc". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convierte un archivo PDF a Doc y guarda el "ResultPDFtoDoc.doc"*/
  const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
  console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="warning" %}}
**Intenta convertir PDF a DOCX en línea**

Aspose.PDF para Node.js te presenta la aplicación gratuita en línea ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), donde puedes intentar investigar la funcionalidad y la calidad con la que trabaja.

[![Aspose.PDF Convertion PDF to Word Free App](/pdf/es/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Convertir PDF a DOCX

Aspose.PDF para Node.js a través del kit de herramientas C++ te permite leer y convertir documentos PDF a DOCX. DOCX es un formato bien conocido para documentos de Microsoft Word cuya estructura se cambió de binaria simple a una combinación de archivos XML y binarios. Los archivos Docx pueden abrirse con Word 2007 y versiones posteriores, pero no con las versiones anteriores de MS Word que soportan extensiones de archivo DOC.

En caso de que quieras convertir un documento PDF, puedes usar la función [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/). 
Por favor, revisa el siguiente fragmento de código para convertir en un entorno Node.js.

**CommonJS:**

1. Llama a `require` e importa el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifica el nombre del archivo PDF que se convertirá.

1. Llama a `AsposePdf` como Promise y realiza la operación para convertir el archivo. Recibe el objeto si tiene éxito.
1. Llama a la función [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. Convierte archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPDFtoDocX.docx". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convierte un archivo PDF a DocX y guarda el "ResultPDFtoDocX.docx"*/
      const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
      console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF que será convertido.

1. Inicialice el módulo AsposePdf. Reciba el objeto si es exitoso.
1. Llame a la función [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. Convierta el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPDFtoDocX.docx". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convertir un archivo PDF a DocX y guardar el "ResultPDFtoDocX.docx"*/
  const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
  console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```