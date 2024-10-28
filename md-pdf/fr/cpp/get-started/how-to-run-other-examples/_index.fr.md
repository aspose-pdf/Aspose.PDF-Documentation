---
title: Comment exécuter d'autres exemples Aspose.PDF pour C++
linktitle: Comment exécuter d'autres exemples
type: docs
weight: 50
url: /cpp/how-to-run-other-examples/
description: Cette page présente des directives qui seront utiles pour les exigences suivantes avant de télécharger et d'exécuter les exemples.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Exigences logicielles

Veuillez vous assurer de répondre aux exigences suivantes avant de télécharger et d'exécuter les exemples.

1. Microsoft Visual Studio 2017 ou une version ultérieure.
1. Gestionnaire de packages NuGet installé dans Visual Studio. Assurez-vous que la dernière version de l'API NuGet est installée dans Visual Studio. Pour des détails sur la façon d'installer le gestionnaire de packages NuGet, veuillez consulter <http://docs.nuget.org/ndocs/guides/install-nuget>
1. Allez dans `Tools->Options->NuGet Package Manager->Package Sources` et assurez-vous que l'option **nuget.org** est cochée
1. Le projet d'exemple utilise la fonctionnalité de restauration automatique de packages NuGet, vous devez donc avoir une connexion Internet active. Si vous n'avez pas de connexion Internet active sur la machine où les exemples doivent être exécutés, veuillez consulter [Installation](/pdf/cpp/installation/) et ajouter manuellement une référence à Aspose.PDF.dll dans le projet d'exemple.

## Télécharger depuis GitHub

Tous les exemples d'Aspose.PDF pour C++ sont hébergés sur [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-C).

- Vous pouvez soit cloner le dépôt en utilisant votre client GitHub préféré, soit télécharger le fichier ZIP depuis [ici](https://codeload.github.com/aspose-pdf/Aspose.PDF-for-C/zip/master).
- Extrayez le contenu du fichier ZIP dans n'importe quel dossier de votre ordinateur. Tous les exemples se trouvent dans le dossier **Examples**.
- Il y a deux fichiers de solution Visual Studio, un pour la console et l'autre pour l'application Web.
- Les projets sont créés dans Visual Studio 2013, mais les fichiers de solution sont compatibles avec Visual Studio 2010 SP1 et supérieur.

- Ouvrez le fichier de solution dans Visual Studio et construisez le projet.- Lors de la première exécution, les dépendances seront automatiquement téléchargées via NuGet.
- Le dossier **Data** à la racine du dossier **Examples** contient les fichiers d'entrée utilisés par les exemples CSharp. Il est obligatoire de télécharger le dossier **Data** avec le projet d'exemples.
- Ouvrez le fichier *RunExamples.cs*, tous les exemples sont appelés à partir d'ici.
- Décommentez les exemples que vous souhaitez exécuter à partir du projet.

N'hésitez pas à nous contacter via nos forums si vous avez des problèmes pour configurer ou exécuter les exemples.

## Contribuer

Si vous souhaitez ajouter ou améliorer un exemple, nous vous encourageons à contribuer au projet. Tous les exemples et projets de démonstration de ce dépôt sont open source et peuvent être librement utilisés dans vos propres applications.

Pour contribuer, vous pouvez bifurquer le dépôt, modifier le code source et créer une demande de tirage. Nous examinerons les modifications et les inclurons dans le dépôt si elles sont jugées utiles.