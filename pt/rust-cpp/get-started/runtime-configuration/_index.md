---
title: Configuração de Tempo de Execução Aspose.PDF for Rust via C++
linktitle: Configuração de Tempo de Execução
type: docs
weight: 100
url: /pt/rust-cpp/runtime-configuration/
description: Aplicações Rust que dependem de bibliotecas dinâmicas nativas—como o Aspose.PDF—requerem configuração correta do caminho de tempo de execução para funcionar corretamente em sistemas Linux e macOS
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Configurando RPATH para Aspose.PDF Nativo para Rust
Abstract: Ao trabalhar com bibliotecas dinâmicas nativas em Rust, a vinculação correta em tempo de execução é essencial para garantir que sua aplicação possa localizar as dependências necessárias. No Linux e macOS, o carregador dinâmico do sistema não procura automaticamente o diretório do executável a menos que o RPATH seja configurado explicitamente. Este artigo explica como configurar o RPATH para que sua aplicação Rust possa localizar corretamente a biblioteca nativa Aspose.PDF em tempo de execução. Ele cobre a configuração ao nível do projeto usando Cargo, a configuração baseada em ambiente com RUSTFLAGS e as opções de instalação em todo o sistema, juntamente com observações sobre o comportamento no Windows.
SoftwareApplication: rust-cpp
---

> Esta é uma exigência padrão ao usar bibliotecas dinâmicas nativas em Rust.

No Linux e macOS, o carregador dinâmico do sistema não procura automaticamente o diretório do executável a menos que o RPATH esteja configurado. Para garantir que sua aplicação encontre a biblioteca nativa do Aspose.PDF em tempo de execução, você precisa configurar o **RPATH** (caminho de pesquisa em tempo de execução).

Nosso script de compilação extrai a biblioteca e tenta criar um link simbólico para ela no seu diretório de saída (por exemplo, `target/debug/`). Para que o executável o encontre, escolha uma das seguintes opções:

## Opção 1: Configuração ao nível do projeto (Recomendado)

Crie uma pasta chamada `.cargo` no diretório raiz do seu projeto (se não existir) e crie um arquivo chamado `config.toml` dentro dele:

```toml
[target.'cfg(target_os = "linux")']
rustflags = ["-C", "link-arg=-Wl,-rpath,$ORIGIN"]

[target.'cfg(target_os = "macos")']
rustflags = ["-C", "link-arg=-Wl,-rpath,@loader_path"]
```

## Opção 2: variável de ambiente RUSTFLAGS

Compile seu projeto com a seguinte flag:

```bash
# Linux
RUSTFLAGS="-C link-arg=-Wl,-rpath,\$ORIGIN" cargo build

# macOS
RUSTFLAGS="-C link-arg=-Wl,-rpath,@loader_path" cargo build
```

## Opção 3: Instalação em todo o sistema (Não recomendada para desenvolvimento)

Se preferir instalar a biblioteca globalmente:

* **Linux:** Copie o `.so` arquivo para `/usr/local/lib` e execute `sudo ldconfig`.
* **macOS:** Copie o `.dylib` arquivo para `/usr/local/lib`.

> **Windows**
> Nenhuma ação costuma ser necessária porque a biblioteca está localizada na mesma pasta que a `.exe`. Alternativamente, você pode adicionar o diretório que contém o `.dll` para o seu sistema `PATH` variável de ambiente.