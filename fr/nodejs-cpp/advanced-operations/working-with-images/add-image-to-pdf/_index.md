---
title: Ajouter une image au PDF dans Node.js
linktitle: Ajouter une image
type: docs
weight: 10
url: /fr/nodejs-cpp/add-image-to-pdf/
description: Cette section décrit comment ajouter une image à un fichier PDF existant en utilisant Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
---

## Ajouter une image à un fichier PDF existant

On pense communément que l'ajout d'images aux fichiers PDF nécessite un outil spécial complexe. Cependant, avec Aspose.PDF for Node.js, vous pouvez rapidement et facilement ajouter les images dont vous avez besoin au PDF dans un environnement Node.js.

Nous ne pouvons ajouter des images qu'à la fin du fichier, donc le bon exemple est que nous avons quelques pages de documents numérisés et les convertissons en un seul PDF.

Au cas où vous souhaitez ajouter des images, vous pouvez utiliser [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/) fonction. 
Veuillez consulter le fragment de code suivant afin d'ajouter des images dans un environnement Node.js.

**CommonJS:**

1. Appeler `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF dans lequel l'image sera ajoutée.
1. Appeler `AsposePdf` en tant que Promise et effectuez l'opération d'ajout d'image. Recevez l'objet si elle réussit.
1. Appelez la fonction [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. Ajoutez une image à la fin d'un PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultAddImage.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add an image to end a PDF-file and save the "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
      console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6 :**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF dans lequel l'image sera ajoutée.
1. Initialisez le module AsposePdf. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. Ajoutez une image à la fin d'un PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultAddImage.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  /*Add an image to end a PDF-file and save the "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
  console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```