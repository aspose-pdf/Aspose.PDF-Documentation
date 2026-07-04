---
title: Definir permissões para um documento PDF usando Go
linktitle: Definir permissões
type: docs
weight: 80
url: /pt/go-cpp/set_permissions/
description: Definir permissões para um documento PDF com Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Definir permissões de acesso para um documento PDF

Um novo documento PDF é criado e protegido com senhas de usuário e de proprietário, enquanto permissões específicas—como imprimir, modificar o conteúdo e preencher formulários—são explicitamente permitidas. O documento é então salvo com essas restrições de permissão aplicadas.

1. Criar um novo documento PDF.
1. Chamar [SetPermissions](https://reference.aspose.com/pdf/go-cpp/security/setpermissions/) para proteger o documento.
1. Especifique uma senha de usuário para restringir o acesso.
1. Especifique uma senha de proprietário para controlar as configurações de segurança.
1. Defina as operações permitidas usando um bitflag de permissões.
1. Salvar o PDF com permissões aplicadas usando [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/).

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

        // SetPermissions(userPassword, ownerPassword, permissions) sets permissions for PDF-document
        err = pdf.SetPermissions(
            "userpass",
            "ownerpass",
            asposepdf.PrintDocument|
                asposepdf.ModifyContent|
                asposepdf.FillForm,
        )
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_with_permissions.pdf")
        if err != nil {
            log.Fatal(err)
        }
    }
```