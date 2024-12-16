---
title: Ajouter un tampon de texte et d'image
type: docs
weight: 20
url: /fr/java/add-text-and-image-stamp/
description: Cette section explique comment ajouter un tampon de texte et d'image avec com.aspose.pdf.facades en utilisant la classe PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Ajouter un tampon de texte sur toutes les pages d'un fichier PDF

La classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) vous permet d'ajouter un tampon de texte sur toutes les pages d'un fichier PDF.
 In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) and [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes.

Afin d'ajouter un tampon de texte, vous devez d'abord créer des objets des classes [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) et [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Vous devez également créer le tampon de texte en utilisant la méthode BindLogo de la classe [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Vous pouvez définir d'autres attributs tels que l'origine, la rotation, l'arrière-plan, etc., en utilisant également l'objet [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Ensuite, vous pouvez ajouter le tampon dans le fichier PDF en utilisant la méthode [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Le code suivant vous montre comment ajouter un tampon de texte sur toutes les pages d'un fichier PDF.

```java
 public static void AddTextStampOnAllPagesInPdfFile() {
        // Créer un objet PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Ouvrir le document
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Créer un tampon
        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("Hello World!", java.awt.Color.BLUE, java.awt.Color.GRAY, FontStyle.Helvetica,
                EncodingType.Winansi, true, 14));
        stamp.setOrigin(10, 400);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // Ajouter le tampon au fichier PDF
        fileStamp.addStamp(stamp);

        // Enregistrer le fichier PDF mis à jour
        fileStamp.save(_dataDir + "AddTextStamp-All_out.pdf");

        // Fermer fileStamp
        fileStamp.close();
    }
```

## Ajouter un tampon de texte sur des pages particulières dans un fichier PDF

La classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) permet d'ajouter un tampon de texte sur des pages particulières d'un fichier PDF.
 In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp)and [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes.

Afin d'ajouter un tampon de texte, vous devez d'abord créer des objets des classes [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) et [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). You also need to create the text stamp using [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) method of [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) class.

Vous devez également créer le tampon de texte en utilisant la méthode [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) de la classe [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). You can set other attributes like origin, rotation, background etc.  
Vous pouvez définir d'autres attributs tels que l'origine, la rotation, l'arrière-plan, etc. using [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) objet également. Comme vous souhaitez ajouter un tampon de texte sur des pages particulières du fichier PDF, vous devez également définir la propriété [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) de la classe [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Cette propriété nécessite un tableau d'entiers contenant les numéros des pages sur lesquelles vous souhaitez ajouter le tampon. Ensuite, vous pouvez ajouter le tampon dans le fichier PDF en utilisant la méthode [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Le fragment de code suivant vous montre comment ajouter un tampon de texte sur des pages particulières dans un fichier PDF.

```java
 public static void AddTextStampOnParticularPagesInPdfFile() {
        // Créer un objet PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Ouvrir le document
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Créer le tampon
        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("Hello World!", java.awt.Color.BLUE, java.awt.Color.GRAY, FontStyle.Helvetica,
                EncodingType.Winansi, true, 14));
        stamp.setOrigin(10, 400);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // Définir des pages particulières
        stamp.setPages(new int[] { 2 });

        // Ajouter le tampon au fichier PDF
        fileStamp.addStamp(stamp);

        // Enregistrer le fichier PDF mis à jour
        fileStamp.save(_dataDir + "AddTextStamp-Page_out.pdf");

        // Fermer fileStamp
        fileStamp.close();
    }
```

## Ajouter un tampon d'image sur toutes les pages d'un fichier PDF

La classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) vous permet d'ajouter un tampon d'image sur toutes les pages d'un fichier PDF.
 In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) and [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes.

Pour ajouter un tampon d'image, vous devez d'abord créer des objets des classes [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) et [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Vous devez également créer le tampon d'image en utilisant la méthode [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) de la classe [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Vous pouvez définir d'autres attributs comme l'origine, la rotation, l'arrière-plan, etc. en utilisant également l'objet [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Ensuite, vous pouvez ajouter le tampon dans le fichier PDF en utilisant la méthode [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Le code suivant vous montre comment ajouter un tampon d'image sur toutes les pages d'un fichier PDF.

```java
public static void AddImageStampOnParticularPagesInPdfFile() {
        // Créer un objet PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Ouvrir le document
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Créer un tampon
        Stamp stamp = new Stamp();
        stamp.bindImage(_dataDir + "aspose-logo.png");
        stamp.setOrigin(10, 200);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // Ajouter le tampon au fichier PDF
        fileStamp.addStamp(stamp);

        // Enregistrer le fichier PDF mis à jour
        fileStamp.save(_dataDir + "AddImageStamp-All_out.pdf");

        // Fermer fileStamp
        fileStamp.close();
    }
```

### Contrôler la qualité de l'image lors de l'ajout en tant que tampon

Lors de l'ajout d'une image en tant qu'objet tampon, vous pouvez également contrôler la qualité de l'image. Afin de répondre à cette exigence, la propriété Quality est ajoutée à la classe [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Elle indique la qualité de l'image en pourcentages (les valeurs valides sont de 0 à 100).

## Ajouter un tampon d'image sur des pages particulières dans un fichier PDF

La classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) vous permet d'ajouter un tampon d'image sur des pages particulières d'un fichier PDF.
 In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) and [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes.

Afin d'ajouter un tampon d'image, vous devez d'abord créer des objets des classes [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) et [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). You also need to create the image stamp using [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) méthode de la classe [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). You can set other attributes like origin, rotation, background etc.

Vous pouvez définir d'autres attributs tels que l'origine, la rotation, l'arrière-plan, etc. using [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) objet également. Comme vous souhaitez ajouter un tampon d'image sur des pages spécifiques du fichier PDF, vous devez également définir la propriété [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) de la classe [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Cette propriété nécessite un tableau d'entiers contenant les numéros des pages sur lesquelles vous souhaitez ajouter le tampon. Ensuite, vous pouvez ajouter le tampon dans le fichier PDF en utilisant la méthode [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Enfin, enregistrez le fichier PDF de sortie en utilisant la méthode [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) de la classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Le code suivant vous montre comment ajouter un tampon d'image sur des pages spécifiques dans un fichier PDF.

```java
  public static void AddImageStampOnAllPagesInPdfFile() {
        // Créer un objet PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Ouvrir le document
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Créer le tampon
        Stamp stamp = new Stamp();
        stamp.bindImage(_dataDir + "aspose-logo.png");
        stamp.setOrigin(10, 200);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // Définir les pages spécifiques
        stamp.setPages(new int[] { 2 });

        // Ajouter le tampon au fichier PDF
        fileStamp.addStamp(stamp);

        // Enregistrer le fichier PDF mis à jour
        fileStamp.save(_dataDir + "AddImageStamp-Page_out.pdf");

        // Fermer fileStamp
        fileStamp.close();
    }
```