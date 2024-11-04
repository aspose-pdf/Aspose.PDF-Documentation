---

title: Working with JasperReports

type: docs

weight: 10

url: /jasperreports/working-with-jasperreports/

lastmod: "2021-06-05"

---

{{% alert color="primary" %}}

Aspose.Words para JasperReports está disponível gratuitamente, por tempo ilimitado, para avaliação na página de download. As versões de avaliação e licenciada do produto são o mesmo download.

Quando você estiver satisfeito com a versão de avaliação, [compre uma licença](http://www.aspose.com/purchase/default.aspx). Certifique-se de entender e concordar com os termos da licença.

{{% /alert %}}

A licença está disponível para download na página de pedido após o pagamento do pedido. A licença é um arquivo XML assinado digitalmente em texto claro. A licença contém informações como o nome do cliente, o produto adquirido e o tipo de licença. Não modifique o conteúdo do arquivo de licença: isso invalida a licença.

Existem várias maneiras de ativar uma licença:

- [Chamar setLicense](/pdf/jasperreports/working-with-jasperreports/#call-setlicense).

- [Definir um parâmetro de exportador no código](/pdf/jasperreports/working-with-jasperreports/#set-the-licensefile-exporter-parameter-in-the-code).

- [Defina um parâmetro de exportador em **applicationContext.xml**](/pdf/jasperreports/working-with-jasperserver/).



Os dois primeiros são usados com JasperReports, o último com JasperServer.

#### **Chamar setLicense**

<ins> **Este método é usado com JasperReports.**



1. Baixe a licença para o seu computador e copie-a para a pasta apropriada (por exemplo, a pasta do seu aplicativo ou JasperReports\lib).

2. Adicione o seguinte código ao seu projeto:



```

import com.aspose.pdf.jr3_7_0.jasperreports.*;

try

{ 

    // criar um objeto de stream contendo o arquivo de licença

   FileInputStream fstream = new FileInputStream("C:\\Aspose.PDF.JasperReports.lic");  



    // Defina a licença através do objeto de stream

 

   License license = new License();

   license.setLicense(fstream);

}

catch(Exception ex)

{

   System.out.println(ex.toString());

}



```



#### **Defina o Parâmetro Exportador licenseFile no Código**



<ins> **Este método é usado com JasperReports.**



1. Baixe a licença para o seu computador e copie-a para a pasta apropriada (por exemplo, a pasta do seu aplicativo ou JasperReports\lib).

2. Adicione o seguinte código ao seu projeto:



```



import com.aspose.pdf.jr3_7_0.jasperreports.*;



com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();

exporter.setParameter(PdfExporterParameter.LICENSE, "Aspose.PDF.JasperReports.lic");

exporter.exportReport();



```