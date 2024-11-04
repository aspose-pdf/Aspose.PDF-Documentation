---
title: Conversion d'un XML au format FDF
type: docs
weight: 20
url: /net/converting-an-xml-to-fdf-format/
description: Cette section explique comment vous pouvez convertir un XML au format FDF avec FormDataConverter.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Le namespace [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) dans [Aspose.PDF pour .NET](/pdf/net/) supporte très bien les AcroForms. Il supporte également l'importation et l'exportation de données de formulaire vers différents formats de fichiers comme FDF, XFDF, et XML. Cependant, parfois un développeur a besoin de convertir un format en un autre. Dans cet article, nous examinerons la fonctionnalité qui nous permet de convertir un format FDF en XML.

{{% /alert %}}

## Détails

FDF signifie Forms Data Format, et un fichier FDF contient les valeurs de formulaire dans une paire clé/valeur. Nous savons également que le fichier XML contient les valeurs sous forme de balises. Où, principalement, la clé est représentée comme le nom de la balise et la valeur est représentée comme la valeur à l'intérieur de cette balise. Maintenant, [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) offre la flexibilité de convertir un format de fichier XML en format FDF.

Utilisez la classe [FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormDataConverter) à cette fin. Cette classe fournit différentes méthodes pour convertir un format de données en un autre. Cet article montre comment utiliser une méthode, ConvertXmlToFdf(..), qui prend un fichier FDF comme entrée ou flux source et le sauvegarde au format XML. Le code suivant montre comment convertir un fichier FDF en fichier XML.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-XMLToPdf-XMLToPdf.cs" >}}