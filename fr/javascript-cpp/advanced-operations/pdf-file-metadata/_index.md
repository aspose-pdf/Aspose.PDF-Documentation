---
title: Travailler avec les métadonnées de fichiers PDF en utilisant JavaScript via C++
linktitle: Métadonnées de fichiers PDF
type: docs
weight: 130
url: fr/javascript-cpp/pdf-file-metadata/
description: Cette section explique comment obtenir des informations sur les fichiers PDF, comment obtenir des métadonnées d'un fichier PDF, définir les informations du fichier PDF.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtenir des informations sur le fichier PDF

1. Créez un 'FileReader'.
1. La fonction [AsposePdfGetInfo](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetinfo/) est exécutée.
1. Métadonnées PDF qui peuvent être obtenues :
- title - titre
- creator - créateur
- author - auteur
- subject - sujet
- keywords - mots-clés
- creation - date de création
- mod - date de modification
1. Ensuite, si le 'json.errorCode' est 0, alors vous pouvez obtenir la liste des informations du fichier PDF. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, il y aura une erreur dans votre fichier, alors des informations sur cette erreur seront contenues dans le fichier 'json.errorText'.

```js

  var ffilePdfGetInfo = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Obtenir des informations (métadonnées) du fichier PDF.*/
      const json = AsposePdfGetInfo(event.target.result, e.target.files[0].name);
      /* JSON
      title - titre
      creator - créateur
      author - auteur
      subject - sujet
      keywords - mots-clés
      format - format PDF
      version - version PDF
      ispdfa - PDF est PDF/A
      ispdfua - PDF est PDF/UA
      islinearized - PDF est linéarisé
      isencrypted - PDF est chiffré
      permission - permission PDF
      size - taille de la page PDF
      pagecount - Nombre de pages
      сreation Date: json.creation
      modify Date:   json.mod
      annotationcount - Nombre d'annotations
      bookmarkcount - Nombre de signets
      attachmentcount - Nombre de pièces jointes
      metadatacount - Nombre de métadonnées
      javascriptcount - Nombre de JavaScript
      imagecount - Nombre d'images
      */
      if (json.errorCode == 0) document.getElementById('output').textContent = "JSON:\n" + JSON.stringify(json, null, 4);
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


### Utilisation des Web Workers

```js

    /*Créer un Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur depuis le Web Worker : ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ?
          `info:\n${JSON.stringify(evt.data.json, null, 4)}` :
          `Erreur : ${evt.data.json.errorText}`; 

    /*Gestionnaire d'événements*/
    const ffilePdfGetInfo = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Obtenir des informations (métadonnées) d'un fichier PDF - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfGetInfo', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## Obtenir Toutes les Polices

Obtenir des polices à partir d'un fichier PDF peut être un moyen utile de réutiliser des polices dans d'autres documents ou applications.
 
Dans le cas où vous souhaitez obtenir toutes les polices d'un document PDF, vous pouvez utiliser [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetallfonts/). 
Veuillez consulter l'extrait de code suivant pour obtenir toutes les polices d'un document PDF existant en utilisant JavaScript via C++.

1. Créez un 'FileReader'.
1. La fonction [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetallfonts/) est exécutée.
1. Ensuite, si le 'json.errorCode' est 0, vous pouvez obtenir la liste des polices à partir du fichier PDF. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, il y aura une erreur dans votre fichier, alors l'information sur une telle erreur sera contenue dans le fichier 'json.errorText'.

