---
title: Définir les informations du fichier PDF - façades
type: docs
weight: 20
url: /fr/java/set-pdf-information/
description: Cette section explique comment définir les informations du fichier PDF avec Aspose.PDF Facades en utilisant la classe PdfFileInfo.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

La classe [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) vous permet de définir des informations spécifiques au fichier d'un document PDF. Vous devez créer un objet de la classe [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) puis définir différentes propriétés spécifiques au fichier telles que l'Auteur, le Titre, les Mots-clés et le Créateur, etc. Enfin, enregistrez le fichier PDF mis à jour en utilisant la méthode [saveNewInfo(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#saveNewInfo-java.io.OutputStream-) de l'objet [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo).

Le fragment de code suivant montre comment définir les informations du fichier PDF.

```java
 public static void SetPdfInfo()
    {
        PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
        // Définir les informations du PDF
        fileInfo.setAuthor("Aspose");
        fileInfo.setTitle ("Bonjour le monde!");
        fileInfo.setKeywords("Paix et Développement");
        fileInfo.setCreator ("Aspose");
        
        // Enregistrer le fichier mis à jour
        fileInfo.saveNewInfo(_dataDir + "SetfileInfo_out.pdf");
    }
```


## Définir les Informations Méta

La méthode [setMetaInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#setMetaInfo-java.lang.String-java.lang.String-) vous permet d'ajouter des informations. Dans notre exemple, nous avons ajouté un champ. Consultez le prochain extrait de code :

```java
   public static void SetMetaInfo()
    {
        // Créer une instance de l'objet PdffileInfo
        PdfFileInfo fInfo = new PdfFileInfo(_dataDir + "sample.pdf");
       
        // Définir un nouvel attribut client comme info méta
        fInfo.setMetaInfo("Reviewer", "Aspose.PDF user");

        // Enregistrer le fichier mis à jour
        fInfo.saveNewInfo(_dataDir + "SetMetaInfo_out.pdf");

    }
```