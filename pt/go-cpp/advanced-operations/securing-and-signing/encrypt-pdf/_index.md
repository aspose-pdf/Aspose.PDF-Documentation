---
title:  Criptografar PDF usando Go
linktitle: Criptografar arquivo PDF
type: docs
weight: 10
url: /pt/go-cpp/encrypt-pdf/
description: Criptografar arquivo PDF com Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Criptografar arquivo PDF usando usando senha de usuário ou de proprietário

Para criptografar documentos de forma fácil e segura, você pode usar Aspose.PDF for Go via C++.

- O **userPassword**, se definido, é o que você precisa fornecer para abrir um PDF. Acrobat/Reader solicitará que o usuário insira a senha de usuário. Se não estiver correta, o documento não será aberto.
- A **ownerPassword**, se definida, controla permissões, como impressão, edição, extração, comentários, etc. O Acrobat/Reader impedirá essas ações com base nas configurações de permissão. O Acrobat exigirá essa senha se você quiser definir/alterar permissões.

O PDF está protegido com senhas de usuário e proprietário, configurado com permissões de acesso específicas, e criptografado usando o algoritmo AES-128 com segurança compatível com PDF 2.0. O documento criptografado é então salvo no disco.

1. Crie um novo documento PDF.
1. Criptografe o documento PDF com [encrypt](https://reference.aspose.com/pdf/go-cpp/security/encrypt/) método.
1. Especifique uma senha de usuário para restringir a abertura do documento.
1. Especifique uma senha de proprietário para controlar as permissões.
1. Defina ações permitidas usando uma bandeira de bits de permissões.
1. Escolha AES-128 como o algoritmo de criptografia.
1. Ative a criptografia PDF 2.0 para conformidade de segurança moderna.
1. Salve o documento protegido usando [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/), gravando-o em um novo arquivo.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // New creates a new PDF-document
        pdf, err := asposepdf.New()
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
        // Encrypt(userPassword, ownerPassword, permissions, cryptoAlgorithm, usePdf20) encrypts PDF-document
        err = pdf.Encrypt(
            "userpass",
            "ownerpass",
            asposepdf.PrintDocument|asposepdf.ModifyContent|asposepdf.FillForm,
            asposepdf.AESx128,
            true,
        )
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_with_password.pdf")
        if err != nil {
            log.Fatal(err)
        }
    }
```