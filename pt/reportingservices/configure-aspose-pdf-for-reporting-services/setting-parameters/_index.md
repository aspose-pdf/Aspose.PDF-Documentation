---
title: Configuração de Parâmetros
linktitle: Configuração de Parâmetros
type: docs
weight: 10
url: /pt/reportingservices/setting-parameters/
description: Descubra como definir parâmetros para a renderização de PDF no Aspose.PDF for Reporting Services. Alcance controle preciso sobre a saída.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Você pode especificar certos parâmetros de configuração que afetam como o Aspose.Pdf for Reporting Services gera documentos. Esta seção descreve esse processo.

{{% /alert %}}

Para configurar o Aspose.Pdf para Reporting Services, você precisa editar o arquivo C:\\Program Files\\Microsoft SQL Server\\<Instance>\\Reporting Services\\ReportServer\\rsreportserver.config. Este é um arquivo XML e a configuração do renderizador está dentro do ```<Extension>``` elemento correspondente ao renderizador Aspose.PDF.

**Exemplo**

{{< highlight csharp >}}

<Render>
…
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
<!--Insert configuration elements for exporting to PDF here. The following is an example
For PageOrientation -->
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% alert color="primary" %}}

Se você quiser definir parâmetros para um arquivo de relatório específico, mas não para todos os relatórios no servidor, pode adicionar um parâmetro de relatório para o relatório específico no Report Builder conforme as etapas a seguir (por exemplo, iremos adicionar um parâmetro ‘IsLandscape’ mostrado anteriormente):

1. Abra o relatório no Report Designer, clique com o botão direito na pasta ‘Parameters’ no painel ‘Report Data’ e selecione ‘Add Parameter…’ (ou, alternativamente, abra a lista ‘New’ e selecione ‘Parameter…’).
 
![todo:image_alt_text](setting-parameters_1.png)

1. Na caixa de diálogo ‘Report Parameter Properties’, crie o parâmetro chamado ‘IsLandscape’, com o tipo de dado Boolean, e adicione o valor True na guia ‘Default Values’.

![todo:image_alt_text](setting-parameters_2.png)

{{% /alert %}}

