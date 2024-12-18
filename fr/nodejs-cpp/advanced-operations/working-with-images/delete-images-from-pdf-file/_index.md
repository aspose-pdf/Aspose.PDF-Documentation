---
title: Supprimer des Images d'un Fichier PDF en Node.js
linktitle: Supprimer des Images
type: docs
weight: 20
url: /fr/nodejs-cpp/delete-images-from-pdf-file/
description: Cette section explique comment supprimer des Images d'un Fichier PDF en utilisant Aspose.PDF pour Node.js via C++.
lastmod: "2023-11-16"
---

Vous pouvez supprimer des images d'un fichier PDF en utilisant Aspose.PDF pour Node.js via C++.

Dans le cas où vous souhaitez supprimer des images d'un PDF, vous pouvez utiliser la fonction [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/). 
Veuillez vérifier l'extrait de code suivant afin de supprimer des images dans un environnement Node.js.

**CommonJS:**

1. Appelez `require` et importez le module `asposepdfnodejs` comme variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF dans lequel l'image sera supprimée.
1. Appelez `AsposePdf` en tant que Promesse et effectuez l'opération pour supprimer les images. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).

1. Supprimer des images d'un PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfDeleteImages.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Supprimer des images d'un fichier PDF et enregistrer le "ResultPdfDeleteImages.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
        console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Importer le module `asposepdfnodejs`.
1. Spécifier le nom du fichier PDF dans lequel l'image sera supprimée.
1. Initialiser le module AsposePdf. Recevoir l'objet si réussi.

1. Appelez la fonction [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
1. Supprimez les images d'un PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfDeleteImages.pdf". Si le paramètre json.errorCode n'est pas 0 et, par conséquent, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Supprimez les images d'un fichier PDF et enregistrez "ResultPdfDeleteImages.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
    console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```