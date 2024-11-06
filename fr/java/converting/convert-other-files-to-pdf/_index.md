---
title: Convertir divers formats de fichiers en PDF 
linktitle: Convertir d'autres formats de fichiers en PDF 
type: docs
weight: 80
url: fr/java/convert-other-files-to-pdf/
lastmod: "2021-11-19"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir d'autres formats de fichiers en document PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Convertir EPUB en PDF

**Aspose.PDF pour Java** vous permet de convertir simplement des fichiers EPUB au format PDF.

<abbr title="publication électronique">EPUB</abbr> (abréviation de publication électronique) est une norme de livre électronique libre et ouverte du Forum international de l'édition numérique (IDPF). Les fichiers ont l'extension .epub. EPUB est conçu pour un contenu reflowable, ce qui signifie qu'un lecteur EPUB peut optimiser le texte pour un appareil d'affichage particulier.

Pour convertir des fichiers EPUB au format PDF, Aspose.PDF pour Java dispose d'une classe nommée [EpubLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubLoadOptions) qui est utilisée pour charger le fichier EPUB source.
 Après cela, l'objet est passé comme argument à l'initialisation de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document), car cela aide le moteur de rendu PDF à déterminer le format d'entrée du document source.

Le code suivant montre le processus de conversion d'un fichier EPUB en format PDF.

1. Créez un [`LoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/loadoptions) EPUB.
1. Initialisez l'objet [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document).
1. Enregistrez le document PDF de sortie.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertEPUBtoPDF {

    private ConvertEPUBtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Créez un LoadOptions EPUB
        EpubLoadOptions options = new EpubLoadOptions();

        // Initialisez l'objet document
        String epubFileName = Paths.get(_dataDir.toString(), "aliceDynamic.epub").toString();
        Document document = new Document(epubFileName, options);

        // Enregistrez le document PDF de sortie
        document.save(Paths.get(_dataDir.toString(),"EPUBtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**Essayez de convertir EPUB en PDF en ligne**

Aspose.PDF pour Java vous présente l'application gratuite en ligne ["EPUB en PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion EPUB en PDF avec application gratuite](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## Convertir Markdown en PDF

**Cette fonctionnalité est prise en charge par la version 19.6 ou supérieure.**

{{% alert color="success" %}}
**Essayez de convertir Markdown en PDF en ligne**

Aspose.PDF pour Java vous présente l'application gratuite en ligne ["Markdown en PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion Markdown en PDF avec application gratuite](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Markdown est un outil de conversion de texte en HTML pour les auteurs web.
 Markdown vous permet d'écrire dans un format texte brut facile à lire et à écrire, puis de le convertir en XHTML (ou HTML) structurellement valide.

Le snippet de code suivant montre comment utiliser cette fonctionnalité avec Aspose.PDF pour Java :

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertMDtoPDF {

    private ConvertMDtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Instancier l'objet option de chargement Latex
        MdLoadOptions options = new MdLoadOptions();
        
        // Créer un objet Document
        String markdownFileName = Paths.get(_dataDir.toString(), "samplefile.md").toString();
        Document document = new Document(markdownFileName, options);

        // Enregistrer le document PDF de sortie
        document.save(Paths.get(_dataDir.toString(),"MarkdownToPDF.pdf").toString());
    }
}

```

## Convertir PCL en PDF

<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language) est un langage d'imprimante Hewlett-Packard développé pour accéder aux fonctionnalités standard des imprimantes. Les niveaux PCL 1 à 5e/5c sont des langages basés sur des commandes qui utilisent des séquences de contrôle traitées et interprétées dans l'ordre de leur réception. Au niveau consommateur, les flux de données PCL sont générés par un pilote d'impression. La sortie PCL peut également être facilement générée par des applications personnalisées.

{{% alert color="success" %}}
**Essayez de convertir PCL en PDF en ligne**

