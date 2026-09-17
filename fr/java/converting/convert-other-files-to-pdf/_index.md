---
title: Convertir d'autres formats de fichiers en PDF en Java
linktitle: Convertir d'autres formats de fichiers en PDF
type: docs
weight: 80
url: /java/convert-other-files-to-pdf/
lastmod: "2026-06-16"
description: Découvrez comment convertir des fichiers EPUB, Markdown, PCL, XPS, PostScript, XML, XSL-FO, OFD et TeX en PDF en Java avec Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Comment convertir d'autres formats de fichiers en PDF en Java
Abstract: Cet article explique comment convertir plusieurs formats de fichiers sources en PDF à l'aide d'Aspose.PDF pour Java. Il couvre les flux de travail de conversion EPUB, Markdown, OFD, PCL, PostScript, EPS, TeX, texte, XML, XPS et XSL-FO en utilisant des options de chargement spécifiques au format et des étapes de prétraitement si nécessaire.
---
Aspose.PDF pour Java prend en charge la conversion des formats de document, de balisage et de description de page en PDF.


## 
Convertir OFD en PDF



Utilisez cet exemple lorsqu'un document OFD doit être converti en PDF.


1. 
Ouvrez la source OFD en passant le chemin du fichier et [`OfdLoadOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/ofdloadoptions/) dans le constructeur [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Laissez Aspose.PDF analyser le package OFD dans le modèle de document PDF.
1. Enregistrez le PDF résultant dans le chemin de sortie cible.


```java
public static void convertOfdToPdf(Path inputFile, Path outputFile) {
       try (Document document = new Document(inputFile.toString(), new OfdLoadOptions())) {
           document.save(outputFile.toString());
       }
       System.out.println(inputFile + " converted into " + outputFile);
   }
```

## 
Convertir TeX en PDF



Utilisez cet exemple lorsque le contenu TeX doit être rendu directement au format PDF.


1. 
Ouvrez la source TeX en passant le chemin du fichier et [`TeXLoadOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/texloadoptions/) dans le constructeur [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Laissez Aspose.PDF interpréter le balisage TeX et créer la mise en page PDF pendant le chargement.
1. Enregistrez le PDF généré.


```java
public static void convertTexToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new com.aspose.pdf.TeXLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir PostScript en PDF



Utilisez cet exemple lorsqu'un fichier PostScript doit être converti en document PDF.


1. 
Ouvrez la source PostScript avec [`PsLoadOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/) dans le constructeur [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Laissez Aspose.PDF traduire le flux de description de page PostScript en un modèle de document PDF.
1. Enregistrez le fichier PDF converti.


```java
public static void convertPostScripToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir EPS en PDF



Utilisez cet exemple lorsqu'un fichier PostScript encapsulé doit être converti en PDF.


1. 
Ouvrez la source EPS avec [`PsLoadOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/psloadoptions/) car EPS suit le même chemin de chargement basé sur PostScript.

1. 
Chargez le fichier dans un [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) afin que le contenu de la description de la page soit converti lors de l'importation.
1. Enregistrez le PDF de sortie.


```java
public static void convertEpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir EPUB en PDF



Utilisez cet exemple lorsqu'un livre électronique EPUB doit être converti en PDF.


1. 
Ouvrez la source EPUB en passant le chemin du fichier et [`EpubLoadOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/epubloadoptions/) dans le constructeur [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Laissez Aspose.PDF charger la structure de l'ebook et la transformer en pages PDF.
1. Enregistrez le PDF converti.


```java
public static void convertEpubToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new EpubLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir Markdown en PDF



Utilisez cet exemple lorsque le contenu Markdown doit être rendu et enregistré au format PDF.


1. 
Ouvrez la source Markdown en passant le chemin du fichier et [`MdLoadOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/mdloadoptions/) dans le constructeur [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Laissez Aspose.PDF interpréter le contenu Markdown et le restituer dans le contenu de la page PDF.
1. Enregistrez le fichier PDF de sortie.


```java
public static void convertMdToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new MdLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertissez du texte en PDF avec un flux de travail simple



Utilisez cet exemple lorsqu'un fichier texte brut doit être rapidement converti en PDF.


1. 
Lisez la source en texte brut avec le décodage UTF-8 afin que le contenu du texte soit disponible sous forme de chaîne Java.

1. 
Créez un [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vide et ajoutez un [`Page`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Enveloppez le texte dans un [`TextFragment`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) et ajoutez-le à la collection de paragraphes de la page.

1. 
Enregistrez le PDF généré.


```java
public static void convertTxtToPdfSimple(Path inputFile, Path outputFile) throws Exception {
    String textContent = Files.readString(inputFile, StandardCharsets.UTF_8);
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment(textContent));
        page.close();
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertissez du texte en PDF avec des options avancées



Utilisez cet exemple lorsque le texte brut doit être converti avec des options de mise en page ou de codage supplémentaires.


1. 
Lisez toutes les lignes de texte du fichier d'entrée afin que les marqueurs de saut de page puissent être inspectés pendant la conversion.
1. Créez un [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) vide et configurez chaque [`Page`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) avec des marges et un état de texte par défaut.

1. 
Résolvez la police à espacement fixe via [`FontRepository`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/) et ajoutez chaque ligne sous la forme d'un [`TextFragment`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).

1. 
Enregistrez le fichier de sortie une fois la boucle de création de page terminée.


```java
public static void convertTxtToPdf(Path inputFile, Path outputFile) throws Exception {
    List<String> lines = Files.readAllLines(inputFile);
    try (Document document = new Document()) {
        com.aspose.pdf.Page page = document.getPages().add();
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        int pageCount = 1;
        for (String line : lines) {
            if (!line.isEmpty() && line.charAt(0) == '\f') {
                page = document.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
                page.getPageInfo().getDefaultTextState().setFontSize(12);
                pageCount++;
                if (pageCount == 4) {
                    break;
                }
            } else {
                page.getParagraphs().add(new TextFragment(line));
            }
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir PCL en PDF



Utilisez cet exemple lorsqu'un flux d'impression PCL doit être converti en PDF.

1. Créez [`PclLoadOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pclloadoptions/) et activez la suppression des erreurs d'analyse lorsqu'un comportement d'importation indulgent est requis.

