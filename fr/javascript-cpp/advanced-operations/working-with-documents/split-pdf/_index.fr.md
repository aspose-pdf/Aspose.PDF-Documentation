---
title: Diviser un PDF en utilisant JavaScript
linktitle: Diviser des fichiers PDF
type: docs
weight: 30
url: /javascript-cpp/split-pdf/
description: Ce sujet montre comment diviser les pages PDF en fichiers PDF individuels avec Aspose.PDF pour JavaScript via C++.
lastmod: "2022-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Diviser un PDF en deux fichiers en utilisant JavaScript

Ce sujet montre comment diviser les pages PDF en fichiers PDF individuels en utilisant JavaScript. Actuellement, nous supportons la division en deux parties. Cela signifie que `pageToSplit` est un marqueur pour la division. Le premier fichier contiendra toutes les pages de 1 à `pageToSplit` inclusivement, et le second fichier aura le reste des pages.

L'opération de division dépend du nombre de pages dans le document et peut être très chronophage. Par conséquent, nous recommandons fortement d'utiliser les Web Workers.

L'exemple de code fourni est un exemple d'utilisation d'un Web Worker en JavaScript pour diviser un fichier PDF en deux fichiers PDF distincts et offrir à l'utilisateur l'option de télécharger les fichiers résultants.
 Voici les étapes du code :

1. Création d'un Web Worker. Un web worker est initialisé en utilisant le fichier script "AsposePDFforJS.js". Ce web worker gérera les tâches de découpage de fichiers PDF en arrière-plan. Dans notre exemple, toutes les erreurs survenant dans le worker sont capturées et enregistrées dans la console.
1. Gestion des Messages. Le web worker est configuré pour écouter les messages en utilisant le gestionnaire d'événements onmessage. Lorsqu'il reçoit un message de la page web, il traite la demande et envoie une réponse au thread principal.
1. Gestionnaire d'Événements de Découpage de Fichier. Il y a un gestionnaire d'événements ffileSplit qui se déclenche lorsqu'un utilisateur sélectionne un fichier PDF pour le découpage. Il lit le fichier PDF sélectionné à l'aide d'un FileReader et envoie le contenu du fichier et les paramètres pertinents (comme le nombre de pages à découper et les noms des fichiers de sortie) au web worker via un appel postMessage.
1. Fonction de téléchargement de fichier. La fonction [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) est responsable de la génération d'un lien qui permet à l'utilisateur de télécharger un fichier. Elle accepte le nom de fichier, le type MIME, et le contenu du fichier. La fonction crée un lien de téléchargement, associe le contenu du fichier à celui-ci, définit le nom de fichier, et l'ajoute au document. Cela permet à l'utilisateur de télécharger les fichiers PDF résultants.

1. Gestion des messages dans le Web Worker. Ensuite, si le 'json.errorCode' est 0, alors json.fileNameResult contiendra le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, il y aura une erreur dans votre fichier, alors des informations sur cette erreur seront contenues dans la propriété 'json.errorText'.

1. Affichage des résultats. La page principale comprend un élément avec l'ID 'output'. Lorsque le web worker envoie un message avec le résultat, il met à jour l'élément 'output'. Si l'opération est réussie, elle affiche des liens de téléchargement pour les deux fichiers PDF divisés. S'il y a une erreur, elle affiche un message d'erreur.

Ce code démontre une méthode pour déléguer les tâches de division de fichiers PDF gourmandes en ressources à un web worker afin d'éviter de bloquer le thread principal de l'interface utilisateur. Il offre également une méthode conviviale pour télécharger les fichiers PDF divisés.

```js

    /*Créer un Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ?
          `Résultat:\n${DownloadFile(evt.data.json.fileNameResult1, "application/pdf", evt.data.params[0])}
                  \n${DownloadFile(evt.data.json.fileNameResult2, "application/pdf", evt.data.params[1])}` :
          `Erreur: ${evt.data.json.errorText}`;

    /*Gestionnaire d'événements*/
    const ffileSplit = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Définir le nombre de pages à diviser*/
        const pageToSplit = 1;
        /*Diviser en deux fichiers PDF et enregistrer les "ResultSplit1.pdf", "ResultSplit2.pdf" - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSplit2Files',
            "params": [event.target.result, e.target.files[0].name, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf"] },
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

The following JavaScript code snippet shows simple example of splitting PDF pages into individual PDF files:

Le code JavaScript suivant montre un exemple simple de division des pages PDF en fichiers PDF individuels :

1. Select a PDF file for splitting.
1. Sélectionnez un fichier PDF à diviser.
2. Create a 'FileReader' object in handler.
2. Créez un objet 'FileReader' dans le gestionnaire.
3. Set number a page to split.
3. Définissez le numéro de la page à diviser.
4. Call [AsposePdfSplit2Files](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfsplit2files/) in the last handler.
4. Appelez [AsposePdfSplit2Files](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfsplit2files/) dans le dernier gestionnaire.
5. Analyse the result. The name of the resulting file is set, in this example "ResultSplit2.pdf".
5. Analysez le résultat. Le nom du fichier résultant est défini, dans cet exemple "ResultSplit2.pdf".
6. Next, if the 'json.errorCode' is 0, then json.fileNameResult will contain the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' property.
6. Ensuite, si le 'json.errorCode' est 0, alors json.fileNameResult contiendra le nom que vous avez spécifié précédemment. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, il y aura une erreur dans votre fichier, alors des informations sur une telle erreur seront contenues dans la propriété 'json.errorText'.
7. You can use helper function [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/).
7. Vous pouvez utiliser la fonction d'assistance [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/).

```js

  var ffileSplit = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Set number a page to split*/
      /*Définissez le numéro de la page à diviser*/
      const pageToSplit = 1;
      /*Split to two PDF-files and save the "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      /*Divisez en deux fichiers PDF et enregistrez les "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      const json = AsposePdfSplit2Files(event.target.result, e.target.files[0].name, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = e.target.files[0].name + " split: " + json.fileNameResult1 + ", " + json.fileNameResult2;
      else document.getElementById('output').textContent = json.errorText;
      /*Make a link to download the first result file*/
      /*Créez un lien pour télécharger le premier fichier résultat*/
      DownloadFile(json.fileNameResult1, "application/pdf");
      /*Make a link to download the second result file*/
      /*Créez un lien pour télécharger le deuxième fichier résultat*/
      DownloadFile(json.fileNameResult2, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```