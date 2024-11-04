---
title: Opérations avancées en utilisant JavaScript via C++
linktitle: Opérations avancées
type: docs
weight: 60
url: /javascript-cpp/advanced-operations/
description: Aspose.PDF pour JavaScript via C++ peut effectuer non seulement des tâches simples et faciles, mais aussi atteindre des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Opérations Avancées** est une section sur la façon de gérer les fichiers PDF existants de manière programmatique, qu'il s'agisse de documents créés avec Aspose.PDF comme discuté dans [Opérations de Base](/pdf/javascript-cpp/basic-operations/), ou de PDF créés avec Adobe Acrobat, Google Docs, Microsoft Office, Open Office ou tout autre producteur de PDF.

## Utilisation des Web Workers

La version 23.6 a ajouté la possibilité d'utiliser des Web Workers :

```js
const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
```

L'utilisation des Web Workers à partir de JavaScript via C++, vous permet d'effectuer des opérations sans bloquer l'interface, dans un thread de travail séparé.

Web Workers est un outil simple pour exécuter des scripts en arrière-plan. Ce qui vous permet d'effectuer des tâches sans interférer avec l'interface utilisateur, dans un thread de travail séparé.

Vous apprendrez différentes manières de :

- [Travailler avec des documents](/pdf/javascript-cpp/working-with-documents/) - compresser, diviser et fusionner des documents et effectuer d'autres opérations avec l'ensemble du document.
- [Travailler avec des pages](/pdf/javascript-cpp/working-with-pages/) - ajouter, déplacer ou supprimer, rogner des pages, des tampons.
- [Métadonnées dans les PDFs](/pdf/javascript-cpp/pdf-file-metadata/) - obtenir ou définir des métadonnées dans les documents.
- [Travailler avec des images](/pdf/javascript-cpp/working-with-images/) - insérer, supprimer, extraire une image dans le document
- [Navigation et interaction](/pdf/javascript-cpp/navigation-and-interaction/) - gérer les actions, les signets, naviguer dans les pages
- [Annotations](/pdf/javascript-cpp/annotations/) - Les annotations permettent aux utilisateurs d'ajouter du contenu personnalisé sur les pages PDF. Vous pouvez ajouter, supprimer et modifier l'annotation des documents PDF.

- [Sécurisation et signature](/pdf/javascript-cpp/securing-and-signing/) - protéger et signer votre document PDF par programme
- [Pièces jointes](/pdf/javascript-cpp/attachments/) - Les documents PDF peuvent contenir des pièces jointes. Ces pièces jointes peuvent être d'autres documents PDF ou tout type de fichier, comme des fichiers audio, des documents Microsoft Office, etc. Vous apprendrez comment ajouter des pièces jointes à un PDF, obtenir les informations d'une pièce jointe, l'enregistrer dans un fichier, supprimer la pièce jointe d'un PDF de manière programmatique avec JavaScript.