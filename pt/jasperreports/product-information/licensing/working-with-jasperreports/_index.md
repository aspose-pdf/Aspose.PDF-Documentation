---
title: Trabalhando com JasperReports
linktitle: Trabalhando com JasperReports
type: docs
weight: 10
url: /pt/jasperreports/working-with-jasperreports/
description: Domine o trabalho com JasperReports usando Aspose.PDF. Crie e exporte relatórios detalhados em formato PDF com recursos avançados.
lastmod: "2026-09-09"
---

{{% alert color="primary" %}}

Aspose.Words for JasperReports está disponível gratuitamente, com avaliação ilimitada de tempo a partir da página de download. A versão de avaliação e a versão licenciada do produto são o mesmo download.

Quando você estiver satisfeito com a versão de avaliação, [purchase a license](http://www.aspose.com/purchase/default.aspx). Certifique‑se de que entende e concorda com os termos da licença.

{{% /alert %}}

A licença está disponível para download na página de pedido após o pagamento do pedido. A licença é um arquivo XML de texto puro, assinado digitalmente. A licença contém informações como o nome do cliente, o produto adquirido e o tipo da licença. Não modifique o conteúdo do arquivo de licença: isso invalida a licença.

Existem várias maneiras de ativar uma licença:

- [Chame o método setLicense](/pdf/pt/jasperreports/working-with-jasperreports/#call-setlicense).
- [Definir um parâmetro de exportador no código](/pdf/pt/jasperreports/working-with-jasperreports/#set-the-licensefile-exporter-parameter-in-the-code).
- [Definir um parâmetro de exportador no **applicationContext.xml**](/pdf/pt/jasperreports/working-with-jasperserver/).

Os dois primeiros são usados com JasperReports, o último com JasperServer.

## Chame setLicense

Este método é usado com JasperReports.

1. Faça o download da licença para o seu computador e copie-a para a pasta apropriada (por exemplo, a pasta da sua aplicação ou JasperReports\lib).
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

## Defina o parâmetro licenseFile Exporter no código

Este método é usado com JasperReports.

1. Faça o download da licença para o seu computador e copie-a para a pasta apropriada (por exemplo, a pasta da sua aplicação ou JasperReports\lib).
2. Adicione o seguinte código ao seu projeto:

```java

import com.aspose.pdf.jr3_7_0.jasperreports.*;

com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();
exporter.setParameter(PdfExporterParameter.LICENSE, "Aspose.PDF.JasperReports.lic");
exporter.exportReport();

```

