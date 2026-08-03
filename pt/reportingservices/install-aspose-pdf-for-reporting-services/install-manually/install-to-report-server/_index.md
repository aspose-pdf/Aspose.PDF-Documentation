---
title: Instalar no servidor de relatório
linktitle: Install to Report Server
type: docs
weight: 10
url: /reportingservices/install-to-report-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Você só precisará seguir essas etapas se instalar o Aspose.PDF para Reporting Services manualmente, sem usar o instalador MSI. O instalador MSI executa todas as ações necessárias de instalação e registro automaticamente.

{{% /alert %}}

Nas etapas a seguir, você precisará copiar e modificar arquivos no diretório onde o Microsoft SQL Server Reporting Services está instalado. O assembly do SSRS 2016 está localizado no diretório \Bin\SSRS2016 do pacote zip; o assembly SSRS 2017 está localizado no diretório \Bin\SSRS2017; o assembly SSRS 2019 está localizado no diretório \Bin\SSRS2019; o assembly SSRS 2022 está localizado no diretório \Bin\SSRS2022; o assembly do Servidor de Relatórios do Power BI está localizado no diretório \Bin\PowerBI.

**Etapa 1.** Localize o diretório de instalação do Report Server. O diretório raiz do Microsoft SQL Server geralmente é C:\Program Files\Microsoft SQL Server. O processo adicional é um pouco diferente para o Reporting Services 2016, o Reporting Services 2017 e posterior e o Power BI Report Server:

- O Report Server 2016, por padrão, é instalado no diretório C:\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer. Se você estiver usando instâncias nomeadas personalizadas em vez da padrão, o caminho padrão será C:\Program Files\Microsoft SQL Server\MSRS13.[SSRSInstanceName]\Reporting Services\ReportServer
- O Report Server 2017 e posterior, por padrão, é instalado no diretório C:\Program Files\Microsoft SQL Server Reporting Services\SSRS\ReportServer.
- Por padrão, o Power BI Report Server é instalado no diretório C:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServer.

No texto a seguir, o diretório de instalação do Reporting Services (um dos caminhos mencionados acima) será referenciado como `<Instance>`.

**Etapa 2.** Copie Aspose.Pdf.ReportingServices.dll da versão SSRS correspondente para a pasta `<Instance>\bin`.

**Etapa 3.** Registre Aspose.PDF para Reporting Services como uma extensão de renderização. Abra o arquivo `<Instance>\rsreportserver.config` e adicione as seguintes linhas ao elemento `<Render>`:

## Exemplo

```xml
<Render>
...
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices"/>
</Render>
```

**Etapa 4.** Forneça ao Aspose.PDF para Reporting Services permissões de execução. Abra o arquivo `<Instance>\rssrvpolicy.config` e adicione o seguinte texto como o último item no segundo elemento externo `<CodeGroup>` que deve ser `<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">):`

## Exemplo

```xml

 <CodeGroup>
...

<CodeGroup>
...

<!--Start here.-->

<CodeGroup class="UnionCodeGroup" version="1" PermissionSetName="FullTrust"

Name="Aspose.Pdf_for_Reporting_Services" Description="This code group grants full trust to the AP4SSRS assembly.">

<IMembershipCondition class="StrongNameMembershipCondition" version="1" PublicKeyBlob="00240000048000009400000006020000002400005253413100040000010001005542e99cecd28842dad186257b2c7b6ae9b5947e51e0b17b4ac6d8cecd3e01c4d20658c5e4ea1b9a6c8f854b2d796c4fde740dac65e834167758cff283eed1be5c9a812022b015a902e0b97d4e95569eb8c0971834744e633d9cb4c4a6d8eda03c12f486e13a1a0cb1aa101ad94943236384cbbf5c679944b994de9546e493bf " />

</CodeGroup>

<!--End here. -->

</CodeGroup>

</CodeGroup>
```

**Etapa 5.** Verifique se o Aspose.PDF para Reporting Services foi instalado com êxito. Abra o portal da Web Reporting Services e verifique a lista de formatos de exportação disponíveis para um relatório. Você pode iniciar o portal da web iniciando um navegador da web e digitando o URL do portal da web do Reporting Services na barra de endereço (por padrão é http://`<Reporting_Services_server_name>`/reports/). Selecione um dos relatórios disponíveis em seu portal da web e abra a lista suspensa Exportar. Você deverá ver a lista de formatos de exportação, incluindo aqueles fornecidos pela extensão Aspose.PDF para Reporting Services. Selecione PDF por meio do item Aspose.PDF.

![Install to report server](install-to-report-server_1.png)

Clique no item selecionado. Ele irá gerar o relatório no formato selecionado, enviá-lo ao cliente e, dependendo das configurações do seu navegador, mostrar a caixa de diálogo Salvar arquivo para escolher onde salvar o relatório exportado ou baixar automaticamente o arquivo para sua pasta Downloads.

Parabéns, você instalou com sucesso o Aspose.PDF for Reporting Services e exportou um relatório como um documento PDF!


