---
title: Convertir un PDF en EPUB, texte, XPS et plus en Java
linktitle: Convertir un PDF vers d'autres formats
type: docs
weight: 90
url: /java/convert-pdf-to-other-files/
lastmod: "2026-06-16"
description: Apprenez à convertir des fichiers PDF en EPUB, LaTeX, Markdown, texte, XPS et MobiXML en Java avec Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Comment convertir un PDF vers d'autres formats en Java
Abstract: Cet article explique comment convertir des fichiers PDF aux formats EPUB, TeX, Markdown, texte, XPS et MobiXML à l'aide d'Aspose.PDF pour Java, avec des options d'enregistrement spécifiques au format si nécessaire.
---
Aspose.PDF pour Java peut exporter des documents PDF vers des formats de sortie orientés texte, ebook, impression et balisage.


## 
Convertir un PDF en EPUB



Utilisez cet exemple lorsqu'un document PDF doit être exporté au format ebook EPUB.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez [`EpubSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/epubsaveoptions/) et définissez le mode de reconnaissance sur `Flow`.
1. Appelez `document.save(outputFile.toString(), saveOptions)` pour que le contenu PDF soit exporté sous forme de balisage EPUB redistribuable.

1. 
Enregistrez le fichier EPUB converti.


```java
public static void convertPdfToEpub(Path inputFile, Path outputFile) {
        try (Document document = new Document(inputFile.toString())) {
            EpubSaveOptions saveOptions = new EpubSaveOptions();
            saveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.Flow);
            document.save(outputFile.toString(), saveOptions);
        }
        System.out.println(inputFile + " converted into " + outputFile);
    }
```

## 
Convertir un PDF en TeX



Utilisez cet exemple lorsque le contenu PDF doit être exporté dans le balisage TeX.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Créez [`TeXSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/texsaveoptions/) pour la sérialisation TeX.

1. 
Appelez `document.save(outputFile.toString(), saveOptions)` pour que le contenu PDF soit émis sous forme de balisage TeX.

1. 
Enregistrez le fichier TeX résultant.


```java
public static void convertPdfToTex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), new TeXSaveOptions());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir un PDF en texte brut



Utilisez cet exemple lorsqu'un document PDF doit être exporté sous forme de fichier texte.

1. Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez un [`TextDevice`] (https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/textdevice/) pour extraire le contenu textuel des pages PDF.

1. 
Appelez `device.process(document.getPages().get_Item(1), outputFile.toString())` pour écrire la première page sous forme de texte brut.

1. 
Enregistrez le fichier de sortie texte.


```java
public static void convertPdfToTxt(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextDevice device = new TextDevice();
        device.process(document.getPages().get_Item(1), outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir un PDF en XPS

Utilisez cet exemple lorsqu'un document PDF doit être converti au format XPS.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez [`XpsSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/xpssaveoptions/) et activez les polices TrueType intégrées.

1. 
Appelez `document.save(outputFile.toString(), saveOptions)` pour que le PDF soit sérialisé au format XPS avec des ressources de polices intégrées.

1. 
Enregistrez le fichier XPS converti.

```java
public static void convertPdfToXps(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XpsSaveOptions saveOptions = new XpsSaveOptions();
        saveOptions.setUseEmbeddedTrueTypeFonts(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir un PDF en Markdown



Utilisez cet exemple lorsque le contenu PDF doit être exporté au format Markdown.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez [`MarkdownSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/markdownsaveoptions/) et configurez le répertoire de ressources d'image ainsi que la sortie de balise d'image HTML.

1. 
Appelez `document.save(outputFile.toString(), saveOptions)` pour que le contenu PDF soit émis en tant que Markdown avec des ressources d'images externes.
1. Enregistrez le fichier Markdown généré.


```java
public static void convertPdfToMd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
        saveOptions.setResourcesDirectoryName("images");
        saveOptions.setUseImageHtmlTag(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir un PDF en Mobi XML



Utilisez cet exemple lorsque le contenu PDF doit être exporté au format XML compatible Mobi.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Sélectionnez [`SaveFormat`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/saveformat/) `MobiXml` comme format de sérialisation cible.
1. Appelez `document.save(outputFile.toString(), SaveFormat.MobiXml)` pour que le PDF soit exporté au format XML compatible Mobi.

1. 
Enregistrez le fichier converti.

```java
public static void convertPdfToMobiXml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), SaveFormat.MobiXml);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
