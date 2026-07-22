---
title: Convertir PDF a EPUB, TeX, Texto, XPS en Node.js
linktitle: Convertir PDF a otros formatos
type: docs
weight: 90
url: /es/nodejs-cpp/convert-pdf-to-other-files/
lastmod: "2026-07-18"
description: Este tema le muestra cómo convertir un archivo PDF a otros formatos de archivo como EPUB, LaTeX, Texto, XPS, etc., en el entorno Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

{{% alert color="success" %}}
**Intenta convertir PDF a EPUB en línea**

Aspose.PDF para Node.js le presenta una aplicación gratuita en línea ["PDF a EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), donde puede probar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión PDF a EPUB con Aplicación Gratis](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## Convertir PDF a EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** es un estándar de libros electrónicos gratuito y abierto del International Digital Publishing Forum (IDPF). Los archivos tienen la extensión .epub.
EPUB está diseñado para contenido refluible, lo que significa que un lector EPUB puede optimizar el texto para un dispositivo de visualización particular. EPUB también soporta contenido de diseño fijo. El formato está destinado a ser un formato único que los editores y las casas de conversión pueden usar internamente, así como para la distribución y venta. Reemplaza el estándar Open eBook.

En caso de que desees convertir un documento PDF, puedes usar [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/) función. 
Por favor, revisa el siguiente fragmento de código para convertir en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifica el nombre del archivo PDF que será convertido.
1. Llamar `AsposePdf` como Promise y realiza la operación para convertir el archivo. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/).
1. Convertir archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPDFtoEPUB.epub". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to ePub and save the "ResultPDFtoEPUB.epub"*/
      const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
      console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF que se convertirá
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/).
1. Convertir archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPDFtoEPUB.epub". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to ePub and save the "ResultPDFtoEPUB.epub"*/
  const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
  console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**Intenta convertir PDF a LaTeX/TeX en línea**

Aspose.PDF para Node.js le presenta una aplicación gratuita en línea ["PDF a LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), donde puede probar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión PDF a LaTeX/TeX con aplicación gratuita](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Convertir PDF a TeX

**Aspose.PDF for Node.js** soporta la conversión de PDF a TeX.
En caso de que desees convertir un documento PDF, puedes usar [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/) función. 
Por favor, revisa el siguiente fragmento de código para convertir en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifica el nombre del archivo PDF que será convertido.
1. Llamar `AsposePdf` como Promise y realiza la operación para convertir el archivo. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/).
1. Convertir archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPDFtoTeX.tex". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to TeX and save the "ResultPDFtoTeX.tex"*/
      const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
      console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF que se convertirá
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/).
1. Convertir archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPDFtoTeX.tex". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to TeX and save the "ResultPDFtoTeX.tex"*/
  const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
  console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**Intenta convertir PDF a Texto en línea**

Aspose.PDF para Node.js le presenta una aplicación gratuita en línea ["PDF a Texto"](https://products.aspose.app/pdf/conversion/pdf-to-txt), donde puede probar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de PDF a texto con aplicación gratuita](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Convertir PDF a TXT

En caso de que desees convertir un documento PDF, puedes usar [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/) función. 
Por favor, revisa el siguiente fragmento de código para convertir en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifica el nombre del archivo PDF que será convertido.
1. Llamar `AsposePdf` como Promise y realiza la operación para convertir el archivo. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/).
1. Convertir archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPDFtoTxt.txt". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to Txt and save the "ResultPDFtoTxt.txt"*/
      const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
      console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF que se convertirá
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/).
1. Convertir archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPDFtoTxt.txt". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to Txt and save the "ResultPDFtoTxt.txt"*/
  const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
  console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**Intenta convertir PDF a XPS en línea**

Aspose.PDF para Node.js le presenta una aplicación gratuita en línea ["PDF a XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), donde puede probar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión PDF a XPS con aplicación gratuita](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## Convertir PDF a XPS

El tipo de archivo XPS está asociado principalmente con la XML Paper Specification de Microsoft Corporation. La XML Paper Specification (XPS), anteriormente con el nombre en código Metro y que engloba el concepto de marketing Next Generation Print Path (NGPP), es la iniciativa de Microsoft para integrar la creación y visualización de documentos en el sistema operativo Windows.

**Aspose.PDF for Node.js** brinda la posibilidad de convertir archivos PDF a <abbr title="XML Paper Specification">XPS</abbr> formato. Intentemos usar el fragmento de código presentado para convertir archivos PDF a formato XPS con Node.js.

En caso de que desees convertir un documento PDF, puedes usar [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/) función. 
Por favor, revisa el siguiente fragmento de código para convertir en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifica el nombre del archivo PDF que será convertido.
1. Llamar `AsposePdf` como Promise y realiza la operación para convertir el archivo. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/).
1. Convertir archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en \"ResultPDFtoXps.xps\". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to Xps and save the "ResultPDFtoXps.xps"*/
      const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
      console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifica el nombre del archivo PDF que será convertido.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/).
1. Convertir archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en \"ResultPDFtoXps.xps\". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to Xps and save the "ResultPDFtoXps.xps"*/
  const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
  console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

## Convertir PDF a PDF en escala de grises

Convertir PDF a blanco y negro con Aspose.PDF for Node.js via C++ toolkit. 
¿Por qué debería convertir PDF a escala de grises? Si el archivo PDF contiene muchas imágenes en color y el tamaño del archivo es importante en lugar del color, la conversión ahorra espacio. Si imprime un archivo PDF en blanco y negro, convertirlo le permitirá verificar visualmente cómo se ve el resultado final. 

En caso de que desees convertir un documento PDF, puedes usar [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/) función. 
Por favor, revisa el siguiente fragmento de código para convertir en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifica el nombre del archivo PDF que será convertido.
1. Llamar `AsposePdf` como Promise y realiza la operación para convertir el archivo. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/).
1. Convertir archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultConvertToGrayscale.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

const AsposePdf = require('asposepdfnodejs');
const pdf_file = 'Aspose.pdf';
AsposePdf().then(AsposePdfModule => {
    /*Convert a PDF-file to grayscale and save the "ResultConvertToGrayscale.pdf"*/
    const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
    console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
});
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifica el nombre del archivo PDF que será convertido.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/).
1. Convertir archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultConvertToGrayscale.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to grayscale and save the "ResultConvertToGrayscale.pdf"*/
  const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
  console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```






