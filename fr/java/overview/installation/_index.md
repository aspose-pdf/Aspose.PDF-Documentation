---
title: Installer la bibliothèque
linktitle: Installation
type: docs
weight: 40
url: /java/installation/
description: Découvrez comment installer Aspose.PDF for Java dans un projet Maven et configurer ses dépendances.
lastmod: "2026-09-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Installation d'Aspose.PDF for Java
Abstract: Cet article présente Aspose.PDF for Java, les limites de la version d’évaluation et la configuration du dépôt Aspose et de la dépendance Maven. Il fournit également des indications sur les dépendances nécessaires avec JDK 11.
---
## Bibliothèque Aspose.PDF for Java

{{% alert color="primary" %}}

**Aspose.PDF est un composant Java** conçu pour permettre aux développeurs de créer des documents PDF, qu'ils soient simples ou complexes, à la volée par programme. Aspose.PDF for Java permet aux développeurs d'insérer des tableaux, des graphiques, des images, des hyperliens, des polices personnalisées - et bien plus encore - dans des documents PDF. De plus, il est également possible de compresser des documents PDF. Aspose.PDF for Java fournit d'excellentes fonctionnalités de sécurité pour développer des documents PDF sécurisés. Et la caractéristique la plus distinctive d'Aspose.PDF for Java est qu'il prend en charge la création de documents PDF via une API et à partir de modèles XML.

{{% /alert %}}

## Description du produit

**Aspose.PDF for Java** est implémenté à l'aide de Java et fonctionne avec JDK 1.8 et supérieur. Aspose.PDF for Java peut être intégré à n'importe quelle application, par exemple une application Web JSP/JSF ou une application Windows.

**Aspose.PDF for Java** est rapide et léger. Il crée des documents PDF efficacement et aide votre application à mieux fonctionner. Aspose.PDF for Java est le premier choix de nos clients lors de la création de documents PDF en raison de son prix, de ses superbes performances et de son excellent support.
Grâce à cette bibliothèque, vous pouvez mettre en œuvre de riches fonctionnalités pour créer des fichiers PDF à partir de zéro ou traiter complètement des documents PDF existants sans installer Adobe Acrobat.

## Évaluer Aspose.PDF for Java

{{% alert color="primary" %}}

Vous pouvez télécharger [Aspose.PDF for Java](https://releases.aspose.com/java/repo/com/aspose/aspose-pdf/) pour évaluation. Le téléchargement d'évaluation est le même que le téléchargement acheté. La version d'évaluation devient simplement sous licence lorsque vous ajoutez quelques lignes de code pour [appliquer la licence](/pdf/java/licensing/).

{{% /alert %}}

La version d'évaluation d'Aspose.PDF fournit toutes les fonctionnalités du produit, mais présente deux limitations :

- Elle insère un filigrane d’évaluation.
- Seuls quatre éléments par collection peuvent être consultés ou modifiés.
- **Un document montrant le filigrane d'évaluation**

{{% alert color="primary" %}}

Si vous souhaitez tester Aspose.PDF for Java sans les limitations de la version d'évaluation, vous pouvez également demander une licence temporaire de 30 jours. Veuillez vous référer à [Comment obtenir une licence temporaire ?](https://purchase.aspose.com/temporary-license)

{{% /alert %}}

## Installer Aspose.PDF for Java depuis le dépôt Aspose

Aspose héberge toutes les API Java sur [Aspose Repository](https://releases.aspose.com/java/repo/com/aspose/aspose-pdf/). Vous pouvez facilement utiliser l'API Aspose.PDF for Java directement dans vos projets Maven avec des configurations simples.

### Spécifier la configuration du dépôt Aspose

Vous devez d’abord spécifier la configuration/l’emplacement du dépôt Aspose dans votre fichier Maven `pom.xml` comme suit :

```xml
 <repositories>
    <repository>
        <id>AsposeJavaAPI</id>
        <name>Aspose Java API</name>
        <url>https://releases.aspose.com/java/repo/</url>
    </repository>
</repositories>
```

### Définir la dépendance Aspose.PDF for Java

Définissez ensuite la dépendance de l'API Aspose.PDF for Java dans votre fichier `pom.xml` comme suit :

```xml
 <dependencies>
    <dependency>
        <groupId>com.aspose</groupId>
        <artifactId>aspose-pdf</artifactId>
        <version>21.7</version>
    </dependency>
</dependencies>
```

Après avoir effectué les étapes ci-dessus, la dépendance Aspose.PDF for Java sera enfin définie dans votre projet Maven.

### Directives de compatibilité et d'utilisation du JDK 11

L'API est optimisée pour l'environnement Java 11 et tous les tests et fonctionnalités fonctionnent correctement. Cependant, pour certaines classes, vous devez ajouter la dépendance externe pour ajouter le chemin de classe de la classe : javax.xml.bind.annotation.adapters.HexBinaryAdapter, qui a été supprimé de JRE.

Par exemple :

```xml
 <dependency>
    <groupId>javax.xml.bind</groupId>
    <artifactId>jaxb-api</artifactId>
    <version>2.3.0</version>
</dependency>
```
