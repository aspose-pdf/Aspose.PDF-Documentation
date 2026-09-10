---
title: Convertir les formats d'image en PDF en Java
linktitle: Convertir des images en PDF
type: docs
weight: 60
url: /java/convert-images-format-to-pdf/
lastmod: "2026-06-16"
description: Apprenez à convertir BMP, CGM, DICOM, PNG, TIFF, EMF, SVG, CDR et d'autres formats d'image en PDF en Java avec Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Comment convertir des images en PDF en Java
Abstract: Cet article explique comment convertir plusieurs formats d'image en PDF à l'aide d'Aspose.PDF pour Java. Il couvre le placement direct de l'image dans une nouvelle page PDF ainsi que les options de chargement spécifiques au type de fichier pour les entrées CGM, SVG et CDR.
---
Aspose.PDF pour Java peut convertir de nombreux formats d'images raster et vectorielles en documents PDF.


## 
Convertir BMP en PDF



Utilisez cet exemple lorsqu'une image BMP doit être placée dans un document PDF.


1. 
Créez un [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vide pour contenir le PDF de sortie.

1. 
Ajoutez un [`Page`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) et placez le BMP avec `page.addImage(...)`.
1. Définissez le rectangle de l'image cible avec [`Rectangle`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) afin que le contenu raster remplisse la zone de la page PDF.

1. 
Enregistrez le fichier PDF de sortie.


```java
public static void convertBmpToPdf(Path inputFile, Path outputFile) {
        try (Document document = new Document()) {
            try (Page page = document.getPages().add()) {
                page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
            }
            document.save(outputFile.toString());
        }
        System.out.println(inputFile + " converted into " + outputFile);
    }
```

## 
Convertir CGM en PDF



Utilisez cet exemple lorsqu'un fichier graphique CGM doit être converti en PDF.


1. 
Ouvrez la source CGM en passant le chemin du fichier et [`CgmLoadOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) dans le constructeur [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Laissez Aspose.PDF interpréter le flux graphique CGM pendant le chargement du document.

1. 
Enregistrez le PDF converti dans le chemin de sortie cible.


```java
public static void convertCgmToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CgmLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir DICOM en PDF



Utilisez cet exemple lorsqu’une image médicale DICOM doit être enveloppée dans un document PDF.


1. 
Créez un [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vide pour la sortie PDF.
1. Créez un objet [`Image`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/image/), définissez son [`ImageFileType`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/imagefiletype/) sur `Dicom` et attribuez le chemin du fichier source.

1. 
Ajoutez un [`Page`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) et ajoutez l'image DICOM à la collection de paragraphes de page.

1. 
Enregistrez le résultat au format PDF.


```java
public static void convertDicomToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        Image image = new Image();
        image.setFileType(ImageFileType.Dicom);
        image.setFile(inputFile.toString());

        try (Page page = document.getPages().add()) {
            page.getParagraphs().add(image);
        }

        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertissez EMF en PDF avec chargement direct de documents



Utilisez cet exemple lorsqu'un fichier EMF doit être converti en PDF via le chemin de chargement EMF principal.

1. Créez un [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vide et ouvrez la source EMF sous forme de flux binaire.

1. 
Ajoutez un [`Page`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) et effacez ses marges afin que l'illustration EMF puisse occuper toute la zone de la page.

1. 
Créez un [`Image`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/image/), liez-y le flux EMF et ajoutez-le à la collection de paragraphes de page.

1. 
Enregistrez le fichier PDF de sortie.


```java
public static void convertEmfToPdf01(Path inputFile, Path outputFile) throws IOException {
    try (Document document = new Document();
         FileInputStream imageStream = new FileInputStream(inputFile.toFile())) {
        try (Page page = document.getPages().add()) {
            page.getPageInfo().getMargin().setBottom(0);
            page.getPageInfo().getMargin().setTop(0);
            page.getPageInfo().getMargin().setLeft(0);
            page.getPageInfo().getMargin().setRight(0);

            Image image = new Image();
            image.setFileType(ImageFileType.Unknown);
            image.setImageStream(imageStream);
            page.getParagraphs().add(image);
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertissez EMF en PDF avec un flux de travail alternatif

Utilisez cet exemple lorsque le contenu EMF doit être converti à l’aide d’une configuration alternative ou d’un flux de composition de page.


1. 
Chargez la source EMF avec Aspose.Imaging et restituez-la dans un flux PNG en mémoire avant le placement du PDF.

1. 
Créez un [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vide et ajoutez un [`Page`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Créez un [`Image`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) à partir du flux d'octets intermédiaire et ajoutez-le à la page.

1. 
Enregistrez le PDF converti.

```java
public static void convertEmfToPdf02(Path inputFile, Path outputFile) throws IOException {
    try (Document document = new Document();
         com.aspose.imaging.Image emfImage = com.aspose.imaging.Image.load(inputFile.toString());
         ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream()) {
        emfImage.save(byteArrayOutputStream, new PngOptions());

        try (Page page = document.getPages().add()) {
            Image image = new Image();
            image.setImageStream(new ByteArrayInputStream(byteArrayOutputStream.toByteArray()));
            page.getParagraphs().add(image);
        }

        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir GIF en PDF



Utilisez cet exemple lorsqu'une image GIF doit être ajoutée à une page PDF.


1. 
Créez un [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vide pour la sortie PDF.

1. 
Ajoutez un [`Page`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) et placez le GIF avec `page.addImage(...)`.

1. 
Définissez les limites de placement avec [`Rectangle`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) afin que l'image remplisse la zone de la page.
1. Enregistrez le PDF de sortie.


```java
public static void convertGifToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir JPEG en PDF



Utilisez cet exemple lorsqu'une image JPEG doit être convertie en PDF d'une page.


1. 
Créez un [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vide pour le PDF de sortie.

1. 
Ajoutez un [`Page`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) et insérez l'image JPEG avec `page.addImage(...)`.
1. Utilisez [`Rectangle`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) pour contrôler la manière dont l'image raster est mappée aux coordonnées de la page.

1. 
Enregistrez le fichier PDF généré.


```java
public static void convertJpegToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir PNG en PDF



Utilisez cet exemple lorsqu'une image PNG doit être enveloppée dans un document PDF.


1. 
Créez un [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vide pour la sortie de conversion.
1. Ajoutez un [`Page`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) et placez l'image PNG dessus avec `page.addImage(...)`.

1. 
Utilisez [`Rectangle`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) pour redimensionner l'image par rapport au canevas de la page.

1. 
Enregistrez le fichier de sortie.


```java
public static void convertPngToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir SVG en PDF



Utilisez cet exemple lorsqu'une illustration SVG doit être rendue dans un document PDF.

1. Ouvrez la source SVG en passant le chemin du fichier et [`SvgLoadOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions/) dans le constructeur [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Laissez Aspose.PDF analyser le balisage SVG et créer le modèle graphique PDF correspondant pendant le chargement.

1. 
Enregistrez la sortie PDF dans le chemin du fichier cible.


```java
public static void convertSvgToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new SvgLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir TIFF en PDF



Utilisez cet exemple lorsqu'une image TIFF doit être convertie en PDF.

1. Créez un [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vide pour la sortie PDF.

1. 
Ajoutez un [`Page`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) et placez l'image TIFF avec `page.addImage(...)`.

1. 
Définissez la zone de placement avec [`Rectangle`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) afin que le contenu TIFF soit mappé aux coordonnées de la page.

1. 
Enregistrez le résultat au format PDF.


```java
public static void convertTiffToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir CDR en PDF

Utilisez cet exemple lorsqu'un fichier CorelDRAW CDR doit être converti en PDF.


1. 
Ouvrez la source CDR en passant le chemin du fichier et [`CdrLoadOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/cdrloadoptions/) dans le constructeur [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Laissez Aspose.PDF charger le contenu CorelDRAW dans le modèle de document PDF.

1. 
Enregistrez le fichier PDF converti dans le chemin de sortie demandé.

```java
public static void convertCdrToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CdrLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
