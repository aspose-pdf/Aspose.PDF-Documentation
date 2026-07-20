---
title: Optimiser les ressources PDF dans Node.js
linktitle: Optimiser les ressources PDF
type: docs
weight: 15
url: /fr/nodejs-cpp/optimize-pdf-resources/
description: Optimiser les ressources des fichiers PDF pour un affichage web rapide à l'aide de l'outil Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Optimiser les ressources PDF

Optimiser les ressources dans le document :

1. Les ressources qui ne sont pas utilisées sur les pages du document sont supprimées
1. Les ressources identiques sont réunies en un seul objet
1. Les objets inutilisés sont supprimés
 

Au cas où vous voudriez optimiser les ressources PDF, vous pouvez utiliser [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/) fonction. 
Veuillez vérifier le fragment de code suivant afin d'optimiser les ressources PDF dans l'environnement Node.js.

**CommonJS:**

1. Appel `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF dont les ressources seront optimisées.
1. Appel `AsposePdf` en tant que Promise et effectuez l'opération d'optimisation du fichier. Recevez l'objet si l'opération réussit.
1. Appelez la fonction [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. Optimisez les ressources d'un PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfOptimizeResource.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Optimize resources of PDF-file and save the "ResultPdfOptimizeResource.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
      console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF dont les ressources seront optimisées.
1. Initialiser le module AsposePdf. Recevoir l'objet si réussi.
1. Appelez la fonction [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. Optimisez les ressources d'un PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfOptimizeResource.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Optimize resources of PDF-file and save the "ResultPdfOptimizeResource.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
  console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```