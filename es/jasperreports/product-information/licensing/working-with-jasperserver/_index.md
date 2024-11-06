---
title: Trabajando con JasperServer
type: docs
weight: 20
url: es/jasperreports/working-with-jasperserver/
lastmod: "2021-06-05"
---

#### <ins>**Establecer el parámetro licenseFile Exporter en applicationContext.xml**
{{% alert color="primary" %}}

Este método se utiliza con JasperServer.

{{% /alert %}}

1. Descargue la licencia a su computadora y cópiela en la carpeta ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF```, donde ```<InstallDir>``` representa el directorio de instalación de JasperServer.
2. Localice el archivo ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml``` y agregue las siguientes líneas:

```
<bean id="AsposeExportParameters" class="comcom.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">
    <property name="licenseFile" value="C:/jasperserver-pro-3.7.1/apache-tomcat/webapps/jasperserver-pro/WEB-  
    INF/Aspose.Total.JasperReports.lic"/>

</bean>
```
{{% alert color="primary" %}}
Nota: Tenga en cuenta que la ruta de instalación no debe contener espacios, por ejemplo, C:/Program Files/JasperServer… ya que eso causa problemas al acceder al archivo de licencia.
{{% /alert %}}

#### **Verificar que la Licencia Funciona**
Exporte cualquier informe a formato PDF y verifique si el informe contiene un mensaje de evaluación. Si no hay un mensaje de evaluación, entonces la licencia está funcionando correctamente.

**Aspose.PDF para JasperReports inyecta una marca de agua cuando se trabaja en modo de evaluación**

![todo:image_alt_text](working-with-jasperserver_1.png)



**Aspose.PDF para JasperReports inyecta una marca de agua cuando se trabaja en modo de evaluación**

![todo:image_alt_text](working-with-jasperserver_2.png)