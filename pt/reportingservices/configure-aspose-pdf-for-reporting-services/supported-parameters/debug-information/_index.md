---
title: Informações de depuração
linktitle: Informações de depuração
type: docs
weight: 90
url: /pt/reportingservices/debug-information/
description: Acesse e analise informações de depuração da renderização de PDF no Aspose.PDF for Reporting Services para solucionar problemas de forma eficaz.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

É inevitável que algo esteja errado com a renderização ou com o resultado renderizado. Por razões como sigilo ou privacidade, não podemos obter a fonte de dados usada no relatório do usuário, portanto não conseguimos reproduzir o erro no relatório. Para tornar a comunicação entre clientes e desenvolvedores mais fácil e fluida, adicionamos este parâmetro. Se você encontrar problemas ao renderizar seu relatório com Aspose.PDF for Reporting Services, defina este parâmetro de relatório; assim você receberá o documento renderizado no formato XML. Em seguida, publique o arquivo XML para nós no fórum do produto.

{{% /alert %}}

{{% alert color="primary" %}}
**Nome do Parâmetro**: SavingXmlFormat  
**Tipo de Data**: Boolean  
**Valores suportados**: True, False (padrão)  

**Exemplo**
{{< highlight csharp >}}

<Render>
...
<Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">
<Configuration>
<SavingXmlFormat > True </SavingXmlFormat>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}

