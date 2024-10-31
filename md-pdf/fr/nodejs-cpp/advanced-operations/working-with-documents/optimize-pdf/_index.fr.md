---
title: Optimiser le PDF en utilisant Aspose.PDF pour Node.js via C++
linktitle: Optimiser le fichier PDF
type: docs
weight: 10
url: /nodejs-cpp/optimize-pdf/
description: Optimiser et compresser les fichiers PDF pour une visualisation web rapide en utilisant l'environnement Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Optimiser le document PDF

Le kit d'outils Aspose.PDF pour Node.js via C++ vous permet d'optimiser le contenu PDF pour l'environnement Node.js.

L'optimisation, ou linéarisation, fait référence au processus de rendre un fichier PDF adapté à la navigation en ligne à l'aide d'un navigateur web.

Dans le cas où vous souhaitez optimiser un PDF, vous pouvez utiliser la fonction [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
Veuillez consulter l'extrait de code suivant afin d'optimiser les fichiers PDF dans l'environnement Node.js.

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF qui sera optimisé.

1. Appelez `AsposePdf` en tant que Promise et effectuez l'opération pour optimiser le fichier. Recevez l'objet si cela réussit.
1. Appelez la fonction [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. Optimisez un fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultOptimize.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Optimiser un fichier PDF et enregistrer le "ResultOptimize.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
      console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF qui sera optimisé.

1. Initialisez le module AsposePdf. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. Optimisez un fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultOptimize.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Optimisez un fichier PDF et enregistrez le "ResultOptimize.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
  console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```