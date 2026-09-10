---
title: Convertir un PDF en PDF/A, PDF/E et PDF/X en Java
linktitle: Convertir un PDF en PDF/A, PDF/E et PDF/X
type: docs
weight: 120
url: /java/convert-pdf-to-pdf_x/
lastmod: "2026-06-16"
description: Découvrez comment convertir des fichiers PDF en PDF/A, PDF/E et PDF/X en Java avec Aspose.PDF pour les flux de travail d'archivage, d'ingénierie, d'accessibilité et d'impression.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Comment convertir un PDF aux formats PDF/x
Abstract: Cet article explique comment valider et convertir des documents PDF aux formats PDF/A, PDF/E et PDF/X à l'aide d'Aspose.PDF pour Java. Il couvre la génération de journaux, la conservation des pièces jointes pour PDF/A-3, la substitution des polices manquantes, le marquage automatique, la configuration du profil ICC et les paramètres d'intention de sortie.
---
Aspose.PDF pour Java peut valider et convertir des fichiers PDF standard en standards PDF orientés archivage et échange.


## 
Convertir un PDF en PDF/A



Utilisez cet exemple lorsqu'un PDF standard doit être converti en un document d'archives compatible PDF/A.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Appelez `document.convert(...)` avec [`PdfFormat`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_1B` et [`ConvertErrorAction`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction/) `Delete`.
1. Écrivez le journal de validation dans un fichier XML side-car afin que les problèmes de conformité soient enregistrés lors de la conversion.

1. 
Enregistrez la sortie PDF/A validée.


```java
public static void convertPdfToPdfA(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.convert(logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
        document.save(outputFile.toString());
    }
}
```

## 
Convertir un PDF en PDF/E



Utilisez cet exemple lorsqu'un PDF doit être converti au standard PDF/E orienté ingénierie.


1. 
Créez [`PdfFormatConversionOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) pour [`PdfFormat`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_E_1` et le chemin du fichier journal souhaité.
1. Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Appelez `document.convert(options)` pour que la conversion de conformité soit exécutée avec l'objet d'options préparé.

1. 
Enregistrez le fichier PDF conforme obtenu.


```java
public static void convertPdfToPdfE(Path inputFile, Path outputFile) {
    PdfFormatConversionOptions options = new PdfFormatConversionOptions(
            logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_E_1, ConvertErrorAction.Delete);

    try (Document document = new Document(inputFile.toString())) {
        document.convert(options);
        document.save(outputFile.toString());
    }
}
```

## 
Convertir un PDF en PDF/X



Utilisez cet exemple lorsqu'un PDF doit être converti au format PDF/X orienté impression.

1. Créez [`PdfFormatConversionOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) pour [`PdfFormat`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_X_4` et le chemin du fichier journal souhaité.

1. 
Configurez un [`OutputIntent`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/outputintent/) tel que `FOGRA39` afin que le profil de couleur cible d'impression soit intégré dans les paramètres de conversion.

1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et appelez `document.convert(options)`.

1. 
Enregistrez la sortie PDF/X convertie.

```java
public static void convertPdfToPdfX(Path inputFile, Path outputFile) {
    PdfFormatConversionOptions options = new PdfFormatConversionOptions(
            logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_X_4, ConvertErrorAction.Delete);
    options.setOutputIntent(new OutputIntent("FOGRA39"));

    try (Document document = new Document(inputFile.toString())) {
        document.convert(options);
        document.save(outputFile.toString());
    }
}
```
