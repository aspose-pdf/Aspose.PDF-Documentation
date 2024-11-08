---
title: Convertir un fichier HTML en PDF en Java
linktitle: Convertir un fichier HTML en PDF
type: docs
weight: 40
url: /fr/java/convert-html-to-pdf/
lastmod: "2021-11-19"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir les formats HTML et MHTML en fichier PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Aperçu

Cet article explique comment convertir HTML en PDF en utilisant Java. Le code est très simple, il suffit de charger le HTML dans la classe Document et de l'enregistrer en tant que PDF de sortie. La conversion de MHTML en PDF en Java est également similaire. Il couvre les sujets suivants

- [Java HTML en PDF](#convert-html-to-pdf)
- [Java MHTML en PDF](#convert-mhtml-to-pdf)
- [Java Convertir HTML en PDF](#convert-html-to-pdf)
- [Java Convertir MHTML en PDF](#convert-mhtml-to-pdf)
- [Java PDF à partir de HTML](#convert-html-to-pdf)
- [Java PDF à partir de MHTML](#convert-mhtml-to-pdf)
- [Java Convertisseur HTML en PDF - Comment convertir une page Web en PDF](#convert-html-to-pdf)

- [Java Bibliothèque HTML en PDF, API ou Code pour rendre, enregistrer, générer ou créer un PDF de manière programmatique à partir de HTML](#convert-html-to-pdf)

## Java HTML to PDF Converter Library

**Aspose.PDF for Java** est une API de manipulation PDF qui vous permet de convertir n'importe quel document HTML existant en PDF sans problème.
Le processus de conversion de HTML en PDF peut être personnalisé de manière flexible.

## Convertir HTML en PDF

L'exemple de code Java suivant montre comment convertir un document HTML en PDF.

1. Créez une instance de la classe [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions).
1. Initialisez l'objet [Document](https://reference.aspose.com/page/java/com.aspose.page/document).
1. Enregistrez le document PDF de sortie en appelant la méthode **Document.save(String)**.

```java
// Ouvrir le document PDF source
Document document = new Document(DATA_DIR + "PDFToHTML.pdf")

// Instancier un objet HTML SaveOptions
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();

// Enregistrer le document
document.save(DATA_DIR + "MultiPageHTML_out.html", htmlsaveOptions);
```

{{% alert color="success" %}}
**Essayez de convertir HTML en PDF en ligne**

Aspose vous présente une application en ligne gratuite ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Convertion HTML to PDF using Free App](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## Conversion avancée de HTML à PDF

Le moteur de conversion HTML dispose de plusieurs options qui nous permettent de contrôler le processus de conversion.

### Support des Media Queries

1. Créez un [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) HTML.
1. Définissez le mode Impression ou Écran.
1. Initialisez l'[objet Document](<https://reference.aspose.com/page/java/com.aspose.page/document>).
1. Enregistrez le document PDF de sortie.

Les media queries sont une technique populaire pour fournir une feuille de style adaptée à différents appareils. Nous pouvons définir le type d'appareil en utilisant la propriété [HtmlMediaType](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlMediaType).

```java
// Créez un LoadOptions HTML
HtmlLoadOptions options = new HtmlLoadOptions();

// Définissez le mode Impression ou Écran
options.setHtmlMediaType(HtmlMediaType.Print);

// Initialisez l'objet document
String htmlFileName = Paths.get(DATA_DIR.toString(), "test.html").toString();
Document document = new Document(htmlFileName, options);

// Enregistrez le document PDF de sortie
document.save(Paths.get(DATA_DIR.toString(), "HTMLtoPDF.pdf").toString());
document.close();
```


### Activer (désactiver) l'intégration des polices

1. Ajouter de nouvelles [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) HTML.
1. Activer/Désactiver l'intégration des polices.
1. Enregistrer un nouveau Document.

Les pages HTML utilisent souvent des polices (par exemple, des polices du dossier local, Google Fonts, etc.). Nous pouvons également contrôler l'intégration des polices dans un document en utilisant la propriété [IsEmbedFonts](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions#isEmbedFonts--).

```java
HtmlLoadOptions options = new HtmlLoadOptions();
// Activer/Désactiver l'intégration des polices
options.setEmbedFonts(true);

Document document = new Document(DATA_DIR + "test_fonts.html", options);
document.save(DATA_DIR + "html_test.PDF");
document.close();
```

### Gérer le chargement des ressources externes

Le moteur de conversion fournit un mécanisme qui vous permet de contrôler le chargement de certaines ressources associées au document HTML.

La classe [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) a la propriété [CustomLoaderOfExternalResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions#setCustomLoaderOfExternalResources-com.aspose.pdf.LoadOptions.ResourceLoadingStrategy-) avec laquelle nous pouvons définir le comportement du chargeur de ressources.

```java
HtmlLoadOptions options = new HtmlLoadOptions();

options.setCustomLoaderOfExternalResources(
        new LoadOptions.ResourceLoadingStrategy() {
            public LoadOptions.ResourceLoadingResult invoke(String resourceURI) {
                // Création d'un modèle de ressource vide pour remplacement :
                LoadOptions.ResourceLoadingResult res = new LoadOptions.ResourceLoadingResult(new byte[] {});
                // Retourner un tableau d'octets vide dans le cas du serveur i.imgur.com
                if (resourceURI.contains("i.imgur.com")) {
                    return res;
                } else {
                    // Traiter les ressources avec le chargeur de ressources par défaut
                    res.setLoadingCancelled(true);
                    return res;
                }
            }   
});

Document document = new Document(DATA_DIR + "test.html", options);
document.save(DATA_DIR + "html_test.PDF");
document.close();    
```

## Convertir MHTML en PDF

{{% alert color="success" %}}
**Essayez de convertir MHTML en PDF en ligne**


Aspose.PDF pour Java vous présente l'application en ligne gratuite ["MHTML vers PDF"](https://products.aspose.app/pdf/conversion/mhtml-to-pdf), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF MHTML vers PDF en utilisant l'application gratuite](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)
{{% /alert %}}

<abbr title="Encapsulation MIME de documents HTML agrégés">MHTML</abbr>, abréviation de MIME HTML, est un format d'archive de page web utilisé pour combiner des ressources qui sont généralement représentées par des liens externes (tels que des images, des animations Flash, des applets Java et des fichiers audio) avec du code HTML en un seul fichier. Le contenu d'un fichier MHTML est encodé comme s'il s'agissait d'un message email HTML, en utilisant le type MIME multipart/related.

Le prochain extrait de code montre comment convertir des fichiers MHTML au format PDF avec Java :

```java
// Créer une instance de MhtLoadOptions pour spécifier les options de 
// chargement pour le fichier MHTML.
MhtLoadOptions options = new MhtLoadOptions();

// Définir le chemin du fichier MHTML.
String mhtmlFileName = Paths.get(DATA_DIR.toString(), "samplefile.mhtml").toString();

// Charger le fichier MHTML dans un objet Document.
Document document = new Document(mhtmlFileName, options);

// Enregistrer le document en tant que fichier PDF.
document.save(Paths.get(DATA_DIR.toString(), "MarkdowntoPDF.pdf").toString());

// Fermer le document.
document.close();
```