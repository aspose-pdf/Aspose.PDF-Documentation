---
title: Faire pivoter les pages PDF en Node.js
linktitle: Faire pivoter les pages PDF
type: docs
weight: 50
url: /fr/nodejs-cpp/rotate-pages/
description: Ce sujet décrit comment faire pivoter l'orientation des pages dans un fichier PDF existant de manière programmatique dans un environnement Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Cette section décrit comment faire pivoter les pages d'un fichier PDF existant en utilisant Aspose.PDF pour Node.js via C++.

Si vous souhaitez faire pivoter les pages PDF, vous pouvez utiliser la fonction [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). Cette fonction utilise un paramètre spécial 'AsposePdfModule.Rotation' pour la valeur de rotation. Avec cela, vous pouvez définir de combien de degrés vous avez besoin de faire pivoter le PDF. Il y a des variantes : Aucun, 90, 180 ou 270 degrés.

Veuillez consulter l'extrait de code suivant afin de faire pivoter les pages PDF dans un environnement Node.js.

**CommonJS:**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.

1. Spécifiez le nom du fichier PDF à faire pivoter.
1. Appelez `AsposePdf` en tant que Promesse et effectuez l'opération de rotation des pages. Recevez l'objet si l'opération réussit.
1. Appelez la fonction [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/).
1. Faites pivoter tous les fichiers PDF. La rotation est réglée à 270 degrés (on270). Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultRotation.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js
  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Faire pivoter les pages PDF et enregistrer dans "ResultRotation.pdf"*/
      const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
      console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF à faire pivoter.
1. Initialisez le module AsposePdf. Recevez l'objet si l'initialisation réussit.
1. Appelez la fonction [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/).
1. Faites pivoter tous les fichiers PDF. La rotation est réglée sur 270 degrés (on270). Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultRotation.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Faire pivoter les pages PDF et sauvegarder dans "ResultRotation.pdf"*/
  const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
  console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```