1. 
Ouvrez la source PCL en transmettant le chemin du fichier et chargez les options dans le constructeur [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Enregistrez le résultat au format PDF.


```java
public static void convertPclToPdf(Path inputFile, Path outputFile) {
    PclLoadOptions loadOptions = new PclLoadOptions();
    loadOptions.setSupressErrors(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir XML en PDF via XSLT et HTML



Utilisez cet exemple lorsque les données XML doivent être transformées avant la génération finale du PDF.

1. Transformez la source XML avec le fichier XSLT en fichier HTML temporaire en appelant la méthode de transformation dédiée.

1. 
Transmettez le fichier HTML généré dans la fonction de conversion HTML vers PDF existante afin que le PDF final utilise le flux de travail standard [`HtmlLoadOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/).

1. 
Supprimez le fichier HTML temporaire dans le bloc `finally` une fois la conversion terminée.

1. 
Enregistrez le fichier PDF généré.


```java
public static void convertXmlToPdf(Path xsltFile, Path xmlFile, Path outputFile) throws Exception {
    Path htmlFile = Files.createTempFile("aspose-pdf-xml-", ".html");
    try {
        transformXmlToHtml(xmlFile, xsltFile, htmlFile);
        HtmlToPdfExamples.convertHtmlToPdf(htmlFile, outputFile);
    } finally {
        Files.deleteIfExists(htmlFile);
    }
    System.out.println(xmlFile + " converted into " + outputFile);
}
```

## 
Convertir XPS en PDF

Utilisez cet exemple lorsqu'un document XPS doit être converti en PDF.


1. 
Ouvrez la source XPS en passant le chemin du fichier et [`XpsLoadOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/xpsloadoptions/) dans le constructeur [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Laissez Aspose.PDF interpréter la description de la page XPS pendant le chargement du document.

1. 
Enregistrez le PDF converti.


```java
public static void convertXpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new XpsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir XSL-FO en PDF

Utilisez cet exemple lorsque le contenu XSL-FO doit être rendu au format PDF.


1. 
Créez [`XslFoLoadOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions/) avec le chemin XSLT afin que la source XML puisse être transformée lors du chargement.

1. 
Configurez le mode de gestion des erreurs d'analyse pour qu'il soit lancé immédiatement lorsqu'un XSL-FO non valide est rencontré.

1. 
Ouvrez la source XML dans un [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) avec ces options de chargement.

1. 
Enregistrez le document PDF résultant.

```java
public static void convertXslFoToPdf(Path xsltFile, Path xmlFile, Path outputFile) {
    XslFoLoadOptions loadOptions = new XslFoLoadOptions(xsltFile.toString());
    loadOptions.setParsingErrorsHandlingType(XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately);
    try (Document document = new Document(xmlFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(xmlFile + " converted into " + outputFile);
}
```

## Transformer XML en HTML intermédiaire



Utilisez cette méthode lorsque les données XML doivent être transformées en HTML avant l'étape finale de conversion PDF.


1. 
Ouvrez les fichiers d'entrée XML et XSLT en tant que sources de transformation.

1. 
Créez un `Transformer` à partir de la feuille de style XSLT et exécutez-le sur la source XML.

1. 
Écrivez le fichier HTML transformé sur le disque afin que la fonction de conversion PDF en aval puisse le charger.

```java
private static void transformXmlToHtml(Path xmlFile, Path xsltFile, Path htmlFile) throws Exception {
    Transformer transformer = TransformerFactory.newInstance()
            .newTransformer(new StreamSource(xsltFile.toFile()));
    transformer.transform(new StreamSource(xmlFile.toFile()), new StreamResult(htmlFile.toFile()));
}
```
