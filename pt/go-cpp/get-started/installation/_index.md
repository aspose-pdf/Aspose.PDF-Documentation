---
title: Como Instalar Aspose.PDF para Go via C++
linktitle: Instalação
type: docs
weight: 20
url: /pt/go-cpp/installation/
description: Esta seção apresenta uma descrição do produto e instruções para instalar o Aspose.PDF for Go por conta própria.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guia de instalação do Aspose.PDF for Go
Abstract: O guia de Instalação do Aspose.PDF for Go via C++ fornece instruções passo a passo para instalar e configurar a biblioteca para uso em projetos Go com integração C++. Ele cobre vários métodos de instalação, incluindo configuração manual e o uso de gerenciadores de pacotes como NuGet. O guia também descreve os requisitos do sistema, dependências e as etapas de configuração necessárias para garantir uma integração perfeita nos ambientes de desenvolvimento. Esta documentação ajuda os desenvolvedores a iniciar a criação, leitura e manipulação de documentos PDF em Go via C++ de forma eficaz.
SoftwareApplication: go-cpp
---

## Instalação

Este pacote inclui um arquivo grande que está armazenado como um arquivo bzip2.

1. Adicione o pacote asposepdf ao seu projeto:

```sh
go get github.com/aspose-pdf/aspose-pdf-go-cpp@latest
```

2. Gere o arquivo grande:

- **macOS e Linux**

1. Abrir Terminal

2. Liste as pastas do github.com/aspose-pdf no cache do módulo Go:

```sh
ls $(go env GOMODCACHE)/github.com/aspose-pdf/
```

3. Altere a pasta atual para a pasta da versão específica do pacote obtido na etapa anterior:

```sh
cd $(go env GOMODCACHE)/github.com/aspose-pdf/aspose-pdf-go-cpp@vx.x.x
```

Substitua `@vx.x.x` pela versão real do pacote.

4. Execute go generate com privilégios de superusuário:

```sh
sudo go generate
```

- **Windows**

1. Abrir Prompt de Comando

2. Liste as pastas do github.com/aspose-pdf no cache do módulo Go:

```cmd
for /f "delims=" %G in ('go env GOMODCACHE') do for /d %a in ("%G\github.com\aspose-pdf\*") do echo %~fa
```

3. Altere a pasta atual para a pasta da versão específica do pacote obtido na etapa anterior:

```cmd
cd <specific version folder of the package>
```

4. Execute go generate:

```cmd
go generate
```

5. Adicione a pasta da versão específica do pacote à variável de ambiente %PATH%:

```cmd
setx PATH "%PATH%;<specific version folder of the package>\lib\"
```

Substituir `<specific version folder of the package>` com o caminho real obtido na etapa 2.

## Teste

A execução do teste a partir da pasta raiz do pacote:

```sh
go test -v
```

## Início Rápido

Todos os trechos de código estão contidos no [trecho](https://github.com/aspose-pdf/aspose-pdf-go-cpp).