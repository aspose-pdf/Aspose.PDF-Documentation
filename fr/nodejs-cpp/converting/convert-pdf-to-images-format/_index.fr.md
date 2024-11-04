---
title: Convertir PDF en Formats d'Image dans Node.js
linktitle: Convertir PDF en Images
type: docs
weight: 70
url: /nodejs-cpp/convert-pdf-to-images-format/
lastmod: "2023-11-16"
description: Ce sujet vous montre comment utiliser Aspose.PDF pour convertir un PDF en divers formats d'images tels que TIFF, BMP, JPEG, PNG, SVG avec quelques lignes de code dans l'environnement Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Node.js Convertir PDF en Image

Dans cet article, nous vous montrerons les options pour convertir un PDF en formats d'image.

Les documents précédemment numérisés sont souvent enregistrés au format de fichier PDF. Cependant, avez-vous besoin de le modifier dans un éditeur graphique ou de l'envoyer ensuite au format image ? Nous avons un outil universel pour vous permettre de convertir un PDF en images utilisant 
La tâche la plus courante est lorsque vous devez enregistrer un document PDF entier ou certaines pages spécifiques d'un document sous forme d'un ensemble d'images.
 **Aspose pour Node.js via C++** vous permet de convertir des PDF aux formats JPG et PNG pour simplifier les étapes nécessaires pour obtenir vos images à partir d'un fichier PDF spécifique.

**Aspose.PDF pour Node.js via C++** prend en charge la conversion de divers formats d'image PDF. Veuillez consulter la section [Formats de fichiers pris en charge par Aspose.PDF](https://docs.aspose.com/pdf/nodejs-cpp/supported-file-formats/).

{{% alert color="success" %}}
**Essayez de convertir PDF en JPEG en ligne**

Aspose.PDF pour Node.js vous présente l'application en ligne gratuite ["PDF to JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF PDF en JPEG avec application gratuite](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## Convertir PDF en JPEG

Dans le cas où vous souhaitez convertir un document PDF, vous pouvez utiliser la fonction [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).

Veuillez consulter l'extrait de code suivant pour effectuer la conversion dans un environnement Node.js.
**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appelez `AsposePdf` en tant que Promise et effectuez l'opération de conversion du fichier. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).
1. Convertissez le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfToJpg{0:D2}.jpg". Où {0:D2} représente le numéro de page avec un format à deux chiffres. Les images sont enregistrées avec une résolution de 150 DPI. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convertir un fichier PDF en JPG avec le modèle "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format du numéro de page), résolution de 150 DPI et enregistrer*/
      const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
      console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Initialisez le module AsposePdf. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).
1. Convertissez le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfToJpg{0:D2}.jpg". Où {0:D2} représente le numéro de page avec un format à deux chiffres. Les images sont enregistrées avec une résolution de 150 DPI. Si le paramètre json.errorCode n'est pas 0 et, par conséquent, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convertir un fichier PDF en JPG avec le modèle "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format numéro de page), résolution 150 DPI et enregistrer*/
  const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
  console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


{{% alert color="success" %}}
**Essayez de convertir un PDF en TIFF en ligne**

Aspose.PDF pour Node.js vous propose une application en ligne gratuite ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF de PDF en TIFF avec une application gratuite](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Convertir PDF en TIFF

Dans le cas où vous souhaitez convertir un document PDF, vous pouvez utiliser la fonction [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/). 
Veuillez consulter l'extrait de code suivant afin de convertir dans l'environnement Node.js.

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appelez `AsposePdf` en tant que promesse et effectuez l'opération de conversion du fichier. Recevez l'objet en cas de succès.

1. Appelez la fonction [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/).
1. Convertissez le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfToTiff{0:D2}.tiff". Où {0:D2} représente le numéro de page avec un format à deux chiffres. Les images sont enregistrées avec une résolution de 150 DPI. Si le paramètre json.errorCode n'est pas 0 et, par conséquent, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convertir un fichier PDF en TIFF avec le modèle "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... numéro de page au format), résolution 150 DPI et enregistrer*/
      const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
      console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Initialisez le module AsposePdf. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/).
1. Convertissez le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfToTiff{0:D2}.tiff". Où {0:D2} représente le numéro de page avec un format à deux chiffres. Les images sont enregistrées avec une résolution de 150 DPI. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convertir un fichier PDF en TIFF avec le modèle "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... format numéro de page), résolution 150 DPI et enregistrer*/
  const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
  console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


{{% alert color="success" %}}
**Essayez de convertir un PDF en PNG en ligne**

À titre d'exemple de la manière dont nos applications gratuites fonctionnent, veuillez vérifier la fonctionnalité suivante.

