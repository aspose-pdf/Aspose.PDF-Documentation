---
title: JasperServer 작업
linktitle: JasperServer 작업
type: docs
weight: 20
description: Aspose.PDF를 사용하여 JasperServer로 효율적으로 작업하는 방법을 살펴보세요. 보고서를 전문적인 PDF로 쉽게 내보낼 수 있습니다.
lastmod: "2021-06-05"
---

## <ins>applicationContext.xml에서 LicenseFile 내보내기 매개변수 설정

{{% alert color="primary" %}}

이 방법은 JasperServer와 함께 사용됩니다.

{{% /alert %}}

1. 라이선스를 컴퓨터에 다운로드하고 JasperServer 설치 디렉터리를 의미하는 ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF``` folder, where  ```<InstallDir>```에 복사하세요.
2. ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml``` 파일을 찾아 다음 줄을 추가하세요:

```xml
 <bean id="AsposeExportParameters" class="comcom.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">
    <property name="licenseFile" value="C:/jasperserver-pro-3.7.1/apache-tomcat/webapps/jasperserver-pro/WEB-  
    INF/Aspose.Total.JasperReports.lic"/>
</bean>
```

{{% alert color="primary" %}}
참고: 설치 경로에는 공백이 포함되어서는 안 됩니다(예: C:/Program Files/JasperServer…). 공백이 있으면 라이선스 파일에 액세스할 때 문제가 발생합니다.
{{% /alert %}}

## 라이센스가 작동하는지 확인

보고서를 PDF 형식으로 내보내고 보고서에 평가 메시지가 포함되어 있는지 확인하세요. 평가 메시지가 없으면 라이센스가 제대로 작동하는 것입니다.

Aspose.PDF for JasperReports는 평가 모드에서 작업할 때 워터마크를 삽입합니다.

![Integration with JasperServer_1](working-with-jasperserver_1.png)

Aspose.PDF for JasperReports는 평가 모드에서 작업할 때 워터마크를 삽입합니다.

![Integration with JasperServer_2](working-with-jasperserver_2.png)

