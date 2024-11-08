---
title: Suppression de pièce jointe d'un PDF
linktitle: Suppression de pièce jointe d'un PDF existant
type: docs
weight: 30
url: /fr/cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF pour C++ peut supprimer des pièces jointes de vos documents PDF. Utilisez l'API PDF C++ pour supprimer des pièces jointes dans les fichiers PDF en utilisant la bibliothèque Aspose.PDF.
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF peut supprimer des pièces jointes des fichiers PDF. Les pièces jointes d'un document PDF sont contenues dans la collection EmbeddedFiles de l'objet Document.

Pour supprimer toutes les pièces jointes associées à un fichier PDF :

1. Appelez la méthode [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection#afff8b235b554a66c203464b61204b843) de la collection [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection).
1. Enregistrez le fichier mis à jour en utilisant la méthode Save de l'objet [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

Le code suivant montre comment supprimer des pièces jointes d'un document PDF.

```cpp
void WorkingWithAttachments::RemovingAttachment() {

 String _dataDir("C:\\Samples\\");

 // Ouvrir le document
 auto pdfDocument = new Document(_dataDir + u"DeleteAllAttachments.pdf");

 // Supprimer toutes les pièces jointes
 pdfDocument->get_EmbeddedFiles()->Delete();

 // Enregistrer le fichier mis à jour
 pdfDocument->Save(_dataDir + u"DeleteAllAttachments_out.pdf");
}
```