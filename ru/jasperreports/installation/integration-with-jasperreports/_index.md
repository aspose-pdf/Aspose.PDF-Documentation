---
title: Интеграция с JasperReports
linktitle: Интеграция с JasperReports
type: docs
weight: 20
url: /ru/jasperreports/integration-with-jasperreports/
description: Узнайте, как интегрировать Aspose.PDF с JasperReports. Легко экспортируйте отчеты в PDF-файлы профессионального уровня с расширенными функциями.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

Чтобы использовать Aspose.PDF for JasperReports в своем приложении, скопируйте **Aspose.PDF.jasperreports.jar** из папки \lib в **Aspose.PDF.JasperReports.zip** в каталог JasperReports\lib или в папку библиотеки вашего приложения. После этого вы можете получить доступ к экспортерам программно.

{{% /alert %}}

В следующем примере показан типичный код, необходимый для экспорта отчета в формат PDF с использованием Aspose.PDF for JasperReports. Дополнительные примеры можно найти в демонстрационных отчетах, включенных в загрузку продукта.

```java
import com.Aspose.PDF.jr3_7_0.jasperreports.*;

com.Aspose.PDF.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.Aspose.PDF. jr3_7_0.jasperreports.JrPdfExporter();

File sourceFile = new File(fileName);

JasperPrint jasperPrint = (JasperPrint)JRLoader.loadObject(sourceFile);

exporter.setParameter(JRExporterParameter.JASPER_PRINT, jasperPrint);

File destFile = new File(sourceFile.getParent(), jasperPrint.getName() + ".pdf");

exporter.setParameter(JRExporterParameter.OUTPUT_FILE_NAME, destFile.toString());

exporter.exportReport();
```

Приведенный выше фрагмент кода был протестирован с помощью JasperReports 3.5.2. Если вы используете JasperReports 3.1.0, попробуйте использовать import com.Aspose.PDF.jr3_1_0.jasperreports.; а также замените версию продукта в остальной части кода.
