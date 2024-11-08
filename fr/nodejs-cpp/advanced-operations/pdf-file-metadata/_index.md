---
title: Travailler avec les métadonnées des fichiers PDF dans Node.js 
linktitle: Métadonnées des fichiers PDF
type: docs
weight: 130
url: /fr/nodejs-cpp/pdf-file-metadata/
description: Cette section explique comment obtenir des informations sur un fichier PDF, comment obtenir des métadonnées à partir d'un fichier PDF, définir des informations de fichier PDF dans Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtenir des informations sur un fichier PDF

Si vous souhaitez obtenir des informations sur un fichier PDF, vous pouvez utiliser la fonction [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/). 
Veuillez vérifier l'extrait de code suivant pour obtenir des informations sur un fichier PDF dans l'environnement Node.js.

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF à partir duquel les informations seront extraites.
1. Appelez `AsposePdf` en tant que Promesse et effectuez l'opération pour extraire les informations. Recevez l'objet si réussi.

1. Appelez la fonction [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. Les métadonnées extraites sont stockées dans l'objet JSON. Ainsi, si 'json.errorCode' est 0, les métadonnées extraites sont affichées à l'aide de console.log. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Obtenez des informations (métadonnées) d'un fichier PDF*/
      const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
      /* JSON
        Titre             : json.title
        Créateur          : json.creator
        Auteur            : json.author
        Sujet             : json.subject
        Mots-clés         : json.keywords
        Date de création  : json.creation
        Date de modification : json.mod
        Format PDF        : json.format
        Version PDF       : json.version
        PDF est PDF/A     : json.ispdfa
        PDF est PDF/UA    : json.ispdfua
        PDF est linéarisé : json.islinearized
        PDF est crypté    : json.isencrypted
        Permission PDF    : json.permission
        Taille de page PDF: json.size
        Nombre de pages   : json.pagecount
        Nombre d'annotations : json.annotationcount
        Nombre de signets : json.bookmarkcount
        Nombre de pièces jointes : json.attachmentcount
        Nombre de métadonnées : json.metadatacount
        Nombre de JavaScript : json.javascriptcount
        Nombre d'images   : json.imagecount
      */
      console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Titre: ' + json.title : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF à partir duquel les informations seront extraites.
1. Initialisez le module AsposePdf. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. Les métadonnées extraites sont stockées dans l'objet JSON. Ainsi, si 'json.errorCode' est 0, les métadonnées extraites sont affichées à l'aide de console.log. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Obtenez des informations (métadonnées) à partir d'un fichier PDF*/
    const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
    /* JSON
      Titre             : json.title
      Créateur          : json.creator
      Auteur            : json.author
      Sujet             : json.subject
      Mots-clés         : json.keywords
      Date de création  : json.creation
      Date de modification : json.mod
      Format PDF        : json.format
      Version PDF       : json.version
      PDF est PDF/A     : json.ispdfa
      PDF est PDF/UA    : json.ispdfua
      PDF est linéarisé : json.islinearized
      PDF est chiffré   : json.isencrypted
      Permission PDF    : json.permission
      Taille de la page PDF : json.size
      Nombre de pages   : json.pagecount
      Nombre d'annotations : json.annotationcount
      Nombre de signets : json.bookmarkcount
      Nombre de pièces jointes : json.attachmentcount
      Nombre de métadonnées : json.metadatacount
      Nombre de JavaScript : json.javascriptcount
      Nombre d'images   : json.imagecount
    */
    console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Titre: ' + json.title : json.errorText);
```


## Obtenir Toutes les Polices

Obtenir des polices à partir d'un fichier PDF peut être un moyen utile de réutiliser des polices dans d'autres documents ou applications.

Au cas où vous souhaiteriez obtenir des polices à partir d'un fichier PDF, vous pouvez utiliser la fonction [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/). Veuillez vérifier l'extrait de code suivant afin d'obtenir des polices à partir d'un fichier PDF dans un environnement Node.js.

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` comme variable `AsposePdf`.
1. Spécifiez le nom du fichier PDF à partir duquel les polices seront extraites.
1. Appelez `AsposePdf` en tant que Promise et effectuez l'opération pour extraire les polices. Recevez l'objet en cas de succès.
1. Appelez la fonction [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).

1. Les polices extraites sont stockées dans l'objet JSON. Ainsi, si 'json.errorCode' est 0, il affiche un tableau de détails des polices, y compris le nom de la police, si elle est intégrée, et son statut d'accessibilité en utilisant console.log. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Obtenez la liste des polices à partir d'un fichier PDF*/
      const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
      /*json.fonts - tableau des polices: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
      console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
  });
```

**ECMAScript/ES6 :**

1. Importer le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF à partir duquel les polices seront extraites.

1. Initialiser le module AsposePdf. Recevez l'objet si la connexion est réussie.
1. Appelez la fonction [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).
1. Les polices extraites sont stockées dans l'objet JSON. Ainsi, si 'json.errorCode' est 0, il affiche un tableau de détails de police, y compris le nom de la police, si elle est incorporée, et son statut d'accessibilité en utilisant console.log. Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Obtenez la liste des polices d'un fichier PDF*/
  const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
  /*json.fonts - tableau de polices : { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
  console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
```

## Définir les Informations du Fichier PDF


Aspose.PDF pour Node.js via C++ vous permet de définir des informations spécifiques au fichier pour un PDF, telles que l'auteur, la date de création, le sujet et le titre. Pour définir ces informations :

Dans le cas où vous souhaitez définir des informations spécifiques au fichier, vous pouvez utiliser la fonction [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/). Veuillez consulter l'extrait de code suivant afin de définir les informations du fichier dans l'environnement Node.js.

Possible de définir :
- titre
- créateur
- auteur
- sujet
- lister les mots-clés
- date de création
- date de modification
- nom du fichier résultant

**CommonJS :**

1. Appelez `require` et importez le module `asposepdfnodejs` en tant que variable `AsposePdf`.
2. Spécifiez le nom du fichier PDF où les informations seront définies.
3. Appelez `AsposePdf` en tant que Promesse et effectuez l'opération. Recevez l'objet en cas de succès.
4. Appelez la fonction [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).

1. Définir les informations du fichier PDF. Des informations telles que le titre, le créateur, l'auteur, le sujet, les mots-clés, la date de création et la date de modification sont fournies en tant que paramètres. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultSetInfo.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Définir les infos PDF : titre, créateur, auteur, sujet, mots-clés, création (date), mod (date de modification)*/
      /*Si pas besoin de définir une valeur, utiliser undefined ou "" (chaîne vide)*/
      /*Définir les infos (métadonnées) dans un fichier PDF et enregistrer le "ResultSetInfo.pdf"*/
      const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Définition des informations du document PDF", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
      console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF où les informations seront définies.
1. Initialisez le module AsposePdf. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).
1. Définissez les informations du fichier PDF. Les informations telles que le titre, le créateur, l'auteur, le sujet, les mots-clés, la date de création et la date de modification sont fournies en tant que paramètres. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultSetInfo.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations sur l'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Définir les infos PDF : titre, créateur, auteur, sujet, mots-clés, création (date), mod (date de modification)*/
  /*Si vous n'avez pas besoin de définir une valeur, utilisez undefined ou "" (chaîne vide)*/
  /*Définir les infos (métadonnées) dans un fichier PDF et enregistrer le "ResultSetInfo.pdf"*/
  const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Définition des informations du document PDF", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
  console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```


## Supprimer les informations du fichier PDF

Aspose.PDF pour Node.js via C++ vous permet de supprimer les métadonnées du fichier PDF :

Dans le cas où vous souhaitez supprimer les métadonnées d'un PDF, vous pouvez utiliser la fonction [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/). Veuillez consulter l'extrait de code suivant afin de supprimer les métadonnées d'un PDF dans un environnement Node.js.

**CommonJS :**

1. Requérir le module AsposePDFforNode.js.
1. Spécifiez le nom du fichier PDF dont les informations seront supprimées.
1. Initialisez le module AsposePdf. Recevez l'objet si cela réussit.
1. Appelez la fonction [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. Supprimez les informations du fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfRemoveMetadata.pdf". Si le paramètre json.errorCode n'est pas 0 et, en conséquence, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Supprimer les métadonnées d'un fichier PDF et enregistrer le "ResultPdfRemoveMetadata.pdf"*/
      const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
      console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importez le module `asposepdfnodejs`.
1. Spécifiez le nom du fichier PDF dont les informations seront supprimées.
1. Initialisez le module AsposePdf. Recevez l'objet si réussi.
1. Appelez la fonction [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. Supprimez les informations du fichier PDF. Ainsi, si 'json.errorCode' est 0, le résultat de l'opération est enregistré dans "ResultPdfRemoveMetadata.pdf". Si le paramètre json.errorCode n'est pas 0 et, par conséquent, une erreur apparaît dans votre fichier, les informations d'erreur seront contenues dans 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Supprimer les métadonnées d'un fichier PDF et enregistrer dans "ResultPdfRemoveMetadata.pdf"*/
  const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
  console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```