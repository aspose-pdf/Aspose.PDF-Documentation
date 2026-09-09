---
title: Trabalhar com JasperServer
linktitle: Trabalhar com JasperServer
type: docs
weight: 20
description: Descubra como trabalhar eficientemente com o JasperServer utilizando o Aspose.PDF. Exporte relatórios para PDFs profissionais com facilidade.
lastmod: "2021-06-05"
---

## <ins>Set the licenseFile Exporter Parameter in applicationContext.xml

{{% alert color="primary" %}}

Este método é utilizado com o JasperServer.

{{% /alert %}}

1. Descarregue a licença para o seu computador e copie-a para a pasta ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF```, onde ```<InstallDir>``` representa o directório de instalação do JasperServer.
2. Localize o ficheiro ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml``` e adicione as seguintes linhas:

```xml
 <bean id="AsposeExportParameters" class="comcom.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">
    <property name="licenseFile" value="C:/jasperserver-pro-3.7.1/apache-tomcat/webapps/jasperserver-pro/WEB-  
    INF/Aspose.Total.JasperReports.lic"/>
</bean>
```

{{% alert color="primary" %}}
Nota: O caminho de instalação não deve conter espaços (por exemplo, C:/Program Files/JasperServer…), uma vez que isso causa problemas no acesso ao ficheiro de licença.
{{% /alert %}}

## Verifique se a licença funciona

Exporte qualquer relatório para formato PDF e verifique se o relatório contém mensagem de avaliação. Se não houver mensagem de avaliação, a licença está funcionando corretamente.

O Aspose.PDF for JasperReports insere uma marca de água ao operar no modo de avaliação.

![Integration with JasperServer_1](working-with-jasperserver_1.png)

Aspose.PDF for JasperReports injeta uma marca d'água ao trabalhar no modo de avaliação

![Integration with JasperServer_2](working-with-jasperserver_2.png)
