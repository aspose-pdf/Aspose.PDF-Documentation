---
title: Intégration avec JasperReports
linktitle: Intégration avec JasperReports
type: docs
weight: 20
url: /fr/jasperreports/integration-with-jasperreports/
description: Découvrez comment intégrer Aspose.PDF à JasperReports. Exportez en toute transparence des rapports vers des PDF de qualité professionnelle avec des fonctionnalités améliorées.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Pour utiliser Aspose.PDF pour JasperReports dans votre application, copiez **aspose.pdf.jasperreports.jar** du dossier \lib du **Aspose.PDF.JasperReports.zip** vers le répertoire JasperReports\lib ou dans un dossier de bibliothèque de votre application. Après cela, vous pouvez accéder aux exportateurs par programmation.

{{% /alert %}}

L'exemple suivant montre le code typique nécessaire pour exporter un rapport au format PDF à l'aide d'Aspose.PDF pour JasperReports. D'autres exemples peuvent être trouvés dans les rapports de démonstration inclus dans le téléchargement du produit.

```java
import com.aspose.pdf.jr3_7_0.jasperreports.*;

com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf. jr3_7_0.jasperreports.JrPdfExporter();

File sourceFile = new File(fileName);

JasperPrint jasperPrint = (JasperPrint)JRLoader.loadObject(sourceFile);

exporter.setParameter(JRExporterParameter.JASPER_PRINT, jasperPrint);

File destFile = new File(sourceFile.getParent(), jasperPrint.getName() + ".pdf");

exporter.setParameter(JRExporterParameter.OUTPUT_FILE_NAME, destFile.toString());

exporter.exportReport();
```

The above code snippet has been tested with JasperReports 3.5.2. If using JasperReports 3.1.0, please try using import com.aspose.pdf.jr3_1_0.jasperreports.; and replace the product version in the rest of the code as well.

