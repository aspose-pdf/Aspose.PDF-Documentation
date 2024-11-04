---
title: Definir Privilégios em PDF
type: docs
weight: 50
url: /net/set-privileges/
description: Este tópico explica como definir privilégios em um arquivo PDF existente usando a Classe PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Definir Privilégios em um Arquivo PDF Existente

Para definir os privilégios de um arquivo PDF, crie um objeto [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) e chame o método SetPrivilege. Você pode especificar os privilégios usando o objeto DocumentPrivilege e então passar este objeto para o método SetPrivilege. O trecho de código a seguir mostra como definir os privilégios de um arquivo PDF.

```csharp
public static void SetPrivilege1()
 {
    // Criar objeto DocumentPrivileges
    DocumentPrivilege privilege = DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    // Criar objeto PdfFileSecurity
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample.pdf");
    fileSecurity.SetPrivilege(privilege);
    fileSecurity.Save(_dataDir + "sample_privileges.pdf");
}
```

Veja o seguinte método especificando uma senha:

```csharp
 public static void SetPrivilege2()
 {
    // Criar objeto DocumentPrivileges
    DocumentPrivilege privilege = DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    // Criar objeto PdfFileSecurity
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample.pdf");
    fileSecurity.SetPrivilege(string.Empty, "P@ssw0rd", privilege);
    fileSecurity.Save(_dataDir + "sample_privileges.pdf");
}
```

## Remover Funcionalidade de Direitos Estendidos do PDF

Documentos PDF suportam a funcionalidade de direitos estendidos para permitir que o usuário final preencha dados em campos de formulário usando o Adobe Acrobat Reader e, em seguida, salve uma cópia do formulário preenchido. No entanto, isso garante que o arquivo PDF não seja modificado e, se qualquer modificação na estrutura do PDF for feita, o recurso de direitos estendidos é perdido. Ao visualizar tal documento, uma mensagem de erro é exibida, informando que os direitos estendidos foram removidos porque o documento foi modificado. Recentemente, recebemos uma exigência para remover os direitos estendidos de um documento PDF.

Para remover os direitos estendidos de um arquivo PDF, um novo método chamado RemoveUsageRights() foi adicionado à classe PdfFileSignature. Outro método chamado ContainsUsageRights() foi adicionado para determinar se o PDF de origem contém direitos estendidos.

{{% alert color="primary" %}}
A partir do Aspose.PDF para .NET 9.5.0, os nomes dos seguintes métodos foram atualizados. Por favor, note que os métodos anteriores ainda estão na API, mas foram marcados como obsoletos e serão removidos. Portanto, é recomendável tentar usar os métodos atualizados.

- O método IsContainSignature(.) foi renomeado para ContainsSignature(..).

- O método IsCoversWholeDocument(..) foi renomeado para CoversWholeDocument(..).{{% /alert %}}

O código a seguir mostra como remover os direitos de uso do documento:

```csharp
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_SecuritySignatures();
string input = dataDir + "DigitallySign.pdf";
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(input);
    if (pdfSign.ContainsUsageRights())
    {
        pdfSign.RemoveUsageRights();
    }

    pdfSign.Document.Save(dataDir + "RemoveRights_out.pdf");
}
```