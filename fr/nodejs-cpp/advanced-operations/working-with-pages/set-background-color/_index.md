---
title: Définir la couleur d'arrière-plan pour PDF en Node.js
linktitle: Définir la couleur d'arrière-plan
type: docs
weight: 80
url: fr/nodejs-cpp/set-background-color/
description: Définissez la couleur d'arrière-plan de votre fichier PDF avec Node.js via C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Dans le cas où vous souhaitez définir la couleur d'arrière-plan d'un PDF, vous pouvez utiliser la fonction [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/).

Veuillez consulter l'extrait de code suivant pour définir la couleur d'arrière-plan d'un PDF dans l'environnement Node.js.

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
2. Spécifiez le nom du fichier PDF dont vous souhaitez définir la couleur d'arrière-plan.
3. Appelez `AsposePdf` en tant que Promise et effectuez l'opération pour définir la couleur d'arrière-plan. Recevez l'objet en cas de succès.

1. Appelez la fonction [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/). 
1. Définissez la couleur de fond pour le fichier PDF. Vous devez passer 3 arguments à cette fonction : un nom de fichier d'entrée, une couleur souhaitée sous forme hexadécimale, et un nom de fichier de sortie. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultRotation.pdf". Si le paramètre json.errorCode n'est pas 0 et qu'une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Définissez la couleur de fond pour le fichier PDF et enregistrez le "ResultPdfSetBackgroundColor.pdf"*/
      const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
      console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF dont vous souhaitez définir la couleur de fond.
1. Initialisez le module AsposePdf. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/).
1. Définissez la couleur de fond pour le fichier PDF. La couleur de fond est définie sur "#426bf4," qui est un code couleur hexadécimal représentant une nuance de bleu. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultRotation.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Définissez la couleur de fond pour le fichier PDF et enregistrez "ResultPdfSetBackgroundColor.pdf"*/
  const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
  console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```