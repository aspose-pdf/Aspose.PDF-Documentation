---

title: Integração com JasperReports

type: docs

weight: 20

url: pt/jasperreports/integration-with-jasperreports/

lastmod: "2021-06-05"

---



{{% alert color="primary" %}}



Para usar o Aspose.PDF para JasperReports em sua aplicação, copie **aspose.pdf.jasperreports.jar** da pasta \lib no **Aspose.PDF.JasperReports.zip** para o diretório JasperReports\lib, ou para uma pasta de biblioteca de sua aplicação. Depois disso, você pode acessar os exportadores programaticamente.



{{% /alert %}}



O exemplo a seguir mostra o código típico necessário para exportar um relatório em formato PDF usando o Aspose.PDF para JasperReports. Mais exemplos podem ser encontrados nos relatórios de demonstração incluídos no download do produto.



{{< highlight csharp >}}





   import com.aspose.pdf.jr3_7_0.jasperreports.*;



   com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf. jr3_7_0.jasperreports.JrPdfExporter();





   File sourceFile = new File(fileName);




   JasperPrint jasperPrint = (JasperPrint)JRLoader.loadObject(sourceFile);


exporter.setParameter(JRExporterParameter.JASPER_PRINT, jasperPrint);

File destFile = new File(sourceFile.getParent(), jasperPrint.getName() + ".pdf");

exporter.setParameter(JRExporterParameter.OUTPUT_FILE_NAME, destFile.toString());

exporter.exportReport();

{{< /highlight >}}

O trecho de código acima foi testado com JasperReports 3.5.2. Se estiver usando JasperReports 3.1.0, por favor, tente usar import com.aspose.pdf.jr3_1_0.jasperreports.; e substitua a versão do produto no restante do código também.
```