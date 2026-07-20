---
title: Salvar documento PDF programaticamente
linktitle: Salvar PDF
type: docs
weight: 30
url: /pt/go-cpp/save-pdf-document/
description: Saiba como salvar arquivo PDF com Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Salvar documento PDF com Aspose.PDF for Go via C++
Abstract: Aspose.PDF for Go via C++ oferece funcionalidade abrangente para salvar documentos PDF em vários formatos e locais com alta eficiência e flexibilidade. A biblioteca permite que os desenvolvedores salvem PDFs em sistemas de arquivos, fluxos de memória ou os exportem em formatos alternativos, como DOCX, XLSX e imagens. Ela fornece opções para personalizar os parâmetros de salvamento, otimizar o tamanho do arquivo e garantir a integridade dos dados. A documentação inclui instruções detalhadas e exemplos de código para ajudar os desenvolvedores a implementar de forma eficiente as capacidades de salvamento de PDF em suas aplicações.
SoftwareApplication: go-cpp
---

## Salvar documento PDF no sistema de arquivos

O exemplo demonstra o [New](https://reference.aspose.com/pdf/go-cpp/core/new/) método para criar um novo documento PDF, que é um recurso fundamental para gerar documentos dinamicamente, como relatórios ou faturas.

O código é simples e pode servir como modelo para recursos mais avançados, como adicionar texto, imagens ou anotações ao PDF.

Este exemplo demonstra o uso direto da biblioteca Aspose.PDF Go, mostrando seu potencial para criar, modificar e salvar documentos.

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
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_New_SaveAs.pdf")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
