---
title: Abrir um PDF protegido por senha usando Go
linktitle: Abrir um PDF protegido por senha
type: docs
weight: 70
url: /pt/go-cpp/open-password-protected-pdf/
description: Abrir um arquivo PDF protegido por senha com Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Abrir um documento PDF protegido por senha

Este trecho de código explica como abrir um documento PDF protegido por senha usando Aspose.PDF for Go via C++. O documento é aberto com a senha de proprietário, que fornece acesso total e permite operações adicionais, como ler metadados, inspecionar permissões, descriptografar o arquivo ou modificar o conteúdo.

1. Abrir o documento PDF protegido.
1. Chamar [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) e forneça o nome do arquivo juntamente com a senha do proprietário para desbloquear o documento.
1. Use 'defer pdf.Close()' para liberar todos os recursos alocados assim que o processamento for concluído.
1. Depois de abrir o documento, você pode prosseguir com tarefas adicionais, como descriptografar o PDF, mudar permissões ou extrair informações.

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
        // working...
    }
```