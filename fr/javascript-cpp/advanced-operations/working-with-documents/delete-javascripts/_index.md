---
title: Effacer le code JavaScript d'un fichier PDF
linktitle: Supprimer JavaScripts
type: docs
weight: 50
url: /fr/javascript-cpp/delete-javascripts/
description: Effacez les macros JavaScript d'un fichier PDF directement sur le Web avec Aspose.PDF.
lastmod: "2023-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Supprimer JavaScript d'un fichier PDF peut être nécessaire pour des raisons de sécurité et de confidentialité. JavaScript dans les fichiers PDF peut parfois être utilisé de manière malveillante ou pour des fonctions non désirées. Vous pouvez obtenir le résultat directement dans votre navigateur.

1. Créez un 'FileReader'.
1. La fonction [AsposePdfDeleteJavaScripts](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeletejavascripts/) est exécutée.
1. Le nom du fichier résultant est défini, dans cet exemple "ResultPdfDeleteJavaScripts.pdf".

1. Ensuite, si le 'json.errorCode' est 0, alors votre DownloadFile porte le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, par conséquent, il y aura une erreur dans votre fichier, alors les informations sur une telle erreur seront contenues dans le fichier 'json.errorText'.
1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

```js

    var ffilePdfDeleteJavaScripts = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*Supprimer les JavaScripts d'un fichier PDF et sauvegarder le "ResultPdfDeleteJavaScripts.pdf"*/
        const json = AsposePdfDeleteJavaScripts(event.target.result, e.target.files[0].name, "ResultPdfDeleteJavaScripts.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Créer un lien pour télécharger le fichier résultat*/
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
        (evt.data.json.errorCode == 0) ? `Résultat:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Erreur : ${evt.data.json.errorText}`;

    /*Gestionnaire d'événements*/
    const ffilePdfDeleteJavaScripts = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*Supprimer les JavaScripts d'un fichier PDF et enregistrer le "ResultPdfDeleteJavaScripts.pdf" - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteJavaScripts', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteJavaScripts.pdf"] }, [event.target.result]);
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