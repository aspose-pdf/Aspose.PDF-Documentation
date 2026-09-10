---
title: Aspose.PDF Java utilisant Maven pour Eclipse
linktitle: Aspose.PDF Java utilisant Maven pour Eclipse
type: docs
weight: 80
url: /java/aspose-pdf-java-using-maven-for-eclipse/
description: Configurez Aspose.PDF pour Java dans Eclipse à l'aide de Maven. Simplifiez la gestion des dépendances pour un développement PDF efficace.
lastmod: "2026-06-09"
---
## 
Introduction


### 
Eclipse

Eclipse IDE est un célèbre environnement de développement intégré (IDE) Java. L'EDI est certainement le produit le plus connu du projet Eclipse Open Source. Il s'agit aujourd'hui du principal environnement de développement pour Java avec une part de marché d'environ 60 %.



L'IDE Eclipse peut être étendu avec des composants logiciels supplémentaires. Eclipse appelle ces composants logiciels Plug-ins. Plusieurs projets et entreprises Open Source ont étendu l'IDE Eclipse ou créé des applications autonomes (Eclipse RCP) au-dessus du framework Eclipse.


### 
Aspose.PDF pour Java



[Aspose.PDF for Java] (https://products.aspose.com/pdf/java/) est une API robuste de création de documents PDF qui permet à vos applications Java de lire, d'écrire et de manipuler des documents PDF sans utiliser Adobe Acrobat.



Aspose.PDF pour Java offre une incroyable richesse de fonctionnalités, notamment des options de compression PDF, la création et la manipulation de tableaux, la prise en charge de graphiques, des fonctions d'image, une fonctionnalité étendue de liens hypertexte, des contrôles de sécurité étendus et une gestion des polices personnalisées.

### Aspose.PDF Java (Maven) pour Eclipse


- 
Aspose.PDF Java (Maven) pour Eclipse est un plugin pour **Eclipse IDE** par **Aspose.** Ce plugin est destiné aux développeurs utilisant la plateforme Maven pour les développements Java et souhaitant utiliser Aspose.PDF pour Java dans leurs projets. Le plugin vous permet de créer des projets Maven pour utiliser Aspose.PDF pour l'API Java et également de télécharger des [exemples de code] (https://github.com/aspose-pdf/Aspose.Pdf-for-Java) de l'API.

- 
Le plugin fournit les fonctionnalités suivantes pour travailler confortablement avec l'API Aspose.PDF pour Java dans **Eclipse IDE** :


![todo:image_alt_text](https://i.imgur.com/KWKGljg.png)


**ASSISTANTS** :


Le plugin contient deux assistants

**Projet Aspose.PDF Maven (assistant)**


- 
Cet assistant de nouveau projet permet aux développeurs de créer un projet**Maven** pour utiliser Aspose.PDF pour Java à partir de Nouveau -> Projet -> Maven-> Projet Aspose.PDF Maven.

- 
La référence de la dépendance maven de l'API Java Aspose.PDF est automatiquement extraite de [Aspose Cloud Maven Repository] (https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo) et est ajoutée dans le pom.xml.

- 
Le projet créé contiendra toujours la version disponible la plus récente **Maven** Dépendance pour Aspose.PDF pour l'API Java.

- 
Les étapes de l'assistant proposent également la possibilité de télécharger des [Exemples de code] (https://github.com/aspose-pdf/Aspose.Pdf-for-Java) pour utiliser Aspose.PDF pour l'API Java.
Exemple de code Aspose.PDF (assistant)


- 
Cet assistant de nouveau fichier vous permet de copier les [exemples de code] (https://github.com/aspose-pdf/Aspose.Pdf-for-Java) téléchargés dans votre projet pour utiliser Aspose.PDF pour Java à partir de Nouveau -> Autre -> Java -> Exemple de code Aspose.PDF.

- 
Les échantillons disponibles sont affichés sous forme d'arborescence à partir de laquelle l'utilisateur peut les sélectionner de manière catégorique.

- 
Tous les exemples de la catégorie sélectionnée seront copiés dans le dossier du package « **com.aspose.pdf.examples** » du projet avec les ressources requises dans le dossier « **src/main/resources** » nécessaires pour exécuter les exemples.

- 
Les exemples de code d'Aspose.PDF pour l'API Java sont destinés à démontrer les différentes fonctions de l'API.
- L'assistant recherchera et mettra également à jour les exemples de code nouvellement disponibles) à partir du référentiel d'exemples Aspose.PDF pour Java.


## 
Configuration système requise et plates-formes prises en charge


### 
Configuration système requise


- 
**Mémoire système :** 2 Go ou plus (recommandé)

- 
**OS :** tout système d'exploitation prenant en charge la machine virtuelle Java (machine virtuelle)
- **Connexion Internet :** 2 Mo ou plus (recommandé)


### 
Plateformes prises en charge


- 
Eclipse Mars.1 (4.5.1) - Recommandé

- 
Eclipse Juno ou version ultérieure.


## 
Téléchargement

### Download Eclipse IDE



You will need to first install Eclipse IDE before downloading the Aspose.PDF Java (Maven) for Eclipse plugin.



To download Eclipse IDE


1. 
Go to [https://eclipse.org](https://eclipse.org/).

1. 
Download and install the recommended Eclipse IDE for Java SE / EE developers.

### Télécharger Aspose.PDF Java (Maven) pour Eclipse



Following are three recommended methods for the successful downloading and installation of Aspose.PDF Java (Maven) for Eclipse plugin:


- 
Drag and drop installation from [Eclipse Marketplace](https://marketplace.eclipse.org/content/asposepdf-java-maven-eclipse) to your Eclipse workspace.

- 
Ou allez à **Aide** > **Installer un nouveau logiciel...** > Entrez l'URL du site de mise à jour suivante dans **Travailler avec


Then select "Aspose.PDF Java (Maven) for Eclipse" and **Finish**. Acceptez le contrat de licence et installez le plugin.

## Installation



Installation d'Aspose.PDF Java (Maven) pour Eclipse


## 
Utiliser le plugin



Utilisation d'Aspose.PDF Java (Maven) pour Eclipse


### 
Comment appliquer la licence Aspose ?

Ce plugin utilise une version d'évaluation d'Aspose.PDF. Une fois que vous êtes satisfait de votre évaluation, vous pouvez acheter une licence sur le [site Web Aspose] (https://purchase.aspose.com/buy).


Pour supprimer le message d'évaluation et les limitations des fonctionnalités, une licence de produit doit être appliquée. Vous recevrez un fichier de licence après avoir acheté le produit. Veuillez suivre les étapes ci-dessous pour appliquer la licence


- 
Assurez-vous que le fichier de licence est nommé Aspose.PDF.Java.lic

- 
Placez le fichier **Aspose.PDF.Java.lic** dans le dossier contenant le fichier Aspose.PDF.jar.

- 
Utilisez le code suivant pour activer la licence :

{{< highlight java >}}

 Licence licence = nouvelle Licence();



licence.setLicense("Aspose.PDF.Java.lic");


{{< /highlight >}}

## 
Soutenir, étendre et contribuer


### 
Assistance


- 
Si vous souhaitez voir les problèmes connus/signalés (par les utilisateurs ou l'équipe Q.A) dans le plugin.
- Ou vous souhaitez signaler tout problème que vous avez trouvé dans le plugin

- 
Vous avez des suggestions d'amélioration ou souhaitez faire une demande de fonctionnalité



Veuillez suivre [**GitHub Issues Tracker**] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues) pour enregistrer tous les problèmes trouvés dans le plugin.


### 
Prolongez et contribuez



Aspose.PDF Java (Maven) pour Eclipse est open source et son code source est disponible sur les principaux sites Web de codage social répertoriés ci-dessous. Les développeurs sont encouragés à télécharger le code source et à contribuer en suggérant ou en ajoutant de nouvelles fonctionnalités ou en améliorant celles existantes afin que d'autres puissent également en bénéficier. Les développeurs peuvent également en tirer des leçons pour créer leurs propres plugins.

- [GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_Maven_for_Eclipse)


### 
Comment configurer le code source d'Aspose.PDF Java (Maven) pour Eclipse



Les étapes simples ci-dessous mèneront facilement à une configuration réussie du code source du plug-in **"Aspose.PDF Java (Maven) pour Eclipse"** dans l'IDE Eclipse.


1. 
Téléchargez/Clonez le code source.

1. 
Choisissez **Fichier** > Importer > Général > Projets existants dans l'espace de travail.
1. Accédez à la dernière source de projet que vous avez téléchargée

1. 
Sélectionnez le projet Eclipse que vous souhaitez importer

1. 
Cliquez sur Terminer

1. 
Le code du plugin Aspose.PDF Java pour Eclipse est maintenant prêt à être amélioré.
