---
title: Como - usar Aspose.Pdf para demos offline do JasperReports
type: docs
weight: 10
url: /pt/jasperreports/how-to-use-aspose-pdf-for-jasperreports-offline-demos/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF para JasperReports inclui vários projetos de demonstração para ajudá-lo a começar a exportar relatórios para formatos PDF a partir da sua aplicação. As demonstrações são demonstrações padrão do JasperReports que foram modificadas para demonstrar como usar novos exportadores.

{{% /alert %}}
### **Executando Demos do Aspose.PDF para JasperReports**
Para executar demos do Aspose.PDF para JasperReports:

{{% alert color="primary" %}}

1. Baixe o JasperReports de <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>. Certifique-se de baixar todo o projeto arquivado com o código-fonte e demos, não apenas um único JAR.
2. Descompacte o projeto arquivado em algum local do seu disco rígido, por exemplo C:\.
3. 1. Copie todas as pastas de demonstração da pasta \demo em **Aspose.PDF.JasperReports.zip** para ```<InstallDir>```\jasperreports\demo\samples, onde ```<InstallDir>``` é o local onde você descompactou o JasperReports. Este passo é necessário porque os scripts de construção de demonstração dependem da estrutura de pastas do JasperReports, caso contrário, você terá que modificar os scripts de construção.
2. Copie o arquivo **aspose.pdf.jasperreports.jar** da pasta \lib em **Aspose.PDF.JasperReports.zip** para ```<InstallDir>```\jasperreports\lib.
3. Baixe a ferramenta ANT de <http://ant.apache.org/bindownload.cgi>.
4. Descompacte a ferramenta ANT e configure as variáveis de ambiente conforme descrito no manual da ferramenta.
5. Mude o diretório atual para ```<InstallDir>```\demo\hsqldb e execute o seguinte comando na linha de comando:
   ant runServer
6. Abra uma nova instância do prompt de comando e mude o diretório atual para uma das demonstrações do Aspose.PDF para JasperReports, por exemplo, ```<InstallDir>```\demo\samples\charts.ap.
7. Execute os seguintes comandos na linha de comando:
8. ant javac – para compilar os arquivos fonte Java da aplicação de teste.  
11. ant compile – para compilar o design do relatório XML e produzir o arquivo .jasper  
12. ant fill – para preencher o design do relatório compilado com dados e produzir o arquivo .jrprint  
13. Execute o seguinte comando na linha de comando:  
   ant pdf – para produzir um arquivo PDF a partir do relatório de demonstração.  
14. Abra um dos documentos resultantes para visualizar, por exemplo ```<InstallDir>```\demo\samples\charts.ap\AreaChartReport.pdf no Adobe Reader ou em outra aplicação.  

{{% /alert %}}