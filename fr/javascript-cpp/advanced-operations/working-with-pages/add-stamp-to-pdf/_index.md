---
title: Ajouter des tampons d'image dans un PDF en utilisant JavaScript via C++
linktitle: Tampons d'image dans un fichier PDF
type: docs
weight: 60
url: /fr/javascript-cpp/stamping/
description: Ajoutez le tampon d'image à votre document PDF en utilisant la fonction AsposePdfAddStamp avec l'outil JavaScript.
lastmod: "2023-04-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ajouter un tampon d'image dans un fichier PDF

Tamponner un document PDF est similaire à tamponner un document papier. Un tampon dans un fichier PDF fournit des informations supplémentaires au fichier PDF, telles que la protection du fichier PDF pour que d'autres l'utilisent et la confirmation de la sécurité du contenu du fichier PDF.
Vous pouvez utiliser la fonction [AsposePdfAddStamp](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddstamp/) pour ajouter un tampon d'image à un fichier PDF en utilisant JavaScript.

Pour ajouter un tampon d'image :

1. Définissez le nom de fichier d'image par défaut.
1. Créez un 'FileReader'.
1. Définissez le nom de fichier d'image.
1. Préparez le fichier de tampon à partir du BLOB.

Le code suivant montre comment ajouter un tampon d'image dans le fichier PDF.

```js

  /*définir le nom de fichier de tampon par défaut*/
  var fileStamp = "/Aspose.jpg";

  var ffileStamp = function (e) {
    const file_reader = new FileReader();
    /*définir le nom de fichier de tampon*/
    fileStamp = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*préparer(sauvegarder) le fichier de tampon à partir du BLOB*/
      AsposePdfPrepare(event.target.result, fileStamp);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


1. Créez un 'FileReader'.
1. La fonction [AsposePdfAddStamp](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddstamp/) est exécutée.
1. Ajoutez le fichier image à la fin d'un fichier PDF et enregistrez le "ResultImage.pdf".
1. Ensuite, si le 'json.errorCode' est 0, alors votre DownloadFile reçoit le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, il y aura une erreur dans votre fichier, alors les informations sur une telle erreur seront contenues dans le fichier 'json.errorText'.
1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

```js
  var ffileAddStamp = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*insérer le fichier de tampon dans un fichier PDF et enregistrer le "ResultImage.pdf"*/
      const json = AsposePdfAddStamp(event.target.result, e.target.files[0].name, fileStamp, 0, 5, 5, 40, 40, Module.Rotation.on270, 0.5, "ResultStamp.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*créer un lien pour télécharger le fichier résultat*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


## Utilisation des Web Workers

```js

    /*Créer un Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur de Web Worker : ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ?
          `Résultat:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            'image préparée!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Erreur : ${evt.data.json.errorText}`;

    /*Définir le nom de fichier de tampon par défaut : 'Aspose.jpg' déjà chargé, voir les paramètres dans 'settings.json'*/
    var fileStamp = "Aspose.jpg";

    /*Gestionnaire d'événements*/
    const ffileAddStamp = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const setBackground = 0;
        const setXIndent_ = 5;
        const setYIndent_ = 5;
        const setHeight_ = 40;
        const setWidth_ = 40;
        const rotation_ = 'Module.Rotation.on270';
        const setOpacity = 0.5;
        /*Ajouter un tampon à un fichier PDF et enregistrer le "ResultStamp.pdf" - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddStamp',
            "params": [event.target.result, e.target.files[0].name, fileStamp, setBackground, setXIndent_, setYIndent_,
                      setHeight_, setWidth_, rotation_, setOpacity, "ResultStamp.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileStamp = e => {
      const file_reader = new FileReader();
      /*Définir le nom de fichier du tampon*/
      fileStamp = e.target.files[0].name;
      file_reader.onload = event => {
        /*Enregistrer le BLOB dans la mémoire FS pour traitement*/
        AsposePDFWebWorker.postMessage(
            { "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] },
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