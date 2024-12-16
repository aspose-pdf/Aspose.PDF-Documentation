---
title: Supprimer des images d'un fichier PDF via JavaScript
linktitle: Supprimer des images
type: docs
weight: 20
url: /fr/javascript-cpp/delete-images-from-pdf-file/
description: Cette section explique comment supprimer des images d'un fichier PDF en utilisant Aspose.PDF pour JavaScript.
lastmod: "2022-02-17"
---

Vous pouvez supprimer des images d'un fichier PDF en utilisant Aspose.PDF pour JavaScript via C++. Vous pouvez obtenir le résultat directement dans votre navigateur.

1. Créez un 'FileReader'.
1. La fonction [AsposePdfDeleteImages](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeleteimages/) est exécutée.
1. Le nom du fichier résultant est défini, dans cet exemple "ResultPdfDeleteImages.pdf".
1. Ensuite, si le 'json.errorCode' est 0, alors votre DownloadFile reçoit le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, il y aura une erreur dans votre fichier, alors des informations sur cette erreur seront contenues dans le fichier 'json.errorText'.

1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

```js

    var ffilePdfDeleteImages = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*Supprimer les images d'un fichier PDF et enregistrer le "ResultPdfDeleteImages.pdf"*/
        const json = AsposePdfDeleteImages(event.target.result, e.target.files[0].name, "ResultPdfDeleteImages.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Créer un lien pour télécharger le fichier de résultat*/
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
        (evt.data.json.errorCode == 0) ? `Résultat:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Erreur: ${evt.data.json.errorText}`;

    /*Gestionnaire d'événements*/
    const ffilePdfDeleteImages = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*Supprimer les images d'un fichier PDF et enregistrer le "ResultPdfDeleteImages.pdf" - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteImages', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteImages.pdf"] }, [event.target.result]);
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Créer un lien pour télécharger le fichier de résultat*/
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