---
title: Réparer le PDF dans Node.js
linktitle: Réparer le PDF
type: docs
weight: 10
url: /fr/nodejs-cpp/repair-pdf/
description: Cet article décrit comment réparer le PDF dans l'environnement Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for Node.js permet une réparation de PDF de haute qualité. Le fichier PDF peut ne pas s'ouvrir pour quelque raison que ce soit, quel que soit le programme ou le navigateur. Dans certains cas, le document peut être restauré, essayez le code suivant et voyez par vous-même.
Dans le cas où vous souhaiteriez réparer un document PDF, vous pouvez utiliser [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/) fonction. 
Veuillez vérifier le fragment de code suivant afin de réparer le fichier PDF dans l'environnement Node.js.

**CommonJS:**

1. Appel `require` et importer `asposepdfnodejs` module en tant que `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF qui sera réparé.
1. Appel `AsposePdf` en tant que Promise et exécuter l'opération de réparation du fichier. Recevez l'objet si succès.
1. Appeler la fonction [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. Réparer le fichier PDF. Ainsi, si 'json.errorCode' vaut 0, le résultat de l'opération est enregistré dans "ResultPdfRepair.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
    /*Repair a PDF-file and save the "ResultPdfRepair.pdf"*/
    const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
    console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF qui sera réparé.
1. Initialisez le module AsposePdf. Recevez l'objet si l'opération réussit.
1. Appeler la fonction [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. Réparer le fichier PDF. Ainsi, si 'json.errorCode' vaut 0, le résultat de l'opération est enregistré dans "ResultPdfRepair.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Repair a PDF-file and save the "ResultPdfRepair.pdf"*/
  const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
  console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```