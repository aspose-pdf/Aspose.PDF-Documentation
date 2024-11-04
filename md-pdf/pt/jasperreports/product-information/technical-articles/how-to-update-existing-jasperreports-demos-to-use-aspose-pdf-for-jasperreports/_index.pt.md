---
title: Como - Atualizar demos existentes do JasperReports para usar o Aspose.Pdf para JasperReports
type: docs
weight: 20
url: /jasperreports/how-to-update-existing-jasperreports-demos-to-use-aspose-pdf-for-jasperreports/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF para JasperReports inclui uma série de projetos de demonstração para ajudá-lo a começar a exportar relatórios para PDF. Estas demonstrações são baseadas em demonstrações padrão do JasperReports que foram modificadas para demonstrar como usar novos exportadores. Este tutorial percorre os passos necessários para atualizar as demonstrações existentes do JasperReports para usar o Aspose.PDF para JasperReports.

{{% /alert %}}
### **Atualizando Demos para usar Aspose.PDF**

{{% alert color="primary" %}}

Os seguintes passos explicam como atualizar as demonstrações existentes para usar a extensão de exportação Aspose.PDF para JasperReports em vez de usar o recurso padrão de exportação em PDF do JasperReports.

1. Baixe o JasperReports de <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>.
   Certifique-se de baixar todo o projeto arquivado com o código-fonte e demos, não apenas um único JAR. Este tutorial foi preparado usando JasperReports-3.5.2.  
2. Descompacte o projeto arquivado em algum local no seu disco rígido, por exemplo C:\.  
3. Copie **aspose.pdf.jasperreports.jar** da pasta \lib em **Aspose.PDF.JasperReports.zip** para ```<InstallDir>```\jasperreports\lib.  
4. Abra ```<InstallDir>```\jasperreports\demo\samples, (onde ```<InstallDir>``` é o local onde você descompactou o JasperReports) para atualizar um demo existente. Se você escolheu o demo de fontes, por exemplo, para usar com Aspose.PDF para JasperReports, crie uma cópia dele para que o demo original permaneça o mesmo. Para o propósito deste exemplo, nomeamos a nova pasta como **fonts.ap**.  
Nota: os demos serão executados a partir de ```<InstallDir>``` \jasperreports\demo\samples porque os scripts de construção dos demos dependem da estrutura de pastas do JasperReports. Se você mudar a pasta de exemplo, você terá que modificar os scripts de construção.  
5. Abra o arquivo **FontsApp.java** da pasta src e adicione uma referência ao Aspose.PDF para JasperReports:  

   import com.aspose.pdf.jr3_7_0.jasperreports.*;(Estamos usando jr3_7_0 porque este tutorial foi preparado com JasperReports 3.5.2.)
6. Adicione uma nova string:
   private static final String TASK_ASPOSE_PDF = "aspose_pdf"; juntamente com as variáveis existentes como uma opção de exportação via Aspose.PDF para JasperReports.
7. Localize o segmento de código for else if (TASK_PDF.equals(taskName)) e copie todo o segmento.
8. Cole o trecho de código sob o mesmo segmento.

```
 else if (TASK_PDF.equals(taskName))
{
  File sourceFile = new File(fileName);
  JasperPrint jasperPrint = (JasperPrint)JRLoader.loadObject(sourceFile);
  File destFile = new File(sourceFile.getParent(), jasperPrint.getName() + ".pdf");
  JRPdfExporter exporter = new JRPdfExporter();
  HashMap fontMap = new HashMap();
  FontKey key = new FontKey("DejaVu Serif", true, false);
  PdfFont font = new PdfFont("DejaVuSerif-Bold.ttf", "Cp1252", true);
  fontMap.put(key, font);
  exporter.setParameter(JRExporterParameter.JASPER_PRINT, jasperPrint);

  exporter.setParameter(JRExporterParameter.OUTPUT_FILE_NAME, destFile.toString());
```java
exporter.setParameter(JRExporterParameter.FONT_MAP, fontMap);
exporter.exportReport();
System.err.println("Tempo de criação do PDF : " + (System.currentTimeMillis() - start));
}
```

```
update
else if (TASK_PDF.equals(taskName))
as
else if (TASK_ASPOSE_PDF.equals(taskName))
replace
JRPdfExporter exporter = new JRPdfExporter();
with
com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new
com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();
```
9. Abra o arquivo **build.xml**.
10. Faça uma cópia do seguinte segmento e coloque-o dentro do mesmo arquivo:

```
<target name="pdf" description="Gerar PDF via Aspose.PDF para JasperReports.">
    <java classname="${class.name}">
        <arg value="pdf"/>
        <arg value="${file.name}.jrprint"/>
        <classpath refid="classpath"/>
    </java>
</target>
```

```
update  name="pdf"  as   name="aspose_pdf"
update  <arg value="pdf"/>  as   <arg value="aspose_pdf"/>
```

11. Para executar a demonstração:

   - Baixe a ferramenta ANT de <http://ant.apache.org/bindownload.cgi>.
```
- Descompacte a ferramenta ANT e configure as variáveis de ambiente conforme descrito no manual da ferramenta.
- Altere o diretório atual para <InstallDir>\demo\hsqldb e execute o seguinte comando na linha de comando:
  ant runServer
12. Abra uma nova instância do prompt de comando e altere o diretório atual para <InstallDir>\demo\samples\fonts.ap e execute os seguintes comandos na linha de comando:
13. ant javac – para compilar os arquivos fonte Java da aplicação de teste
14. ant compile – para compilar o design do relatório XML e produzir o arquivo .jasper
15. ant fill – para preencher o design do relatório compilado com dados e produzir o arquivo .jrprint
16. ant aspose_pdf – para produzir um arquivo PDF usando Aspose.PDF para JasperReports.
17. Abra o PDF resultante (**FontsReport.pdf**) da pasta <InstallDir>\demo\samples\ fonts.ap\build\reports\.

{{% /alert %}}