---
title: Definindo Parâmetros
type: docs
weight: 10
url: /reportingservices/setting-parameters/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Você pode especificar certos parâmetros de configuração que afetam como o Aspose.Pdf for Reporting Services gera documentos. Esta seção descreve esse processo.

{{% /alert %}}

Para configurar o Aspose.Pdf for Reporting Services, você precisa editar o arquivo C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config. Este é um arquivo XML e a configuração do renderizador está dentro do elemento ```<Extension>``` correspondente ao renderizador Aspose.PDF.

**Exemplo**

{{< highlight csharp >}}

<Render>
…
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
<!--Insira elementos de configuração para exportar para PDF aqui. O seguinte é um exemplo
Para PageOrientation -->
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
</Extension>
</Render>

{{< /highlight >}}


{{% alert color="primary" %}}

Se você deseja definir parâmetros para um arquivo de relatório específico, mas não para todos os relatórios no servidor, você pode adicionar um parâmetro de relatório para o relatório específico no Report Builder seguindo os passos abaixo (por exemplo, vamos adicionar um parâmetro 'IsLandscape' mostrado anteriormente):

1. Abra o relatório no Report Designer, clique com o botão direito do mouse na pasta 'Parameters' no painel 'Report Data', e selecione 'Add Parameter…' (ou, alternativamente, expanda a lista 'New' e selecione 'Parameter…').
 
![todo:image_alt_text](setting-parameters_1.png)

1. No diálogo 'Report Parameter Properties', crie o parâmetro chamado 'IsLandscape', com o tipo de dado Boolean, e adicione o valor True na aba 'Default Values'.

![todo:image_alt_text](setting-parameters_2.png)

{{% /alert %}}