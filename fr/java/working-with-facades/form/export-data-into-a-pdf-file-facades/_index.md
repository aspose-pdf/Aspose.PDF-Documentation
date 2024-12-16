---
title: Exporter des Données vers XML à partir d'un Fichier PDF (Façades)
type: docs
weight: 20
url: /fr/java/export-data-into-a-pdf-file-facades/
description: Cette section explique comment exporter des Données vers XML à partir d'un Fichier PDF avec Aspose.PDF Facades en utilisant la classe Form.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

La classe [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) vous permet d'exporter des données vers un fichier XML à partir d'un fichier PDF en utilisant la méthode exportXml. Pour exporter des données vers XML, vous devez créer un objet de la classe [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form), ouvrir le formulaire PDF source en utilisant la méthode bindPDF, puis appeler la méthode exportXml en utilisant l'objet OutputStream. Enfin, vous pouvez fermer l'objet OutputStream et libérer l'objet Form. Le code suivant vous montre comment exporter des données vers un fichier XML.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Forms-ExportDataToXMLFromAPDFFile-.java" >}}