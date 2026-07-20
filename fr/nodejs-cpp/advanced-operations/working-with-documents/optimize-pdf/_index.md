---
title: Optimiser le PDF à l'aide d'Aspose.PDF for Node.js via C++
linktitle: Optimiser le fichier PDF
type: docs
weight: 10
url: /fr/nodejs-cpp/optimize-pdf/
description: Optimiser et compresser les fichiers PDF pour une visualisation Web rapide en utilisant l'environnement Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Optimiser le document PDF

La boîte à outils d'Aspose.PDF for Node.js via C++ vous permet d'optimiser le contenu PDF pour l'environnement Node.js. 

L'optimisation, ou la linéarisation, désigne le processus consistant à rendre un fichier PDF adapté à la navigation en ligne à l'aide d'un navigateur Web.

Dans le cas où vous souhaitez optimiser le PDF, vous pouvez utiliser [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/) fonction. 
Veuillez consulter l'extrait de code suivant afin d'optimiser les fichiers PDF dans un environnement Node.js.

**CommonJS :**

1. Appel `require` et importer `asposepdfnodejs` module en tant que `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF qui sera optimisé.
1. Appel `AsposePdf` en tant que Promise et effectuer l'opération d'optimisation du fichier. Recevoir l'objet en cas de succès.
1. Appelez la fonction [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. Optimisez un fichier PDF. Ainsi, si ’json.errorCode’ est 0, le résultat de l'opération est enregistré dans "ResultOptimize.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans ’json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Optimize a PDF-file and save the "ResultOptimize.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
      console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF qui sera optimisé.
1. Initialisez le module AsposePdf. Recevez l'objet si la opération réussit.
1. Appelez la fonction [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. Optimisez un fichier PDF. Ainsi, si ’json.errorCode’ est 0, le résultat de l'opération est enregistré dans "ResultOptimize.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans ’json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Optimize a PDF-file and save the "ResultOptimize.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
  console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```