---
title: Aspose.PDF Java using Maven for Eclipse
type: docs
weight: 80
url: /java/aspose-pdf-java-using-maven-for-eclipse/
lastmod: "2021-06-05"
---

## Introduction

### Eclipse IDE

Eclipse IDE est un environnement de développement intégré Java célèbre. L'IDE est certainement le produit le plus connu du projet Open Source Eclipse. Aujourd'hui, c'est l'environnement de développement principal pour Java avec une part de marché d'environ 60%.

L'IDE Eclipse peut être étendu avec des composants logiciels supplémentaires. Eclipse appelle ces composants logiciels des Plug-ins. Plusieurs projets Open Source et entreprises ont étendu l'IDE Eclipse ou créé des applications autonomes (Eclipse RCP) sur la base du cadre Eclipse.

### Aspose.PDF pour Java

[Aspose.PDF pour Java](https://products.aspose.com/pdf/java/) est une API robuste de création de documents PDF qui permet à vos applications Java de lire, écrire et manipuler des documents PDF sans utiliser Adobe Acrobat.

Aspose.PDF pour Java offre une incroyable richesse de fonctionnalités, y compris des options de compression PDF, la création et la manipulation de tableaux, le support des graphiques, des fonctions d'image, une fonctionnalité de lien hypertexte étendue, des contrôles de sécurité avancés et une gestion personnalisée des polices.

### Aspose.PDF Java (Maven) pour Eclipse

- Aspose.PDF Java (Maven) pour Eclipse est un Plugin pour **Eclipse IDE** par **Aspose.** Ce Plugin est destiné aux développeurs utilisant la plateforme Maven pour les développements Java et qui souhaitent utiliser Aspose.PDF pour Java dans leurs projets. Le Plugin vous permet de créer des projets maven pour utiliser Aspose.PDF pour l'API Java et de télécharger également des [Exemples de Code](https://github.com/aspose-pdf/Aspose.Pdf-for-Java) de l'API.
- Le plugin offre les fonctionnalités suivantes pour travailler confortablement avec l'API Aspose.PDF pour Java au sein de **Eclipse IDE** :

![todo:image_alt_text](https://i.imgur.com/KWKGljg.png)

**ASSISTANTS** :
Le plugin contient deux assistants

**Projet Maven Aspose.PDF (assistant)**

- Ce nouvel assistant de projet permet aux développeurs de créer un projet **Maven** pour utiliser Aspose.PDF pour Java à partir de Nouveau -> Projet -> Maven-> Projet Maven Aspose.PDF.

- La référence de la dépendance maven de l'API Aspose.PDF pour Java est automatiquement récupérée depuis le [Dépôt Maven Cloud Aspose](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo) et est ajoutée dans le pom.xml.
- Le projet créé contiendra toujours la version la plus récente disponible de la dépendance **Maven** pour l'API Aspose.PDF pour Java.
- Les étapes de l'assistant sont également présentées avec l'option de téléchargement des [Exemples de Code](https://github.com/aspose-pdf/Aspose.Pdf-for-Java) pour utiliser l'API Aspose.PDF pour Java.
Exemple de Code Aspose.PDF (assistant)

- Cet assistant de Nouveau Fichier vous permet de copier les [Exemples de Code](https://github.com/aspose-pdf/Aspose.Pdf-for-Java) téléchargés dans votre projet pour utiliser Aspose.PDF pour Java depuis Nouveau -> Autre -> Java -> Exemple de Code Aspose.PDF.
- Les exemples disponibles sont affichés sous forme d'arborescence à partir de laquelle l'utilisateur peut les sélectionner catégoriquement.
- Tous les exemples de la catégorie sélectionnée seront copiés dans le dossier du package "**com.aspose.pdf.examples**" du projet ainsi que les ressources requises dans le dossier "**src/main/resources**" nécessaires pour exécuter les exemples.
- Les Exemples de Code de l'API Aspose.PDF pour Java sont destinés à démontrer les diverses fonctions de l'API.

- L'assistant recherchera également et mettra à jour les nouveaux Exemples de Code disponibles) depuis le dépôt des exemples Aspose.PDF pour Java.

## Exigences du Système et Plates-formes Supportées

### Exigences du Système

- **Mémoire Système:** 2 Go ou plus (Recommandé)
- **OS:** Tout système d'exploitation qui supporte la Java VM (Machine Virtuelle)
- **Connexion Internet:** 2 MB ou plus rapide (Recommandé)

### Plates-formes Supportées

- Eclipse Mars.1 (4.5.1) - Recommandé
- Eclipse Juno ou plus récent.

## Téléchargement

### Télécharger Eclipse IDE

Vous devrez d'abord installer Eclipse IDE avant de télécharger le plugin Aspose.PDF Java (Maven) pour Eclipse.

Pour télécharger Eclipse IDE

1. Allez sur [https://eclipse.org](https://eclipse.org/).
1. Téléchargez et installez l'Eclipse IDE recommandé pour les développeurs Java SE / EE.

### Télécharger Aspose.PDF Java (Maven) pour Eclipse

Voici trois méthodes recommandées pour le téléchargement et l'installation réussis du plugin Aspose.PDF Java (Maven) pour Eclipse :

- Installation par glisser-déposer depuis [Eclipse Marketplace](https://marketplace.eclipse.org/content/asposepdf-java-maven-eclipse) vers votre espace de travail Eclipse.

- Ou allez dans **Aide** > **Installer un nouveau logiciel...** > Entrez l'URL du site de mise à jour suivante dans **Travailler avec**
Then select "Aspose.PDF Java (Maven) for Eclipse" and **Terminer**. Acceptez le contrat de licence et installez le plugin.

## Installation

Installation d'Aspose.PDF Java (Maven) pour Eclipse

## Utilisation du Plugin

Utilisation d'Aspose.PDF Java (Maven) pour Eclipse

### Comment appliquer la licence Aspose ?

Ce plugin utilise une version d'évaluation d'Aspose.PDF. Une fois que vous êtes satisfait de votre évaluation, vous pouvez acheter une licence sur le [site Web d'Aspose](https://purchase.aspose.com/buy).
Pour supprimer le message d'évaluation et les limitations de fonctionnalités, une licence de produit doit être appliquée. Vous recevrez un fichier de licence après avoir acheté le produit. Veuillez suivre les étapes ci-dessous pour appliquer la licence

- Assurez-vous que le fichier de licence est nommé Aspose.PDF.Java.lic
- Placez le fichier **Aspose.PDF.Java.lic** dans le dossier contenant Aspose.PDF.jar
- Utilisez le code suivant pour activer la licence :

{{< highlight java >}}

 License license = new License();

license.setLicense("Aspose.PDF.Java.lic");

{{< /highlight >}}


## Support, Extension et Contribution

### Support

- Si vous souhaitez voir les problèmes connus/rapportés (par les utilisateurs ou l'équipe Q.A) dans le plugin.
- Ou si vous voulez signaler un problème que vous avez trouvé dans le plugin.
- Avez-vous une suggestion d'amélioration ou souhaitez-vous faire une demande de fonctionnalité ?

Veuillez suivre [**GitHub Issues Tracker**](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues) pour enregistrer tout problème trouvé dans le plugin.

### Étendre et Contribuer

Aspose.PDF Java (Maven) pour Eclipse est open source et son code source est disponible sur les principaux sites de codage social listés ci-dessous. Les développeurs sont encouragés à télécharger le code source et à contribuer en suggérant ou en ajoutant de nouvelles fonctionnalités ou en améliorant les fonctionnalités existantes afin que d'autres puissent également en bénéficier. Les développeurs peuvent également apprendre à partir de celui-ci pour créer leurs propres plugins.

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_Maven_for_Eclipse)

### Comment configurer le code source d'Aspose.PDF Java (Maven) pour Eclipse

Les étapes simples ci-dessous vous guideront facilement vers une configuration réussie du code source du plugin **"Aspose.PDF Java (Maven) for Eclipse"** dans l'IDE Eclipse.

1. Téléchargez / Clonez le code source.
1. Choisissez **Fichier** > Importer > Général > Projets existants dans l'espace de travail
1. Parcourez jusqu'à la source du projet la plus récente que vous avez téléchargée
1. Sélectionnez le projet Eclipse que vous souhaitez importer
1. Cliquez sur Terminer
1. Le code du plugin Aspose.PDF Java pour Eclipse est maintenant prêt à être amélioré.