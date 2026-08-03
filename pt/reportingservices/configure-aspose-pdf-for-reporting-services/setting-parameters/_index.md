---
title: Definir parâmetros
linktitle: Setting Parameters
type: docs
weight: 10
url: /reportingservices/setting-parameters/
description: Descubra como definir parâmetros para renderização de PDF em Aspose.PDF para Reporting Services. Obtenha controle preciso sobre a produção.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Você pode especificar determinados parâmetros de configuração que afetam como o Aspose.PDF for Reporting Services gera documentos. Esta seção descreve esse processo.

{{% /alert %}}

Para configurar Aspose.Pdf para Reporting Services, você precisa editar o arquivo `C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config`. Este é um arquivo XML e a configuração do renderizador está dentro do elemento `<Extension>` correspondente ao renderizador Aspose.PDF.

## Exemplo

```xml
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
```

{{% alert color="primary" %}}

Se desejar definir parâmetros para um arquivo de relatório específico, mas não para todos os relatórios no servidor, você poderá adicionar um parâmetro de relatório para o relatório específico no Report Builder conforme as etapas a seguir (por exemplo, adicionaremos um parâmetro 'IsLandscape' mostrado anteriormente):

1. Abra o relatório no Report Designer, clique com o botão direito na pasta 'Parâmetros' no painel 'Dados do relatório' e selecione 'Adicionar parâmetro...' (ou, alternativamente, abra a lista 'Novo' e selecione 'Parâmetro...').

![Parameters set up. Step 1](setting-parameters_1.png)

1. Na caixa de diálogo 'Propriedades do parâmetro do relatório', crie o parâmetro denominado 'IsLandscape', com o tipo de dados Booleano, e adicione o valor True na guia 'Valores padrão'.

![Parameters set up. Step 2](setting-parameters_2.png)

{{% /alert %}}
