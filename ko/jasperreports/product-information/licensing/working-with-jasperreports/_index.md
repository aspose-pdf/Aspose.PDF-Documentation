---

title: Working with JasperReports

type: docs

weight: 10

url: ko/jasperreports/working-with-jasperreports/

lastmod: "2021-06-05"

---

{{% alert color="primary" %}}

Aspose.Words for JasperReports는 다운로드 페이지에서 무료로 시간 제한 없이 평가판을 사용할 수 있습니다. 제품의 평가판과 라이선스 버전은 동일한 다운로드입니다.

평가판에 만족하시면, [라이선스를 구매하세요](http://www.aspose.com/purchase/default.aspx). 라이선스 조건을 이해하고 동의하는지 확인하세요.

{{% /alert %}}

라이선스는 주문이 완료된 후 주문 페이지에서 다운로드할 수 있습니다. 라이선스는 클리어 텍스트로 된 디지털 서명된 XML 파일입니다. 라이선스에는 클라이언트 이름, 구매한 제품 및 라이선스 유형과 같은 정보가 포함되어 있습니다. 라이선스 파일의 내용을 수정하지 마세요: 라이선스가 무효화됩니다.

라이선스를 활성화하는 몇 가지 방법이 있습니다:

- [setLicense 호출하기](/pdf/jasperreports/working-with-jasperreports/#call-setlicense).

- [코드에서 내보내기 매개변수 설정하기](/pdf/jasperreports/working-with-jasperreports/#set-the-licensefile-exporter-parameter-in-the-code).

- [**applicationContext.xml**에서 내보내기 매개변수 설정](/pdf/jasperreports/working-with-jasperserver/).



처음 두 개는 JasperReports와 함께 사용되고, 마지막은 JasperServer와 함께 사용됩니다.

#### **setLicense 호출**

<ins> **이 메서드는 JasperReports와 함께 사용됩니다.**



1. 컴퓨터에 라이선스를 다운로드하고 적절한 폴더(예: 애플리케이션 폴더 또는 JasperReports\lib)에 복사합니다.

2. 프로젝트에 다음 코드를 추가합니다:



```

import com.aspose.pdf.jr3_7_0.jasperreports.*;

try

{ 

    // 라이선스 파일을 포함하는 스트림 객체 생성

   FileInputStream fstream = new FileInputStream("C:\\Aspose.PDF.JasperReports.lic");  



    // 스트림 객체를 통해 라이선스 설정

 

   License license = new License();

   license.setLicense(fstream);

}

catch(Exception ex)

{

   System.out.println(ex.toString());

}



```



#### **코드에서 licenseFile 내보내기 매개변수 설정**



<ins> **이 메서드는 JasperReports와 함께 사용됩니다.**



1. 라이센스를 컴퓨터에 다운로드하고 적절한 폴더(예: 애플리케이션 폴더 또는 JasperReports\lib)에 복사합니다.

2. 다음 코드를 프로젝트에 추가합니다:
   
```
import com.aspose.pdf.jr3_7_0.jasperreports.*;

com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();
exporter.setParameter(PdfExporterParameter.LICENSE, "Aspose.PDF.JasperReports.lic");
exporter.exportReport();
```