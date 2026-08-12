---
title: JasperReports와 통합
linktitle: JasperReports와 통합
type: docs
weight: 20
url: /ko/jasperreports/integration-with-jasperreports/
description: Aspose.PDF를 JasperReports와 통합하는 방법을 알아보세요. 향상된 기능을 통해 보고서를 전문가 수준의 PDF로 원활하게 내보낼 수 있습니다.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

애플리케이션에서 Aspose.PDF for JasperReports를 사용하려면 **Aspose.PDF.JasperReports.zip**의 \lib 폴더에서 **aspose.pdf.jasperreports.jar**를 JasperReports\lib 디렉터리나 애플리케이션의 라이브러리 폴더로 복사하세요. 그런 다음 프로그래밍 방식으로 내보내기에 액세스할 수 있습니다.

{{% /alert %}}

다음 예는 Aspose.PDF for JasperReports를 사용하여 보고서를 PDF 형식으로 내보내는 데 필요한 일반적인 코드를 보여줍니다. 제품 다운로드에 포함된 데모 보고서에서 더 많은 예를 확인할 수 있습니다.

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

위의 코드 조각은 JasperReports 3.5.2에서 테스트되었습니다. JasperReports 3.1.0을 사용하는 경우 import com.aspose.pdf.jr3_1_0.jasperreports를 사용해 보십시오.; 코드의 나머지 부분에서도 제품 버전을 교체합니다.

