---
title: Formatação HTML
linktitle: Formatação HTML
type: docs
weight: 20
url: /pt/reportingservices/html-formatting/
description: Habilite a formatação HTML em relatórios PDF usando Aspose.PDF for Reporting Services. Adicione estilos e estrutura com facilidade.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Às vezes, você pode desejar exportar texto em caixas de texto com formatação. Infelizmente, o Reporting Services não oferece suporte a isso. No entanto, ainda é possível implementá‑lo usando Aspose.PDF for Reporting Services. Basta habilitar um modo especial no qual todo o texto nas caixas de texto é tratado como HTML e inserir as tags HTML necessárias para formatar o texto no documento de saída. Por exemplo, para ter texto normal, em negrito e itálico na mesma caixa de texto, insira o seguinte valor na caixa de texto:

Alguma parte deste texto é ```<b>bold</b>``` e outro texto é ```<i>italic</i>```.

Ao exportar, o texto ficará assim: parte deste texto está **bold** e outro texto está *italic*.

Observe que esta abordagem tem algumas limitações

{{% /alert %}}

{{% alert color="primary" %}}

- A formatação não é visível no tempo de design (no Report Builder, no portal web do Reporting Services etc.). Em vez disso, você verá o texto HTML na forma de texto simples com tags.
- A extensão de renderização Aspose.PDF for Reporting Services reconhece e formata corretamente o código HTML em caixas de texto. O renderizador PDF padrão do Reporting Services exportará essa marcação como texto simples.

**Nome do Parâmetro**: IsHtmlTagSupported  
**Tipo de Dados**: Boolean  
**Valores suportados**: True, False (padrão)   

**Exemplo**

{{< highlight csharp >}}

 <Render>
...
    <Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices ">
    <Configuration>
    <IsHtmlTagSupported >True</IsHtmlTagSupported>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

Se você quiser adicionar este parâmetro no Report Designer, use o tipo de dados 'Boolean'.

 
Atualmente Aspose.Pdf for Reporting Services suporta um subconjunto de todas as tags HTML. Você pode encontrar mais informações na documentação do Aspose.PDF [Documentação](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom).

{{% /alert %}}

