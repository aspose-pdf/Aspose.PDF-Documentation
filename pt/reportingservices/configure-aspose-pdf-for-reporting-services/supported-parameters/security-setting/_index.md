---
title: Configuração de Segurança
linktitle: Configuração de Segurança
type: docs
weight: 30
url: /pt/reportingservices/security-setting/
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

A segurança sempre foi a questão mais importante em todas as áreas, seja a proteção de uma rede ou de um documento PDF. Os documentos são tornados seguros por diversos motivos possíveis: o autor do documento pode querer manter o conteúdo do documento seguro e não deseja permitir que outros o alterem, etc.

Aspose.PDF for Reporting Services tem cuidado muito bem desses aspectos de segurança ao fornecer esses recursos aos desenvolvedores que podem ser úteis para proteger seus documentos PDF. Portanto, ele contém vários parâmetros que permitem aos desenvolvedores aplicar diferentes medidas de segurança aos documentos PDF.

Uma dessas medidas é proteger o documento PDF com senha durante a criptografia. Você também pode restringir ou permitir a modificação de conteúdo, a cópia do conteúdo, a impressão do documento ou permitir/desativar o preenchimento de formulários. Esses recursos atualmente não são suportados pelo Exportador PDF padrão do SQL Reporting Services, mas você pode implementá‑los usando Aspose.PDF for Reporting Services. Basta adicionar os parâmetros de segurança correspondentes a um relatório ou ao arquivo de configuração do servidor de relatórios, e você poderá criar documentos PDF seguros com privilégios limitados.

Atualmente, o renderizador Aspose.PDF for Reporting Services suporta os seguintes atributos de segurança:

{{% /alert %}}

{{% alert color="primary" %}}

**Nome do Parâmetro**: Senha do Usuário  
**Tipo de Dados**: String  
**Valores suportados**: Qualquer texto simples

**Nome do Parâmetro**: Senha Mestra  
**Tipo de Dados**: String  
**Valores suportados**: Qualquer texto simples 

**Nome do parâmetro**: IsCopyingAllowed  
**Tipo de dado**: Boolean  
**Valores suportados**: True, False (default)  

**Nome do parâmetro**: IsPrintingAllowed  
**Tipo de dado**: Boolean  
**Valores suportados**: True, False (default)  

**Nome do parâmetro**: IsContentsModifyingAllowed  
**Tipo de dado**: Boolean  
**Valores suportados**: True, False (default)  

**Nome do parâmetro**: IsFormFillingAllowed  
**Tipo de dado**: Boolean  
**Valores suportados**: True, False (default)  

**Exemplo**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <UserPassword>aspose</UserPassword>
    <IsCopyingAllowed>Falso</IsCopyingAllowed>
    <IsPrintingAllowed>Falso</IsPrintingAllowed>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
