---
title: Décrypter un PDF en utilisant JavaScript
linktitle: Décrypter un fichier PDF
type: docs
weight: 40
url: fr/javascript-cpp/decrypt-pdf/
description: Décrypter un fichier PDF avec Aspose.PDF pour JavaScript via C++.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Décrypter un fichier PDF en utilisant un mot de passe propriétaire

Récemment, de plus en plus d'utilisateurs échangent des documents cryptés afin de ne pas devenir victimes de fraudes sur Internet et de protéger leurs documents. À cet égard, il devient nécessaire d'accéder au fichier PDF crypté, car un tel accès ne peut être obtenu que par un utilisateur autorisé. De plus, les gens recherchent diverses solutions pour décrypter les fichiers PDF.

Il est préférable de résoudre ce problème une fois en utilisant Aspose.PDF pour JavaScript via C++ directement dans votre navigateur web. Le code suivant vous montre comment décrypter des fichiers PDF.

1. Sélectionnez un fichier PDF à décrypter.
1. Créez un 'FileReader'.
1. La fonction [AsposePdfDecrypt](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfdecrypt/) est exécutée.

1. Le nom du fichier résultant est défini, dans cet exemple "ResultDecrypt.pdf".
1. Ensuite, si le 'json.errorCode' est 0, alors votre DownloadFile reçoit le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, par conséquent, qu'il y aura une erreur dans votre fichier, alors les informations concernant cette erreur seront contenues dans le fichier 'json.errorText'.
1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

```js

    var ffileDecrypt = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Décrypter un fichier PDF avec le mot de passe "owner" et enregistrer le "ResultDecrypt.pdf"*/
        const json = AsposePdfDecrypt(event.target.result, e.target.files[0].name, "owner", "ResultDecrypt.pdf");
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
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker : ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ?
          `Résultat:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Erreur : ${evt.data.json.errorText}`;

    /*Gestionnaire d'événements*/
    const ffileDecrypt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'owner';
        /*Décrypter un fichier PDF avec le mot de passe "owner" et enregistrer le "ResultDecrypt.pdf" - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfDecrypt',
            "params": [event.target.result, e.target.files[0].name, password, "ResultDecrypt.pdf"] }, 
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