---
title: Configuração de Segurança
linktitle: Configuração de Segurança
type: docs
weight: 30
url: /pt/reportingservices/security-setting/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

A segurança sempre foi a questão mais importante em todos os campos, seja na proteção de uma rede ou de um documento PDF. Os documentos são protegidos por muitos motivos possíveis: o autor do documento pode querer manter o conteúdo do documento seguro e não querer permitir que outros o alterem, etc.

Aspose.Pdf for Reporting Services tem se preocupado muito com esses aspectos de segurança, oferecendo esses recursos aos desenvolvedores que podem ser úteis para proteger seus documentos PDF. Portanto, ele contém diversos parâmetros que permitem aos desenvolvedores aplicar diferentes medidas de segurança aos documentos PDF.

Uma dessas medidas é proteger o documento PDF com senha durante a criptografia. Você também pode restringir ou permitir a modificação do conteúdo, a cópia do conteúdo, a impressão do documento ou habilitar/desabilitar o preenchimento de formulários. Esses recursos no momento não são suportados pelo Exportador PDF padrão do SQL Reporting Services, mas você pode implementá-los usando o Aspose.Pdf for Reporting Services. Basta adicionar os parâmetros de segurança correspondentes a um relatório ou ao arquivo de configuração do servidor de relatórios, e você poderá criar documentos PDF seguros com privilégios limitados.

Atualmente, o renderizador Aspose.Pdf for Reporting Services suporta os seguintes atributos de segurança:

{{% /alert %}}

{{% alert color="primary" %}}

**Nome do parâmetro**: Senha do Usuário  
**Tipo de data**: String  
**Valores suportados**: Qualquer texto simples

**Nome do parâmetro**: Senha mestre  
**Tipo de data**: String  
**Valores suportados**: Qualquer texto simples 

**Nome do Parâmetro**: IsCopyingAllowed  
**Tipo de Dados**: Boolean  
**Valores suportados**: True, False (default)  

**Nome do Parâmetro**: IsPrintingAllowed  
**Tipo de Dados**: Boolean  
**Valores suportados**: True, False (default)  

**Nome do Parâmetro**: IsContentsModifyingAllowed  
**Tipo de Dados**: Boolean  
**Valores suportados**: True, False (default)  

**Nome do Parâmetro**: IsFormFillingAllowed  
**Tipo de Dados**: Boolean  
**Valores suportados**: True, False (default)  

**Exemplo**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <UserPassword>aspose</UserPassword>
    <IsCopyingAllowed>False</IsCopyingAllowed>
    <IsPrintingAllowed>False</IsPrintingAllowed>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}

