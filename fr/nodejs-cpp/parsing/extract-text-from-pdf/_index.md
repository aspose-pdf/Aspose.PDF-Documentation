---
title: Analyser le texte d'un PDF en Node.js
linktitle: Analyser le texte d'un PDF
type: docs
weight: 30
url: /fr/nodejs-cpp/extract-text-from-pdf/
description: Cet article décrit différentes façons d'analyser le texte des documents PDF à l'aide d'Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Analyser le texte d'un document PDF

L'analyse du texte du document PDF est une tâche très courante et utile. 
L'extraction de texte à partir de fichiers PDF répond à de multiples objectifs, de l'amélioration de la recherche et de la disponibilité à la facilitation de l'analyse et de l'automatisation des données dans divers secteurs tels que les affaires, la recherche et la gestion de l'information.

Dans le cas où vous souhaitez extraire du texte d'un document PDF, vous pouvez utiliser [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/) fonction. 
Veuillez consulter le fragment de code suivant afin d'extraire du texte d'un fichier PDF en utilisant Node.js via C\u002B\u002B.

Vérifiez les extraits de code et suivez les étapes pour extraire le texte de votre PDF :

**CommonJS :**

1. Appel `require` et importer `asposepdfnodejs` module en tant que `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF à partir duquel le texte sera extrait.
1. Appel `AsposePdf` en tant que Promise et effectuer l'opération d'extraction de texte. Recevez l'objet si le traitement réussit.
1. Appelez la fonction [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. Le texte extrait est stocké dans l'objet JSON. Ainsi, si 'json.errorCode' est 0, le texte extrait est affiché à l'aide de console.log. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extract text from a PDF-file*/
      const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
      console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF à partir duquel le texte sera extrait.
1. Initialisez le module AsposePdf. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. Le texte extrait est stocké dans l'objet JSON. Ainsi, si 'json.errorCode' est 0, le texte extrait est affiché à l'aide de console.log. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Extract text from a PDF-file*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```