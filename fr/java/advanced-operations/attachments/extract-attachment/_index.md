---
title: Extraire les pièces jointes d'un PDF
linktitle: Extraire les pièces jointes
type: docs
weight: 50
url: /java/extract-attachment/
description: Découvrez comment extraire des fichiers incorporés et des annotations de pièces jointes à partir de documents PDF en Java à l'aide d'Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraire un ou tous les fichiers intégrés d'un PDF avec Java
Abstract: Cet article explique comment extraire les pièces jointes de documents PDF avec Aspose.PDF pour Java. Il couvre l'extraction d'une pièce jointe nommée unique, l'enregistrement de chaque fichier intégré dans un dossier de sortie, la lecture des métadonnées du fichier et l'exportation du contenu à partir d'une annotation FileAttachment sur une page.
---
Aspose.PDF pour Java prend en charge plusieurs flux d'extraction en fonction de la manière dont les pièces jointes sont stockées dans le document.


## 
Extraire une seule pièce jointe par son nom



Utilisez cet exemple lorsque vous devez enregistrer un fichier intégré spécifique à partir d'un PDF.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez la collection de fichiers intégrés jusqu'à ce que le nom de la pièce jointe requis soit trouvé.
1. Copiez le flux de pièces jointes dans le fichier de sortie et arrêtez-vous après l'extraction.


```java
public static void extractSingleAttachment(Path inputFile, String attachmentName, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Extracting attachment: " + attachmentName);

        boolean attachmentFound = false;
        for (FileSpecification fileSpecification : document.getEmbeddedFiles()) {
            if (attachmentName.equals(fileSpecification.getName())) {
                try (InputStream inputStream = fileSpecification.getContents();
                     OutputStream outputStream = Files.newOutputStream(outputFile)) {
                    inputStream.transferTo(outputStream);
                }
                System.out.println("Attachment extracted successfully");
                attachmentFound = true;
                break;
            }
        }

        if (!attachmentFound) {
            throw new IllegalArgumentException("Attachment '" + attachmentName + "' not found in PDF");
        }
    }
}
```

## 
Imprimer les paramètres du fichier intégré



Cette méthode d'assistance imprime les métadonnées stockées dans un objet [FileParams] (https://reference.aspose.com/pdf/java/com.aspose.pdf/fileparams/).


1. 
Vérifiez si l'objet de paramètres de fichier existe.

1. 
Lisez la somme de contrôle disponible, la date de création, la date de modification et les valeurs de taille.
1. Imprimez les valeurs sur la console.


```java
public static void printFileParams(FileParams params) {
    if (params != null) {
        try {
            System.out.println("CheckSum: " + params.getCheckSum());
        } catch (Exception ex) {
            System.out.println("CheckSum: null");
        }
        System.out.println("Creation Date: " + params.getCreationDate());
        System.out.println("Modification Date: " + params.getModDate());
        System.out.println("Size: " + params.getSize());
    }
}
```

## 
Extraire toutes les pièces jointes intégrées



Utilisez cet exemple lorsque chaque fichier incorporé dans le PDF doit être écrit dans un répertoire de sortie.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez la collection de fichiers intégrés et déterminez un nom de fichier de sortie sécurisé pour chaque élément.
1. Imprimez les métadonnées, enregistrez chaque flux de pièces jointes et continuez jusqu'à ce que tous les fichiers soient exportés.


```java
public static void extractAttachments(Path inputFile, Path outputDir) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Total files: " + document.getEmbeddedFiles().size());

        int fileIndex = 1;
        for (FileSpecification fileSpecification : document.getEmbeddedFiles()) {
            String fileName = fileSpecification.getName();
            if (fileName == null || fileName.isBlank()) {
                fileName = fileSpecification.getUnicodeName();
            }
            if (fileName == null || fileName.isBlank()) {
                fileName = "attachment_" + fileIndex + ".bin";
            }

            System.out.println("Name: " + fileName);
            System.out.println("Description: " + fileSpecification.getDescription());
            System.out.println("Mime Type: " + fileSpecification.getMIMEType());
            printFileParams(fileSpecification.getParams());

            Path outputPath = outputDir.resolve(fileName);
            try (InputStream inputStream = fileSpecification.getContents();
                 OutputStream outputStream = Files.newOutputStream(outputPath)) {
                inputStream.transferTo(outputStream);
            }
            fileIndex++;
        }
    }
}
```

## 
Extraire une annotation de pièce jointe



Utilisez cet exemple lorsque le fichier est joint via une annotation de page plutôt que via la collection de fichiers incorporés.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Localisez le premier [FileAttachmentAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/fileattachmentannotation/) sur la page.
1. Lisez sa spécification de fichier, exportez le contenu et imprimez le chemin de destination.

```java
public static void extractFileAttachmentAnnotation(Path inputFile, Path outputDir) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        FileAttachmentAnnotation fileAttachment = null;
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.FileAttachment) {
                fileAttachment = (FileAttachmentAnnotation) annotation;
                break;
            }
        }

        if (fileAttachment == null) {
            System.out.println("File attachment annotation not found.");
            return;
        }

        FileSpecification fileSpecification = fileAttachment.getFile();
        System.out.println("File name: " + fileSpecification.getName());

        Path outputPath = outputDir.resolve("extracted-" + fileSpecification.getName());
        try (InputStream inputStream = fileSpecification.getContents();
             OutputStream outputStream = Files.newOutputStream(outputPath)) {
            inputStream.transferTo(outputStream);
        }

        System.out.println("Extracted to: " + outputPath);
    }
}
```
