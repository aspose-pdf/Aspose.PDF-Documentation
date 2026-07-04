---
title: Descriptografar PDF usando Go
linktitle: Descriptografar Arquivo PDF
type: docs
weight: 40
url: /pt/go-cpp/decrypt-pdf/
description: Descriptografar Arquivo PDF com Aspose.PDF para Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Descriptografar Arquivo PDF usando Senha do Proprietário

Você pode abrir, descriptografar e salvar um documento PDF protegido por senha usando o Aspose.PDF para Go via C++. O arquivo PDF é aberto com a senha do proprietário, descriptografado para remover todas as restrições de segurança e, então, salvo como um novo documento não protegido.

1. Chamar [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) e forneça o nome do arquivo juntamente com a senha do proprietário para acessar o PDF criptografado.
1. Chame o [Decrypt](https://reference.aspose.com/pdf/go-cpp/security/decrypt/) método para remover a proteção por senha e todas as restrições de segurança associadas do documento.
1. Salve o PDF descriptografado usando [SalvarComo](https://reference.aspose.com/pdf/go-cpp/core/saveas/).

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // OpenWithPassword(filename string, password string) opens a password-protected PDF-document
        pdf, err := asposepdf.OpenWithPassword("sample_with_password.pdf", "ownerpass")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
        // Decrypt() decrypts PDF-document
        err = pdf.Decrypt()
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_without_password.pdf")
        if err != nil {
            log.Fatal(err)
        }
    }
```