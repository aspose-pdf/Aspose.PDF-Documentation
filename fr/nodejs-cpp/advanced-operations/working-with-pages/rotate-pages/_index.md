---
title: Faire pivoter les pages PDF dans Node.js
linktitle: Faire pivoter les pages PDF
type: docs
weight: 50
url: /fr/nodejs-cpp/rotate-pages/
description: Ce sujet décrit comment faire pivoter l'orientation des pages dans un fichier PDF existant de manière programmatique dans un environnement Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Cette section décrit comment faire pivoter les pages d'un fichier PDF existant en utilisant Aspose.PDF for Node.js via C++.

Dans le cas où vous souhaitez faire pivoter des pages PDF, vous pouvez utiliser [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/) fonction. Cette fonction utilise un paramètre spécial 'AsposePdfModule.Rotation' pour la valeur de rotation. Avec celui-ci, vous pouvez définir le nombre de degrés nécessaires pour faire pivoter le PDF. Les variantes sont : None, 90, 180 ou 270 degrés.

Veuillez vérifier le fragment de code suivant afin de faire pivoter les pages PDF dans un environnement Node.js.

**CommonJS:**

1. Appeler `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF à faire pivoter.
1. Appeler `AsposePdf` comme Promise et effectuez l'opération de rotation des pages. Recevez l'objet si réussi.
1. Appeler la fonction [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). 
1. Faire pivoter tous les fichiers PDF. La rotation est réglée à 270 degrés (on270). Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultRotation.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Rotate PDF-pages and save the "ResultRotation.pdf"*/
      const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
      console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6 :**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF à faire pivoter.
1. Initialisez le module AsposePdf. Recevez l'objet si l'opération réussit.
1. Appeler la fonction [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). 
1. Faire pivoter tous les fichiers PDF. La rotation est réglée à 270 degrés (on270). Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultRotation.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Rotate PDF-pages and save the "ResultRotation.pdf"*/
  const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
  console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```