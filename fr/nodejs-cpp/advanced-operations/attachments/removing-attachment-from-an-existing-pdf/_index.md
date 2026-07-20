---
title: Suppression des pièces jointes du PDF dans Node.js
linktitle: Suppression d'une pièce jointe d'un PDF existant
type: docs
weight: 10
url: /fr/nodejs-cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF peut supprimer les pièces jointes de vos documents PDF. Utilisez l'environnement Node.js pour supprimer les pièces jointes des fichiers PDF avec Aspose.PDF.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Vous pouvez supprimer les pièces jointes d'un fichier PDF en utilisant Aspose.PDF for Node.js via C++. Au cas où vous souhaiteriez supprimer des pièces jointes d'un PDF, vous pouvez utiliser [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/) fonction. 
Veuillez vérifier le fragment de code suivant afin de supprimer les pièces jointes d'un fichier PDF dans un environnement Node.js.

**CommonJS:**

1. Appeler `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF dont les pièces jointes seront supprimées.
1. Appeler `AsposePdf` en tant que Promise et exécuter l'opération pour supprimer les pièces jointes. Recevoir l'objet si réussi.
1. Appelez la fonction [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. Supprimer les pièces jointes. Ainsi, si 'json.errorCode' vaut 0, le résultat de l'opération est enregistré dans "ResultPdfDeleteAttachments.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete attachments from a PDF-file and save the "ResultPdfDeleteAttachments.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
        console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF dont les pièces jointes seront supprimées.
1. Initialisez le module AsposePdf. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. Supprimer les pièces jointes. Ainsi, si 'json.errorCode' vaut 0, le résultat de l'opération est enregistré dans "ResultPdfDeleteAttachments.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete attachments from a PDF-file and save the "ResultPdfDeleteAttachments.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
    console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```