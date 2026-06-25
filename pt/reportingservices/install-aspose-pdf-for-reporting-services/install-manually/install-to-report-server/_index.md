---
title: Instalar no Report Server
linktitle: Instalar no Report Server
type: docs
weight: 10
url: /pt/reportingservices/install-to-report-server/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Você só precisa seguir estas etapas se instalar o Aspose.PDF for Reporting Services manualmente, não usando o instalador MSI. O instalador MSI executa todas as ações necessárias de instalação e registro automaticamente.

{{% /alert %}}

Nas etapas seguintes, você precisará copiar e modificar arquivos no diretório onde o Microsoft SQL Server Reporting Services está instalado. O assembly do SSRS 2016 está localizado no diretório \Bin\SSRS2016 do pacote zip; o assembly do SSRS 2017 está localizado no diretório \Bin\SSRS2017; o assembly do SSRS 2019 está localizado no diretório \Bin\SSRS2019; o assembly do SSRS 2022 está localizado no diretório \Bin\SSRS2022; o assembly do Power BI Report Server está localizado no diretório \Bin\PowerBI. 

{{% alert color="primary" %}}

**Etapa 1.** Localize o diretório de instalação do Report Server. O diretório raiz do Microsoft SQL Server geralmente é C:\Program Files\Microsoft SQL Server. O processo posterior é um pouco diferente para Reporting Services 2016, Reporting Services 2017 e posteriores, e para o Power BI Report Server:

- O Report Server 2016, por padrão, é instalado no diretório C:\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer. Se você estiver usando instâncias com nomes personalizados em vez da padrão, o caminho padrão será C:\Program Files\Microsoft SQL Server\MSRS13.[SSRSInstanceName]\Reporting Services\ReportServer
- O Report Server 2017 e versões posteriores, por padrão, são instalados no diretório C:\Program Files\Microsoft SQL Server Reporting Services\SSRS\ReportServer.
- O Power BI Report Server, por padrão, é instalado no diretório C:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServer.

No texto a seguir, o diretório de instalação do Reporting Services (um dos caminhos mencionados) será referenciado como ```<Instance>```.
{{% /alert %}}

{{% alert color="primary" %}}
**Etapa 2.** Copie Aspose.Pdf.ReportingServices.dll para a versão correspondente do SSRS para ```<Instance>```pasta \bin.
{{% /alert %}}

{{% alert color="primary" %}}
**Etapa 3.** Registre o Aspose.Pdf for Reporting Services como uma extensão de renderização. Abra o ```<Instance>```\rsreportserver.config file e adicione as linhas a seguir no ```<Render>``` elemento:
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
**Etapa 4.** Forneça o Aspose.Pdf for Reporting Services com permissões para executar. Abra o ```<Instance>```arquivo \\rssrvpolicy.config e adicione o texto a seguir como o último item no segundo ao externo ```<CodeGroup>``` elemento (que deve ser ```<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">):```
{{% /alert %}}

**Exemplo**

{{< highlight csharp >}}

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

{{< /highlight >}}

{{% alert color="primary" %}}
**Etapa 5.** Verifique se o Aspose.Pdf for Reporting Services foi instalado com sucesso. Abra o portal web do Reporting Services e verifique a lista de formatos de exportação disponíveis para um relatório. Você pode iniciar o portal web iniciando um navegador e digitando a URL do portal web do Reporting Services na barra de endereço (por padrão, ela é http://```<Reporting_Services_server_name>```/reports/). Selecione um dos relatórios disponíveis em seu portal da Web e abra a lista suspensa Exportar. Você deve ver a lista de formatos de exportação, incluindo os fornecidos pela extensão Aspose.Pdf for Reporting Services. Selecione o item PDF via Aspose.PDF.

 
{{% /alert %}}

![todo:image_alt_text](install-to-report-server_1.png)

Clique no item selecionado. Ele gerará o relatório no formato selecionado, enviará ao cliente e, dependendo das configurações do seu navegador, exibirá a caixa de diálogo Salvar arquivo para escolher onde salvar o relatório exportado ou baixará automaticamente o arquivo para a sua pasta Downloads.

{{% alert color="primary" %}}
Parabéns, você instalou o Aspose.Pdf for Reporting Services com sucesso e exportou um relatório como documento PDF!
{{% /alert %}}




