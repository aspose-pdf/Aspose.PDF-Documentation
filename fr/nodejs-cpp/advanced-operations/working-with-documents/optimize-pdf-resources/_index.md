---
title: Optimiser les ressources PDF dans Node.js
linktitle: Optimiser les ressources PDF
type: docs
weight: 15
url: /fr/nodejs-cpp/optimize-pdf-resources/
description: Optimiser les ressources des fichiers PDF pour une vue web rapide en utilisant l'outil Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Optimiser les ressources PDF

Optimiser les ressources dans le document :

1. Les ressources qui ne sont pas utilisées sur les pages du document sont supprimées
1. Les ressources égales sont réunies en un seul objet
1. Les objets inutilisés sont supprimés

Si vous souhaitez optimiser les ressources PDF, vous pouvez utiliser la fonction [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/). 
Veuillez vérifier l'extrait de code suivant pour optimiser les ressources PDF dans l'environnement Node.js.

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` comme variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF pour lequel les ressources seront optimisées.

1. Appelez `AsposePdf` en tant que Promise et effectuez l'opération pour optimiser le fichier. Recevez l'objet si cela réussit.
1. Appelez la fonction [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. Optimisez les ressources d'un PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfOptimizeResource.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Optimiser les ressources du fichier PDF et enregistrer dans "ResultPdfOptimizeResource.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
      console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6 :**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF pour lequel les ressources seront optimisées.
1. Initialisez le module AsposePdf. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. Optimisez les ressources d'un PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfOptimizeResource.pdf". Si le paramètre json.errorCode n'est pas 0 et, par conséquent, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Optimisez les ressources du fichier PDF et enregistrez le "ResultPdfOptimizeResource.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
  console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```