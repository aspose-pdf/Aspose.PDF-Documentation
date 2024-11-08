```
---
title: Importer et Exporter des Signets
type: docs
weight: 20
url: /fr/net/import-and-export-bookmarks/
description: Cette section explique comment importer et exporter des signets avec Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

## Importer des Signets d'un Fichier XML vers un Fichier PDF Existant

[ImportBookmarksWithXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1) méthode vous permet d'importer des signets dans un fichier PDF à partir d'un fichier XML.
``` Pour importer les signets, vous devez créer un objet [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) et lier le fichier PDF en utilisant la méthode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Ensuite, vous devez appeler la méthode [ImportBookmarksWithXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/importbookmarkswithxml/methods/1). Enfin, enregistrez le fichier PDF mis à jour en utilisant la méthode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). Le code suivant vous montre comment importer des signets à partir d'un fichier XML.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ImportFromXML-ImportFromXML.cs" >}}

## Exporter des signets vers XML à partir d'un fichier PDF existant

La méthode ExportBookmarksToXml vous permet d'exporter des signets d'un fichier PDF vers un fichier XML.

Pour exporter des signets :

1. Créez un objet PdfBookmarkEditor et liez le fichier PDF en utilisant la méthode BindPdf.  
1. Appelez la méthode ExportBookmarksToXml.  
1. Enregistrez le fichier PDF mis à jour en utilisant la méthode Save.  

Le code suivant vous montre comment exporter des signets vers un fichier XML.  

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ExportToXML-ExportToXML.cs" >}}