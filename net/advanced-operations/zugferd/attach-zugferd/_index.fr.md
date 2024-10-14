---
title: Création de PDF conforme PDF/3-A et ajout d'une facture ZUGFeRD en C#
linktitle: Joindre ZUGFeRD à un PDF
type: docs
weight: 10
url: /net/attach-zugferd/
description: Apprenez à générer un document PDF avec ZUGFeRD dans Aspose.PDF pour .NET
lastmod: "2023-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Joindre ZUGFeRD à un PDF

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

Nous recommandons les étapes suivantes pour attacher ZUGFeRD à un PDF :

* Définir une variable de chemin qui pointe vers un dossier où se trouvent les fichiers PDF d'entrée et de sortie.
* Créer un objet document en chargeant un fichier PDF existant (par exemple, "ZUGFeRD-test.pdf") à partir du chemin.
* Créer un objet [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification/) en fournissant le chemin et la description d'un autre fichier nommé "factur-x.xml", qui contient des métadonnées de facture conformes à la norme ZUGFeRD.
* Ajouter des propriétés à l'objet de spécification de fichier, telles que la description, le type MIME et la relation AF.
* Ajouter des propriétés à l'objet de spécification de fichier, telles que la description, le type MIME et la relation AF.
* Ajouter l'objet de spécification de fichier à la collection de fichiers intégrés du document. Le nom du fichier doit être spécifié selon la norme ZUGFeRD, par exemple "factur-x.xml".
* Convertir le document au format PDF/A-3U, un sous-ensemble de PDF qui assure la préservation à long terme des documents électroniques. Le PDF/A-3U permet d'intégrer des fichiers de tout format dans des documents PDF.
* Enregistrer le document converti en tant que nouveau fichier PDF (par exemple, "ZUGFeRD-res.pdf").

```cs
var path = @"C:\Samples\ZUGFeRD\";

var document = new Aspose.Pdf.Document(Path.Combine(path,"ZUGFeRD-test.pdf"));
// Configurer le nouveau fichier à ajouter en tant que pièce jointe
var description = "Métadonnées de facture conformes à la norme ZUGFeRD";
var fileSpecification = new Aspose.Pdf.FileSpecification(Path.Combine(path, "factur-x.xml"), description)
{
    Description = "Zugferd",
    MIMEType = "text/xml",
    AFRelationship = Aspose.Pdf.AFRelationship.Alternative
};
// Ajouter la pièce jointe à la collection de pièces jointes du document
document.EmbeddedFiles.Add(fileSpecification);
document.Convert(new MemoryStream(), Aspose.Pdf.PdfFormat.PDF_A_3U, Aspose.Pdf.ConvertErrorAction.Delete);
document.Save(Path.Combine(path, "ZUGFeRD-res.pdf"));
```
La méthode convert prend un flux, un format PDF et une action en cas d'erreur de conversion en tant que paramètres. Le paramètre flux peut être utilisé pour sauvegarder le journal de conversion. Le paramètre action en cas d'erreur de conversion spécifie quoi faire si des erreurs surviennent pendant la conversion. Dans ce cas, il est défini sur "Supprimer", ce qui signifie que tout élément non conforme au format PDF/A-3U sera supprimé du document.
