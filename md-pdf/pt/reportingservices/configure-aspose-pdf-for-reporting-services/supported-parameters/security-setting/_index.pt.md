---
title: Security Setting
type: docs
weight: 30
url: /reportingservices/security-setting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

A segurança sempre foi a questão mais importante em todos os campos, seja a proteção de uma rede ou de um documento PDF. Documentos são protegidos por várias razões possíveis: o autor do documento pode querer manter o conteúdo do documento seguro e não permitir que outros o alterem, etc.

O Aspose.Pdf para Reporting Services tem cuidado com esses aspectos de segurança, fornecendo esses recursos para desenvolvedores que podem ser úteis para proteger seus documentos PDF. Portanto, ele contém vários parâmetros que permitem aos desenvolvedores aplicar diferentes medidas de segurança aos documentos PDF.

Uma dessas medidas é proteger o documento PDF com senha durante a criptografia. Você também pode restringir ou permitir a modificação de conteúdos, copiar o conteúdo, impressão do documento ou permitir/desabilitar o preenchimento de formulários. Essas funcionalidades atualmente não são suportadas pelo Exportador PDF padrão do SQL Reporting Services, mas você pode implementar essas funcionalidades usando o Aspose.Pdf para Reporting Services. Basta adicionar os parâmetros de segurança correspondentes a um relatório ou a um arquivo de configuração do servidor de relatórios, e você poderá criar documentos PDF seguros com privilégios limitados.

Atualmente, o renderizador Aspose.Pdf para Reporting Services suporta os seguintes atributos de segurança:

{{% /alert %}}

{{% alert color="primary" %}}

**Nome do Parâmetro**: User Password  
**Tipo de Dado**: String  
**Valores suportados**: Qualquer texto simples

**Nome do Parâmetro**: Master Password  
**Tipo de Dado**: String  
**Valores suportados**: Qualquer texto simples 

**Nome do Parâmetro**: IsCopyingAllowed  
**Tipo de Dado**: Boolean  
**Valores suportados**: True, False (padrão)  

**Nome do Parâmetro**: IsPrintingAllowed  
**Tipo de Dado**: Boolean  

**Valores suportados**: True, False (padrão)  
**Nome do Parâmetro**: IsContentsModifyingAllowed  
**Tipo de Dado**: Booleano  
**Valores suportados**: True, False (padrão)  

**Nome do Parâmetro**: IsFormFillingAllowed  
**Tipo de Dado**: Booleano  
**Valores suportados**: True, False (padrão)  

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