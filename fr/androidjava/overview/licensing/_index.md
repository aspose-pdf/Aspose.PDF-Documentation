---
title: Licence et limitations
linktitle: Licence et limitations
type: docs
weight: 50
url: /fr/androidjava/licensing/
description: Aspose.PDF for Android via Java invite ses clients à obtenir une Classic license et une Metered License. Ainsi que d’utiliser une limited license pour mieux explorer le produit.
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Limitation d’une version d’évaluation

Nous voulons que nos clients testent nos composants de manière approfondie avant d’acheter, c’est pourquoi la version d’évaluation vous permet de l’utiliser comme vous le feriez normalement.

- **PDF créé avec un filigrane d'évaluation.** La version d'évaluation d'Aspose.PDF pour Android via Java offre toutes les fonctionnalités du produit, mais toutes les pages des documents PDF générés sont marquées d'un filigrane "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" en haut.

- **Limite du nombre d'éléments de collection pouvant être traités.**
Dans la version d'évaluation, à partir de n'importe quelle collection, vous ne pouvez traiter que quatre éléments (par exemple, seulement 4 pages, 4 champs de formulaire, etc.).

Vous pouvez télécharger une version d'évaluation d'Aspose.PDF pour Android via Java depuis [Référentiel Aspose](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). La version d'évaluation offre absolument les mêmes capacités que la version sous licence du produit. De plus, la version d'évaluation devient simplement sous licence lorsque vous achetez une licence et ajoutez quelques lignes de code pour appliquer la licence.

Une fois que vous êtes satisfait de votre évaluation de **Aspose.PDF**, vous pouvez [acheter une licence](https://purchase.aspose.com/) sur le site Web d'Aspose. Familiarisez‑vous avec les différents types d'abonnement proposés. Si vous avez des questions, n'hésitez pas à contacter l'équipe commerciale d'Aspose.

Chaque licence Aspose comprend un abonnement d'un an pour des mises à jour gratuites vers toutes les nouvelles versions ou correctifs publiés pendant cette période. Le support technique est gratuit, illimité et fourni tant aux utilisateurs sous licence qu'aux utilisateurs en version d'évaluation.

>Si vous souhaitez tester Aspose.PDF pour Android via Java sans les limitations de la version d'évaluation, vous pouvez également demander une licence temporaire de 30 jours. Veuillez vous référer à [Comment obtenir une licence temporaire ?](https://purchase.aspose.com/temporary-license)

## Licence classique

La licence peut être chargée à partir d'un fichier ou d'un objet flux. Le moyen le plus simple de définir une licence consiste à placer le fichier de licence dans le même dossier que le fichier Aspose.PDF.dll et à spécifier le nom du fichier sans chemin, comme indiqué dans l'exemple ci-dessous.

La licence est un fichier XML en texte brut qui contient des détails tels que le nom du produit, le nombre de développeurs pour lesquels elle est concédée, la date d'expiration de l'abonnement, etc. Le fichier est signé numériquement, ne le modifiez donc pas ; même l'ajout accidentel d'un saut de ligne supplémentaire dans le fichier l'invalidera.

Vous devez définir une licence avant d'effectuer toute opération avec des documents. Vous n'êtes tenu de définir une licence qu'une seule fois par application ou processus.

La licence peut être chargée à partir d'un flux ou d'un fichier aux emplacements suivants :

1. Chemin explicite.
1. Le dossier qui contient le aspose-pdf-xx.x.jar.

Utilisez la méthode License.setLicense pour licencier le composant. Souvent, la façon la plus simple de définir une licence consiste à placer le fichier de licence dans le même dossier que Aspose.PDF.jar et à spécifier uniquement le nom du fichier sans le chemin, comme illustré dans l'exemple suivant :

{{% alert color="primary" %}}

À partir d'Aspose.PDF for Java 4.2.0, vous devez appeler les lignes de code suivantes pour initialiser la licence.

{{% /alert %}}

### Chargement d'une licence à partir d'un fichier

Dans cet exemple **Aspose.PDF** tentera de trouver le fichier de licence dans le dossier qui contient les JAR de votre application.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Call setLicense method to set license
license.setLicense("Aspose.Pdf.Java.lic");
```

### Chargement de la licence à partir d'un objet flux

L'exemple suivant montre comment charger une licence à partir d'un flux.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set license from Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

#### Définition d'une licence achetée avant le 22/01/2005

**Aspose.PDF** pour Java ne prend plus en charge les anciennes licences, donc veuillez contacter notre [équipe de vente](https://company.aspose.com/contact) pour obtenir un nouveau fichier de licence.

### Valider la licence

Il est possible de vérifier si la licence a été correctement définie ou non. La classe Document possède la méthode isLicensed qui renverra true si la licence a été correctement définie.

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Check if license has been validated
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```
## Licence à l'usage

Aspose.PDF permet aux développeurs d’appliquer une clé à comptage. C’est un nouveau mécanisme de licence. Le nouveau mécanisme de licence sera utilisé en parallèle avec la méthode de licence existante. Les clients qui souhaitent être facturés en fonction de l’utilisation des fonctionnalités de l’API peuvent utiliser la licence à comptage. Pour plus de détails, veuillez vous référer à [FAQ sur la licence à la consommation](https://purchase.aspose.com/faqs/licensing/metered) section.

```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// Optionally, the following two lines returns true if a valid license has been applied;
// false if the component is running in evaluation mode.
License lic = new License();
System.out.println("License is set = " + lic.isLicensed());
```
## Utilisation de plusieurs produits Aspose

Si vous utilisez plusieurs produits Aspose dans votre application, par exemple Aspose.PDF et Aspose.Words, voici quelques conseils utiles.

- **Définissez la licence pour chaque produit Aspose séparément.** Même si vous avez un seul fichier de licence pour tous les composants, par exemple 'Aspose.Total.lic', vous devez toujours appeler **License.SetLicense** séparément pour chaque produit Aspose que vous utilisez dans votre application.
- **Utilisez le nom complet de la classe de licence.** Chaque produit Aspose possède une classe **License** dans son espace de noms. Par exemple, Aspose.PDF possède la classe **com.aspose.pdf.License** et Aspose.Words possède la classe **com.aspose.words.License**. Utiliser le nom complet de la classe permet d'éviter toute confusion sur la licence appliquée à chaque produit.

```java
// Instantiate the License class of Aspose.Pdf
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set the license
license.setLicense("Aspose.Total.Java.lic");

// Setting license for Aspose.Words for Java

// Instantiate the License class of Aspose.Words
com.aspose.words.License licenseaw = new com.aspose.words.License();
// Set the license
licenseaw.setLicense("Aspose.Total.Java.lic");
```
