---
title: Como Instalar Aspose.PDF para Rust via C++
linktitle: Instalação
type: docs
weight: 20
url: /pt/rust-cpp/installation/
description: Esta seção mostra uma descrição do produto e instruções para instalar o Aspose.PDF for Rust por conta própria.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guia de instalação do Aspose.PDF for Rust
Abstract: O guia de Instalação do Aspose.PDF for Rust via C++ fornece instruções passo a passo para instalar e configurar a biblioteca para uso em projetos Rust com integração C++. Ele cobre vários métodos de instalação, incluindo configuração manual e o uso de gerenciadores de pacotes como NuGet. O guia também descreve os requisitos do sistema, dependências e as etapas de configuração necessárias para garantir uma integração perfeita nos ambientes de desenvolvimento. Esta documentação ajuda os desenvolvedores a começar a criar, ler e manipular documentos PDF em Rust via C++ de forma eficaz.
SoftwareApplication: rust-cpp
---

## Instalação

### Instalação a partir do site da Aspose

Este pacote inclui um arquivo grande que está armazenado como um arquivo bzip2.

1. **Baixe** o arquivo **Aspose.PDF for Rust via C++** do site oficial da Aspose.
   A versão mais recente (mais atual) está listada no topo e é baixada por padrão ao clicar no botão **Download**.
   Recomenda-se usar esta versão mais recente. Baixe uma versão anterior somente se necessário.
   Exemplo: `Aspose.PDF-for-Rust-via-CPP-25.6.zip`

   O formato do nome de arquivo do arquivo é: `Aspose.PDF-for-Rust-via-CPP-YY.M.zip`, onde:
   - `YY` = últimos dois dígitos do ano (por exemplo, `25` para 2025)
   - `M` = número do mês a partir de `1` para `12`

2. **Extrair** o arquivo para o diretório escolhido `{path}` usando uma ferramenta adequada:

   - Em Linux/macOS:

     ```bash
     unzip Aspose.PDF-for-Rust-via-CPP-YY.M.zip -d {path}
     ```

   - No Windows, use a extração incorporada do Explorer ou qualquer ferramenta de descompactação (7-Zip, WinRAR).

3. **Adicionar** a biblioteca como dependência no seu projeto Rust. Você pode fazer isso de duas maneiras:

   - **Usando a linha de comando:**

     ```bash
     cargo add asposepdf --path {path}/asposepdf
     ```

   - **Edição manual `Cargo.toml`:**
     Abra o projeto `Cargo.toml` e adicione o seguinte abaixo `[dependencies]`:

     ```toml
     [dependencies]
     asposepdf = { path = "{path}/asposepdf" }
     ```

4. **Compile seu projeto** (`cargo build`). Na primeira compilação, a biblioteca dinâmica apropriada para sua plataforma será extraída automaticamente de `.bz2` arquivo em `lib` pasta e vinculada ao seu projeto.

**Notas**

