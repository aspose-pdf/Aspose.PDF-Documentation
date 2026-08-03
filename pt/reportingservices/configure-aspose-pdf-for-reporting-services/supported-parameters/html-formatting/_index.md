---
title: Formatação HTML
linktitle: HTML Formatting
type: docs
weight: 20
url: /reportingservices/html-formatting/
description: Habilite a formatação HTML em relatórios PDF usando Aspose.PDF para Reporting Services. Adicione estilos e estrutura com facilidade.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Às vezes você pode querer exportar texto em caixas de texto com formatação. Infelizmente, o Reporting Services não oferece suporte para isso. No entanto, você ainda pode implementá-lo usando Aspose.PDF para Reporting Services. Basta ativar um modo especial no qual todo o texto nas caixas de texto é tratado como HTML e colocar as tags HTML necessárias para formatar o texto no documento de saída. Por exemplo, para ter texto normal, em negrito e itálico na mesma caixa de texto, insira o seguinte valor de caixa de texto:

Parte deste texto é `<b>bold</b>` e outro texto é `<i>italic</i>`.

Quando exportado, o texto terá a aparência de parte deste texto em **negrito** e outro texto em *itálico*.

Observe que esta abordagem tem algumas limitações

{{% /alert %}}

{{% alert color="primary" %}}

- A formatação não é visível em tempo de design (no Report Builder, no portal da Web Reporting Services etc.). Em vez disso, você verá o texto HTML na forma de texto simples com tags.
- A extensão de renderização Aspose.PDF para Reporting Services reconhece e formata corretamente o código HTML em caixas de texto. O renderizador de PDF padrão do Reporting Services exportará essa marcação como texto simples.

```text
Parameter Name: IsHtmlTagSupported  
Date Type: Boolean  
Values supported: True, False (default)   
```

## Exemplo

```xml
<Render>
...
    <Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices ">
    <Configuration>
    <IsHtmlTagSupported >True</IsHtmlTagSupported>
    </Configuration>
    </Extension>
</Render>
```

Se desejar adicionar esse parâmetro no Report Designer, use o tipo de dados `Boolean`.

Atualmente Aspose.Pdf para Reporting Services oferece suporte a um subconjunto de todas as tags HTML. Você pode encontrar mais informações em Aspose.PDF [Documentação](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom).

{{% /alert %}}
