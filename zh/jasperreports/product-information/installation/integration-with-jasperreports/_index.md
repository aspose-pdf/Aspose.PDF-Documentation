title: 与 JasperReports 的集成

type: docs

weight: 20

url: /zh/jasperreports/integration-with-jasperreports/

lastmod: "2021-06-05"

---

{{% alert color="primary" %}}

要在您的应用程序中使用 Aspose.PDF for JasperReports，请从 **Aspose.PDF.JasperReports.zip** 的 \lib 文件夹中复制 **aspose.pdf.jasperreports.jar** 到 JasperReports\lib 目录，或到应用程序的库文件夹。之后，您可以以编程方式访问导出器。

{{% /alert %}}

以下示例展示了使用 Aspose.PDF for JasperReports 将报告导出为 PDF 格式所需的典型代码。更多示例可以在产品下载中包含的演示报告中找到。

{{< highlight csharp >}}

import com.aspose.pdf.jr3_7_0.jasperreports.*;

com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf. jr3_7_0.jasperreports.JrPdfExporter();

File sourceFile = new File(fileName);

JasperPrint jasperPrint = (JasperPrint)JRLoader.loadObject(sourceFile);
```

exporter.setParameter(JRExporterParameter.JASPER_PRINT, jasperPrint);

File destFile = new File(sourceFile.getParent(), jasperPrint.getName() + ".pdf");

exporter.setParameter(JRExporterParameter.OUTPUT_FILE_NAME, destFile.toString());

exporter.exportReport();

{{< /highlight >}}

上面的代码片段已经在 JasperReports 3.5.2 中进行了测试。如果使用 JasperReports 3.1.0，请尝试使用 import com.aspose.pdf.jr3_1_0.jasperreports.; 并在代码的其余部分也替换产品版本。