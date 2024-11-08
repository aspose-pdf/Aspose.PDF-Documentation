---
title: Changer le mot de passe d'un fichier PDF
linktitle: Changer le mot de passe
type: docs
weight: 50
url: /fr/javascript-cpp/change-password-pdf/
description: Changer le mot de passe d'un fichier PDF avec Aspose.PDF pour JavaScript via C++.
lastmod: "2023-09-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Changer le mot de passe d'un fichier PDF

Si vous souhaitez changer le mot de passe d'un fichier PDF de "owner" à "newowner", essayez le code suivant :

1. Sélectionnez un fichier PDF.
1. Créez un 'FileReader'.
1. La fonction [AsposePdfChangePassword](https://reference.aspose.com/pdf/javascript-cpp/security/asposepdfchangepassword/) est exécutée.
1. Le nom du fichier résultant est défini, dans cet exemple "ResultPdfChangePassword.pdf".
1. Ensuite, si le 'json.errorCode' est 0, alors votre DownloadFile est donné le nom que vous avez spécifié plus tôt. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, il y aura une erreur dans votre fichier, alors les informations sur une telle erreur seront contenues dans le fichier 'json.errorText'.

1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

```js

    var ffilePdfChangePassword = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Changer les mots de passe d'un fichier PDF de "owner" à "newowner" et enregistrer le "ResultPdfChangePassword.pdf"*/
        const json = AsposePdfChangePassword(event.target.result, e.target.files[0].name, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
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

  /*Créer Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ? `Résultat:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Erreur: ${evt.data.json.errorText}`;

    /*Gestionnaire d'événements*/
    const ffilePdfChangePassword = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const ownerPassword = 'owner'; /*Mot de passe propriétaire*/
        const newUserPassword = "newuser"; /*Nouveau mot de passe utilisateur*/
        const newOwnerPassword = "newowner"; /*Nouveau mot de passe propriétaire*/
        /*Changer les mots de passe d'un fichier PDF de "owner" à "newowner" et enregistrer le "ResultPdfChangePassword.pdf" - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfChangePassword', "params": [event.target.result, e.target.files[0].name, ownerPassword, newUserPassword, newOwnerPassword, "ResultPdfChangePassword.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Code snippet]

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