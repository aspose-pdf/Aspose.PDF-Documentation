---
title: Licensing and limitations
linktitle: Licensing and limitations
type: docs
weight: 90
url: /php-java/licensing/
description: Aspose.PDF pour PHP via Java invite ses clients à obtenir une licence classique et une licence comptée. Ainsi qu'à utiliser une licence limitée pour mieux explorer le produit.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Limitation d'une version d'évaluation

Nous souhaitons que nos clients testent nos composants de manière approfondie avant d'acheter, donc la version d'évaluation vous permet de l'utiliser comme vous le feriez normalement.

- **PDF créé avec un filigrane d'évaluation.** La version d'évaluation d'Aspose.PDF pour PHP via Java offre toutes les fonctionnalités du produit, mais toutes les pages des documents PDF générés sont marquées d'un filigrane "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" en haut.

- **La limite du nombre d'éléments de collection qui peuvent être traités.**

Dans la version d'évaluation, à partir de n'importe quelle collection, vous pouvez traiter uniquement quatre éléments (par exemple, seulement 4 pages, 4 champs de formulaire, etc.).

You can download an evaluation version of **Aspose.PDF** pour Java depuis [Aspose Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). La version d'évaluation offre exactement les mêmes capacités que la version sous licence du produit. De plus, la version d'évaluation devient simplement sous licence lorsque vous achetez une licence et ajoutez quelques lignes de code pour appliquer la licence.

Une fois que vous êtes satisfait de votre évaluation de **Aspose.PDF**, vous pouvez [acheter une licence](https://purchase.aspose.com/) sur le site Web d'Aspose. Familiarisez-vous avec les différents types d'abonnements proposés. Si vous avez des questions, n'hésitez pas à contacter l'équipe de vente d'Aspose.

Chaque licence Aspose comprend un abonnement d'un an pour des mises à jour gratuites vers toute nouvelle version ou correctif publié pendant cette période. Le support technique est gratuit et illimité et est fourni aussi bien aux utilisateurs sous licence qu'aux utilisateurs en évaluation.

>Si vous souhaitez tester Aspose.PDF pour PHP via Java sans les limitations de la version d'évaluation, vous pouvez également demander une licence temporaire de 30 jours.
 Veuillez vous référer à [Comment obtenir une licence temporaire ?](https://purchase.aspose.com/temporary-license)

## Licence classique

La licence peut être chargée à partir d'un fichier ou d'un objet flux. La manière la plus simple de définir une licence est de placer le fichier de licence dans le même dossier que le fichier Aspose.PDF.dll et de spécifier le nom de fichier sans chemin, comme indiqué dans l'exemple ci-dessous.

La licence est un fichier XML en texte clair qui contient des détails tels que le nom du produit, le nombre de développeurs auquel elle est attribuée, la date d'expiration de l'abonnement, etc. Le fichier est signé numériquement, donc ne modifiez pas le fichier ; même l'ajout involontaire d'un saut de ligne supplémentaire dans le fichier l'invalidera.

Vous devez définir une licence avant d'effectuer toute opération avec des documents. Vous n'êtes tenu de définir une licence qu'une seule fois par application ou processus.

La licence peut être chargée à partir d'un flux ou d'un fichier dans les emplacements suivants :

1. Chemin explicite.
1. Le dossier qui contient aspose-pdf-xx.x.jar.

Utilisez la méthode License.setLicense pour licencier le composant. Souvent, le moyen le plus simple de définir une licence est de placer le fichier de licence dans le même dossier que Aspose.PDF.jar et de spécifier simplement le nom du fichier sans chemin, comme indiqué dans l'exemple suivant :

{{% alert color="primary" %}}

À partir de Aspose.PDF pour PHP via Java 4.2.0, vous devez appeler les lignes de code suivantes pour initialiser la licence.

{{% /alert %}}

### Chargement d'une licence à partir d'un fichier

Dans cet exemple, **Aspose.PDF** tentera de trouver le fichier de licence dans le dossier contenant les JARs de votre application.

```java
// Initialiser l'instance de licence
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Appeler la méthode setLicense pour définir la licence
license.setLicense("Aspose.Pdf.Java.lic");
```
### Chargement de la licence à partir d'un objet flux

L'exemple suivant montre comment charger une licence à partir d'un flux.

```java
// Initialiser l'instance de licence
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Définir la licence à partir du flux
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

#### Définir une licence achetée avant le 2005/01/22**Aspose.PDF** pour Java ne prend plus en charge les anciennes licences, veuillez donc contacter notre [équipe commerciale](https://company.aspose.com/contact) pour obtenir un nouveau fichier de licence.

### Valider la Licence

Il est possible de valider si la licence a été correctement définie ou non. La classe Document possède la méthode isLicensed qui retournera vrai si la licence a été correctement définie.

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Vérifiez si la licence a été validée
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```
## Licence Mesurée

Aspose.PDF permet aux développeurs d'appliquer une clé mesurée. C'est un nouveau mécanisme de licence. Le nouveau mécanisme de licence sera utilisé en parallèle avec la méthode de licence existante. Les clients qui souhaitent être facturés en fonction de l'utilisation des fonctionnalités de l'API peuvent utiliser la licence mesurée. Pour plus de détails, veuillez vous référer à la section [FAQ sur les licences mesurées](https://purchase.aspose.com/faqs/licensing/metered).

Une nouvelle classe [Metered](https://reference.aspose.com/pdf/java/com.aspose.pdf/Metered) a été introduite pour appliquer la clé mesurée.
 Voici le code exemple démontrant comment définir une clé publique et privée mesurée.

```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// Optionnellement, les deux lignes suivantes renvoient vrai si une licence valide a été appliquée ;
// faux si le composant fonctionne en mode évaluation.
License lic = new License();
System.out.println("License is set = " + lic.isLicensed());
```
## Utilisation de plusieurs produits Aspose

Si vous utilisez plusieurs produits Aspose dans votre application, par exemple Aspose.PDF et Aspose.Words, voici quelques conseils utiles.

- **Définissez la licence pour chaque produit Aspose séparément.** Même si vous avez un seul fichier de licence pour tous les composants, par exemple 'Aspose.Total.lic', vous devez tout de même appeler **License.SetLicense** séparément pour chaque produit Aspose que vous utilisez dans votre application.
- **Utilisez le nom de classe de licence entièrement qualifié.** Chaque produit Aspose a une classe **License** dans son espace de noms. Par exemple, Aspose.PDF a la classe **com.aspose.pdf.License** et Aspose.Words a la classe **com.aspose.words.License**. Utiliser le nom de classe entièrement qualifié vous permet d'éviter toute confusion sur la licence appliquée à quel produit.

```java
// Instancier la classe License d'Aspose.Pdf
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Définir la licence
license.setLicense("Aspose.Total.Java.lic");

// Définir la licence pour Aspose.Words pour Java

// Instancier la classe License d'Aspose.Words
com.aspose.words.License licenseaw = new com.aspose.words.License();
// Définir la licence
licenseaw.setLicense("Aspose.Total.Java.lic");
```