title: Интеграция с JasperReports

type: docs

weight: 20

url: /ru/jasperreports/integration-with-jasperreports/

lastmod: "2021-06-05"

---

{{% alert color="primary" %}}

Чтобы использовать Aspose.PDF для JasperReports в вашем приложении, скопируйте **aspose.pdf.jasperreports.jar** из папки \lib в **Aspose.PDF.JasperReports.zip** в директорию JasperReports\lib или в папку библиотеки вашего приложения. После этого, вы сможете программно получить доступ к экспортерам.

{{% /alert %}}

Следующий пример показывает типичный код, необходимый для экспорта отчета в формат PDF, используя Aspose.PDF для JasperReports. Больше примеров можно найти в демонстрационных отчетах, включенных в загрузку продукта.

{{< highlight csharp >}}

import com.aspose.pdf.jr3_7_0.jasperreports.*;

com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();

File sourceFile = new File(fileName);

JasperPrint jasperPrint = (JasperPrint)JRLoader.loadObject(sourceFile);
```

```java
exporter.setParameter(JRExporterParameter.JASPER_PRINT, jasperPrint);

File destFile = new File(sourceFile.getParent(), jasperPrint.getName() + ".pdf");

exporter.setParameter(JRExporterParameter.OUTPUT_FILE_NAME, destFile.toString());

exporter.exportReport();
```

{{< /highlight >}}

Приведенный выше фрагмент кода был протестирован с JasperReports 3.5.2. Если вы используете JasperReports 3.1.0, попробуйте использовать import com.aspose.pdf.jr3_1_0.jasperreports.; и замените версию продукта в остальной части кода также.