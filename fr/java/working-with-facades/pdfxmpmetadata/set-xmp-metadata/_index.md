---
title: Définir les métadonnées XMP d'un PDF existant - façades
type: docs
weight: 20
url: fr/java/set-xmp-metadata/
description: Cette section explique comment définir les métadonnées XMP avec Aspose.PDF Facades en utilisant la classe PdfXmpMetadata.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Pour définir les métadonnées XMP dans un fichier PDF, vous devez créer un objet [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata) et lier le fichier PDF en utilisant la méthode [bindPdf(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Facade#bindPdf-com.aspose.pdf.IDocument-).
 You can use the method setByDefaultMetadataProperties(..) de la classe [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata) pour ajouter différentes propriétés. Enfin, appelez la méthode [save(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/SaveableFacade#save-java.io.OutputStream-) de la classe [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata).

Le snippet de code suivant vous montre comment ajouter des métadonnées XMP dans un fichier PDF.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Document-SetXMPMetadataOfAnExistingPDF-.java" >}}