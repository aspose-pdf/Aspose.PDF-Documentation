---
title: Ajouter un arrière-plan au PDF en Node.js
linktitle: Ajouter un arrière-plan
type: docs
weight: 10
url: /fr/nodejs-cpp/add-background/
description: Ajouter une image d'arrière-plan à votre fichier PDF en Node.js
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Les extraits de code suivants montrent comment ajouter une image d'arrière-plan aux pages PDF en utilisant la fonction [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/) en Node.js.

Veuillez vérifier l'extrait de code suivant afin d'ajouter une image d'arrière-plan dans l'environnement Node.js.

**CommonJS:**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
2. Spécifiez le nom du fichier PDF dans lequel l'image d'arrière-plan sera ajoutée.
3. Appelez `AsposePdf` en tant que Promise et effectuez l'opération pour ajouter une image d'arrière-plan. Recevez l'objet en cas de succès.
4. Appelez la fonction [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/).

1. Ajouter une image de fond à un fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultAddBackgroundImage.pdf". Si le paramètre json.errorCode n'est pas 0 et qu'une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Ajouter une image de fond à un fichier PDF et enregistrer dans "ResultBackgroundImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
      console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6 :**

1. Importer le module `asposepdfnodejs`.
1. Spécifier le nom du fichier PDF dans lequel l'image de fond sera ajoutée.
1. Initialiser le module AsposePdf. Recevoir l'objet en cas de succès.

1. Appelez la fonction [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/).
1. Ajoutez une image de fond à un fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultAddBackgroundImage.pdf". Si le paramètre json.errorCode n'est pas 0 et qu'une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  /*Ajoutez une image de fond à un fichier PDF et enregistrez "ResultBackgroundImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
  console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```