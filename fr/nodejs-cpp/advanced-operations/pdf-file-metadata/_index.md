---
title: Travailler avec les métadonnées du fichier PDF dans Node.js
linktitle: Métadonnées du fichier PDF
type: docs
weight: 130
url: /fr/nodejs-cpp/pdf-file-metadata/
description: Cette section explique comment obtenir les informations d’un fichier PDF, comment obtenir les métadonnées d’un fichier PDF, et comment définir les informations du fichier PDF dans Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtenir des informations sur le fichier PDF

Dans le cas où vous souhaitez obtenir des informations sur le fichier PDF, vous pouvez utiliser [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/) fonction. 
Veuillez vérifier le fragment de code suivant afin d'obtenir des informations sur le fichier PDF dans un environnement Node.js.

**CommonJS:**

1. Appeler `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF à partir duquel les informations seront extraites.
1. Appeler `AsposePdf` en tant que Promise et effectuez l'opération d'extraction d'informations. Recevez l'objet si réussite.
1. Appeler la fonction [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. Les métadonnées extraites sont stockées dans l'objet JSON. Ainsi, si 'json.errorCode' vaut 0, les métadonnées extraites sont affichées à l'aide de console.log. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Get info (metadata) from a PDF-file*/
      const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
      /* JSON
        Title             : json.title
        Creator           : json.creator
        Author            : json.author
        Subject           : json.subject
        Keywords          : json.keywords
        Creation Date     : json.creation
        Modify Date       : json.mod
        PDF format        : json.format
        PDF version       : json.version
        PDF is PDF/A      : json.ispdfa
        PDF is PDF/UA     : json.ispdfua
        PDF is linearized : json.islinearized
        PDF is encrypted  : json.isencrypted
        PDF permission    : json.permission
        PDF page size     : json.size
        Page count        : json.pagecount
        Annotation count  : json.annotationcount
        Bookmark count    : json.bookmarkcount
        Attachment count  : json.attachmentcount
        Metadata count    : json.metadatacount
        JavaScript count  : json.javascriptcount
        Image count       : json.imagecount
      */
      console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
  });
```

