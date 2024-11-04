---
title: Conversion d'un FDF en format XML
type: docs
weight: 10
url: /net/converting-an-fdf-to-xml-format/
description: Cette section explique comment vous pouvez convertir un FDF en format XML avec la classe FormDataConverter.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Le namespace [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) dans [Aspose.PDF for .NET](/pdf/net/) supporte très bien les AcroForms. Il supporte également l'importation et l'exportation des données de formulaire vers différents formats de fichiers comme FDF, XFDF et XML. Cependant, parfois, les développeurs peuvent avoir besoin de convertir un format en un autre. Cet article examine la fonctionnalité qui convertit FDF en XML.

{{% /alert %}}

## Détails

FDF signifie Forms Data Format, et un fichier FDF contient les valeurs du formulaire dans une paire clé/valeur. Nous savons également que le fichier XML contient les valeurs en tant que balises. Où, généralement, la clé est représentée comme le nom de la balise et la valeur est représentée comme la valeur à l'intérieur de cette balise. Maintenant, [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) nous offre la flexibilité de convertir un format de fichier FDF en un format XML.

Nous pouvons utiliser la classe [FormDataConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter) à cet effet. Cette classe nous fournit différentes méthodes pour convertir un format de données en un autre format. Dans cet article, nous utiliserons simplement une méthode nommée [ConvertFdfToXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formdataconverter/methods/convertfdftoxml). Cette méthode prend le fichier FDF comme entrée ou flux source et le sauvegarde au format XML.

Le code suivant vous montre comment convertir un fichier FDF en un fichier XML :



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConvertPdfToXML-ConvertPdfToXML.cs" >}}