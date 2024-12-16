---
title: Instalar no Servidor de Relatórios
type: docs
weight: 10
url: /pt/reportingservices/install-to-report-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Você só precisa seguir estas etapas se instalar o Aspose.PDF para Reporting Services manualmente, sem usar o instalador MSI. O instalador MSI executa automaticamente todas as ações necessárias de instalação e registro.

{{% /alert %}}

Nas etapas a seguir, você precisará copiar e modificar arquivos no diretório onde o Microsoft SQL Server Reporting Services está instalado. O assembly SSRS 2016 está localizado no diretório \Bin\SSRS2016 do pacote zip; o assembly SSRS 2017 está localizado no diretório \Bin\SSRS2017; o assembly SSRS 2019 está localizado no diretório \Bin\SSRS2019; o assembly SSRS 2022 está localizado no diretório \Bin\SSRS2022; o assembly do Power BI Report Server está localizado no diretório \Bin\PowerBI.

{{% alert color="primary" %}}

**Etapa 1.** Localize o diretório de instalação do Servidor de Relatórios. O diretório raiz para o Microsoft SQL Server geralmente é C:\Program Files\Microsoft SQL Server. O processo é um pouco diferente para o Reporting Services 2016, Reporting Services 2017 e posteriores, e o Power BI Report Server:

- O Report Server 2016, por padrão, é instalado no diretório C:\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer. Se você estiver usando instâncias nomeadas personalizadas em vez da padrão, o caminho padrão será C:\Program Files\Microsoft SQL Server\MSRS13.[SSRSInstanceName]\Reporting Services\ReportServer
- O Report Server 2017 e posteriores, por padrão, são instalados no diretório C:\Program Files\Microsoft SQL Server Reporting Services\SSRS\ReportServer.
- O Power BI Report Server, por padrão, é instalado no diretório C:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServer.

No texto a seguir, o diretório de instalação do Reporting Services (um dos caminhos mencionados acima) será referenciado como ```<Instance>```.
**Passo 2.** Copie Aspose.Pdf.ReportingServices.dll para a versão correspondente do SSRS para a pasta ```<Instance>```\bin.
{{% /alert %}}

{{% alert color="primary" %}}
**Passo 3.** Registre o Aspose.Pdf para o Reporting Services como uma extensão de renderização. Abra o arquivo ```<Instance>```\rsreportserver.config e adicione as seguintes linhas no elemento ```<Render>```:
{{% /alert %}}

**Exemplo**

{{< highlight csharp >}}

 <Render>
...
<!--Start here.-->

<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices"/>

</Render>

{{< /highlight >}}

{{% alert color="primary" %}}
**Passo 4.** Conceda permissões ao Aspose.Pdf para o Reporting Services para executar. Abra o arquivo ```<Instance>```\rssrvpolicy.config e adicione o seguinte texto como o último item no segundo elemento ```<CodeGroup>``` mais externo (que deve ser ```<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">):```

{{% /alert %}}

**Exemplo**

{{< highlight csharp >}}

<CodeGroup>
...

<CodeGroup>
...

<!--Comece aqui.-->

<CodeGroup class="UnionCodeGroup" version="1" PermissionSetName="FullTrust"

Name="Aspose.Pdf_for_Reporting_Services" Description="Este grupo de código concede confiança total ao assembly AP4SSRS.">

<IMembershipCondition class="StrongNameMembershipCondition" version="1" PublicKeyBlob="00240000048000009400000006020000002400005253413100040000010001005542e99cecd28842dad186257b2c7b6ae9b5947e51e0b17b4ac6d8cecd3e01c4d20658c5e4ea1b9a6c8f854b2d796c4fde740dac65e834167758cff283eed1be5c9a812022b015a902e0b97d4e95569eb8c0971834744e633d9cb4c4a6d8eda03c12f486e13a1a0cb1aa101ad94943236384cbbf5c679944b994de9546e493bf " />

</CodeGroup>

<!--Termine aqui. -->

</CodeGroup>

</CodeGroup>

{{< /highlight >}}

{{% alert color="primary" %}}
**Passo 5.** Verifique se o Aspose.Pdf para Reporting Services foi instalado com sucesso. Abra o portal da web do Reporting Services e verifique a lista de formatos de exportação disponíveis para um relatório. Você pode iniciar o portal da web começando um navegador e digitando o URL do portal da web do Reporting Services na barra de endereços (por padrão é http://```<Reporting_Services_server_name>```/reports/). Selecione um dos relatórios disponíveis no seu portal da web e puxe a lista suspensa Exportar. Você deve ver a lista de formatos de exportação, incluindo aqueles fornecidos pela extensão Aspose.Pdf for Reporting Services. Selecione o item PDF via Aspose.PDF.

Clique no item selecionado. Ele gerará o relatório no formato selecionado, enviará para o cliente e, dependendo das configurações do seu navegador, ou mostrará o diálogo Salvar Arquivo para escolher onde salvar o relatório exportado, ou baixará automaticamente o arquivo para a sua pasta de Downloads.

Parabéns, você instalou com sucesso o Aspose.Pdf for Reporting Services e exportou um relatório como um documento PDF!{{% /alert %}}