- O script de compilação tenta criar um **link simbólico** para a biblioteca no seu diretório de saída (por exemplo, `target/debug/`).
- Para **Linux e macOS**, você também deve seguir o [Configuração de Tempo de Execução](#runtime-configuration) seção abaixo para garantir que o executável possa encontrar a biblioteca em tempo de execução.
- Tudo `.bz2` arquivos têm correspondentes `.sha256` arquivos de checksum. Se um checksum estiver ausente ou inválido, a compilação falhará.

### Instalação a partir do GitHub

Este pacote inclui bibliotecas nativas pré-compiladas (`.dll`, `.so`, `.dylib`) que são armazenados como comprimidos `.bz2` arquivos dentro do repositório do GitHub.

1. **Adicionar** a biblioteca como dependência no seu projeto Rust. Você pode fazer isso de duas maneiras:

   - **Usando a linha de comando:**

     ```bash
     cargo add asposepdf --git https://github.com/aspose-pdf/aspose-pdf-rust-cpp.git
     ```

   - **Edição manual `Cargo.toml`:**

     Abra o projeto `Cargo.toml` e adicione o seguinte abaixo `[dependencies]`:

     ```toml
     [dependencies]
     asposepdf = { git = "https://github.com/aspose-pdf/aspose-pdf-rust-cpp.git" }
     ```

    > **Nota:** Para usar uma versão de lançamento específica, você pode especificar uma tag:
    >
    > ```toml
    > asposepdf = { git = "https://github.com/aspose-pdf/aspose-pdf-rust-cpp.git", tag = "v1.26.1" }
    > ```

2. **Compile seu projeto** (`cargo build`). Na primeira compilação, a biblioteca dinâmica apropriada para sua plataforma será extraída automaticamente de `.bz2` arquivo em `lib` pasta e vinculada ao seu projeto.

**Notas**

- Você não precisa baixar ou extrair manualmente nenhum arquivo - tudo está incluído no repositório do GitHub.
- O script de compilação tenta criar um **link simbólico** para a biblioteca no seu diretório de saída (por exemplo, `target/debug/`).
- Para **Linux e macOS**, você também deve seguir o [Configuração de Tempo de Execução](#runtime-configuration) seção abaixo para garantir que o executável possa encontrar a biblioteca em tempo de execução.
- Tudo `.bz2` os arquivos têm correspondência `.sha256` arquivos de checksum. O checksum é verificado antes da descompactação.
- Se a verificação de checksum falhar ou o arquivo estiver ausente, a compilação falhará com um erro detalhado.

### Instalação a partir do crates.io

Este pacote está disponível em [crates.io](https://crates.io/crates/asposepdf). 
Devido a limitações de tamanho, a crate publicada não inclui as bibliotecas binárias nativas (`.dll`, `.so`, ou `.dylib`).
Você pode obter as bibliotecas nativas necessárias tanto do arquivo de distribuição oficial (veja [Instalação a partir do site da Aspose](#installation-from-aspose-website)) ou do repositório GitHub (veja [Instalação a partir do GitHub](#installation-from-github)).
O script de compilação localizará, verificará e extrairá a biblioteca nativa apropriada de um arquivo compactado .bz2 durante o processo de compilação.

1. **Adicionar** a biblioteca como dependência no seu projeto Rust. Você pode fazer isso de duas maneiras:

   - **Usando a linha de comando:**

     ```bash
     cargo add asposepdf
     ```

   - **Edição manual `Cargo.toml`:**

     Abra o projeto `Cargo.toml` e adicione o seguinte abaixo `[dependencies]`:

     ```toml
     [dependencies]
     asposepdf = "1.26.1"
     ```

2. **Defina o caminho** para o diretório que contém as bibliotecas nativas e faça o download dos arquivos necessários:

   - **Definir a variável de ambiente** `ASPOSE_PDF_LIB_DIR`** para apontar para a pasta onde você colocará o nativo `.bz2` arquivos, seus `.sha256` arquivos de checksum, e as bibliotecas nativas extraídas (`.dll`, `.so`, `.dylib`, e para Windows também `.lib`):

     - No Linux/macOS:

       ```bash
       export ASPOSE_PDF_LIB_DIR=/path/to/lib
       ```

     - No Windows (Prompt de Comando):

       ```cmd
       set ASPOSE_PDF_LIB_DIR=C:\path\to\lib
       ```

     - No Windows (PowerShell):
     
       ```powershell
       $env:ASPOSE_PDF_LIB_DIR = "C:\path\to\lib"
       ```

**Nota sobre ASPOSE_PDF_LIB_DIR**

O `ASPOSE_PDF_LIB_DIR` variável de ambiente define o diretório de trabalho para o script de construção. Ela é usada **apenas durante a compilação** para localizar, verificar e extrair os arquivos de biblioteca nativa. Definir esta variável **não** adiciona automaticamente o diretório ao caminho de pesquisa de bibliotecas em tempo de execução do seu sistema (veja [Configuração de Tempo de Execução](#runtime-configuration)).

  - **Baixe o necessário `.bz2` arquivos** e arquivos de soma de verificação do repositório GitHub [`lib/` pasta](https://github.com/aspose-pdf/aspose-pdf-rust-cpp/tree/main/lib) e **coloque-os** na pasta definida em `ASPOSE_PDF_LIB_DIR`:

  - Para **Linux x64**, baixe:
    - `libAsposePDFforRust_linux_amd64.so.bz2`
    - `libAsposePDFforRust_linux_amd64.so.bz2.sha256`

  - Para **macOS x86_64**, download:
    - `libAsposePDFforRust_darwin_amd64.dylib.bz2`
    - `libAsposePDFforRust_darwin_amd64.dylib.bz2.sha256`

  - Para **macOS arm64**, baixar:
    - `libAsposePDFforRust_darwin_arm64.dylib.bz2`
    - `libAsposePDFforRust_darwin_arm64.dylib.bz2.sha256`

  - Para **Windows x64**, faça o download:
    - `AsposePDFforRust_windows_amd64.dll.bz2`
    - `AsposePDFforRust_windows_amd64.dll.bz2.sha256`
    - `AsposePDFforRust_windows_amd64.lib` (biblioteca de importação nativa, não compactada)

**Nota:** Você precisa baixar manualmente esses arquivos do GitHub e colocá-los no diretório apontado por `ASPOSE_PDF_LIB_DIR`.  
O script de compilação desempacotará automaticamente as bibliotecas nativas do `.bz2` arquivos na primeira compilação.

3. **Construa** seu projeto (`cargo build`). No primeiro build, a biblioteca nativa que corresponde à sua plataforma será extraída automaticamente da `.bz2` arquivar e vincular ao seu projeto.

**Importante:** Para **Linux e macOS**, você também deve seguir o [Configuração de Tempo de Execução](#runtime-configuration) seção abaixo para garantir que o executável possa encontrar a biblioteca em tempo de execução.

**Notas**

- O `ASPOSE_PDF_LIB_DIR` variável é usada **apenas durante o processo de compilação** para localizar e extrair os arquivos.
- O script de compilação tenta criar um **link simbólico** para a biblioteca extraída em seu diretório de saída (por exemplo, `target/debug/`).
- Você deve fornecer a pasta que contém o `.bz2` e `.sha256` arquivos separadamente, pois esses arquivos binários não são distribuídos via crates.io.
- Se o arquivo necessário estiver ausente ou a soma de verificação falhar, a compilação falhará com um erro detalhado.
- Os mesmos arquivos binários usados para instalação via GitHub ou o site da Aspose podem ser reutilizados aqui.

## Início rápido

Todos os trechos de código estão contidos no [trecho](https://onedrive.live.com/examples).