---
title: JasperReports 작업
linktitle: JasperReports 작업
type: docs
weight: 10
url: /ko/jasperreports/working-with-jasperreports/
description: Aspose.PDF를 사용하여 JasperReports 작업을 마스터하세요. 고급 기능을 사용하여 상세 보고서를 PDF 형식으로 생성하고 내보낼 수 있습니다.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

JasperReports용 Aspose.Words는 다운로드 페이지에서 시간 제한 없이 무료로 평가판을 사용할 수 있습니다. 제품의 평가판과 라이선스 버전은 동일한 다운로드입니다.

평가판에 만족하신다면, [라이센스를 구매하다](https://purchase.aspose.com/buy?ppId=98899). 라이센스 조항을 이해하고 동의했는지 확인하십시오.

{{% /alert %}}

라이선스는 주문 결제 후 주문 페이지에서 다운로드할 수 있습니다. 라이센스는 디지털 서명된 일반 텍스트 XML 파일입니다. 라이선스에는 클라이언트 이름, 구매한 제품, 라이선스 유형 등의 정보가 포함됩니다. 라이센스 파일의 내용을 수정하지 마십시오. 라이센스가 무효화됩니다.

라이센스를 활성화하는 방법에는 여러 가지가 있습니다.

- [setLicense 호출](/pdf/ko/jasperreports/working-with-jasperreports/#call-setlicense).
- [코드에서 내보내기 매개변수 설정](/pdf/ko/jasperreports/working-with-jasperreports/#set-the-licensefile-exporter-parameter-in-the-code).
- [**applicationContext.xml**에서 내보내기 매개변수 설정](/pdf/ko/jasperreports/working-with-jasperserver/).

처음 두 개는 JasperReports와 함께 사용되고 마지막은 JasperServer와 함께 사용됩니다.

## setLicense 호출

이 방법은 JasperReports와 함께 사용됩니다.

1. 라이센스를 컴퓨터에 다운로드하고 적절한 폴더(예: 응용 프로그램 폴더 또는 JasperReports\lib)에 복사합니다.
2. 프로젝트에 다음 코드를 추가합니다.

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

## 코드에서 LicenseFile 내보내기 매개변수 설정

이 방법은 JasperReports와 함께 사용됩니다.

1. 라이센스를 컴퓨터에 다운로드하고 적절한 폴더(예: 응용 프로그램 폴더 또는 JasperReports\lib)에 복사합니다.
2. 프로젝트에 다음 코드를 추가합니다.

```java

import com.aspose.pdf.jr3_7_0.jasperreports.*;

com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();
exporter.setParameter(PdfExporterParameter.LICENSE, "Aspose.PDF.JasperReports.lic");
exporter.exportReport();

```


