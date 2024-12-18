---
title: PdfFileMend Class
type: docs
weight: 20
url: /fr/java/pdffilemend-class/
description: Cette section explique comment travailler avec Aspose.PDF Facades en utilisant la classe PdfFileMend.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Il ne semblerait pas difficile d'insérer [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) dans un document PDF, à condition que vous ayez la version éditable originale de ce document. Supposons que vous ayez créé un document, puis que vous vous souveniez que vous devez ajouter une autre ligne ou que nous parlons d'un plus grand volume de documents, dans les deux cas, Aspose.PDF Facades vous aidera. Considérons la possibilité d'ajouter du texte dans un fichier PDF existant avec la classe [PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend).

## Ajouter du texte dans un fichier PDF existant (facades)

Nous pouvons ajouter du texte de plusieurs manières.
 Considérez le premier. Nous prenons le [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) et l'ajoutons à la Page. Ensuite, nous indiquons les coordonnées du coin inférieur gauche, puis nous ajoutons notre texte à la Page.

```java
    public static void AddText01()
    {
        PdfFileMend mender = new PdfFileMend();
        mender.BindPdf(_dataDir + "sample.pdf");
        FormattedText message = new FormattedText("Bienvenue chez Aspose !");

        mender.AddText(message, 1, 10, 750);

        // enregistrer le fichier de sortie
        mender.Save(_dataDir + "PdfFileMend01_output.pdf");
    }
```

Vérifiez à quoi cela ressemble :

![Ajouter du texte](/pdf/fr/net/images/add_text.png)

La deuxième façon d'ajouter [FormattedText](https://reference.aspose.com/pdf//java/com.aspose.pdf.facades/formattedtext). De plus, nous indiquons un rectangle dans lequel notre texte doit s'insérer.

```java
public static void AddText02()
    {
        PdfFileMend mender = new PdfFileMend();
        mender.BindPdf(_dataDir + "sample.pdf");
        FormattedText message = new FormattedText("Bienvenue chez Aspose ! Bienvenue chez Aspose !");

        mender.AddText(message, 1, 10, 700, 55, 810);
        mender.WrapMode = WordWrapMode.ByWords;

        // enregistrer le fichier de sortie
        mender.Save(_dataDir + "PdfFileMend02_output.pdf");
    }
```

Le troisième exemple offre la possibilité d'ajouter du texte à des pages spécifiées. Dans notre exemple, ajoutons une légende sur les pages 1 et 3 du document.

```java
public static void AddText03()
    {
        Document document = new Document(_dataDir + "sample.pdf");
        document.Pages.Add();
        document.Pages.Add();
        document.Pages.Add();
        PdfFileMend mender = new PdfFileMend();
        mender.BindPdf(document);
        FormattedText message = new FormattedText("Bienvenue chez Aspose!");
        int[] pageNums = new int[] { 1, 3 };
        mender.AddText(message, pageNums, 10, 750, 310, 760);

        // enregistrer le fichier de sortie
        mender.Save(_dataDir + "PdfFileMend03_output.pdf");
    }
```

## Ajouter une image dans un fichier PDF existant (facades)

Avez-vous déjà essayé d'ajouter une image à un fichier PDF existant ?
 Nous sommes sûrs que vous savez que ce n'est pas une tâche facile. Peut-être remplissez-vous un formulaire en ligne et devez-vous joindre une photo pour identification ou joindre votre photo à un CV existant. Auparavant, une telle tâche était résolue en créant une photo, en l'attachant à un document, en la scannant et en l'envoyant. Ce processus était très compliqué et prenait beaucoup de temps.

Ajouter des images et du texte dans un fichier PDF existant est une exigence courante et le namespace com.aspose.pdf.facades répond très bien à cette exigence. Il fournit une classe [PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend) qui vous permet d'ajouter des images dans le fichier PDF.

Cet article vous montrera comment insérer une image dans un PDF en utilisant com.aspose.pdf.facades. Il existe également plusieurs options pour ajouter des images au PDF.

Insérer une image dans le document PDF en définissant les paramètres du rectangle.

```java
public static void AddImage01()
    {
        Document document = new Document(_dataDir + "sample.pdf");
        PdfFileMend mender = new PdfFileMend();

        // Charger l'image dans le flux
        var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
        mender.BindPdf(document);
        mender.AddImage(imageStream, 1, 10, 650, 110, 750);

        // enregistrer le fichier de sortie
        mender.Save(_dataDir + "PdfFileMend04_output.pdf");
    }
```

![Ajouter une image](/pdf/fr/net/images/add_image1.png)

Considérons le deuxième extrait de code. En utilisant des variations des paramètres de la classe [CompositingParameters](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters), nous pouvons obtenir différents effets de conception. Nous avons essayé l'un d'eux.

```java
 public static void AddImage02()
    {
        Document document = new Document(_dataDir + "sample_color.pdf");
        PdfFileMend mender = new PdfFileMend();
        // Charger l'image dans le flux
        var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
        mender.BindPdf(document);
        int pageNum = 1;
        int lowerLeftX = 10;
        int lowerLeftY = 650;
        int upperRightX = 110;
        int upperRightY = 750;
        CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply);
        mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

        // enregistrer le fichier de sortie
        mender.Save(_dataDir + "PdfFileMend05_output.pdf");
    }
```


![Add Image](/pdf/fr/net/images/add_image2.png)

Dans le code suivant, nous utilisons [ImageFilterType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageFilterType). ImageFilterType indique le type de codec de flux qui sera utilisé pour l'encodage, par défaut Jpeg. Si vous chargez une image depuis le format PNG, elle sera alors enregistrée dans le document en tant que JPEG (ou dans un autre format que j'ai spécifié).

```java
    public static void AddImage03()
    {
        Document document = new Document(_dataDir + "sample_color.pdf");
        PdfFileMend mender = new PdfFileMend();
        // Charger l'image dans le flux
        var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
        mender.BindPdf(document);
        int pageNum = 1;
        int lowerLeftX = 10;
        int lowerLeftY = 650;
        int upperRightX = 110;
        int upperRightY = 750;
        CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Exclusion, ImageFilterType.Flate);
        mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

        // enregistrer le fichier de sortie
        mender.Save(_dataDir + "PdfFileMend06_output.pdf");
    }
```


Dans le prochain extrait de code, vous pouvez noter l'utilisation de la méthode [IsMasked](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters#isMasked--).

[IsMasked](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters#isMasked--) est un indicateur, qui indique s'il faut appliquer un masque à l'image afin d'obtenir la transparence de l'image originale.

```java
public static void AddImage04()
{
    Document document = new Document(_dataDir + "sample_color.pdf");
    PdfFileMend mender = new PdfFileMend();
    // Charger l'image dans le flux
    var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
    mender.BindPdf(document);
    int pageNum = 1;
    int lowerLeftX = 10;
    int lowerLeftY = 650;
    int upperRightX = 110;
    int upperRightY = 750;
    CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply, ImageFilterType.Flate,false);
    mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

    // enregistrer le fichier de sortie
    mender.Save(_dataDir + "PdfFileMend07_output.pdf");
}
```