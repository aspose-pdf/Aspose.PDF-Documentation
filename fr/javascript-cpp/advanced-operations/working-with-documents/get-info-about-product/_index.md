---
title: Obtenez des informations sur le produit en utilisant JavaScript
linktitle: Obtenez des informations sur le produit
type: docs
weight: 70
url: fr/javascript-cpp/get-info-about-product/
description: Ce sujet montre comment obtenir des informations sur le produit avec Aspose.PDF pour JavaScript via C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Ce sujet explique comment obtenir des informations sur le produit en utilisant JavaScript.

```js

    /*Créer un Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erreur du Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'chargé!' :
        (evt.data.json.errorCode !== 0) ? `Erreur: ${evt.data.json.errorText}` :
                          "Produit      : " + evt.data.json.product
                      + "\nFamille      : " + evt.data.json.family
                      + "\nVersion      : " + evt.data.json.version
                      + "\nDate de sortie : " + evt.data.json.releasedate
                      + "\nProducteur   : " + evt.data.json.producer
                      + "\nEst sous licence : " + evt.data.json.islicensed;

    /*Gestionnaire d'événements*/
    const onAsposePdfAbout = e => {
      /*Obtenez des informations sur le produit - Demander au Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfAbout', "params": [] }, []);
    };
```


The following JavaScript code snippet shows simple example of getting info about Product:

1. La fonction [AsposePdfAbout](https://reference.aspose.com/pdf/javascript-cpp/misc/asposepdfabout/) est exécutée.
1. Informations sur le produit qui peuvent être obtenues :
- Nom du produit
- Famille de produits
- Version du produit
- Date de sortie
- Nom complet/producteur
- Le produit est sous licence
1. Ensuite, si le 'json.errorCode' est 0, vous pouvez obtenir des informations sur le produit. Si le paramètre 'json.errorCode' n'est pas égal à 0 et, en conséquence, il y aura une erreur dans votre fichier, alors les informations sur cette erreur seront contenues dans le fichier 'json.errorText'.

```js

  var onAsposePdfAbout = function () {
    /*Obtenir des informations sur le produit*/
    const json = AsposePdfAbout();
    /* JSON
    Nom du produit       : json.product
    Famille de produits  : json.family
    Version du produit   : json.version
    Date de sortie       : json.releasedate
    Nom complet/producteur : json.producer
    Le produit est sous licence : json.islicensed
    */
    if (json.errorCode == 0) document.getElementById('output').textContent = 
                    "Produit      : " + json.product
                + "\nFamille      : " + json.family
                + "\nVersion      : " + json.version
                + "\nDate de sortie : " + json.releasedate
                + "\nProducteur   : " + json.producer
                + "\nSous licence : " + json.islicensed;
    else document.getElementById('output').textContent = json.errorText;
  }
```