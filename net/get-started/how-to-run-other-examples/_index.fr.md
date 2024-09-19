---
title: Comment exécuter d'autres exemples
linktitle: Comment exécuter d'autres exemples
type: docs
weight: 50
url: /net/how-to-run-other-examples/    
description: Cette page présente des directives qui seront utiles pour respecter les exigences suivantes avant de télécharger et d'exécuter les exemples.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Exigences logicielles

Veuillez vous assurer de répondre aux exigences suivantes avant de télécharger et d'exécuter les exemples.

1. Visual Studio 2010 ou supérieur
1. Gestionnaire de paquets NuGet installé dans Visual Studio. Assurez-vous que la dernière version de l'API NuGet est installée dans Visual Studio. Pour plus de détails sur comment installer le gestionnaire de paquets NuGet, veuillez consulter <https://docs.microsoft.com/en-us/nuget/install-nuget-client-tools>
1. Allez dans `Outils->Options->Gestionnaire de paquets NuGet->Sources de paquets` et assurez-vous que l'option **nuget.org** est cochée
1.
## Télécharger depuis GitHub

Tous les exemples de Aspose.PDF pour .NET sont hébergés sur [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-.NET).

- Vous pouvez soit cloner le dépôt en utilisant votre client GitHub préféré, soit télécharger le fichier ZIP depuis [ici](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/archive/master.zip).
- Extrayez le contenu du fichier ZIP dans n'importe quel dossier sur votre ordinateur. Tous les exemples se trouvent dans le dossier **Exemples**.
- Il y a deux fichiers de solution Visual Studio, un pour la Console et l'autre pour l'Application Web.
- Les projets sont créés dans Visual Studio 2013, mais les fichiers de solution sont compatibles avec Visual Studio 2010 SP1 et versions ultérieures.
- Ouvrez le fichier de solution dans Visual Studio et construisez le projet.
- Lors de la première exécution, les dépendances seront automatiquement téléchargées via NuGet.
- Le dossier **Data** à la racine du dossier **Exemples** contient les fichiers d'entrée utilisés par les exemples CSharp. Il est obligatoire de télécharger le dossier **Data** en même temps que le projet d'exemples.
- Ouvrez le fichier *RunExamples.cs*, tous les exemples sont appelés à partir de là.
- Ouvrez le fichier *RunExamples.cs*, tous les exemples sont appelés à partir de là.
- Décommentez les exemples que vous souhaitez exécuter dans le projet.

N'hésitez pas à nous contacter via nos Forums si vous rencontrez des problèmes pour configurer ou exécuter les exemples.

## Contribuer

Si vous souhaitez ajouter ou améliorer un exemple, nous vous encourageons à contribuer au projet. Tous les exemples et projets de démonstration de ce dépôt sont open source et peuvent être librement utilisés dans vos propres applications.

Pour contribuer, vous pouvez forker le dépôt, modifier le code source et créer une pull request. Nous examinerons les modifications et les inclurons dans le dépôt si elles sont jugées utiles.
