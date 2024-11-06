title: JasperReportsとの統合

type: docs

weight: 20

url: ja/jasperreports/integration-with-jasperreports/

lastmod: "2021-06-05"

---

{{% alert color="primary" %}}

アプリケーションでAspose.PDF for JasperReportsを使用するには、**Aspose.PDF.JasperReports.zip**の\libフォルダーから**aspose.pdf.jasperreports.jar**をJasperReports\libディレクトリまたはアプリケーションのライブラリフォルダーにコピーします。その後、プログラムからエクスポーターにアクセスできます。

{{% /alert %}}

次の例は、Aspose.PDF for JasperReportsを使用してレポートをPDF形式でエクスポートするために必要な一般的なコードを示しています。製品ダウンロードに含まれるデモレポートでより多くの例を見つけることができます。

{{< highlight csharp >}}

import com.aspose.pdf.jr3_7_0.jasperreports.*;

com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();

File sourceFile = new File(fileName);

JasperPrint jasperPrint = (JasperPrint)JRLoader.loadObject(sourceFile);
```

exporter.setParameter(JRExporterParameter.JASPER_PRINT, jasperPrint);

File destFile = new File(sourceFile.getParent(), jasperPrint.getName() + ".pdf");

exporter.setParameter(JRExporterParameter.OUTPUT_FILE_NAME, destFile.toString());

exporter.exportReport();

{{< /highlight >}}

上記のコードスニペットはJasperReports 3.5.2でテストされています。JasperReports 3.1.0を使用する場合は、import com.aspose.pdf.jr3_1_0.jasperreports.; を使用して、コードの残りの部分でも製品バージョンを置き換えてみてください。