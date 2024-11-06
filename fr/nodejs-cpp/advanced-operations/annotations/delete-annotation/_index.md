---
title: Supprimer une Annotation dans Node.js
linktitle: Supprimer une Annotation
type: docs
weight: 10
url: fr/nodejs-cpp/delete-annotation/
description: Avec Aspose.PDF pour Node.js, vous pouvez supprimer une annotation de votre fichier PDF.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Vous pouvez supprimer des annotations d'un fichier PDF en utilisant Aspose.PDF pour Node.js via C++. Si vous souhaitez supprimer des annotations d'un PDF, vous pouvez utiliser la fonction [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/). Veuillez consulter l'extrait de code suivant pour supprimer des annotations d'un fichier PDF dans l'environnement Node.js.

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
2. Spécifiez le nom du fichier PDF dont l'annotation sera supprimée.
3. Appelez `AsposePdf` en tant que Promise et effectuez l'opération pour supprimer les annotations. Recevez l'objet en cas de succès.

1. Appelez la fonction [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/).
1. Supprimez les annotations. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfDeleteAnnotations.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Supprimer les annotations d'un fichier PDF et enregistrer le "ResultPdfDeleteAnnotations.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAnnotations(pdf_file, "ResultPdfDeleteAnnotations.pdf");
        console.log("AsposePdfDeleteAnnotations => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6 :**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF à partir duquel l'annotation sera supprimée.

1. Initialiser le module AsposePdf. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/).
1. Supprimez les annotations. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfDeleteAnnotations.pdf". Si le paramètre json.errorCode n'est pas 0 et, par conséquent, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Supprimer les annotations d'un fichier PDF et enregistrer dans "ResultPdfDeleteAnnotations.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAnnotations(pdf_file, "ResultPdfDeleteAnnotations.pdf");
    console.log("AsposePdfDeleteAnnotations => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```