---
title: Requisitos do Sistema
linktitle: Requisitos do Sistema
type: docs
weight: 30
url: /python-net/system-requirements/
description: Esta seção lista os sistemas operacionais suportados que um desenvolvedor precisa para trabalhar com sucesso com Aspose.PDF para Python.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Visão Geral

Aspose.PDF para Python via .NET, API de Processamento de PDF que permite aos desenvolvedores trabalhar com documentos PDF sem precisar do Microsoft Office® ou Adobe Acrobat Automation. Aspose.PDF para Python pode ser usado para desenvolver aplicativos Python de 32 bits e 64 bits para diferentes sistemas operacionais (como Windows e Linux) onde o Python 3.5 ou posterior está instalado.

## Sistema Operacional Suportado

### Windows

- Windows 2003 Server
- Windows 2008 Server
- Windows 2012 Server
- Windows 2012 R2 Server
- Windows 2016 Server
- Windows 2019 Server
- Windows XP
- Windows Vista
- Windows 7
- Windows 8, 8.1
- Windows 10
- Windows 11

### Linux

- Ubuntu
- OpenSUSE
- CentOS
- e outros

## Requisitos do Sistema para o Linux Alvo

- Bibliotecas de tempo de execução GCC-6 (ou posterior).

- Dependências do .NET Core Runtime. A instalação do .NET Core Runtime em si NÃO é necessária.

- Para Python 3.5-3.7: É necessária a compilação pymalloc do Python. A opção de compilação do Python --with-pymalloc é habilitada por padrão. Normalmente, a compilação pymalloc do Python é marcada com o sufixo m no nome do arquivo.

- Biblioteca compartilhada libpython do Python.
 A opção de compilação --enable-shared do Python está desabilitada por padrão, algumas distribuições do Python não contêm a biblioteca compartilhada libpython. Para algumas plataformas Linux, a biblioteca compartilhada libpython pode ser instalada usando o gerenciador de pacotes, por exemplo: sudo apt-get install libpython3.7. O problema comum é que a biblioteca libpython é instalada em um local diferente do local padrão do sistema para bibliotecas compartilhadas. O problema pode ser resolvido usando as opções de compilação do Python para definir caminhos alternativos de bibliotecas ao compilar o Python, ou resolvido criando um link simbólico para o arquivo da biblioteca libpython no local padrão do sistema para bibliotecas compartilhadas. Tipicamente, o nome do arquivo da biblioteca compartilhada libpython é libpythonX.Ym.so.1.0 para Python 3.5-3.7, ou libpythonX.Y.so.1.0 para Python 3.8 ou posterior (por exemplo: libpython3.7m.so.1.0, libpython3.9.so.1.0).