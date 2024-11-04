---
title: Ajouter une image au PDF dans Node.js 
linktitle: Ajouter une image
type: docs
weight: 10
url: /nodejs-cpp/add-image-to-pdf/
description: Cette section décrit comment ajouter une image à un fichier PDF existant en utilisant Aspose.PDF pour Node.js via C++.
lastmod: "2023-11-16"
---

## Ajouter une image à un fichier PDF existant

Il est communément admis que l'ajout d'images aux fichiers PDF nécessite un outil spécial complexe. Cependant, avec Aspose.PDF pour Node.js, vous pouvez rapidement et facilement ajouter les images dont vous avez besoin dans l'environnement Node.js.

Nous pouvons ajouter des images uniquement à la fin du fichier, donc l'exemple correct est que nous avons des pages de documents scannées et les convertissons en un seul PDF.

Dans le cas où vous souhaitez ajouter des images, vous pouvez utiliser la fonction [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/). 
Veuillez consulter l'extrait de code suivant pour ajouter des images dans l'environnement Node.js.

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.

1. Spécifiez le nom du fichier PDF dans lequel l'image sera ajoutée.
1. Appelez `AsposePdf` en tant que Promise et effectuez l'opération d'ajout d'image. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. Ajoutez l'image à la fin d'un PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultAddImage.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js
  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Ajoutez une image à la fin d'un fichier PDF et enregistrez le "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
      console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF dans lequel l'image sera ajoutée.
1. Initialisez le module AsposePdf. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. Ajoutez une image à la fin d'un PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultAddImage.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, l'information sur l'erreur sera contenue dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  /*Ajoutez une image à la fin d'un fichier PDF et enregistrez le "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
  console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```