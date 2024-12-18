---
title: Réparer un PDF en Node.js 
linktitle: Réparer PDF
type: docs
weight: 10
url: /fr/nodejs-cpp/repair-pdf/
description: Ce sujet décrit comment réparer un PDF dans l'environnement Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF pour Node.js permet une réparation de PDF de haute qualité. Le fichier PDF peut ne pas s'ouvrir pour une raison quelconque, quel que soit le programme ou le navigateur. Dans certains cas, le document peut être restauré, essayez le code suivant et voyez par vous-même. Si vous souhaitez réparer un document PDF, vous pouvez utiliser la fonction [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/). Veuillez vérifier l'extrait de code suivant afin de réparer le fichier PDF dans l'environnement Node.js.

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF qui sera réparé.
1. Appelez `AsposePdf` en tant que Promise et effectuez l'opération de réparation du fichier. Recevez l'objet si réussi.

1. Appelez la fonction [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. Réparez le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfRepair.pdf". Si le paramètre json.errorCode n'est pas 0 et qu'une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
    /*Réparer un fichier PDF et enregistrer le "ResultPdfRepair.pdf"*/
    const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
    console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6 :**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF qui sera réparé.
1. Initialisez le module AsposePdf. Recevez l'objet en cas de succès.

1. Appelez la fonction [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. Réparez le fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfRepair.pdf". Si le paramètre json.errorCode n'est pas 0 et, par conséquent, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Réparez un fichier PDF et enregistrez le "ResultPdfRepair.pdf"*/
  const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
  console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```