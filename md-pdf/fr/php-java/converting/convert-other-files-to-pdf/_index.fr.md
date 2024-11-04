---
title: Convertir divers formats de fichiers en PDF 
linktitle: Convertir d'autres formats de fichiers en PDF 
type: docs
weight: 80
url: /php-java/convert-other-files-to-pdf/
lastmod: "2024-05-20"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir d'autres formats de fichiers en document PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Convertir EPUB en PDF

**Aspose.PDF pour PHP** vous permet de convertir simplement des fichiers EPUB en format PDF.

<abbr title="publication électronique">EPUB</abbr> est une norme de livre électronique libre et ouverte de l'International Digital Publishing Forum (IDPF). Les fichiers ont l'extension .epub. EPUB est conçu pour un contenu reformatable, ce qui signifie qu'un lecteur EPUB peut optimiser le texte pour un périphérique d'affichage particulier.

Pour convertir des fichiers EPUB en format PDF, Aspose.PDF pour PHP dispose d'une classe nommée [EpubLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubLoadOptions) qui est utilisée pour charger le fichier EPUB source.
 Après cela, l'objet est passé comme argument à l'initialisation de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document), car il aide le moteur de rendu PDF à déterminer le format d'entrée du document source.

Le code suivant montre le processus de conversion d'un fichier EPUB en format PDF.

1. Créez une [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubloadoptions/) EPUB.
2. Initialisez l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document).
3. Enregistrez le document PDF de sortie.

```php
// Créez une nouvelle instance de EpubLoadOptions
$loadOption = new EpubLoadOptions();

// Créez un nouvel objet Document et chargez le fichier EPUB
$document = new Document($inputFile, $loadOption);

// Enregistrez le document en tant que fichier PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**Essayez de convertir EPUB en PDF en ligne**

Aspose.PDF pour PHP vous propose une application en ligne gratuite ["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.
[![Aspose.PDF Conversion EPUB en PDF avec Application Gratuite](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## Convertir Markdown en PDF

{{% alert color="success" %}}
**Essayez de convertir Markdown en PDF en ligne**

Aspose.PDF pour PHP vous présente l'application gratuite en ligne ["Markdown en PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion Markdown en PDF avec Application Gratuite](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Markdown est un outil de conversion de texte en HTML pour les auteurs web. Markdown vous permet d'écrire dans un format de texte brut facile à lire et à écrire, puis de le convertir en XHTML (ou HTML) structurellement valide.

L'extrait de code suivant montre comment utiliser cette fonctionnalité avec Aspose.PDF pour PHP :

```php
// Créez une nouvelle instance de MdLoadOptions
$loadOption = new MdLoadOptions();

// Créez une nouvelle instance de Document et chargez le fichier Markdown d'entrée
$document = new Document($inputFile, $loadOption);

