---
title: Convertir le PDF en formats d'image dans Node.js
linktitle: Convertir le PDF en images
type: docs
weight: 70
url: /fr/nodejs-cpp/convert-pdf-to-images-format/
lastmod: "2026-07-18"
description: Ce sujet vous montre comment utiliser Aspose.PDF pour convertir des PDF en divers formats d'images, par ex. TIFF, BMP, JPEG, PNG, SVG, avec quelques lignes de code dans l'environnement Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Node.js Convertir PDF en image

Dans cet article, nous vous présenterons les options de conversion du PDF vers des formats d'image.

Les documents numérisés précédemment sont souvent enregistrés au format de fichier PDF. Cependant, avez-vous besoin de les éditer dans un éditeur graphique ou de les envoyer ultérieurement au format image ? Nous avons un outil universel pour vous convertir le PDF en images en utilisant 
La tâche la plus courante est lorsque vous devez enregistrer un document PDF complet ou certaines pages spécifiques d'un document sous forme d'un ensemble d'images. **Aspose for Node.js via C++** vous permet de convertir des PDF aux formats JPG et PNG afin de simplifier les étapes nécessaires pour obtenir vos images à partir d'un fichier PDF spécifique.

**Aspose.PDF for Node.js via C++** prend en charge diverses conversions de PDF en formats d'image. Veuillez vérifier la section [Formats de fichiers pris en charge par Aspose.PDF](https://docs.aspose.com/pdf/nodejs-cpp/supported-file-formats/).

{{% alert color="success" %}}
**Essayez de convertir le PDF en JPEG en ligne**