Aspose.PDF pour Node.js vous présente l'application gratuite en ligne ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Comment convertir un PDF en PNG en utilisant l'application gratuite](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Convertir PDF en PNG

Dans le cas où vous souhaitez convertir un document PDF, vous pouvez utiliser la fonction [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/). 
Veuillez vérifier l'extrait de code suivant afin de convertir dans un environnement Node.js.

**CommonJS:**

1. Appelez `require` et importez le module `asposepdfnodejs` comme variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appelez `AsposePdf` en tant que Promise et effectuez l'opération pour convertir le fichier. Recevez l'objet en cas de succès.

1. Appelez la fonction [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfToPng{0:D2}.png". Où {0:D2} représente le numéro de page avec un format à deux chiffres. Les images sont enregistrées avec une résolution de 150 DPI. Si le paramètre json.errorCode n'est pas 0 et qu'une erreur apparaît donc dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convertir un fichier PDF en PNG avec le modèle "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... format numéro de page), résolution 150 DPI et enregistrer*/
      const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
      console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6 :**

1. Importer le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Initialisez le module AsposePdf. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfToPng{0:D2}.png". Où {0:D2} représente le numéro de page avec un format à deux chiffres. Les images sont enregistrées avec une résolution de 150 DPI. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, l'information sur l'erreur sera contenue dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convertir un fichier PDF en PNG avec le modèle "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... format numéro de page), résolution 150 DPI et enregistrer*/
  const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
  console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


{{% alert color="success" %}}
**Essayez de convertir PDF en SVG en ligne**

Aspose.PDF pour Node.js vous présente une application en ligne gratuite ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Conversion PDF en SVG avec l'application gratuite Aspose.PDF](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** est une famille de spécifications d'un format de fichier basé sur XML pour les graphiques vectoriels bidimensionnels, à la fois statiques et dynamiques (interactifs ou animés). La spécification SVG est une norme ouverte qui est en développement par le World Wide Web Consortium (W3C) depuis 1999.

## Convertir PDF en SVG

### Convertir PDF en SVG classique

Dans le cas où vous souhaitez convertir un document PDF, vous pouvez utiliser la fonction [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
Veuillez vérifier l'extrait de code suivant afin de convertir dans l'environnement Node.js.


**CommonJS:**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appelez `AsposePdf` comme Promise et effectuez l'opération de conversion du fichier. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
1. Convertissez le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfToSvg.svg". Si le paramètre json.errorCode n'est pas 0 et qu'une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convertir un fichier PDF en SVG et enregistrer le "ResultPdfToSvg.svg"*/
      const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
      console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF qui sera converti
1. Initialisez le module AsposePdf. Recevez l'objet si cela réussit.
1. Appelez la fonction [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
1. Convertissez le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfToSvg.svg". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convertir un fichier PDF en SVG et enregistrer le "ResultPdfToSvg.svg"*/
  const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
  console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

### Convertir PDF en SVG zippé

Au cas où vous voudriez convertir un document PDF, vous pouvez utiliser la fonction [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
 
Veuillez vérifier l'extrait de code suivant afin de le convertir dans l'environnement Node.js.

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appelez `AsposePdf` en tant que Promise et effectuez l'opération de conversion de fichier. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
1. Convertissez le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfToSvgZip.zip". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convertir un fichier PDF en SVG(zip) et enregistrer le "ResultPdfToSvgZip.zip"*/
      const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
      console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Initialisez le module AsposePdf. Recevez l'objet si cela réussit.
1. Appelez la fonction [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
1. Convertissez le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfToSvgZip.zip". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*convertir un fichier PDF en SVG zip et enregistrer le "ResultPdfToSvgZip.zip"*/
  const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
  console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText)
```

## Convertir PDF en DICOM

Si vous souhaitez convertir un document PDF, vous pouvez utiliser la fonction [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
 
Veuillez vérifier l'extrait de code suivant afin de le convertir dans l'environnement Node.js.

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appelez `AsposePdf` comme une Promesse et effectuez l'opération de conversion du fichier. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
1. Convertissez le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfToDICOM{0:D2}.dcm". Où {0:D2} représente le numéro de page avec un format à deux chiffres. Les images sont enregistrées avec une résolution de 150 DPI. Si le paramètre json.errorCode n'est pas 0 et qu'une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convertir un fichier PDF en DICOM avec le modèle "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... format numéro de page), résolution 150 DPI et sauvegarder*/
      const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
      console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importer le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Initialisez le module AsposePdf. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfToDICOM{0:D2}.dcm". Où {0:D2} représente le numéro de page avec un format à deux chiffres. Les images sont enregistrées avec une résolution de 150 DPI. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convertir un fichier PDF en DICOM avec le modèle "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... format numéro de page), résolution 150 DPI et sauvegarder*/
  const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
  console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


## Convertir PDF en BMP

Au cas où vous voudriez convertir un document PDF, vous pouvez utiliser la fonction [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/). Veuillez vérifier l'extrait de code suivant afin de convertir dans un environnement Node.js.

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF qui sera converti.
1. Appelez `AsposePdf` en tant que Promise et effectuez l'opération de conversion du fichier. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/).

1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfToBmp{0:D2}.bmp". Où {0:D2} représente le numéro de page avec un format à deux chiffres. Les images sont enregistrées avec une résolution de 150 DPI. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convertir un fichier PDF en BMP avec le modèle "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... format du numéro de page), résolution 150 DPI et enregistrer*/
      const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
      console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6 :**

1. Importer le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF qui sera converti.

1. Initialiser le module AsposePdf. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/).
1. Convertir le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfToBmp{0:D2}.bmp". Où {0:D2} représente le numéro de page avec un format à deux chiffres. Les images sont enregistrées avec une résolution de 150 DPI. Si le paramètre json.errorCode n'est pas 0 et, par conséquent, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convertir un fichier PDF en BMP avec le modèle "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... format numéro de page), résolution 150 DPI et enregistrer*/
  const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
  console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```