---
title: Extraire le texte d'un PDF avec JavaScript
linktitle: Extraire le texte d'un PDF
type: docs
weight: 10
url: /javascript-cpp/extract-text/
description: Cette section décrit comment extraire du texte d'un document PDF en utilisant un kit d'outils JavaScript.
lastmod: "2022-12-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraire le texte de toutes les pages d'un document PDF

Extraire du texte d'un PDF n'est pas facile. Peu de lecteurs PDF peuvent extraire du texte à partir d'images PDF ou de PDF numérisés. Mais l'outil **Aspose.PDF pour JavaScript via C++** vous permet d'extraire facilement le texte de tout fichier PDF.

Vérifiez l'extrait de code et suivez les étapes pour extraire le texte de votre PDF :

1. Sélectionnez un fichier PDF pour extraire le texte.
1. Créez un 'FileReader' pour lire le texte.
1. La fonction [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfextracttext/) est exécutée.

1. Ensuite, si le 'json.errorCode' est 0, alors le 'json.extractText' contiendra le contenu extrait. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, votre fichier aura une erreur, alors l'information sur cette erreur sera contenue dans le 'json.errorText'.
1. En conséquence, vous recevrez une chaîne avec le texte extrait de votre PDF.

```js

    var ffileExtract = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Extraire le texte d'un fichier PDF*/
        const json = AsposePdfExtractText(event.target.result, e.target.files[0].name);
        if (json.errorCode == 0) document.getElementById('output').textContent = json.extractText;
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## Utilisation des Web Workers

```js

    /*Créer un Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur de Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode == 0) ?
          evt.data.json.extractText :
          `Erreur: ${evt.data.json.errorText}`; 

    /*Gestionnaire d'événements*/
    const ffileExtract = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Extraire le texte d'un fichier PDF - Demander au Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfExtractText', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```