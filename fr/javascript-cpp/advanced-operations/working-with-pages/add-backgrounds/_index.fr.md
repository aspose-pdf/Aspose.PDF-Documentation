---
title: Ajouter un arrière-plan à un PDF avec JavaScript via C++
linktitle: Ajouter des arrière-plans
type: docs
weight: 10
url: /javascript-cpp/add-backgrounds/
description: Ajouter une image d'arrière-plan à votre fichier PDF avec JavaScript via C++.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Les extraits de code suivants montrent comment ajouter une image d'arrière-plan aux pages PDF en utilisant la fonction [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddbackgroundimage/) avec JavaScript.

Dans le prochain extrait de code, nous téléchargeons l'image pour un travail ultérieur dans le système de fichiers interne :

1. Créez un 'FileReader'.
1. Définissez le nom du fichier image.
1. Préparez le fichier image à partir du BLOB.

```js

  var ffileImage = function (e) {
    const file_reader = new FileReader();
    /*définissez le nom du fichier image*/
    fileBackgroundImage = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*préparez(sauvegardez) le fichier image à partir du BLOB*/
      AsposePdfPrepare(event.target.result, fileBackgroundImage);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


In the next example, we select the PDF file to handle.  
1. Créez un 'FileReader'.  
1. La fonction [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddbackgroundimage/) est exécutée.  
1. Ajoutez le fichier image dans le PDF et enregistrez le "ResultBackgroundImage.pdf".  
1. Ensuite, si le 'json.errorCode' est 0, alors votre DownloadFile reçoit le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, par conséquent, il y aura une erreur dans votre fichier, alors les informations concernant cette erreur seront contenues dans le fichier 'json.errorText'.  
1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.  

```js

  var ffileAddBackgroundImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*ajouter un fichier image de fond dans le PDF et enregistrer le "ResultBackgroundImage.pdf"*/
      const json = AsposePdfAddBackgroundImage(event.target.result, e.target.files[0].name, fileBackgroundImage, "ResultBackgroundImage.pdf");
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
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ? 
          `Résultat:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            'image préparée!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Erreur: ${evt.data.json.errorText}`;

    /*Définir le nom de fichier image par défaut: 'Aspose.jpg' déjà chargé, voir les paramètres dans 'settings.json'*/
    var fileBackgroundImage = "Aspose.jpg";

    /*Gestionnaire d'événements*/
    const ffileAddBackgroundImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Ajouter une image de fond à un fichier PDF et enregistrer le "ResultBackgroundImage.pdf" - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddBackgroundImage',
            "params": [event.target.result, e.target.files[0].name, fileBackgroundImage, "ResultBackgroundImage.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*Définir le nom du fichier image*/
      fileBackgroundImage = e.target.files[0].name;
      file_reader.onload = event => {
        /*Enregistrer le BLOB dans le système de fichiers en mémoire pour traitement*/
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