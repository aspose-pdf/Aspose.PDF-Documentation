---
title: Convertir un fichier PDF en d'autres formats 
linktitle: Convertir PDF en d'autres formats 
type: docs
weight: 90
url: /fr/java/convert-pdf-to-other-files/
lastmod: "2021-11-19"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir un fichier PDF en d'autres formats de fichier.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convertir PDF en EPUB

{{% alert color="success" %}}
**Essayez de convertir un PDF en EPUB en ligne**

Aspose.PDF pour Java vous présente une application en ligne gratuite ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Conversion PDF en EPUB avec Aspose.PDF avec une application gratuite](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Electronic Publication">EPUB</abbr>** (abréviation de publication électronique) est une norme gratuite et ouverte pour les livres électroniques du Forum International de Publication Numérique (IDPF).
 Les fichiers ont l'extension .epub. EPUB est conçu pour le contenu reformatable, ce qui signifie qu'un lecteur EPUB peut optimiser le texte pour un appareil d'affichage particulier. EPUB prend également en charge le contenu à mise en page fixe. Le format est destiné à être un format unique que les éditeurs et les maisons de conversion peuvent utiliser en interne, ainsi que pour la distribution et la vente. Il remplace la norme Open eBook.

Aspose.PDF pour Java prend en charge la fonctionnalité de conversion des documents PDF au format EPUB. Aspose.PDF pour Java a une classe nommée [EpubSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubSaveOptions) qui peut être utilisée comme deuxième argument de la méthode [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).save(..), pour générer un fichier EPUB. Veuillez essayer d'utiliser le fragment de code suivant pour accomplir cette exigence.

```java
// Charger le document PDF
Document document = new Document(DATA_DIR + "PDFToEPUB.pdf");
// Instancier les options de sauvegarde Epub
EpubSaveOptions options = new EpubSaveOptions();
// Spécifier la mise en page pour les contenus
options.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.Flow);
// Enregistrer le document ePUB
document.save(DATA_DIR + "PDFToEPUB_out.epub", options);
document.close();
```

## Convertir PDF en LaTeX/TeX

**Aspose.PDF pour Java** prend en charge la conversion de PDF en LaTeX/TeX.  
Le format de fichier LaTeX est un format de fichier texte avec un balisage spécial utilisé dans le système de préparation de documents basé sur TeX pour la composition de haute qualité.

Pour convertir des fichiers PDF en TeX, Aspose.PDF dispose de la classe [TeXSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXSaveOptions) qui fournit la méthode `setOutDirectoryPath` pour enregistrer des images temporaires pendant le processus de conversion.

L'extrait de code suivant montre le processus de conversion de fichiers PDF au format TEX avec Java.

```java
String documentFileName = Paths.get(DATA_DIR.toString(), "PDFToTeX.pdf").toString();
String texDocumentFileName = Paths.get(DATA_DIR.toString(), "PDFToTeX_out.tex").toString();

// Créer un objet Document
Document document = new Document(documentFileName);

// Instancier l'option de sauvegarde LaTex
TeXSaveOptions saveOptions = new TeXSaveOptions();

// Spécifier le répertoire de sortie
String pathToOutputDirectory = DATA_DIR.toString();

// Définir le chemin du répertoire de sortie pour l'objet d'option de sauvegarde
saveOptions.setOutDirectoryPath(pathToOutputDirectory);

// Enregistrer le fichier PDF au format LaTex
document.save(texDocumentFileName, saveOptions);
document.close();
```


{{% alert color="success" %}}
**Essayez de convertir PDF en LaTeX/TeX en ligne**

Aspose.PDF pour Java vous présente l'application en ligne gratuite ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en LaTeX/TeX avec l'application gratuite](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Convertir PDF en Texte

**Aspose.PDF pour Java** prend en charge la conversion de l'ensemble du document PDF et d'une seule page en un fichier texte.

### Convertir l'ensemble du document PDF en fichier texte

Vous pouvez convertir un document PDF en fichier TXT en utilisant la méthode Visit de la classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber).

Le snippet de code suivant explique comment extraire les textes de toutes les pages.

```java
// Ouvrir le document
String pdfFileName = Paths.get(DATA_DIR.toString(), "demo.pdf").toString();
String txtFileName = Paths.get(DATA_DIR.toString(), "PDFToTXT_out.txt").toString();

// Charger le document PDF
Document document = new Document(pdfFileName);
TextAbsorber ta = new TextAbsorber();
ta.visit(document);
// Enregistrer le texte extrait dans un fichier texte
BufferedWriter writer = new BufferedWriter(new FileWriter(txtFileName));
writer.write(ta.getText());
writer.close();
```


{{% alert color="success" %}}
**Essayez de convertir Convertir PDF en Texte en ligne**

Aspose.PDF pour Java vous présente l'application en ligne gratuite ["PDF en Texte"](https://products.aspose.app/pdf/conversion/pdf-to-txt), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en Texte avec Application Gratuite](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### Convertir une page PDF en fichier texte

Vous pouvez convertir un document PDF en fichier TXT avec Aspose.PDF pour Java. Vous devez utiliser la méthode Visit de la classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) pour résoudre cette tâche.

Le code suivant explique comment extraire les textes des pages particulières.

```java
String pdfFileName = Paths.get(DATA_DIR.toString(), "demo.pdf").toString();
String txtFileName = Paths.get(DATA_DIR.toString(), "PDFToTXT_out.txt").toString();

// Charger le document PDF
Document document = new Document(pdfFileName);

TextAbsorber ta = new TextAbsorber();
int[] pages = new int[] { 1, 3, 4 };

for (int page : pages) {
    ta.visit(document.getPages().get_Item(page));
}

// Enregistrer le texte extrait dans un fichier texte
BufferedWriter writer = new BufferedWriter(new FileWriter(txtFileName));
writer.write(ta.getText());
writer.close();
document.close();
```


## Convertir PDF en XPS

**Aspose.PDF pour Java** offre la possibilité de convertir des fichiers PDF au format <abbr title="Spécification du Papier XML">XPS</abbr>. Essayons d'utiliser l'extrait de code présenté pour convertir des fichiers PDF au format XPS avec Java.

{{% alert color="success" %}}
**Essayez de convertir PDF en XPS en ligne**

Aspose.PDF pour Java vous présente une application gratuite en ligne ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en XPS avec Application Gratuite](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

Le type de fichier XPS est principalement associé à la Spécification du Papier XML par Microsoft Corporation. La Spécification du Papier XML (XPS), anciennement nommée Metro et englobant le concept marketing Next Generation Print Path (NGPP), est l'initiative de Microsoft pour intégrer la création et la visualisation de documents dans le système d'exploitation Windows.

Pour convertir des fichiers PDF en XPS, Aspose.PDF dispose de la classe [XpsSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsSaveOptions) utilisée comme deuxième argument du constructeur Document.save(..) pour générer le fichier XPS.
 Le code suivant montre le processus de conversion des fichiers PDF au format XPS.

```java
String documentFileName = Paths.get(DATA_DIR.toString(), "sample.pdf").toString();
String xpsDocumentFileName = Paths.get(DATA_DIR.toString(), "sample-res-xps.xps").toString();

// Créer un objet Document
Document document = new Document(documentFileName);

// Instancier les options de sauvegarde XPS
XpsSaveOptions saveOptions = new XpsSaveOptions();

// Sauvegarder la sortie au format XML
document.save(xpsDocumentFileName, saveOptions);
document.close();
```