---
title: Extraire du texte d'un PDF en Node.js
linktitle: Extraire du texte d'un PDF
type: docs
weight: 30
url: /fr/nodejs-cpp/extract-text-from-pdf/
description: Cet article décrit diverses façons d'extraire du texte de documents PDF en utilisant Aspose.PDF pour Node.js via C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraire du texte d'un document PDF

L'extraction de texte d'un document PDF est une tâche très courante et utile. 
Extraire du texte de PDF sert à diverses fins, de l'amélioration de la recherche et de la disponibilité à l'analyse et à l'automatisation des données dans divers domaines tels que les affaires, la recherche et la gestion de l'information.

Si vous souhaitez extraire du texte d'un document PDF, vous pouvez utiliser la fonction [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/). 
Veuillez vérifier l'extrait de code suivant pour extraire du texte d'un fichier PDF en utilisant Node.js via C++.

Vérifiez les extraits de code et suivez les étapes pour extraire du texte de votre PDF :


**CommonJS:**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF à partir duquel le texte sera extrait.
1. Appelez `AsposePdf` en tant que Promise et effectuez l'opération pour extraire le texte. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. Le texte extrait est stocké dans l'objet JSON. Ainsi, si 'json.errorCode' est 0, le texte extrait est affiché en utilisant console.log. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extraire le texte d'un fichier PDF*/
      const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
      console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
  });
```


**ECMAScript/ES6 :**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF à partir duquel le texte sera extrait.
1. Initialisez le module AsposePdf. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. Le texte extrait est stocké dans l'objet JSON. Ainsi, si 'json.errorCode' est 0, le texte extrait est affiché en utilisant console.log. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Extraire le texte d'un fichier PDF*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```