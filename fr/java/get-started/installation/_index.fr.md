---
title: Installer Aspose.PDF pour Java
linktitle: Installation
type: docs
weight: 20
url: /java/installation/
description: Cette section montre une description du produit et des instructions pour installer Aspose.PDF pour Java par vous-même, ainsi qu'en utilisant NuGet.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Composant Aspose.PDF pour Java

{{% alert color="primary" %}}

**Aspose.PDF est un composant Java** conçu pour permettre aux développeurs de créer des documents PDF, qu'ils soient simples ou complexes, à la volée de manière programmatique. Aspose.PDF pour Java permet aux développeurs d'insérer des tables, des graphiques, des images, des hyperliens, des polices personnalisées - et plus encore - dans les documents PDF. De plus, il est également possible de compresser les documents PDF. Aspose.PDF pour Java offre d'excellentes fonctionnalités de sécurité pour développer des documents PDF sécurisés. Et la caractéristique la plus distincte d'Aspose.PDF pour Java est qu'il prend en charge la création de documents PDF à la fois via une API et à partir de modèles XML.

{{% /alert %}}

## Description du produit


**Aspose.PDF for Java** est implémenté en utilisant Java et fonctionne avec JDK 1.8 et supérieur. Aspose.PDF for Java peut être intégré à n'importe quelle application, par exemple une application web JSP/JSF ou une application Windows.

**Aspose.PDF for Java** est rapide et léger. Il crée des documents PDF efficacement et aide votre application à mieux fonctionner. Aspose.PDF for Java est le premier choix de nos clients pour la création de documents PDF en raison de son prix, de ses performances exceptionnelles et de son excellent support. En utilisant cette bibliothèque, vous pouvez implémenter des fonctionnalités avancées pour créer des fichiers PDF à partir de zéro, ou traiter complètement des documents PDF existants sans installer Adobe Acrobat.

# Installation

## Évaluer Aspose.PDF pour Java

{{% alert color="primary" %}}

Vous pouvez télécharger [Aspose.PDF for Java](https://releases.aspose.com/java/repo/com/aspose/aspose-pdf/) pour évaluation.
 Le téléchargement d'évaluation est identique au téléchargement acheté. La version d'évaluation devient simplement sous licence lorsque vous ajoutez quelques lignes de code pour [appliquer la licence](/pdf/java/licensing/).

{{% /alert %}}

La version d'évaluation d'Aspose.PDF offre une fonctionnalité complète du produit, mais elle a deux limitations :

- Elle insère un filigrane d'évaluation.
- Pas plus de quatre éléments de toute collection ne peuvent être visualisés/édités.
- **Un document montrant le filigrane d'évaluation**

![Évaluation de Aspose.PDF](evaluate-aspose-pdf_1.png)

{{% alert color="primary" %}}

Si vous souhaitez tester Aspose.PDF pour Java sans les limitations de la version d'évaluation, vous pouvez également demander une licence temporaire de 30 jours. Veuillez consulter [Comment obtenir une licence temporaire ?](https://purchase.aspose.com/temporary-license)

{{% /alert %}}

## Installation d'Aspose.PDF pour Java à partir du dépôt Aspose

Aspose héberge toutes les API Java sur [Dépôt Aspose](https://releases.aspose.com/java/repo/com/aspose/aspose-pdf/). Vous pouvez facilement utiliser l'API Aspose.PDF pour Java directement dans vos projets Maven avec des configurations simples.

### Spécifier la Configuration du Dépôt Aspose

Tout d'abord, vous devez spécifier la configuration / l'emplacement du dépôt Aspose dans votre Maven pom.xml comme suit :

```xml
 <repositories>
    <repository>
        <id>AsposeJavaAPI</id>
        <name>Aspose Java API</name>
        <url>https://releases.aspose.com/java/repo/</url>
    </repository>
</repositories>
```

### Définir la Dépendance Aspose.PDF pour l'API Java

Ensuite, définissez la dépendance Aspose.PDF pour l'API Java dans votre pom.xml comme suit :

```xml
 <dependencies>
    <dependency>
        <groupId>com.aspose</groupId>
        <artifactId>aspose-pdf</artifactId>
        <version>21.7</version>
    </dependency>
</dependencies>
```

Après avoir effectué les étapes ci-dessus, la dépendance Aspose.PDF pour Java sera finalement définie dans votre projet Maven.

### Compatibilité JDK 11 et Ligne Directrice d'Utilisation

L'API est optimisée pour l'environnement Java 11 et tous les tests et fonctionnalités fonctionnent correctement. Cependant, pour certaines classes, vous devez ajouter la dépendance externe pour ajouter le classpath de la classe : javax.xml.bind.annotation.adapters.HexBinaryAdapter, qui a été supprimée du JRE.

Par exemple :

```xml
 <dependency>
    <groupId>javax.xml.bind</groupId>
    <artifactId>jaxb-api</artifactId>
    <version>2.3.0</version>
</dependency>
```