---
title: Configuração de segurança
linktitle: Security Setting
type: docs
weight: 30
url: /reportingservices/security-setting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

A segurança sempre foi a questão mais importante em todos os campos, seja na proteção de uma rede ou de um documento PDF. Os documentos são protegidos por vários motivos possíveis: o autor do documento pode querer manter o conteúdo do documento seguro e não querer permitir que outros o alterem, etc.

Aspose.PDF for Reporting Services cuidou muito desses aspectos de segurança, fornecendo esses recursos aos desenvolvedores que podem ser úteis para proteger seus documentos PDF. Portanto, contém uma série de parâmetros que permitem aos desenvolvedores aplicar diferentes medidas de segurança aos documentos PDF.

Uma dessas medidas é proteger o documento PDF com senha durante a criptografia. Você também pode restringir ou permitir modificação de conteúdo, cópia de conteúdo, impressão de documentos ou permitir/desabilitar preenchimento de formulários. No momento, esses recursos não são suportados pelo SQL Reporting Services PDF Exporter padrão, mas você pode implementar esses recursos usando Aspose.PDF para Reporting Services. Basta adicionar parâmetros de segurança correspondentes a um relatório ou arquivo de configuração do servidor de relatório e você poderá criar documentos PDF seguros com privilégios limitados.

Atualmente, o renderizador Aspose.PDF para Reporting Services oferece suporte aos seguintes atributos de segurança:

{{% /alert %}}

```text
Parameter Name: User Password  
Date Type: String  
Values supported: Any plain text
```

```text
Parameter Name: Master Password  
Date Type: String  
Values supported: Any plain text 
```

```text
Parameter Name: IsCopyingAllowed  
Date Type: Boolean  
Values supported: True, False (default) 
```

```text
Parameter Name: IsPrintingAllowed  
Date Type: Boolean  
Values supported: True, False (default)  
```

```text
Parameter Name: IsContentsModifyingAllowed  
Date Type: Boolean  
Values supported: True, False (default) 
```

```text
Parameter Name: IsFormFillingAllowed  
Date Type: Boolean  
Values supported: True, False (default)  
```

## Exemplo

```xml
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
```

