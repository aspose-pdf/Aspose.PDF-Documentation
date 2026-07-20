---
title: Supprimer l'annotation dans Node.js
linktitle: Supprimer l'annotation
type: docs
weight: 10
url: /fr/nodejs-cpp/delete-annotation/
description: Avec Aspose.PDF for Node.js, vous pouvez supprimer l'annotation de votre fichier PDF.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Vous pouvez supprimer des annotations d'un fichier PDF en utilisant Aspose.PDF for Node.js via C\u002B\u002B. Au cas où vous voudriez supprimer des annotations d'un PDF, vous pouvez utiliser [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/) fonction. 
Veuillez vérifier le fragment de code suivant afin de supprimer les annotations d'un fichier PDF dans un environnement Node.js.

**CommonJS:**

1. Appeler `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF dont l'annotation sera supprimée.
1. Appeler `AsposePdf` en tant que Promise et exécuter l'opération de suppression des annotations. Recevez l'objet si le traitement réussit.
1. Appelez la fonction [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/).
1. Supprimer les annotations. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfDeleteAnnotations.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete annotations from a PDF-file and save the "ResultPdfDeleteAnnotations.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAnnotations(pdf_file, "ResultPdfDeleteAnnotations.pdf");
        console.log("AsposePdfDeleteAnnotations => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF dont l'annotation sera supprimée.
1. Initialisez le module AsposePdf. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/).
1. Supprimer les annotations. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfDeleteAnnotations.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete annotations from a PDF-file and save the "ResultPdfDeleteAnnotations.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAnnotations(pdf_file, "ResultPdfDeleteAnnotations.pdf");
    console.log("AsposePdfDeleteAnnotations => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```
