---
title: Insérer des pages PDF
type: docs
weight: 50
url: /net/insert-pdf-pages/
description: Cette section explique comment insérer des pages PDF avec Aspose.PDF Facades en utilisant la classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## Insérer des pages PDF entre deux numéros en utilisant les chemins de fichiers

Une plage particulière de pages peut être insérée d'un PDF dans un autre en utilisant la méthode [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor). Afin de le faire, vous avez besoin d'un fichier PDF d'entrée dans lequel vous souhaitez insérer les pages, d'un fichier port à partir duquel les pages doivent être prises pour l'insertion, d'un emplacement où les pages doivent être insérées, et d'une plage de pages du fichier port qui doivent être insérées dans le fichier PDF d'entrée. Cette plage est spécifiée avec des paramètres de page de début et de page de fin. Enfin, le fichier PDF de sortie est enregistré avec la plage de pages spécifiée insérée dans le fichier d'entrée. L'extrait de code suivant vous montre comment insérer des pages PDF entre deux numéros en utilisant des flux de fichiers.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-InsertPages-InsertPagesBetweenNumbers-InsertPagesBetweenNumbers.cs" >}}

## Insérer un tableau de pages PDF en utilisant des chemins de fichiers

Si vous souhaitez insérer certaines pages spécifiées dans un autre fichier PDF, vous pouvez utiliser une surcharge de la méthode [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) qui nécessite un tableau d'entiers de pages. Dans ce tableau, vous pouvez spécifier quelles pages particulières vous souhaitez insérer dans le fichier PDF d'entrée. Pour cela, vous avez besoin d'un fichier PDF d'entrée dans lequel vous souhaitez insérer les pages, d'un fichier source à partir duquel les pages doivent être prises pour l'insertion, d'un emplacement où les pages doivent être insérées et d'un tableau d'entiers des pages du fichier source qui doivent être insérées dans le fichier PDF d'entrée. Ce tableau contient une liste de pages particulières que vous souhaitez insérer dans le fichier PDF d'entrée. Enfin, le fichier PDF de sortie est enregistré avec le tableau spécifié de pages insérées dans le fichier d'entrée.

Le code suivant vous montre comment insérer un tableau de pages PDF en utilisant les chemins de fichiers.

## Insérer des Pages PDF entre Deux Nombres en Utilisant des Flux

Si vous souhaitez insérer la plage de pages en utilisant des flux, vous devez simplement utiliser la surcharge appropriée de la méthode [Insert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor). Afin de faire cela, vous avez besoin d'un flux PDF d'entrée dans lequel vous souhaitez insérer les pages, d'un flux de port à partir duquel les pages doivent être prises pour insertion, d'un emplacement où les pages doivent être insérées, et d'une plage de pages du flux de port qui doivent être insérées dans le flux PDF d'entrée. Cette plage est spécifiée avec les paramètres de la page de début et de la page de fin. Enfin, le flux PDF de sortie est enregistré avec la plage de pages spécifiée insérée dans le flux d'entrée. L'extrait de code suivant vous montre comment insérer des pages PDF entre deux numéros en utilisant des flux.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-InsertPages-InsertPagesBetweenNumbersUsingStreams-InsertPagesBetweenNumbersUsingStreams.cs" >}}

## Insérer un tableau de pages PDF en utilisant des flux

Vous pouvez également insérer un tableau de pages dans un autre fichier PDF en utilisant des flux avec l'aide de la surcharge appropriée de la méthode Insert qui nécessite un tableau entier de pages. Dans ce tableau, vous pouvez spécifier quelles pages particulières vous souhaitez insérer dans le flux PDF d'entrée. Pour ce faire, vous avez besoin d'un flux PDF d'entrée dans lequel vous voulez insérer les pages, d'un flux de port à partir duquel les pages doivent être prises pour l'insertion, d'un emplacement où les pages doivent être insérées, et d'un tableau d'entiers des pages du flux de port qui doivent être insérées dans le fichier PDF d'entrée. Ce tableau contient une liste de pages particulières que vous souhaitez insérer dans le flux PDF d'entrée. Enfin, le flux PDF de sortie est enregistré avec le tableau spécifié de pages insérées dans le fichier d'entrée. Le fragment de code suivant vous montre comment insérer un tableau de pages PDF en utilisant des flux.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-InsertPages-InsertPagesUsingStreams-InsertPagesUsingStreams.cs" >}}