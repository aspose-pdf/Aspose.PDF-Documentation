---
title: Optimiser, Compresser ou Réduire la Taille d'un PDF en Python
linktitle: Optimiser PDF
type: docs
weight: 30
url: /fr/python-cpp/optimize-pdf/
description: Optimiser un fichier PDF, réduire toutes les images, réduire la taille du PDF, désintégrer les polices, supprimer les objets inutilisés avec Python.
lastmod: "2023-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Un document PDF peut parfois contenir des données supplémentaires. Réduire la taille d'un fichier PDF vous aidera à optimiser le transfert réseau et le stockage. Cela est particulièrement utile pour publier sur des pages web, partager sur les réseaux sociaux, envoyer par e-mail ou archiver dans le stockage. Nous pouvons utiliser plusieurs techniques pour optimiser un PDF :

- Optimiser le contenu des pages pour la navigation en ligne
- Réduire ou compresser toutes les images
- Activer la réutilisation du contenu des pages
- Fusionner les flux en double
- Désintégrer les polices
- Supprimer les objets inutilisés
- Supprimer les champs de formulaire aplatis
- Supprimer ou aplatir les annotations

{{% alert color="primary" %}}

Explication détaillée des méthodes d'optimisation peut être trouvée dans la page Vue d'ensemble des méthodes d'optimisation.

{{% /alert %}}

## Optimiser un document PDF pour le Web

L'optimisation, ou la linéarisation pour le Web, se réfère au processus de rendre un fichier PDF adapté à la navigation en ligne à l'aide d'un navigateur web. Pour optimiser un fichier pour l'affichage web :

Le code suivant montre comment optimiser un document PDF pour le web.

```python

    import AsposePDFPythonWrappers as ap

    # Le chemin vers le répertoire des documents.
    dataDir = "..."

    # Ouvrir le document
    document = ap.Document(dataDir + "OptimizeDocument.pdf")

    # Optimiser pour le web
    document.optimize()

    dataDir = dataDir + "OptimizeDocument_out.pdf"

    # Enregistrer le document de sortie
    document.Save(dataDir)
```