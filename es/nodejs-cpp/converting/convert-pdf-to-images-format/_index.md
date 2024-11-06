---
title: Convertir PDF a Formatos de Imagen en Node.js
linktitle: Convertir PDF a Imágenes
type: docs
weight: 70
url: es/nodejs-cpp/convert-pdf-to-images-format/
lastmod: "2023-11-16"
description: Este tema te muestra cómo usar Aspose.PDF para convertir PDF a varios formatos de imágenes, por ejemplo, TIFF, BMP, JPEG, PNG, SVG con unas pocas líneas de código en el entorno de Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Node.js Convertir PDF a Imagen

En este artículo, te mostraremos las opciones para convertir PDF a formatos de imagen.

Los documentos previamente escaneados a menudo se guardan en el formato de archivo PDF. Sin embargo, ¿necesitas editarlo en un editor gráfico o enviarlo en formato de imagen? Tenemos una herramienta universal para ti para convertir PDF a imágenes utilizando 
La tarea más común es cuando necesitas guardar un documento PDF completo o algunas páginas específicas de un documento como un conjunto de imágenes.
 **Aspose for Node.js via C++** te permite convertir PDF a formatos JPG y PNG para simplificar los pasos necesarios para obtener tus imágenes de un archivo PDF específico.

**Aspose.PDF for Node.js via C++** admite la conversión de varios formatos de imagen a partir de PDF. Por favor, consulta la sección [Formatos de Archivo Soportados por Aspose.PDF](https://docs.aspose.com/pdf/nodejs-cpp/supported-file-formats/).

{{% alert color="success" %}}
**Intenta convertir PDF a JPEG en línea**

Aspose.PDF for Node.js te presenta la aplicación gratuita en línea ["PDF to JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), donde puedes probar investigar la funcionalidad y calidad con la que funciona.

[![Conversión de Aspose.PDF de PDF a JPEG con App Gratis](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## Convertir PDF a JPEG

En caso de que quieras convertir un documento PDF, puedes usar la función [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).

Por favor, revisa el siguiente fragmento de código para convertir en el entorno Node.js.
**CommonJS:**

1. Llame a `require` e importe el módulo `asposepdfnodejs` como la variable `AsposePdf`.
1. Especifique el nombre del archivo PDF que se convertirá.
1. Llame a `AsposePdf` como Promise y realice la operación para convertir el archivo. Reciba el objeto si tiene éxito.
1. Llame a la función [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).
1. Convierta el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToJpg{0:D2}.jpg". Donde {0:D2} representa el número de página con un formato de dos dígitos. Las imágenes se guardan con una resolución de 150 DPI. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convertir un archivo PDF a JPG con la plantilla "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... formato de número de página), resolución 150 DPI y guardar*/
      const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
      console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF que será convertido.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llama a la función [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).
1. Convierte el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToJpg{0:D2}.jpg". Donde {0:D2} representa el número de página con un formato de dos dígitos. Las imágenes se guardan con una resolución de 150 DPI. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convierte un archivo PDF a JPG con la plantilla "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... formato de número de página), resolución 150 DPI y guarda*/
  const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
  console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


{{% alert color="success" %}}
**Intenta convertir PDF a TIFF en línea**

Aspose.PDF para Node.js te presenta una aplicación gratuita en línea ["PDF a TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), donde puedes intentar investigar la funcionalidad y la calidad con la que trabaja.

[![Aspose.PDF conversión de PDF a TIFF con Aplicación Gratuita](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Convertir PDF a TIFF

En caso de que desees convertir un documento PDF, puedes utilizar la función [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/). 
Por favor, revisa el siguiente fragmento de código para convertir en un entorno Node.js.

**CommonJS:**

1. Llama a `require` e importa el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifica el nombre del archivo PDF que será convertido.
1. Llama a `AsposePdf` como Promesa y realiza la operación para convertir el archivo. Recibe el objeto si tiene éxito.

1. Llama a la función [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/).
1. Convierte el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToTiff{0:D2}.tiff". Donde {0:D2} representa el número de página con un formato de dos dígitos. Las imágenes se guardan con una resolución de 150 DPI. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convierte un archivo PDF a TIFF con la plantilla "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... formato de número de página), resolución 150 DPI y guarda*/
      const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
      console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF que será convertido.
1. Inicializa el módulo AsposePdf. Recibe el objeto si es exitoso.
1. Llama a la función [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/).
1. Convierte el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToTiff{0:D2}.tiff". Donde {0:D2} representa el número de página con un formato de dos dígitos. Las imágenes se guardan con una resolución de 150 DPI. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convierte un archivo PDF a TIFF con la plantilla "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... formato de número de página), resolución 150 DPI y guarda*/
  const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
  console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


{{% alert color="success" %}}
**Intenta convertir PDF a PNG en línea**

Como ejemplo de cómo funcionan nuestras aplicaciones gratuitas, por favor revisa la siguiente característica.

Aspose.PDF para Node.js te presenta la aplicación en línea gratuita ["PDF a PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Cómo convertir PDF a PNG usando la aplicación gratuita](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Convertir PDF a PNG

En caso de que quieras convertir un documento PDF, puedes usar la función [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/). 
Por favor, revisa el siguiente fragmento de código para convertir en un entorno Node.js.

**CommonJS:**

1. Llama a `require` e importa el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifica el nombre del archivo PDF que será convertido.
1. Llama a `AsposePdf` como Promise y realiza la operación para convertir el archivo. Recibe el objeto si es exitoso.

1. Llama a la función [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
1. Convierte el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToPng{0:D2}.png". Donde {0:D2} representa el número de página con un formato de dos dígitos. Las imágenes se guardan con una resolución de 150 DPI. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convierte un archivo PDF a PNG con la plantilla "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... formato número de página), resolución 150 DPI y guarda*/
      const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
      console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF que será convertido.
1. Inicializa el módulo AsposePdf. Recibe el objeto si es exitoso.
1. Llama a la función [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
1. Convierte el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToPng{0:D2}.png". Donde {0:D2} representa el número de página en un formato de dos dígitos. Las imágenes se guardan con una resolución de 150 DPI. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convertir un archivo PDF a PNG con la plantilla "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... formato de número de página), resolución 150 DPI y guardar*/
  const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
  console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


{{% alert color="success" %}}
**Intenta convertir PDF a SVG en línea**

Aspose.PDF para Node.js te presenta una aplicación gratuita en línea ["PDF a SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Aspose.PDF Conversión PDF a SVG con Aplicación Gratuita](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Gráficos Vectoriales Escalables (SVG)** es una familia de especificaciones de un formato de archivo basado en XML para gráficos vectoriales bidimensionales, tanto estáticos como dinámicos (interactivos o animados). La especificación SVG es un estándar abierto que ha estado en desarrollo por el Consorcio World Wide Web (W3C) desde 1999.

## Convertir PDF a SVG

### Convertir PDF a SVG clásico

En caso de que desees convertir un documento PDF, puedes usar la función [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
Por favor, revisa el siguiente fragmento de código para convertir en el entorno de Node.js.


**CommonJS:**

1. Llama a `require` e importa el módulo `asposepdfnodejs` como la variable `AsposePdf`.
1. Especifica el nombre del archivo PDF que será convertido.
1. Llama a `AsposePdf` como Promise y realiza la operación para convertir el archivo. Recibe el objeto si es exitoso.
1. Llama a la función [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
1. Convierte el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToSvg.svg". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convierte un archivo PDF a SVG y guarda el "ResultPdfToSvg.svg"*/
      const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
      console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF que será convertido.
1. Inicializa el módulo AsposePdf. Recibe el objeto si se completa con éxito.
1. Llama a la función [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
1. Convierte el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToSvg.svg". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error se contendrá en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convierte un archivo PDF a SVG y guarda el "ResultPdfToSvg.svg"*/
  const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
  console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

### Convertir PDF a SVG comprimido

En caso de que desees convertir un documento PDF, puedes usar la función [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
 
Please check the following code snippet in order to convert in Node.js environment.

**CommonJS:**

1. Llamar a `require` e importar el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especificar el nombre del archivo PDF que será convertido.
1. Llamar a `AsposePdf` como Promise y realizar la operación para convertir el archivo. Recibir el objeto si es exitoso.
1. Llamar a la función [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
1. Convertir el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToSvgZip.zip". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error se contendrá en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convertir un archivo PDF a SVG(zip) y guardar en "ResultPdfToSvgZip.zip"*/
      const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
      console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF que se convertirá
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llama a la función [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
1. Convierte el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToSvgZip.zip". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error se contendrá en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*convierte un archivo PDF a SVG zip y guarda en "ResultPdfToSvgZip.zip"*/
  const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
  console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText)
```

## Convertir PDF a DICOM

En caso de que desees convertir un documento PDF, puedes usar la función [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
 
Por favor, revise el siguiente fragmento de código para convertir en un entorno Node.js.

**CommonJS:**

1. Llame a `require` e importe el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifique el nombre del archivo PDF que será convertido.
1. Llame a `AsposePdf` como Promesa y realice la operación para convertir el archivo. Reciba el objeto si tiene éxito.
1. Llame a la función [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
1. Convierta el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToDICOM{0:D2}.dcm". Donde {0:D2} representa el número de página con un formato de dos dígitos. Las imágenes se guardan con una resolución de 150 DPI. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convertir un archivo PDF a DICOM con la plantilla "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... formato de número de página), resolución 150 DPI y guardar*/
      const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
      console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF que se convertirá.
1. Inicializa el módulo AsposePdf. Recibe el objeto si es exitoso.
1. Llama a la función [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
1. Convierte el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToDICOM{0:D2}.dcm". Donde {0:D2} representa el número de página con un formato de dos dígitos. Las imágenes se guardan con una resolución de 150 DPI. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se contendrá en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convierte un archivo PDF a DICOM con la plantilla "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... formato número de página), resolución 150 DPI y guarda*/
  const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
  console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


## Convertir PDF a BMP

En caso de que desees convertir un documento PDF, puedes utilizar la función [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/). 
Por favor revisa el siguiente fragmento de código para realizar la conversión en un entorno Node.js.

**CommonJS:**

1. Llama a `require` e importa el módulo `asposepdfnodejs` como la variable `AsposePdf`.
1. Especifica el nombre del archivo PDF que será convertido.
1. Llama a `AsposePdf` como Promise y realiza la operación para convertir el archivo. Recibe el objeto si es exitoso.
1. Llama a la función [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/).

1. Convertir archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToBmp{0:D2}.bmp". Donde {0:D2} representa el número de página con un formato de dos dígitos. Las imágenes se guardan con una resolución de 150 DPI. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se contendrá en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convertir un archivo PDF a BMP con la plantilla "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... formato de número de página), resolución 150 DPI y guardar*/
      const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
      console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el módulo `asposepdfnodejs`.
1. Especificar el nombre del archivo PDF que será convertido.

1. Inicializar el módulo AsposePdf. Recibir el objeto si tiene éxito.
1. Llamar a la función [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/).
1. Convertir archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfToBmp{0:D2}.bmp". Donde {0:D2} representa el número de página con un formato de dos dígitos. Las imágenes se guardan con una resolución de 150 DPI. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convertir un archivo PDF a BMP con la plantilla "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... número de página en formato), resolución 150 DPI y guardar*/
  const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
  console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```