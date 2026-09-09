---
title: Integration with JasperReports
linktitle: Integration with JasperReports
type: docs
weight: 20
url: /id/jasperreports/integration-with-jasperreports/
description: Temukan cara mengintegrasikan Aspose.PDF dengan JasperReports. Ekspor laporan dengan lancar ke PDF tingkat profesional dengan fungsionalitas yang ditingkatkan.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

To use Aspose.PDF for JasperReports in your application, copy **aspose.pdf.jasperreports.jar** from the \lib folder in the **Aspose.PDF.JasperReports.zip** to the JasperReports\lib directory, or to a library folder of your application. After that, you can access the exporters programmatically.

{{% /alert %}}

Contoh berikut menunjukkan kode umum yang diperlukan untuk mengekspor laporan ke format PDF menggunakan Aspose.PDF for JasperReports. Contoh lainnya dapat ditemukan di laporan demo yang disertakan dalam unduhan produk.

```java
import com.aspose.pdf.jr3_7_0.jasperreports.*;

com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();

File sourceFile = new File(fileName);

JasperPrint jasperPrint = (JasperPrint)JRLoader.loadObject(sourceFile);

exporter.setParameter(JRExporterParameter.JASPER_PRINT, jasperPrint);

File destFile = new File(sourceFile.getParent(), jasperPrint.getName() + ".pdf");

exporter.setParameter(JRExporterParameter.OUTPUT_FILE_NAME, destFile.toString());

exporter.exportReport();
```

Cuplikan kode di atas telah diuji dengan JasperReports 3.5.2. Jika menggunakan JasperReports 3.1.0, silakan coba gunakan import com.aspose.pdf.jr3_1_0.jasperreports.; dan ganti juga versi produk di sisa kodenya.

