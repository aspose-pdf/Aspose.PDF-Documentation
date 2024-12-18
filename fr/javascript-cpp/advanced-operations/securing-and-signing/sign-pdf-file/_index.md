---
title: Ajouter une signature numérique ou signer numériquement un PDF en JavaScript via C++
linktitle: Signer numériquement un PDF
type: docs
weight: 70
url: /fr/javascript-cpp/sign-pdf/
description: Signer numériquement des documents PDF en utilisant JavaScript via C++.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Une signature numérique dans un document PDF est un moyen de vérifier l'authenticité et l'intégrité du document. Il s'agit du processus de signature électronique d'un document PDF à l'aide d'une clé privée et d'un certificat numérique. Cette signature garantit au détenteur que le document n'a pas été altéré ou modifié depuis la signature et que le signataire est celui qu'il approuve. Pour signer un PDF avec JavaScript, utilisez l'outil Aspose.PDF.

Aspose.PDF pour JavaScript via C++ prend en charge la fonction de signature numérique des fichiers PDF en utilisant le [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfsignpkcs7/).

## Signer un PDF avec des signatures numériques

```js

    /*Définir le nom de fichier par défaut de la clé PKCS7*/
    var fileSign = "/test.pfx";

    var ffileSign = function (e) {
      const file_reader = new FileReader();
      /*Définir le nom de fichier de la clé PKCS7*/
      fileImage = e.target.files[0].name;
      file_reader.onload = (event) => {
        /*Enregistrer le BLOB dans le FS mémoire pour le traitement*/
        AsposePdfPrepare(event.target.result, fileSign);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Définir le nom de fichier par défaut de l'image (Apparence de la signature)*/
    var signatureAppearance = "/Aspose.jpg";

    var ffileImage = function (e) {
      const file_reader = new FileReader();
      /*Définir le nom de fichier de l'image*/
      signatureAppearance = e.target.files[0].name;
      file_reader.onload = (event) => {
        /*Enregistrer le BLOB dans le FS mémoire pour le traitement*/
        AsposePdfPrepare(event.target.result, signatureAppearance);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    var ffileSignPKCS7 = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        let pswSign = document.getElementById("passwordSign").value;
        /*Signer un fichier PDF avec des signatures numériques et enregistrer le "ResultSignPKCS7.pdf"*/
        const json = AsposePdfSignPKCS7(event.target.result, e.target.files[0].name, 1, fileSign, pswSign, 200, 200, 200, 100, "TEST", "test@test.com", "EU", 1, signatureAppearance,"ResultSignPKCS7.pdf");
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
        (evt.data.json.errorCode == 0) ?
          `Résultat:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            'fichier préparé!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Erreur : ${evt.data.json.errorText}`;

    /*Définir le nom de fichier clé PKCS7 par défaut*/
    var fileSign = "test.pfx";
    /*Définir le nom de fichier de l'image par défaut (Apparence de la Signature) : 'Aspose.jpg' déjà chargé, voir les paramètres dans 'settings.json'*/
    var signatureAppearance = "Aspose.jpg";

    /*Gestionnaire d'événements*/
    const ffileSignPKCS7 = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const pageNum = 1;
        const pswSign = document.getElementById("passwordSign").value;
        const setXIndent = 100;
        const setYIndent = 100;
        const setHeight = 200;
        const setWidth = 100;
        const reason = 'Raison';
        const contact = 'contact@test.com';
        const location = 'Emplacement';
        const isVisible = 1;
        /*Signer un fichier PDF avec des signatures numériques et enregistrer le "ResultSignPKCS7.pdf" - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSignPKCS7',
            "params": [event.target.result, e.target.files[0].name, pageNum, fileSign, pswSign, setXIndent, setYIndent,
                      setHeight, setWidth, reason, contact, location, isVisible, signatureAppearance, "ResultSignPKCS7.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileSign = e => {
      const file_reader = new FileReader();
      /*Définir le nom de fichier clé PKCS7*/
      fileSign = e.target.files[0].name;
      file_reader.onload = event => {
        /*Enregistrer le BLOB dans le système de fichiers en mémoire pour traitement*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, fileSign] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*Définir le nom de fichier de l'image*/
      signatureAppearance = e.target.files[0].name;
      file_reader.onload = event => {
        /*Enregistrer le BLOB dans le système de fichiers en mémoire pour traitement*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, signatureAppearance] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Créer un lien pour télécharger le fichier résultant*/
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