// Enregistrez le document en tant que fichier PDF
$document->save($outputFile);
```


## Convertir PCL en PDF

<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language) est un langage d'imprimante Hewlett-Packard développé pour accéder aux fonctionnalités standard des imprimantes. Les niveaux PCL 1 à 5e/5c sont des langages basés sur des commandes qui utilisent des séquences de contrôle traitées et interprétées dans l'ordre de réception. Au niveau consommateur, les flux de données PCL sont générés par un pilote d'impression. La sortie PCL peut également être facilement générée par des applications personnalisées.

{{% alert color="success" %}}
**Essayez de convertir PCL en PDF en ligne**

Aspose.PDF pour PHP vous propose une application en ligne gratuite ["PCL to PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PCL en PDF avec une application gratuite](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**Actuellement, seules les versions PCL5 et antérieures sont prises en charge.**

|**Ensembles de Commandes**|**Support**|**Exceptions**|**Description**|

| :- | :- | :- | :- |
|Commandes de contrôle de travail|+|Mode d'impression recto verso|Contrôler le processus d'impression : nombre de copies, bac de sortie, impression recto/verso, marges de gauche et en haut, etc.|
|Commandes de contrôle de page|+|Commande de saut de perforation|Spécifier la taille de la page, les marges, l'orientation de la page, les interlignes, les distances entre caractères, etc.|
|Commandes de positionnement du curseur|+| |Spécifier la position du curseur et, par conséquent, les origines du texte, des images raster ou vectorielles et des détails.|

|Commandes de sélection de police|+|<p>1. Commande de données d'impression transparente.</p><p>2. Polices intégrées. Dans la version actuelle, au lieu de créer une police intégrée, notre bibliothèque sélectionne une police appropriée à partir des polices TrueType "dures" existantes installées sur une machine cible. <br>   L'adéquation est définie par le ratio largeur/hauteur. <br>   Cette fonctionnalité fonctionne uniquement pour les polices Bitmap et TrueType et ne garantit pas que le texte imprimé avec une police intégrée sera pertinent par rapport à celui dans le fichier source. <br>   Parce que les codes de caractères dans la police intégrée peuvent ne pas correspondre aux codes par défaut.</p><p>3. Jeux de symboles définis par l'utilisateur.</p>|Permet le chargement de polices intégrées depuis le fichier PCL et leur gestion en mémoire.|
|Commandes graphiques raster|+|Seulement noir et blanc|Permet le chargement d'images raster depuis le fichier PCL en mémoire, spécifie les paramètres raster <br> tels que la largeur, la hauteur, le type de compression, la résolution, etc.|
|Commandes de couleur|+| |Permet la coloration de tous les objets imprimables.|
|Commandes de modèle d'impression|+| |Permet de remplir le texte, les images raster et les zones rectangulaires avec des motifs raster prédéfinis et définis par l'utilisateur, spécifie le mode de transparence pour les motifs et l'image raster source.|
 <br>Les motifs prédéfinis sont le hachurage, le croisement de hachures et les motifs d'ombrage.|
|Commandes de remplissage de zone rectangulaire|+| |Permet la création et le remplissage de zones rectangulaires avec des motifs.|
|Commandes graphiques vectorielles HP-GL/2|+|Les commandes de vecteur criblé (SV), de mode de transparence (TR), de données transparentes (TD), RO (Rotation du système de coordonnées), de polices évolutives ou bitmap (SB), d'inclinaison de caractères (SL) et d'espace supplémentaire (ES) ne sont pas implémentées et les commandes DV (Définir le chemin de texte variable) sont réalisées en version bêta.|<p>- Permet le chargement d'images vectorielles HP-GL/2 depuis le fichier PCL en mémoire. Vector image a une origine dans le coin inférieur gauche de la zone imprimable, peut être mise à l'échelle, translatée, tournée et découpée.</p><p>- Une image vectorielle peut contenir du texte, comme des étiquettes, et des figures géométriques telles que rectangle, cercle, ellipse, ligne, arc, courbe de Bézier et figures complexes composées des simples.</p><p>- Les figures fermées, y compris les lettres des étiquettes, peuvent être remplies avec un remplissage solide ou un motif vectoriel.</p><p>- Le motif peut être un hachurage, un hachurage croisé, un ombrage, un motif défini par l'utilisateur, un hachurage PCL ou un hachurage croisé et un motif défini par l'utilisateur PCL. Les motifs PCL sont des trames. Les étiquettes peuvent être individuellement tournées, mises à l'échelle et orientées dans quatre directions : haut, bas, gauche et droite. Les directions gauche et droite impliquent un agencement de lettres les unes après les autres. Les directions haut et bas impliquent un agencement de lettres les unes sous les autres.</p>|
|Macross|―| |Permet de charger une séquence de commandes PCL en mémoire et d'utiliser cette séquence plusieurs fois, par exemple, pour imprimer l'en-tête de page ou définir un formatage pour un ensemble de pages.|
|Unicode text|―| |Permet d'imprimer des caractères non-ASCII. Non implémenté en raison de l'absence de fichiers d'exemple avec texte Unicode.  
|PCL6 (PCL-XL)| |Réalisé uniquement dans la version bêta en raison du manque de fichiers de test. Les polices embarquées ne sont pas non plus prises en charge. L'extension JetReady n'est pas prise en charge car il est impossible d'avoir la spécification JetReady.|Format de fichier binaire.|

### Conversion d'un fichier PCL en format PDF

Pour permettre la conversion de PCL en PDF, [Aspose.PDF pour PHP](https://products.aspose.com/pdf/php-java) possède la classe [PclLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PclLoadOptions) qui est utilisée pour initialiser l'objet [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Cet objet est ensuite passé comme argument lors de l'initialisation de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) et aide le moteur de rendu PDF à déterminer le format d'entrée du document source.

L'extrait de code suivant montre le processus de conversion d'un fichier PCL en format PDF.

```php
// Créez une nouvelle instance de PclLoadOptions
$loadOption = new PclLoadOptions();

// Créez une nouvelle instance de Document et chargez le fichier PCL
$document = new Document($inputFile, $loadOption);

