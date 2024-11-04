---
title: Manipuler les propriétés de la page
type: docs
weight: 80
url: /net/manipulate-page-properties/
description: Cette section explique comment manipuler les propriétés de la page avec Aspose.PDF Facades en utilisant la classe PdfPageEditor.
lastmod: "2021-06-05"
draft: false
---

## Obtenir les propriétés de la page PDF à partir d'un fichier PDF existant

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) vous permet de travailler avec des pages individuelles du fichier PDF. Cela vous aide à obtenir les propriétés de chaque page individuelle telles que les différentes tailles de boîte de page, la rotation de page, le zoom de page, etc. Afin d'obtenir ces propriétés, vous devez créer un objet [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Après cela, vous pouvez utiliser différentes méthodes pour obtenir les propriétés de la page comme [GetPageRotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpagerotation), [GetPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpages), [GetPageBoxSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/methods/getpageboxsize) etc.

Le code suivant vous montre comment obtenir les propriétés des pages PDF à partir d'un fichier PDF existant.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-GetPageProperties-GetPageProperties.cs" >}}
## Définir les propriétés de page PDF dans un fichier PDF existant

Pour définir des propriétés de page comme la rotation de page, le zoom ou le point d'origine, vous devez utiliser la classe [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor). Cette classe fournit différentes méthodes et propriétés pour définir ces propriétés de page. Tout d'abord, vous devez créer un objet de la classe [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) et lier le fichier PDF d'entrée en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Après cela, vous pouvez utiliser ces méthodes et propriétés pour définir les propriétés de page. Enfin, enregistrez le fichier PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save).

L'extrait de code suivant vous montre comment définir les propriétés de page PDF dans un fichier PDF existant.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-SetPageProperties-SetPageProperties.cs" >}}

## Redimensionner le contenu des pages spécifiques dans un fichier PDF

La méthode ResizeContents de la classe [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) vous permet de redimensionner le contenu des pages dans un fichier PDF. La classe [ContentsResizeParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/contentsresizeparameters) est utilisée pour spécifier les paramètres à utiliser pour redimensionner la ou les pages, par exemple les marges en pourcentage ou en unités, etc. Vous pouvez redimensionner toutes les pages ou spécifier un tableau de pages à redimensionner en utilisant la méthode ResizeContents.

Le snippet de code suivant montre comment redimensionner le contenu de certaines pages spécifiques d'un fichier PDF.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ManipulatePageProperties-ResizePageContents-ResizePageContents.cs" >}}