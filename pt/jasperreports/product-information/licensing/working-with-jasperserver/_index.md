---

title: Trabalhando com JasperServer

type: docs

weight: 20

url: /pt/jasperreports/working-with-jasperserver/

lastmod: "2021-06-05"

---



#### <ins>**Defina o parâmetro licenseFile no applicationContext.xml**

{{% alert color="primary" %}}



Este método é usado com o JasperServer.



{{% /alert %}}



1. Baixe a licença para o seu computador e copie-a para a pasta ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF```, onde ```<InstallDir>``` representa o diretório de instalação do JasperServer.

2. Localize o arquivo ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml``` e adicione as seguintes linhas:



```

 <bean id="AsposeExportParameters" class="comcom.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-pro-3.7.1/apache-tomcat/webapps/jasperserver-pro/WEB-  

    INF/Aspose.Total.JasperReports.lic"/>

</bean>

```

{{% alert color="primary" %}}


Nota: Por favor, note que o caminho de instalação não deve conter espaços, por exemplo C:/Program Files/JasperServer… pois isso causa problemas ao acessar o arquivo de licença.

{{% /alert %}}



#### **Verifique se a Licença Funciona**

Exporte qualquer relatório para o formato PDF e verifique se o relatório contém uma mensagem de avaliação. Se não houver mensagem de avaliação, então a licença está funcionando corretamente.



**Aspose.PDF para JasperReports injeta uma marca d'água quando trabalha no modo de avaliação**



![todo:image_alt_text](working-with-jasperserver_1.png)







**Aspose.PDF para JasperReports injeta uma marca d'água quando trabalha no modo de avaliação**



![todo:image_alt_text](working-with-jasperserver_2.png)