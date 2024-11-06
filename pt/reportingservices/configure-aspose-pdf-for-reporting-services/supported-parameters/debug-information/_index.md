---
title: Informações de Depuração
type: docs
weight: 90
url: pt/reportingservices/debug-information/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

É inevitável que haja algo errado com a renderização ou com o resultado renderizado. Por alguns motivos, como sigilo ou privacidade, não conseguimos obter a fonte de dados usada no relatório do usuário, portanto, não conseguimos reproduzir o erro no relatório. Para facilitar e suavizar a comunicação entre clientes e desenvolvedores, adicionamos este parâmetro. Se você encontrar problemas ao renderizar seu relatório com Aspose.PDF para Reporting Services, por favor, defina este parâmetro de relatório, então você receberá o documento renderizado no formato XML. Depois disso, por favor poste o arquivo XML para nós no fórum do produto.

{{% /alert %}}

{{% alert color="primary" %}}
**Nome do Parâmetro**: SavingXmlFormat  
**Tipo de Dado**: Boolean  
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
```