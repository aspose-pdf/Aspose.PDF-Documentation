---
title: Definir Parâmetros
linktitle: Definir Parâmetros
type: docs
weight: 10
url: /pt/reportingservices/setting-parameters/
description: Descubra como definir parâmetros para a renderização de PDF no Aspose.PDF for Reporting Services e obter controle preciso sobre a saída.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

Você pode especificar determinados parâmetros de configuração que afetam a forma como o Aspose.PDF for Reporting Services gera documentos. Esta seção descreve esse processo.

{{% /alert %}}

Para configurar o Aspose.PDF for Reporting Services, você precisa editar o arquivo `C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config`. Esse é um arquivo XML, e a configuração do renderizador fica dentro do elemento ```<Extension>``` correspondente ao renderizador Aspose.PDF.

**Exemplo**

{{< highlight csharp >}}

<Render>
...
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

Se você quiser definir parâmetros para um arquivo de relatório específico, mas não para todos os relatórios no servidor, poderá adicionar um parâmetro de relatório para esse relatório no Report Builder seguindo as etapas abaixo. Neste exemplo, adicionaremos o parâmetro `IsLandscape` mostrado anteriormente.

1. Abra o relatório no Report Designer, clique com o botão direito na pasta `Parameters` no painel `Report Data` e selecione `Add Parameter...` (ou, alternativamente, abra a lista `New` e selecione `Parameter...`).
 
![todo:image_alt_text](setting-parameters_1.png)

1. Na caixa de diálogo `Report Parameter Properties`, crie o parâmetro chamado `IsLandscape`, defina o tipo de dado como Boolean e adicione o valor True na guia `Default Values`.

![todo:image_alt_text](setting-parameters_2.png)

{{% /alert %}}

