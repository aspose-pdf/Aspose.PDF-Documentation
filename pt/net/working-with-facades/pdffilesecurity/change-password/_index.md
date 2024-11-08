---
title: Alterar Senha de Arquivo PDF
type: docs
weight: 40
url: /pt/net/change-password/
description: Este tópico explica como alterar a senha em um arquivo PDF usando a Classe PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Alterar Senha de um Arquivo PDF

Para alterar a senha de um arquivo PDF, você precisa criar um objeto [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) e então chamar o método [ChangePassword](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2). Você precisa passar a senha de proprietário existente e as novas senhas de usuário e proprietário para o método [ChangePassword](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2).

{{% alert color="primary" %}}

- A **senha do usuário**, se definida, é o que você precisa fornecer para abrir um PDF. O Acrobat/Reader solicitará que o usuário insira a senha do usuário. Se não estiver correta, o documento não abrirá.
- A **senha do proprietário**, se definida, controla permissões, como impressão, edição, extração, comentários, etc. Acrobat/Reader irá desativar essas coisas com base nas configurações de permissão. O Acrobat exigirá esta senha se você quiser definir/mudar permissões.

{{% /alert %}}

O trecho de código a seguir mostra como alterar senhas de um arquivo PDF.

```csharp
public static void ChangePassword()
        {
            PdfFileInfo pdfFileInfo = new PdfFileInfo(_dataDir + "sample_encrypted.pdf");
            // Criar objeto PdfFileSecurity
            if (pdfFileInfo.IsEncrypted)
            {
                PdfFileSecurity fileSecurity = new PdfFileSecurity();
                fileSecurity.BindPdf(_dataDir + "sample_encrypted.pdf");
                fileSecurity.ChangePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", DocumentPrivilege.Print, KeySize.x256);
                fileSecurity.Save(_dataDir + "sample_encrtypted1.pdf");
            }
        }
```