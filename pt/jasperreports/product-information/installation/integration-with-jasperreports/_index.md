---
title: Integração com JasperReports
linktitle: Integração com JasperReports
type: docs
weight: 20
url: /pt/jasperreports/integration-with-jasperreports/
description: Descubra como integrar Aspose.PDF com JasperReports. Exporte relatórios perfeitamente para PDFs de nível profissional com funcionalidade aprimorada.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Para usar Aspose.PDF para JasperReports em seu aplicativo, copie **aspose.pdf.jasperreports.jar** da pasta \lib em **Aspose.PDF.JasperReports.zip** para o diretório JasperReports\lib ou para uma pasta de biblioteca de seu aplicativo. Depois disso, você poderá acessar os exportadores de forma programática.

{{% /alert %}}

O exemplo a seguir mostra o código típico necessário para exportar um relatório para o formato PDF usando Aspose.PDF para JasperReports. Mais exemplos podem ser encontrados nos relatórios de demonstração incluídos no download do produto.

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

O trecho de código acima foi testado com JasperReports 3.5.2. Se estiver usando JasperReports 3.1.0, tente usar import com.aspose.pdf.jr3_1_0.jasperreports.; e substitua a versão do produto no restante do código também.

