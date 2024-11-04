---
title: Édition des pages individuelles d'un PDF
type: docs
weight: 20
url: /net/editing-a-pdf-s-individual-pages-using-pdfpageeditor-class/
description: Cette section explique comment éditer les pages individuelles d'un PDF en utilisant la classe PdfPageEditor.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

L'espace de noms Aspose.Pdf.Facades dans [Aspose.PDF pour .NET](/pdf/net/) vous permet de manipuler des pages individuelles dans un fichier PDF. Cette fonctionnalité vous aide à travailler avec l'affichage des pages, l'alignement et la transition, etc. La classe PdfPageEditor aide à réaliser cette fonctionnalité. Dans cet article, nous examinerons les propriétés et méthodes fournies par cette classe ainsi que le fonctionnement de ces méthodes.

{{% /alert %}}

## Explication

La classe [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) est différente de la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) et de la classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). Tout d'abord, nous devons comprendre la différence, puis nous serons en mesure de mieux comprendre la classe PdfPageEditor. La classe PdfFileEditor vous permet de manipuler toutes les pages d'un fichier comme ajouter, supprimer ou concaténer des pages, etc., tandis que la classe PdfContentEditor vous aide à manipuler le contenu d'une page, c'est-à-dire le texte et d'autres objets, etc. Alors que, la classe PdfPageEditor ne fonctionne qu'avec la page individuelle elle-même comme la rotation, le zoom et l'alignement d'une page, etc.

Nous pouvons diviser les fonctionnalités fournies par cette classe en trois catégories principales, c'est-à-dire Transition, Alignement et Affichage. Nous allons discuter de ces catégories ci-dessous :

### Transition

Cette classe contient deux propriétés liées à la transition, c'est-à-dire. [TransitionType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/transitiontype) et [TransitionDuration](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/transitionduration). TransitionType spécifie le style de transition à utiliser lors du passage à cette page depuis une autre page pendant une présentation. TransitionDuration spécifie la durée d'affichage des pages.

### Alignment

La classe PdfPageEditor prend en charge les alignements horizontaux et verticaux. Il fournit deux propriétés pour servir l'objectif, c'est-à-dire [Alignment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/alignment) et [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/VerticalAlignment). La propriété Alignment est utilisée pour aligner le contenu horizontalement. La propriété Alignment prend une valeur de AlignmentType, qui contient trois options, c'est-à-dire Center, Left, et Right. La propriété VerticalAlignment prend une valeur de VerticalAlignmentType, qui contient trois options, c'est-à-dire Bottom, Center, et Top.

### Affichage

Dans la catégorie affichage, nous pouvons inclure des propriétés comme PageSize, Rotation, Zoom, et DisplayDuration. PageSize property specifies the size of individual page in the file. This property takes PageSize object as an input, which encapsulates predefined page size like A0, A1, A2, A3, A4, A5, A6, B5, Letter, Ledger, and P11x17. Rotation property is used to set the rotation of an individual page. It can take values 0, 90, 180, or 270. Zoom property sets the zoom coefficient for the page, and it takes a float value as an input. This class also provides method to get page size and page rotation of the individual page in the file.

La propriété PageSize spécifie la taille de la page individuelle dans le fichier. Cette propriété prend un objet PageSize en entrée, qui encapsule des tailles de page prédéfinies comme A0, A1, A2, A3, A4, A5, A6, B5, Lettre, Ledger et P11x17. La propriété Rotation est utilisée pour définir la rotation d'une page individuelle. Elle peut prendre les valeurs 0, 90, 180 ou 270. La propriété Zoom définit le coefficient de zoom pour la page et prend une valeur flottante en entrée. Cette classe fournit également une méthode pour obtenir la taille de la page et la rotation de la page individuelle dans le fichier.

You can find samples of the above mentioned methods in the code snippet given below:

Vous pouvez trouver des exemples des méthodes mentionnées ci-dessus dans l'extrait de code ci-dessous :



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-EditPdfPages-EditPdfPages.cs" >}}

## Conclusion

{{% alert color="primary" %}}
In this article, we have taken a closer look on the [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) class.

Dans cet article, nous avons examiné de plus près la classe [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor). We have elaborated the properties and methods provided by this class. It makes the manipulation of individual pages in a class a very easy and simple task.  
{{% /alert %}}

{{% alert color="primary" %}}

Nous avons élaboré les propriétés et méthodes fournies par cette classe. Cela rend la manipulation des pages individuelles dans une classe une tâche très facile et simple.  
{{% /alert %}}