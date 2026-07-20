---
title: Supprimer les images du fichier PDF dans Node.js
linktitle: Supprimer les images
type: docs
weight: 20
url: /fr/nodejs-cpp/delete-images-from-pdf-file/
description: Cette section explique comment supprimer les images d'un fichier PDF en utilisant Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
---


Vous pouvez supprimer des images d'un fichier PDF en utilisant Aspose.PDF for Node.js via C++.

Dans le cas où vous souhaitez supprimer des images d'un PDF, vous pouvez utiliser [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/) fonction. 
Veuillez vérifier le fragment de code suivant afin de supprimer des images dans un environnement Node.js.

**CommonJS:**

1. Appel `require` et importer `asposepdfnodejs` module en tant que `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF dans lequel l'image sera supprimée.
1. Appel `AsposePdf` en tant que Promise et exécuter l'opération de suppression d'images. Recevoir l'objet si réussi.
1. Appeler la fonction [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
1. Supprimer les images d'un PDF. Ainsi, si 'json.errorCode' vaut 0, le résultat de l'opération est enregistré dans "ResultPdfDeleteImages.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete images from a PDF-file and save the "ResultPdfDeleteImages.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
        console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6 :**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF dans lequel l'image sera supprimée.
1. Initialisez le module AsposePdf. Recevez l'objet si l'opération réussit.
1. Appeler la fonction [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
1. Supprimer les images d'un PDF. Ainsi, si 'json.errorCode' vaut 0, le résultat de l'opération est enregistré dans "ResultPdfDeleteImages.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete images from a PDF-file and save the "ResultPdfDeleteImages.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
    console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```