Aspose.PDF for Node.js vous présente une application en ligne gratuite ["PDF en JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), où vous pouvez tenter d’enquêter sur la fonctionnalité et la qualité de son fonctionnement.

[![Conversion PDF en JPEG avec l'application gratuite Aspose.PDF](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## Convertir le PDF en JPEG

Dans le cas où vous souhaitez convertir un document PDF, vous pouvez utiliser [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/) fonction. 
Veuillez vérifier le fragment de code suivant afin de le convertir dans un environnement Node.js.

**CommonJS:**

1. Appeler `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appeler `AsposePdf` en tant que Promise et exécuter l'opération de conversion de fichier. Recevoir l'objet si réussi.
1. Appelez la fonction [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).
1. Convertir le fichier PDF. Ainsi, si \u0027json.errorCode\u0027 est 0, le résultat de l'opération est enregistré dans \u0022ResultPdfToJpg{0:D2}.jpg\u0022. Où {0:D2} représente le numéro de page au format à deux chiffres. Les images sont enregistrées avec une résolution de 150 DPI. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans \u0027json.errorText\u0027.

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

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF qui sera converti
1. Initialisez le module AsposePdf. Recevez l'objet si le processus réussit.
1. Appelez la fonction [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).
1. Convertir le fichier PDF. Ainsi, si \u0027json.errorCode\u0027 est 0, le résultat de l'opération est enregistré dans \u0022ResultPdfToJpg{0:D2}.jpg\u0022. Où {0:D2} représente le numéro de page au format à deux chiffres. Les images sont enregistrées avec une résolution de 150 DPI. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans \u0027json.errorText\u0027.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to JPG with template "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
  console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

{{% alert color="success" %}}
**Essayez de convertir le PDF en TIFF en ligne**

Aspose.PDF for Node.js vous présente une application en ligne gratuite ["PDF vers TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), où vous pouvez tenter d’enquêter sur la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF de PDF en TIFF avec l'application gratuite](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Convertir PDF en TIFF

Dans le cas où vous souhaitez convertir un document PDF, vous pouvez utiliser [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/) fonction. 
Veuillez vérifier le fragment de code suivant afin de le convertir dans un environnement Node.js.

**CommonJS:**

1. Appeler `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appeler `AsposePdf` en tant que Promise et exécuter l'opération de conversion de fichier. Recevoir l'objet si réussi.
1. Appelez la fonction [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfToTiff{0:D2}.tiff". Où {0:D2} représente le numéro de page au format à deux chiffres. Les images sont enregistrées avec une résolution de 150 DPI. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

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

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF qui sera converti
1. Initialisez le module AsposePdf. Recevez l'objet si le processus réussit.
1. Appelez la fonction [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfToTiff{0:D2}.tiff". Où {0:D2} représente le numéro de page au format à deux chiffres. Les images sont enregistrées avec une résolution de 150 DPI. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to TIFF with template "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
  console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

{{% alert color="success" %}}
**Essayez de convertir le PDF en PNG en ligne**

À titre d'exemple de la façon dont nos applications gratuites fonctionnent, veuillez vérifier la fonctionnalité suivante.

Aspose.PDF for Node.js vous présente une application en ligne gratuite ["PDF en PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), où vous pouvez tenter d’enquêter sur la fonctionnalité et la qualité de son fonctionnement.

[![Comment convertir un PDF en PNG à l'aide d'une application gratuite](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Convertir le PDF en PNG

Dans le cas où vous souhaitez convertir un document PDF, vous pouvez utiliser [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/) fonction. 
Veuillez vérifier le fragment de code suivant afin de le convertir dans un environnement Node.js.

**CommonJS:**

1. Appeler `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appeler `AsposePdf` en tant que Promise et exécuter l'opération de conversion de fichier. Recevoir l'objet si réussi.
1. Appelez la fonction [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfToPng{0:D2}.png". Où {0:D2} représente le numéro de page au format à deux chiffres. Les images sont enregistrées avec une résolution de 150 DPI. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

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

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF qui sera converti
1. Initialisez le module AsposePdf. Recevez l'objet si le processus réussit.
1. Appelez la fonction [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfToPng{0:D2}.png". Où {0:D2} représente le numéro de page au format à deux chiffres. Les images sont enregistrées avec une résolution de 150 DPI. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to PNG with template "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
  console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

{{% alert color="success" %}}
**Essayez de convertir le PDF en SVG en ligne**

Aspose.PDF for Node.js vous présente une application en ligne gratuite ["PDF en SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), où vous pouvez tenter d’enquêter sur la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en SVG avec l'application gratuite](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** est une famille de spécifications d'un format de fichier basé sur XML pour les graphiques vectoriels bidimensionnels, à la fois statiques et dynamiques (interactifs ou animés). La spécification SVG est une norme ouverte qui est en cours de développement par le World Wide Web Consortium (W3C) depuis 1999.

## Convertir le PDF en SVG

### Convertir le PDF en SVG classique

Dans le cas où vous souhaitez convertir un document PDF, vous pouvez utiliser [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/) fonction. 
Veuillez vérifier le fragment de code suivant afin de le convertir dans un environnement Node.js.

**CommonJS:**

1. Appeler `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appeler `AsposePdf` en tant que Promise et exécuter l'opération de conversion de fichier. Recevoir l'objet si réussi.
1. Appelez la fonction [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' vaut 0, le résultat de l'opération est enregistré dans "ResultPdfToSvg.svg". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

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

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF qui sera converti
1. Initialisez le module AsposePdf. Recevez l'objet si le processus réussit.
1. Appelez la fonction [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' vaut 0, le résultat de l'opération est enregistré dans "ResultPdfToSvg.svg". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to SVG and save the "ResultPdfToSvg.svg"*/
  const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
  console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

### Convertir le PDF en SVG compressé

Dans le cas où vous souhaitez convertir un document PDF, vous pouvez utiliser [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/) fonction. 
Veuillez vérifier le fragment de code suivant afin de le convertir dans un environnement Node.js.

**CommonJS:**

1. Appeler `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appeler `AsposePdf` en tant que Promise et exécuter l'opération de conversion de fichier. Recevoir l'objet si réussi.
1. Appelez la fonction [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfToSvgZip.zip". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

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

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF qui sera converti
1. Initialisez le module AsposePdf. Recevez l'objet si le processus réussit.
1. Appelez la fonction [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfToSvgZip.zip". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*convert a PDF-file to SVG zip and save the "ResultPdfToSvgZip.zip"*/
  const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
  console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText)
```

## Convertir le PDF en DICOM

Dans le cas où vous souhaitez convertir un document PDF, vous pouvez utiliser [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/) fonction. 
Veuillez vérifier le fragment de code suivant afin de le convertir dans un environnement Node.js.

**CommonJS:**

1. Appeler `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appeler `AsposePdf` en tant que Promise et exécuter l'opération de conversion de fichier. Recevoir l'objet si réussi.
1. Appelez la fonction [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfToDICOM{0:D2}.dcm". Où {0:D2} représente le numéro de page au format à deux chiffres. Les images sont enregistrées avec une résolution de 150 DPI. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

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

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF qui sera converti
1. Initialisez le module AsposePdf. Recevez l'objet si le processus réussit.
1. Appelez la fonction [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfToDICOM{0:D2}.dcm". Où {0:D2} représente le numéro de page au format à deux chiffres. Les images sont enregistrées avec une résolution de 150 DPI. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to DICOM with template "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
  console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

## Convertir le PDF en BMP

Dans le cas où vous souhaitez convertir un document PDF, vous pouvez utiliser [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/) fonction. 
Veuillez vérifier le fragment de code suivant afin de le convertir dans un environnement Node.js.

**CommonJS:**

1. Appeler `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appeler `AsposePdf` en tant que Promise et exécuter l'opération de conversion de fichier. Recevoir l'objet si réussi.
1. Appelez la fonction [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' vaut 0, le résultat de l'opération est enregistré dans "ResultPdfToBmp{0:D2}.bmp". Où {0:D2} représente le numéro de page au format à deux chiffres. Les images sont enregistrées avec une résolution de 150 DPI. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

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

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF qui sera converti
1. Initialisez le module AsposePdf. Recevez l'objet si le processus réussit.
1. Appelez la fonction [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' vaut 0, le résultat de l'opération est enregistré dans "ResultPdfToBmp{0:D2}.bmp". Où {0:D2} représente le numéro de page au format à deux chiffres. Les images sont enregistrées avec une résolution de 150 DPI. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to BMP with template "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
  console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```





