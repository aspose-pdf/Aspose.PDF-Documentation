---
title: Chiffrer un PDF en utilisant JavaScript
linktitle: Chiffrer un fichier PDF
type: docs
weight: 50
url: /javascript-cpp/encrypt-pdf/
description: Chiffrer un fichier PDF avec Aspose.PDF pour JavaScript via C++.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Chiffrer un fichier PDF en utilisant un mot de passe utilisateur ou propriétaire

Si vous envoyez un e-mail à quelqu'un avec une pièce jointe PDF contenant des informations confidentielles, vous pourriez souhaiter ajouter d'abord une certaine sécurité pour éviter qu'elle ne tombe entre de mauvaises mains. La meilleure façon de limiter l'accès non autorisé à un document PDF est de le protéger avec un mot de passe. Pour chiffrer facilement et en toute sécurité des documents, vous pouvez utiliser Aspose.PDF pour JavaScript via C++.

>Veuillez spécifier des mots de passe utilisateur et propriétaire différents lors du chiffrement du fichier PDF.

- Le **mot de passe utilisateur**, s'il est défini, est celui que vous devez fournir pour ouvrir un PDF. Acrobat/Reader demandera à un utilisateur de saisir le mot de passe utilisateur. S'il n'est pas correct, le document ne s'ouvrira pas.
- Le **mot de passe propriétaire**, s'il est défini, contrôle les autorisations, telles que l'impression, la modification, l'extraction, les commentaires, etc.
 Acrobat/Reader désactivera ces fonctionnalités en fonction des paramètres d'autorisation. Acrobat nécessitera ce mot de passe si vous souhaitez définir/modifier les autorisations.

Le code suivant vous montre comment chiffrer des fichiers PDF.

1. Sélectionnez un fichier PDF à chiffrer.
1. Créez un 'FileReader'.
1. La fonction [AsposePdfEncrypt](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfencrypt/) est exécutée.
1. Le nom du fichier résultant est défini, dans cet exemple "ResultEncrypt.pdf".
1. Ensuite, si le 'json.errorCode' est 0, alors votre DownloadFile est nommé comme vous l'avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et qu'en conséquence, il y aura une erreur dans votre fichier, alors les informations concernant cette erreur seront contenues dans le fichier 'json.errorText'.
1. En conséquence, la fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) génère un lien et vous permet de télécharger le fichier résultant sur le système d'exploitation de l'utilisateur.

```js

  var ffileEncrypt = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*chiffrer un fichier PDF avec les mots de passe "user" et "owner", et enregistrer le "ResultDecrypt.pdf"*/
      const json = AsposePdfEncrypt(event.target.result, e.target.files[0].name, "user", "owner", Module.Permissions.PrintDocument, Module.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*créer un lien pour télécharger le fichier résultant*/
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
          `Résultat:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Erreur: ${evt.data.json.errorText}`;

    /*Gestionnaire d'événement*/
    const ffileEncrypt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password_user = 'utilisateur';
        const password_owner = 'propriétaire';
        const permissions = 'Module.Permissions.PrintDocument';
        const algorithm = 'Module.CryptoAlgorithm.RC4x40';
        /*Crypter un fichier PDF avec les mots de passe "utilisateur" et "propriétaire", et enregistrer le "ResultEncrypt.pdf" - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfEncrypt',
            "params": [event.target.result, e.target.files[0].name, password_user, password_owner,
                      permissions, algorithm, "ResultEncrypt.pdf"] },
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