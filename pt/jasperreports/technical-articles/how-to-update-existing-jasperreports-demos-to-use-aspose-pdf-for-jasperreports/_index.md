---
title: Como fazer - Atualizar demonstrações existentes do JasperReports para usar Aspose.PDF for JasperReports
linktitle: Como fazer - Atualizar demonstrações existentes do JasperReports para usar Aspose.PDF for JasperReports
type: docs
weight: 20
url: /pt/jasperreports/how-to-update-existing-jasperreports-demos-to-use-aspose-pdf-for-jasperreports/
description: Aprenda como atualizar as demonstrações existentes do JasperReports para aproveitar os recursos do Aspose.PDF for JasperReports.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReports inclui vários projetos de demonstração para ajudá-lo a começar a exportar relatórios para PDF. Essas demonstrações são baseadas em demonstrações padrão do JasperReports que foram modificadas para demonstrar como usar novos exportadores. Este tutorial percorre as etapas necessárias para atualizar as demonstrações existentes do JasperReports para usar o Aspose.PDF for JasperReports.

{{% /alert %}}

## Atualizando demonstrações para usar Aspose.PDF

{{% alert color="primary" %}}

As etapas a seguir explicam como atualizar demonstrações existentes para usar a extensão de exportação Aspose.PDF for JasperReports em vez de usar o recurso de exportação de PDF padrão do JasperReport.

1. Baixe JasperReports em <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>.
   Certifique-se de baixar todo o projeto arquivado com o código-fonte e as demonstrações, não apenas um único JAR. Este tutorial foi preparado usando JasperReports-3.5.2.
2. Descompacte o projeto arquivado em algum local do seu disco rígido, por exemplo C:\.
3. Copie **aspose.pdf.jasperreports.jar** da pasta \lib em **Aspose.PDF.JasperReports.zip** para ```<InstallDir>```\jasperreports\lib.
4. Abra ```<InstallDir>```\jasperreports\demo\samples, (where ```<InstallDir>``` é o local onde você descompactou o JasperReports) para atualizar uma demonstração existente. Se você selecionou a demonstração de fontes, por exemplo, para usar com Aspose.PDF for JasperReports, crie uma cópia dela para que a demonstração original permaneça a mesma. Para fins deste exemplo, nomeamos a nova pasta **fonts.ap**.
Nota: as demos serão executadas em ```<InstallDir>``` \jasperreports\demo\samples porque os scripts de construção de demonstração dependem da estrutura de pastas do JasperReports. Se você alterar a pasta de amostra, será necessário modificar os scripts de construção.
5. Abra o arquivo **FontsApp.java** da pasta src e adicione uma referência a Aspose.PDF for JasperReports:
   importar com.aspose.pdf.jr3_7_0.jasperreports.*;
   (Estamos usando jr3_7_0 porque este tutorial foi preparado com JasperReports 3.5.2.)
6. Adicione uma nova string:
   string final estático privado TASK_ASPOSE_PDF = "aspose_pdf"; junto com variáveis ​​existentes como uma opção de exportação via Aspose.PDF for JasperReports.
7. Localize o segmento de código for else if (TASK_PDF.equals(taskName)) e copie o segmento inteiro.
8. Cole o snippet de código no mesmo segmento.

```java
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
  exporter.setParameter(JRExporterParameter.FONT_MAP, fontMap);
  exporter.exportReport();
  System.err.println("PDF creation time : " + (System.currentTimeMillis() - start));
}
```

```text
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

```xml
 <target name="pdf" description="Generat PDF via Aspose.PDF for JasperReports.">
    <java classname="${class.name}">
        <arg value="pdf"/>
        <arg value="${file.name}.jrprint"/>
        <classpath refid="classpath"/>
    </java>
</target>
```

```diff
update  name="pdf"  as   name="aspose_pdf"
update  <arg value="pdf"/>  as   <arg value="aspose_pdf"/>
```

11. Para executar a demonstração:
   -  Baixe a ferramenta ANT em <http://ant.apache.org/bindownload.cgi>.
   - Descompacte a ferramenta ANT e configure as variáveis ​​de ambiente conforme descrito no manual da ferramenta.
   -  Altere o diretório atual para <InstallDir>\demo\hsqldb e execute a seguinte linha de comando:
      ant runServer
12. Abra uma nova instância do prompt de comando e altere o diretório atual para <InstallDir>\demo\samples\fonts.ap e execute os seguintes comandos na linha de comando:
13. ant javac – para compilar os arquivos fonte Java do aplicativo de teste
14. ant compile – para compilar o design do relatório XML e produzir o arquivo .jasper
15. ant fill – para preencher o design do relatório compilado com dados e produzir o arquivo .jrprint
16. ant aspose_ pdf – para produzir um arquivo PDF usando Aspose.PDF for JasperReports.
17. Abra o PDF resultante (**FontsReport.pdf**) na pasta <InstallDir>\demo\samples\ fonts.ap\build\reports\.

{{% /alert %}}