Aspose.PDF pour Java vous présente l'application gratuite en ligne ["PCL to PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Conversion d'Aspose.PDF de PCL en PDF avec une application gratuite](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**Actuellement, seules les versions PCL5 et antérieures sont prises en charge.**

|**Jeux de commandes**|**Support**|**Exceptions**|**Description**|

| :- | :- | :- | :- |
|Commandes de contrôle de travail|+|Mode d'impression recto verso|Contrôler le processus d'impression : nombre de copies, bac de sortie, impression en recto/verso, décalages gauche et haut, etc.|
|Commandes de contrôle de page|+|Commande de saut de perforation|Spécifier une taille de page, marges, orientation de la page, interlignes, distances inter-caractères, etc.|
|Commandes de positionnement du curseur|+| |Spécifier la position du curseur et, par conséquent, les origines du texte, des images raster ou vectorielles et des détails.|

|Commandes de sélection de police|+|<p>1. Commande de données d'impression transparente.</p><p>2. Polices intégrées. Dans la version actuelle, au lieu de créer une police intégrée, notre bibliothèque sélectionne une police appropriée parmi les polices TrueType "dures" existantes installées sur une machine cible. <br>   L'adéquation est définie par le rapport largeur/hauteur. <br>   Cette fonctionnalité fonctionne uniquement pour les polices Bitmap et TrueType et ne garantit pas que le texte imprimé avec une police intégrée sera pertinent pour celui du fichier source. <br>   Parce que les codes de caractères dans la police intégrée peuvent ne pas correspondre aux codes par défaut.</p><p>3. Jeux de symboles définis par l'utilisateur.</p>|Permet le chargement de polices intégrées depuis le fichier PCL et leur gestion en mémoire.|
|Commandes graphiques raster|+|Seulement noir et blanc|Permet le chargement d'images raster depuis le fichier PCL en mémoire, spécifie des paramètres raster <br>tels que la largeur, la hauteur, le type de compression, la résolution, etc.|
|Commandes couleur|+| |Permet la coloration de tous les objets imprimables.|
|Commandes de modèle d'impression|+| |Permet de remplir le texte, les images raster et les zones rectangulaires avec des motifs prédéfinis et définis par l'utilisateur, spécifie le mode de transparence pour les motifs et l'image raster source.|
 <br>Les motifs prédéfinis sont le hachurage, le croisillon et les ombrages.|
|Commandes de remplissage de zone rectangulaire|+| |Permet la création et le remplissage de zones rectangulaires avec des motifs.|
|Commandes graphiques vectorielles HP-GL/2|+|La commande vectorielle criblée (SV), la commande de mode de transparence (TR), la commande de données transparentes (TD), RO (Rotation du système de coordonnées), la commande de polices évolutives ou bitmap (SB), la commande d'inclinaison des caractères (SL) et l'espace supplémentaire (ES) ne sont pas implémentés et les commandes DV (Définir le chemin du texte variable) sont réalisées en version bêta.|<p>- Permet de charger des images vectorielles HP-GL/2 à partir du fichier PCL en mémoire. L'image vectorielle a une origine dans le coin inférieur gauche de la zone imprimable, peut être mise à l'échelle, translatée, tournée et coupée.</p><p>- Une image vectorielle peut contenir du texte, comme des étiquettes, et des figures géométriques telles que rectangle, cercle, ellipse, ligne, arc, courbe de Bézier et figures complexes composées des simples.</p><p>- Les figures fermées, y compris les lettres des étiquettes, peuvent être remplies avec un remplissage uni ou un motif vectoriel.</p><p>- Le motif peut être un hachurage, un hachurage croisé, un ombrage, un hachurage défini par l'utilisateur, un hachurage PCL ou un hachurage croisé et défini par l'utilisateur PCL. Les motifs PCL sont des trames. Les étiquettes peuvent être individuellement tournées, mises à l'échelle, et orientées dans quatre directions : haut, bas, gauche et droite. Les directions gauche et droite impliquent un arrangement des lettres l'une après l'autre. Les directions haut et bas impliquent un arrangement des lettres l'une sous l'autre.</p>|
|Macross|―| |Permet de charger une séquence de commandes PCL en mémoire et d'utiliser cette séquence plusieurs fois, par exemple, pour imprimer l'en-tête de page ou définir un formatage pour un ensemble de pages.|
|Unicode text|―| |Permet d'imprimer des caractères non-ASCII.  Non implémenté en raison de l'absence de fichiers d'exemple avec <br>texte Unicode|
|PCL6 (PCL-XL)| |Réalisé uniquement dans la version Beta en raison de l'absence de fichiers de test. Les polices intégrées ne sont pas non plus prises en charge. L'extension JetReady n'est pas prise en charge car il est impossible d'avoir la spécification JetReady.|Format de fichier binaire.|

### Conversion d'un fichier PCL en format PDF

Pour permettre la conversion de PCL en PDF, [Aspose.PDF pour Java](https://products.aspose.com/pdf/java) dispose de la classe [PclLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PclLoadOptions) qui est utilisée pour initialiser l'objet [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Cet objet est ensuite passé en argument lors de l'initialisation de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) et aide le moteur de rendu PDF à déterminer le format d'entrée du document source.

Le code suivant montre le processus de conversion d'un fichier PCL en format PDF.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPCLtoPDF {

    private ConvertPCLtoPDF() {
        
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {        
        ConvertPCLtoPDF_Simple();
        ConvertPCLtoPDF_Advanced();
    }

    public static void ConvertPCLtoPDF_Simple() {
        PclLoadOptions options = new PclLoadOptions();
        Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
        pdfDocument.save(_dataDir + "epub_test.pdf");        
    }

    public static void ConvertPCLtoPDF_Advanced() {
        PclLoadOptions options = new PclLoadOptions();
        options.SupressErrors=true;
        Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
        if (options.Exceptions!=null)
            for (Exception ex : options.Exceptions)
            {
                System.out.println(ex.getMessage());
            }
        pdfDocument.save(_dataDir + "pcl_test.pdf");        
    }
}
```

### Problèmes Connus

1. L'origine des chaînes de texte et des images peut légèrement différer de celles d'un fichier PCL source si la direction d'impression n'est pas de 0º. Il en va de même pour les images vectorielles si le système de coordonnées du tracé vectoriel est tourné (commande RO précédée).
2. L'origine des étiquettes dans les images vectorielles peut différer de celles d'un fichier PCL source si les étiquettes sont influencées par une séquence de commandes : Origine de l'étiquette (LO), Définir le chemin du texte variable (DV), Direction absolue (DI) ou Direction relative (DR).
3. Un texte peut être lu incorrectement s'il doit être rendu avec une police Bitmap ou TrueType (intégrée), car actuellement ces polices ne sont que partiellement prises en charge (voir exceptions dans le "tableau des fonctionnalités prises en charge"). Dans cette situation, le texte peut être correctement lu uniquement si les codes des caractères dans une police intégrée correspondent à ceux par défaut. Le style du texte lu peut également différer de celui du fichier PCL source car il n'est pas nécessaire de définir le style dans l'en-tête de la police intégrée.

1. Si le fichier PCL analysé contient des polices Intellifont ou Universal soft, une exception sera levée, car les polices Intellifont et Universal ne sont pas prises en charge du tout.
1. Si le fichier PCL analysé contient des commandes de macros, le résultat de l'analyse différera fortement du fichier source, car les commandes de macros ne sont pas prises en charge.

## Convertir du texte en PDF

**Aspose.PDF pour Java** offre la possibilité de convertir des fichiers texte au format PDF. Dans cet article, nous démontrons avec quelle facilité et efficacité nous pouvons convertir un fichier texte en PDF à l'aide d'Aspose.PDF.

Lorsque vous avez besoin de convertir un fichier texte en PDF, lisez initialement le fichier texte source dans un lecteur. Nous avons utilisé StringBuilder pour lire le contenu du fichier texte. Instanciez un objet Document et ajoutez une nouvelle page dans la collection Pages. Créez un nouvel objet TextFragment et passez l'objet StringBuilder à son constructeur. Ajoutez un nouveau paragraphe dans la collection Paragraphs à l'aide de l'objet TextFragment et enregistrez le fichier PDF résultant à l'aide de la méthode Save de la classe Document.

{{% alert color="success" %}}
**Essayez de convertir du TEXTE en PDF en ligne**

Aspose.PDF pour Java vous présente l'application en ligne gratuite ["Texte en PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Conversion Aspose.PDF TEXTE en PDF avec l'application gratuite](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

### Convertir un fichier texte brut en PDF

```java
package com.aspose.pdf.examples;
/**
 * Convertir TXT en PDF
 */

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertTextToPDF {

    private ConvertTextToPDF() {
    }

    final static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");
    final static Charset ENCODING = StandardCharsets.UTF_8;

    public static void main(String[] args) throws IOException {
        ConvertTXT_to_PDF_Simple();
    }

    public static void ConvertTXT_to_PDF_Simple() throws IOException {
        // Initialiser l'objet document

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        Path txtDocumentFileName = Paths.get(_dataDir.toString(), "rfc822.txt");

        // Instancier un objet Document en appelant son constructeur vide
        Document pdfDocument = new Document();

        // Ajouter une nouvelle page dans la collection Pages du Document
        Page page = pdfDocument.getPages().add();

        // Créer une instance de TextFragment et passer le texte de l'objet lecteur à son
        // constructeur en tant qu'argument
        TextFragment text = new TextFragment(Files.readString(txtDocumentFileName, ENCODING));

        // Ajouter un nouveau paragraphe de texte dans la collection de paragraphes et passer l'objet TextFragment
        page.getParagraphs().add(text);

        // Enregistrer le fichier PDF résultant
        pdfDocument.save(pdfDocumentFileName);
    }
```


### Convertir un fichier texte pré-formaté en PDF

```java
    public static void ConvertPreFormattedTextToPdf() throws IOException {

        Path txtDocumentFileName = Paths.get(_dataDir.toString(), "rfc822.txt");
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();

        // Lire le fichier texte comme un tableau de chaînes
        java.util.List<String> lines = Files.readAllLines(txtDocumentFileName, ENCODING);

        // Instancier un objet Document en appelant son constructeur vide
        Document pdfDocument = new Document();

        // Ajouter une nouvelle page dans la collection Pages du Document
        Page page = pdfDocument.getPages().add();

        // Définir les marges gauche et droite pour une meilleure présentation
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        for (String line : lines) {
            // vérifier si la ligne contient le caractère "saut de page"
            // voir https://en.wikipedia.org/wiki/Page_break
            if (line.startsWith("\f")) {
                page = pdfDocument.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
                page.getPageInfo().getDefaultTextState().setFontSize(12);
            } else {
                // Créer une instance de TextFragment et
                // passer la ligne à son
                // constructeur en tant qu'argument
                TextFragment text = new TextFragment(line);

                // Ajouter un nouveau paragraphe de texte dans la collection de paragraphes et passer l'objet TextFragment
                page.getParagraphs().add(text);
            }

            pdfDocument.save(pdfDocumentFileName);
        }
    }
}
```


## Convertir XPS en PDF

**Aspose.PDF pour Java** prend en charge la conversion des fichiers <abbr title="XML Paper Specification">XPS</abbr> au format PDF. Consultez cet article pour résoudre vos tâches.

XPS, XML Paper Specification, est un format de fichier Microsoft utilisé pour intégrer la création et la visualisation de documents dans Windows. Avec Aspose.PDF pour Java, il est possible de convertir des fichiers XPS en PDF, le format de fichier portable d'Adobe.

Le format de fichier est essentiellement un fichier XML compressé, principalement utilisé pour la distribution et le stockage. Il est très difficile à éditer et principalement implémenté par Microsoft.

Pour convertir un fichier XPS en PDF à l'aide de [Aspose.PDF pour Java](https://products.aspose.com/pdf/java), utilisez la classe [XpsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsLoadOptions).
 Cela est utilisé pour initialiser un objet [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Plus tard, cet objet est passé en tant qu'argument lors de l'initialisation de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) et aide le moteur de rendu PDF à déterminer le format d'entrée du document source.

Dans XP et Windows 7, vous devriez trouver une imprimante XPS préinstallée si vous regardez dans le Panneau de configuration, puis Imprimantes. Pour créer des fichiers XPS, vous pouvez utiliser cette imprimante comme périphérique de sortie. Dans Windows 7, vous devriez pouvoir simplement double-cliquer sur le fichier pour l'ouvrir dans un visualiseur XPS. Vous pouvez également télécharger le [visualiseur XPS](http://windows.microsoft.com/en-US/windows-vista/what-is-the-xps-viewer) depuis le site Web de Microsoft.

Le snippet de code suivant montre le processus de conversion du fichier XPS au format PDF.

```java
public final class ConvertXPStoPDF {

    private ConvertXPStoPDF() {
    }

    final static Path _dataDir = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {
        Convert_XSLFO_to_PDF();
    }

    public static void Convert_XSLFO_to_PDF() throws IOException {
        // Initialiser l'objet document

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        String xpsDocumentFileName = Paths.get(_dataDir.toString(), "demo.xml").toString();

        // Instancier un objet LoadOption en utilisant l'option de chargement XPS
        LoadOptions options = new XpsLoadOptions();

        // Instancier un objet Document en appelant son constructeur vide
        Document pdfDocument = new Document(xpsDocumentFileName, options);

        // Sauvegarder le fichier PDF résultant
        pdfDocument.save(pdfDocumentFileName);
    }
}
```

{{% alert color="success" %}}
**Essayez de convertir le format XPS en PDF en ligne**

Aspose.PDF pour Java vous présente l'application en ligne gratuite ["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion XPS en PDF avec application gratuite](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## Convertir PostScript en PDF

**Aspose.PDF pour Java** prend en charge les fonctionnalités de conversion des fichiers PostScript en format PDF. L'une des fonctionnalités d'Aspose.PDF est que vous pouvez définir un ensemble de dossiers de polices à utiliser lors de la conversion.

Afin de convertir un fichier PostScript en format PDF, Aspose.PDF pour Java propose la classe [PsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PsLoadOptions) qui est utilisée pour initialiser l'objet LoadOptions. Ensuite, cet objet peut être passé en argument au constructeur de l'objet Document, ce qui aidera le moteur de rendu PDF à déterminer le format du document source.


Le code ci-dessous peut être utilisé pour convertir un fichier PostScript en format PDF :

```java
public static void ConvertPostScriptToPDF_Simple(){
        // Initialiser l'objet document

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo.pdf").toString();
        String psDocumentFileName = Paths.get(_dataDir.toString(), "demo.ps").toString();
        PsLoadOptions options = new PsLoadOptions();

        // Créer l'objet Document
        Document document = new Document(psDocumentFileName, options);

        // Enregistrer le document PDF de sortie
        document.save(pdfDocumentFileName);
    }
```

De plus, vous pouvez définir un ensemble de dossiers de polices qui seront utilisés lors de la conversion :

```java
public static void ConvertPostscriptToPDFAvdanced() {
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo.pdf").toString();
        String psDocumentFileName = Paths.get(_dataDir.toString(), "demo.ps").toString();
        PsLoadOptions options = new PsLoadOptions();
        
        options.setFontsFolders(new String[] { "c:\tmp\fonts1", "c:\tmp\fonts2" });

        // Créer l'objet Document
        Document document = new Document(psDocumentFileName, options);

        // Enregistrer le document PDF de sortie
        document.save(pdfDocumentFileName);
    }
```


## Convertir XML en PDF

Le format XML est utilisé pour stocker des données structurées. Il existe plusieurs façons de convertir <abbr title="Extensible Markup Language">XML</abbr> en PDF dans Aspose.PDF.

{{% alert color="success" %}}
**Essayez de convertir XML en PDF en ligne**

Aspose.PDF pour Java vous propose une application gratuite en ligne ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), où vous pouvez essayer d'explorer la fonctionnalité et la qualité du travail.

[![Aspose.PDF Conversion XML en PDF avec Application Gratuite](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

Considérez l'option d'utilisation d'un document XML basé sur la norme XSL-FO.

### Convertir XSL-FO en PDF

La conversion de fichiers XSL-FO en PDF peut être réalisée en utilisant l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) avec [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions).

```java
package com.aspose.pdf.examples;
/**
 * Convertir XML en PDF
 */

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertXMLtoPDF {

    private ConvertXMLtoPDF() {
    }

    final static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");
    public static void main(String[] args) throws IOException {
        Convert_XSLFO_to_PDF();
        Convert_XSLFO_to_PDF_Adv();
    }

    public static void Convert_XSLFO_to_PDF() throws IOException {
        // Initialiser l'objet document

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        String xmlDocumentFileName = Paths.get(_dataDir.toString(), "demo.xml").toString();
        String xsltDocumentFileName = Paths.get(_dataDir.toString(), "employees.xslt").toString();

        XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);

        // Instancier un objet Document en appelant son constructeur vide
        Document pdfDocument = new Document(xmlDocumentFileName, options);

        // Enregistrer le fichier PDF résultant
        pdfDocument.save(pdfDocumentFileName);
    }
}
```


### Convertir XSL-FO en PDF avec une stratégie de gestion des erreurs définie

```java
// Initialiser l'objet document

String documentFileName = Paths.get(DATA_DIR.toString(), "demo_txt.pdf").toString();
String xmlDocumentFileName = Paths.get(DATA_DIR.toString(), "demo.xml").toString();
String xsltDocumentFileName = Paths.get(DATA_DIR.toString(), "employees.xslt").toString();

XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);

