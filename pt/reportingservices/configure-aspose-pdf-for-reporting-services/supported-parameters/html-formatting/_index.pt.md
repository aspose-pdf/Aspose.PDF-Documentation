---
title: HTML Formatting
type: docs
weight: 20
url: /reportingservices/html-formatting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Às vezes você pode querer exportar texto em caixas de texto com formatação. Infelizmente, o Reporting Services não suporta isso. No entanto, você ainda pode implementá-lo usando Aspose.PDF para Reporting Services. Basta habilitar um modo especial no qual todo o texto em caixas de texto é tratado como HTML e colocar as tags HTML necessárias para formatar o texto no documento de saída. Por exemplo, para ter texto normal, em negrito e em itálico na mesma caixa de texto, insira o seguinte valor na caixa de texto:

Alguns deste texto é ```<b>negrito</b>``` e outro texto é ```<i>itálico</i>```.

Quando exportado, o texto aparecerá como se parte deste texto fosse **negrito** e outra parte fosse *itálico*.

Por favor, note que esta abordagem tem algumas limitações.

{{% /alert %}}

{{% alert color="primary" %}}

- A formatação não é visível no tempo de design (no Report Builder, portal web do Reporting Services etc.). Em vez disso, você verá o texto HTML em forma de texto simples com tags.  
- A extensão de renderização Aspose.PDF para Serviços de Relatórios reconhece e formata adequadamente o código HTML em caixas de texto. O renderizador PDF padrão dos Serviços de Relatórios exportará esta marcação como texto simples.

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

Se você quiser adicionar este parâmetro no Designer de Relatórios, use o tipo de dado 'Boolean'.

Atualmente, o Aspose.Pdf para Serviços de Relatórios suporta um subconjunto de todas as tags HTML. Você pode encontrar mais informações na [Documentação](https://docs.aspose.com/pdf/net/add-text-to-pdf-file/#add-html-string-using-dom) Aspose.PDF.

{{% /alert %}}