```js

  var ffilePdfGetAllFonts = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*obtenir la liste des polices à partir du fichier PDF.*/
      const json = AsposePdfGetAllFonts(event.target.result, e.target.files[0].name);
      if (json.errorCode == 0) document.getElementById('output').textContent = "JSON:\n" + JSON.stringify(json, null, 4);
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

## Utilisation des Web Workers

```js

    /*Créer un Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ?
          `polices:\n${JSON.stringify(evt.data.json.fonts, null, 4)}` :
          `Erreur: ${evt.data.json.errorText}`; 

    /*Gestionnaire d'événements*/
    const ffilePdfGetAllFonts = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Obtenir une liste des polices d'un fichier PDF - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfGetAllFonts', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```
## Définir les informations du fichier PDF

Aspose.PDF pour JavaScript via C++ vous permet de définir des informations spécifiques au fichier pour un PDF, telles que l'auteur, la date de création, le sujet et le titre.
 Pour définir ces informations :

1. Créez un 'FileReader'.
1. Si vous n'avez pas besoin de définir une valeur, utilisez undefined ou "" (chaîne vide).
1. La fonction [AsposePdfSetInfo](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfsetinfo/) est exécutée.
1. Le nom du fichier résultant est défini, dans cet exemple "ResultSetInfo.pdf".
1. Ensuite, si le 'json.errorCode' est 0, alors votre DownloadFile reçoit le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, il y aura une erreur dans votre fichier, alors les informations sur cette erreur seront contenues dans le fichier 'json.errorText'.
1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

```js

    var ffilePdfSetInfo = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Définir les infos PDF : titre, créateur, auteur, sujet, mots-clés, création (date), mod (date de modification)*/
        /*Si vous n'avez pas besoin de définir de valeur, utilisez undefined ou "" (chaîne vide)*/
        /*Définir les infos (métadonnées) dans un fichier PDF et enregistrer le "ResultSetInfo.pdf"*/
        const json = AsposePdfSetInfo(event.target.result, e.target.files[0].name, "Définition des informations du document PDF", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "16/02/2023 23:55", "ResultSetInfo.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Créer un lien pour télécharger le fichier résultat*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

### Utilisation des Web Workers

```js

    /*Créer un Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker : ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ?
          `Résultat:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Erreur : ${evt.data.json.errorText}`;

    /*Gestionnaire d'événements*/
    const ffilePdfSetInfo = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Infos PDF : titre, créateur, auteur, sujet, mots-clés, création (date), mod (date de modification)*/
        const title = 'Définition des informations du document PDF';
        const creator = ''; /*si besoin de ne pas définir la valeur, utilisez : undefined ou ""/'' (chaîne vide)*/
        const author = 'Aspose';
        const subject = undefined;
        const keywords = 'Aspose.Pdf, DOM, API';
        const creation = undefined; /*date de création*/
        const mod = '16/02/2023 11:55 PM'; /*date de modification*/
        /*Définir les infos (métadonnées) dans un fichier PDF et enregistrer "ResultSetInfo.pdf" - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSetInfo',
            "params": [event.target.result, e.target.files[0].name, title, creator, author, subject, keywords, creation, mod, "ResultSetInfo.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Créer un lien pour télécharger le fichier résultat*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Cliquez ici pour télécharger le fichier " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


## Supprimer les informations du fichier PDF

Aspose.PDF pour JavaScript via C++ vous permet de supprimer les métadonnées d'un fichier PDF :

1. Créez un 'FileReader'.
1. La fonction [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/javascript-cpp/metadata/asposepdfremovemetadata/) est exécutée.
1. Le nom du fichier résultant est défini, dans cet exemple "ResultPdfRemoveMetadata.pdf".
1. Ensuite, si le 'json.errorCode' est 0, alors votre DownloadFile prend le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, il y aura une erreur dans votre fichier, alors les informations sur cette erreur seront contenues dans le fichier 'json.errorText'.
1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

```js

    var ffilePdfRemoveMetadata = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Supprimez les métadonnées d'un fichier PDF et enregistrez "ResultPdfRemoveMetadata.pdf"*/
        const json = AsposePdfRemoveMetadata(event.target.result, e.target.files[0].name, "ResultPdfRemoveMetadata.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Créer un lien pour télécharger le fichier résultant*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


### Utilisation des Web Workers

```js

    /*Créer un Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker : ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ? `Résultat:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Erreur : ${evt.data.json.errorText}`;

    /*Gestionnaire d'événements*/
    const ffilePdfRemoveMetadata = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Supprimer les métadonnées d'un fichier PDF et enregistrer le "ResultPdfRemoveMetadata.pdf" - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfRemoveMetadata', "params": [event.target.result, e.target.files[0].name, "ResultPdfRemoveMetadata.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Extrait de code]

    /*Créer un lien pour télécharger le fichier résultat*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Cliquez ici pour télécharger le fichier " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```