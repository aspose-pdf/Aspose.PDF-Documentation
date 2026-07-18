---
title: Définir la couleur d'arrière-plan du PDF dans Node.js
linktitle: Définir la couleur d'arrière-plan
type: docs
weight: 80
url: /fr/nodejs-cpp/set-background-color/
description: Définir la couleur d'arrière-plan pour votre fichier PDF avec Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Au cas où vous voudriez définir la couleur d'arrière-plan du PDF, vous pouvez utiliser [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/) fonction. 

Veuillez vérifier le fragment de code suivant afin de définir la couleur d'arrière-plan du PDF dans un environnement Node.js.

**CommonJS :**

1. Appel `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF dont vous souhaitez définir la couleur d'arrière-plan.
1. Appel `AsposePdf` en tant que Promise et exécuter l'opération de définition de la couleur d'arrière-plan. Recevez l'objet si l'opération réussit.
1. Appelez la fonction [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/). 
1. Définissez la couleur d'arrière-plan du fichier PDF. Vous devez transmettre 3 arguments à cette fonction : un nom de fichier d'entrée, une couleur souhaitée au format hexadécimal, et un nom de fichier de sortie. Ainsi, si 'json.errorCode' vaut 0, le résultat de l'opération est enregistré dans "ResultRotation.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set the background color for the PDF-file and save the "ResultPdfSetBackgroundColor.pdf"*/
      const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
      console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF dont vous souhaitez définir la couleur d'arrière-plan.
1. Initialisez le module AsposePdf. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/). 
1. Définissez la couleur d'arrière-plan du fichier PDF. La couleur d'arrière-plan est définie sur "#426bf4", qui est un code couleur hexadécimal représentant une nuance de bleu. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultRotation.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set the background color for the PDF-file and save the "ResultPdfSetBackgroundColor.pdf"*/
  const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
  console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```