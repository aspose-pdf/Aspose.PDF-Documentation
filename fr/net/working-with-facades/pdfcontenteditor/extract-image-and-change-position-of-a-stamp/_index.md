---
title: Extraire une image et changer la position du timbre
type: docs
weight: 30
url: fr/net/extract-image-and-change-position-of-a-stamp/
description: Cette section explique comment extraire une image et changer la position d'un timbre avec Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

## Extraire une image d'un timbre image

La classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) vous permet d'extraire des images d'un timbre dans un fichier PDF. Tout d'abord, vous devez créer un objet de la classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Après cela, appelez la méthode [GetStamps](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/getstamps) pour obtenir un tableau d'objets StampInfo à partir d'une page particulière du fichier PDF. Ensuite, vous pouvez obtenir l'image d'un StampInfo en utilisant la propriété StampInfo.Image. Une fois que vous avez l'image, vous pouvez enregistrer l'image ou travailler avec différentes propriétés de l'image. Le fragment de code suivant vous montre comment extraire une image d'un tampon d'image.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ExtractImageImageStamp-ExtractImageImageStamp.cs" >}}

## Changer la position d'un tampon dans un fichier PDF

La classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) vous permet de changer la position d'un tampon dans un fichier PDF. Tout d'abord, vous devez créer un objet de la classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) et lier le fichier PDF d'entrée à l'aide de la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Après cela, appelez la méthode [MoveStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/movestamp) avec l'index du tampon et la nouvelle position sur une page particulière du fichier PDF. Ensuite, vous pouvez enregistrer le fichier mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). L'extrait de code suivant vous montre comment déplacer un tampon dans une page particulière.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ChangeStampPosition-ChangeStampPosition.cs" >}}

De plus, vous pouvez utiliser la méthode [MoveStampById](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/movestampbyid) pour déplacer un tampon spécifique en utilisant StampId.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Stamps-Watermarks-ChangeStampPosition-ChangeStampPositionByID.cs" >}}