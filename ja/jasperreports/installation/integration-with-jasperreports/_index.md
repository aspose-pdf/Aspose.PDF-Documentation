---
title: JasperReports との統合
linktitle: JasperReports との統合
type: docs
weight: 20
url: /ja/jasperreports/integration-with-jasperreports/
description: Aspose.PDF を JasperReports と統合する方法をご覧ください。強化された機能を備えたプロ仕様の PDF にレポートをシームレスにエクスポートします。
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

アプリケーションで Aspose.PDF for JasperReports を使用するには、**Aspose.PDF.JasperReports.zip** の \lib フォルダーから **aspose.pdf.jasperreports.jar** を JasperReports\lib ディレクトリまたはアプリケーションのライブラリ フォルダーにコピーします。その後、プログラムでエクスポーターにアクセスできるようになります。

{{% /alert %}}

次の例は、Aspose.PDF for JasperReports を使用してレポートを PDF 形式にエクスポートするために必要な一般的なコードを示しています。製品のダウンロードに含まれるデモ レポートには、さらに多くの例が含まれています。

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

上記のコード スニペットは、JasperReports 3.5.2 でテストされています。 JasperReports 3.1.0 を使用している場合は、import com.aspose.pdf.jr3_1_0.jasperreports を使用してみてください。コードの残りの部分でも製品バージョンを置き換えます。

