---
title: Extraire des Images d'un PDF en Node.js
linktitle: Extraire des Images d'un PDF
type: docs
weight: 20
url: /fr/nodejs-cpp/extract-images-from-the-pdf-file/
description: Comment extraire une partie de l'image d'un PDF en utilisant Aspose.PDF pour Node.js via l'outil C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraire des images des fichiers PDF dans l'environnement Node.js

Dans le cas où vous souhaitez extraire des images d'un document PDF, vous pouvez utiliser la fonction [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).  
Nous devons passer trois arguments à cette fonction : le nom du fichier d'entrée et de sortie et la résolution.  
Veuillez consulter l'extrait de code suivant pour extraire des images d'un fichier PDF en utilisant Node.js.

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` comme variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF à partir duquel l'image sera extraite.

1. Appelez `AsposePdf` en tant que Promise et effectuez l'opération pour extraire l'image. Recevez l'objet si cela réussit.
1. Appelez la fonction [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. Extrayez les images du fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfExtractImage{0:D2}.jpg". Où {0:D2} représente le numéro de page avec un format à deux chiffres. Les images sont enregistrées avec une résolution de 150 DPI. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extraire une image d'un fichier PDF avec le modèle "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format numéro de page), résolution 150 DPI et enregistrer*/
      const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
      console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF à partir duquel l'image sera extraite.
1. Initialisez le module AsposePdf. Recevez l'objet si cela réussit.
1. Appelez la fonction [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. Extrayez des images du fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfExtractImage{0:D2}.jpg". Où {0:D2} représente le numéro de page avec un format à deux chiffres. Les images sont enregistrées avec une résolution de 150 DPI. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Extraire l'image d'un fichier PDF avec le modèle "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format numéro de page), résolution 150 DPI et sauvegarder*/
    const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
    console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```