// Enregistrez le document sous forme de fichier PDF
$document->save($outputFile);
```

### Problèmes Connus

1. L'origine des chaînes de texte et des images peut légèrement différer de celles d'un fichier PCL source si la direction d'impression n'est pas de 0º. Il en va de même pour les images vectorielles si le système de coordonnées du tracé vectoriel est tourné (commande RO précédée).
2. L'origine des étiquettes dans les images vectorielles peut différer de celles d'un fichier PCL source si les étiquettes sont influencées par une séquence de commandes : Origine de l'étiquette (LO), Définir le chemin du texte variable (DV), Direction Absolue (DI) ou Direction Relative (DR).
3. Un texte peut être incorrectement lu s'il doit être rendu avec une police Bitmap ou TrueType (intégrée), car actuellement ces polices ne sont que partiellement prises en charge (voir exceptions dans le "tableau des fonctionnalités supportées"). Dans cette situation, le texte ne peut être correctement lu que si les codes de caractères dans une police intégrée correspondent aux codes par défaut. Le style du texte lu peut également différer de celui du fichier PCL source car il n'est pas nécessaire de définir le style dans l'en-tête de la police intégrée.

1. Si le fichier PCL analysé contient des polices Intellifont ou des polices logicielles universelles, une exception sera levée, car les polices Intellifont et universelles ne sont pas du tout prises en charge.
1. Si le fichier PCL analysé contient des commandes de macros, le résultat de l'analyse différera fortement du fichier source, car les commandes de macros ne sont pas prises en charge.

## Convertir du texte en PDF

**Aspose.PDF pour PHP** offre la possibilité de convertir des fichiers texte en format PDF. Dans cet article, nous démontrons à quel point nous pouvons facilement et efficacement convertir un fichier texte en PDF en utilisant Aspose.PDF.

Lorsque vous avez besoin de convertir un fichier texte en PDF, commencez par lire le fichier texte source dans un lecteur. Nous avons utilisé StringBuilder pour lire le contenu du fichier texte. Instanciez un objet Document et ajoutez une nouvelle page dans la collection Pages. Créez un nouvel objet TextFragment et passez l'objet StringBuilder à son constructeur. Ajoutez un nouveau paragraphe dans la collection Paragraphes en utilisant l'objet TextFragment et enregistrez le fichier PDF résultant en utilisant la méthode Save de la classe Document.
**Essayez de convertir le TEXTE en PDF en ligne**

Aspose.PDF pour PHP vous présente l'application en ligne gratuite ["Texte en PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.
{{% alert color="primary" %}}

[![Conversion Aspose.PDF TEXTE en PDF avec application gratuite](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

### Convertir un fichier texte brut en PDF

```php
// Créez un nouvel objet Document.
$document = new Document();

// Ajoutez une nouvelle page au document.
$page = $document->getPages()->add();

// Lisez le contenu du fichier texte d'entrée.
$text = file_get_contents($inputFile);

// Créez un nouvel objet FontRepository.
$fontRepository = new FontRepository();

// Trouvez la police "Courier" dans le dépôt.
$font = $fontRepository->findFont("Courier");

// Créez un nouvel objet TextFragment avec le texte d'entrée.
$textFragment = new TextFragment($text);

// Définissez la police du fragment de texte à "Courier".
$textFragment->getTextState()->setFont($font);

// Ajoutez le fragment de texte à la page.
$page->getParagraphs()->add($textFragment);

// Enregistrez le document dans le fichier de sortie.
$document->save($outputFile);
```


## Convertir XPS en PDF

**Aspose.PDF pour PHP** prend en charge la conversion des fichiers <abbr title="XML Paper Specification">XPS</abbr> au format PDF. Consultez cet article pour résoudre vos tâches.

XPS, XML Paper Specification, est un format de fichier Microsoft utilisé pour intégrer la création et la visualisation de documents dans Windows. Avec Aspose.PDF pour PHP, il est possible de convertir des fichiers XPS en PDF, le format de fichier portable d'Adobe.

Le format de fichier est essentiellement un fichier XML compressé, principalement utilisé pour la distribution et le stockage. Il est très difficile à éditer et principalement implémenté par Microsoft.

Pour convertir un fichier XPS en PDF en utilisant [Aspose.PDF pour PHP](https://products.aspose.com/pdf/php-java), utilisez la classe [XpsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsLoadOptions).
 Ceci est utilisé pour initialiser un objet [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Plus tard, cet objet est passé en tant qu'argument lors de l'initialisation de l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) et aide le moteur de rendu PDF à déterminer le format d'entrée du document source.

Le code suivant montre le processus de conversion du fichier XPS en format PDF.

```php
// Créer une nouvelle instance de la classe XpsLoadOptions
$loadOption = new XpsLoadOptions();

// Créer une nouvelle instance de la classe Document et charger le fichier XPS
$document = new Document($inputFile, $loadOption);

// Enregistrer le document en tant que fichier PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**Essayez de convertir le format XPS en PDF en ligne**

