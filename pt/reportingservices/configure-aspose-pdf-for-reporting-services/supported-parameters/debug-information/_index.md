---
title: Informações de depuração
linktitle: Debug Information
type: docs
weight: 90
url: /reportingservices/debug-information/
description: Acesse e analise informações de depuração para renderização de PDF no Aspose.PDF for Reporting Services para solucionar problemas de maneira eficaz.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

É inevitável que haja algo errado com a renderização ou com o resultado renderizado. Por alguns motivos, como sigilo ou privacidade, não conseguimos obter a fonte de dados utilizada no relatório do usuário e, portanto, não conseguimos reproduzir o erro no relatório. Para tornar a comunicação entre clientes e desenvolvedores mais fácil e tranquila, adicionamos este parâmetro. Se você encontrar problemas ao renderizar seu relatório com Aspose.PDF para Reporting Services, defina este parâmetro de relatório, então você obterá o documento renderizado com o formato XML. Depois disso, poste o arquivo XML para nós no fórum do produto.

{{% /alert %}}

{{% alert color="primary" %}}

```txt
Parameter Name: SavingXmlFormat
Date Type: Boolean  
Values supported**: True, False (default)
```

## Exemplo

```xml
<Render>
...
<Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">
<Configuration>
<SavingXmlFormat > True </SavingXmlFormat>
</Configuration>
</Extension>
</Render>
```

{{% /alert %}}
