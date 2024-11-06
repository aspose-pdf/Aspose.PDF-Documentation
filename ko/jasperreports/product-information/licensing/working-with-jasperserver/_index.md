---

title: Working with JasperServer

type: docs

weight: 20

url: ko/jasperreports/working-with-jasperserver/

lastmod: "2021-06-05"

---



#### <ins>**applicationContext.xml에서 licenseFile Exporter 매개변수 설정**

{{% alert color="primary" %}}



이 방법은 JasperServer와 함께 사용됩니다.



{{% /alert %}}



1. 라이센스를 컴퓨터에 다운로드하고 ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF``` 폴더에 복사합니다. 여기서 ```<InstallDir>```는 JasperServer 설치 디렉토리를 의미합니다.

2. ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml``` 파일을 찾아서 다음 줄을 추가합니다:



```

 <bean id="AsposeExportParameters" class="comcom.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-pro-3.7.1/apache-tomcat/webapps/jasperserver-pro/WEB-  

    INF/Aspose.Total.JasperReports.lic"/>

</bean>

```

{{% alert color="primary" %}}


참고: 설치 경로에 공백이 포함되어 있으면 안 됩니다. 예를 들어 C:/Program Files/JasperServer…와 같이 공백이 포함된 경우 라이센스 파일에 접근할 때 문제가 발생합니다.

{{% /alert %}}



#### **라이선스가 작동하는지 확인**

보고서를 PDF 형식으로 내보내고 보고서에 평가 메시지가 포함되어 있는지 확인하십시오. 평가 메시지가 없으면 라이선스가 제대로 작동하는 것입니다.



**Aspose.PDF for JasperReports는 평가 모드에서 작업할 때 워터마크를 삽입합니다**



![todo:image_alt_text](working-with-jasperserver_1.png)







**Aspose.PDF for JasperReports는 평가 모드에서 작업할 때 워터마크를 삽입합니다**



![todo:image_alt_text](working-with-jasperserver_2.png)