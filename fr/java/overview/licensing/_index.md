---
title: Licence PDF Aspose
linktitle: Licences et limites
type: docs
weight: 50
url: /java/licensing/
description: Aspose.PDF for Python invite ses clients à obtenir une licence Classic. En plus d'utiliser une licence limitée pour mieux explorer le produit.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Licence d'Aspose.PDF pour Java
Abstract: L'article traite des limitations et des options de licence pour Aspose.PDF pour Python. Il souligne que la version d'évaluation permet de tester toutes les fonctionnalités, mais ajoute un filigrane aux PDF générés, indiquant « Évaluation uniquement » ainsi que les informations de droit d'auteur. Pour les utilisateurs souhaitant tester sans ces limitations, une licence temporaire de 30 jours est disponible. L'article explique en outre comment implémenter une licence classique en la chargeant à partir d'un fichier ou d'un flux, en recommandant de placer le fichier de licence dans le même répertoire que le fichier Aspose.PDF.dll et de définir la licence à l'aide de la classe `Aspose.Pdf.License`. Des extraits de code sont fournis pour illustrer le processus de licence.
---
## Limitation d'une version d'évaluation



Nous souhaitons que nos clients testent minutieusement nos composants avant d'acheter afin que la version d'évaluation vous permette de l'utiliser comme vous le feriez normalement.


- 
**PDF créé avec un filigrane d'évaluation.** La version d'évaluation d'Aspose.PDF pour Java fournit toutes les fonctionnalités du produit, mais toutes les pages des documents PDF générés sont filigranées avec "Évaluation uniquement. Créé avec Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" en haut.


- 
**La limite du nombre d'éléments de collection pouvant être traités.**


Dans la version d'évaluation de n'importe quelle collection, vous ne pouvez traiter que quatre éléments (par exemple, seulement 4 pages, 4 champs de formulaire, etc.).

Vous pouvez télécharger une version d'évaluation de **Aspose.PDF** pour Java à partir de [Aspose Repository] (https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). La version d'évaluation offre absolument les mêmes fonctionnalités que la version sous licence du produit. De plus, la version d'évaluation devient simplement sous licence lorsque vous achetez une licence et ajoutez quelques lignes de code pour appliquer la licence.



Une fois que vous êtes satisfait de votre évaluation de **Aspose.PDF**, vous pouvez [acheter une licence] (https://purchase.aspose.com/) sur le site Web d'Aspose. Familiarisez-vous avec les différents types d'abonnements proposés. Si vous avez des questions, n'hésitez pas à contacter l'équipe commerciale Aspose.



Chaque licence Aspose comporte un abonnement d'un an pour des mises à niveau gratuites vers toute nouvelle version ou correctif publié pendant cette période. Le support technique est gratuit et illimité et fourni aux utilisateurs sous licence et en évaluation.



>Si vous souhaitez tester Aspose.PDF pour Java sans les limitations de la version d'évaluation, vous pouvez également demander une licence temporaire de 30 jours. Veuillez vous référer à [Comment obtenir une licence temporaire ?] (https://purchase.aspose.com/temporary-license)


## 
Licence classique

La licence peut être chargée à partir d'un fichier ou d'un objet flux. Le moyen le plus simple de définir une licence consiste à placer le fichier de licence dans le même dossier que le fichier Aspose.PDF.dll et à spécifier le nom du fichier sans chemin, comme indiqué dans l'exemple ci-dessous.



La licence est un fichier XML en texte brut qui contient des détails tels que le nom du produit, le nombre de développeurs auxquels il est concédé sous licence, la date d'expiration de l'abonnement, etc. Le fichier est signé numériquement, ne modifiez donc pas le fichier ; même l'ajout par inadvertance d'un saut de ligne supplémentaire dans le fichier l'invalidera.



Vous devez définir une licence avant d'effectuer toute opération avec des documents. Vous n'êtes tenu de définir une licence qu'une seule fois par application ou processus.



La licence peut être chargée à partir d'un flux ou d'un fichier aux emplacements suivants :


1. 
Chemin explicite.
1. Le dossier qui contient le fichier aspose-pdf-xx.x.jar.



Utilisez la méthode License.setLicense pour obtenir une licence pour le composant. Souvent, le moyen le plus simple de définir une licence consiste à placer le fichier de licence dans le même dossier que Aspose.PDF.jar et à spécifier uniquement le nom du fichier sans chemin, comme indiqué dans l'exemple suivant :


{{% alert color="primary" %}}


À partir d'Aspose.PDF pour Java 4.2.0, vous devez appeler les lignes de code suivantes pour initialiser la licence.


{{% /alert %}}

### 
Charger une licence à partir d'un fichier



Dans cet exemple, **Aspose.PDF** tentera de trouver le fichier de licence dans le dossier contenant les JAR de votre application.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Call setLicense method to set license
license.setLicense("Aspose.Pdf.Java.lic");
```

### Chargement de la licence depuis un objet flux



L'exemple suivant montre comment charger une licence à partir d'un flux.


```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set license from Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

### 
Valider la licence



Il est possible de valider si la licence a été correctement paramétrée ou non. La classe Document possède la méthode isLicensed qui renverra true si la licence a été correctement définie.


```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Check if license has been validated
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```

## 
Licence mesurée

Aspose.PDF permet aux développeurs d'appliquer une clé mesurée. Il s'agit d'un nouveau mécanisme de licence. Le nouveau mécanisme de licence sera utilisé parallèlement à la méthode de licence existante. Les clients qui souhaitent être facturés en fonction de l'utilisation des fonctionnalités de l'API peuvent utiliser la licence limitée. Pour plus de détails, veuillez vous référer à la section [FAQ sur les licences mesurées] (https://purchase.aspose.com/faqs/licensing/metered).



Une nouvelle classe [Metered] (https://reference.aspose.com/pdf/java/com.aspose.pdf/Metered)В a été introduite pour appliquer une clé mesurée. Voici un exemple de code montrant comment définir une clé publique et privée mesurée.


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

## 
Utiliser plusieurs produits d'Aspose



Si vous utilisez plusieurs produits Aspose dans votre application, par exemple Aspose.PDF et Aspose.Words, voici quelques conseils utiles.


- 
**Définissez la licence pour chaque produit Aspose séparément.** Même si vous disposez d'un seul fichier de licence pour tous les composants, par exemple « Aspose.Total.lic », vous devez toujours appeler **License.SetLicense** séparément pour chaque produit Aspose que vous utilisez dans votre application.
- **Utilisez un nom de classe de licence complet.** Chaque produit Aspose possède une classe **Licence** dans son espace de noms. Par exemple, Aspose.PDF a **com.aspose.pdf.License** et Aspose.Words a la classe **com.aspose.words.License**. L'utilisation du nom de classe complet vous permet d'éviter toute confusion quant à la licence appliquée à quel produit.

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
