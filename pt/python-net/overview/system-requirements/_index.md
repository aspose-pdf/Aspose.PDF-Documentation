---
title: Requisitos do Sistema
linktitle: Requisitos do Sistema
type: docs
weight: 30
url: /pt/python-net/system-requirements/
description: Esta seção lista os sistemas operacionais suportados que um desenvolvedor precisa para trabalhar com sucesso com o Aspose.PDF para Python.
lastmod: "2025-02-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Sistemas Operacionais Suportados do Aspose.PDF para Python via .NET
Abstract: Aspose.PDF para Python via .NET é uma API de processamento de PDF projetada para desenvolvedores gerenciarem documentos PDF sem a necessidade do Microsoft Office ou da Automação do Adobe Acrobat. Ela oferece suporte ao desenvolvimento de aplicações Python de 32 bits e 64 bits em diversos sistemas operacionais, incluindo Windows e Linux, onde o Python 3.5 ou superior está instalado. A API é compatível com várias versões do Windows, desde o Windows XP até o Windows 11, e com as principais distribuições Linux, como Ubuntu, OpenSUSE e CentOS. Para sistemas Linux, os requisitos específicos incluem as bibliotecas de tempo de execução GCC-6, dependências do .NET Core Runtime (sem necessidade de instalar o runtime em si) e a compilação pymalloc do Python para as versões 3.5‑3.7. Além disso, é necessária uma biblioteca libpython compartilhada, que pode exigir ajustes de configuração para o reconhecimento correto do caminho da biblioteca.
---

## Visão geral

Aspose.PDF para Python via .NET, API de Processamento de PDF que permite aos desenvolvedores trabalhar com documentos PDF sem precisar do Microsoft Office® ou da Automação do Adobe Acrobat. O Aspose.PDF para Python pode ser usado para desenvolver aplicações Python de 32 bits e 64 bits para diferentes sistemas operacionais (como Windows e Linux) onde o Python 3.5 ou posterior está instalado.

## Sistemas Operacionais Suportados

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

## Requisitos do Sistema para Linux Alvo

- Bibliotecas de tempo de execução GCC-6 (ou superior).

- Dependências do .NET Core Runtime. Instalar o próprio .NET Core Runtime NÃO é necessário.

- Para Python 3.5-3.7: É necessária a compilação pymalloc do Python. A opção de compilação --with-pymalloc do Python está habilitada por padrão. Normalmente, a compilação pymalloc do Python é marcada com o sufixo m no nome do arquivo.

- Biblioteca libpython compartilhada do Python. A opção de compilação --enable-shared do Python está desativada por padrão; algumas distribuições Python não contêm a biblioteca compartilhada libpython. Em algumas plataformas Linux, a biblioteca compartilhada libpython pode ser instalada usando o gerenciador de pacotes, por exemplo: sudo apt-get install libpython3.7. O problema comum é que a biblioteca libpython é instalada em um local diferente do local padrão do sistema para bibliotecas compartilhadas. O problema pode ser resolvido usando as opções de compilação do Python para definir caminhos alternativos de biblioteca ao compilar o Python, ou criando um link simbólico para o arquivo da biblioteca libpython no local padrão do sistema para bibliotecas compartilhadas. Normalmente, o nome do arquivo da biblioteca compartilhada libpython é libpythonX.Ym.so.1.0 para Python 3.5-3.7, ou libpythonX.Y.so.1.0 para Python 3.8 ou superior (por exemplo: libpython3.7m.so.1.0, libpython3.9.so.1.0).



