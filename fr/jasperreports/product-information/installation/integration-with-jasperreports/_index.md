---
title: Intégration avec JasperReports

type: docs

weight: 20

url: /fr/jasperreports/integration-with-jasperreports/

lastmod: "2021-06-05"

---

{{% alert color="primary" %}}

Pour utiliser Aspose.PDF pour JasperReports dans votre application, copiez **aspose.pdf.jasperreports.jar** du dossier \lib dans le fichier **Aspose.PDF.JasperReports.zip** vers le répertoire JasperReports\lib, ou vers un dossier de bibliothèque de votre application. Après cela, vous pouvez accéder aux exportateurs par programme.

{{% /alert %}}

L'exemple suivant montre le code typique nécessaire pour exporter un rapport au format PDF en utilisant Aspose.PDF pour JasperReports. Plus d'exemples peuvent être trouvés dans les rapports de démonstration inclus dans le téléchargement du produit.

{{< highlight csharp >}}

import com.aspose.pdf.jr3_7_0.jasperreports.*;

com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf. jr3_7_0.jasperreports.JrPdfExporter();

File sourceFile = new File(fileName);

JasperPrint jasperPrint = (JasperPrint)JRLoader.loadObject(sourceFile);

   exporter.setParameter(JRExporterParameter.JASPER_PRINT, jasperPrint);





   File destFile = new File(sourceFile.getParent(), jasperPrint.getName() + ".pdf");



   exporter.setParameter(JRExporterParameter.OUTPUT_FILE_NAME, destFile.toString());





   exporter.exportReport();





{{< /highlight >}}



Le code ci-dessus a été testé avec JasperReports 3.5.2. Si vous utilisez JasperReports 3.1.0, veuillez essayer d'utiliser import com.aspose.pdf.jr3_1_0.jasperreports.; et remplacer également la version du produit dans le reste du code.