---
title: Gérer l'en-tête et le pied de page
type: docs
weight: 40
url: fr/java/manage-header-and-footer/
description: Cette section explique comment gérer l'en-tête et le pied de page avec Aspose.PDF Facades en utilisant la classe PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Ajouter un en-tête dans un fichier PDF

La classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) permet d'ajouter un en-tête dans un fichier PDF.
 In order to add header, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class.

Afin d'ajouter un en-tête, vous devez d'abord créer un objet de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Vous pouvez formater le texte de l'en-tête en utilisant la classe [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText). Une fois que vous êtes prêt à ajouter un en-tête dans le fichier, vous devez appeler la méthode [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Vous devez également spécifier au moins la marge supérieure dans la méthode [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Le snippet de code suivant vous montre comment ajouter un en-tête dans un fichier PDF.

```java
 public static void AddHeader() {
        // Créer un objet PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Ouvrir le document
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Créer un texte formaté pour le numéro de page
        FormattedText formattedText = new FormattedText("Aspose - Vos experts en formats de fichiers!", java.awt.Color.YELLOW,
                java.awt.Color.BLACK, FontStyle.Courier, EncodingType.Winansi, false, 14);

        // Ajouter l'en-tête
        fileStamp.addHeader(formattedText, 20);

        // Enregistrer le fichier PDF mis à jour
        fileStamp.save(_dataDir + "AddHeader_out.pdf");

        // Fermer fileStamp
        fileStamp.close();
    }
```

## Ajouter un Pied de Page dans un Fichier PDF

La classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) vous permet d'ajouter un pied de page dans un fichier PDF.
 In order to add footer, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class.

Pour ajouter un pied de page, vous devez d'abord créer un objet de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Vous pouvez formater le texte du pied de page en utilisant la classe [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText). Une fois que vous êtes prêt à ajouter un pied de page dans le fichier, vous devez appeler la méthode [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Vous devez également spécifier au moins la marge inférieure dans la méthode [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Le code d'exemple suivant vous montre comment ajouter un pied de page dans un fichier PDF.

```java
 public static void AddFooter() {
        // Créer un objet PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Ouvrir le document
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Créer un texte formaté pour le numéro de page
        FormattedText formattedText = new FormattedText("Aspose - Vos experts en formats de fichiers!", java.awt.Color.BLUE,
                java.awt.Color.GRAY, FontStyle.Courier, EncodingType.Winansi, false, 14);

        // Ajouter le pied de page
        fileStamp.addFooter(formattedText, 10);

        // Enregistrer le fichier PDF mis à jour
        fileStamp.save(_dataDir + "AddFooter_out.pdf");

        // Fermer fileStamp
        fileStamp.close();
    }
```

## Ajouter une Image dans l'En-tête d'un Fichier PDF Existant

La classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) permet d'ajouter une image dans l'en-tête d'un fichier PDF.
 Afin d'ajouter une image dans l'en-tête, vous devez d'abord créer un objet de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Ensuite, vous devez appeler la méthode [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Vous pouvez passer l'image à la méthode [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Le snippet de code suivant vous montre comment ajouter une image dans l'en-tête d'un fichier PDF.

```java
public static void AddImageHeader() {
        // Créer un objet PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Ouvrir le document
        fileStamp.bindPdf(_dataDir + "sample.pdf");
        FileInputStream fs;
        try {
            fs = new FileInputStream(_dataDir + "aspose-logo.png");
            // Ajouter l'en-tête
            fileStamp.addHeader(fs, 10);

            // Enregistrer le fichier PDF mis à jour
            fileStamp.save(_dataDir + "AddImage-Header_out.pdf");
        } catch (FileNotFoundException e) {

            e.printStackTrace();
        }

        // Fermer fileStamp
        fileStamp.close();
    }
```

## Ajouter une Image dans le Pied de Page d'un Fichier PDF Existant

La classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) vous permet d'ajouter une image dans le pied de page d'un fichier PDF.
 Afin d'ajouter une image dans le pied de page, vous devez d'abord créer un objet de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Après cela, vous devez appeler la méthode [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Vous pouvez passer l'image à la méthode [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Le code suivant vous montre comment ajouter une image dans le pied de page d'un fichier PDF.

```java
    public static void AddImageFooter() {
        // Créer un objet PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Ouvrir le document
        fileStamp.bindPdf(_dataDir + "sample.pdf");
        FileInputStream fs;
        try {
            fs = new FileInputStream(_dataDir + "aspose-logo.png");
            // Ajouter un pied de page
            fileStamp.addFooter(fs, 10);

            // Enregistrer le fichier PDF mis à jour
            fileStamp.save(_dataDir + "AddImage-Footer_out.pdf");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        // Fermer fileStamp
        fileStamp.close();
    }
```