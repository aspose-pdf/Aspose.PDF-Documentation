---
title: Encrypt and Decrypt PDF
linktitle: Encrypt and Decrypt PDF File
type: docs
weight: 30
url: pt/python-cpp/set-privileges-encrypt-and-decrypt-pdf-file/
description: Encrypt and Decrypt PDF File with Python via C++ application.
lastmod: "2024-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Criptografar Arquivo PDF usando Diferentes Tipos de Criptografia e Algoritmos

Uma maneira eficaz de proteger arquivos PDF é através da criptografia. Neste artigo, exploraremos como criptografar documentos PDF usando Python com a ajuda da biblioteca Aspose.PDF.

A criptografia de PDF envolve embaralhar o conteúdo de um documento PDF usando algoritmos criptográficos para impedir o acesso não autorizado. Arquivos PDF criptografados exigem uma senha para serem abertos e podem ter restrições em ações como impressão, cópia e edição.

- A **senha do usuário**, se definida, é o que você precisa fornecer para abrir um PDF. O Acrobat/Reader solicitará ao usuário que insira a senha do usuário. Se não for correta, o documento não será aberto.
- A **senha do proprietário**, se definida, controla permissões, como impressão, edição, extração, comentários, etc.
 Acrobat/Reader impedirá essas coisas com base nas configurações de permissão. O Acrobat exigirá esta senha se você quiser definir/alterar permissões.

O trecho de código a seguir mostra como criptografar arquivos PDF.

1. Criar o caminho do arquivo de entrada e saída
1. Carregar o documento PDF usando AsposePDFPythonWrappers
1. Definir as permissões para o documento criptografado
1. Definir o algoritmo de criptografia a ser usado
1. Criptografar o documento com as senhas de usuário e proprietário especificadas, permissões e algoritmo de criptografia usando o método 'document.encrypt'
1. Salvar o documento criptografado no arquivo de saída especificado com o método 'document.save'.

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # Definir o caminho do diretório para os arquivos de exemplo
    dataDir = os.path.join(os.getcwd(), "samples")

    # Definir o caminho do arquivo de entrada
    input_file = os.path.join(dataDir, "sample.pdf")

    # Definir o caminho do arquivo de saída
    output_file = os.path.join(dataDir, "results", "sample-enc.pdf")

    # Carregar o documento PDF usando AsposePDFPythonWrappers
    document = apw.Document(inputFile)

    # Definir as permissões para o documento criptografado
    permission = apCore.Permissions(apCore.Permissions.ExtractContent | apCore.ModifyContent)

    # Definir o algoritmo de criptografia a ser usado
    cryptoAlgorithm = apCore.CryptoAlgorithm.RC4x128

    # Criptografar o documento com as senhas de usuário e proprietário especificadas, permissões e algoritmo de criptografia
    document.encrypt("user", "owner", permission, cryptoAlgorithm)

    # Salvar o documento criptografado no arquivo de saída especificado
    document.save(output_file)
```

## Descriptografar Arquivo PDF usando Senha do Proprietário

1. Criar o caminho do arquivo de entrada e saída
1. Criar uma nova instância da classe Document do módulo AsposePDFPythonWrappers
1. Descriptografar o documento usando o método [document_decrypt](https://reference.aspose.com/pdf/python-cpp/core/document_decrypt/)
1. Salvar o documento descriptografado no caminho do arquivo de saída usando o método save() com a função [document_save](https://reference.aspose.com/pdf/python-cpp/core/document_save/).

```Python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # Definir o caminho do diretório para os arquivos de exemplo
    dataDir = os.path.join(os.getcwd(), "samples")

    # Definir o caminho do arquivo de entrada
    input_file = os.path.join(dataDir, "sample_enc.pdf")

    # Definir o caminho do arquivo de saída
    output_file = os.path.join(dataDir, "results", "sample-dec.pdf")

    # Criar uma nova instância da classe Document do módulo AsposePDFPythonWrappers
    document = apw.Document(input_file, "owner")

    # Descriptografar o documento usando o método decrypt()
    document.decrypt()

    # Salvar o documento descriptografado no caminho do arquivo de saída usando o método save()
    document.save(output_file)
```