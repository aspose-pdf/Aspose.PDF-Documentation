---
title: Comment installer Aspose.PDF pour .NET
linktitle: Installation
type: docs
weight: 20
url: /net/installation/
description: Cette section présente une description du produit et des instructions pour installer Aspose.PDF pour .Net par vous-même, ainsi que l'utilisation de NuGet.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Composant Aspose.PDF C#

{{% alert color="primary" %}}

**Aspose.PDF est un** composant .NET conçu pour permettre aux développeurs de créer des documents PDF, qu'ils soient simples ou complexes, de manière programmée à la volée. Aspose.PDF pour .NET permet aux développeurs d'insérer des tables, des graphiques, des images, des hyperliens, des polices personnalisées - et plus encore - dans des documents PDF. De plus, il est également possible de compresser les documents PDF. Aspose.PDF pour .NET offre d'excellentes fonctionnalités de sécurité pour développer des documents PDF sécurisés. Et la caractéristique la plus distincte d'Aspose.PDF pour .NET est qu'il prend en charge la création de documents PDF à la fois via une API et à partir de modèles XML.

{{% /alert %}}

## Description du produit

**Aspose.PDF pour .NET** est un composant .NET robuste qui permet aux développeurs de créer des documents PDF à partir de zéro sans utiliser Adobe Acrobat.
**Aspose.PDF pour .NET** est un composant .NET robuste qui permet aux développeurs de créer des documents PDF à partir de zéro sans utiliser Adobe Acrobat.

**Aspose.PDF pour .NET** est implémenté en utilisant Managed C# et peut être utilisé avec n'importe quel langage .NET comme C#, VB.NET et J# etc. Il peut être intégré à tout type d'application, qu'il s'agisse d'une application Web ASP.NET ou d'une application Windows.

Afin que les développeurs puissent démarrer rapidement, Aspose.PDF pour .NET fournit des démos complètes et des exemples fonctionnels écrits en C#. En utilisant ces démos, les développeurs peuvent rapidement apprendre les fonctionnalités offertes par Aspose.PDF pour .NET.

Le composant rapide et léger crée des documents PDF de manière efficace et aide votre application à mieux performer. Aspose.PDF pour .NET est le premier choix de nos clients lors de la création de documents PDF en raison de son prix, de ses performances exceptionnelles et de son excellent support.

**Aspose.PDF pour .NET** est sûr pour les multi-thread tant qu'un seul thread travaille sur un document à la fois.
**Aspose.PDF pour .NET** est sûr pour l'exécution multithread tant que seulement un thread travaille sur un document à la fois.

## Déclaration

Tous les composants Aspose .NET nécessitent un ensemble d'autorisations de confiance totale. La raison en est que les composants Aspose .NET doivent accéder aux paramètres du registre, aux fichiers système autres que le répertoire virtuel pour certaines opérations telles que l'analyse des polices, etc. De plus, les composants Aspose .NET sont basés sur les classes système de base .NET qui nécessitent également un ensemble d'autorisations de confiance totale dans de nombreux cas.

Les fournisseurs de services Internet hébergeant plusieurs applications de différentes entreprises imposent généralement un niveau de sécurité de confiance moyenne. Dans le cas de .NET 2.0, ce niveau de sécurité applique les contraintes suivantes :

- **OleDbPermission n'est pas disponible.** Cela signifie que vous ne pouvez pas utiliser le fournisseur de données OLE DB géré par ADO.NET pour accéder aux bases de données.
- **EventLogPermission n'est pas disponible.** Cela signifie que vous ne pouvez pas accéder au journal des événements Windows.
- **ReflectionPermission n'est pas disponible.** Cela signifie que vous ne pouvez pas utiliser la réflexion.
- **RegistryPermission n'est pas disponible.** Cela signifie que vous ne pouvez pas accéder au registre.

changefreq: "monthly"
type: docs
- **RegistryPermission n'est pas disponible.** Cela signifie que vous ne pouvez pas accéder au registre.
- **WebPermission est restreint.** Cela signifie que votre application ne peut communiquer qu'avec une adresse ou une plage d'adresses que vous définissez dans l'élément `<trust>`.
- **FileIOPermission est restreint.** Cela signifie que vous ne pouvez accéder qu'aux fichiers dans la hiérarchie des répertoires virtuels de votre application.
Pour les raisons spécifiées ci-dessus, les composants Aspose .NET ne peuvent pas être utilisés sur des serveurs accordant un ensemble de permissions autre que Full Trust.

# Installation

## Évaluer Aspose.PDF pour .NET

Vous pouvez facilement télécharger Aspose.PDF pour .Net pour évaluation. Le téléchargement d'évaluation est identique au téléchargement acheté. La version d'évaluation devient simplement licenciée lorsque vous ajoutez quelques lignes de code pour appliquer la licence.

