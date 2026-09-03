---
title: 与 JasperReports 集成
linktitle: 与 JasperReports 集成
type: docs
weight: 20
url: /zh/jasperreports/integration-with-jasperreports/
description: 了解如何将 Aspose.PDF 与 JasperReports 集成。将报告无缝导出为具有增强功能的专业级 PDF。
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

要在应用程序中使用 Aspose.PDF for JasperReports，请将 **aspose.pdf.jasperreports.jar** 从 **Aspose.PDF.JasperReports.zip** 中的 \lib 文件夹复制到 JasperReports\lib 目录，或复制到应用程序的库文件夹。之后，您可以通过编程方式访问导出器。

{{% /alert %}}

以下示例显示了使用 Aspose.PDF for JasperReports 将报表导出为 PDF 格式所需的典型代码。更多示例可以在产品下载中包含的演示报告中找到。

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

上面的代码片段已经使用 JasperReports 3.5.2 进行了测试。如果使用 JasperReports 3.1.0，请尝试使用 import com.aspose.pdf.jr3_1_0.jasperreports。并替换其余代码中的产品版本。

