title: JasperReports와의 통합

type: docs

weight: 20

url: /ko/jasperreports/integration-with-jasperreports/

lastmod: "2021-06-05"

---

{{% alert color="primary" %}}

응용 프로그램에서 Aspose.PDF for JasperReports를 사용하려면 **Aspose.PDF.JasperReports.zip**의 \lib 폴더에서 **aspose.pdf.jasperreports.jar**를 JasperReports\lib 디렉토리 또는 응용 프로그램의 라이브러리 폴더로 복사하십시오. 그런 다음 프로그래밍 방식으로 내보내기에 액세스할 수 있습니다.

{{% /alert %}}

다음 예제는 Aspose.PDF for JasperReports를 사용하여 보고서를 PDF 형식으로 내보내는 데 필요한 일반적인 코드를 보여줍니다. 제품 다운로드에 포함된 데모 보고서에서 더 많은 예제를 찾을 수 있습니다.

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

위의 코드 스니펫은 JasperReports 3.5.2로 테스트되었습니다. JasperReports 3.1.0을 사용하는 경우, import com.aspose.pdf.jr3_1_0.jasperreports.;를 사용해 보고 나머지 코드에서도 제품 버전을 교체해 보세요.
```