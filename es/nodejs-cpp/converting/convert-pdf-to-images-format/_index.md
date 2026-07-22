---
title: Convertir PDF a formatos de imagen en Node.js
linktitle: Convertir PDF a imágenes
type: docs
weight: 70
url: /es/nodejs-cpp/convert-pdf-to-images-format/
lastmod: "2026-07-18"
description: Este tema le muestra cómo usar Aspose.PDF para convertir PDF a varios formatos de imagen, p. ej. TIFF, BMP, JPEG, PNG, SVG con unas pocas líneas de código en el entorno Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Node.js Convertir PDF a Imagen

En este artículo, le mostraremos las opciones para convertir PDF a formatos de imagen.

Los documentos escaneados previamente a menudo se guardan en el formato de archivo PDF. Sin embargo, ¿necesitas editarlo en un editor gráfico o enviarlo posteriormente en formato de imagen? Tenemos una herramienta universal para que conviertas PDF a imágenes usando 
La tarea más común es cuando necesitas guardar un documento PDF completo o algunas páginas específicas de un documento como un conjunto de imágenes. **Aspose for Node.js via C++** permite convertir PDF a formatos JPG y PNG para simplificar los pasos necesarios para obtener tus imágenes de un archivo PDF específico.

**Aspose.PDF for Node.js via C++** admite la conversión de varios formatos de PDF a imagen. Por favor, verifica la sección [Formatos de archivo compatibles con Aspose.PDF](https://docs.aspose.com/pdf/nodejs-cpp/supported-file-formats/).

{{% alert color="success" %}}
**Intenta convertir PDF a JPEG en línea**

Aspose.PDF para Node.js le presenta una aplicación gratuita en línea ["PDF a JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), donde puede probar la funcionalidad y la calidad con la que funciona.

[![Conversión de PDF a JPEG con Aspose.PDF y aplicación gratuita](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## Convertir PDF a JPEG

En caso de que desees convertir un documento PDF, puedes usar [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/) función. 
Por favor, revisa el siguiente fragmento de código para convertir en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifica el nombre del archivo PDF que será convertido.
1. Llamar `AsposePdf` como Promise y realiza la operación para convertir el archivo. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).
1. Convertir archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en \"ResultPdfToJpg{0:D2}.jpg\". Donde {0:D2} representa el número de página con formato de dos dígitos. Las imágenes se guardan con una resolución de 150 DPI. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to JPG with template "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
      console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF que se convertirá
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).
1. Convertir archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en \"ResultPdfToJpg{0:D2}.jpg\". Donde {0:D2} representa el número de página con formato de dos dígitos. Las imágenes se guardan con una resolución de 150 DPI. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to JPG with template "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
  console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

{{% alert color="success" %}}
**Intente convertir PDF a TIFF en línea**

Aspose.PDF para Node.js le presenta una aplicación gratuita en línea ["PDF a TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), donde puede probar la funcionalidad y la calidad con la que funciona.

[![Conversión de Aspose.PDF de PDF a TIFF con aplicación gratuita](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Convertir PDF a TIFF

En caso de que desees convertir un documento PDF, puedes usar [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/) función. 
Por favor, revisa el siguiente fragmento de código para convertir en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifica el nombre del archivo PDF que será convertido.
1. Llamar `AsposePdf` como Promise y realiza la operación para convertir el archivo. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/).
1. Convertir archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToTiff{0:D2}.tiff". Donde {0:D2} representa el número de página con un formato de dos dígitos. Las imágenes se guardan con una resolución de 150 DPI. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to TIFF with template "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
      console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF que se convertirá
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/).
1. Convertir archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToTiff{0:D2}.tiff". Donde {0:D2} representa el número de página con un formato de dos dígitos. Las imágenes se guardan con una resolución de 150 DPI. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to TIFF with template "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
  console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

{{% alert color="success" %}}
**Intenta convertir PDF a PNG en línea**

Como ejemplo de cómo funcionan nuestras aplicaciones gratuitas, por favor revise la siguiente característica.

Aspose.PDF para Node.js le presenta una aplicación gratuita en línea ["PDF a PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), donde puede probar la funcionalidad y la calidad con la que funciona.

[![Cómo convertir PDF a PNG usando una aplicación gratuita](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Convertir PDF a PNG

En caso de que desees convertir un documento PDF, puedes usar [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/) función. 
Por favor, revisa el siguiente fragmento de código para convertir en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifica el nombre del archivo PDF que será convertido.
1. Llamar `AsposePdf` como Promise y realiza la operación para convertir el archivo. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
1. Convertir archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToPng{0:D2}.png". Donde {0:D2} representa el número de página con un formato de dos dígitos. Las imágenes se guardan con una resolución de 150 DPI. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to PNG with template "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
      console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF que se convertirá
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
1. Convertir archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToPng{0:D2}.png". Donde {0:D2} representa el número de página con un formato de dos dígitos. Las imágenes se guardan con una resolución de 150 DPI. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to PNG with template "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
  console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

{{% alert color="success" %}}
**Intenta convertir PDF a SVG en línea**

Aspose.PDF para Node.js le presenta una aplicación gratuita en línea ["PDF a SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), donde puede probar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de PDF a SVG con aplicación gratuita](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** es una familia de especificaciones de un formato de archivo basado en XML para gráficos vectoriales bidimensionales, tanto estáticos como dinámicos (interactivos o animados). La especificación SVG es un estándar abierto que ha sido desarrollado por el World Wide Web Consortium (W3C) desde 1999.

## Convertir PDF a SVG

### Convertir PDF a SVG clásico

En caso de que desees convertir un documento PDF, puedes usar [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/) función. 
Por favor, revisa el siguiente fragmento de código para convertir en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifica el nombre del archivo PDF que será convertido.
1. Llamar `AsposePdf` como Promise y realiza la operación para convertir el archivo. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
1. Convertir archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToSvg.svg". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to SVG and save the "ResultPdfToSvg.svg"*/
      const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
      console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF que se convertirá
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
1. Convertir archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToSvg.svg". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to SVG and save the "ResultPdfToSvg.svg"*/
  const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
  console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

### Convertir PDF a SVG comprimido

En caso de que desees convertir un documento PDF, puedes usar [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/) función. 
Por favor, revisa el siguiente fragmento de código para convertir en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifica el nombre del archivo PDF que será convertido.
1. Llamar `AsposePdf` como Promise y realiza la operación para convertir el archivo. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
1. Convertir archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToSvgZip.zip". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to SVG(zip) and save the "ResultPdfToSvgZip.zip"*/
      const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
      console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF que se convertirá
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
1. Convertir archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToSvgZip.zip". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*convert a PDF-file to SVG zip and save the "ResultPdfToSvgZip.zip"*/
  const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
  console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText)
```

## Convertir PDF a DICOM

En caso de que desees convertir un documento PDF, puedes usar [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/) función. 
Por favor, revisa el siguiente fragmento de código para convertir en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifica el nombre del archivo PDF que será convertido.
1. Llamar `AsposePdf` como Promise y realiza la operación para convertir el archivo. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
1. Convertir archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToDICOM{0:D2}.dcm". Donde {0:D2} representa el número de página con un formato de dos dígitos. Las imágenes se guardan con una resolución de 150 DPI. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to DICOM with template "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
      console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF que se convertirá
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
1. Convertir archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToDICOM{0:D2}.dcm". Donde {0:D2} representa el número de página con un formato de dos dígitos. Las imágenes se guardan con una resolución de 150 DPI. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to DICOM with template "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
  console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

## Convertir PDF a BMP

En caso de que desees convertir un documento PDF, puedes usar [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/) función. 
Por favor, revisa el siguiente fragmento de código para convertir en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifica el nombre del archivo PDF que será convertido.
1. Llamar `AsposePdf` como Promise y realiza la operación para convertir el archivo. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/).
1. Convertir archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToBmp{0:D2}.bmp". Donde {0:D2} representa el número de página con formato de dos dígitos. Las imágenes se guardan con una resolución de 150 DPI. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to BMP with template "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
      console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF que se convertirá
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/).
1. Convertir archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToBmp{0:D2}.bmp". Donde {0:D2} representa el número de página con formato de dos dígitos. Las imágenes se guardan con una resolución de 150 DPI. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to BMP with template "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
  console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```





