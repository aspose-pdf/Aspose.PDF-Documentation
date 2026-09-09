---
title: JasperReports와 작업하기
linktitle: JasperReports와 작업하기
type: docs
weight: 10
url: /ko/jasperreports/working-with-jasperreports/
description: Aspose.PDF를 사용하여 JasperReports 작업을 마스터하십시오. 고급 기능을 사용하여 PDF 형식으로 자세한 보고서를 만들고 내보냅니다.
lastmod: "2026-09-09"
---

{{% alert color="primary" %}}

Aspose.Words for JasperReports는 다운로드 페이지에서 무제한 무료 평가판으로 제공됩니다. 평가판과 정식 라이선스 버전은 동일한 다운로드 파일입니다.

평가 버전이 만족스러우면, [purchase a license](http://www.aspose.com/purchase/default.aspx). 라이선스 조건을 이해하고 동의했는지 확인하십시오.

{{% /alert %}}

주문이 결제된 후 주문 페이지에서 라이선스를 다운로드할 수 있습니다. 라이선스는 일반 텍스트이며 디지털 서명된 XML 파일입니다. 라이선스에는 클라이언트 이름, 구매한 제품 및 라이선스 유형과 같은 정보가 포함됩니다. 라이선스 파일의 내용을 수정하지 마십시오: 라이선스가 무효화됩니다.

라이선스를 활성화하는 방법에는 여러 가지가 있습니다:

- [Call setLicense](/pdf/ko/jasperreports/working-with-jasperreports/#call-setlicense).
- [Set an exporter parameter in the code](/pdf/ko/jasperreports/working-with-jasperreports/#set-the-licensefile-exporter-parameter-in-the-code).
- [Set an exporter parameter in **applicationContext.xml**](/pdf/ko/jasperreports/working-with-jasperserver/).

처음 두 개는 JasperReports와 함께 사용되고, 마지막은 JasperServer와 함께 사용됩니다.

## setLicense를 호출합니다

이 메서드는 JasperReports와 함께 사용됩니다.

1. 라이선스를 컴퓨터에 다운로드한 뒤 적절한 폴더(예: 애플리케이션의 폴더 또는 JasperReports\lib)로 복사합니다.
2. 프로젝트에 다음 코드를 추가합니다:

```java
import com.aspose.pdf.jr3_7_0.jasperreports.*;
try
{ 
    // create a stream object containing the license file
   FileInputStream fstream = new FileInputStream("C:\\Aspose.PDF.JasperReports.lic");  

    // Set the license through the stream object
 
   License license = new License();
   license.setLicense(fstream);
}
catch(Exception ex)
{
   System.out.println(ex.toString());
}

```

## 코드에서 licenseFile Exporter 매개변수를 설정합니다

이 메서드는 JasperReports와 함께 사용됩니다.

1. 라이선스를 컴퓨터에 다운로드한 뒤 적절한 폴더(예: 애플리케이션의 폴더 또는 JasperReports\lib)로 복사합니다.
2. 프로젝트에 다음 코드를 추가합니다:

```java

import com.aspose.pdf.jr3_7_0.jasperreports.*;

com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();
exporter.setParameter(PdfExporterParameter.LICENSE, "Aspose.PDF.JasperReports.lic");
exporter.exportReport();

```