// Définir la stratégie de gestion des erreurs
options.setParsingErrorsHandlingType(XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately);

// Instancier un objet Document en appelant son constructeur vide
Document document = new Document(xmlDocumentFileName, options);

// Enregistrer le fichier PDF résultant
document.save(documentFileName);
document.close();
```

## Convertir LaTeX/TeX en PDF

Le format de fichier LaTeX est un format de fichier texte avec un balisage dans le dérivé LaTeX de la famille de langages TeX et LaTeX est un format dérivé du système TeX.
 LaTeX (ˈleɪtɛk/ lay-tek ou lah-tek) est un système de préparation de documents et un langage de balisage de documents. Il est largement utilisé pour la communication et la publication de documents scientifiques dans de nombreux domaines, y compris les mathématiques, la physique et l'informatique. Il joue également un rôle important dans la préparation et la publication de livres et d'articles contenant des matériaux multilingues complexes, tels que le sanskrit et l'arabe, y compris les éditions critiques. LaTeX utilise le programme de composition TeX pour formater sa sortie et est lui-même écrit dans le langage macro TeX.

**Aspose.PDF for Java** prend en charge la fonctionnalité de convertir des fichiers TeX au format PDF et pour accomplir cette exigence, le package com.aspose.pdf a une classe nommée [LatexLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LatexLoadOptions) qui fournit les capacités de charger des fichiers LaTex et de rendre la sortie au format PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document). Le code suivant montre le processus de conversion d'un fichier LaTeX au format PDF.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertLATEXtoPDF {

    private ConvertLATEXtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Instancier l'objet option de chargement Latex
        TeXLoadOptions options = new TeXLoadOptions();
        
        // Créer un objet Document
        String latexFileName = Paths.get(_dataDir.toString(), "samplefile.tex").toString();
        Document document = new Document(latexFileName, options);

        // Enregistrer le document PDF de sortie
        document.save(Paths.get(_dataDir.toString(),"TEXtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**Essayez de convertir LaTeX/TeX en PDF en ligne**

Aspose.PDF pour Java vous propose une application gratuite en ligne ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.
[![Aspose.PDF Conversion LaTeX/TeX en PDF avec une application gratuite](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}