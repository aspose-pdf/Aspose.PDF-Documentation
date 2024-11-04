---
title: Diviser les pages PDF
type: docs
weight: 60
url: /net/split-pdf-pages/
description: Cette section explique comment diviser les pages PDF avec Aspose.PDF Facades en utilisant la classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Diviser les pages PDF à partir de la première en utilisant les chemins de fichiers

La méthode [SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) vous permet de diviser le fichier PDF en commençant par la première page et en terminant à la page spécifiée. Si vous souhaitez manipuler les fichiers PDF à partir du disque, vous pouvez passer les chemins des fichiers PDF d'entrée et de sortie à cette méthode. L'extrait de code suivant vous montre comment diviser les pages PDF à partir de la première en utilisant les chemins de fichiers.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesUsingPaths-SplitPagesUsingPaths.cs" >}}

## Diviser les pages PDF à partir de la première en utilisant les flux de fichiers

[SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) méthode de la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) vous permet de diviser le fichier PDF en commençant par la première page et en terminant au numéro de page spécifié. Si vous souhaitez manipuler les fichiers PDF à partir des flux, vous pouvez passer les flux PDF d'entrée et de sortie à cette méthode. L'extrait de code suivant vous montre comment diviser les pages PDF à partir de la première en utilisant des flux de fichiers.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesUsingStreams-SplitPagesUsingStreams.cs" >}}

## Diviser les pages PDF en vrac en utilisant les chemins de fichiers

[SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/splittobulks/index) méthode de la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor) vous permet de diviser le fichier PDF en plusieurs ensembles de pages. Dans cet exemple, nous avons besoin de deux ensembles de pages (1, 2) et (5, 6). Si vous souhaitez accéder au fichier PDF depuis le disque, vous devez passer le PDF d'entrée en tant que chemin de fichier. Cette méthode renvoie un tableau de MemoryStream. Vous pouvez parcourir ce tableau et enregistrer les ensembles individuels de pages en tant que fichiers séparés. L'extrait de code suivant vous montre comment diviser les pages PDF en vrac en utilisant des chemins de fichiers.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToBulkUsingPaths-SplitPagesToBulkUsingPaths.cs" >}}

## Diviser les pages PDF en vrac en utilisant des flux

La méthode [SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittobulks/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) vous permet de diviser le fichier PDF en plusieurs ensembles de pages. Dans cet exemple, nous avons besoin de deux ensembles de pages (1, 2) et (5, 6). Vous pouvez passer un flux à cette méthode au lieu d'accéder au fichier depuis le disque. Cette méthode retourne un tableau de MemoryStream. Vous pouvez parcourir ce tableau et enregistrer les ensembles individuels de pages en tant que fichiers séparés. L'extrait de code suivant vous montre comment diviser les pages PDF en masse à l'aide de flux.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToBulkUsingStreams-SplitPagesToBulkUsingStreams.cs" >}}

## Diviser les pages PDF jusqu'à la fin en utilisant des chemins de fichiers

La méthode [SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) vous permet de diviser le PDF à partir du numéro de page spécifié jusqu'à la fin du fichier PDF et de l'enregistrer en tant que nouveau PDF. Afin de faire cela, en utilisant les chemins de fichiers, vous devez passer les chemins de fichiers d'entrée et de sortie ainsi que le numéro de page à partir duquel la séparation doit commencer. Le PDF de sortie sera enregistré sur le disque. L'extrait de code suivant vous montre comment séparer les pages PDF jusqu'à la fin en utilisant des chemins de fichiers.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToEndUsingPaths-SplitPagesToEndUsingPaths.cs" >}}

## Séparer les Pages PDF jusqu'à la Fin en Utilisant des Flux

La méthode [SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) vous permet de séparer le PDF à partir du numéro de page spécifié jusqu'à la fin du fichier PDF et de l'enregistrer comme un nouveau PDF. Pour ce faire, en utilisant des flux, vous devez passer les flux d'entrée et de sortie et le numéro de page à partir duquel la séparation doit commencer. Le PDF de sortie sera enregistré dans le flux de sortie. Le code suivant vous montre comment diviser les pages PDF jusqu'à la fin en utilisant des flux.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToEndUsingStreams-SplitPagesToEndUsingStreams.cs" >}}

## Diviser un PDF en pages individuelles en utilisant les chemins de fichiers

{{% alert color="primary" %}}

Vous pouvez essayer de diviser le document PDF et voir les résultats en ligne à ce lien :

[products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter) {{% /alert %}}

Pour diviser un fichier PDF en pages individuelles, vous devez passer le PDF en tant que chemin de fichier à la méthode [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index). Ce document décrit une méthode permettant de retourner un tableau de MemoryStream contenant des pages individuelles du fichier PDF. Vous pouvez parcourir ce tableau de MemoryStream et enregistrer des pages individuelles en tant que fichiers PDF séparés sur le disque. Le snippet de code suivant vous montre comment diviser un PDF en pages individuelles en utilisant des chemins de fichiers.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitToIndividualPagesUsingPaths-SplitToIndividualPagesUsingPaths.cs" >}}

## Diviser un PDF en Pages Individuelles en Utilisant des Flux

Pour diviser un fichier PDF en pages individuelles, vous devez passer le PDF en tant que flux à la méthode [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index). Cette méthode retournera un tableau de MemoryStream contenant des pages individuelles du fichier PDF. Vous pouvez parcourir ce tableau de MemoryStream et enregistrer des pages individuelles en tant que fichiers PDF individuels sur le disque, ou vous pouvez conserver ces pages individuelles dans le flux de mémoire pour une utilisation ultérieure dans votre application. L'extrait de code suivant vous montre comment diviser un PDF en pages individuelles en utilisant des flux.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitToIndividualPagesUsingStreams-SplitToIndividualPagesUsingStreams.cs" >}}