---
title: Informação de Depuração
linktitle: Informação de Depuração
type: docs
weight: 90
url: /pt/reportingservices/debug-information/
description: Acesse e analise informações de depuração da renderização de PDF no Aspose.PDF for Reporting Services para solucionar problemas de maneira eficaz.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

É inevitável que haja algo errado na renderização ou no resultado renderizado. Por algumas razões, como sigilo ou privacidade, não conseguimos obter a fonte de dados usada no relatório do usuário, portanto não pudemos reproduzir o erro no relatório. Para tornar a comunicação entre clientes e desenvolvedores mais fácil e fluida, adicionamos este parâmetro. Se você encontrar problemas ao renderizar seu relatório com Aspose.PDF for Reporting Services, por favor defina este parâmetro no relatório; então você receberá o documento renderizado no formato XML. Em seguida, por favor publique o arquivo XML para nós no fórum do produto.

{{% /alert %}}

{{% alert color="primary" %}}
**Nome do Parâmetro**: SavingXmlFormat  
**Tipo de Dados**: Boolean  
**Valores suportados**: True, False (padrão)  

**Exemplo**
{{< highlight csharp >}}

<Render>
...
<Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">
<Configuration>
<SavingXmlFormat > Verdadeiro </SavingXmlFormat>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
