---
title: Création d'un PDF conforme PDF/3-A et attachement d'une facture ZUGFeRD en Java
linktitle: Attacher ZUGFeRD au PDF
type: docs
weight: 10
url: /java/attach-zugferd/
description: Apprenez à générer un document PDF avec ZUGFeRD dans Aspose.PDF pour Java
lastmod: "2024-01-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Attacher ZUGFeRD au PDF

Nous recommandons les étapes suivantes pour attacher ZUGFeRD au PDF :

* Définissez une variable de chemin qui pointe vers un dossier où se trouvent les fichiers PDF d'entrée et de sortie.
* Définissez une variable de type chaîne qui stocke le chemin vers le fichier PDF qui sera traité. Utilisez la méthode `Paths.get` pour combiner les parties du chemin complet.
* Créez une instruction try-with-resources qui garantit que l'objet Document créé à partir de la variable de chemin sera fermé automatiquement après la fin de l'instruction. L'objet Document représente le document PDF qui sera modifié et enregistré.

* Créez un objet [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) en fournissant le chemin et la description d'un autre fichier, qui contient les métadonnées de la facture conformes à la norme ZUGFeRD.
* Ajoutez des propriétés à l'objet de spécification de fichier, telles que la description, le type MIME et la relation AF. La relation AF indique comment le fichier incorporé est lié au document PDF. Dans ce cas, elle est définie sur "Alternative", ce qui signifie que le fichier incorporé est une représentation alternative du contenu PDF.
* Ajoutez l'objet de spécification de fichier à la collection de fichiers incorporés du document. Le nom du fichier doit être spécifié selon la norme ZUGFeRD, par exemple "factor-x.xml".
* Convertissez le document au format PDF/A-3U, un sous-ensemble de PDF qui assure la préservation à long terme des documents électroniques. PDF/A-3U permet l'incorporation de fichiers de n'importe quel format dans les documents PDF.
* Enregistrez le document converti sous un nouveau fichier PDF (par exemple "ZUGFeRD-res.pdf").
* Fermez l'instruction try-with-resources et libérez l'objet Document.

```java
String _dataDir = "/home/aspose/pdf-examples/Samples/";
String path = Paths.get(_dataDir, "ZUGFeRD", "ZUGFeRD-test.pdf").toString();
try (Document document = new Document(path)) {
    String description = "Métadonnées de facture conformes à la norme ZUGFeRD";
    path = Paths.get(_dataDir, "ZUGFeRD", "factur-x.xml").toString();
    FileSpecification fileSpecification = new FileSpecification(path.toString(), description);
    fileSpecification.setMIMEType("text/xml");
    fileSpecification.setAFRelationship(com.aspose.pdf.AFRelationship.Alternative);

    // Ajouter la pièce jointe à la collection de pièces jointes du document
    document.getEmbeddedFiles().add(fileSpecification);
    path = Paths.get(_dataDir, "ZUGFeRD", "log.xml").toString();
    document.convert(path, PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
    path = Paths.get(_dataDir, "ZUGFeRD", "ZUGFeRD-res.pdf").toString();
    document.save(path);
}
```