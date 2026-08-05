---
title: Trabalhando com JasperReports
linktitle: Trabalhando com JasperReports
type: docs
weight: 10
url: /pt/jasperreports/working-with-jasperreports/
description: Domine o trabalho com JasperReports usando Aspose.PDF. Crie e exporte relatórios detalhados em formato PDF com recursos avançados.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.Words for JasperReports está disponível para avaliação gratuita e por tempo ilimitado na página de download. As versões de avaliação e licenciadas do produto são o mesmo download.

Quando estiver satisfeito com a versão de avaliação, [adquira uma licença](http://www.aspose.com/purchase/default.aspx). Certifique-se de compreender e concordar com os termos da licença.

{{% /alert %}}

A licença está disponível para download na página do pedido após o pagamento do pedido. A licença é um arquivo XML de texto não criptografado e assinado digitalmente. A licença contém informações como o nome do cliente, o produto adquirido e o tipo de licença. Não modifique o conteúdo do arquivo de licença: isso invalida a licença.

Existem várias maneiras de ativar uma licença:

- [Chamada setLicense](/pdf/pt/jasperreports/working-with-jasperreports/#call-setlicense).
- [Defina um parâmetro de exportador no código](/pdf/pt/jasperreports/working-with-jasperreports/#set-the-licensefile-exporter-parameter-in-the-code).
- [Set an exporter parameter in **applicationContext.xml**](/pdf/pt/jasperreports/working-with-jasperserver/).

Os dois primeiros são usados ​​com JasperReports, o último com JasperServer.

## Conjunto de chamadasLicença

Este método é usado com JasperReports.

1. Baixe a licença para o seu computador e copie-a para a pasta apropriada (por exemplo, a pasta do seu aplicativo ou JasperReports\lib).
2. Adicione o seguinte código ao seu projeto:

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

## Defina o parâmetro LicenseFile Exporter no código

Este método é usado com JasperReports.

1. Baixe a licença para o seu computador e copie-a para a pasta apropriada (por exemplo, a pasta do seu aplicativo ou JasperReports\lib).
2. Adicione o seguinte código ao seu projeto:

```java

import com.aspose.pdf.jr3_7_0.jasperreports.*;

com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();
exporter.setParameter(PdfExporterParameter.LICENSE, "Aspose.PDF.JasperReports.lic");
exporter.exportReport();

```