**ECMAScript/ES6 :**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF à partir duquel les informations seront extraites.
1. Initialisez le module AsposePdf. Recevez l'objet si succès.
1. Appeler la fonction [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. Les métadonnées extraites sont stockées dans l'objet JSON. Ainsi, si 'json.errorCode' vaut 0, les métadonnées extraites sont affichées à l'aide de console.log. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Get info (metadata) from a PDF-file*/
    const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
    /* JSON
      Title             : json.title
      Creator           : json.creator
      Author            : json.author
      Subject           : json.subject
      Keywords          : json.keywords
      Creation Date     : json.creation
      Modify Date       : json.mod
      PDF format        : json.format
      PDF version       : json.version
      PDF is PDF/A      : json.ispdfa
      PDF is PDF/UA     : json.ispdfua
      PDF is linearized : json.islinearized
      PDF is encrypted  : json.isencrypted
      PDF permission    : json.permission
      PDF page size     : json.size
      Page count        : json.pagecount
      Annotation count  : json.annotationcount
      Bookmark count    : json.bookmarkcount
      Attachment count  : json.attachmentcount
      Metadata count    : json.metadatacount
      JavaScript count  : json.javascriptcount
      Image count       : json.imagecount
    */
    console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
```

## Obtenir toutes les polices

Extraire les polices d'un fichier PDF peut être un moyen utile de réutiliser les polices dans d'autres documents ou applications. 

Dans le cas où vous souhaitez extraire les polices d'un fichier PDF, vous pouvez utiliser [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/) fonction. 
Veuillez vérifier le fragment de code suivant afin de récupérer les polices d'un fichier PDF dans un environnement Node.js.

**CommonJS:**

1. Appeler `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF à partir duquel les polices seront extraites.
1. Appeler `AsposePdf` en tant que Promise et effectuez l'opération d'extraction des polices. Recevez l'objet si réussi.
1. Appeler la fonction [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).
1. Les polices extraites sont stockées dans l'objet JSON. Ainsi, si 'json.errorCode' vaut 0, il affiche un tableau de détails sur les polices, incluant le nom de la police, si elle est incorporée, et son statut d'accessibilité en utilisant console.log. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Get list fonts from a PDF-file*/
      const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
      /*json.fonts - array of fonts: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
      console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
  });
```

**ECMAScript/ES6 :**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF à partir duquel les polices seront extraites.
1. Initialisez le module AsposePdf. Recevez l'objet si succès.
1. Appeler la fonction [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).
1. Les polices extraites sont stockées dans l'objet JSON. Ainsi, si 'json.errorCode' vaut 0, il affiche un tableau de détails sur les polices, incluant le nom de la police, si elle est incorporée, et son statut d'accessibilité en utilisant console.log. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Get list fonts from a PDF-file*/
  const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
  /*json.fonts - array of fonts: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
  console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
```

## Définir les informations du fichier PDF

Aspose.PDF for Node.js via C++ permet de définir des informations spécifiques à un fichier PDF, telles que l'auteur, la date de création, le sujet et le titre. Pour définir ces informations :

Dans le cas où vous souhaitez définir des informations spécifiques au fichier, vous pouvez utiliser [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/) fonction. 
Veuillez vérifier le fragment de code suivant afin de définir les informations du fichier dans un environnement Node.js.

Possible de définir : 
- titre
- créateur
- auteur
- sujet
- liste de mots-clés
- date de création
- modifier la date
- nom du fichier de résultat

**CommonJS:**

1. Appeler `require` et importer `asposepdfnodejs` module comme `AsposePdf` variable.
1. Spécifiez le nom du fichier PDF où les informations seront définies.
1. Appeler `AsposePdf` en tant que Promise et exécuter l'opération. Recevoir l'objet en cas de succès.
1. Appeler la fonction [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).
1. Définir les informations du fichier PDF. Des informations telles que le titre, le créateur, l'auteur, le sujet, les mots‑clés, la date de création et la date de modification sont fournies en tant que paramètres. Ainsi, si 'json.errorCode' vaut 0, le résultat de l'opération est enregistré dans "ResultSetInfo.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set PDF info: title, creator, author, subject, keywords, creation (date), mod (date modify)*/
      /*If not need to set value, use undefined or "" (empty string)*/
      /*Set info (metadata) in a PDF-file and save the "ResultSetInfo.pdf"*/
      const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
      console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6 :**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF où les informations seront définies.
1. Initialisez le module AsposePdf. Recevez l'objet si succès.
1. Appeler la fonction [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).
1. Définir les informations du fichier PDF. Des informations telles que le titre, le créateur, l'auteur, le sujet, les mots‑clés, la date de création et la date de modification sont fournies en tant que paramètres. Ainsi, si 'json.errorCode' vaut 0, le résultat de l'opération est enregistré dans "ResultSetInfo.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set PDF info: title, creator, author, subject, keywords, creation (date), mod (date modify)*/
  /*If not need to set value, use undefined or "" (empty string)*/
  /*Set info (metadata) in a PDF-file and save the "ResultSetInfo.pdf"*/
  const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
  console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

## Supprimer les informations du fichier PDF

Aspose.PDF for Node.js via C++ vous permet de supprimer les métadonnées du fichier PDF :

Dans le cas où vous souhaitez supprimer les métadonnées d'un PDF, vous pouvez utiliser [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/) fonction. 
Veuillez vérifier le fragment de code suivant afin de supprimer les métadonnées du PDF dans un environnement Node.js.

**CommonJS:**

1. Exigez le module AsposePDFforNode.js.
1. Spécifiez le nom du fichier PDF dont les informations seront supprimées.
1. Initialisez le module AsposePdf. Recevez l'objet si succès.
1. Appeler la fonction [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. Supprimez les informations du fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfRemoveMetadata.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Remove metadata from a PDF-file and save the "ResultPdfRemoveMetadata.pdf"*/
      const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
      console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6 :**

1. Importer le `asposepdfnodejs` module.
1. Spécifiez le nom du fichier PDF dont les informations seront supprimées.
1. Initialisez le module AsposePdf. Recevez l'objet si succès.
1. Appeler la fonction [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. Supprimez les informations du fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfRemoveMetadata.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Remove metadata from a PDF-file and save the "ResultPdfRemoveMetadata.pdf"*/
  const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
  console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```