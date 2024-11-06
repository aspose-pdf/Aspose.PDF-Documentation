---
title: Suppression des pièces jointes d'un PDF dans Node.js
linktitle: Suppression de la pièce jointe d'un PDF existant
type: docs
weight: 10
url: fr/nodejs-cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF peut supprimer les pièces jointes de vos documents PDF. Utilisez l'environnement Node.js pour supprimer les pièces jointes dans les fichiers PDF avec Aspose.PDF.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Vous pouvez supprimer des pièces jointes d'un fichier PDF en utilisant Aspose.PDF pour Node.js via C++. Si vous souhaitez supprimer des pièces jointes d'un PDF, vous pouvez utiliser la fonction [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/). Veuillez consulter l'extrait de code suivant pour supprimer des pièces jointes d'un fichier PDF dans l'environnement Node.js.

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF dont les pièces jointes seront supprimées.

1. Appelez `AsposePdf` en tant que Promesse et effectuez l'opération de suppression des pièces jointes. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. Supprimez les pièces jointes. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfDeleteAttachments.pdf". Si le paramètre json.errorCode n'est pas 0 et qu'une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Supprimez les pièces jointes d'un fichier PDF et enregistrez le "ResultPdfDeleteAttachments.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
        console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6 :**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF à partir duquel les pièces jointes seront supprimées.
1. Initialisez le module AsposePdf. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. Supprimez les pièces jointes. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfDeleteAttachments.pdf". Si le paramètre json.errorCode n'est pas 0 et qu'une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Supprimez les pièces jointes d'un fichier PDF et enregistrez le "ResultPdfDeleteAttachments.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
    console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```