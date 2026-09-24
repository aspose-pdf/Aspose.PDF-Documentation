---
title: Como usar o Aspose.PDF para demonstrações offline do JasperReports
linktitle: Como usar o Aspose.PDF para demonstrações offline do JasperReports
type: docs
weight: 10
url: /pt/jasperreports/how-to-use-aspose-pdf-for-jasperreports-offline-demos/
description: Explore demonstrações off-line do Aspose.PDF for JasperReports. Aprenda implementações e recursos práticos de maneira prática.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReports inclui vários projetos de demonstração para ajudá-lo a começar a exportar relatórios para formatos PDF a partir do seu aplicativo. As demonstrações são demonstrações padrão do JasperReports que foram modificadas para demonstrar como usar novos exportadores.

{{% /alert %}}

## Executando Aspose.PDF para demonstrações do JasperReports

Para executar demonstrações do Aspose.PDF for JasperReports:

{{% alert color="primary" %}}

1. Baixe JasperReports de <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>. Certifique-se de baixar todo o projeto arquivado com o código-fonte e demonstrações, não apenas um único JAR.
2. Descompacte o projeto arquivado em algum local do seu disco rígido, por exemplo C:\.
3. Copie todas as pastas de demonstração da pasta \demo em **Aspose.PDF.JasperReports.zip** para ```<InstallDir>```\jasperreports\demo\samples, where ```<InstallDir>``` é o local para o qual você descompactou o JasperReports. Esta etapa é necessária porque os scripts de construção de demonstração dependem da estrutura de pastas JasperReports, caso contrário, você terá que modificar os scripts de construção.
4. Copie o arquivo **aspose.pdf.jasperreports.jar** da pasta \lib em **Aspose.PDF.JasperReports.zip** para ```<InstallDir>```\jasperreports\lib.
5. Baixe a ferramenta ANT em <http://ant.apache.org/bindownload.cgi>.
6. Descompacte a ferramenta ANT e configure as variáveis ​​de ambiente conforme descrito no manual da ferramenta.
7. Mude o diretório atual para ```<InstallDir>```\demo\hsqldb e execute a seguinte linha de comando:
   ant runServer
8. Abra a nova instância do prompt de comando e altere o diretório atual para uma das demonstrações do Aspose.PDF for JasperReports, por exemplo ```<InstallDir>```\demo\samples\charts.ap.
9. Execute os seguintes comandos na linha de comando:
10. ant javac – para compilar os arquivos fonte Java do aplicativo de teste.
11. ant compile – para compilar o design do relatório XML e produzir o arquivo .jasper
12. ant fill – para preencher o design do relatório compilado com dados e produzir o arquivo .jrprint
13. Execute o seguinte comando na linha de comando:
   ant pdf – para produzir um arquivo PDF do relatório de demonstração.
14. Abra um dos documentos resultantes para visualizar, por exemplo ```<InstallDir>```\demo\samples\charts.ap\AreaChartReport.pdf no Adobe Reader ou outro aplicativo.

{{% /alert %}}

