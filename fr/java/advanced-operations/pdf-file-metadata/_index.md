---
title: Travailler avec les Métadonnées de Fichier PDF 
linktitle: Métadonnées de Fichier PDF
type: docs
weight: 140
url: fr/java/pdf-file-metadata/
description: Cette section explique comment obtenir des informations sur les fichiers PDF, comment obtenir les métadonnées XMP d'un fichier PDF, définir les informations du fichier PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtenir des Informations sur le Fichier PDF

Pour obtenir des informations spécifiques à un fichier sur un fichier PDF, d'abord, obtenez l'objet [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo) en utilisant la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)  [getInfo()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getInfo--). Une fois l'objet [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo) récupéré, vous pouvez obtenir les valeurs des propriétés individuelles.

Le fragment de code suivant montre comment définir les informations du fichier PDF.

```java
public class ExampleMetadata {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Metadata/";

    public static void GetPDFFileInformation() {
        // Créez un nouveau document PDF
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
        // Obtenez les informations du document
        DocumentInfo docInfo = pdfDocument.getInfo();
        // Afficher les informations du document
        System.out.println("Auteur: " + docInfo.getAuthor());
        System.out.println("Date de Création: " + docInfo.getCreationDate());
        System.out.println("Mots-clés: " + docInfo.getKeywords());
        System.out.println("Date de Modification: " + docInfo.getModDate());
        System.out.println("Sujet: " + docInfo.getSubject());
        System.out.println("Titre: " + docInfo.getTitle());
    }
```


## Définir les Informations du Fichier PDF

Aspose.PDF pour Java vous permet de définir des informations spécifiques au fichier pour un PDF, telles que l'auteur, la date de création, le sujet et le titre.

Pour définir ces informations :

1. Créez un objet [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo).
2. Définissez les valeurs des propriétés.
3. Enregistrez le document mis à jour en utilisant la méthode [save()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save-com.aspose.ms.System.IO.FileStream-) de la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

{{% alert color="primary" %}}

Veuillez noter que vous ne pouvez pas définir de valeurs pour les champs **Producer** et **Creator**, car Aspose.PDF pour Java x.x.x sera affiché pour ces champs.

{{% /alert %}}

Le code suivant montre comment définir les informations du fichier PDF.

```java
 public static void SetPDFFileInformation() {
        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // Spécifier les informations du document
        DocumentInfo docInfo = new DocumentInfo(pdfDocument);

        docInfo.setAuthor("Aspose");
        docInfo.setCreationDate(new java.util.Date());
        docInfo.setKeywords("Aspose.Pdf, DOM, API");
        docInfo.setModDate(new java.util.Date());
        docInfo.setSubject("Informations PDF");
        docInfo.setTitle("Définir les Informations du Document PDF");

        // Enregistrer le document de sortie
        pdfDocument.save(_dataDir + "SetFileInfo_out.pdf");
    }
```


## Obtenir les métadonnées XMP d'un fichier PDF

Aspose.PDF pour Java vous permet d'accéder aux métadonnées XMP d'un fichier PDF.

Pour obtenir les métadonnées d'un fichier PDF,

1. Créez un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) et ouvrez le fichier PDF d'entrée.
1. Utilisez la propriété [getMetadata()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getMetadata--) pour obtenir les métadonnées.

Le code suivant vous montre comment obtenir les métadonnées du fichier PDF.

```java
   public static void GetXMPMetadata() {

        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "SetXMPMetadata.pdf");

        System.out.println("xmp:CreateDate: " + pdfDocument.getMetadata().get_Item("xmp:CreateDate"));
        System.out.println("xmp:Nickname: " + pdfDocument.getMetadata().get_Item("xmp:Nickname"));
        System.out.println("xmp:CustomProperty: " + pdfDocument.getMetadata().get_Item("xmp:CustomProperty"));

    }
```

## Définir les métadonnées XMP dans un fichier PDF

Aspose.PDF pour Java vous permet de définir des métadonnées dans un fichier PDF.
 Pour définir les métadonnées :

1. Créez un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Définissez les valeurs des métadonnées en utilisant la propriété [getMetadata()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getMetadata--).
1. Enregistrez le document mis à jour en utilisant la méthode [save()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save-com.aspose.ms.System.IO.FileStream-) de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Le snippet de code suivant vous montre comment définir les métadonnées dans un fichier PDF.

```java
    public static void SetXMPMetadata() {

        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // Définir les propriétés
        pdfDocument.getMetadata().set_Item("xmp:CreateDate", new XmpValue(new java.util.Date()));
        pdfDocument.getMetadata().set_Item("xmp:Nickname", new XmpValue("Nickname"));
        pdfDocument.getMetadata().set_Item("xmp:CustomProperty", new XmpValue("Custom Value"));

        // Enregistrer le document
        pdfDocument.save(_dataDir + "SetXMPMetadata.pdf");
    }
```

## Insérer des Métadonnées avec Préfixe

Certains développeurs ont besoin de créer un nouvel espace de noms de métadonnées avec un préfixe. L'extrait de code suivant montre comment insérer des métadonnées avec un préfixe.

```java
    public static void InsertMetadataWithPrefix() {
        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "SetXMPMetadata.pdf");
        pdfDocument.getMetadata().registerNamespaceUri("adc", "http://tempuri.org/adc/1.0");
        pdfDocument.getMetadata().set_Item("adc:format", new XmpValue("application/pdf"));
        pdfDocument.getMetadata().set_Item("adc:title", new XmpValue("alternative title"));        
        // Enregistrer le document
        pdfDocument.save(_dataDir + "SetPrefixMetadata_out.pdf");
    }
}
```