La version d'évaluation d'Aspose.PDF (sans licence spécifiée) offre toutes les fonctionnalités du produit, mais elle présente deux limitations : elle insère un filigrane d'évaluation, et seulement quatre éléments de toute collection peuvent être visualisés/édités.

{{% alert color="primary" %}}
{{% alert color="primary" %}}

Si vous souhaitez tester Aspose.PDF pour .NET sans les limitations de la version d'évaluation, vous pouvez également demander une Licence Temporaire de 30 jours. Veuillez consulter [Comment obtenir une Licence Temporaire ?](https://purchase.aspose.com/temporary-license)

{{% /alert %}}

## Installation de Aspose.PDF pour .NET via NuGet

NuGet est un système de gestion de paquets gratuit et open source axé sur les développeurs pour la plateforme .NET, visant à simplifier le processus d'intégration de bibliothèques tierces dans une application .NET pendant le développement.
NuGet est un système de gestion de paquets gratuit et open source axé sur les développeurs pour la plateforme .NET, qui vise à simplifier le processus d'intégration de bibliothèques tierces dans une application .NET pendant le développement.

### Référencement d'Aspose.PDF pour .NET

#### Installer le paquet en utilisant la console du gestionnaire de paquets

- Ouvrez votre application .NET dans Visual Studio.
- Dans le menu Outils, sélectionnez **Gestionnaire de Paquets NuGet** puis **Console du Gestionnaire de Paquets**.
- Tapez la commande `Install-Package Aspose.PDF` pour installer la dernière version complète, ou tapez la commande `Install-Package Aspose.PDF -prerelease` pour installer la dernière version incluant des correctifs.
- Appuyez sur `Entrée`

#### Mettre à jour le paquet en utilisant la console du gestionnaire de paquets

Si vous avez déjà référencé le composant via NuGet, suivez ces étapes pour mettre à jour la référence à la dernière version :

- Ouvrez votre application .NET dans Visual Studio.
- Dans le menu Outils, sélectionnez **Gestionnaire de Paquets NuGet** puis **Console du Gestionnaire de Paquets**.
- Tapez la commande `Update-Package Aspose.PDF` pour référencer la dernière version complète, ou tapez la commande `Update-Package Aspose.PDF -prerelease` pour installer la dernière version incluant des correctifs.
- Tapez la commande `Update-Package Aspose.PDF` pour référencer la dernière version complète, ou tapez la commande `Update-Package Aspose.PDF -prerelease` pour installer la dernière version incluant les correctifs.

#### Installer le paquet en utilisant l'interface graphique du gestionnaire de paquets

Suivez ces étapes pour référencer le composant via l'interface graphique du gestionnaire de paquets :

- Ouvrez votre application .NET dans Visual Studio.

- Depuis le menu Projet, sélectionnez **Gérer les paquets NuGet**.

![Installation_step](../images/install_step.png)

- Sélectionnez l'onglet **Parcourir**.

![Installation_step1](../images/install_step1.png)

- Tapez Aspose.PDF dans la zone de recherche pour trouver Aspose.PDF pour .NET.

- Cliquez sur Installer/Mettre à jour à côté de la dernière version de Aspose.PDF pour .NET.

![Installation_step2](../images/install_step2.png)

- Et cliquez sur Accepter dans la fenêtre pop-up.

![Installation_step3](../images/install_step3.png)

![Installation](../images/install.gif)

### Travailler avec les DLL .NET Core dans un environnement non Windows

Comme Aspose.PDF pour .NET fournit un support .NET Standard 2.0 (.NET Core 2.0), il peut être utilisé dans des applications Core fonctionnant sous des systèmes d'exploitation de type Linux.
Comme Aspose.PDF pour .NET prend en charge .NET Standard 2.0 (.NET Core 2.0), il peut être utilisé dans les applications Core fonctionnant sous des systèmes d'exploitation similaires à Linux.

Veuillez installer :

- le paquet libgdiplus
- le paquet avec des polices compatibles Microsoft : **ttf-mscorefonts-installer**. (par exemple, `sudo apt-get install ttf-mscorefonts-installer`)
Ces polices doivent être placées dans le répertoire "/usr/share/fonts/truetype/msttcorefonts" car Aspose.PDF pour .NET scanne ce dossier sur des systèmes d'exploitation similaires à Linux. Dans le cas où le système d'exploitation a un autre dossier/répertoire par défaut pour les polices, vous devriez utiliser la ligne de code suivante avant d'effectuer toute opération utilisant Aspose.PDF.

```csharp
Aspose.Pdf.Text.FontRepository.Sources.Add(new FolderFontSource("<chemin de l'utilisateur vers les polices ms>"));
```
