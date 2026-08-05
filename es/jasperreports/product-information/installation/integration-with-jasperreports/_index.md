---
title: Integración con JasperReports
linktitle: Integración con JasperReports
type: docs
weight: 20
url: /es/jasperreports/integration-with-jasperreports/
description: Descubra cómo integrar Aspose.PDF con JasperReports. Exporte informes sin problemas a archivos PDF de nivel profesional con funcionalidad mejorada.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Para usar Aspose.PDF para JasperReports en su aplicación, copie **aspose.pdf.jasperreports.jar** de la carpeta \lib en **Aspose.PDF.JasperReports.zip** al directorio JasperReports\lib o a una carpeta de biblioteca de su aplicación. Después de eso, puede acceder a los exportadores mediante programación.

{{% /alert %}}

El siguiente ejemplo muestra el código típico necesario para exportar un informe a formato PDF usando Aspose.PDF para JasperReports. Se pueden encontrar más ejemplos en los informes de demostración incluidos en la descarga del producto.

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

El fragmento de código anterior se ha probado con JasperReports 3.5.2. Si utiliza JasperReports 3.1.0, intente utilizar import com.aspose.pdf.jr3_1_0.jasperreports.; y reemplace también la versión del producto en el resto del código.

