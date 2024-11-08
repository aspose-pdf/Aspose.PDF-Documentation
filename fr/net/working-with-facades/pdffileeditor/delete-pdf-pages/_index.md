---
title: Supprimer des pages PDF
type: docs
weight: 70
url: /fr/net/delete-pdf-pages/
description: Cette section explique comment supprimer des pages PDF avec Aspose.PDF Facades en utilisant la classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

Si vous souhaitez supprimer un certain nombre de pages du fichier PDF qui se trouve sur le disque, vous pouvez utiliser la surcharge de la méthode [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) qui prend les trois paramètres suivants : chemin du fichier d'entrée, tableau des numéros de pages à supprimer, et chemin du fichier PDF de sortie. Le deuxième paramètre est un tableau d'entiers représentant toutes les pages qui doivent être supprimées. Les pages spécifiées sont retirées du fichier d'entrée et le résultat est enregistré en tant que fichier de sortie. Le code suivant vous montre comment supprimer des pages PDF en utilisant des chemins de fichiers.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-DeletePages-DeletePagesUsingFilePath-DeletePagesUsingFilePath.cs" >}}


## Supprimer des pages PDF en utilisant des flux

Le [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) méthode de la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) fournit également une surcharge qui vous permet de supprimer les pages du fichier PDF d'entrée, tandis que les fichiers d'entrée et de sortie sont dans les flux. Cette surcharge prend les trois paramètres suivants : flux d'entrée, tableau d'entiers des pages PDF à supprimer et flux de sortie. Le snippet de code suivant vous montre comment supprimer des pages PDF en utilisant des flux.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-DeletePages-DeletePagesUsingStream-DeletePagesUsingStream.cs" >}}