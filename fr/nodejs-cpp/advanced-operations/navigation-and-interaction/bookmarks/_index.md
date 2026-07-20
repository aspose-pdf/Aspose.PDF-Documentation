---
title: Signets dans PDF en Node.js
linktitle: Signets dans PDF
type: docs
weight: 10
url: /fr/nodejs-cpp/bookmark/
description: Vous pouvez ajouter ou supprimer des signets dans un document PDF dans l'environnement Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Supprimer un signet particulier d'un document PDF

Vous pouvez supprimer des signets d'un fichier PDF à l'aide d'Aspose.PDF for Node.js via C++. Si vous souhaitez supprimer des signets d'un PDF, vous pouvez utiliser [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/) fonction. 
Veuillez vérifier le fragment de code suivant afin de supprimer les signets d’un fichier PDF dans un environnement Node.js.

**CommonJS :**

1. Appel `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF à partir duquel les signets seront supprimés.
1. Appel `AsposePdf` en tant que Promise et exécuter l'opération de suppression du signet. Recevoir l'objet en cas de succès.
1. Appeler la fonction [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. Supprimer les signets. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfDeleteBookmarks.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete bookmarks from a PDF-file and save the "ResultPdfDeleteBookmarks.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
        console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF à partir duquel les signets seront supprimés.
1. Initialisez le module AsposePdf. Recevez l'objet en cas de succès.
1. Appeler la fonction [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. Supprimer les signets. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfDeleteBookmarks.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete bookmarks from a PDF-file and save the "ResultPdfDeleteBookmarks.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
    console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```