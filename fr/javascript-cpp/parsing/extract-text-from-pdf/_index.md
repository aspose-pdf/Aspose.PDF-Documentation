---
title: Extraire du texte d'un PDF en utilisant JavaScript
linktitle: Extraire du texte d'un PDF
type: docs
weight: 30
url: fr/javascript-cpp/extract-text-from-pdf/
description: Cet article décrit diverses manières d'extraire du texte de documents PDF en utilisant Aspose.PDF pour JavaScript.
lastmod: "2023-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraire du texte d'un document PDF

Extraire du texte d'un document PDF est une tâche très courante et utile. L'extraction de texte à partir de PDF sert à diverses fins, allant de l'amélioration de la recherche et de la disponibilité à l'analyse et l'automatisation des données dans divers domaines tels que le commerce, la recherche et la gestion de l'information.

Au cas où vous voudriez extraire du texte d'un document PDF, vous pouvez utiliser la fonction [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextracttext/). Veuillez consulter l'extrait de code suivant afin d'extraire du texte d'un fichier PDF en utilisant JavaScript via C++.

1. Créer un 'FileReader'.

1. La fonction [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextracttext/) est exécutée.
1. Ensuite, si le 'json.errorCode' est 0, vous pouvez obtenir des liens vers les fichiers résultants. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, il y aura une erreur dans votre fichier, alors l'information sur une telle erreur sera contenue dans le fichier 'json.errorText'.

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
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker: ${evt.message}`);
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