Aspose.PDF pour PHP vous présente une application en ligne gratuite ["XPS to PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), où vous pouvez essayer d'explorer la fonctionnalité et la qualité avec lesquelles elle fonctionne.


[![Aspose.PDF Conversion XPS en PDF avec une application gratuite](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/){{% /alert %}}

## Convertir PostScript en PDF

**Aspose.PDF pour PHP** prend en charge les fonctionnalités de conversion des fichiers PostScript au format PDF. L'une des fonctionnalités d'Aspose.PDF est que vous pouvez définir un ensemble de dossiers de polices à utiliser pendant la conversion.

Afin de convertir un fichier PostScript au format PDF, Aspose.PDF pour PHP offre la classe [PsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PsLoadOptions) qui est utilisée pour initialiser l'objet LoadOptions. Plus tard, cet objet peut être passé comme argument au constructeur de l'objet Document, ce qui aidera le moteur de rendu PDF à déterminer le format du document source.

Le code suivant peut être utilisé pour convertir un fichier PostScript en format PDF :

```php
// Créer un nouvel objet PsLoadOptions.
$loadOption = new PsLoadOptions();

// Créer un nouvel objet Document et charger le fichier PS d'entrée.
$document = new Document($inputFile, $loadOption);

// Enregistrer le document en tant que fichier PDF.
$document->save($outputFile);
```

## Convertir XML en PDF

Le format XML est utilisé pour stocker des données structurées.
 Il existe plusieurs façons de convertir <abbr title="Extensible Markup Language">XML</abbr> en PDF dans Aspose.PDF.

{{% alert color="success" %}}
**Essayez de convertir XML en PDF en ligne**

Aspose.PDF pour PHP vous présente une application gratuite en ligne ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion XML to PDF with Free App](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

Considérez l'option d'utilisation d'un document XML basé sur la norme XSL-FO.

### Convertir XSL-FO en PDF

La conversion des fichiers XSL-FO en PDF peut être mise en œuvre en utilisant l'objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) avec [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions).

```php
// Définir le chemin vers les fichiers d'exemple
$dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";
$inputFoFile = $dataDir . DIRECTORY_SEPARATOR . "sample.xslt";
$inputFile = $dataDir . DIRECTORY_SEPARATOR . "sample.xml";
$outputFile = $dataDir . DIRECTORY_SEPARATOR . "results" . DIRECTORY_SEPARATOR . 'result-xmlfo-to-pdf.pdf';

// Créer une nouvelle instance de la classe XslFoLoadOptions et passer le chemin du fichier XSL-FO en entrée
$loadOption = new XslFoLoadOptions($inputFoFile);

// Créer une nouvelle instance de la classe Document et passer le fichier XML en entrée et les options de chargement XSL-FO
$document = new Document($inputFile, $loadOption);

// Enregistrer le document PDF converti dans le chemin du fichier de sortie
$document->save($outputFile);
```

## Convertir LaTeX/TeX en PDF

Le format de fichier LaTeX est un format de fichier texte avec balisage dans le dérivé LaTeX de la famille de langues TeX, et LaTeX est un format dérivé du système TeX. LaTeX (ˈleɪtɛk/ lay-tek ou lah-tek) est un système de préparation de documents et un langage de balisage de documents. Il est largement utilisé pour la communication et la publication de documents scientifiques dans de nombreux domaines, y compris les mathématiques, la physique et l'informatique. Il joue également un rôle important dans la préparation et la publication de livres et d'articles contenant des matériaux multilingues complexes, tels que le sanskrit et l'arabe, y compris les éditions critiques. LaTeX utilise le programme de composition TeX pour formater sa sortie et est lui-même écrit dans le langage macro TeX.

**Aspose.PDF for PHP** prend en charge la fonctionnalité de conversion des fichiers TeX au format PDF et pour répondre à cette exigence, le package com.aspose.pdf dispose d'une classe nommée [LatexLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LatexLoadOptions) qui fournit les capacités de charger des fichiers LaTex et de rendre la sortie au format PDF en utilisant la classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document).
 Le snippet de code suivant montre le processus de conversion d'un fichier LaTeX au format PDF.

```php
// Créer une nouvelle instance de la classe LatexLoadOptions
$loadOption = new LatexLoadOptions();

// Créer une nouvelle instance de la classe Document et charger le fichier TeX en utilisant les TeXLoadOptions
$document = new Document($inputFile, $loadOption);

// Enregistrer le document en tant que fichier PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**Essayez de convertir LaTeX/TeX en PDF en ligne**

Aspose.PDF pour PHP vous présente une application en ligne gratuite ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), où vous pouvez essayer d'examiner la fonctionnalité et la qualité avec lesquelles elle fonctionne.

[![Conversion Aspose.PDF LaTeX/TeX en PDF avec l'application gratuite](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}